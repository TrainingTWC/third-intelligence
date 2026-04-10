import hashlib
import json
import logging
import os
import re
import threading

import faiss
import httpx
import numpy as np
from fastembed import TextEmbedding

logger = logging.getLogger(__name__)

# Common English stopwords — excluded from keyword scoring to reduce false positives
STOPWORDS = frozenset({
    "a", "an", "the", "is", "it", "in", "on", "at", "to", "of", "for", "and",
    "or", "not", "but", "by", "with", "from", "as", "be", "was", "were", "been",
    "are", "am", "do", "does", "did", "will", "would", "could", "should", "may",
    "might", "shall", "can", "has", "have", "had", "if", "so", "no", "yes",
    "this", "that", "these", "those", "what", "which", "who", "whom", "how",
    "when", "where", "why", "all", "each", "every", "both", "few", "more",
    "most", "some", "any", "such", "than", "too", "very", "just", "about",
    "also", "into", "over", "after", "before", "between", "under", "again",
    "then", "here", "there", "up", "out", "its", "my", "your", "our", "their",
    "me", "we", "you", "he", "she", "they", "him", "her", "us", "them",
    "i", "tell", "know", "get", "got", "like", "want", "need", "please",
    "give", "make", "made", "let", "going", "go", "come", "take", "say",
    "said", "thing", "things", "much", "many", "through", "only",
})

CACHE_DIR = os.path.join(os.path.dirname(__file__), ".faiss_cache")
LEARNED_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "learned.json")


class RAGEngine:
    """Hybrid retrieval engine: FAISS cosine-similarity search + keyword scoring."""

    def __init__(self, data_path: str = "../data/data.json", model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self._lock = threading.Lock()
        self._model_name = model_name
        self._embedder = None  # Lazy-loaded on first use to save RAM at startup
        self._data_json = self._fetch_data(data_path)
        self.documents, self.doc_sources = self._parse_documents(self._data_json)
        self._seen_keys = {doc.strip().lower() for doc in self.documents}
        self.index = self._build_or_load_index()
        # Load previously learned knowledge (conversations + uploads)
        self._load_learned()
        logger.info("RAGEngine ready — %d documents indexed", len(self.documents))

    @property
    def embedder(self):
        """Lazy-load the ONNX embedding model on first use."""
        if self._embedder is None:
            self._embedder = TextEmbedding(model_name=self._model_name)
        return self._embedder

    # ── Data loading ──────────────────────────────────────────────

    def _fetch_data(self, file_path: str) -> str:
        """Fetch knowledge data from Convex (primary) or local JSON file (fallback).

        Returns the raw JSON string for hashing and parsing.
        """
        convex_url = os.getenv("CONVEX_URL", "").strip().rstrip("/")
        if convex_url:
            try:
                logger.info("Fetching knowledge base from Convex: %s", convex_url)
                resp = httpx.post(
                    f"{convex_url}/api/query",
                    json={"path": "knowledge:getAll", "args": {}, "format": "json"},
                    timeout=30,
                )
                resp.raise_for_status()
                payload = resp.json()
                if payload.get("status") == "success":
                    data_str = json.dumps(payload["value"], ensure_ascii=False)
                    logger.info("Loaded knowledge base from Convex (%d bytes)", len(data_str))
                    return data_str
                logger.warning("Convex query returned non-success: %s", payload)
            except Exception as e:
                logger.warning("Convex fetch failed, falling back to file: %s", e)

        logger.info("Loading knowledge base from %s", file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def _parse_documents(self, data_json: str) -> tuple[list[str], list[str]]:
        """Parse JSON knowledge base into searchable document strings.

        Returns (documents, sources) where sources[i] is the module title for documents[i].
        Supports both the legacy flat Q&A format and the new modular chunk format.
        Deduplicates identical documents.
        """
        data = json.loads(data_json)

        docs: list[str] = []
        sources: list[str] = []
        seen: set[str] = set()

        def _add(doc: str, source: str):
            key = doc.strip().lower()
            if key not in seen:
                seen.add(key)
                docs.append(doc)
                sources.append(source)

        # New modular format: { "modules": [ { "chunks": [...] } ] }
        if isinstance(data, dict) and "modules" in data:
            for module in data["modules"]:
                module_title = module.get("title", "General")
                for chunk in module.get("chunks", []):
                    chunk_title = chunk.get("title", module_title)
                    source_label = f"{module_title} → {chunk_title}"

                    # Extract Q&A pairs
                    for qa in chunk.get("qa_pairs", []):
                        if "instruction" in qa and "output" in qa:
                            _add(f"Q: {qa['instruction']}\nA: {qa['output']}", source_label)

                    # Build a document from the chunk's structured fields
                    parts = []
                    if chunk.get("title"):
                        parts.append(chunk["title"])
                    if module.get("description"):
                        parts.append(f"Topic: {module['description']}")
                    if chunk.get("intent"):
                        parts.append(f"Intent: {chunk['intent']}")
                    if chunk.get("content"):
                        parts.append(chunk["content"])
                    if chunk.get("tags"):
                        parts.append("Tags: " + ", ".join(chunk["tags"]))
                    if chunk.get("response_templates"):
                        parts.append("Response templates: " + " | ".join(chunk["response_templates"]))
                    if chunk.get("steps"):
                        parts.append("Steps: " + " → ".join(chunk["steps"]))
                    if chunk.get("failure_patterns"):
                        parts.append("Failure patterns: " + ", ".join(chunk["failure_patterns"]))
                    if chunk.get("coaching_actions"):
                        parts.append("Coaching: " + ", ".join(chunk["coaching_actions"]))
                    if chunk.get("metrics_impacted"):
                        parts.append("Metrics: " + ", ".join(chunk["metrics_impacted"]))
                    ex = chunk.get("examples", {})
                    if ex.get("good"):
                        parts.append("Good examples: " + ", ".join(ex["good"]))
                    if ex.get("bad"):
                        parts.append("Bad examples: " + ", ".join(ex["bad"]))
                    if parts:
                        _add(f"[{module_title}] " + "\n".join(parts), source_label)

        # Legacy flat format: [ { "instruction": ..., "output": ... } ]
        elif isinstance(data, list):
            for item in data:
                if "instruction" in item and "output" in item:
                    _add(f"Q: {item['instruction']}\nA: {item['output']}", "Knowledge Base")

        logger.info("Loaded %d unique documents", len(docs))
        return docs, sources

    # ── Index construction (with disk cache) ──────────────────────

    def _build_or_load_index(self) -> faiss.IndexFlatIP:
        """Load cached FAISS index from disk, or build + cache a new one."""
        os.makedirs(CACHE_DIR, exist_ok=True)
        data_hash = hashlib.md5(self._data_json.encode("utf-8")).hexdigest()
        index_path = os.path.join(CACHE_DIR, "index.faiss")
        hash_path = os.path.join(CACHE_DIR, "data.hash")
        embed_path = os.path.join(CACHE_DIR, "embeddings.npy")

        # Check if cache is valid
        if (os.path.exists(index_path) and os.path.exists(hash_path) and os.path.exists(embed_path)):
            with open(hash_path, "r") as f:
                cached_hash = f.read().strip()
            if cached_hash == data_hash:
                logger.info("Loading cached FAISS index")
                self.embeddings = np.load(embed_path)
                return faiss.read_index(index_path)

        logger.info("Building new FAISS index (cosine similarity)")
        embeddings = np.array(list(self.embedder.embed(self.documents)), dtype=np.float32)
        # Normalize for cosine similarity via inner product
        faiss.normalize_L2(embeddings)
        self.embeddings = embeddings

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)
        index.add(np.array(embeddings))

        # Cache to disk
        faiss.write_index(index, index_path)
        np.save(embed_path, embeddings)
        with open(hash_path, "w") as f:
            f.write(data_hash)
        logger.info("FAISS index cached to %s", CACHE_DIR)

        return index

    # ── Semantic retrieval ────────────────────────────────────────

    def _semantic_search(self, query: str, k: int) -> list[tuple[int, float]]:
        """Return (index, score) tuples of top-k semantically similar documents."""
        query_vec = np.array(list(self.embedder.embed([query])), dtype=np.float32)
        faiss.normalize_L2(query_vec)
        scores, indices = self.index.search(np.array(query_vec), k)
        return [(int(idx), float(score)) for idx, score in zip(indices[0], scores[0]) if idx >= 0]

    # ── Keyword retrieval ─────────────────────────────────────────

    def _keyword_search(self, query: str, k: int) -> list[tuple[int, float]]:
        """Score documents by how many query keywords appear in them.

        Returns (index, score) tuples of the top-k keyword-matched documents,
        excluding documents with zero matches. Filters stopwords, gives bonus
        for title/Q matches, dotted-acronym exact matches, and multi-word
        phrase matches.
        """
        q = query.lower()
        # Detect dotted acronyms BEFORE collapsing (e.g. "c.o.f.f.e.e.", "l.e.a.s.t.")
        dotted_acronyms = re.findall(r'(?:[a-z]\.){2,}[a-z]?\.?', q)
        # Collapse dotted acronyms: R.E.S.P.E.C.T. → respect, L.E.A.S.T. → least
        q_collapsed = re.sub(r'(?:[a-z]\.){2,}[a-z]?\.?', lambda m: m.group().replace('.', ''), q)
        # Tokenise into words, drop single-character tokens and stopwords
        all_words = [w for w in re.findall(r"\w+", q_collapsed) if len(w) > 1]
        keywords = {w for w in all_words if w not in STOPWORDS}
        if not keywords:
            # If only stopwords, fall back to all non-single-char words
            keywords = {w for w in all_words if len(w) > 1}
        if not keywords:
            return []

        # Build bigrams for phrase matching (e.g., "customer complaint" matches better)
        bigrams = []
        for i in range(len(all_words) - 1):
            if all_words[i] not in STOPWORDS or all_words[i+1] not in STOPWORDS:
                bigrams.append(f"{all_words[i]} {all_words[i+1]}")

        scores: list[tuple[int, float]] = []
        for idx, doc in enumerate(self.documents):
            doc_lower = doc.lower()
            hits = sum(1 for kw in keywords if kw in doc_lower)
            if hits > 0:
                # Bonus: if keyword appears in the first line (title/question), it's more relevant
                first_line = doc_lower.split('\n', 1)[0]
                title_hits = sum(2 for kw in keywords if kw in first_line)
                # Big bonus: if the original dotted acronym appears in the document
                acronym_bonus = sum(5 for acr in dotted_acronyms if acr in doc_lower)
                # Phrase bonus: consecutive-word matches are stronger signals
                phrase_bonus = sum(2 for bg in bigrams if bg in doc_lower)
                scores.append((idx, hits + title_hits + acronym_bonus + phrase_bonus))

        # Sort by hit count descending, take top-k
        scores.sort(key=lambda x: x[1], reverse=True)
        return [(idx, score) for idx, score in scores[:k]]

    # ── Hybrid merge ──────────────────────────────────────────────

    def _merge_results(self, keyword_results: list[tuple[int, float]],
                        semantic_results: list[tuple[int, float]], k: int) -> list[tuple[int, float]]:
        """Merge results using Reciprocal Rank Fusion (RRF).

        Combines keyword and semantic rankings into a single score.
        Returns (index, rrf_score) tuples sorted by combined score.
        """
        rrf_k = 60  # RRF constant — standard value
        scores: dict[int, float] = {}

        # Keyword ranking contribution
        for rank, (idx, _) in enumerate(keyword_results):
            scores[idx] = scores.get(idx, 0.0) + 1.0 / (rrf_k + rank + 1)

        # Semantic ranking contribution
        for rank, (idx, _) in enumerate(semantic_results):
            scores[idx] = scores.get(idx, 0.0) + 1.0 / (rrf_k + rank + 1)

        # Sort by combined RRF score descending
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:k]

    # ── Public API ────────────────────────────────────────────────

    def retrieve(self, query: str, k: int = 8) -> dict:
        """Run hybrid retrieval and return results with sources and confidence.

        Oversamples candidates (2x k) from both keyword and semantic search,
        merges via Reciprocal Rank Fusion, then filters by minimum relevance.

        Returns:
            {"context": str, "sources": list[str], "confidence": str}
        """
        oversample = k * 2  # fetch more candidates for better RRF merge
        keyword_results = self._keyword_search(query, oversample)
        semantic_results = self._semantic_search(query, oversample)

        # Build semantic score map for confidence calculation
        sem_score_map = {idx: score for idx, score in semantic_results}

        # RRF merge
        merged = self._merge_results(keyword_results, semantic_results, k)
        final_ids = [idx for idx, _ in merged]

        # Filter out documents with very low semantic relevance (below 0.15)
        # unless they had strong keyword hits (keeps exact-match results)
        kw_ids = {idx for idx, _ in keyword_results[:k]}
        filtered_ids = []
        for idx in final_ids:
            sem_score = sem_score_map.get(idx, 0.0)
            if sem_score >= 0.15 or idx in kw_ids:
                filtered_ids.append(idx)
        if not filtered_ids and final_ids:
            filtered_ids = final_ids[:3]  # fallback: keep top 3 even if low score

        # Build structured context with source labels per document
        context_parts = []
        seen_sources: set[str] = set()
        source_list: list[str] = []
        for i in filtered_ids:
            src = self.doc_sources[i]
            if src not in seen_sources:
                seen_sources.add(src)
                source_list.append(src)
            context_parts.append(f"[Source: {src}]\n{self.documents[i]}")

        # Confidence based on best cosine similarity score
        best_score = max((sem_score_map.get(i, 0.0) for i in filtered_ids), default=0.0)
        if best_score >= 0.45:
            confidence = "high"
        elif best_score >= 0.25:
            confidence = "medium"
        else:
            confidence = "low"

        logger.debug("Query: %s", query)
        logger.debug("Keyword (%d) | Semantic (%d) | RRF merged (%d) | After filter (%d)",
                     len(keyword_results), len(semantic_results), len(merged), len(filtered_ids))
        logger.debug("Best semantic score: %.3f → confidence: %s", best_score, confidence)
        for i, idx in enumerate(filtered_ids, 1):
            logger.debug("  [%d] (sem=%.3f) %s", i, sem_score_map.get(idx, 0.0), self.documents[idx][:120])

        return {
            "context": "\n\n".join(context_parts),
            "sources": source_list,
            "confidence": confidence,
        }

    # ── Learned knowledge persistence ─────────────────────────────

    def _read_learned(self) -> dict:
        if os.path.exists(LEARNED_PATH):
            with open(LEARNED_PATH, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except (json.JSONDecodeError, ValueError):
                    pass
        return {"conversations": [], "documents": []}

    def _write_learned(self, data: dict):
        os.makedirs(os.path.dirname(LEARNED_PATH), exist_ok=True)
        with open(LEARNED_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def _load_learned(self):
        """Load previously persisted learned knowledge into the live index."""
        data = self._read_learned()
        docs, sources = [], []
        for entry in data.get("conversations", []):
            doc = f"Q: {entry['question']}\nA: {entry['answer']}"
            key = doc.strip().lower()
            if key not in self._seen_keys:
                docs.append(doc)
                sources.append("Learned → Conversation")
        for entry in data.get("documents", []):
            src_label = f"Learned → {entry.get('filename', 'Upload')}"
            for chunk in entry.get("chunks", []):
                key = chunk.strip().lower()
                if key not in self._seen_keys:
                    docs.append(chunk)
                    sources.append(src_label)
        if docs:
            self._hot_add(docs, sources)
            logger.info("Loaded %d learned documents from %s", len(docs), LEARNED_PATH)

    def _hot_add(self, new_docs: list[str], new_sources: list[str]):
        """Add new documents to the live FAISS index without rebuild."""
        embeddings = np.array(list(self.embedder.embed(new_docs)), dtype=np.float32)
        faiss.normalize_L2(embeddings)
        with self._lock:
            self.index.add(np.array(embeddings))
            self.embeddings = np.vstack([self.embeddings, embeddings])
            self.documents.extend(new_docs)
            self.doc_sources.extend(new_sources)
            for d in new_docs:
                self._seen_keys.add(d.strip().lower())

    def learn_qa(self, question: str, answer: str) -> bool:
        """Learn a verified Q&A pair from a positively-rated conversation."""
        doc = f"Q: {question}\nA: {answer}"
        key = doc.strip().lower()
        if key in self._seen_keys:
            return False
        # Persist
        learned = self._read_learned()
        learned["conversations"].append({
            "question": question,
            "answer": answer,
            "timestamp": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        })
        self._write_learned(learned)
        # Hot-add to live index
        self._hot_add([doc], ["Learned → Conversation"])
        logger.info("Learned Q&A: %.80s…", question)
        return True

    def learn_document(self, filename: str, text: str) -> int:
        """Chunk and learn an uploaded document. Returns number of chunks added."""
        chunks = self._chunk_text(text, filename)
        if not chunks:
            return 0
        # Deduplicate against existing knowledge
        new_chunks = []
        for c in chunks:
            if c.strip().lower() not in self._seen_keys:
                new_chunks.append(c)
        if not new_chunks:
            return 0
        # Persist
        learned = self._read_learned()
        learned["documents"].append({
            "filename": filename,
            "chunks": new_chunks,
            "timestamp": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
        })
        self._write_learned(learned)
        # Hot-add to live index
        src = f"Learned → {filename}"
        self._hot_add(new_chunks, [src] * len(new_chunks))
        logger.info("Learned %d chunks from upload: %s", len(new_chunks), filename)
        return len(new_chunks)

    @staticmethod
    def _chunk_text(text: str, filename: str, max_chars: int = 800) -> list[str]:
        """Split text into overlapping paragraph-based chunks."""
        paragraphs = [p.strip() for p in re.split(r"\n{2,}", text) if p.strip()]
        if not paragraphs:
            return []
        chunks = []
        current = f"[{filename}]\n"
        for para in paragraphs:
            if len(current) + len(para) > max_chars and len(current) > len(filename) + 4:
                chunks.append(current.strip())
                current = f"[{filename}]\n"
            current += para + "\n\n"
        if current.strip() and len(current) > len(filename) + 4:
            chunks.append(current.strip())
        return chunks
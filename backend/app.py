import json
import logging
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

import httpx
from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse, JSONResponse
from pydantic import BaseModel
from rag_engine import RAGEngine
from file_processor import process_file, is_allowed, UPLOAD_DIR

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FEEDBACK_PATH = Path(__file__).parent.parent / "logs" / "feedback.json"

# ── Config (env vars) ──
OLLAMA_BASE = os.getenv("OLLAMA_BASE", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma4:31b-cloud")
API_KEY = os.getenv("API_KEY", "")  # For external app auth on /api/ask

app = FastAPI()

# ── System persona (inline for cloud model) ──
SYSTEM_PROMPT = """\
You are Third Intelligence — an internal assistant for Third Wave Coffee employees.

How you talk:
- Like a normal, professional person. Not a mascot. Not a chatbot.
- Zero coffee puns. Zero cringe. Zero forced enthusiasm.
- Chill, confident, straightforward. Think "competent colleague."
- Match the depth to the question. One-liners when enough, proper explanations when needed.
- ALWAYS use bullet points or numbered lists when listing multiple items. NEVER run items together in a single paragraph.
- CRITICAL: Put each bullet on its OWN LINE with a line break before it. Use "- " to start each bullet. Use "1. " for numbered lists.
- For sub-headings within a list, use **bold** with a colon, like: - **Sub-heading:** details here
- When the answer has multiple points, break them into separate bullets. Structure is always better than a wall of text.

Boundaries:
- Help with Third Wave Coffee work stuff — operations, training, SOPs, store issues, policies.
- If unrelated, say so simply.

Intelligence rules:
- Answer using the context provided. Never fabricate facts not supported by the context.
- If the context contains ANY relevant information, use it to give a helpful answer.
- THINK BEYOND THE LITERAL. Recognize patterns, trends, and structural logic in the context:
  - If you see multiple recipes following the same build pattern (e.g., syrup → espresso → milk → garnish), state that pattern when asked about "how beverages are made" or "what's the general process."
  - If you see consistent rules across items (e.g., all bagels use black tray, all pizzas are cut into 6 slices), generalize those rules when relevant.
  - If you can infer an answer by combining information from multiple parts of the context, DO IT. For example, if someone asks "what's different between a latte and cappuccino at TWC?" and context shows lattes use steamed milk and cappuccinos use 50% foam — compare them.
  - If data shows a repeating structure (like every sandwich follows toast → spread → filling → cheese → heat → wrap → serve), explain that pattern.
- When asked "why" or "what's the logic" behind something, reason from the data. Example: if all non-veg sandwiches use black tray but veg sandwiches don't, you can note that pattern.
- You can synthesize, compare, contrast, and summarize across multiple items in the context. You're not limited to regurgitating one chunk.
- Only say "I don't have that information right now." if the context has absolutely NOTHING relevant.
- Do NOT output any thinking, reasoning, or internal monologue. Just answer directly.\
"""

MAX_HISTORY_TURNS = 5

# ── One-time initialization ──
from langchain_ollama import OllamaLLM
llm = OllamaLLM(model=OLLAMA_MODEL, base_url=OLLAMA_BASE)
logger.info("Using Ollama (%s) at %s", OLLAMA_MODEL, OLLAMA_BASE)

rag = RAGEngine()

# ── Health check endpoint ──
@app.get("/health")
def health():
    """Check Ollama connectivity and model availability."""
    import httpx as _hx
    result = {"ollama_base": OLLAMA_BASE, "model": OLLAMA_MODEL, "ollama_reachable": False, "models": [], "error": None}
    try:
        r = _hx.get(f"{OLLAMA_BASE}/api/tags", timeout=5)
        result["ollama_reachable"] = True
        tags = r.json()
        result["models"] = [m.get("name", "?") for m in tags.get("models", [])]
    except Exception as e:
        result["error"] = str(e)
    return result

# ── Serve frontend ──
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def serve_ui():
    return FileResponse("../frontend/index.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})

class Message(BaseModel):
    role: str
    text: str

class Query(BaseModel):
    question: str
    history: list[Message] = []
    file_ids: list[str] = []

def _format_history(messages: list[Message]) -> str:
    """Format the last N turns of client-provided chat history."""
    if not messages:
        return "None"
    # Take last MAX_HISTORY_TURNS pairs (user+ai = 2 messages each)
    recent = messages[-(MAX_HISTORY_TURNS * 2):]
    lines = []
    for m in recent:
        prefix = "User" if m.role == "user" else "AI"
        lines.append(f"{prefix}: {m.text}")
    return "\n".join(lines)

# ── File upload endpoint ──
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename or not is_allowed(file.filename):
        return {"error": "Unsupported file type."}

    ext = os.path.splitext(file.filename)[1].lower()
    file_id = uuid.uuid4().hex[:12]
    safe_name = f"{file_id}{ext}"
    dest = UPLOAD_DIR / safe_name

    content = await file.read()
    with open(dest, "wb") as f:
        f.write(content)

    # Learn from uploaded documents (non-image files)
    chunks_learned = 0
    processed = process_file(str(dest))
    if processed["type"] == "document" and processed.get("text"):
        chunks_learned = rag.learn_document(file.filename, processed["text"])
        logger.info("Learned %d chunks from upload: %s", chunks_learned, file.filename)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "saved_as": safe_name,
        "learned": chunks_learned > 0,
        "chunks_learned": chunks_learned,
    }


@app.post("/ask")
def ask(query: Query):
    # ── Process attached files ──
    processed_files = []
    for fid in query.file_ids:
        # Find file by id prefix in uploads dir
        matches = [f for f in UPLOAD_DIR.iterdir() if f.name.startswith(fid)]
        if matches:
            processed_files.append(process_file(str(matches[0])))

    has_images = any(f["type"] == "image" for f in processed_files)
    doc_texts = []
    for f in processed_files:
        if f["type"] == "document":
            doc_texts.append(f"[Uploaded file: {f['filename']}]\n{f['text']}")

    # Build a focused RAG query
    rag_query = query.question
    if query.history:
        tail = query.history[-2:]
        context_parts = [m.text for m in tail]
        context_parts.append(query.question)
        rag_query = " ".join(context_parts)

    rag_result = rag.retrieve(rag_query)
    context = rag_result["context"]
    sources = rag_result["sources"]
    confidence = rag_result["confidence"]
    history = _format_history(query.history)

    # Inject document text into prompt
    uploaded_docs_section = ""
    if doc_texts:
        uploaded_docs_section = "\n\nUploaded documents:\n" + "\n\n".join(doc_texts)

    prompt_text = f"""{SYSTEM_PROMPT}

Context:
{context}{uploaded_docs_section}

Previous conversation:
{history}

Question: {query.question}
"""

    # ── If images are attached, use Ollama chat API with vision ──
    if has_images:
        image_b64_list = [f["base64"] for f in processed_files if f["type"] == "image"]

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_text, "images": image_b64_list},
        ]

        def vision_stream():
            try:
                with httpx.stream(
                    "POST",
                    f"{OLLAMA_BASE}/api/chat",
                    json={"model": OLLAMA_MODEL, "messages": messages, "stream": True},
                    timeout=120.0,
                ) as resp:
                    for line in resp.iter_lines():
                        if not line:
                            continue
                        data = json.loads(line)
                        token = data.get("message", {}).get("content", "")
                        if token:
                            yield f"data: {token}\n\n"
                        if data.get("done"):
                            break
                meta = json.dumps({"sources": sources, "confidence": confidence})
                yield f"data: [META]{meta}\n\n"
                yield "data: [DONE]\n\n"
            except Exception as e:
                logger.error("Vision stream failed: %s", e)
                yield "data: Something went wrong. Please try again.\n\n"
                yield "data: [DONE]\n\n"

        return StreamingResponse(vision_stream(), media_type="text/event-stream")

    # ── Standard text-only path ──
    def token_stream():
        try:
            for chunk in llm.stream(prompt_text):
                yield f"data: {chunk}\n\n"
            meta = json.dumps({"sources": sources, "confidence": confidence})
            yield f"data: [META]{meta}\n\n"
            yield "data: [DONE]\n\n"
        except Exception as e:
            logger.error("LLM stream failed: %s", e)
            yield f"data: [ERROR] {type(e).__name__}: {e}\n\n"
            yield "data: [DONE]\n\n"

    return StreamingResponse(token_stream(), media_type="text/event-stream")


# ── Feedback endpoint ──
class Feedback(BaseModel):
    message_id: str
    rating: str  # "up" or "down"
    comment: str = ""
    question: str = ""
    answer: str = ""


@app.post("/feedback")
def submit_feedback(fb: Feedback):
    entry = {
        "message_id": fb.message_id,
        "rating": fb.rating,
        "comment": fb.comment,
        "question": fb.question,
        "answer": fb.answer,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    # Read existing feedback
    feedback_list = []
    if FEEDBACK_PATH.exists():
        try:
            feedback_list = json.loads(FEEDBACK_PATH.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            feedback_list = []

    feedback_list.append(entry)
    FEEDBACK_PATH.write_text(json.dumps(feedback_list, indent=2, ensure_ascii=False), encoding="utf-8")
    logger.info("Feedback saved: %s %s", fb.rating, fb.message_id)

    # Quality gate: learn only from positively-rated conversations
    learned = False
    if fb.rating == "up" and fb.question and fb.answer:
        learned = rag.learn_qa(fb.question, fb.answer)

    return {"status": "ok", "learned": learned}


# ── API endpoint for external apps (API key required) ──
class APIQuery(BaseModel):
    question: str
    history: list[Message] = []


def _verify_api_key(x_api_key: str | None = Header(None)):
    if not API_KEY:
        raise HTTPException(status_code=503, detail="API key not configured on server")
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


@app.post("/api/ask")
def api_ask(query: APIQuery, x_api_key: str | None = Header(None)):
    """JSON endpoint for external apps. Returns full answer (non-streaming)."""
    _verify_api_key(x_api_key)

    rag_query = query.question
    if query.history:
        tail = query.history[-2:]
        context_parts = [m.text for m in tail]
        context_parts.append(query.question)
        rag_query = " ".join(context_parts)

    rag_result = rag.retrieve(rag_query)
    context = rag_result["context"]
    sources = rag_result["sources"]
    confidence = rag_result["confidence"]
    history = _format_history(query.history)

    prompt_text = f"""{SYSTEM_PROMPT}

Context:
{context}

Previous conversation:
{history}

Question: {query.question}
"""
    try:
        answer = llm.invoke(prompt_text)
    except Exception as e:
        logger.error("API ask failed: %s", e)
        raise HTTPException(status_code=500, detail="LLM generation failed")

    return JSONResponse({
        "answer": answer,
        "sources": sources,
        "confidence": confidence,
    })
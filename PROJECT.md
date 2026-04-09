# Third Intelligence — Project Documentation

## Overview

**Third Intelligence** is an internal AI assistant built for Third Wave Coffee employees. It answers questions about operations, training programs, SOPs, store processes, and company policies using an LLM powered by Ollama (gemma4:31b-cloud) with a RAG (Retrieval-Augmented Generation) pipeline for accurate, context-grounded responses.

The stack: **Ollama** (LLM via gemma4:31b-cloud) + **FastAPI** (backend API) + **FAISS** (cosine similarity vector search) + **Vanilla HTML/CSS/JS** (frontend).

---

## Project Structure

```
third-intelligence/
├── backend/
│   ├── app.py              # FastAPI server — API + static file serving + feedback
│   ├── rag_engine.py        # RAG pipeline — hybrid FAISS + keyword retrieval
│   ├── file_processor.py    # File processing (PDF, DOCX, images, text)
│   └── .faiss_cache/        # Cached FAISS index (auto-generated)
├── data/
│   └── data.json           # Knowledge base — 16 modules, ~400+ QA pairs
├── frontend/
│   ├── index.html          # Chat UI — single-page app
│   ├── logo.png            # Dark logo (used in light mode)
│   └── logo-white.png      # White logo (used in dark mode)
├── logs/
│   └── feedback.json       # User feedback store (thumbs up/down)
├── models/
│   └── Modelfile           # Legacy — not used, kept for reference
├── scripts/                 # Data enrichment scripts
├── requirements.txt        # Python dependencies
└── PROJECT.md              # This file
```

---

## File Details

### `backend/app.py`

**Purpose:** Main server. Handles API requests, file uploads, streaming responses, and serves the frontend.

**Key features:**
- Initializes Ollama model (`gemma4:31b-cloud`) via `langchain_ollama.OllamaLLM`
- RAG-powered responses with source attribution and confidence scoring
- SSE streaming for real-time token delivery
- File upload support (images, PDFs, DOCX, text)
- Vision support via Ollama chat API for image analysis
- Feedback collection endpoint

**API Endpoints:**

| Method | Path       | Body                                              | Response                  |
|--------|------------|---------------------------------------------------|---------------------------|
| GET    | /          | —                                                  | index.html                |
| POST   | /upload    | `multipart/form-data` with file                    | `{ file_id, filename }`   |
| POST   | /ask       | `{ question, history[], file_ids[] }`              | SSE stream (tokens + metadata) |
| POST   | /feedback  | `{ message_id, rating, comment, question, answer }`| `{ status: "ok" }`       |

**SSE stream format:**
- `data: <token>` — streamed text tokens
- `data: [META]{"sources":[], "confidence":"high|medium|low"}` — metadata after response
- `data: [DONE]` — end of stream

**Run command:**
```bash
cd backend
python -m uvicorn app:app --reload
```
Server starts at `http://127.0.0.1:8000`

---

### `backend/rag_engine.py`

**Purpose:** Hybrid retrieval engine combining FAISS cosine similarity search with keyword matching.

**How it works:**

1. **On startup:**
   - Loads `SentenceTransformer` model (`all-MiniLM-L6-v2`, 384-dim embeddings)
   - Reads modular knowledge base from `data/data.json` (16 modules, chunks with QA pairs)
   - Deduplicates documents automatically
   - Tracks source module for each document
   - Builds FAISS `IndexFlatIP` index with L2-normalized embeddings (cosine similarity)
   - Caches index to `.faiss_cache/` — rebuilds only when data.json changes (MD5 hash check)

2. **On query** (`retrieve(query, k=5)`):
   - Runs keyword search (token matching, scored by hit count)
   - Runs semantic search (FAISS cosine similarity)
   - Merges results with interleaved ranking (semantic first, then keyword)
   - Returns dict: `{ context, sources[], confidence }`

**Confidence levels:** high (≥0.45), medium (≥0.25), low (<0.25) based on best cosine similarity score

---

### `data/data.json`

**Purpose:** The knowledge base. Contains all information the AI can reference.

**Format:** Modular JSON with 16 modules, each containing chunks with QA pairs:
```json
{
  "modules": [
    {
      "id": "module_id",
      "title": "Module Title",
      "description": "...",
      "chunks": [
        {
          "title": "Chunk Title",
          "intent": "...",
          "content": "...",
          "qa_pairs": [
            { "instruction": "Question", "output": "Answer" }
          ]
        }
      ]
    }
  ]
}
```

**Topics covered:**
- WING's Program (talent pipeline, career progression, assessment)
- RESPECT Framework (values-based evaluation)
- Customer Experience Execution (greeting, engagement, suggestive selling, recovery)
- BLEND Framework (CX in-store execution)
- Coffee Knowledge (blends, brewing, beans)
- Store Operations (opening/closing, SOPs)
- CX Playbook (guest journey, feedback handling)
- Glossary (company-specific terms)

---

### `frontend/index.html`

**Purpose:** Complete chat interface. Single HTML file with embedded CSS and JS.

**Design:**
- Glassmorphism aesthetic (translucent surfaces, blur effects, noise texture)
- Dark & light mode with toggle (persisted to localStorage)
- Ambient floating orbs in the background

**Features:**
- Splash screen with logo flight animation
- Sidebar with chat history (localStorage), search filter, pin toggle
- Suggestion cards for quick starts
- Real-time SSE streaming with typing indicator
- File upload (drag-and-drop + button) for images, PDFs, DOCX, text
- Code block rendering with syntax labels and copy button
- Copy-to-clipboard on AI messages
- Thumbs up/down feedback buttons on AI messages
- Source attribution tags showing which knowledge module was used
- Confidence indicator (high/medium/low) on responses
- Mobile responsive with hamburger sidebar

---

### `models/Modelfile`

**Purpose:** Legacy file — no longer used by the application. The system prompt is now defined inline in `app.py`. Kept for reference.

---

### `requirements.txt`

```
fastapi
uvicorn
langchain-ollama
sentence-transformers
faiss-cpu
numpy
python-multipart
pdfplumber
python-docx
Pillow
httpx
```

---

## Architecture

```
┌──────────────────────────────────┐
│  Frontend (index.html)           │
│  • Chat UI + SSE streaming       │
│  • File upload + drag-drop       │
│  • Source tags + feedback buttons │
│  • localStorage chat history     │
└─────────────┬────────────────────┘
              │ POST /ask, /upload, /feedback
┌─────────────▼────────────────────┐
│  FastAPI (app.py)                │
│  • Prompt construction           │
│  • SSE token streaming           │
│  • File processing pipeline      │
│  • Feedback storage              │
├──────────────┬───────────────────┤
│  RAG Engine  │  Ollama LLM       │
│  (FAISS +    │  gemma4:31b-cloud │
│   keyword)   │                   │
└──────┬───────┴───────────────────┘
       │
┌──────▼───────┐
│  data.json   │
│  16 modules  │
│  ~400+ QAs   │
└──────────────┘
```

---

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Ensure Ollama is running with gemma4:31b-cloud
ollama list  # should show gemma4:31b-cloud

# 3. Start the server
cd backend
python -m uvicorn app:app --reload

# 4. Open in browser
# http://127.0.0.1:8000
```
- Context-aware: short replies for greetings, detailed for real questions
- No coffee puns, no forced enthusiasm, no themed language
- Honest about not knowing things — never fabricates answers
- Scoped to Third Wave Coffee operations — politely redirects off-topic questions
- No unnecessary bullet points, lists, or narration

**Build command:**
```bash
ollama create third-intelligence -f models/Modelfile
```

---

### `requirements.txt`

**Python dependencies:**

| Package | Purpose |
|---------|---------|
| `fastapi` | Web framework — API server |
| `uvicorn` | ASGI server — runs FastAPI |
| `langchain-ollama` | LangChain wrapper for Ollama LLM calls |
| `sentence-transformers` | Generates text embeddings for vector search |
| `faiss-cpu` | Facebook's vector similarity search library |
| `numpy` | Numerical operations (required by FAISS) |

**Install:**
```bash
pip install -r requirements.txt
```

---

### `logs/feedback.json`

**Purpose:** Placeholder for storing user feedback on AI responses.

**Current state:** Empty array (`[]`). Not currently connected to any endpoint.

---

## How It All Connects

```
User types question
        │
        ▼
  ┌─────────────┐     POST /ask      ┌──────────────┐
  │  Frontend    │ ──────────────────▶│   app.py     │
  │  index.html  │                    │   (FastAPI)  │
  └─────────────┘                    └──────┬───────┘
        ▲                                   │
        │                    ┌──────────────┴──────────────┐
        │                    │                             │
        │                    ▼                             ▼
        │          ┌──────────────────┐          ┌─────────────────┐
        │          │  rag_engine.py   │          │  Ollama LLM     │
        │          │  (FAISS search)  │          │  (llama3.2:1b)  │
        │          └────────┬─────────┘          └────────┬────────┘
        │                   │                             │
        │                   ▼                             │
        │          ┌──────────────────┐                   │
        │          │  data.json       │                   │
        │          │  (97 Q&A pairs)  │                   │
        │          └──────────────────┘                   │
        │                                                 │
        │            { "answer": "..." }                  │
        └─────────────────────────────────────────────────┘
```

1. User sends a question from the chat UI
2. `app.py` receives it at `/ask`
3. `rag_engine.py` encodes the question → searches FAISS → returns top 5 matching Q&A pairs
4. `app.py` builds a prompt with the retrieved context + question
5. The prompt is sent to the Ollama model (`third-intelligence`)
6. The model generates a response using its personality (Modelfile) + the provided context
7. The response is returned to the frontend and displayed

---

## Setup & Run

### Prerequisites
- **Python 3.10+**
- **Ollama** installed and running (`ollama serve`)

### Steps

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Create the custom Ollama model
ollama create third-intelligence -f models/Modelfile

# 3. Start the server
cd backend
python -m uvicorn app:app --reload

# 4. Open in browser
# http://127.0.0.1:8000
```

# Deploying Third Intelligence (Free)

## Architecture

- **Hosting**: Render.com (free tier — 512 MB RAM, auto-sleep after 15 min idle)
- **LLM**: gemma4:31b-cloud via Ollama (inference runs on Ollama's cloud servers — no local GPU/RAM needed)
- **RAG**: Runs on Render (SentenceTransformer + FAISS, ~200 MB RAM)
- **Ollama**: Installed as a thin client in the Docker container — just routes requests to Ollama's cloud

---

## Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "initial commit"
git remote add origin https://github.com/YOUR_USER/third-intelligence.git
git push -u origin main
```

---

## Step 2: Deploy on Render.com

1. Go to https://render.com and sign up (free, use GitHub login)
2. Click **New → Web Service**
3. Connect your GitHub repo (`third-intelligence`)
4. Render auto-detects the `Dockerfile`. Settings:
   - **Name**: `third-intelligence`
   - **Plan**: Free
   - **Region**: Pick closest to you
5. Add **Environment Variables**:
   | Key | Value |
   |---|---|
   | `OLLAMA_MODEL` | `gemma4:31b-cloud` |
   | `API_KEY` | *(any random string — this is for external app auth)* |
6. Click **Deploy**

Your app will be live at: `https://third-intelligence.onrender.com`

> **Note**: Free tier sleeps after 15 min of inactivity. First request after sleep takes ~30-60s to cold-start (Ollama daemon + model registration).

---

## Step 3: Use from Other Apps

Your other apps can call the AI via the `/api/ask` endpoint:

### Request

```
POST https://third-intelligence.onrender.com/api/ask
Content-Type: application/json
X-API-Key: YOUR_API_KEY

{
  "question": "How do I dial in espresso?",
  "history": []
}
```

### Response

```json
{
  "answer": "To dial in espresso at TWC, follow these steps: ...",
  "sources": ["espresso_dial_in :: basic_parameters"],
  "confidence": "high"
}
```

### Code Examples

**Python:**
```python
import requests

resp = requests.post(
    "https://third-intelligence.onrender.com/api/ask",
    json={"question": "What is the WING program?"},
    headers={"X-API-Key": "YOUR_API_KEY"},
)
data = resp.json()
print(data["answer"])
```

**JavaScript (fetch):**
```javascript
const resp = await fetch("https://third-intelligence.onrender.com/api/ask", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "X-API-Key": "YOUR_API_KEY",
  },
  body: JSON.stringify({ question: "What is the WING program?" }),
});
const data = await resp.json();
console.log(data.answer);
```

**cURL:**
```bash
curl -X POST https://third-intelligence.onrender.com/api/ask \
  -H "Content-Type: application/json" \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{"question": "What is the WING program?"}'
```

---

## Local Development (Still Works)

Nothing changed for local dev. Just run as before:

```bash
cd backend
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Ollama must be running locally with `gemma4:31b-cloud` pulled.

---

## Alternative Free Hosts

| Platform | Free Tier | Notes |
|---|---|---|
| **Render.com** | 512 MB, auto-sleep | Recommended. Easiest setup. |
| **HuggingFace Spaces** | 2 vCPU, 16 GB RAM | More RAM but slower cold starts. Use Docker SDK. |
| **Railway.app** | $5/month credit | No sleep, but limited credits. |
| **Google Cloud Run** | 2M requests/month free | More setup, needs GCP account. |

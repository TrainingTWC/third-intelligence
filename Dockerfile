FROM python:3.11-slim AS builder

WORKDIR /app

# Build dependencies for faiss-cpu
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ── Final slim image ──────────────────────────────────────────
FROM python:3.11-slim

WORKDIR /app

# Only runtime deps: curl + zstd for Ollama install
RUN apt-get update && apt-get install -y --no-install-recommends curl zstd && \
    curl -fsSL https://ollama.com/install.sh | sh && \
    apt-get purge -y curl zstd && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* /tmp/* /root/.cache

# Copy pre-built Python packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

EXPOSE 8000

COPY start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]

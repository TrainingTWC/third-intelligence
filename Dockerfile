FROM python:3.11-slim

WORKDIR /app

# Install system deps + Ollama client
RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl zstd && \
    curl -fsSL https://ollama.com/install.sh | sh && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 8000

# Start Ollama daemon + pull cloud model + start uvicorn
COPY start.sh .
RUN chmod +x start.sh
CMD ["./start.sh"]

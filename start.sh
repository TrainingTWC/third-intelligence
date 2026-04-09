#!/bin/bash
set -e

# Constrain Ollama memory — cloud models don't need local RAM
export OLLAMA_NUM_PARALLEL=1
export OLLAMA_MAX_LOADED_MODELS=0
export OLLAMA_KEEP_ALIVE=0

# Start Ollama daemon in background (needed for cloud model routing)
echo "Starting Ollama daemon..."
ollama serve &
OLLAMA_PID=$!

# Wait for Ollama to be ready
echo "Waiting for Ollama..."
for i in $(seq 1 30); do
    if curl -sf http://localhost:11434/api/tags > /dev/null 2>&1; then
        echo "Ollama ready"
        break
    fi
    sleep 1
done

# Pull the cloud model (lightweight — just registers it, inference runs remotely)
echo "Pulling ${OLLAMA_MODEL:-gemma4:31b-cloud}..."
ollama pull "${OLLAMA_MODEL:-gemma4:31b-cloud}" || echo "Pull failed — model may already exist or will be pulled on first use"

# Start the FastAPI server
echo "Starting Third Intelligence..."
cd /app/backend
exec uvicorn app:app --host 0.0.0.0 --port "${PORT:-8000}"

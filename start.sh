#!/bin/bash
set -e

# Start the FastAPI server
echo "Starting Third Intelligence..."
cd /app/backend
exec uvicorn app:app --host 0.0.0.0 --port "${PORT:-8000}"

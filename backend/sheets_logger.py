"""
Background Google Sheets logger via Apps Script webhook.

Sends logs to a Google Sheet without blocking API responses.
Falls back silently if the webhook URL is not configured or the request fails.
"""

import json
import logging
import os
import threading
from datetime import datetime, timezone
from queue import Queue, Empty

import httpx

logger = logging.getLogger(__name__)

SHEETS_WEBHOOK_URL = os.getenv("GOOGLE_SHEETS_WEBHOOK", "")

# Background queue — holds (sheet_name, headers, row) tuples
_queue: Queue = Queue(maxsize=500)
_worker_started = False


def _worker():
    """Drain the queue and POST rows to the Apps Script webhook."""
    while True:
        try:
            sheet_name, headers, row = _queue.get(timeout=5)
        except Empty:
            continue
        if not SHEETS_WEBHOOK_URL:
            _queue.task_done()
            continue
        try:
            payload = {"sheet": sheet_name, "headers": headers, "row": row}
            resp = httpx.post(
                SHEETS_WEBHOOK_URL,
                json=payload,
                timeout=15.0,
                follow_redirects=True,
            )
            if resp.status_code != 200:
                logger.warning("Sheets webhook returned %s: %s", resp.status_code, resp.text[:200])
        except Exception as e:
            logger.warning("Sheets webhook failed: %s", e)
        finally:
            _queue.task_done()


def _ensure_worker():
    global _worker_started
    if _worker_started:
        return
    t = threading.Thread(target=_worker, daemon=True)
    t.start()
    _worker_started = True


def _enqueue(sheet_name: str, headers: list[str], row: list):
    """Add a row to the background queue. Drops silently if queue is full."""
    if not SHEETS_WEBHOOK_URL:
        return
    _ensure_worker()
    try:
        _queue.put_nowait((sheet_name, headers, row))
    except Exception:
        pass  # Queue full — drop silently


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def _truncate(text: str, max_len: int = 2000) -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."


# ── Public API ──

def log_interaction(question: str, answer: str, mode: str, language: str,
                    confidence: str, sources: list[str]):
    """Log a Q&A interaction to the Interactions sheet."""
    _enqueue(
        "Interactions",
        ["Timestamp", "Question", "Answer", "Mode", "Language", "Confidence", "Sources"],
        [_now(), _truncate(question, 500), _truncate(answer), mode, language,
         confidence, ", ".join(sources) if sources else ""],
    )


def log_feedback(question: str, answer: str, rating: str, comment: str):
    """Log feedback to the Feedback sheet."""
    _enqueue(
        "Feedback",
        ["Timestamp", "Question", "Answer", "Rating", "Comment"],
        [_now(), _truncate(question, 500), _truncate(answer), rating, _truncate(comment, 500)],
    )


def log_knowledge_gap(question: str):
    """Log a knowledge gap to the Knowledge Gaps sheet."""
    _enqueue(
        "Knowledge Gaps",
        ["Timestamp", "Question"],
        [_now(), _truncate(question, 500)],
    )

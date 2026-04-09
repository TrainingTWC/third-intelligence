"""
File processing utilities for Third Intelligence.
Handles images, PDFs, DOCX, TXT, and CSV files.
"""

import base64
import csv
import io
import os
from pathlib import Path

import pdfplumber
from docx import Document
from PIL import Image

# Max text characters to inject into the prompt from a document
MAX_TEXT_CHARS = 12000

UPLOAD_DIR = Path(__file__).parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    "image": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"},
    "pdf": {".pdf"},
    "docx": {".docx"},
    "text": {".txt", ".csv", ".md", ".log", ".json"},
}

def get_file_type(filename: str) -> str | None:
    ext = Path(filename).suffix.lower()
    for ftype, exts in ALLOWED_EXTENSIONS.items():
        if ext in exts:
            return ftype
    return None


def is_allowed(filename: str) -> bool:
    return get_file_type(filename) is not None


def image_to_base64(filepath: str) -> str:
    with Image.open(filepath) as img:
        # Resize large images to save context
        max_dim = 1024
        if max(img.size) > max_dim:
            img.thumbnail((max_dim, max_dim), Image.LANCZOS)
        buf = io.BytesIO()
        fmt = "PNG" if img.mode == "RGBA" else "JPEG"
        img.save(buf, format=fmt)
        return base64.b64encode(buf.getvalue()).decode("utf-8")


def extract_pdf_text(filepath: str) -> str:
    pages = []
    with pdfplumber.open(filepath) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                pages.append(f"--- Page {i+1} ---\n{text}")
    full = "\n\n".join(pages)
    if len(full) > MAX_TEXT_CHARS:
        full = full[:MAX_TEXT_CHARS] + "\n\n[...document truncated...]"
    return full


def extract_docx_text(filepath: str) -> str:
    doc = Document(filepath)
    text = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    if len(text) > MAX_TEXT_CHARS:
        text = text[:MAX_TEXT_CHARS] + "\n\n[...document truncated...]"
    return text


def extract_text_file(filepath: str) -> str:
    ext = Path(filepath).suffix.lower()
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        if ext == ".csv":
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                rows.append(" | ".join(row))
                if i > 200:
                    rows.append("[...rows truncated...]")
                    break
            text = "\n".join(rows)
        else:
            text = f.read()
    if len(text) > MAX_TEXT_CHARS:
        text = text[:MAX_TEXT_CHARS] + "\n\n[...file truncated...]"
    return text


def process_file(filepath: str) -> dict:
    """
    Process a file and return its content in a structured dict.
    Returns:
      {"type": "image", "base64": "...", "filename": "..."}
      {"type": "document", "text": "...", "filename": "..."}
    """
    filename = os.path.basename(filepath)
    ftype = get_file_type(filename)

    if ftype == "image":
        return {
            "type": "image",
            "base64": image_to_base64(filepath),
            "filename": filename,
        }
    elif ftype == "pdf":
        return {
            "type": "document",
            "text": extract_pdf_text(filepath),
            "filename": filename,
        }
    elif ftype == "docx":
        return {
            "type": "document",
            "text": extract_docx_text(filepath),
            "filename": filename,
        }
    elif ftype == "text":
        return {
            "type": "document",
            "text": extract_text_file(filepath),
            "filename": filename,
        }
    else:
        return {"type": "unsupported", "filename": filename}

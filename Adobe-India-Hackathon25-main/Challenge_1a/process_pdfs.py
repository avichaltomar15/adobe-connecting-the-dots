import fitz  # PyMuPDF
import os
import json
from pathlib import Path
import re
from pdf2image import convert_from_path
import pytesseract
import tempfile

def is_header_line(text):
    text = text.strip()
    return (
        re.match(r'^\d+[\.\)]?\s+[A-Z]', text) or
        re.match(r'^[A-Z \-\:\.]{5,}$', text) or
        text.isupper() or
        len(text.split()) < 8
    )

def extract_outline_from_page_text(text, page_number):
    outline = []
    for line in text.splitlines():
        line = line.strip()
        if len(line) >= 3 and is_header_line(line):
            outline.append({
                "level": "1",
                "text": line,
                "page": page_number + 1
            })
    return outline

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []

    any_text_found = False

    # Try native text extraction first
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text = page.get_text().strip()
        if text:
            any_text_found = True
            outline.extend(extract_outline_from_page_text(text, page_number))

    # If no text found (likely scanned PDF), fall back to OCR
    if not any_text_found:
        print(f"Using OCR for scanned PDF: {pdf_path}")
        with tempfile.TemporaryDirectory() as temp_dir:
            images = convert_from_path(pdf_path, dpi=300, output_folder=temp_dir)
            for i, image in enumerate(images):
                ocr_text = pytesseract.image_to_string(image)
                outline.extend(extract_outline_from_page_text(ocr_text, i))

    return outline

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        title = pdf_file.stem
        print(f"Processing: {pdf_file.name}")
        outline = extract_outline_from_pdf(str(pdf_file))

        output = {
            "title": title,
            "outline": outline
        }

        with open(output_dir / f"{title}.json", "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    process_pdfs()


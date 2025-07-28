# Adobe India Hackathon 2025 – Connecting the Dots 🚀

Welcome to my submission for the Adobe India Hackathon 2025. This repository contains solutions for both **Round 1A (PDF Structure Extraction)** and **Round 1B (Persona-Based Multi-PDF Analysis)**.

---

## 📁 Repository Structure

```
Adobe-India-Hackathon25-main/
│
├── analyze_collection.py         # Main script for Challenge 1B
├── process_pdfs.py               # Main script for Challenge 1A
│
├── sample_dataset/               # Shared resources (if any)
│
├── Challenge_1a/                 # Round 1A Folder
│   ├── Dockerfile
│   ├── process_pdfs.py
│   ├── requirements.txt
│   ├── sample_dataset/
│   └── README.md
│
├── Challenge_1b/                 # Round 1B Folder
│   ├── Collection 1/
│   │   ├── PDFs/
│   │   ├── challenge1b_input.json
│   │   └── challenge1b_output.json
│   ├── Collection 2/
│   ├── Collection 3/
│   └── README.md
│
├── .gitignore
└── README.md (this file)
```

---

### ✅ Challenge 1A – PDF Structure Extraction (Dockerized)

#### 📌 Description  
This module extracts structured section-wise content (headings, subheadings, paragraphs) from both text-based and scanned PDFs using a combination of PyMuPDF and OCR (Tesseract). The extracted content is saved in a structured JSON format for downstream tasks.

#### ▶️ How to Run (Using Docker)

1. Navigate to the Challenge 1A directory:
   cd Challenge_1a

2. Build the Docker image:
   docker build -t adobe-challenge-1a .

3. Run the Docker container:
   docker run --rm -v "$(pwd)/sample_dataset:/app/sample_dataset" adobe-challenge-1a

   - --rm: Automatically removes the container after execution.
   - -v "$(pwd)/sample_dataset:/app/sample_dataset": Mounts the local sample_dataset folder into the container.
   - Output JSON files will be written to the same sample_dataset/ directory.

#### 📂 Output

For each PDF in the sample_dataset/ folder, a corresponding structured JSON file will be generated in the same directory. These JSON files contain section-wise extracted content including headings, subheadings, and associated text blocks.

---

## ✅ Challenge 1B – Persona-Based PDF Collection Analysis

### 📌 Description

Given a **persona and task**, this module processes multiple PDFs across three collections and extracts the most relevant sections, ranks them, and summarizes them.

### ▶️ How to Run

1. **Navigate to the main repo folder**:
```bash
cd Adobe-India-Hackathon25-main
```

2. **Install dependencies**:
```bash
pip install -r Challenge_1a/requirements.txt
pip install sentence-transformers transformers
```

3. **Run the script**:
```bash
python analyze_collection.py
```

This script will:
- Process each `Collection {1,2,3}` under `Challenge_1b/`
- Read from `challenge1b_input.json`
- Generate `challenge1b_output.json` with relevant sections and summaries

---


---
## 🛠 Tech Stack

- Python 3.8+
- PyMuPDF (fitz)
- pytesseract & OpenCV (for OCR)
- Transformers & SentenceTransformers (for relevance & embeddings)
- Docker support (Challenge 1A)
- 
---

## 🙏 Acknowledgement

Thanks to Adobe India for this incredible opportunity to explore real-world NLP and PDF extraction use cases!

---


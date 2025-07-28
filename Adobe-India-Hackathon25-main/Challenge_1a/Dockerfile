FROM --platform=linux/amd64 python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
 && rm -rf /var/lib/apt/lists/*

# Install Python packages directly
RUN pip install --no-cache-dir \
    pymupdf==1.23.7 \
    pytesseract==0.3.10 \
    pdf2image==1.16.3

# Set working directory and copy script
WORKDIR /app
COPY process_pdfs.py .

# Run the script
CMD ["python", "process_pdfs.py"]


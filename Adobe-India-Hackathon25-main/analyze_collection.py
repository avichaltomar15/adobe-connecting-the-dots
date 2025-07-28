import os
import json
import datetime
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text_sections = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text().strip()
        if text:
            text_sections.append((page_num + 1, text))  # 1-based page numbers
    doc.close()
    return text_sections

def is_relevant(text, keywords):
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords)

def process_collection(collection_path):
    input_json_path = os.path.join(collection_path, "challenge1b_input.json")
    output_json_path = os.path.join(collection_path, "challenge1b_output.json")
    pdf_folder = os.path.join(collection_path, "PDFs")

    with open(input_json_path, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    task = input_data["job_to_be_done"]["task"]
    input_documents = [doc["filename"] for doc in input_data["documents"]]

    keywords = task.lower().split()

    extracted_sections = []
    subsection_analysis = []

    rank_counter = 1

    for pdf_file in input_documents:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        if not os.path.exists(pdf_path):
            continue

        sections = extract_text_from_pdf(pdf_path)

        for page_num, section_text in sections:
            if is_relevant(section_text, keywords):
                section_title = f"{pdf_file.replace('.pdf','')}, Page {page_num}"
                extracted_sections.append({
                    "document": pdf_file,
                    "section_title": section_title,
                    "importance_rank": rank_counter,
                    "page_number": page_num
                })
                subsection_analysis.append({
                    "document": pdf_file,
                    "refined_text": section_text[:1000],  # limit long texts
                    "page_number": page_num
                })
                rank_counter += 1

    output_data = {
        "metadata": {
            "input_documents": input_documents,
            "persona": persona,
            "job_to_be_done": task,
            "processing_timestamp": str(datetime.datetime.now())
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=4)

    print(f"✅ Processed: {collection_path}")

def process_all_collections(base_path="Challenge_1b"):
    for i in range(1, 4):
        folder_name = f"Collection {i}"
        full_path = os.path.join(base_path, folder_name)
        if os.path.exists(full_path):
            process_collection(full_path)
        else:
            print(f"❌ Missing folder: {folder_name}")

if __name__ == "__main__":
    process_all_collections()


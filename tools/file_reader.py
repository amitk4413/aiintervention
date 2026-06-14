from pypdf import PdfReader
from docx import Document

def read_file(file_path: str) -> str:
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    elif file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join([p.extract_text() or "" for p in reader.pages])

    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        raise ValueError("Unsupported file format")
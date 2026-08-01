import pypdf
import docx
import re

class DataIngestion:
    @staticmethod
    def parse_file(file_path: str, filename: str) -> str:
        ext = filename.split(".")[-1].lower()
        text = ""
        if ext == "pdf":
            reader = pypdf.PdfReader(file_path)
            for page in reader.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"
        elif ext in ["doc", "docx"]:
            doc = docx.Document(file_path)
            text = "\n".join([p.text for p in doc.paragraphs if p.text])
        elif ext == "txt":
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        return DataIngestion.clean_text(text)

    @staticmethod
    def clean_text(text: str) -> str:
        text = re.sub(r'[\r\t\f\v]', ' ', text)
        text = re.sub(r' +', ' ', text)
        return text.strip()
from pathlib import Path
from pypdf import PdfReader


def parse_file(path: Path) -> str:
    if path.suffix == ".pdf":
        reader = PdfReader(str(path))
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text

    if path.suffix in [".txt", ".md", ".py", ".c", ".cpp", ".java"]:
        return path.read_text(errors="ignore")

    return ""
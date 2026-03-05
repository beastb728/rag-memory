from pathlib import Path
from .parser import parse_file


def chunk_text(text, size=300):
    words = text.split()
    for i in range(0, len(words), size):
        yield " ".join(words[i:i+size])


def ingest_directory(directory):
    files = list(Path(directory).rglob("*"))

    chunks = []

    for file in files:
        text = parse_file(file)

        if not text:
            continue

        for i, chunk in enumerate(chunk_text(text)):
            chunk_id = f"{file}_chunk_{i}"

            chunks.append({
                "id": chunk_id,
                "text": chunk,
                "source": str(file)
            })

    return chunks
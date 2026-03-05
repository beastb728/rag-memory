import typer
from rag_memory.ingest import ingest_directory
from rag_memory.embeddings import embed
from rag_memory.vector_store import add_chunks
from rag_memory.search import semantic_search

app = typer.Typer()


@app.command()
def ingest(folder: str):
    chunks = ingest_directory(folder)

    texts = [c["text"] for c in chunks]

    embeddings = embed(texts)

    add_chunks(chunks, embeddings)

    print("Indexed", len(chunks), "chunks")


@app.command()
def search(query: str):
    semantic_search(query)


if __name__ == "__main__":
    app()
import typer

from .ingest import ingest_directory
from .embeddings import embed
from .vector_store import add_chunks
from .search import semantic_search
from .timeline import show_timeline
from .ask import ask_question

app = typer.Typer()


@app.command()
def ingest(folder: str):
    """Index files from a directory."""
    chunks = ingest_directory(folder)

    texts = [c["text"] for c in chunks]

    embeddings = embed(texts)

    add_chunks(chunks, embeddings)

    print("Indexed", len(chunks), "chunks")


@app.command()
def search(query: str):
    """Semantic search over indexed files."""
    semantic_search(query)


@app.command()
def timeline():
    """Show timeline of indexed documents."""
    show_timeline()

@app.command()
def ask(question: str):
    ask_question(question)

if __name__ == "__main__":
    app()
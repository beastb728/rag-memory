import typer

from .ingest import ingest_directory
from .embeddings import embed
from .vector_store import add_chunks
from .search import semantic_search
from .timeline import show_timeline
from .ask import ask_question
from .watcher import watch_folder

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
def watch(folder: str):
    """Watch a folder and automatically index file changes."""
    watch_folder(folder)

@app.command()
def ask(question: str):
    ask_question(question)

@app.command()
def index(folder: str):
    """
    Initial indexing + start watching for changes
    """

    print("Starting initial indexing...\n")

    chunks = ingest_directory(folder)

    texts = [c["text"] for c in chunks]

    embeddings = embed(texts)

    add_chunks(chunks, embeddings)

    print(f"Initial indexing complete. Indexed {len(chunks)} chunks.\n")

    print("Starting file watcher...\n")

    watch_folder(folder)

if __name__ == "__main__":
    app()
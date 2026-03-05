import chromadb

# Persistent client (data will be stored in ./chroma_db)
client = chromadb.PersistentClient(path="./chroma_db")

# Create or load collection
collection = client.get_or_create_collection(name="rag-memory")


def add_chunks(chunks, embeddings):
    documents = [c["text"] for c in chunks]
    sources = [c["source"] for c in chunks]

    ids = [c["id"] for c in chunks]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas=[{"source": s} for s in sources]
    )


def search(query_embedding, k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    return results
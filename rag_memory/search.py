from .embeddings import embed
from .vector_store import search


def semantic_search(query):
    query_embedding = embed([query])[0]

    results = search(query_embedding)

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    for doc, meta in zip(docs, metas):
        print("\nSource:", meta["source"])
        print(doc[:300])
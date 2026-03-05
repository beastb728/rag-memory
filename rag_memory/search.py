from .embeddings import embed
from .vector_store import search


def semantic_search(query):
    query_embedding = embed([query])[0]

    results = search(query_embedding)

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    if not docs:
        print("No results found.")
        return

    for doc, meta, dist in zip(docs, metas, distances):
        score = 1 - dist

        print("\n-----------------------------")
        print("Source:", meta.get("source", "Unknown"))
        print("Created:", meta.get("created", "Unknown"))
        print("Modified:", meta.get("modified", "Unknown"))
        print("Score:", round(score, 3))

        print("\nSnippet:")
        print(doc[:300])
import ollama
from .embeddings import embed
from .vector_store import search


SIMILARITY_THRESHOLD = 0.6   # lower distance = more similar


def ask_question(question):

    # Convert question to embedding
    query_embedding = embed([question])[0]

    # Retrieve similar chunks
    results = search(query_embedding)

    docs = results["documents"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    context = ""

    for doc, meta, dist in zip(docs, metas, distances):

        # Filter weak matches
        if dist > SIMILARITY_THRESHOLD:
            continue

        context += f"\nSource: {meta['source']}\n{doc}\n"

    # If no useful context found
    if context.strip() == "":
        print("\nNo relevant information found in indexed files.")
        return

    prompt = f"""
You are an assistant answering questions using the user's local files.

Only use the provided context to answer.

Context:
{context}

Question:
{question}

Answer clearly and reference the file names when possible.
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nAnswer:\n")
    print(response["message"]["content"])
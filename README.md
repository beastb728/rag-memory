# 🧠 RAG-Memory

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![ChromaDB](https://img.shields.io/badge/Vector%20DB-ChromaDB-orange)](https://www.trychroma.com/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama/Mistral-white)](https://ollama.ai/)

**RAG-Memory** turns your local filesystem into a searchable, sentient brain. It continuously indexes your documents, notes, and code, allowing you to perform semantic searches and chat with your files—**100% locally**. 

No cloud, no subscription, no privacy leaks.

---

## 🔥 Key Features

- **⚡ Real-Time Semantic Sync**: Uses `watchdog` to monitor file changes. Save a file, and it’s indexed in seconds.
- **🔍 True Meaning Search**: Forget keywords. Find "that algorithm for sorting nodes" even if you never used the word "sorting."
- **🤖 Local Brain**: Powered by **Ollama + Mistral** and `all-MiniLM-L6-v2`. Your data never leaves your machine.
- **📅 Neural Timeline**: View your digital breadcrumbs chronologically. See exactly what you were working on and when.
- **🛠️ Swiss Army CLI**: A beautiful command-line interface built with `Typer`.

---

## 🏗️ Core Architecture

The system follows a high-performance pipeline to transform raw bytes into actionable intelligence:

`filesystem` → `parsing` → `chunking` → `embeddings` → `vector store` → `semantic retrieval` → `LLM reasoning`

---

## 🚀 Quick Start

### 1. Prerequisites
Ensure you have [Ollama](https://ollama.ai/) installed and the Mistral model pulled:
```bash
ollama pull mistral

# Clone the repository
git clone [https://github.com/beastb728/rag-memory.git](https://github.com/beastb728/rag-memory.git)
cd rag-memory

# Setup environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Usage
The "Set and Forget" Command:
Index your documents and start the live watcher in one go:
```bash
python -m rag_memory.cli index ~/Documents
```
Query Your Brain:
```bash
# Semantic search for snippets
python -m rag_memory.cli search "graph traversal algorithms"

# Ask a specific question
python -m rag_memory.cli ask "Where did I mention the O(n log n) complexity?"

# See your history
python -m rag_memory.cli timeline
```

---

## 🛠️ Tech Stack

| Component | Technology | Language |
|-----------|------------|----------|
| **Embeddings** | `sentence-transformers` (all-MiniLM-L6-v2) | Python |
| **Vector DB** | [ChromaDB](https://www.trychroma.com/) | Python |
| **Inference** | [Ollama](https://ollama.ai/) (Mistral) | Python |
| **CLI** | [Typer](https://typer.tiangolo.com/) | Python |
| **Watcher** | [Watchdog](https://github.com/gorakhargosh/watchdog) | Python |

---

## 🗺️ Roadmap

- [ ] **Web UI**: A sleek React-based dashboard for browsing memories.
- [ ] **Graph Mode**: Map relationships between documents (Knowledge Graph).
- [ ] **OCR Support**: Indexing text within images and PDFs.
- [ ] **Hybrid Search**: Combining BM25 keyword matching with Vector search.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.     
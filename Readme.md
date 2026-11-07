# Document-Grounded RAG

A lightweight Python prototype for building a document-grounded retrieval-augmented generation (RAG) workflow using LangChain, Hugging Face embeddings, ChromaDB, and Groq models.

This project demonstrates the core idea of RAG:

- load documents from a local folder
- split them into manageable chunks
- convert text into embeddings
- store embeddings in a vector database
- retrieve relevant context for grounded answers

## Features

- Supports `.txt`, `.pdf`, and `.docx` files
- Uses `sentence-transformers/all-MiniLM-L6-v2` for embeddings
- Uses `RecursiveCharacterTextSplitter` to chunk text
- Stores vectors in Chroma
- Uses a Groq-backed LLM for experimentation and chat-style prompts

## Project structure

```text
Document-Grounded_RAG/
├── app.py
├── requirements.txt
├── .env.example
├── LICENSE
├── Readme.md
├── checks.json
├── data/
│   └── documents/
│       ├── company_policy.txt
│       └── phase3.txt
├── src/
│   ├── embeddings.py
│   ├── loader.py
│   ├── splitter.py
│   └── vectorstore.py
├── vectorstore/
└── .gitignore
```

## How it works

1. `src/loader.py` loads files from the documents directory.
2. `src/splitter.py` splits each document into chunks.
3. `src/embeddings.py` creates an embedding model using Hugging Face.
4. `src/vectorstore.py` stores the chunked documents in a Chroma vector store.
5. `app.py` is a simple Groq example script for testing model access and prompting.

## Prerequisites

- Python 3.11+
- A Groq API key
- Internet access for installing packages and downloading the embedding model

## Setup

1. Clone the repository

```bash
git clone https://github.com/gopalgupta46300-ui/Document-Grounded_RAG.git
cd Document-Grounded_RAG
```

2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file in the project root

```env
GROQ_API_KEY=your_groq_api_key_here
```

4. Add your documents to `data/documents/`

Place files such as `.txt`, `.pdf`, or `.docx` inside the folder below:

```text
data/documents/
```

## Running the project

### Build the vector store

```bash
python src/vectorstore.py
```

This script loads documents, splits them into chunks, creates embeddings, and saves them to the `vectorstore/` directory using Chroma.

### Run the sample app

```bash
python app.py
```

The current `app.py` is a basic Groq smoke test and prints a sample response. It is useful for confirming that your API credentials and model access are working correctly.

## Important note for local use

The repository includes a sample document pipeline, but the loader currently uses a hardcoded Windows-style path in `src/loader.py`:

```python
DOCUMENTS_PATH = Path(r"E:\Ultimate_Folder\demo-RAG-system\data\documents")
```

For local execution, update this to a project-relative path similar to:

```python
from pathlib import Path

DOCUMENTS_PATH = Path(__file__).resolve().parent.parent / "data" / "documents"
```

This will ensure the app reads the documents from the repository itself instead of an external folder.

## Requirements summary

The project depends on:

- `langchain`
- `langchain-groq`
- `langchain-community`
- `langchain-text-splitters`
- `langchain-huggingface`
- `python-dotenv`
- `chromadb`
- `pypdf`
- `sentence-transformers`

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Current status

This is a beginner-friendly RAG starter project and a useful foundation for building more advanced document Q&A systems. The repository is intentionally simple and easy to extend with:

- prompt templates
- retriever logic
- chat interfaces
- document metadata filters
- Azure/OpenAI or other LLM backends
- UI integration with Streamlit or FastAPI

## Example next steps

- Add a retrieval layer for question answering
- Build a web UI for document chat
- Improve source tracking and citation support
- Add support for richer document metadata
- Replace the simple smoke-test app with a real RAG chat flow


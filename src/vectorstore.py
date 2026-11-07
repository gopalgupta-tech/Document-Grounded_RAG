from pathlib import Path

from langchain_chroma import Chroma

from embeddings import get_embedding_model
from loader import load_documents
from splitter import split_documents


VECTORSTORE_PATH = Path("vectorstore")
COLLECTION_NAME = "company_documents"


def create_vectorstore():
    documents = load_documents()

    if not documents:
        raise ValueError("No documents found in data/documents/")

    chunks = split_documents(documents)

    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")

    embeddings = get_embedding_model()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(VECTORSTORE_PATH),
    )

    vectorstore.add_documents(chunks)

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

    return vectorstore


if __name__ == "__main__":
    create_vectorstore()
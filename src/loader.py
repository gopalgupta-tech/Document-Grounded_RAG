from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
)


DOCUMENTS_PATH = Path(r"E:\Ultimate_Folder\demo-RAG-system\data\documents")


def load_documents():
    documents = []

    for file_path in DOCUMENTS_PATH.iterdir():

        if file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))

        elif file_path.suffix.lower() == ".txt":
            loader = TextLoader(
                str(file_path),
                encoding="utf-8"
            )

        elif file_path.suffix.lower() == ".docx":
            loader = Docx2txtLoader(str(file_path))

        else:
            print(f"Skipping unsupported file: {file_path.name}")
            continue

        loaded_documents = loader.load()
        documents.extend(loaded_documents)

    return documents

if __name__ == "__main__":
    documents = load_documents()

    print(f"Loaded {len(documents)} document(s)")

    for document in documents:
        print("\n--- DOCUMENT ---")
        print(document.page_content)
        print("Metadata:", document.metadata)
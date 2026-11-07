from langchain_text_splitters import RecursiveCharacterTextSplitter

from loader import load_documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    documents = load_documents()
    chunks = split_documents(documents)

    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")

    for i, chunk in enumerate(chunks[:5]):
        print(f"\n--- CHUNK {i + 1} ---")
        print(chunk.page_content)
        print("Metadata:", chunk.metadata)
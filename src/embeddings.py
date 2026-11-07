from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """Initializes and returns the HuggingFace embedding model."""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings


if __name__ == "__main__":
    # 1. Initialize the embedding model
    embeddings = get_embedding_model()

    # 2. Define sample text
    text = "Employees receive 20 paid leave days per year."

    # 3. Generate the vector embedding
    vector = embeddings.embed_query(text)

    # 4. Print results
    print(f"Vector dimensions: {len(vector)}")
    print(f"First 5 values: {vector[:5]}")

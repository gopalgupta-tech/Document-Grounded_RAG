# Project Structure

```text
company-private-chatbot/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── app.py
│
├── data/
│   └── documents/
│
├── vectorstore/
│
└── src/
    ├── __init__.py
    ├── loader.py
    ├── splitter.py
    ├── embeddings.py
    ├── vectorstore.py
    ├── retriever.py
    ├── prompt.py
    └── chatbot.py
```
## Embeddings.py file

### 📋 Key Optimization Points

* **Ultra-Lightweight Footprint**: Uses the `all-MiniLM-L6-v2` model which requires only **~90 MB of storage space**, making it instant to download and process.
* **Universal Laptop Compatibility**: Explicitly configures the execution environment to use standard **CPU** computing threads, ensuring smooth performance even on budget hardware without dedicated GPUs.
* **No Memory Spikes**: Limits OpenMP and Intel MKL processor threads to `1` to prevent sudden multi-core CPU background spikes, keeping your computer fully usable while generating embeddings.
* **Persistent Local Cache**: The framework only downloads the architecture files on your first initial execution; subsequent program launches load instantly from local memory.
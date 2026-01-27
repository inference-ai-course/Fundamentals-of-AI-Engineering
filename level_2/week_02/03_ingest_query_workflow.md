# Week 2 — Part 03: Minimal `ingest.py` + `query.py` workflow
 
## Overview
 
Your Week 2 deliverable is an end-to-end pipeline:
 
- `ingest.py` indexes documents into your vector DB
- `query.py` retrieves top-k chunks for a text query
 
The point of this deliverable is to have a **repeatable debugging loop**:
 
- ingest
- query
- inspect what came back
- adjust chunking/metadata
 
---
 
## Recommended CLI design (simple but real)
 
Make the scripts runnable like this:
 
```bash
python ingest.py --input_dir data --persist_dir chroma --collection kb
python query.py --persist_dir chroma --collection kb --query "what is RAG?" --top_k 5
```
 
This makes it easy to reproduce runs and compare results.
 
---
 
## Minimal `ingest.py` responsibilities
 
1. Find input files (txt/markdown/pdf depending on your project scope)
2. Load text
3. Chunk text
4. Compute embeddings
5. Upsert into vector DB with metadata
 
You can stub embeddings initially (for learning), then swap in a real embedding model.
 
---
 
## Minimal `query.py` responsibilities
 
1. Embed the query
2. Query vector DB for top-k
3. Print results in a human-debuggable format
4. (optional) Write a JSON file for later evaluation
 
## Minimal `query.py` contract
 
Inputs:
 
- `--query "..."`
- `--top_k 5`
 
Outputs:
 
- print hits with:
  - doc_id
  - chunk_id
  - score
  - text
 
Recommended output format:
 
- always print `rank`, `score`, `doc_id`, `chunk_id`, and a short text preview
- keep it stable so you can diff outputs across runs
 
---
 
## Sample `query.py` (Chroma-style example)
 
This is intentionally compact and shows the “shape” of the workflow.
 
```python
import argparse
 
import chromadb
 
 
def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--persist_dir", default="./chroma")
    parser.add_argument("--collection", default="kb")
    parser.add_argument("--query", required=True)
    parser.add_argument("--top_k", type=int, default=5)
    args = parser.parse_args()
 
    client = chromadb.PersistentClient(path=args.persist_dir)
    collection = client.get_or_create_collection(name=args.collection)
 
    # Replace this with a real embedding model.
    # For learning, you can precompute embeddings or use a placeholder.
    query_embedding = [0.1, 0.2, 0.3]
 
    res = collection.query(query_embeddings=[query_embedding], n_results=args.top_k)
    ids = res.get("ids", [[]])[0]
    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]
    dists = res.get("distances", [[]])[0]  # may vary by backend
 
    for i, chunk_id in enumerate(ids):
        meta = metas[i] if i < len(metas) else {}
        doc_id = meta.get("doc_id", "")
        score = dists[i] if i < len(dists) else None
        text = docs[i] if i < len(docs) else ""
        preview = (text[:200] + "...") if len(text) > 200 else text
        print(f"#{i+1} score={score} doc_id={doc_id} chunk_id={chunk_id}\n{preview}\n")
 
 
if __name__ == "__main__":
    main()
```
 
---
 
## Engineering requirements (make it reliable)
 
Add these behaviors early so you don’t suffer later:
 
- ingestion is idempotent (upsert by stable `chunk_id`)
- input parsing failures are explicit (file not found, empty file)
- you can rerun ingest/query and get consistent outputs
- you can log which embedding model + chunking config you used
 
---
 
## References
 
- Chroma docs: https://docs.trychroma.com/
- Python argparse: https://docs.python.org/3/library/argparse.html
- OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings

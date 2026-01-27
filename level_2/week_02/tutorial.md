# Level 2 — Week 2 Tutorials

## Overview

Week 2 builds ingestion to a vector store:

- parse documents
- chunk
- embed
- upsert into a vector DB

You’ll also define metadata so retrieval can be debugged later.

This week is the foundation for everything later:

- Week 3: retrieval becomes `/search`
- Week 4: chat uses retrieved chunks + citations
- Week 5: evaluation measures whether changes improved retrieval

A good Week 2 outcome is not “a lot of code”. It’s a system that is **repeatable**:

- you can rerun ingestion without duplicates
- you can run query and clearly see which chunks were retrieved and why
- you can iterate on chunking and immediately observe the effect

## Navigation

- [01 — Vector DB fundamentals + minimal metadata schema](01_vector_db_fundamentals.md)
- [02 — Chunking + idempotent ingestion](02_chunking_idempotent_ingestion.md)
- [03 — Minimal `ingest.py` and `query.py` workflow](03_ingest_query_workflow.md)

## Suggested mini project layout

Keep the structure boring and obvious:

- `data/` (your source docs)
- `ingest.py` (CLI to ingest)
- `query.py` (CLI to query)
- `chroma/` (or `vector_store/`) (local persisted vector DB files)
- `output/` (optional: saved query results/eval artifacts)

## Recommended order

1. Read 01 and decide your stored schema.
2. Read 02 and implement chunk ids / dedup.
3. Read 03 and run ingest + query end-to-end.

## What “done” looks like (acceptance checklist)

- You can ingest the same folder twice and the collection size does not double.
- A query prints the top-k results with `chunk_id`, `doc_id`, and a text preview.
- You can locate the original source for any retrieved chunk (via metadata like `url/section/page`).
- You can change one chunking setting (size/overlap) and observe different retrieval results.

## References

- Chroma docs: https://docs.trychroma.com/
- Sentence-Transformers: https://www.sbert.net/
- OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings

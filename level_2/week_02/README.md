# Level 2 — Week 2: RAG + Vector DB Foundations (Ingestion to Index)

## What you should be able to do by the end of this week

- Ingest documents into a vector store with a repeatable pipeline (parse -> chunk -> embed -> upsert).
- Design basic metadata that enables filtering and debugging.
- Run a minimal retrieval query against your indexed data.

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_vector_db_fundamentals.md](01_vector_db_fundamentals.md)
- [02_chunking_idempotent_ingestion.md](02_chunking_idempotent_ingestion.md)
- [03_ingest_query_workflow.md](03_ingest_query_workflow.md)

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) Vector DB fundamentals (what you store and why)

**Mental model**:

- You store embeddings plus metadata so you can retrieve the most relevant chunks.
- Metadata enables filtering (source, doc type, date) and debugging.
- Upsert/query/delete are the basic lifecycle operations.

**What students usually misunderstand**:

- A vector DB does not “understand documents”. It stores:
  - vectors (numbers)
  - ids
  - metadata
  - raw text (optional but common for debugging)
- Retrieval quality depends as much on:
  - chunking
  - metadata
  - query construction
  as on the database itself.

**Minimum schema to teach (start simple)**:

- `doc_id`: which document this came from
- `chunk_id`: which chunk inside the document
- `source`: filename/URL
- `text`: the actual chunk text

Citations:

- https://docs.trychroma.com/
- https://github.com/milvus-io/milvus-docs
- https://www.pinecone.io/learn/retrieval-augmented-generation/

### 2) Chunking and metadata schema (setup for retrieval)

**Mental model**:

- Chunking defines the retrieval unit (too small loses context; too big dilutes similarity).
- A minimal schema usually includes: doc_id, source, chunk_id, and text.
- Dedup can be as simple as hashing text chunks to avoid duplicates on repeated runs.

**Chunking strategies to introduce (in order)**:

- Fixed-size chunking:
  - simplest
  - good baseline
- Structure-aware chunking:
  - split on headings, bullet lists, code blocks
  - often improves citation quality

**Idempotency for ingestion**:

- Goal: running `ingest.py` twice should not double-index the same chunk.
- Simple patterns:
  - chunk hash as id
  - store a version field
  - delete-then-rebuild per document

Citations:

- https://www.pinecone.io/learn/retrieval-augmented-generation/
- https://12factor.net/

### 3) Embeddings choice (practical intuition)

**Mental model**:

- Embeddings map text to vectors where semantic similarity becomes distance in vector space.
- Start with one embedding model and only change after you have a baseline.

**Practical guidance**:

- Keep the embedding model fixed while you debug chunking and metadata.
- Record embedding settings in your index metadata:
  - model name
  - dimension
  - date/version

Citations:

- https://www.sbert.net/

## Common pitfalls

- Ingestion is not idempotent (re-running creates duplicates).
- No metadata, so you cannot debug why a chunk was retrieved.
- Chunking too aggressively without measuring retrieval quality.

## Workshop / Implementation Plan

- Implement `ingest.py` to load files, chunk, embed, and upsert.
- Store metadata: doc_id/source/chunk_id.
- Implement `query.py` to retrieve top-k chunks for a query.

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: System architecture overview


### Figure B: Data and control flow (ingestion -> retrieval -> generation -> evaluation)


## Self-check questions

- If you run ingestion twice, do you get duplicates?
- Can you filter retrieval to a subset using metadata?

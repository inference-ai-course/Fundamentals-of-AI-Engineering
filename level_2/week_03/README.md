# Level 2 — Week 3: Retrieval API + Debuggable Retrieval Metrics (RAG Without Generation Yet)

## What you should be able to do by the end of this week

- Expose retrieval via a debuggable `/search` API (filters + top-k).
- Build a small retrieval query set and compute simple retrieval metrics (hit rate / recall@k).
- Produce logs that let you inspect which chunks were retrieved and why.

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) Retrieval as an API (separate from chat)

**Mental model**:

- Treat retrieval as a first-class component with its own endpoint and logs.
- A `/search` API lets you debug retrieval independent of LLM behavior.

**Why this separation matters**:

- If chat answers are bad, you need to know whether the problem is:
  - retrieval returned the wrong chunks
  - retrieval returned good chunks but the prompt failed
  - retrieval returned nothing but the model answered anyway

**Minimum `/search` contract**:

- Request:
  - `query` (string)
  - `top_k` (int)
  - `filters` (optional object)
- Response:
  - list of hits with `doc_id`, `chunk_id`, `score`, `text`, and `metadata`

Citations:

- https://fastapi.tiangolo.com/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

### 2) Filtering + top-k and what can go wrong

**Mental model**:

- Filters reduce false positives by constraining search to the right subset.
- Top-k is a tradeoff: higher k improves recall but increases noise and cost downstream.

**Common failure modes to demo in class**:

- Wrong filter:
  - you silently retrieve from the wrong subset
- No filter:
  - you retrieve “similar but irrelevant” chunks from other topics
- Too small `top_k`:
  - the relevant chunk exists but is not retrieved
- Too large `top_k`:
  - you pass too much noise into `/chat` and citation quality drops

Citations:

- https://docs.trychroma.com/
- https://github.com/milvus-io/milvus-docs

### 3) Retrieval metrics (minimum viable)

**Mental model**:

- Build a small query set and measure hit rate / recall@k to catch regressions.
- Track misses and inspect retrieved chunks to form hypotheses.

**Definitions (teach with concrete examples)**:

- Hit rate:
  - did we retrieve at least one correct chunk for the query?
- Recall@k:
  - if the correct chunk is in the index, did it appear in the top k?

**How to build a small query set**:

- Start with 10–20 queries covering:
  - obvious in-KB questions
  - confusing near-duplicate questions
  - out-of-KB questions (should retrieve low-signal)

Citations:

- https://www.pinecone.io/learn/retrieval-augmented-generation/
- https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html

## Common pitfalls

- Mixing retrieval and generation so you cannot tell which failed.
- No saved query set or metrics, so improvements are subjective.

## Workshop / Implementation Plan

- Implement `/search` endpoint that wraps vector DB query + filters.
- Add logs to print retrieved chunk IDs and sources for each query.
- Create a small query set and compute retrieval metrics.

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: System architecture overview


### Figure B: Data and control flow (ingestion -> retrieval -> generation -> evaluation)


## Self-check questions

- Can you explain why a specific chunk was retrieved?
- Do your retrieval metrics catch obvious regressions?

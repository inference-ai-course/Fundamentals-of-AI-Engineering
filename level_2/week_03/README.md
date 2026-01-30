# Level 2 — Week 3: Retrieval API + Debuggable Retrieval Metrics (RAG Without Generation Yet)

## What you should be able to do by the end of this week

- Expose retrieval via a debuggable `/search` API (filters + top-k).
- Build a small retrieval query set and compute simple retrieval metrics (hit rate / recall@k).
- Produce logs that let you inspect which chunks were retrieved and why.

Tutorials:
 
- [tutorial.md](tutorial.md)
- [01_retrieval_as_api.md](01_retrieval_as_api.md)
- [02_filters_topk_tradeoffs.md](02_filters_topk_tradeoffs.md)
- [03_retrieval_evaluation.md](03_retrieval_evaluation.md)

## Key Concepts (with explanations + citations)

### 1) Retrieval as a stable API (separate from chat)

**Mental model**:

- Treat retrieval as a first-class component with its own endpoint and logs.
- A `/search` API lets you debug retrieval independent of LLM behavior.

**Underlying theory**:

Retrieval can be modeled as a function:

$$
R(q; \theta) \rightarrow E
$$

Where:
- $q$ is the user query text
- $\theta$ are retrieval parameters (embedding model, distance metric, filters, `top_k`)
- $E$ is the evidence set (returned chunk hits)

Making `/search` a separate endpoint makes $R$ **observable** and **testable**.

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

**Underlying theory (formal definitions)**:

Let:
- $R$ be the set of relevant chunk ids for a query
- $L_k = [\ell_1, \ldots, \ell_k]$ be the ordered list of retrieved chunk ids
- $\text{hits}_k = R \cap \{\ell_1, \ldots, \ell_k\}$

Then:

$$
\mathrm{Precision@k} = \frac{|\text{hits}_k|}{k}, \quad \mathrm{Recall@k} = \frac{|\text{hits}_k|}{|R|}
$$

**Intuition**:

- **Precision@k**: "how noisy are the retrieved chunks?"
- **Recall@k**: "did I get the evidence I needed at all?"

**Hit rate** (a.k.a. success@k):

$$
\mathrm{Hit@k} = \mathbb{1}[|\text{hits}_k| > 0]
$$

("Did we retrieve at least one correct chunk?")

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

```mermaid
flowchart LR
  U[Client] --> API[FastAPI]
  API --> S[/search/]
  API --> C[/chat/ (later)]

  S --> RET[Retrieval service]
  RET --> V[(Vector DB)]
  RET --> LOG[Logs: query + filters + top_k + hits]

  EVAL[retrieval_eval.py] --> RET
  EVAL --> REP[Metrics report]
```

### Figure B: Data and control flow (ingestion -> retrieval -> generation -> evaluation)

```mermaid
flowchart TD
  QSET[Query set (10-20 items)] --> EVAL[Eval runner]
  EVAL --> S[/search/]
  S --> RET[Retrieve top-k]
  RET --> V[(Vector DB)]
  V --> H[Hits + scores]
  H --> J[Judge: hit? recall@k?]
  J --> M[Metrics summary]
  H --> F[Top failures + evidence]
```

## Self-check questions

- Can you explain why a specific chunk was retrieved?
- Do your retrieval metrics catch obvious regressions?

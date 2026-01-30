# Week 3 — Part 01: Retrieval as an API (separate from chat)

## Overview

If chat answers are bad, you need to know whether the problem is:

- retrieval returned the wrong chunks
- retrieval returned good chunks but generation failed
- retrieval returned nothing but the model answered anyway

So retrieval should be a first-class endpoint.

---

## Underlying theory: retrieval is nearest-neighbor search with a contract

### Retrieval as a function

In a RAG system, retrieval can be modeled as a function:

$$
R(q; \theta) \rightarrow E
$$

Where:

- $q$ is the user query text
- $\theta$ are retrieval parameters (embedding model, distance metric, index settings, filters, `top_k`)
- $E$ is the evidence set (your returned chunk hits)

Making `/search` a separate endpoint is a practical way to make $R$ observable and testable.

### Nearest-neighbor definition (what the vector DB is doing)

Let:

- $f(\cdot)$ be the embedding function mapping text to $\mathbb{R}^d$
- $s(\cdot,\cdot)$ be a similarity score (larger is more similar) or a distance $d(\cdot,\cdot)$ (smaller is closer)

Compute:

$$
\mathbf{q} = f(q), \quad \mathbf{x}_i = f(e_i)
$$

Then top-k retrieval returns the $k$ evidence items with best scores:

$$
\mathrm{TopK}(q) = \operatorname{argsort}_{i} \; s(\mathbf{q}, \mathbf{x}_i) \; [1:k]
$$

Or equivalently (for distances):

$$
\mathrm{TopK}(q) = \operatorname{argsort}_{i} \; d(\mathbf{q}, \mathbf{x}_i) \; [1:k]
$$

Key implication:

- retrieval returns what is *numerically close* under your embedding + metric, not what is *factually correct*

### Why “API contract” matters more than “best retrieval” early

In Week 3, your goal is not to maximize quality; it is to make failures attributable.

If you can reliably answer:

- what query was used?
- what `top_k` and filters were used?
- what ranked chunk ids and scores were returned?

Then you can improve retrieval systematically instead of guessing.

---

## Minimal `/search` contract

Request:

- `query`: string
- `top_k`: int
- `filters`: optional object

Response:

- list of hits with:
  - `doc_id`
  - `chunk_id`
  - `score`
  - `text`
  - `metadata`

Practical interpretation of fields:

- `chunk_id` is your primary debug handle (lets you locate the exact stored chunk)
- `score` is a retrieval signal (used for thresholding, reranking decisions, and debugging)
- `metadata` is what enables filtering and traceability (source, url/section, version)

---

## Concrete FastAPI model + endpoint (example)

Even if your retrieval is not perfect yet, make the contract real with typed models.

```python
from pydantic import BaseModel, Field
from fastapi import FastAPI

class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=50)
    filters: dict | None = None

class SearchHit(BaseModel):
    doc_id: str
    chunk_id: str
    score: float
    text: str
    metadata: dict

class SearchResponse(BaseModel):
    query: str
    hits: list[SearchHit]

app = FastAPI()

@app.post("/search", response_model=SearchResponse)
def search(req: SearchRequest) -> SearchResponse:
    # TODO: replace with vector DB query
    hits: list[SearchHit] = []
    return SearchResponse(query=req.query, hits=hits)
```

Why this is worth doing early:

- FastAPI generates OpenAPI for you
- Pydantic validation catches bad inputs consistently
- your client integration becomes stable

---

## Practical usage: what to log so retrieval is debuggable

For every `/search` call, log at least:

- query text (or a hash if sensitive)
- `top_k`
- filters
- embedding model name
- distance/similarity metric used by the store
- returned hits: `rank`, `chunk_id`, `doc_id/source`, and `score`

This is what lets you answer: “Is the system failing because $R$ is wrong, or because generation ignored good evidence?”

---

## References

- FastAPI: https://fastapi.tiangolo.com/
- HTTP status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Pydantic: https://docs.pydantic.dev/

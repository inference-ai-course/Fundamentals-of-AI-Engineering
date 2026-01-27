# Week 3 — Part 01: Retrieval as an API (separate from chat)

## Overview

If chat answers are bad, you need to know whether the problem is:

- retrieval returned the wrong chunks
- retrieval returned good chunks but generation failed
- retrieval returned nothing but the model answered anyway

So retrieval should be a first-class endpoint.

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

## References

- FastAPI: https://fastapi.tiangolo.com/
- HTTP status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Pydantic: https://docs.pydantic.dev/

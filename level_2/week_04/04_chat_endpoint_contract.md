# Week 4 — Part 04: Minimal `/chat` endpoint contract

## Overview

Your `/chat` endpoint should be a thin layer:

- validate request
- call retrieval (`/search` logic)
- assemble context
- call model
- validate output (citations + refusal rules)

---

## Contract theory (why a “thin /chat” works)

### Separation of concerns

Conceptually, your system has three distinct functions:

- retrieval: $R(q, \theta_r) \rightarrow E$ (get evidence)
- prompting/packing: $P(q, E, \theta_p) \rightarrow \text{prompt}$ (format evidence)
- generation: $G(\text{prompt}, \theta_g) \rightarrow y$ (produce answer)

Keeping `/chat` thin means:

- retrieval stays testable without generation
- failures have a single obvious location (retrieval vs packing vs generation)

### Invariants you want the contract to enforce

Your API contract should make these properties checkable:

- **Traceability**: every citation points to a retrieved `chunk_id`.
- **Determinism of modes**: `mode` is driven by retrieval signals (empty hits, low score, conflicts), not random wording.
- **Observability**: you can log request inputs and retrieved outputs without guessing.

If these are invariants, you can write tests and eval items for them.

---

## Suggested `/chat` request/response

Request:

```json
{"question": "...", "top_k": 5, "filters": {}}
```

Response:

```json
{
  "answer": "...",
  "citations": [{"doc_id": "...", "chunk_id": "...", "snippet": "..."}],
  "mode": "answer" 
}
```

Where `mode` is one of:

- `answer`
- `clarify`
- `refuse`

---

## Practical implications (what to include and what to avoid)

- Keep request inputs minimal and stable.
  - `question`, `top_k`, and `filters` are enough for a course-grade system.
- Avoid adding “clever” parameters early (rerank configs, multiple retrieval pipelines).
  - if you can’t explain how a parameter changes $E$ (retrieved evidence), you won’t be able to debug it.

---

## Failure modes (and what the contract prevents)

- **Silent hallucination**: happens when you return `mode=answer` without valid citations.
  - contract response should always include citations (possibly empty), so validators can detect this.
- **Un-debuggable behavior**: happens when retrieval and chat are merged and you can’t inspect $E$.
  - separating retrieval logic makes it easy to log the evidence set.
- **Score threshold confusion**: thresholds drift if embedding model/metric changes.
  - keep thresholds as configuration and record them in run artifacts.

---

## Typed schema example (FastAPI/Pydantic)

```python
from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    question: str = Field(min_length=1)
    top_k: int = Field(default=5, ge=1, le=50)
    filters: dict | None = None

class Citation(BaseModel):
    doc_id: str
    chunk_id: str
    snippet: str

class ChatResponse(BaseModel):
    answer: str
    citations: list[Citation]
    mode: str
```

This makes the contract inspectable in `/docs` and makes validation consistent.

---

## Integration notes

Keep `/chat` thin:

- retrieval logic should live in a function/module you can also use for `/search`
- citation validation should run after generation
- refusal/clarify decision should happen before generation (based on retrieval signals)

This separation is what makes debugging possible.

---

## Self-check

- Are citations traceable to stored chunks?
- Does your system refuse/clarify when retrieval is empty?

---

## References

- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/

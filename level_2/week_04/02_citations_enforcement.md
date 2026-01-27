# Week 4 — Part 02: Citation format + enforcement

## Overview

Citations make answers:

- auditable
- debuggable
- safer (less hallucination)

A citation must be traceable to an actual snippet your system retrieved.

---

## Citation theory (why this works)

### Citations are verifiable pointers

In a RAG system, the important property is **verifiability**:

- each answer claim should be backed by a pointer to evidence
- the pointer should resolve to a chunk you actually retrieved

This turns “correctness” into something you can test:

- without citations, you only have subjective “sounds right” judgments
- with citations, you can inspect exactly what the model relied on

### Snippet checks: why strict substring is effective

If you require `snippet` to be a strict substring of the stored chunk text:

- the model is forced to copy evidence rather than invent it
- you get a cheap mechanical check (no extra model call)

Tradeoff:

- strict checks can be brittle (formatting changes, whitespace, punctuation)
- but brittleness is often acceptable early because it encourages clean chunking and stable storage

### When strictness is too brittle

If strict substring validation fails too often, common reasons are:

- chunk text was post-processed (newlines normalized, markdown rendered)
- the model paraphrased instead of quoting
- retrieval returned the right doc but the answer sentence sits across a chunk boundary

Before relaxing validation, try:

- increasing overlap in chunking (Week 2)
- requiring the model to quote exact spans

---

## Simple citation format

Return citations as structured objects:

```json
{"doc_id": "...", "chunk_id": "...", "snippet": "..."}
```

Rules:

- `snippet` must be a substring (or near-substring) of stored chunk text.
- `chunk_id` must exist in the retrieved set.

Practical extension:

- include `url` if you store it in metadata
- keep `snippet` short (e.g., 120–300 chars) so it is readable

---

## Output schema (recommended)

Model outputs are easiest to validate if they are structured.

Suggested response shape:

```json
{
  "answer": "...",
  "citations": [{"doc_id": "...", "chunk_id": "...", "snippet": "..."}],
  "mode": "answer"
}
```

Where `mode` is `answer|clarify|refuse`.

---

## Enforcement idea (engineering)

Before returning a response:

- verify each citation chunk_id is in retrieved hits
- optionally verify snippet overlap

If not, treat as failure and:

- retry with a repair prompt
- or refuse

---

## Minimal validation (example)

```python
def validate_citations(citations: list[dict], retrieved_chunk_ids: set[str], chunks_by_id: dict[str, str]) -> bool:
    for c in citations:
        chunk_id = c.get("chunk_id")
        snippet = c.get("snippet", "")
        if not chunk_id or chunk_id not in retrieved_chunk_ids:
            return False
        chunk_text = chunks_by_id.get(chunk_id, "")
        if snippet and snippet not in chunk_text:
            return False
    return True
```

Notes:

- strict substring checking is simplest and forces good behavior
- if you find it too brittle, you can use a relaxed overlap check later

---

## Repair loop pattern

When validation fails:

1. retry once with a “repair” instruction (don’t change everything)
2. if still invalid, switch to `mode=refuse`

This gives you deterministic behavior instead of random hallucination.

---

## References

- JSON Schema: https://json-schema.org/
- OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs

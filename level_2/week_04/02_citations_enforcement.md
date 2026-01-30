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

What to verify (practical):

- The validator uses the **retrieved hits from this request**, not some global set.
- A citation should fail if:
  - `chunk_id` is missing
  - `chunk_id` was not retrieved
  - `snippet` is not found in the stored chunk text
- Log enough context to debug:
  - requested `top_k`
  - retrieved `chunk_id`s
  - the model’s returned citations

If you log these, you can quickly tell whether the failure is retrieval (wrong chunks) or generation (wrong citations).

If not, treat as failure and:

- retry with a repair prompt
- or refuse

---

## Minimal validation (example with step-by-step explanation)

```python
def validate_citations(citations: list[dict], retrieved_chunk_ids: set[str], chunks_by_id: dict[str, str]) -> bool:
    """
    Validate that all citations reference actually-retrieved chunks and quote real snippets.
    
    Args:
        citations: List of citation dicts with 'chunk_id' and 'snippet'
        retrieved_chunk_ids: Set of chunk IDs that were actually retrieved for this request
        chunks_by_id: Mapping from chunk_id to full stored chunk text
    
    Returns:
        True if all citations are valid, False otherwise
    """
    for c in citations:
        chunk_id = c.get("chunk_id")
        snippet = c.get("snippet", "")
        
        # Check 1: chunk_id must exist and must have been retrieved
        if not chunk_id or chunk_id not in retrieved_chunk_ids:
            return False
        
        # Check 2: snippet must be a substring of the actual stored chunk
        chunk_text = chunks_by_id.get(chunk_id, "")
        if snippet and snippet not in chunk_text:
            return False
    
    return True
```

### Worked example: valid vs invalid citations

Suppose you retrieved these chunks:

```python
retrieved_chunk_ids = {"chunk_001", "chunk_002"}
chunks_by_id = {
    "chunk_001": "FastAPI is a modern web framework for building APIs with Python.",
    "chunk_002": "OpenAPI is a specification for describing REST APIs."
}
```

**Valid citation:**
```python
citation = {
    "chunk_id": "chunk_001",
    "snippet": "modern web framework for building APIs"
}
# ✓ chunk_001 is in retrieved_chunk_ids
# ✓ "modern web framework for building APIs" is substring of chunk_001 text
```

**Invalid citation (hallucinated chunk_id):**
```python
citation = {
    "chunk_id": "chunk_999",  # ✗ not in retrieved_chunk_ids
    "snippet": "some text"
}
```

**Invalid citation (invented snippet):**
```python
citation = {
    "chunk_id": "chunk_001",
    "snippet": "super fast web framework"  # ✗ "super fast" not in actual chunk text
}
```

### Why strict substring checking works

- Forces the model to copy evidence rather than paraphrase
- Makes validation mechanical (no LLM call needed)
- Catches hallucination immediately

### When to relax strictness

If strict checking fails too often, common causes:
- Chunk text was normalized (whitespace, newlines)
- Model used smart quotes vs straight quotes
- Answer spans across chunk boundary

Before relaxing validation:
1. Increase chunk overlap (Week 2)
2. Normalize both stored text and snippet (lowercase, strip whitespace)
3. Require model to quote exact spans in prompt

---

## Repair loop pattern

When validation fails:

1. retry once with a “repair” instruction (don’t change everything)
2. if still invalid, switch to `mode=refuse`

A concrete repair instruction that often works:

- “Return the same answer, but fix citations so that every `chunk_id` is one of: {retrieved_chunk_ids}. The `snippet` must be copied exactly from the corresponding chunk text. Return ONLY JSON.”

Why only one retry:

- If the model can’t produce valid citations after one targeted repair, repeated retries usually just waste time and cost.
- A deterministic refusal is better UX than a long hang or an unverifiable answer.

This gives you deterministic behavior instead of random hallucination.

---

## References

- JSON Schema: https://json-schema.org/
- OpenAI structured outputs: https://platform.openai.com/docs/guides/structured-outputs

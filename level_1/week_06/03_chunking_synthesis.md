# Week 6 — Part 03: Chunking long text + synthesizing summaries

## Overview

When text is too long for the context window:

1. **Split into chunks**
    - Goal: create pieces that are small enough to fit comfortably in the model context along with instructions and output budget.
    - What to verify: each chunk is non-empty and you can trace a chunk back to its position in the original document (chunk index or character offsets).
    - Practical tip: if the document has strong cross-paragraph references, add overlap between chunks (otherwise “boundary facts” get lost).
2. **Process each chunk**
    - Goal: produce a stable intermediate representation per chunk.
    - What to verify: per-chunk outputs follow a consistent structure so you can combine them later.
    - Example per-chunk schema (simple and robust):
      - `summary_bullets`: 3–5 bullets
      - `key_entities`: list of entities
      - `open_questions`: what is unclear/missing
3. **Synthesize a final summary**
    - Goal: merge the per-chunk outputs into one coherent answer.
    - What to verify: the synthesis step references evidence from the chunk summaries and does not invent new facts.
    - Practical tip: synthesis works better when chunk outputs are short (bounded) and consistent.

Even without a framework, you should understand the pattern.

---

## Underlying theory: chunking is a strategy for bounded-context reasoning

If the document is longer than what you can send at once, you have two options:

- **lossy compression**: summarize first (risk losing details)
- **chunking**: split and process pieces (risk missing cross-chunk dependencies)

Chunking introduces a boundary effect:

- information near chunk boundaries can be separated
- the model may miss references that span chunks

Practical implication: if correctness depends on cross-paragraph links, you may need overlap or a second pass.

## Simple chunking utility

```python
def chunk_text(text: str, chunk_size: int = 2000) -> list[str]:
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i : i + chunk_size])
        i += chunk_size
    return chunks
```

Note: chunking by character count is a simple starter, but tokens are what matter for LLM limits. Character chunking can still work for Level 1 as long as you keep chunks comfortably small.

---

## Synthesis pattern (high-level)

- For each chunk: ask the model for a short structured summary.
- After all chunks: ask the model to combine those summaries.

This is a simple form of hierarchical summarization:

- level 1: per-chunk summaries
- level 2: a global synthesis

Practical implication: enforcing a small per-chunk schema (e.g., bullet points or JSON fields) helps reduce drift and makes synthesis more reliable.

---

## References

- LangChain text splitters (reference): https://python.langchain.com/docs/how_to/#text-splitters

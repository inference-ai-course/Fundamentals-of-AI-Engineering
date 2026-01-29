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

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on context limits and workflow patterns:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 3: AI Engineering Fundamentals](../../level_0/Chapters/3/Chapter3.md)

Why it matters here (Week 6):

- Chunking is a practical strategy when inputs exceed the context window.
- Use overlap and a synthesis step when cross-chunk references matter.

## Simple chunking utility

```python
from typing import List


def chunk_text(text: str, chunk_size: int = 2000) -> List[str]:
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

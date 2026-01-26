# Week 6 — Part 03: Chunking long text + synthesizing summaries

## Overview

When text is too long for the context window:

1. split into chunks
2. process each chunk
3. synthesize a final summary

Even without a framework, you should understand the pattern.

---

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

---

## Synthesis pattern (high-level)

- For each chunk: ask the model for a short structured summary.
- After all chunks: ask the model to combine those summaries.

---

## References

- LangChain text splitters (reference): https://python.langchain.com/docs/how_to/#text-splitters

# Week 6 — Part 03: Chunking long text + synthesizing summaries

## Overview

When text is too long for the context window:

1. split into chunks
2. process each chunk
3. synthesize a final summary

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

# Week 2 — Part 02: Chunking + idempotent ingestion

## Overview

Chunking defines the unit you retrieve.

Idempotent ingestion means:

- running ingestion twice does **not** create duplicates
- re-ingesting updated documents produces predictable results
- your `chunk_id` scheme is stable (or versioned deliberately)

---

## Why chunking matters more than the vector DB

Your LLM never reads “the whole KB”. It reads the **top-k retrieved chunks**.

So chunking is directly tied to:

- retrieval accuracy (did we retrieve the right chunk?)
- generation quality (did the chunk contain enough context to answer?)
- citation quality (did the chunk contain the cited sentence?)

---

## Chunking rules of thumb

- Too small → loses context
- Too large → similarity gets diluted

Start with a fixed-size baseline, then iterate later.

Practical starter baseline (for English prose):

- chunk size: ~300–800 tokens (or ~1–3k characters)
- overlap: ~10–20% (or ~100–200 characters)

Keep it simple first. You can introduce structure-aware chunking later.

---

## Chunking theory (tokens, overlap, and the retrieval budget)

### The core constraint: the LLM context window

At answer time, your system typically builds a prompt like:

- system instructions
- user question
- top-k chunks

So you have a finite context budget. If your model context window is $C$ tokens, you can think of it as:

$$
C \approx T_{\text{system}} + T_{\text{question}} + k \cdot T_{\text{chunk}} + T_{\text{formatting}}
$$

Practical implications:

- If $T_{\text{chunk}}$ is too large, you can’t fit enough evidence (small $k$).
- If $T_{\text{chunk}}$ is too small, each chunk may be missing the sentence that makes it “answerable”.

### Overlap math (how much redundancy you introduce)

For a fixed-size sliding window chunker:

- chunk size $S$
- overlap $O$
- stride $\Delta = S - O$
- document length $L$

Approximate number of chunks is:

$$
N \approx \left\lceil \frac{L - O}{S - O} \right\rceil
$$

And the redundancy factor (how many times characters/tokens are repeated across chunks) is roughly:

$$
\text{redundancy} \approx \frac{S}{S - O}
$$

So:

- larger overlap $O$ reduces boundary misses, but increases storage + embedding cost
- overlap of 20% implies redundancy $\approx 1.25$ (you embed ~25% extra)

### Boundary effects (why overlap exists)

Chunk boundaries cut sentences/definitions in half.

If an answer requires a local context window of $W$ tokens (e.g., a definition plus its constraints), you want overlap $O$ large enough that the $W$-token region is likely to appear fully inside at least one chunk.

Rule-of-thumb way to think about it:

- overlap should be at least the typical “dependency span” (often 1–3 sentences)

---

## Practical calibration workflow (how to pick chunk size)

Start with a baseline, then tune using a small evaluation set:

- Pick $S$ and $O$ (e.g., 600 tokens and 100 overlap)
- Create 10–30 questions with known supporting passages
- Run retrieval and inspect:
  - whether the needed sentence appears in top-k
  - whether the chunk includes enough surrounding context to answer safely

Heuristics:

- If you often retrieve the *right location* but the chunk is missing the key sentence, increase overlap $O$ or chunk size $S$.
- If retrieved chunks contain lots of unrelated material, decrease $S$ or add structure-aware splitting.

---

## Chunking strategies (in order of complexity)

- **Fixed-size sliding window** (good baseline)
- **Paragraph-based** (split on blank lines, then merge if too small)
- **Heading-aware** (keep sections together)
- **Semantic chunking** (harder; tends to require heuristics and testing)

---

## Minimal fixed-size chunker (example)

This example chunker uses characters for simplicity (works fine for course projects).

```python
from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    start: int
    end: int


def chunk_text(text: str, chunk_size: int = 1200, overlap: int = 200) -> list[Chunk]:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be > 0")
    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and < chunk_size")

    chunks: list[Chunk] = []
    i = 0
    n = len(text)
    while i < n:
        j = min(i + chunk_size, n)
        chunks.append(Chunk(text=text[i:j], start=i, end=j))
        if j == n:
            break
        i = j - overlap
    return chunks
```

This gives you deterministic chunks for the same input text.

---

## Simple idempotency strategy: chunk hash id

If you generate chunk ids as a hash of content, duplicates naturally overwrite.

```python
import hashlib


def chunk_id_for(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()
```

Why this works:

- identical text → identical id → repeated ingestion overwrites instead of duplicating

Where it can fail:

- if you change chunking parameters, chunks change, ids change, and you may effectively create a new set
- if your documents update frequently, you may want `doc_version` + cleanup strategy

Store:

- `chunk_id` = hash
- metadata includes `doc_id` and `source`
- (recommended) record chunking parameters and embedding model in a run log

---

## Alternative idempotency strategy: deterministic chunk numbering

Another common approach:

- `chunk_id = f"{doc_id}#{chunk_index:05d}"`

Pros:

- stable ids if your chunking is stable
- easier to read in logs

Cons:

- if insertion/deletion happens early in the document, all later indices shift

For projects with frequent document changes, hash ids (or hybrid ids) are usually safer.

---

## References

- Twelve-Factor mindset: https://12factor.net/
- SHA-256 (hash function overview): https://en.wikipedia.org/wiki/SHA-2
- LangChain text splitters (conceptual reference): https://python.langchain.com/docs/concepts/text_splitters/
 - OpenAI tiktoken (tokenization library): https://github.com/openai/tiktoken

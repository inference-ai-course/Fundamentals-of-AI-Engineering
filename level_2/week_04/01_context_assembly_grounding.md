# Week 4 — Part 01: Context assembly and grounding

## Overview

In RAG, you are controlling *what the model is allowed to use*.

Your goal:

- the model answers from retrieved context
- it does not invent unsupported claims

---

## Grounding theory (what you are doing mathematically)

### Grounding as “constrained generation”

In an ideal grounded system, the model’s answer should be a function of:

- the user question $q$
- the retrieved evidence $E = \{e_1, \ldots, e_k\}$

Conceptually:

$$
\text{answer} \approx g(q, E)
$$

The goal is to reduce reliance on the model’s latent priors (what it “remembers”) and increase reliance on explicit evidence.

Practical implication:

- if $E$ is empty or irrelevant, the system should not “guess”
- refusal/clarification is not a prompt trick; it is a decision based on retrieval signals

### Noise vs recall (why context packing matters)

Adding more chunks increases the chance that relevant evidence is included (recall), but it also increases irrelevant tokens (noise).

Heuristic tradeoff:

- higher $k$ (more chunks) often improves recall
- but more noise can degrade generation quality because the model may attend to distractors

This is why “top-k retrieval” is not enough by itself: you need chunking, filters, and packing strategies.

### Context budget math (why you can’t just include everything)

Even before the model starts answering, you spend tokens on structure:

$$
C \approx T_{\text{system}} + T_{\text{context}} + T_{\text{question}} + T_{\text{answer}}
$$

So you should design your context packing so that $T_{\text{context}}$ is high-signal:

- keep metadata small but stable (chunk_id/doc_id/url)
- truncate chunk text if needed, but keep enough to preserve the key sentence

---

## Practical pattern: structured context block

Build a `CONTEXT` block as a list of chunks, each with:

- `doc_id`
- `chunk_id`
- `text`

Example:

```text
CONTEXT:
[1] doc_id=..., chunk_id=..., text="..."
[2] doc_id=..., chunk_id=..., text="..."
```

A practical improvement: include **source fields you can cite**.

```text
CONTEXT:
[1] doc_id=fastapi  chunk_id=fastapi#001  url=https://fastapi.tiangolo.com/  text="..."
[2] doc_id=openapi  chunk_id=openapi#002  url=https://spec.openapis.org/oas/latest.html  text="..."
```

If you later build UI, you can render citations as clickable links.

---

## Prompt rules (recommended)

- Keep task instructions short.
- Explicitly forbid unsupported claims.
- Require citations for each answer claim.

---

## Prompt template (minimal, reliable)

The key is to separate:

- system rules (grounding, citations, refusal)
- the context (retrieved chunks)
- the user question

Example template (conceptual):

```text
You are a grounded assistant.

Rules:
- Use only the CONTEXT.
- If the CONTEXT is insufficient, respond with mode=clarify or mode=refuse.
- For every factual claim, include a citation referencing one of the chunk_id values.

CONTEXT:
[1] doc_id=... chunk_id=... url=... text="..."
[2] doc_id=... chunk_id=... url=... text="..."

Question: {question}
```

You can keep this exact structure even as your system grows.

---

## Context packing tips (avoid hidden failures)

- Prefer fewer, higher-signal chunks over many noisy chunks.
- Keep chunk order stable (rank order) so debugging is consistent.
- When token budget is tight:
  - truncate per-chunk text to a fixed max length
  - keep metadata fields intact (doc_id/chunk_id/url)

---

## What to log

To debug hallucinations, log:

- the search query
- retrieved chunk ids + scores
- the exact chunk ids passed into the prompt
- the exact prompt (or a hash + saved prompt artifact)

Logging the full prompt is often the fastest way to debug grounding failures.

---

## References

- RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/
- Chroma docs: https://docs.trychroma.com/
- OpenAI prompting guide: https://platform.openai.com/docs/guides/prompting

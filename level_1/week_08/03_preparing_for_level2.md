# Week 8 — Part 03: Preparing for Level 2 (what changes)

## Overview

Level 1 is mostly:

- a single-project pipeline
- mostly offline, script-based
- focusing on reproducibility and reliability basics

Level 2 shifts toward **systems thinking**:

- retrieval (RAG)
- evaluation loops
- multi-step agent workflows
- knowledge bases

---

## Underlying theory: Level 2 adds feedback loops and new failure surfaces

In Level 1, many workflows are “run once and inspect outputs”.

In Level 2, you will build systems with feedback loops:

- retrieval quality affects generation quality
- evaluation metrics guide iteration
- multi-step workflows introduce compounding failure probability

Practical implication:

- you need observability (traces/logs) to debug why a system answered
- you need eval sets to prevent “prompt overfitting”
- you need trust boundaries to resist prompt injection when external data is involved

---

## Practical mindset shifts

- From “one script works” → “the system is observable and testable”.
- From “prompting” → “prompt + retrieval + evaluation”.
- From “manual checking” → “repeatable eval sets”.

---

## References

- RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/

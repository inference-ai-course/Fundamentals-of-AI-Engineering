# Week 5 — Part 02: Minimal eval set design (10–20 items)

## Overview

A minimal eval set creates repeatable signals.

You don’t need hundreds of examples to start.

---

## The underlying theory: you are sampling from a distribution

Your real users generate questions from some unknown distribution $D$.

An eval set is a sample from $D$ (or an approximation). If your eval set is biased, you will optimize the wrong behavior.

Practical implication:

- include the failure modes you actually care about, not just easy questions

---

## Coverage beats size (early on)

With 10–20 items, your goal is not high statistical confidence.

Your goal is to cover:

- common intents
- near-miss cases (where retrieval must be correct)
- out-of-KB boundary
- ambiguous queries that should trigger clarification

This makes the eval set sensitive to the changes you will actually make (chunking, filters, top_k, prompt structure).

## Suggested composition (10–20 items)

- 50% obvious in-KB
- 30% near-miss (requires the correct chunk)
- 20% out-of-KB (should refuse/clarify)

---

## What to store per item

- question
- expected mode:
  - answer / clarify / refuse
- expected citation doc_id (optional but helpful)
- (recommended) acceptable chunk_ids (one or more)

---

## Labeling rules: define “correct” operationally

Bad eval sets fail because “correctness” is vague.

For each item, define an operational check:

- retrieval correctness: did we retrieve any acceptable chunk_id in top-k?
- mode correctness: was mode in {answer, clarify, refuse} as expected?
- citation validity: did citations reference retrieved chunks and quote real snippets?

Keep labels simple and mechanically checkable. This is why chunk_ids are so useful.

---

## Example eval item (JSONL)

```json
{
  "id": "q_001",
  "question": "What endpoint shows the service is healthy?",
  "expected_mode": "answer",
  "relevant_chunk_ids": ["fastapi#001", "service#health"],
  "notes": "Should cite health endpoint docs"
}
```

Why JSONL:

- easy to append
- easy to diff in git
- easy to stream/process

---

## Self-check

- Does your eval set cover failure cases you actually observed?

---

## References

- IR evaluation: https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html
- JSON Lines: https://jsonlines.org/

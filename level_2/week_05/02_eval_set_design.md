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

## Example eval items (JSONL format)

### Good example: specific in-KB question
```json
{
  "id": "q_001",
  "question": "What endpoint shows the service is healthy?",
  "expected_mode": "answer",
  "relevant_chunk_ids": ["fastapi#001", "service#health"],
  "notes": "Should cite health endpoint docs"
}
```

### Good example: near-miss requiring exact chunk
```json
{
  "id": "q_002",
  "question": "What is the default timeout for model calls?",
  "expected_mode": "answer",
  "relevant_chunk_ids": ["config#timeout"],
  "notes": "Must retrieve chunk containing timeout value"
}
```

### Good example: out-of-KB question (should refuse)
```json
{
  "id": "q_003",
  "question": "What is the weather in Tokyo tomorrow?",
  "expected_mode": "refuse",
  "relevant_chunk_ids": [],
  "notes": "Not in KB scope, should refuse"
}
```

### Good example: ambiguous question (should clarify)
```json
{
  "id": "q_004",
  "question": "How do I start it?",
  "expected_mode": "clarify",
  "relevant_chunk_ids": [],
  "notes": "Underspecified - 'it' could be service, ingestion, eval script"
}
```

### Bad example: too vague to grade
```json
{
  "id": "bad_001",
  "question": "Tell me about the system",
  "expected_mode": "answer",  // ✗ What counts as a correct answer?
  "relevant_chunk_ids": [],   // ✗ No grading criteria
  "notes": ""
}
```

### Why these examples work

**Good items have:**
- Specific grading criteria (chunk IDs or clear mode expectation)
- Realistic user intent (not contrived edge cases)
- Clear expected behavior (answer with evidence, refuse, or clarify)

**Bad items lack:**
- Mechanical way to check correctness
- Clear boundary between pass/fail

### Building your first 10-item set

Start with these 4 categories:

1. **5 obvious in-KB** (testing retrieval baseline)
   - "What endpoint returns health status?" → should retrieve `fastapi#health`
   - "How do I configure the model?" → should retrieve `config#model`

2. **3 near-miss** (testing chunking/overlap)
   - Questions where the answer is in the KB but requires the right chunk
   - These expose chunking problems early

3. **1-2 out-of-KB** (testing refusal)
   - Questions clearly outside your domain
   - Should trigger `mode=refuse`

4. **1-2 ambiguous** (testing clarification)
   - Underspecified questions
   - Should trigger `mode=clarify`

### Why JSONL format

- Easy to append new items as you find failures
- Easy to diff in git (one item per line)
- Easy to stream/process line-by-line
- No merge conflicts when multiple people add items

---

## Self-check

- Does your eval set cover failure cases you actually observed?
- Can you mechanically grade each item without human judgment?
- Do you have at least one item per mode (answer, clarify, refuse)?

---

## References

- IR evaluation: https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html
- JSON Lines: https://jsonlines.org/

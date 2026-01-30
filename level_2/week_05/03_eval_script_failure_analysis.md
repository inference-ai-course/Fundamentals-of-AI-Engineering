# Week 5 — Part 03: Reproducible eval outputs + failure analysis

## Overview

A good `eval_rag.py` does two things:

- prints metrics
- prints failures with evidence

---

## Minimum metrics (recommended)

- retrieval hit rate / recall@k
- citation coverage rate
- refusal correctness rate

Define each metric precisely before coding it.

Example:

- citation coverage rate = fraction of `mode=answer` responses that have >= 1 valid citation

---

## Metric formalization (examples)

Let the eval set have $n$ items.

### Hit rate@k (retrieval)

Let $h_i \in \{0,1\}$ indicate whether item $i$ retrieved at least one relevant chunk in top-k.

$$
\mathrm{Hit@k} = \frac{1}{n} \sum_{i=1}^{n} h_i
$$

### Refusal correctness

Let $r_i \in \{0,1\}$ indicate whether the predicted mode matches the expected mode.

$$
\mathrm{RefusalCorrect} = \frac{1}{n} \sum_{i=1}^{n} r_i
$$

These definitions look simple, but writing them down prevents “metric drift” where different runs compute different things.

---

## Uncertainty intuition (don’t overfit the eval set)

If you only have 10–20 items, you can “overfit” by tuning until your eval set looks good, without truly improving.

Practical guardrails:

- keep a small hidden set (even 5 items) you don’t look at during tuning
- when you think you improved, validate once on the hidden set

If you don’t want a hidden set, at least keep a “frozen baseline” configuration and compare against it periodically.

---

## Failure labeling (root cause with examples)

For each failure, label one primary cause:

- retrieval miss
- context too noisy
- prompt ambiguous
- model ignored citation rules

This makes iteration focused.

### Worked failure examples

**Example 1: Retrieval miss**
```json
{
  "id": "q_007",
  "question": "What is the default chunk size?",
  "expected_mode": "answer",
  "actual_mode": "refuse",
  "retrieved_chunk_ids": ["config#model", "config#embedding"],
  "relevant_chunk_ids": ["config#chunking"],
  "label": "retrieval_miss",
  "fix": "config#chunking was ranked 6th. Increase top_k from 5 to 8, or improve chunking metadata filters"
}
```
**Root cause:** The relevant chunk exists but wasn't in top-5  
**Action:** Increase `top_k` or add metadata filter

---

**Example 2: Context too noisy**
```json
{
  "id": "q_008",
  "question": "How do I configure retry behavior?",
  "expected_mode": "answer",
  "actual_mode": "answer",
  "retrieved_chunk_ids": ["retry#001", "timeout#002", "error#003", "rate_limit#004", "network#005"],
  "citations": [{"chunk_id": "timeout#002", "snippet": "set timeout to 30s"}],
  "label": "context_too_noisy",
  "fix": "Retrieved 5 chunks but only retry#001 is relevant. Model attended to timeout chunk instead. Reduce top_k or improve filters."
}
```
**Root cause:** Too many irrelevant chunks diluted the signal  
**Action:** Reduce `top_k` or add tighter filters

---

**Example 3: Model ignored citation rules**
```json
{
  "id": "q_009",
  "question": "What embedding model should I use?",
  "expected_mode": "answer",
  "actual_mode": "answer",
  "retrieved_chunk_ids": ["embedding#001"],
  "citations": [],
  "label": "model_ignored_citation_rules",
  "fix": "Model returned answer but zero citations. Strengthen prompt: 'You MUST include citations. If you cannot cite, refuse.'"
}
```
**Root cause:** Prompt wasn't strict enough about citations  
**Action:** Make citation requirement non-optional in prompt

---

**Example 4: Prompt ambiguous**
```json
{
  "id": "q_010",
  "question": "How do I start it?",
  "expected_mode": "clarify",
  "actual_mode": "answer",
  "retrieved_chunk_ids": ["startup#001", "uvicorn#002"],
  "label": "prompt_ambiguous",
  "fix": "System should have asked 'What do you want to start?' but model guessed. Add clarification trigger: if query < 5 words and contains pronoun, clarify."
}
```
**Root cause:** Clarification logic didn't trigger on ambiguous query  
**Action:** Add heuristic for underspecified questions

### Practical tip: "what would fix this?"

Always include one short actionable note:

- "Increase overlap to 200 chars" (for boundary issues)
- "Add filter: source='docs'" (for retrieval precision)
- "Strengthen citation requirement in prompt" (for missing citations)
- "Lower clarify threshold from 0.3 to 0.4" (for false negatives)

This turns failures into your next experiment.

---

## Minimal `eval_rag.py` output contract

For each run, write:

- `metrics.json` (small summary)
- `failures.json` (one record per failing item)

Example `metrics.json`:

```json
{
  "run_id": "2026-01-27_1400_chunk800_overlap150",
  "n_items": 20,
  "retrieval_recall_at_k": 0.55,
  "citation_coverage": 0.90,
  "refusal_correctness": 0.80
}
```

---

## Failure record example (what to save)

```json
{
  "id": "q_014",
  "question": "...",
  "expected_mode": "answer",
  "actual_mode": "answer",
  "retrieved_chunk_ids": ["..."],
  "citations": [{"chunk_id": "...", "snippet": "..."}],
  "label": "retrieval_miss"
}
```

The goal is to have enough evidence to debug without re-running immediately.

---

## Artifacts to save

Per run id, save:

- config
- metrics
- failures list

---

## References

- Python logging: https://docs.python.org/3/library/logging.html
- JSON: https://docs.python.org/3/library/json.html

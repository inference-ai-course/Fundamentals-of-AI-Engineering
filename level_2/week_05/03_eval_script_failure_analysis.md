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

## Failure labeling (root cause)

For each failure, label one primary cause:

- retrieval miss
- context too noisy
- prompt ambiguous
- model ignored citation rules

This makes iteration focused.

Practical tip:

- always include one short note: “what would have made this succeed?”
- this turns failures into actionable changes (chunking, filters, prompt, citation rules)

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

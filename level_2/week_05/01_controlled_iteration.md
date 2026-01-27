# Week 5 — Part 01: Controlled iteration (one variable at a time)

## Overview

RAG systems improve through disciplined iteration.

If you change multiple things at once, you can’t explain improvements.

---

## The underlying theory: metrics are noisy signals

When you run an evaluation on a finite set of questions, your metric is an estimate of true performance.

If a metric is an average of per-item outcomes $x_i$ (e.g., hit=0/1, correct=0/1), then:

$$
\hat{\mu} = \frac{1}{n} \sum_{i=1}^{n} x_i
$$

This estimate has variance:

- small $n$ means more randomness
- a single hard question can move the metric a lot

Practical implication:

- when a metric moves from 0.50 to 0.55 on $n=20$, you should ask: “is this a real change or sampling noise?”

### Confidence intuition (rule-of-thumb)

For a 0/1 metric (a proportion) like hit rate, a rough standard error is:

$$
\mathrm{SE}(\hat{p}) \approx \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
$$

If $\hat{p}=0.5$ and $n=20$, then:

- $\mathrm{SE} \approx \sqrt{0.25/20} \approx 0.11$

So small changes (like +0.03) may not be meaningful on small eval sets.

You don’t need full statistics to start, but you do need the habit: treat metrics as estimates, not truth.

---

## Controlled iteration: isolate cause → effect

If you change one variable at a time, you can build a causal story:

- “chunk overlap increased recall@k, but reduced precision@k”
- “higher top_k increased hit rate but reduced citation validity due to noise”

This is also how you avoid cargo-cult tuning.

## Controlled experiment checklist

- Freeze everything except one variable:
  - chunk size/overlap
  - embedding model
  - top_k
  - rerank on/off

- Keep constant:
  - eval set
  - prompt template
  - dataset

- Save artifacts per run:
  - run id
  - config
  - metrics summary
  - top failures

---

## Practical run-id + folder layout

A simple pattern:

- `runs/2026-01-27_1400_chunk800_overlap150/`
  - `config.json`
  - `metrics.json`
  - `failures.json`
  - `samples.md`

This gives you:

- reproducibility (you can rerun the exact settings)
- rollback (you can compare and revert)
- a paper-trail for your capstone defense

---

## Experiment table (what you should be able to fill)

| run_id | change | metric_before | metric_after | notes |
|---|---|---:|---:|---|
| baseline | none | 0.45 | 0.45 | baseline |
| chunk800 | chunk_size=800 | 0.45 | 0.52 | improved recall, citations ok |

The habit matters more than the exact metric.

---

## Practical guidance: what counts as a “good” experiment

- Keep the eval set fixed during a tuning burst.
- Re-run the same config twice occasionally.
  - if metrics fluctuate a lot, you have an instability problem (non-determinism or too-small eval)
- When a change improves one metric but hurts another:
  - decide which metric aligns to your product goal
  - record the tradeoff explicitly

---

## References

- Twelve-Factor mindset: https://12factor.net/
- JSON Lines (easy run artifacts): https://jsonlines.org/

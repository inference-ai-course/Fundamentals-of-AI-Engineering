# Week 4 — Part 03: Refusal vs clarification (deterministic rules first)

## Overview

Don’t rely on prompt wording to decide refusal.

Implement a deterministic rule first, then use prompting to format the response.

---

## Deterministic rules (examples)

- If no chunks retrieved:
  - ask a clarifying question OR refuse

- If top score < threshold:
  - ask clarifying question

- If chunks conflict:
  - present both with citations OR ask clarification

---

## Underlying theory: refusal is a decision under uncertainty

Your retriever emits a score (similarity or distance). You can treat the top score $s$ as a signal of “is the KB likely relevant?”.

The simplest decision rule:

$$
\text{mode} =
\begin{cases}
\text{answer} & s \ge \tau \\
\text{clarify/refuse} & s < \tau
\end{cases}
$$

Where $\tau$ is a threshold you choose.

### False positives vs false negatives

- If $\tau$ is too low:
  - you answer out-of-KB questions (hallucination risk)
- If $\tau$ is too high:
  - you refuse in-KB questions (bad UX)

So threshold choice is always a product tradeoff, not a universal constant.

### Why score thresholds are model- and metric-specific

Scores are not comparable across:

- different embedding models
- different distance metrics (cosine vs dot vs L2)
- different vector DB implementations
- different chunking strategies

So any threshold must be calibrated on your own data.

---

## Recommended modes (make it explicit)

Use one of:
 
- `answer`: you have enough evidence in retrieved context
- `clarify`: you need the user to specify something to retrieve the right info
- `refuse`: question is out-of-scope/out-of-KB or unsafe to answer without evidence
 
This turns “LLM safety” into product logic.

---

## Thresholding: how to pick a score threshold

Scoring varies by vector DB and embedding model.

Practical approach:

- take 20 known in-KB questions
- log the top score for each
- take 20 known out-of-KB questions
- log the top score for each

Choose a threshold that separates them reasonably.

Even better: store these labeled examples as part of your eval set.

---

## In-KB vs out-of-KB classification

Make it testable:

- create 5–10 questions
- label each:
  - in-KB
  - ambiguous
  - out-of-KB

Your system should behave consistently on these.

A simple expected behavior table:

- in-KB → `answer` with citations
- ambiguous → `clarify`
- out-of-KB → `refuse`

---

## References

- HTTP 422 (validation errors): https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422
- OpenAI safety overview: https://platform.openai.com/docs/guides/safety

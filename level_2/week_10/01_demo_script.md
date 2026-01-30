# Week 10 — Part 01: Demo story + failure case

## Overview

A good demo shows:

- problem
- approach
- live run
- failure case
- evidence
- roadmap

---

## Underlying theory: a demo is an argument (claim → evidence → reasoning)

Good technical demos are not just “look, it runs”. They are a structured argument:

- claim: what your system can do (and cannot do)
- evidence: artifacts and live runs that support the claim
- reasoning: why the evidence supports the claim (mechanism + metrics)

For RAG systems, the most important claims are usually:

- grounded answers when evidence exists
- safe behavior (clarify/refuse) when evidence is missing

---

## Why you must include a failure case

Every real RAG system fails.

Showing a controlled failure case demonstrates:

- you understand failure modes
- you built deterministic guardrails (not “prompt hope”)
- you can debug via `/search` and traces

This builds credibility because it shows engineering control.

## Standard demo timing (example)

- 60s: problem framing + constraints
- 90s: architecture + data flow
- 2m: in-KB answer with citations
- 1m: out-of-KB failure case (refusal/clarification)
- 1m: evidence (metrics + top failures)
- 30s: roadmap

---

## Demo script (what to literally say/do)

- State the problem and constraints in one sentence.
- Show the system diagram and name each component.
- Run an in-KB question:
  - show the answer
  - show citations
  - (optional) show `/search` output to prove evidence
- Run an out-of-KB question:
  - show refusal/clarification
  - explain the deterministic rule
- Show evidence pack:
  - metrics file
  - top failures with labels
- Close with roadmap (two concrete iterations).

Concrete examples (to reduce “demo anxiety”):

- Problem + constraints sentence template:
  - “We built a RAG assistant for X. It must answer with citations, refuse when evidence is missing, and stay under Y seconds latency.”

- In-KB question examples:
  - Pick a question you *know* is answerable from your indexed docs.
  - Show that the answer includes at least one citation, and that the cited `chunk_id` exists in retrieval output.

- Out-of-KB question examples:
  - Ask something plausible but not in your docs.
  - Show the system returns `mode=clarify` or `mode=refuse` (not a confident hallucinated answer).

- Showing `/search` output (optional but powerful):
  - Point out top_k hits, scores, and doc_id/source.
  - If retrieval is empty, explicitly connect it to the refusal/clarification decision.

- Evidence pack presentation:
  - Open `runs/<run_id>/metrics.json` and highlight 1–2 numbers only.
  - Open `runs/<run_id>/failures.json` and show 1–2 labeled failures (with root-cause notes).

Practical rule:

- if you show “before vs after”, name the single variable you changed and the metric that moved

---

## Concrete demo script example (word-for-word)

Here's what a real 6-minute demo sounds like:

---

**[0:00-1:00] Problem + Constraints**

> "We built a RAG assistant for our internal FastAPI documentation. The requirements were: answer with citations, refuse when evidence is missing, and stay under 2 seconds latency for 95% of requests. Here's the architecture diagram."

*[Show diagram: User → `/chat` → Retrieval → Model → Citations]*

---

**[1:00-3:00] Happy path (in-KB question)**

> "Let me show a typical in-KB question."

```bash
$ curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What endpoint shows health status?", "top_k": 5}'
```

*Response:*
```json
{
  "answer": "The /health endpoint shows the health status.",
  "citations": [
    {"chunk_id": "fastapi#001", "doc_id": "fastapi_docs", "snippet": "GET /health returns..."}
  ],
  "mode": "answer"
}
```

> "Notice the citation includes `chunk_id` and a snippet. Let me show this chunk actually exists in retrieval."

```bash
$ curl -X POST http://localhost:8000/search \
  -d '{"query": "What endpoint shows health status?", "top_k": 5}'
```

*Response shows `fastapi#001` in top-3 hits*

> "This proves grounding: the citation references a chunk we actually retrieved."

---

**[3:00-4:00] Failure case (out-of-KB question)**

> "Now let's try an out-of-KB question."

```bash
$ curl -X POST http://localhost:8000/chat \
  -d '{"question": "What is the weather in Tokyo tomorrow?", "top_k": 5}'
```

*Response:*
```json
{
  "answer": "",
  "citations": [],
  "mode": "refuse"
}
```

> "The system refuses because this question is outside our documentation scope. This is deterministic: if retrieval returns empty or low-score hits, we refuse rather than hallucinate."

---

**[4:00-5:00] Evidence pack**

> "Here's our evaluation evidence. We ran 20 test queries."

*[Open `runs/baseline/metrics.json`]*

```json
{
  "retrieval_recall_at_5": 0.75,
  "citation_coverage": 0.90,
  "refusal_correctness": 1.0,
  "p95_latency_ms": 1850
}
```

> "Recall is 75%, meaning we retrieve the right chunk for 3 out of 4 in-KB questions. Citation coverage is 90%. Refusal correctness is 100% - we never hallucinate on out-of-KB queries. And p95 latency is 1.8 seconds, meeting our SLO."

*[Open `runs/baseline/failures.json`]*

```json
[
  {
    "id": "q_014",
    "question": "What is the default timeout?",
    "label": "retrieval_miss",
    "fix": "config#timeout was ranked 6th. Increase top_k to 8."
  }
]
```

> "Our main failure mode is retrieval misses where the right chunk exists but isn't in top-5. The fix is to increase top_k or improve metadata filters."

---

**[5:00-6:00] Roadmap**

> "Next two iterations:
> 1. Increase chunk overlap from 100 to 200 characters to reduce boundary issues
> 2. Add metadata filter for 'source=docs' to improve precision
> 
> We expect this to improve recall from 75% to 85% based on failure analysis."

---

## Self-check

- Can you demo without editing code live?
- Do you have a clear failure case story?
- Can you show metrics and explain what they mean in 30 seconds?
- Do you have a concrete "next 2 iterations" roadmap?

---

## References

- Effective presentations: https://sre.google/workbook/non-abstract-large-system-design/golo.com/
- FastAPI docs (demo via /docs): https://fastapi.tiangolo.com/

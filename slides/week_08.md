---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 8 — Capstone Demo & Retrospective"
style: |
  section { font-size: 24px; }
  pre { font-size: 18px; }
  code { font-size: 18px; }
  h1 { color: #0f3460; border-bottom: 3px solid #00d2ff; padding-bottom: 8px; }
  h2 { color: #16213e; }
  table { font-size: 20px; }
  img { max-height: 420px; display: block; margin: 0 auto; }
  section.lead { text-align: center; background: linear-gradient(135deg, #0f3460, #16213e); color: #e8e8e8; }
  section.lead h1 { color: #00d2ff; border: none; font-size: 48px; }
  section.lead h2 { color: #e8e8e8; font-weight: 400; }
---

<!-- _class: lead -->

# Week 8

## Capstone Demo & Retrospective

---

# Learning Objectives

By the end of this week, you should be able to:

- Demo your capstone with a "fresh clone + README" workflow
- Write a structured retrospective with evidence (logs, artifacts, diffs)
- Identify what shifts going from Foundational Course to Level 2

---

# What is a Retrospective?

![Retrospective cycle](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtSZWZsZWN0IG9uIHByb2plY3RdIC0tPiBCW0lkZW50aWZ5IHRvcCBpc3N1ZXNdCiAgQiAtLT4gQ1tSb290IGNhdXNlIGFuYWx5c2lzXQogIEMgLS0-IERbSW1wbGVtZW50IGZpeGVzXQogIEQgLS0-IEVbVmVyaWZ5IHdpdGggbWV0cmljc10KICBFIC0tPiBGW0RvY3VtZW50IGxlc3NvbnNd)

A **retrospective** = a structured reflection on what happened, why, and what to do differently.

In engineering culture, "blameless postmortems" emphasize **learning** from failures — backed by **evidence** (logs, artifacts, metrics), not guesswork.

---

# What is RAG? (Level 2 Preview)

![RAG concept](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtVc2VyIHF1ZXN0aW9uXSAtLT4gQltSZXRyaWV2ZSByZWxldmFudCBkb2NzXQogIEIgLS0-IENbQXVnbWVudCBwcm9tcHQgd2l0aCBkb2NzXQogIEMgLS0-IERbR2VuZXJhdGUgYW5zd2VyXQogIEQgLS0-IEVbQW5zd2VyIHdpdGggY2l0YXRpb25zXQ==)

**RAG** (Retrieval-Augmented Generation) = instead of sending all data to the LLM, first **retrieve** only the relevant parts, then **augment** the prompt with them.

This is the core pattern of Level 2 — everything you learned in this course (pipelines, validation, caching) applies directly.

---

# Demo Flow

![Demo flow](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtGcmVzaCBjbG9uZV0gLS0-IEJbRm9sbG93IFJFQURNRV0KICBCIC0tPiBDW1J1biBwaXBlbGluZV0KICBDIC0tPiBEW1Nob3cgYXJ0aWZhY3RzXQogIEQgLS0-IEVbU2hvdyBmYWlsdXJlIGNhc2VdCiAgRSAtLT4gRltTaG93IHRlc3RzIHBhc3Nd)

A demo is successful when **another person can reproduce it**.

---

# Demo Readiness Checklist

### Repository

- [ ] `README.md` with clear instructions
- [ ] `.gitignore` includes `.env`, `__pycache__`, output dirs
- [ ] `requirements.txt` with pinned versions
- [ ] `.env.example` with all required variables (no secrets)
- [ ] Sample data included

### Fresh clone test

- [ ] Clone to new directory
- [ ] Follow README from scratch
- [ ] All commands work without modification

---

# Demo Script (~5 min)

| Step | What to show | Time |
|------|-------------|------|
| 1. **Setup** | README, environment, `.env.example` | 2 min |
| 2. **Happy path** | `python run_capstone.py --input data/sample.csv` | 1 min |
| 3. **Artifacts** | Inspect `03_compressed.json`, `04_llm_raw.json` | 1 min |
| 4. **Failure case** | Missing file error, empty CSV error | 1 min |
| 5. **Tests** | `pytest -v` | 30 sec |

**Key rule**: Run from scratch, never edit code during demo.

---

# Retrospective: Structure

| Section | What to write |
|---------|--------------|
| **What I built** | 3-6 sentence description |
| **What went well** | With evidence (diffs, logs, metrics) |
| **What went wrong** | Top 3 issues: symptom, frequency, impact |
| **Root cause analysis** | Surface cause → deeper cause → lesson |
| **Fixes implemented** | Code changes, tests added, results |
| **Metrics summary** | Before/after comparison |
| **What I would do next** | Level 2 direction |

---

# Retrospective: What Went Wrong

For each issue, document:

| Field | Example |
|-------|---------|
| **Symptom** | Pipeline crashed with `json.JSONDecodeError` |
| **When** | First 3 test runs with real data |
| **Frequency** | 2/10 calls (20%) |
| **Evidence** | `output/04_llm_raw.json` contains partial JSON |
| **Impact** | Entire pipeline fails |

### 5 Whys analysis

1. Why crash? → JSON parse error
2. Why parse error? → LLM returned text after JSON
3. Why extra text? → Prompt wasn't explicit about format
4. Why not explicit? → Assumed "return JSON" was enough
5. Why assume? → Didn't test with diverse inputs

---

# Retrospective: Metrics Summary

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Success rate | 70% | 98% | +40% |
| Avg latency | 45s | 42s | -7% |
| JSON parse failures | 20% | 0% | -100% |
| Test coverage | 45% | 78% | +73% |

**Key lessons**:
- Save intermediate artifacts at every stage
- Validate LLM outputs before using them
- Client-side rate limiting prevents 429s
- Dry-run mode enables fast iteration

---

# Preparing for Level 2

### Mindset shifts

| Foundational Course | Level 2 |
|-------------------|---------|
| Single-file scripts | FastAPI services |
| Static prompts | Dynamic prompts (RAG) |
| Manual inspection | Automated eval metrics |
| One LLM call per run | Multi-step workflows |

---

# Level 2 Preview

| Weeks | Focus | Output |
|-------|-------|--------|
| 1-2 | **RAG Foundation** | API endpoint with vector search |
| 3-4 | **Retrieval Quality** | Measurable precision/recall improvements |
| 5-6 | **Production RAG** | Service with citations + streaming |
| 7-8 | **Evaluation + Iteration** | Data-driven quality improvements |

**New concepts**: Vector databases, embeddings, semantic search, reranking, FastAPI

---

# Skills Bridge to Level 2

### You already have (from Foundational Course)

- Python functions, classes, error handling
- API integration (requests, timeouts, retries)
- JSON parsing and validation
- File I/O and data pipelines
- Testing with pytest

### Review before Level 2

- **Embeddings**: text → numeric vectors for similarity search
- **Async Python**: `asyncio` for concurrent API calls
- **FastAPI**: building REST APIs
- **SQL basics**: metadata filtering

---

# Level 2 Readiness Checklist

- [ ] Can write Python with type hints
- [ ] Comfortable with async/await (or ready to learn)
- [ ] Can debug with logs and artifacts
- [ ] Understand cache vs recompute tradeoffs
- [ ] Can estimate token costs and latency budgets
- [ ] Familiar with git, Docker basics, env vars
- [ ] Treat failures as data, not roadblocks
- [ ] Build evaluation before optimization

---

# Workshop / Deliverables

- **Demo**: Run your capstone live (fresh clone → README → output)
- **Retrospective**: Write `RETROSPECTIVE.md` with:
  - Top 3 issues (with evidence)
  - Root cause analysis
  - Fixes implemented (code + tests)
  - Metrics before/after
  - What you'd do next

---

# Self-Check Questions

- Can a teammate run your demo without asking questions?
- Can you explain what RAG is in one sentence?
- Do you have a failure story with evidence (logs/artifacts)?
- Are you comfortable with the Level 2 readiness checklist?

---

# References

- GitHub READMEs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- Google SRE postmortem culture: https://sre.google/sre-book/postmortem-culture/
- RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/
- FastAPI: https://fastapi.tiangolo.com/

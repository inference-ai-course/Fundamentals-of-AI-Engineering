---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 6 — Capstone Prototype (End-to-End Flow)"
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

# Week 6

## Capstone Prototype (End-to-End Flow)

---

# Learning Objectives

By the end of this week, you should be able to:

- Implement the Capstone "happy path" end-to-end
- Keep prompts within limits by sampling/compressing inputs
- Produce stable artifacts: `report.json` and `report.md`

---

# What is a Data Pipeline?

![Pipeline concept](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtSYXcgbWF0ZXJpYWxzXSAtLT4gQltTdGFnZSAxOiBDbGVhbl0KICBCIC0tPiBDW1N0YWdlIDI6IFNoYXBlXQogIEMgLS0-IERbU3RhZ2UgMzogQXNzZW1ibGVdCiAgRCAtLT4gRVtTdGFnZSA0OiBRdWFsaXR5IGNoZWNrXQogIEUgLS0-IEZbRmluaXNoZWQgcHJvZHVjdF0=)

A **pipeline** = a sequence of stages, each with clear inputs and outputs.

Like a factory assembly line: raw materials → clean → shape → assemble → quality check → finished product. If one stage fails, you know exactly where to look.

---

# Why Compress Data for LLMs?

![bg right:50%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtMYXJnZSBkYXRhc2V0OiAxMDAwMCByb3dzXSAtLT4gQltTYW1wbGUgKyBzdW1tYXJpemVdCiAgQiAtLT4gQ1tDb21wcmVzc2VkOiA1MCByb3dzICsgc3RhdHNdCiAgQyAtLT4gRFtGaXRzIGluIGNvbnRleHQgd2luZG93XQogIEQgLS0-IEVbTExNIGNhbiBwcm9jZXNzIGl0XQ==)

You **cannot** send a full dataset to an LLM — it won't fit in the context window. Instead:
- **Sample** representative rows
- **Summarize** statistics
- Keep under ~2000 tokens

---

# End-to-End Capstone Pipeline

![Capstone pipeline](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtDU1ZdIC0tPiBCW1Byb2ZpbGVdCiAgQiAtLT4gQ1twcm9maWxlLmpzb25dCiAgQiAtLT4gRFtDb21wcmVzcy9zYW1wbGVdCiAgRCAtLT4gRVtjb21wcmVzc2VkLmpzb25dCiAgRSAtLT4gRltMTE0gY2xpZW50XQogIEYgLS0-IEdbVmFsaWRhdGUgKyBmb3JtYXRdCiAgRyAtLT4gSFtyZXBvcnQuanNvbl0KICBHIC0tPiBJW3JlcG9ydC5tZF0=)

---

# Capstone Stages

| Stage | Input | Output |
|-------|-------|--------|
| 1. **Load** | `data/*.csv` | In-memory DataFrame |
| 2. **Profile** | DataFrame | `output/profile.json` |
| 3. **Compress** | DataFrame + profile | `output/compressed.json` |
| 4. **LLM** | Prompt + compressed input | `output/llm_raw.json` |
| 5. **Report** | Validated LLM output | `output/report.json` + `report.md` |

**Key rule**: If a stage fails, previous artifacts are still saved for debugging.

---

# Token Budget Estimation

Keep compressed representation under ~2000 tokens:

| Component | Tokens |
|-----------|--------|
| System prompt | ~100–200 |
| Task instructions | ~50–100 |
| Compressed data | <2,000 |
| Output budget | ~500–1,000 |
| **Total** | Well under model limit |

If too large: reduce sample size or remove verbose fields. Rule of thumb: ~4 characters per token.

---

# Smart Sampling Strategies

**Random sampling** may miss rare-but-important cases.

| Strategy | When to use |
|----------|-------------|
| **Random sample** | General purpose, no specific requirements |
| **Stratified sample** | Must represent all categories |
| **Include extremes** | Outlier detection matters |
| **Top-k categories** | Categorical distribution matters |

**Design choices**: fixed `seed` for stability, `sort_keys=True` for deterministic JSON.

---

# Chunking Long Text

![Chunking](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtMb25nIHRleHRdIC0tPiBCW1NwbGl0IGludG8gY2h1bmtzXQogIEIgLS0-IENbQ2h1bmsgMV0KICBCIC0tPiBEW0NodW5rIDJdCiAgQiAtLT4gRVtDaHVuayBOXQogIEMgLS0-IEZbUHJvY2VzcyBlYWNoXQogIEQgLS0-IEYKICBFIC0tPiBGCiAgRiAtLT4gR1tTeW50aGVzaXplIGZpbmFsIG91dHB1dF0=)

When text exceeds the context window: **split → process each chunk → synthesize**.

**Overlap** between chunks prevents losing information at boundaries.

---

# One-Command Runner

Your capstone should run with **one command**:

`python run_capstone.py --input data.csv`

| Flag | Purpose | Default |
|------|---------|---------|
| `--input` | Input CSV (required) | — |
| `--output_dir` | Output directory | `output` |
| `--model` | LLM model name | `gpt-4o-mini` |
| `--sample_size` | Rows to sample | 5 |
| `--seed` | Random seed | 42 |
| `--dry-run` | Skip LLM call | off |

**Dry-run mode**: test the entire pipeline without calling the LLM.

---

# Artifact Naming Convention

| File | Stage | Purpose |
|------|-------|---------|
| `01_loaded.parquet` | 1 | Loaded data |
| `02_profile.json` | 2 | Data profile |
| `03_compressed.json` | 3 | Compressed input for LLM |
| `04_llm_raw.json` | 4 | Raw LLM response |
| `05_report.json` | 5 | Final structured report |
| `05_report.md` | 5 | Human-readable report |

**Why numbered prefixes**: clear execution order, easy to see "how far did the pipeline get?"

---

# Debugging with Artifacts

| Scenario | What to do |
|----------|-----------|
| LLM call fails | Inspect `03_compressed.json`, re-run only stage 4 |
| Profile looks wrong | Check `02_profile.json` against expectations |
| Want to modify compression | Load from `01_loaded.parquet`, skip stage 1 |
| Prompt needs tuning | Read `04_llm_prompt.txt`, adjust, re-call |

**Cost control**: Don't re-call expensive LLM on every debug iteration — use saved artifacts.

---

# Workshop / Deliverables

Implement the full flow:
- CSV → profiling → sampling/compression → LLM call → `report.json` + `report.md`
- Ensure the entire pipeline runs with **one command**
- Save intermediate artifacts at each stage

**Required outputs**: `report.json` (structured) + `report.md` (human-readable)

---

# Self-Check Questions

- Can you identify which stage fails when something breaks?
- Can you re-run and get stable `report.json` fields?
- Do you save intermediate outputs to help debugging?
- Can a teammate run your pipeline without asking questions?

---

# References

- Twelve-Factor methodology: https://12factor.net/
- Neptune.ai ML Pipelines: https://neptune.ai/blog/building-end-to-end-ml-pipeline
- Valohai ML Pipeline: https://valohai.com/machine-learning-pipeline/
- tiktoken: https://github.com/openai/tiktoken

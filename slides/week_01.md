---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 1 — Environment Setup & Data Processing"
style: |
  section { font-size: 24px; }
  pre { font-size: 18px; }
  code { font-size: 18px; }
  h1 { color: #0f3460; border-bottom: 3px solid #00d2ff; padding-bottom: 8px; }
  h2 { color: #16213e; }
  table { font-size: 20px; }
  img { max-height: 350px; display: block; margin: 0 auto; }
  section.lead { text-align: center; background: linear-gradient(135deg, #0f3460, #16213e); color: #e8e8e8; }
  section.lead h1 { color: #00d2ff; border: none; font-size: 48px; }
  section.lead h2 { color: #e8e8e8; font-weight: 400; }
---

<!-- _class: lead -->

# Week 1

## Environment Setup & Data Processing Basics

---

# Learning Objectives

By the end of this week, you should be able to:

- Create a clean Python environment and install dependencies reliably
- Run a project from a README on a fresh machine (or fresh folder)
- Build a small "data profiling" script that reads a CSV and produces reproducible outputs

---

# What is AI Engineering?

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgRFtEYXRhXSAtLT4gUFtQaXBlbGluZV0KICBNW01vZGVscyAvIExMTXNdIC0tPiBQCiAgSVtJbmZyYXN0cnVjdHVyZV0gLS0-IFAKICBQIC0tPiBPW1JlbGlhYmxlIEFJIFN5c3RlbV0=)

AI Engineering = building **reliable systems** that use AI models (including LLMs).

It's not just about the model — it's about **data quality**, **reproducible pipelines**, and **stable infrastructure** around the model.

---

# What This Course Builds

![h:120](https://mermaid.ink/img/Zmxvd2NoYXJ0IExSCiAgVzFbV2VlayAxLTI6IEZvdW5kYXRpb25zXSAtLT4gVzJbV2VlayAzLTU6IExMTSBBUElzXQogIFcyIC0tPiBXM1tXZWVrIDYtODogQ2Fwc3RvbmVd)

- **Week 1**: Environment + data profiling
- **Weeks 2–5**: ML, LLM APIs, local inference
- **Weeks 6–8**: Pipeline, testing, demo

---

# Why This Matters for LLM Projects

LLMs are powerful, but **they don't fix bad engineering**:

| Without engineering discipline | With engineering discipline |
|-------------------------------|---------------------------|
| "Works on my laptop" | Reproducible on any machine |
| Feeding garbage data to LLM | Profiled, validated data → better prompts |
| Can't explain what changed | Artifact trail for every run |
| Random failures | Controlled, debuggable pipeline |

> Every skill this week — environments, data profiling, reproducibility — directly applies when you build LLM-powered systems in later weeks.

---

# What is Data Profiling?

**Data profiling** = understanding your data *before* using it: row counts, column types, missing values, distributions.

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQkRbRGlydHkgZGF0YV0gLS0-IEJNW01vZGVsIHRyYWluZWQgb24gbm9pc2VdCiAgQk0gLS0-IEJPW1dyb25nIHByZWRpY3Rpb25zXQogIEJPIC0tPiBIW0hhbGx1Y2luYXRpb25zXQ==)

### Without profiling (bad path)

Dirty data → model trained on noise → wrong predictions → hallucinations.

Each arrow is a point where profiling could have caught the problem **early**.

---

# Data Quality → AI Quality

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgR0RbUHJvZmlsZWQgKyBjbGVhbmVkIGRhdGFdIC0tPiBHTVtNb2RlbCBvbiBxdWFsaXR5IGRhdGFdCiAgR00gLS0-IEdPW1JlbGlhYmxlIG91dHB1dHNdCiAgR08gLS0-IFRbVHJ1c3R3b3J0aHkgcmVzdWx0c10=)

### With profiling (good path)

Profiled + cleaned data → model on quality data → reliable outputs → trustworthy results.

**For LLM work**: bad data → bad prompts → hallucinations. Profile **early** to avoid expensive failures.

---

# Without Isolation: Version Conflicts

![h:280](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQTFbb3BlbmFpPT0wLjI4XSAtLT4gWFtWZXJzaW9uIGNvbmZsaWN0XQogIEEyW29wZW5haT09MS42XSAtLT4gWAogIEEzW3Rpa3Rva2VuIG1pc21hdGNoXSAtLT4gWAogIFggLS0-IEJbQ29kZSBicmVha3Nd)

LLM libraries change **fast** — `openai` had a breaking API change from v0.x to v1.x.

---

# With Isolation: Each Project is Safe

![h:280](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgVjFbUHJvamVjdCBBIHZlbnZdIC0tPiBPMVtvcGVuYWk9PTAuMjhdCiAgVjJbUHJvamVjdCBCIHZlbnZdIC0tPiBPMltvcGVuYWk9PTEuNl0KICBPMSAtLT4gVzFbV29ya3NdCiAgTzIgLS0-IFcyW1dvcmtzXQ==)

**Pinned versions + isolated venvs** = safety net. Each project has its own dependency versions.

---

# Environment Setup: venv

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtTeXN0ZW0gUHl0aG9uXSAtLT4gQltDcmVhdGUgdmVudl0KICBCIC0tPiBDW0FjdGl2YXRlXQogIEMgLS0-IERbSW5zdGFsbCBkZXBzXQogIEQgLS0-IEVbRnJlZXplIHJlcXVpcmVtZW50cy50eHRdCiAgRSAtLT4gRltSdW4gc2NyaXB0XQ==)

System Python → create venv → activate → install deps → freeze `requirements.txt` → run script.

**Key**: always activate before `pip install`, always freeze after installing.

---

# Environment Setup: Conda

![h:280 Anaconda Distribution](https://www.pngkey.com/png/detail/85-851355_anaconda-distribution-diagram-anaconda-python-libraries.png)

Same pattern as venv — different tool, same discipline.

Base conda → create env → activate → install deps → export `environment.yml` → run script.

---

# The "Fresh Machine" Test

The gold standard: can someone recreate your project from scratch?

| Step | What to do | Success looks like |
|------|-----------|-------------------|
| 1. Create venv | `python -m venv .venv` | New `.venv/` directory |
| 2. Activate | `source .venv/bin/activate` | `which python` → `.venv/bin/python` |
| 3. Install | `pip install -r requirements.txt` | No errors |
| 4. Verify | `python -c "import pandas"` | No ImportError |

**Pin versions** in `requirements.txt`:
```txt
pandas==2.2.3
scikit-learn==1.5.2
openai==1.6.1
```

---

# Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Installing outside env | "Works on my machine" | Always activate before `pip install` |
| Forgetting to record deps | Can't recreate env | `pip freeze > requirements.txt` after install |
| Version drift | "Worked last week" | Pin versions explicitly |
| Platform-specific deps | Fails on other OS | Document system deps separately |

**Diagnosis**: Always check `which python` — should point to your `.venv/`, not `/usr/bin/python`.

---

# Data Profiling Pipeline

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtJbnB1dCBDU1ZdIC0tPiBCe1ZhbGlkYXRlfQogIEIgLS0-fG1pc3NpbmcvZW1wdHl8IENbRmFpbCB3aXRoIGNsZWFyIGVycm9yXQogIEIgLS0-fG9rfCBEW0NvbXB1dGUgc3RhdHNdCiAgRCAtLT4gRVtwcm9maWxlLmpzb24gKyBwcm9maWxlLm1kXQ)

**Defensive programming**: validate early, fail fast.

- If file is missing → clear `FileNotFoundError`
- If file is empty → clear `ValueError`
- If validation passes → compute stats and write reproducible outputs

---

# Data Profiling for LLM Pipelines

In later weeks, you will **compress** data and send it to an LLM for analysis.

| What profiling catches | What happens if you miss it |
|----------------------|---------------------------|
| Missing values (40% of a column) | LLM hallucinates values to fill gaps |
| Wrong column types (dates as strings) | LLM misinterprets the data |
| Unexpected encoding | Garbled text in the prompt |
| Empty dataset | Wasted API call + confusing output |

**Rule**: Profile first, send to LLM second. The profiling habit you build this week is the foundation for every LLM pipeline later.

---

# Reproducibility: Why It Matters

**Reproducibility** = run the same command twice → get **identical** outputs.

| Concept | How we enforce it |
|---------|------------------|
| Deterministic outputs | `sort_keys=True` in JSON |
| Stable environment | Pinned `requirements.txt` |
| Controlled inputs | Explicit `--input` flag |
| Traceable outputs | All artifacts in `output/` directory |

**For LLM work**: When you later compare prompt strategies or model versions, reproducibility lets you **isolate what changed** — was it the data, the prompt, or the model?

---

# Workshop / Deliverables

Implement `data_profile.py`:

- **Input**: `--input path/to.csv`
- **Output**: write files to `output/`
- **Error handling**: clear errors for missing file / empty file / missing columns

**Extensions** (recommended):
- `--required_columns colA,colB` — fail if missing
- Numeric summaries (min/max/mean)
- Frequent values for categorical columns (top 5)

---

# Self-Check Questions

- Can you recreate your environment from scratch using only `requirements.txt`?
- Can you explain **why** environments prevent dependency conflicts?
- If you delete `.venv`, can you recreate it and run the project?
- If the input file is missing, do you get a clear error?
- Can you explain how data profiling helps LLM-based analysis later?

---

# References

- Python `venv`: https://docs.python.org/3/library/venv.html
- pip user guide: https://pip.pypa.io/en/stable/user_guide/
- Conda environments: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
- Pandas getting started: https://pandas.pydata.org/docs/getting_started/index.html

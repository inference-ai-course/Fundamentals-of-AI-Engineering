---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 1 — Environment Setup & Data Quality"
style: |
  @import 'theme.css';
---

<!-- _class: lead -->

# Week 1

## Environment Setup & Data Quality Basics

---

# Learning Objectives

By the end of this week, you should be able to:

- Create a clean Python environment and install dependencies reliably
- Run a project from a README on a fresh machine (or fresh folder)
- Build a data quality profiling script that reads a CSV and produces reproducible outputs

---

# What is AI Engineering?

![bg right:50% h:320](images/concepts/ai_ml_dl.svg)
<div style="position: absolute; bottom: 20px; right: 20px; font-size: 12px; color: #666;">Source: Wikimedia Commons (AI-ML-DL.svg)</div>

AI Engineering = building **reliable systems** that use AI models (including LLMs).

It's not just about the model — it's about **data quality**, **reproducible pipelines**, and **stable infrastructure** around the model.

---

# What This Course Builds

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

# What is Data Quality Profiling?

**Data profiling** = systematically assessing data quality *before* using it (structure, completeness, consistency).

**Key checks**: row counts, column types, missing values (%), distributions, outliers, duplicates.

![bg right:40% h:320](images/concepts/data_profiling.png)

### Without profiling (bad path)

Dirty data → model trained on noise → wrong predictions → hallucinations.

Each arrow is a point where profiling could have caught the problem **early**.

---

# Data Quality → AI Quality

![bg right:40% h:320](images/concepts/machine_learning.png)
<div style="position: absolute; bottom: 20px; right: 20px; font-size: 12px; color: #666;">Source: Wikimedia Commons (Concept of machine learning.png)</div>

### With profiling (good path)

Profiled + cleaned data → model on quality data → reliable outputs → trustworthy results.

**For LLM work**: bad data → bad prompts → hallucinations. Profile **early** to avoid expensive failures.

---

# Without Isolation: Version Conflicts

![h:280](images/concepts/traditional_programming.png)
<div style="position: absolute; bottom: 20px; right: 20px; font-size: 12px; color: #666;">Source: Wikimedia Commons (Concept of traditional computer applications.png)</div>

LLM libraries change **fast** — `openai` had a breaking API change from v0.x to v1.x.

---

# With Isolation: Each Project is Safe

**Pinned versions + isolated venvs** = safety net. Each project has its own dependency versions.

---

<!-- _class: part -->

# Part 01
## Environment Setup + Dependency Management

`week_01/01_environment_setup.md` · `01_environment_setup.ipynb`

---

# Environment Setup: venv

System Python → create venv → activate → install deps → freeze `requirements.txt` → run script.

**Key**: always activate before `pip install`, always freeze after installing.

---

# Environment Setup: Conda

![h:360 Anaconda Distribution](https://www.pngkey.com/png/detail/85-851355_anaconda-distribution-diagram-anaconda-python-libraries.png)

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

<!-- _class: part -->

# Part 02
## Data Quality Profiling Script

`week_01/02_data_profiling_script.md` · `02_data_profiling_script.ipynb`

---

# Data Quality Profiling Pipeline

**Defensive programming**: validate early, fail fast.

- If file is missing → clear `FileNotFoundError`
- If file is empty → clear `ValueError`
- If validation passes → compute stats and write reproducible outputs

---

# Data Quality Profiling for LLM Pipelines

In later weeks, you will **compress** data and send it to an LLM for analysis.

| What profiling catches | What happens if you miss it |
|----------------------|---------------------------|
| Missing values (40% of a column) | LLM hallucinates values to fill gaps |
| Wrong column types (dates as strings) | LLM misinterprets the data |
| Unexpected encoding | Garbled text in the prompt |
| Empty dataset | Wasted API call + confusing output |

**Rule**: Profile first, send to LLM second. The data quality profiling habit you build this week is the foundation for every LLM pipeline later.

---

# Reproducibility: Why It Matters

**Reproducibility** = run the same command twice → get **identical** outputs.

| Concept | How we enforce it |
|---------|------------------|
| Deterministic outputs | `sort_keys=True` in JSON |
| Stable environment | Pinned `requirements.txt` |
| Controlled inputs | Explicit `--input` flag |
| Traceable outputs | All artifacts in `output/` directory (audit trail) |

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

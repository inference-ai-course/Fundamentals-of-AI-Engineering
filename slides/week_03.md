---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 3 — Environment + Data Processing"
style: |
  @import 'theme.css';
---

<!-- _class: lead -->

# Week 3

## Environment + Data Processing

---

# Learning Objectives

By the end of this week, you should be able to:

- Create a clean Python environment
- Install and record dependencies
- Load CSV data with pandas
- Generate `profile.json` and `profile.md`
- Explain data quality findings in plain language

---

# Why Data Comes First

![bg right:40% h:320](images/concepts/data_profiling.svg)

AI systems are only as useful as the data they receive.

- Bad data -> unreliable model or LLM output
- Unknown missing values -> misleading conclusions
- Unclear inputs -> impossible debugging

**Week 3 habit**: profile first, model second.

---

# Environment Setup

Reproducible projects start with isolated environments.

| Step | Example |
|------|---------|
| Create | `python -m venv .venv` |
| Activate | `source .venv/bin/activate` |
| Install | `pip install -r requirements.txt` |
| Record | `pip freeze > requirements.txt` |
| Verify | `python -c "import pandas"` |

---

# Fresh Machine Test

Can another student reproduce your work from the README?

They should know:

- Python version
- Dependencies
- Exact command to run
- Input CSV path
- Expected output files

---

# Data Profiling Checks

Your profiler should report:

- Row and column counts
- Column names and inferred types
- Missing value counts
- Duplicate row count
- Basic numeric statistics (min, max, mean)
- Top categorical values (top 5 per column)

---

# Output Contract

The Week 3 output is intentionally simple:

```text
input.csv
  -> output/profile.json
  -> output/profile.md
```

`profile.json` is for code.
`profile.md` is for humans.

---

# Profiling Pipeline

```text
   CSV file
      |
  Load & Validate
      |
  Compute Profile
   /        \
profile.json  profile.md
```

Each step should fail fast with a clear error if something is wrong.

---

# Workshop

Use the Week 3 tutorials:

- Environment setup
- Dependency management
- CSV loading with pandas
- Data profiling script
- JSON and Markdown outputs

---

# What to Complete

- Runnable data profiling script
- `output/profile.json`
- `output/profile.md`
- Short report with at least 3 findings
- README with setup and run commands
- Manual test checklist or automated tests

---

# Self-Check

- Can someone reproduce your outputs from your README?
- What input file produced the report?
- What is your most important data quality finding?
- Did you verify the output instead of trusting AI blindly?

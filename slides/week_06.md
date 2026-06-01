---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 6 — Intelligent Data Analysis Capstone"
style: |
  @import 'theme.css';
---

<!-- _class: lead -->

# Week 6

## Intelligent Data Analysis Capstone

---

# Capstone Goal

Build a reproducible script that turns CSV data into an AI-assisted report.

```text
CSV input
  -> data overview
  -> sampled/compressed summary
  -> LLM interpretation
  -> report.json + report.md
```

---

# Learning Objectives

By the end of this week, you should be able to:

- Reuse Week 3 data profiling
- Reuse Week 4 structured prompts and reliability controls
- Apply Week 5 data/ML intuition to explain patterns
- Produce stable JSON and readable Markdown
- Demo a reproducible run

---

# MVP Scope

Your project must:

- Accept a CSV path
- Compute data overview statistics
- Avoid sending the full dataset to the LLM
- Generate structured insights and recommendations
- Write `report.json`
- Write `report.md`
- Include README and a short postmortem

---

# Data Overview

Include:

- column types
- missing values
- duplicate rows
- numeric summaries
- categorical summaries
- simple anomaly hints

This is traditional analysis before LLM interpretation.

---

# Sampling and Compression

Do not paste the whole dataset into the model.

Send a compact summary:

- schema
- row/column counts
- selected statistics
- representative samples
- anomaly hints

The LLM interprets the summary, not the raw full CSV.

---

# Structured LLM Interpretation

Ask for a stable shape:

```json
{
  "insights": [],
  "recommendations": [],
  "risk_notes": []
}
```

Then validate the fields before building the final report.

---

# Suggested Structure

```text
analyze.py
src/
  data_profile.py
  sampling.py
  llm_client.py
  report_builder.py
output/
README.md
requirements.txt
postmortem.md
prompts.md
```

Keep it simple and runnable.

---

# What to Complete

- Script or notebook that runs the MVP
- `output/report.json` as the machine-readable result
- `output/report.md` as the human-readable result
- README with one-command run instructions
- Sample input or dataset link
- Short `postmortem.md`: one issue and how you handled it
- Prompt and AI usage notes

---

# Stretch Goals

Optional only:

- charts in the Markdown report
- Excel input
- hosted API + Ollama backend switch
- input-hash caching
- report style flags

Do the MVP first.

---

# Demo Checklist

Show:

- input CSV
- command used
- output files
- one insight from the report
- one issue you handled
- what you would improve next

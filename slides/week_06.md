---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 6 — AI-Assisted CSV Data Analyzer"
style: |
  @import 'theme.css';
---

<!-- _class: lead -->

# Week 6

## AI-Assisted CSV Data Analyzer

---

# Capstone Goal

Build a reproducible project that turns CSV data into an AI-assisted report through a **real LLM call**.

```text
CSV input
  -> data overview
  -> sampled/compressed summary
  -> real LLM interpretation
  -> report.json + report.md
```

---

# Learning Objectives

By the end of this week, you should be able to:

- Reuse Week 3 data profiling
- Reuse Week 4 structured prompts, real LLM calls, and reliability controls
- Apply Week 5 data/ML intuition to explain patterns
- Produce stable JSON and readable Markdown
- Demo a reproducible run

---

# MVP Scope

Your project must:

- Accept a CSV path
- Compute data overview statistics
- Avoid sending the full dataset to the LLM
- Call a real LLM for structured insights and recommendations
- Write `report.json`
- Write `report.md`
- Include README and a short postmortem

---

# Topic Choices

Default:

- General CSV data analyzer

Recommended:

- Customer feedback / support ticket analyzer
- Product review insight reporter

Keep the same CSV -> JSON + Markdown contract.

---

# Real LLM Requirement

Final submission must include:

- A real LLM call
- Saved prompt
- Saved raw or validated response
- Timeout/retry or repair attempt
- Clear failure message

Mock responses are for debugging only.

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

Ask for stable report fields:

```json
{
  "metadata": {},
  "dataset_summary": {},
  "data_quality": {},
  "compression_summary": {},
  "llm_interpretation": {},
  "recommendations": [],
  "risk_notes": [],
  "errors_or_warnings": []
}
```

Then validate the fields before building the final report.

---

# Template Structure

```text
capstone_template/
analyze.py
src/
  data_profile.py
  compression.py
  llm_interpretation.py
  report_builder.py
README.md
requirements.txt
postmortem.md
prompts.md
```

The template has TODOs. It is not a full answer.

---

# Template Walkthrough

Students complete:

- `build_profile()`
- `compress_profile()`
- `build_prompt()`
- `call_llm()`
- `validate_llm_output()`
- `build_json_report()`
- `build_markdown_report()`

AI Agent Coding Tools are allowed, but usage must be documented.

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
- evidence of real LLM call
- one insight from the report
- one issue you handled
- what you would improve next

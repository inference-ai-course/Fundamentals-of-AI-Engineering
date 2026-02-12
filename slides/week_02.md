---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 2 — ML Training Loop & Reproducible Baselines"
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

# Week 2

## The ML Training Loop + Reproducible Baselines

---

# Learning Objectives

By the end of this week, you should be able to:

- Explain why we split data into train/validation
- Train a baseline model, evaluate it, and save artifacts
- Compare two runs and write a short failure retrospective

---

# What is Machine Learning?

### Traditional Programming

![h:250 Traditional](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgUltIdW1hbiB3cml0ZXMgcnVsZXNdIC0tPiBQW1Byb2dyYW1dCiAgRFtEYXRhXSAtLT4gUAogIFAgLS0-IE9bT3V0cHV0XQ==)

Human writes rules → computer follows them.

---

# Machine Learning: The Key Difference

![bg right:28%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgRFtEYXRhICsgZXhwZWN0ZWQgb3V0cHV0XSAtLT4gTFtMZWFybmluZyBhbGdvcml0aG1dCiAgTCAtLT4gTVtNb2RlbF0KICBNIC0tPiBQW05ldyBwcmVkaWN0aW9uc10=)

### Machine Learning

Computer **learns** rules from data + expected outputs. A **model** is the result — a program that was learned, not hand-written.

An **LLM** (Large Language Model) is a very large ML model trained on massive text data. The same ML discipline applies.

---

# What is Training?

![bg right:33%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtUcmFpbmluZyBEYXRhOiB0aG91c2FuZHMgb2YgZXhhbXBsZXNdIC0tPiBCW01vZGVsIHNlZXMgZXhhbXBsZXNdCiAgQiAtLT4gQ1tBZGp1c3RzIGludGVybmFsIHdlaWdodHNdCiAgQyAtLT4gRHtDaGVjazogcHJlZGljdGlvbnMgY29ycmVjdD99CiAgRCAtLT58bm90IHlldHwgQgogIEQgLS0-fGdvb2QgZW5vdWdofCBFW1RyYWluZWQgTW9kZWxdCiAgRSAtLT4gRltVc2UgZm9yIG5ldyBwcmVkaWN0aW9uc10=)

**Training** = the process where a model learns from data by adjusting its internal parameters (weights).

- The model sees thousands of examples
- It makes predictions and checks if they're correct
- It adjusts weights to reduce errors
- Repeats until "good enough"

---

# From ML to LLM: Classical ML

![bg right:28%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgRDFbVGFidWxhciBkYXRhXSAtLT4gVDFbVHJhaW4gY2xhc3NpZmllcl0KICBUMSAtLT4gUDFbUHJlZGljdCBsYWJlbHNdCiAgUDEgLS0-IE0xW1NhdmUgbWV0cmljc10=)

Classical ML: train a model on structured data, predict labels.

Tabular data → train classifier → predict labels → save metrics.

---

# From ML to LLM: LLM-Augmented Pipeline

![bg right:30%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgRDJbVGV4dCAvIENTViBkYXRhXSAtLT4gQ1tDb21wcmVzcyArIHByb2ZpbGVdCiAgQyAtLT4gTFtMTE0gQVBJIGNhbGxdCiAgTCAtLT4gVltWYWxpZGF0ZSBvdXRwdXRdCiAgViAtLT4gUltSZXBvcnQgLyBpbnNpZ2h0c10=)

LLM-augmented: compress data, call LLM API, validate output.

**Different tools, same discipline.**

---

# Shared Discipline: ML ↔ LLM

![bg right:30%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgUzFbUmVwcm9kdWNpYmlsaXR5XSAtLT4gQltCb3RoIE1MIGFuZCBMTE1dCiAgUzJbQXJ0aWZhY3Qgc2F2aW5nXSAtLT4gQgogIFMzW1RyYWluL3ZhbCBzcGxpdF0gLS0-IEIKICBTNFtNZXRyaWNzIGNvbXBhcmlzb25dIC0tPiBC)

Even if you **don't train the LLM yourself**, you still need ML discipline:

- **Train/val splits** → test prompt effectiveness on held-out data
- **Artifact saving** → save prompts, outputs, configs for every run
- **Metrics comparison** → compare LLM outputs across prompt changes

---

# The ML Training Loop

![bg right:33%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtMb2FkICsgc3BsaXQgZGF0YV0gLS0-IEJbVHJhaW4gbW9kZWxdCiAgQiAtLT4gQ1tFdmFsdWF0ZSBvbiB2YWxpZGF0aW9uXQogIEMgLS0-IERbU2F2ZSBhcnRpZmFjdHNdCiAgRCAtLT4gRVtDb21wYXJlIHJ1bnNd)

Load → split → train → predict → compute metrics → save artifacts → compare runs.

Artifacts saved at each run:
- `config.json`
- `metrics.json`
- `model.joblib`
- `val_report.txt`

---

# The Loop: Step by Step

| Step | What you do | Why it matters |
|------|------------|---------------|
| 1. **Load data** | Read CSV into a table | Rows = examples, columns = features |
| 2. **Split train/val** | Separate learning data from test data | Prevents measuring on data the model has already seen |
| 3. **Train** | Fit a model on training data | Model learns patterns |
| 4. **Evaluate** | Predict on validation data | Honest estimate of real-world performance |
| 5. **Save artifacts** | Store config + metrics + model | Creates evidence trail for every experiment |

Even for LLM work, this disciplined loop is the basis for evaluating prompt/model changes.

---

# Overfitting: The Core Trap

![bg right:30%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtUcmFpbmluZyBiZWdpbnNdIC0tPiBCW0JvdGggbWV0cmljcyBpbXByb3ZlXQogIEIgLS0-IENbVmFsIG1ldHJpYyBwZWFrc10KICBDIC0tPiBEW1ZhbCBkZWNsaW5lcyB3aGlsZSB0cmFpbiBpbXByb3Zlc10KICBEIC0tPiBFW0dhcCA9IG92ZXJmaXR0aW5nIHNpZ25hbF0)

**Overfitting** = the model memorizes training data instead of learning general patterns.

- Training metrics keep improving, but validation metrics **decline**
- **Analogy**: a student who memorizes answers but can't solve new problems
- **LLM parallel**: a prompt that works perfectly on your test case but fails on new inputs

---

# Reproducibility Package

Reproducibility means:
- Run the same command twice → results are **identical** (or explainably close)
- A teammate can reproduce your metrics from your command + config

### The four habits

| Habit | What it does | LLM parallel |
|-------|-------------|-------------|
| **Control randomness** | `random_state=42` | Fixed seed for sampling |
| **Parameterize runs** | `--seed`, `--max_iter` as flags | `--model`, `--temperature` as flags |
| **Save artifacts** | `config.json` + `metrics.json` | Prompt + response + latency |
| **Use run IDs** | `run_20260210_073204/` | Timestamped output folders |

---

# Saving Artifacts: The Audit Trail

Every run should produce a traceable folder:

| Artifact | What it answers |
|----------|----------------|
| `config.json` | "What did I try?" (parameters, seed, model) |
| `metrics.json` | "What happened?" (accuracy, F1, latency) |
| `val_report.txt` | "Detailed breakdown?" (per-class performance) |
| `model.joblib` | "Can I reproduce predictions later?" |

**For LLM work**: replace `model.joblib` with saved prompts and raw responses — same principle, different artifacts.

---

# Comparing Runs

A useful experiment changes **one variable** at a time.

| | Baseline | Variant |
|---|---------|---------|
| **seed** | 42 | 42 (same) |
| **max_iter** | 200 | **1000** (changed) |
| **accuracy** | 0.82 | 0.85 |
| **F1** | 0.79 | 0.83 |
| **training time** | 2s | 8s |

**Ask**: Did accuracy/F1 improve? Did runtime increase? Is the improvement large enough to matter?

**LLM parallel**: change one thing (model, temperature, prompt wording) and compare outputs.

---

# Writing a Report

A good report is short and structured:

| Section | What to write |
|---------|--------------|
| **Goal** | What you tried to improve |
| **Change** | Exactly what you changed (one variable) |
| **Result** | Metrics before/after |
| **Interpretation** | Why you think it changed |
| **Failure retrospective** | One run that didn't work + what you learned |
| **Next experiment** | One clear idea |

**Two rules**: always include exact commands, always point to artifact folders.

---

# Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Evaluating on training data | Always compute metrics on **validation** set |
| Changing multiple variables at once | Change one thing per experiment |
| Not saving the config | Save `config.json` every run |
| Overwriting previous runs | Use per-run folders with timestamps |
| Treating one metric as truth | Include at least accuracy **and** F1 |

---

# Workshop / Deliverables

- Implement `train.py` (parameterized: `--input`, `--label_col`, `--seed`)
- Run **2 experiments**: change one hyperparameter or switch models
- Write `report.md`:
  - What you changed
  - What happened (metrics)
  - One failed run + your next experiment idea

---

# Self-Check Questions

- Can you explain overfitting without using equations?
- If someone runs your command twice, will results be identical or explainably close?
- Can you point to the saved artifact that proves your reported metric?
- Can you explain how ML discipline (train/val, artifacts, metrics) applies to LLM work?

---

# References

- scikit-learn getting started: https://scikit-learn.org/stable/getting_started.html
- Controlling randomness: https://scikit-learn.org/stable/common_pitfalls.html#controlling-randomness
- Model evaluation: https://scikit-learn.org/stable/modules/model_evaluation.html
- F1 score: https://en.wikipedia.org/wiki/F1_score

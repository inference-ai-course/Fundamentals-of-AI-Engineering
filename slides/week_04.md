---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 4 — LLM Fundamentals + API Reliability"
style: |
  @import 'theme.css';
---

<!-- _class: lead -->

# Week 4

## LLM Fundamentals + API Reliability

---

# Learning Objectives

By the end of this week, you should be able to:

- Explain tokens and context windows
- Design prompts as contracts
- Produce and validate structured outputs
- Add basic timeout, retry, and logging practices
- Use one working LLM path: hosted API or local inference

---

# What is an LLM Call?

![bg right:40% h:380](images/concepts/api_diagram.svg)

Your code sends:

- instructions
- user input
- optional context

The model returns generated text. Your code must parse, validate, and handle failures.

---

# Tokens and Context Windows

An LLM processes tokens, not "thoughts."

- Token count affects cost and latency
- Context window limits how much input fits
- Long inputs can cause ignored instructions or truncated JSON

**Capstone connection**: do not send the whole CSV to the LLM.

---

# Prompt as Contract

A reliable prompt specifies:

| Component | Purpose |
|-----------|---------|
| Role | What the model is doing |
| Task | What to produce |
| Input format | What data is provided |
| Output schema | Exact JSON keys |
| Constraints | No markdown, no extra prose |
| Fallback | What to do when data is missing |

---

# Structured Output Flow

```text
raw input
  -> prompt contract
  -> LLM call
  -> raw output
  -> parse JSON
  -> validate expected fields
  -> save result
```

Each step can fail independently.

---

# Common Failure Modes

| Failure | Beginner-friendly fix |
|---------|-----------------------|
| Invalid JSON | Repair prompt + bounded retry |
| Markdown around JSON | "Return only valid JSON" |
| Missing fields | Validate required keys |
| Timeout | Set max wait |
| Rate limit | Retry after delay |
| Unknown error | Save raw response + readable message |

---

# Reliability Minimum

For Week 4, "reliable enough" means:

- timeout or max wait
- retry limit or repair attempt
- clear error message
- saved raw responses or logs
- no infinite retries

This is not production engineering yet; it is disciplined beginner practice.

---

# Main Topics

- Tokens and context windows
- Prompt contracts
- Structured outputs and validation
- Timeouts and failure modes
- Bounded retries or repair attempts
- Simple logging and saved raw responses

Optional: Ollama or local-vs-cloud benchmarking.

---

# What to Complete

- Structured-output demo
- At least 3 test inputs and outputs
- Prompt contract
- Simplified LLM client or reliability notes
- Short reflection on one failure mode

Hosted API or local inference is enough. Benchmarking both is optional.

---

# Self-Check

- Why might strict JSON still fail?
- What is your retry limit?
- What raw output did you save for debugging?
- What will your code do when the model call fails?

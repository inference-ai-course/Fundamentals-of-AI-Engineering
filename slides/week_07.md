---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 7 — Capstone Engineering & Quality"
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

# Week 7

## Capstone Engineering & Quality

---

# Learning Objectives

By the end of this week, you should be able to:

- Finalize your CLI so the whole capstone runs with one command
- Handle errors that teach the user what to do
- Write tests that cover happy path, edge case, and failure case

---

# What is a CLI?

![CLI concept](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtVc2VyIHR5cGVzIGNvbW1hbmRdIC0tPiBCW1BhcnNlciByZWFkcyBhcmd1bWVudHNdCiAgQiAtLT4gQ1tWYWxpZGF0ZSBpbnB1dHNdCiAgQyAtLT4gRFtSdW4gcGlwZWxpbmUgbG9naWNdCiAgRCAtLT4gRVtXcml0ZSBvdXRwdXRzXQogIEUgLS0-IEZbU2hvdyByZXN1bHRd)

**CLI** (Command-Line Interface) = how users interact with your tool via terminal commands.

A good CLI makes **correct usage easy** and **incorrect usage obvious** — descriptive `--help`, sensible defaults, clear errors.

---

# The Testing Pyramid

![Test pyramid](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtVbml0IHRlc3RzOiBtYW55LCBmYXN0XSAtLT4gQltJbnRlZ3JhdGlvbiB0ZXN0czogZmV3ZXJdCiAgQiAtLT4gQ1tTbW9rZSB0ZXN0OiBvbmUgZW5kLXRvLWVuZF0=)

- **Unit tests** (many): test individual functions — fast, isolated
- **Integration tests** (fewer): test components together
- **Smoke test** (one): end-to-end run — does it work at all?

For LLM projects: **mock the LLM** in unit tests, only call real APIs in smoke tests.

---

# CLI Design: Your Interface Contract

| Requirement | Why |
|-------------|-----|
| Descriptive `--help` | Users know what flags exist |
| Sensible defaults | README copy-paste works |
| Explicit inputs/outputs | No hidden assumptions |
| Clear error on invalid input | Users fix mistakes fast |

### Key flags for capstone

| Flag | Purpose |
|------|---------|
| `--input` | Input CSV (required) |
| `--output_dir` | Output directory (default: `output`) |
| `--model` | LLM model name |
| `--dry-run` | Skip LLM call for testing |

---

# Config Management: Layers

![Config layers](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtEZWZhdWx0cyBpbiBjb2RlXSAtLT4gQ1tGaW5hbCBjb25maWddCiAgQltFbnZpcm9ubWVudCB2YXJpYWJsZXNdIC0tPiBDCiAgRFtDTEkgYXJndW1lbnRzXSAtLT4gQwogIEMgLS0-IEVbUGlwZWxpbmUgcnVubmVyXQ==)

Configuration priority (highest wins): **CLI args > env vars > defaults**

---

# Secrets Management

**Never** hardcode or commit API keys.

| Type | Storage | Commit? |
|------|---------|---------|
| **Secrets** (API keys, passwords) | `.env` file | NO (gitignored) |
| **Config** (model names, timeouts) | `config.json` or code | YES |

### The `.env` pattern

- `.env` (gitignored) — contains real secrets
- `.env.example` (committed) — template with placeholders
- Load with `python-dotenv` **before** `os.getenv()` calls

---

# Error Handling: Teach the User

![Error flow](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtFcnJvciBvY2N1cnNdIC0tPiBCe1doYXQgdHlwZT99CiAgQiAtLT58aW5wdXR8IENbQ2xlYXIgbWVzc2FnZSArIGZpeCBzdWdnZXN0aW9uXQogIEIgLS0-fExMTXwgRFtSZXRyeSBvciBmYWxsYmFja10KICBCIC0tPnxzeXN0ZW18IEVbTG9nIGRldGFpbHMgKyBmYWlsIGdyYWNlZnVsbHld)

A good error message contains: **what** went wrong, **where**, and **what to try**.

---

# Error Handling Patterns

| Pattern | When to use |
|---------|-------------|
| **Custom exceptions** | Catch by category: `InputValidationError`, `LLMCallError` |
| **Context manager** | Wrap pipeline stages for consistent logging |
| **Retry with fallback** | GPT-4 fails → try GPT-3.5 |
| **Partial success** | Collect both successes and failures in batch |
| **Checkpoint** | Save state before risky LLM call |

**Dual reporting**: short user-facing error + detailed log for debugging.

---

# Minimum 3 Test Cases

| Test type | What to test | Example |
|-----------|-------------|---------|
| **Happy path** | Normal input works | Profile a valid CSV → check row count |
| **Edge case** | Unusual but valid input | CSV with missing values → check missing counts |
| **Failure case** | Invalid input fails clearly | Nonexistent file → expect `InputValidationError` |

---

# Testing LLM Code Without Calling LLM

| Technique | What to test |
|-----------|-------------|
| **Mock LLM response** | Pipeline logic, output handling |
| **Test prompt construction** | Prompt contains key info, under token limit |
| **Test output validation** | Schema validation catches bad outputs |
| **Dry-run mode** | Full pipeline without API call |

**Key insight**: Assert **contracts** (required keys, valid types), not exact text — LLM outputs vary between calls.

---

# Coverage Targets

| Component | Target |
|-----------|--------|
| Data loading/validation | 100% |
| Profiling logic | 90%+ |
| Compression | 80%+ |
| LLM integration | 60%+ (mocked) |

Run with: `pytest --cov=src --cov-report=html`

---

# Workshop / Deliverables

- Finalize `run_capstone.py` CLI with `--help`, `--dry-run`
- Add `.env` / `.env.example` for secrets
- Implement error handling with clear messages
- Write **3+ tests**: happy path, edge case, failure case
- Run `pytest` and confirm all pass

---

# Self-Check Questions

- Can a teammate run `--help` and understand how to use your tool?
- If a beginner runs your project wrong, does the error teach them what to do?
- Can you run tests without calling real LLM APIs?
- Is `.env` in `.gitignore`?

---

# References

- Python argparse: https://docs.python.org/3/library/argparse.html
- python-dotenv: https://github.com/theskumar/python-dotenv
- Twelve-Factor config: https://12factor.net/config
- pytest docs: https://docs.pytest.org/

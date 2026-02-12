---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 3 — LLM Fundamentals & Prompt Engineering"
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

# Week 3

## LLM Fundamentals + Prompt Engineering

---

# Learning Objectives

By the end of this week, you should be able to:

- Explain tokens, context windows, and why long inputs fail
- Design prompts as contracts: clear inputs, clear output schema
- Produce valid JSON outputs and validate them programmatically

---

# What is an API?

![bg right:50%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtZb3VyIEFwcF0gLS0-IEJbSFRUUCBSZXF1ZXN0XQogIEIgLS0-IENbSW50ZXJuZXRdCiAgQyAtLT4gRFtQcm92aWRlciBTZXJ2ZXJdCiAgRCAtLT4gRVtQcm9jZXNzIHJlcXVlc3RdCiAgRSAtLT4gRltIVFRQIFJlc3BvbnNlXQogIEYgLS0-IEMKICBDIC0tPiBB)

**API** (Application Programming Interface) = a way for your code to talk to a remote service.

- You send a **request** (HTTP) with your data
- The server **processes** it and sends back a **response**
- For LLMs: you send a prompt, the server returns generated text

---

# What is a Large Language Model (LLM)?

![What is LLM](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtUcmFpbmVkIG9uIGJpbGxpb25zIG9mIHRleHRdIC0tPiBNW0xhcmdlIExhbmd1YWdlIE1vZGVsXQogIE0gLS0-IEJbSW5wdXQ6IHRleHQgcHJvbXB0XQogIEIgLS0-IE0KICBNIC0tPiBDW091dHB1dDogZ2VuZXJhdGVkIHRleHRd)

An LLM is a **very large ML model** (billions of parameters) trained on massive text data.

- **Input**: text prompt (your question/instruction)
- **Output**: generated text (the model's response)
- It **predicts the next token** based on all previous tokens
- It does NOT "understand" — it generates statistically likely continuations

---

# What Happens When You Call an LLM API?

![bg right:20%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtCdWlsZCBwcm9tcHRdIC0tPiBCW1NlbmQgSFRUUCByZXF1ZXN0XQogIEIgLS0-IENbTW9kZWwgdG9rZW5pemVzIGlucHV0XQogIEMgLS0-IERbTW9kZWwgZ2VuZXJhdGVzIHRva2Vuc10KICBEIC0tPiBFW1JldHVybiByZXNwb25zZSB0ZXh0XQogIEUgLS0-IEZbUGFyc2UgKyB2YWxpZGF0ZSBvdXRwdXRd)

1. You **build a prompt** (system + user instructions + data)
2. Send it as an **HTTP request** to the provider
3. The model **tokenizes** your input
4. The model **generates** output tokens
5. You **parse + validate** the response

---

# Tokens: The Unit LLMs Process

A **token** ≈ a word fragment. Not exactly a word, not exactly a character.

| Text | Approx. tokens | Why |
|------|----------------|-----|
| `Hello world` | ~2 | Common words = 1 token each |
| `Hello, world!` | ~3 | Punctuation = extra tokens |
| `machinelearning` | ~3-4 | No spaces = worse tokenization |
| `你好世界` | ~4+ | Non-English = more tokens per word |

**Why tokens matter**:
- Token count drives **cost** ($X per 1K tokens)
- Token count drives **latency** (more tokens = slower)
- Context window = max tokens per request

---

# Context Window: A Hard Budget

![bg right:40%](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQ1tDb250ZXh0IFdpbmRvd10gLS0-IFNbU3lzdGVtIGluc3RydWN0aW9uc10KICBDIC0tPiBQW1Byb21wdCAvIHVzZXIgaW5wdXRdCiAgQyAtLT4gUltSZXRyaWV2ZWQgY29udGV4dF0KICBDIC0tPiBPW01vZGVsIG91dHB1dF0=)

Everything must fit inside the context window.

| Model | Context window |
|-------|---------------|
| GPT-3.5 | 4k–16k tokens |
| GPT-4 | 8k–128k tokens |
| Claude | 100k–200k tokens |

---

# Why Long Inputs Fail

If you send too much text:

| Problem | What happens |
|---------|-------------|
| **Instructions ignored** | Model "forgets" early instructions |
| **Output truncated** | JSON gets cut off mid-object |
| **Constraints violated** | "Strict JSON" rules get dropped |
| **Cost explodes** | You pay for every input + output token |

**Mitigation strategies**:
- **Sampling**: only send top-k relevant docs
- **Compression**: summarize long contexts (Week 6)
- **Explicit limits**: "Return at most 10 items"

---

# Prompts as API Contracts

A strong prompt is not "clever wording" — it's a **specification**.

| Component | Purpose |
|-----------|---------|
| **Role** | What the model is doing |
| **Task** | What to produce |
| **Input format** | What you will provide |
| **Output schema** | Exact JSON keys and types |
| **Constraints** | No extra keys, no markdown, no commentary |
| **Refusal conditions** | When to output an error / null |

---

# Prompt Contract Flow

![Prompt contract flow](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtSYXcgdGV4dCBpbnB1dF0gLS0-IEJbUHJvbXB0IGNvbnRyYWN0XQogIEIgLS0-IENbTExNIGNhbGxdCiAgQyAtLT4gRFtSYXcgb3V0cHV0IHRleHRdCiAgRCAtLT4gRVtQYXJzZSBKU09OXQogIEUgLS0-IEZbVmFsaWRhdGUgc2NoZW1hXQogIEYgLS0-IEdbVHlwZWQgcmVzdWx0XQ==)

Raw text → prompt contract → LLM call → parse JSON → validate schema → typed result.

Each step can fail independently — separating them helps debugging.

---

# Common Prompt Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| Vague output format | No schema specified | Add exact JSON keys |
| Almost-JSON (single quotes) | "Return JSON" too vague | Add "ONLY valid JSON, no markdown" |
| Hallucinated values | No refusal conditions | Add "Use null if not found" |
| Dropped constraints | Too many at once | Start simple, add incrementally |
| Prose + JSON mixed | Conflicting instructions | Align system and user messages |

---

# Retry / Repair Loop

![Retry repair](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtTZW5kIHByb21wdF0gLS0-IEJbR2V0IHJlc3BvbnNlXQogIEIgLS0-IEN7VmFsaWQgSlNPTj99CiAgQyAtLT58eWVzfCBEe1NjaGVtYSBPSz99CiAgRCAtLT58eWVzfCBFW1JldHVybiByZXN1bHRdCiAgQyAtLT58bm98IEZbUmVwYWlyIHByb21wdCArIHJldHJ5XQogIEQgLS0-fG5vfCBGCiAgRiAtLT4gQg==)

When the LLM returns invalid output:
1. **Parse fails** → tell the model what went wrong, retry
2. **Schema fails** → tell the model which fields are wrong, retry
3. **Cap retries** (e.g., max 2) → uncapped retries waste money

---

# Structured Output Validation

| Step | What it checks | Failure means |
|------|---------------|---------------|
| **JSON parse** | Is it valid JSON? | Prompt issue (format) |
| **Schema validate** | Right keys and types? | Spec issue (contract) |
| **Business rules** | Values make sense? | Data or model issue |

**Tool**: Use **Pydantic** to define expected output schema — it validates types and required fields automatically.

**Key insight**: Separate parse failure from schema failure — they have different root causes and different fixes.

---

# Workshop / Deliverables

Implement `extract.py`:
- Prompt for strict JSON output
- Validate output with Pydantic schema
- Retry/repair on invalid JSON (capped)

Create a small test set with **at least 3 edge inputs**:
- Normal text (person + company present)
- Text with no entities (expect nulls)
- Ambiguous or tricky text

---

# Self-Check Questions

- Why can the model still output invalid JSON even when instructed?
- What are 3 LLM failure modes you observed?
- What's your retry limit and why?
- Does your prompt define exact keys and forbid extra text?

---

# References

- OpenAI tiktoken: https://github.com/openai/tiktoken
- Prompt engineering guide: https://www.promptingguide.ai/
- Pydantic: https://docs.pydantic.dev/latest/
- JSON Schema: https://json-schema.org/

---
marp: true
theme: default
paginate: true
header: "Fundamentals of AI Engineering"
footer: "Week 4 — LLM API Engineering (Reliability & Cost)"
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

# Week 4

## LLM API Engineering (Reliability & Cost)

---

# Learning Objectives

By the end of this week, you should be able to:

- Implement an `llm_client.py` that is safe to reuse across projects
- Explain why timeouts / retries / rate limits / caching exist
- Add logging that helps you debug failures quickly

---

# What Can Go Wrong With an API Call?

![h:280](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtZb3VyIEFwcCBzZW5kcyByZXF1ZXN0XSAtLT4gQntTZXJ2ZXIgcmVzcG9uZHM_fQogIEIgLS0-fHRpbWVvdXR8IENbTm8gcmVzcG9uc2UgaW4gdGltZV0KICBCIC0tPnw0Mjl8IERbVG9vIG1hbnkgcmVxdWVzdHNdCiAgQiAtLT18NTAwLzUwM3wgRVtTZXJ2ZXIgZXJyb3JdCiAgQiAtLT18MjAwIE9LfCBGW1N1Y2Nlc3Nd)

LLM APIs are **remote services** — they can timeout, overload, or fail at any time.

Your code must handle every failure path, not just the happy path.

---

# Reliability Engineering: The Layers

![h:280](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtUaW1lb3V0OiBkb250IGhhbmcgZm9yZXZlcl0gLS0-IEJbUmV0cnk6IHRyeSBhZ2FpbiBvbiBmYWlsdXJlXQogIEIgLS0-IENbQmFja29mZjogd2FpdCBsb25nZXIgZWFjaCByZXRyeV0KICBDIC0tPiBEW0NhY2hlOiByZXVzZSBwcmV2aW91cyByZXN1bHRzXQogIEQgLS0-IEVbTG9nZ2luZzogcmVjb3JkIHdoYXQgaGFwcGVuZWRd)

Each layer protects against a different class of failure. Together they make your LLM client **production-ready**.

Timeout → Retry → Backoff → Cache → Logging

---

# Timeouts: Don't Hang Forever

**Without a timeout**: your program can hang indefinitely.
**With a timeout**: unknown waiting becomes a controlled failure.

| Use case | Connect | Read | Total |
|----------|---------|------|-------|
| Quick chat completion | 3s | 15s | 18s |
| Standard completion | 5s | 30s | 35s |
| Long-form generation | 5s | 90s | 95s |
| Embedding/classification | 3s | 10s | 13s |

- **Connect timeout** (short): catches DNS/network issues quickly
- **Read timeout** (longer): allows model processing time
- **Always make timeouts configurable** (env var or CLI flag)

---

# Retries + Exponential Backoff

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtSZXF1ZXN0IGZhaWxzXSAtLT4gQntSZXRyeWFibGU_fQogIEIgLS0-fDQyOS81MDMvdGltZW91dHwgQ1tCYWNrb2ZmOiAwLjVzLCAxcywgMnNdCiAgQyAtLT4gRFtSZXRyeSBvciBnaXZlIHVwXQogIEIgLS0-fDQwMS80MDR8IEVbRmFpbCBpbW1lZGlhdGVseV0=)

- **Retry transient failures**: timeouts, 429, 503
- **Don't retry permanent failures**: 401, 404
- **Exponential backoff**: 0.5s → 1s → 2s → 4s

---

# Idempotency & Request Tracking

**Idempotent** = "doing it twice has the same effect as doing it once."

| Concept | What to do |
|---------|-----------|
| **Request ID** | Generate a unique ID for every call |
| **Log both sides** | Log request and response with same ID |
| **Idempotency key** | Use where providers support them |

**Why it matters**: If you add retries and the original request actually succeeded, you might get duplicate results. Request IDs help you trace and deduplicate.

---

# Rate Limiting

**HTTP 429** = "Too Many Requests"

| Limit type | Example |
|-----------|---------|
| **RPM** (requests/min) | 60 |
| **TPM** (tokens/min) | 90,000 |
| **Concurrent** | 5 simultaneous |

### Your behavior on 429

1. Respect `Retry-After` header if present
2. Otherwise: exponential backoff
3. Consider **client-side throttling** to prevent hitting limits

---

# Graceful Degradation

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtQcmltYXJ5IG1vZGVsIGZhaWxzXSAtLT4gQntGYWxsYmFjaz99CiAgQiAtLT58eWVzfCBDW1RyeSBzbWFsbGVyIG1vZGVsXQogIEIgLS0-fGNhY2hlfCBEW1NlcnZlIGNhY2hlZCByZXN1bHRdCiAgQiAtLT58cXVldWV8IEVbUXVldWUgZm9yIGxhdGVyXQogIEIgLS0-fG5vfCBGW1JldHVybiBjbGVhciBlcnJvcl0=)

When rate-limited or failing, **degrade instead of crashing**:
- GPT-4 fails → fall back to GPT-3.5
- Non-critical → serve cached result
- Batch workload → queue for later

---

# Caching: Save Money and Time

![bg right:25% h:320](https://mermaid.ink/img/Zmxvd2NoYXJ0IFRECiAgQVtMTE0gUmVxdWVzdF0gLS0-IEtbTWFrZSBjYWNoZSBrZXldCiAgSyAtLT4gQ3tDYWNoZSBoaXQ_fQogIEMgLS0-fHllc3wgSFtSZXR1cm4gY2FjaGVkIHJlc3BvbnNlXQogIEMgLS0-fG5vfCBQW0NhbGwgcHJvdmlkZXJdCiAgUCAtLT4gU1tTdG9yZSByZXNwb25zZV0KICBTIC0tPiBPW1JldHVybiByZXNwb25zZV0=)

**Cache key must include** all parameters that affect output.

**Common pitfalls**:
- Forgetting system prompt in key
- Caching when temperature > 0
- Caching errors

---

# Logging: Minimum Viable Request Log

| Field | Why |
|-------|-----|
| `request_id` | Trace specific requests |
| `model` | Which model was called |
| `latency_s` | Performance monitoring |
| `success/failure` | Error rate tracking |
| `error_type` | Network vs parsing vs validation |
| `prompt_len` | Estimate token usage |

Good logs answer: "What happened, when, and how long did it take?" — essential for debugging production incidents.

---

# The Reusable `llm_client.py`

Your client should combine all reliability layers:

| Layer | What it does |
|-------|-------------|
| **Timeout** | Don't hang forever |
| **Cache check** | Return cached if available |
| **Provider call** | Make actual API request |
| **Retry + backoff** | Retry transient failures |
| **Cache store** | Save successful responses |
| **Logging** | Record request_id, latency, errors |

This becomes your **reusable building block** for every LLM project.

---

# Workshop / Deliverables

Implement `llm_client.py` with:
- Timeouts (configurable)
- Retries + exponential backoff
- Rate limit handling (429 → backoff or degrade)
- Simple caching (in-memory or file-based)
- Structured logs (request_id, model, latency, error)

Add tests or a manual failure checklist:
- Forced timeout scenario
- Forced invalid JSON scenario

---

# Self-Check Questions

- Can you show your client does not hang forever?
- Can you simulate failures and show graceful handling?
- Can you explain what information your logs provide during an incident?
- Does your cache key include all parameters that affect output?

---

# References

- Requests timeouts: https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
- HTTP 429: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
- Tenacity: https://tenacity.readthedocs.io/
- Python logging: https://docs.python.org/3/library/logging.html

# Week 3 — Part 04: OpenAI Compatible API

## Overview

The OpenAI API specification has become the industry standard for LLM interactions. This section introduces the compatibility ecosystem and shows how to use multiple providers with the same codebase.

---

## Pre-study (Self-learn)

For deeper coverage of OpenAI Compatible APIs:

- [Self-learn — OpenAI Compatible API](../self_learn/Chapters/3/04_openai_compatible_api.md)

---

## What is OpenAI Compatible API?

An "OpenAI Compatible API" implements the same HTTP endpoints, request formats, and response formats as OpenAI's official API:

- Same URL patterns (e.g., `/v1/chat/completions`)
- Same request body structure
- Same response JSON schema
- Same Bearer token authentication

### Why this matters

1. **Portability**: Change `base_url` and `api_key`, keep everything else the same
2. **Ecosystem leverage**: Use existing OpenAI SDK with any compatible provider
3. **Vendor independence**: Avoid lock-in to any single provider

---

## Free Providers (No Credit Card Required)

### Groq (Recommended for Learning)

Groq offers ultra-fast inference with a generous free tier. Sign up at [console.groq.com](https://console.groq.com) to get your API key.

**Official Documentation**: [Groq OpenAI Compatibility](https://console.groq.com/docs/openai)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"]
)

# Available models: llama-3.3-70b-versatile, llama-3.1-8b-instant, etc.
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Free Tier Limits**: Rate limits apply (requests/tokens per minute). See [Groq Rate Limits](https://console.groq.com/docs/rate-limits).

**Citation**: *"To start using Groq with OpenAI's client libraries, pass your Groq API key to the api_key parameter and change the base_url to https://api.groq.com/openai/v1"* — [GroqDocs: OpenAI Compatibility](https://console.groq.com/docs/openai)

### OpenRouter

OpenRouter provides access to 100+ models with a free tier. Sign up at [openrouter.ai](https://openrouter.ai) to get your API key.

**Official Documentation**: [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart)

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# Free models have :free suffix
response = client.chat.completions.create(
    model="meta-llama/llama-3.3-70b-instruct:free",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Free Tier Limits**: 20 requests/minute, 50 requests/day. See [OpenRouter Limits](https://openrouter.ai/docs/api-reference/limits).

**Citation**: *"OpenRouter's request and response schemas are very similar to the OpenAI Chat API... OpenRouter normalizes the schema across models and providers so you only need to learn one."* — [OpenRouter API Reference](https://openrouter.ai/docs/api/reference/overview)

### Other Free Providers

For additional providers (Ollama for local inference, LiteLLM proxy, Vercel AI Gateway), see the [Self-learn OpenAI Compatible API](../self_learn/Chapters/3/04_openai_compatible_api.md) documentation.

---

## Core Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/v1/models` | GET | List available models |
| `/v1/chat/completions` | POST | Generate chat responses |
| `/v1/embeddings` | POST | Generate text embeddings |

---

## Quick Example: Using Free Providers

```python
from openai import OpenAI
import os

# Option 1: Groq (ultra-fast, generous free tier)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"]
)

# Option 2: OpenRouter (100+ models, free tier available)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

# Same code works with any provider
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",  # Groq
    # model="meta-llama/llama-3.3-70b-instruct:free",  # OpenRouter
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

---

## Request Parameters (Key Ones)

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Model ID (required) |
| `messages` | array | Conversation history (required) |
| `temperature` | number | Randomness 0-2 (default 1.0) |
| `max_tokens` | integer | Maximum output tokens |
| `stream` | boolean | Enable streaming output |

---

## Response Structure

```json
{
  "id": "chatcmpl-abc123",
  "model": "llama3.2",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help?"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 8,
    "total_tokens": 18
  }
}
```

---

## Error Handling

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Bad Request | Check parameters |
| 401 | Unauthorized | Verify API key |
| 429 | Rate Limited | Implement backoff |
| 500 | Server Error | Retry with backoff |

```python
from openai import RateLimitError, APIError

try:
    response = client.chat.completions.create(...)
except RateLimitError:
    # Wait and retry
    time.sleep(2 ** attempt)
```

---

## Practical Exercise

See the accompanying notebook `04_openai_compatible_api.ipynb` for:

1. Listing models from different providers
2. Making chat completions with multiple backends
3. Implementing a multi-provider client class

---

## References

- [Groq OpenAI Compatibility](https://console.groq.com/docs/openai) — Official documentation for using OpenAI SDK with Groq
- [Groq Supported Models](https://console.groq.com/docs/models) — List of available models on Groq
- [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart) — Getting started with OpenRouter
- [OpenRouter API Reference](https://openrouter.ai/docs/api/reference/overview) — API documentation
- [Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources) — Community-maintained list of free providers

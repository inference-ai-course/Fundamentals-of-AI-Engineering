# OpenAI Compatible API

## Overview

The OpenAI API specification has become the de facto standard for LLM interactions. Understanding this compatibility layer is essential for building portable, provider-agnostic AI applications.

---

## What is OpenAI Compatible API?

An "OpenAI Compatible API" implements the same HTTP interface as OpenAI's official API:

- **Same endpoints**: `/v1/models`, `/v1/chat/completions`, `/v1/embeddings`
- **Same request format**: JSON body with model, messages, parameters
- **Same response format**: JSON with choices, usage statistics
- **Same authentication**: Bearer token in Authorization header

### Why providers adopt this standard

1. **Ecosystem leverage**: Developers already know the OpenAI SDK
2. **Tool compatibility**: Existing tools work without modification
3. **Lower switching cost**: Users can try new providers easily
4. **Standard interface**: Clear contract for integration

### Why this matters for you

- **Write once, run anywhere**: Change `base_url`, keep your code
- **Cost optimization**: Switch to cheaper providers without code changes
- **Latency reduction**: Use local models when network matters
- **Privacy compliance**: Keep sensitive data on-premises
- **Vendor independence**: Avoid lock-in to any single provider

---

## The Provider Landscape

### Free Providers (No Credit Card Required)

#### Groq

Groq offers ultra-fast inference with a generous free tier, making it ideal for learning and development.

**Official Documentation**: [GroqDocs: OpenAI Compatibility](https://console.groq.com/docs/openai)

**Setup:**
1. Sign up at [console.groq.com](https://console.groq.com)
2. Get your API key from [console.groq.com/keys](https://console.groq.com/keys)

**Usage:**
```python
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"]
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Available Models** ([GroqDocs: Models](https://console.groq.com/docs/models)):
- `llama-3.3-70b-versatile` — Production model, 70B parameters
- `llama-3.1-8b-instant` — Fast, lightweight model
- `gpt-oss-120b`, `gpt-oss-20b` — Open-weight GPT models

**Citation**: *"To start using Groq with OpenAI's client libraries, pass your Groq API key to the api_key parameter and change the base_url to https://api.groq.com/openai/v1"* — [GroqDocs: OpenAI Compatibility](https://console.groq.com/docs/openai)

#### OpenRouter

OpenRouter provides access to 100+ models from multiple providers with a free tier.

**Official Documentation**: [OpenRouter Quickstart](https://openrouter.ai/docs/quickstart)

**Setup:**
1. Sign up at [openrouter.ai](https://openrouter.ai)
2. Get your API key from [openrouter.ai/keys](https://openrouter.ai/keys)

**Usage:**
```python
from openai import OpenAI
import os

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

**Free Tier Limits** ([OpenRouter Limits](https://openrouter.ai/docs/api-reference/limits)):
- 20 requests/minute
- 50 requests/day
- Up to 1,000 requests/day with $10 lifetime top-up

**Citation**: *"OpenRouter's request and response schemas are very similar to the OpenAI Chat API... OpenRouter normalizes the schema across models and providers so you only need to learn one."* — [OpenRouter API Reference](https://openrouter.ai/docs/api/reference/overview)

**Free Models Available** ([Free LLM API Resources](https://github.com/cheahjs/free-llm-api-resources)):
- `meta-llama/llama-3.3-70b-instruct:free`
- `meta-llama/llama-3.2-3b-instruct:free`
- `google/gemma-3-12b-it:free`
- `mistralai/mistral-small-3.1-24b-instruct:free`
- `qwen/qwen3-4b:free`

---

### Local Inference

#### Ollama (Local Inference)

Ollama runs models locally and exposes an OpenAI-compatible endpoint.

**Official Documentation**: [Ollama OpenAI Compatibility](https://ollama.com/blog/openai-compatibility)

**Setup:**
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull a model
ollama pull llama3.2
```

**Usage:**
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Any value works, not validated
)

response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Citation**: *"Ollama now has built-in compatibility with the OpenAI Chat Completions API, making it possible to use more tooling and applications with Ollama locally."* — [Ollama Blog: OpenAI Compatibility](https://ollama.com/blog/openai-compatibility)

**Use cases:**
- Local development without API costs
- Privacy-sensitive data
- Offline operation
- Testing and prototyping

---

### Proxy Gateways

#### LiteLLM (Proxy Gateway)

LiteLLM acts as a unified proxy that normalizes requests across 100+ providers.

**Official Documentation**: [LiteLLM OpenAI Compatible Endpoints](https://docs.litellm.ai/docs/providers/openai_compatible)

**Setup:**
```bash
pip install litellm
litellm --model gpt-3.5-turbo
```

**Usage:**
```python
client = OpenAI(
    base_url="http://localhost:4000/v1",
    api_key="your-litellm-key"
)

# Route to different providers via model name
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Routes to OpenAI
    messages=[{"role": "user", "content": "Hello!"}]
)

response = client.chat.completions.create(
    model="claude-3-sonnet-20240229",  # Routes to Anthropic
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Features:**
- Multi-provider routing
- Automatic fallback on failure
- Cost tracking and budgets
- Load balancing

#### Vercel AI Gateway

Vercel's AI Gateway provides a unified endpoint with built-in observability.

**Official Documentation**: [Vercel AI Gateway](https://vercel.com/docs/ai-gateway/openai-compat)

**Usage:**
```python
client = OpenAI(
    base_url="https://ai-gateway.vercel.sh/v1",
    api_key=os.environ["AI_GATEWAY_API_KEY"]
)

# Use provider-prefixed model names
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

**Features:**
- Built-in observability and logging
- Automatic retries
- Provider fallbacks
- Prompt caching

### Anthropic OpenAI Compatibility

Anthropic provides an OpenAI SDK compatibility layer for Claude models.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.anthropic.com/v1/",
    api_key=os.environ["ANTHROPIC_API_KEY"]
)

# Use Claude model names
response = client.chat.completions.create(
    model="claude-3-sonnet-20240229",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

---

## Core Endpoints

### List Models

```http
GET /v1/models
Authorization: Bearer <api-key>
```

Response:
```json
{
  "object": "list",
  "data": [
    {
      "id": "llama3.2",
      "object": "model",
      "created": 1234567890,
      "owned_by": "ollama"
    }
  ]
}
```

### Chat Completions

```http
POST /v1/chat/completions
Authorization: Bearer <api-key>
Content-Type: application/json

{
  "model": "llama3.2",
  "messages": [
    {"role": "system", "content": "You are helpful."},
    {"role": "user", "content": "Hello!"}
  ]
}
```

Response:
```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "llama3.2",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 10,
    "total_tokens": 25
  }
}
```

### Embeddings

```http
POST /v1/embeddings
Authorization: Bearer <api-key>
Content-Type: application/json

{
  "model": "nomic-embed-text",
  "input": "Hello world"
}
```

Response:
```json
{
  "object": "list",
  "data": [{
    "object": "embedding",
    "index": 0,
    "embedding": [0.1, 0.2, ...]
  }],
  "model": "nomic-embed-text",
  "usage": {
    "prompt_tokens": 2,
    "total_tokens": 2
  }
}
```

---

## Request Parameters

### Required Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `model` | string | Model ID to use |
| `messages` | array | Conversation history |

### Message Format

```json
{
  "role": "system" | "user" | "assistant" | "tool",
  "content": "string or array for multimodal"
}
```

Example conversation:
```json
[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "What is Python?"},
  {"role": "assistant", "content": "Python is a programming language..."},
  {"role": "user", "content": "What about JavaScript?"}
]
```

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `temperature` | number | 1.0 | Sampling randomness (0-2) |
| `max_tokens` | integer | varies | Maximum output tokens |
| `top_p` | number | 1.0 | Nucleus sampling threshold |
| `n` | integer | 1 | Number of completions |
| `stream` | boolean | false | Enable streaming |
| `stop` | array | null | Stop sequences |
| `presence_penalty` | number | 0 | Penalty for new topics |
| `frequency_penalty` | number | 0 | Penalty for repetition |
| `response_format` | object | null | Output format constraint |
| `tools` | array | null | Function definitions |
| `tool_choice` | string | null | Tool selection mode |

### Temperature Guide

- **0.0**: Deterministic, most likely tokens (recommended for factual tasks)
- **0.3-0.5**: Low randomness (code generation, structured output)
- **0.7**: Balanced (general conversation)
- **1.0**: Default (creative writing)
- **1.2+**: High variability (brainstorming, poetry)

```python
# Deterministic for factual answers
response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "What is 2+2?"}],
    temperature=0.0
)

# Creative for brainstorming
response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Write a poem about AI"}],
    temperature=1.2
)
```

---

## Response Structure

### Full Response Object

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "llama3.2",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The capital of France is Paris."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 15,
    "completion_tokens": 8,
    "total_tokens": 23
  }
}
```

### Finish Reasons

| Reason | Meaning |
|--------|---------|
| `stop` | Natural end or stop sequence hit |
| `length` | Max tokens reached (output truncated) |
| `tool_calls` | Model made function calls |
| `content_filter` | Content filtered by safety system |

### Usage Tracking

Track costs with token counts:

```python
prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

# Cost estimation (prices vary by provider/model)
input_cost_per_1k = 0.0005  # Example: $0.0005 per 1k input tokens
output_cost_per_1k = 0.0015  # Example: $0.0015 per 1k output tokens

cost = (
    prompt_tokens * input_cost_per_1k +
    completion_tokens * output_cost_per_1k
) / 1000
```

---

## Streaming Responses

Enable streaming for real-time output:

```python
response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Tell me a story"}],
    stream=True
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

### Stream Chunk Format

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion.chunk",
  "choices": [{
    "index": 0,
    "delta": {
      "role": "assistant",
      "content": "Hello"
    },
    "finish_reason": null
  }]
}
```

Final chunk:
```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion.chunk",
  "choices": [{
    "index": 0,
    "delta": {},
    "finish_reason": "stop"
  }]
}
```

---

## Error Handling

### HTTP Status Codes

| Code | Meaning | Common Causes |
|------|---------|---------------|
| 400 | Bad Request | Invalid parameters, malformed JSON |
| 401 | Unauthorized | Missing or invalid API key |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Unknown model or endpoint |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Error | Server-side issue |

### Error Response Format

```json
{
  "error": {
    "message": "Invalid request: missing required parameter 'model'",
    "type": "invalid_request_error",
    "param": "model",
    "code": "missing_parameter"
  }
}
```

### Python Error Handling

```python
from openai import (
    APIError,
    RateLimitError,
    APIConnectionError,
    AuthenticationError,
    BadRequestError
)
import time

def safe_completion(client, messages, max_retries=3, **kwargs):
    """Make a completion request with error handling."""
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(
                model=kwargs.pop("model", "llama3.2"),
                messages=messages,
                **kwargs
            )
            
        except RateLimitError as e:
            wait = 2 ** attempt  # Exponential backoff
            print(f"Rate limited, waiting {wait}s...")
            time.sleep(wait)
            
        except APIConnectionError as e:
            print(f"Connection error: {e}")
            time.sleep(1)
            
        except AuthenticationError as e:
            raise  # Don't retry auth errors
            
        except BadRequestError as e:
            print(f"Bad request: {e}")
            raise  # Don't retry bad requests
            
        except APIError as e:
            print(f"API error: {e}")
            if attempt == max_retries - 1:
                raise
    
    raise Exception("Max retries exceeded")
```

---

## Structured Outputs

### JSON Mode

Force JSON output:

```python
response = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Output valid JSON only."},
        {"role": "user", "content": "List 3 fruits with colors."}
    ],
    response_format={"type": "json_object"}
)

import json
data = json.loads(response.choices[0].message.content)
```

### JSON Schema (when supported)

```python
response = client.chat.completions.create(
    model="gpt-4o",  # Not all providers support this
    messages=[...],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "person",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"}
                },
                "required": ["name", "age"]
            }
        }
    }
)
```

---

## Function Calling (Tools)

Define functions the model can call:

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["location"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "What's the weather in Paris?"}],
    tools=tools
)

# Check if model wants to call a function
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    print(f"Function: {tool_call.function.name}")
    print(f"Arguments: {tool_call.function.arguments}")
```

---

## Practical Patterns

### Multi-Provider Client

```python
class MultiProviderClient:
    """Client that switches between providers."""
    
    PROVIDERS = {
        "local": {
            "base_url": "http://localhost:11434/v1",
            "api_key": "ollama",
            "model": "llama3.2"
        },
        "cloud": {
            "base_url": "https://api.openai.com/v1",
            "api_key": os.environ["OPENAI_API_KEY"],
            "model": "gpt-4o-mini"
        }
    }
    
    def __init__(self, provider="local"):
        config = self.PROVIDERS[provider]
        self.client = OpenAI(
            base_url=config["base_url"],
            api_key=config["api_key"]
        )
        self.model = config["model"]
    
    def chat(self, messages, **kwargs):
        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            **kwargs
        )
```

### Conversation Manager

```python
class Conversation:
    """Manage multi-turn conversations."""
    
    def __init__(self, client, system="You are helpful."):
        self.client = client
        self.messages = [{"role": "system", "content": system}]
    
    def send(self, user_input, **kwargs):
        self.messages.append({"role": "user", "content": user_input})
        
        response = self.client.chat.completions.create(
            model=kwargs.pop("model", "llama3.2"),
            messages=self.messages,
            **kwargs
        )
        
        assistant_msg = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": assistant_msg})
        
        return assistant_msg
```

---

## References

- [Ollama OpenAI Compatibility](https://ollama.com/blog/openai-compatibility)
- [LiteLLM OpenAI Compatible Endpoints](https://docs.litellm.ai/docs/providers/openai_compatible)
- [Vercel AI Gateway Documentation](https://vercel.com/docs/ai-gateway/openai-compat)
- [Anthropic OpenAI SDK Compatibility](https://docs.anthropic.com/en/api/openai-sdk)

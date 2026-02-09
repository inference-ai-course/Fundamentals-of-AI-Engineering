# Week 3 — Part 01: Tokens and context windows (practical intuition)

## Overview

When working with LLMs, the most common “mysterious failures” are actually context budget failures.

This section gives you a mental model to reason about:

- what tokens are
- what a context window is
- why long prompts can cause formatting failures

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on tokenization, prompts, and evaluation mindset:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Prompt engineering and evaluation](../../self_learn/Chapters/3/02_prompt_engineering_evaluation.md)

Why it matters here (Week 3):

- Many “ignored instructions” and broken JSON outputs are caused by context budget pressure and truncation.
- Treat output length as a resource you must reserve up front.

## Tokens: what they are (engineering view)

A token is a unit the model processes.

- It is not exactly a word.
- It is not exactly a character.

Practical consequences:

- Token count is what drives cost (hosted APIs).
- Token count is what drives latency (often).

Rule of thumb: token count grows roughly with text length, but not perfectly. Two strings with the same character length can tokenize very differently.

### Concrete examples

Common English text: ~4 characters per token on average.

```
"Hello world" → ~2 tokens
"Hello, world!" → ~3 tokens (punctuation can add tokens)
"machine learning" → ~2 tokens
"machinelearning" → ~3-4 tokens (no spaces = worse tokenization)
```

Code is often less efficient:

```python
def hello():
    print("hi")
```

This might be 10-15 tokens, not 3 words.

Why this matters:
- Minified JSON/code can actually use *more* tokens than readable formatting
- Repeated strings (like long URLs) each cost tokens every time

### Token counting tools

Install `tiktoken` to count tokens:

```bash
pip install tiktoken
```

Example usage:

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")
text = "This is a test sentence for tokenization."
tokens = enc.encode(text)
print(f"Token count: {len(tokens)}")
print(f"Tokens: {tokens}")
```

This helps you estimate costs and avoid context overflow.

---

## Context window: a hard budget

A context window is the maximum number of tokens the model can handle in a single request.

Typical context windows (as of 2024):
- GPT-3.5: 4k-16k tokens
- GPT-4: 8k-128k tokens
- Claude: 100k-200k tokens

The budget must include:

- system instruction tokens
- developer/user prompt tokens
- any retrieved context (RAG)
- tool/function call payloads (if any)
- model output tokens

So if you "use up" the budget with input, the model has less space to respond.

### Budget calculation example

Suppose your model has a 4k token limit:

- System prompt: 100 tokens
- Your instruction: 50 tokens
- Retrieved documents: 3000 tokens
- Reserved for output: 500 tokens

**Total input**: 100 + 50 + 3000 = 3150 tokens  
**Total with output**: 3150 + 500 = 3650 tokens  
**Remaining buffer**: 4000 - 3650 = 350 tokens

If your retrieved documents grow to 3500 tokens, you exceed the limit and the request fails or gets truncated.

### Practical budgeting

In practice, you should reserve output budget *up front* (even if you don't measure tokens precisely). For example:

- "I want a concise answer"
- "Return at most 20 JSON objects"
- "Return at most 200 tokens" (if your provider supports it)

Some providers let you set `max_tokens` explicitly:

```python
response = client.chat.completions.create(
    model="gpt-4",
    messages=[...],
    max_tokens=500  # Reserve exactly 500 tokens for output
)
```

This prevents the model from "rambling" and using up your budget.

---

## Why long inputs fail

If you send too much text:

- the model may ignore earlier instructions
- output can be truncated
- "strict JSON" instructions get violated

Why "strict JSON" is fragile under budget pressure:

- JSON requires balanced braces/quotes
- truncation in the middle almost always produces invalid JSON
- long contexts increase the chance the model drifts into prose

### Example failure scenario

You ask for JSON output:

```json
{
  "items": [
    {"name": "item1", "value": 10},
    {"name": "item2", "value": 20},
    ...
  ]
}
```

But you hit the token limit mid-response:

```json
{
  "items": [
    {"name": "item1", "value": 10},
    {"name": "item2", "val
```

Result: invalid JSON, parsing fails, downstream code crashes.

### Mitigation strategies

This is why in later weeks you'll practice:

- **Sampling**: only send top-k relevant docs
- **Compression**: summarize long contexts
- **Chunking**: split large inputs into multiple requests
- **Explicit limits**: "Return at most 10 items"

---

## Practical habit: always budget output space

Even if you don’t know exact token counts, you should:

- keep prompts short
- keep schemas small
- request concise outputs

If you later use tools like `tiktoken`, you can make this quantitative:

- count tokens for your prompt
- decide a fixed maximum output token budget
- enforce a maximum input length before calling the model

---

## References

- OpenAI tiktoken (tokenization library): https://github.com/openai/tiktoken
- Transformer intuition (visual): https://jalammar.github.io/illustrated-transformer/

# Week 3 — Part 01: Tokens and context windows (practical intuition)

## Overview

When working with LLMs, the most common “mysterious failures” are actually context budget failures.

This section gives you a mental model to reason about:

- what tokens are
- what a context window is
- why long prompts can cause formatting failures

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on tokenization, prompts, and evaluation mindset:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Prompt engineering and evaluation](../../level_0/Chapters/3/02_prompt_engineering_evaluation.md)

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

---

## Context window: a hard budget

A context window is the maximum number of tokens the model can handle in a single request.

The budget must include:

- system instruction tokens
- developer/user prompt tokens
- any retrieved context (RAG)
- tool/function call payloads (if any)
- model output tokens

So if you “use up” the budget with input, the model has less space to respond.

In practice, you should reserve output budget *up front* (even if you don’t measure tokens precisely). For example:

- “I want a concise answer”
- “Return at most 20 JSON objects”
- “Return at most 200 tokens” (if your provider supports it)

---

## Why long inputs fail

If you send too much text:

- the model may ignore earlier instructions
- output can be truncated
- “strict JSON” instructions get violated

Why “strict JSON” is fragile under budget pressure:

- JSON requires balanced braces/quotes
- truncation in the middle almost always produces invalid JSON
- long contexts increase the chance the model drifts into prose

This is why in Week 6 you’ll practice:

- sampling
- compression
- chunking

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

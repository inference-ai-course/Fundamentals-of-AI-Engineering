# Week 3 — Part 01: Tokens and context windows (practical intuition)

## Overview

When working with LLMs, the most common “mysterious failures” are actually context budget failures.

This section gives you a mental model to reason about:

- what tokens are
- what a context window is
- why long prompts can cause formatting failures

---

## Tokens: what they are (engineering view)

A token is a unit the model processes.

- It is not exactly a word.
- It is not exactly a character.

Practical consequences:

- Token count is what drives cost (hosted APIs).
- Token count is what drives latency (often).

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

---

## Why long inputs fail

If you send too much text:

- the model may ignore earlier instructions
- output can be truncated
- “strict JSON” instructions get violated

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

---

## References

- OpenAI tiktoken (tokenization library): https://github.com/openai/tiktoken
- Transformer intuition (visual): https://jalammar.github.io/illustrated-transformer/

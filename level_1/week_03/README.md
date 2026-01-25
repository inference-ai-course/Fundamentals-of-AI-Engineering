# Level 1 — Week 3: LLM Fundamentals + Prompt Engineering

## What you should be able to do by the end of this week

- Explain tokens, context windows, and why long inputs fail.
- Design prompts as contracts: clear inputs, clear output schema.
- Produce valid JSON outputs and validate them programmatically.

Practice notebook: [practice.ipynb](practice.ipynb)

## Key Concepts (with explanations + citations)

### 1) Tokens and context windows

**Mental model**:

- LLMs operate on tokens, not characters.
- The **context window** is a hard limit: prompt + retrieved context + tool outputs + model output must fit.

Citations:

- OpenAI tiktoken (tokenization library): https://github.com/openai/tiktoken

### 2) Transformer intuition

**Mental model**:

- A Transformer uses attention to decide which tokens matter for predicting the next token.
- You do not need the full math to use LLMs effectively, but you should know:
  - long contexts are expensive
  - attention patterns can be brittle

Citations:

- The Illustrated Transformer (Jay Alammar): https://jalammar.github.io/illustrated-transformer/
- “Attention Is All You Need” (original paper): https://arxiv.org/abs/1706.03762

### 3) Hallucinations and typical failure modes

**Mental model**:

- LLMs are pattern completion systems; they can sound confident even when wrong.
- Your job as an engineer is to constrain behavior with:
  - schema constraints
  - verification steps
  - retrieval/tooling

Citations:

- Prompt Engineering Guide (community): https://www.promptingguide.ai/
- Anthropic Cookbook (GitHub): https://github.com/anthropics/anthropic-cookbook

### 4) Prompts as API contracts

**Mental model**:

- A “good prompt” is not poetry; it’s a spec.
- Define:
  - task
  - allowed inputs
  - output format
  - refusal conditions

Citations:

- OpenAI Python SDK examples (GitHub): https://github.com/openai/openai-python

### 5) Structured output validation (JSON + schema)

**Why this matters**:

- A model can produce almost-JSON, which breaks downstream code.
- Validation turns messy model output into a pass/fail condition.

Citations:

- JSON Schema (official): https://json-schema.org/
- Python `json` module: https://docs.python.org/3/library/json.html
- Pydantic validation: https://docs.pydantic.dev/latest/

### 6) Retry/repair patterns

**Mental model**:

- Retries are for transient problems (formatting, occasional provider hiccups).
- Always cap retries.

Citations:

- Tenacity (retry library): https://tenacity.readthedocs.io/

## Workshop / Implementation Plan

- Implement `extract.py`:
  - prompt for strict JSON
  - validate output
  - retry/repair on invalid JSON
- Create a small test set with at least 3 edge inputs

## Figures (Comprehensive Overviews — Leave Blank)

### Figure A: Prompt as contract (inputs -> model -> validated JSON)


### Figure B: Context window budget (prompt + context + output)


## Self-check questions

- Why can the model still output invalid JSON even when instructed?
- What are 3 LLM failure modes you observed?
- What’s your retry limit and why?

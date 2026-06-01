# Week 4 Tutorials: LLM Fundamentals + API Reliability

## Pre-study (Optional Refresher)

Self-learn is optional. If you want extra background:

- [Pre-study guide](../PRESTUDY.md)
- [Self-learn - Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)
- [Self-learn - Chapter 4: Hugging Face Platform and Local Inference](../self_learn/Chapters/4/Chapter4.md)

## Overview

Week 4 focuses on structured LLM workflows:

- tokens and context windows
- prompts as contracts
- JSON parsing and validation
- timeout, retry, logging, and clear failure handling

## Main Navigation

LLM fundamentals:

- [Tokens and context windows](01_tokens_context.md)
- [Prompt contracts](02_prompt_contracts.md)
- [Structured outputs and validation](03_structured_outputs_validation.md)

API reliability:

- [Timeouts and failures](04_timeouts_failures.md)
- [Retries and backoff](05_retries_backoff.md)
- [Rate limiting](06_rate_limiting.md)
- [Caching and logging](07_caching_logging.md)
- [LLM client skeleton](08_llm_client_skeleton.md)

## Optional/Advanced Reference

- [Local inference setup](optional_local_inference/01_local_inference_setup.md)
- [Ollama HTTP client](optional_local_inference/02_ollama_http_client.md)
- [Benchmarking script](optional_local_inference/03_benchmarking_script.md)
- [OpenAI compatible API](09_openai_compatible_api.md)

## Recommended Order

1. Learn the token/context mental model.
2. Write a prompt contract with explicit JSON fields.
3. Parse and validate outputs.
4. Add timeout, bounded retry/repair, and saved raw responses.
5. Document one failure mode and how you handled it.

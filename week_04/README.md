# Week 4: LLM Fundamentals + API Reliability

Week 4 turns LLM usage into a workflow that code can depend on. You will learn how tokens and context windows shape model behavior, how to design prompts as contracts, and how to add simple reliability controls around model-like calls.

The required Week 4 path can run without an API key. It uses the Week 3 `profile.json` and a mock LLM response so students can practice parsing, validation, repair, and logging before connecting to hosted or local models.

## Pre-study (Optional Refresher)

Self-learn is optional. Use these only if you want extra background:

- [Pre-study guide](../PRESTUDY.md)
- [Self-learn - Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)
- [Self-learn - Chapter 4: Hugging Face Platform and Local Inference](../self_learn/Chapters/4/Chapter4.md)

## What You Should Be Able to Do

By the end of this week, you should be able to:

- Explain tokens, context windows, and why long inputs fail.
- Write a structured prompt with clear input and output expectations.
- Produce JSON-like output and validate it programmatically.
- Add beginner-friendly timeout, retry, logging, and readable error handling.
- Convert a Week 3 data profile into structured insight JSON.

## Setup

Use the same course environment prepared in Week 2, then install Week 4 dependencies:

```bash
cd week_04
pip install -r requirements.txt
```

If `tiktoken` does not install on your machine, the required offline demo still works. `tiktoken` is only for more accurate token counting in the token/context lesson.

## Tutorials

Main Week 4 learning path:

- [01_tokens_context.md](01_tokens_context.md)
- [02_prompt_contracts.md](02_prompt_contracts.md)
- [03_structured_outputs_validation.md](03_structured_outputs_validation.md)
- [04_timeouts_failures.md](04_timeouts_failures.md)
- [05_retries_backoff.md](05_retries_backoff.md)
- [09_profile_to_insights_demo.md](09_profile_to_insights_demo.md)

Optional/advanced:

- [06_rate_limiting.md](06_rate_limiting.md)
- [07_caching_logging.md](07_caching_logging.md)
- [08_llm_client_skeleton.md](08_llm_client_skeleton.md)
- [opt_01_local_inference_setup.md](opt_01_local_inference_setup.md)
- [opt_02_ollama_http_client.md](opt_02_ollama_http_client.md)
- [opt_03_benchmarking_script.md](opt_03_benchmarking_script.md)
- [opt_04_openai_compatible_api.md](opt_04_openai_compatible_api.md)

## Workshop Plan

1. Write a prompt contract with:
   - task
   - input format
   - output JSON keys
   - fallback behavior for missing information
2. Use Week 3 `profile.json` as the main input.
3. Parse the output as JSON and validate the expected fields.
4. Add reliability controls:
   - timeout or max wait
   - retry limit or repair attempt
   - readable error messages
   - saved raw responses or basic logs
5. Write a short note describing one failure mode you observed.

## What to Complete

- Structured-output demo code or notebook.
- Week 3 profile-to-insights output, plus at least 2 additional small test inputs or simulated responses.
- Saved raw and parsed outputs where possible.
- Simplified reliability notes: timeout/max wait, bounded retry/repair, and logging/raw-response saving.
- Prompt contract and AI usage documentation.

Hosted API, instructor-provided API, or Ollama/local inference are optional extensions. The required demo must work offline with the mock response path.

## Common Pitfalls

- Asking for "JSON" without specifying exact keys.
- Letting the model return Markdown around JSON.
- Retrying forever instead of setting a retry limit.
- Sending too much CSV data directly to the model.
- Not saving raw responses, making debugging impossible.

## Self-check Questions

- Why can a model return invalid JSON even when asked not to?
- What is your retry limit and why?
- What happens when the input is too long?
- Can your code fail with a readable error?

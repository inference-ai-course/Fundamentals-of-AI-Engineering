# Week 4: LLM Fundamentals + API Reliability

Week 4 turns LLM usage into a workflow that code can depend on. You will learn how tokens and context windows shape model behavior, how to design prompts as contracts, and how to add simple reliability controls around API or local model calls.

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
- Use either a hosted API or local inference path for a small demo.

## Tutorials

Main Week 4 learning path:

- [01_tokens_context.md](01_tokens_context.md)
- [02_prompt_contracts.md](02_prompt_contracts.md)
- [03_structured_outputs_validation.md](03_structured_outputs_validation.md)
- [04_timeouts_failures.md](04_timeouts_failures.md)
- [05_retries_backoff.md](05_retries_backoff.md)
- [06_rate_limiting.md](06_rate_limiting.md)
- [07_caching_logging.md](07_caching_logging.md)
- [08_llm_client_skeleton.md](08_llm_client_skeleton.md)

Optional/advanced:

- [optional_local_inference/01_local_inference_setup.md](optional_local_inference/01_local_inference_setup.md)
- [optional_local_inference/02_ollama_http_client.md](optional_local_inference/02_ollama_http_client.md)
- [optional_local_inference/03_benchmarking_script.md](optional_local_inference/03_benchmarking_script.md)
- [09_openai_compatible_api.md](09_openai_compatible_api.md)

## Workshop Plan

1. Write a prompt contract with:
   - task
   - input format
   - output JSON keys
   - fallback behavior for missing information
2. Run the prompt on at least 3 test inputs.
3. Parse the output as JSON or validate the expected fields.
4. Add reliability controls:
   - timeout or max wait
   - retry limit or repair attempt
   - readable error messages
   - saved raw responses or basic logs
5. Write a short note describing one failure mode you observed.

## Deliverables

- Structured-output demo code or notebook.
- At least 3 test inputs and outputs.
- Saved raw and parsed outputs where possible.
- Simplified LLM client or wrapper notes.
- Prompt contract and AI usage documentation.

Hosted API, instructor-provided API, or Ollama/local inference are all acceptable. Local-vs-cloud benchmarking is optional.

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

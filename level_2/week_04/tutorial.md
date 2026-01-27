# Level 2 — Week 4 Tutorials

## Overview

Week 4 builds **RAG v1**:

- `/chat` uses `/search` results
- answers include **citations** (traceable to retrieved chunks)
- implement **refusal/clarification** when context is insufficient

## Navigation

- [01 — Context assembly + grounding prompt](01_context_assembly_grounding.md)
- [02 — Citation format + enforcement](02_citations_enforcement.md)
- [03 — Refusal vs clarification (deterministic rules first)](03_refusal_clarification.md)
- [04 — Minimal `/chat` endpoint contract](04_chat_endpoint_contract.md)

## Recommended order

1. Read 01–02 and ensure your prompt and outputs are auditable.
2. Read 03 and add deterministic safety behaviors.
3. Read 04 and wire it into your API.

## What “done” looks like

- `/chat` always returns one of:
  - `mode=answer` with at least one valid citation
  - `mode=clarify` with a concrete clarification question
  - `mode=refuse` with a short refusal reason
- Every citation references a `chunk_id` that was actually retrieved.
- You can reproduce a failure:
  - given a question, you can show the retrieved chunks and the exact prompt context
- You have a small labeled set of:
  - in-KB questions
  - ambiguous questions
  - out-of-KB questions

## References

- Pinecone RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/
- OpenAI prompting best practices: https://platform.openai.com/docs/guides/prompting
- JSON Schema: https://json-schema.org/

# Level 2 (System Building & Engineering) Overview

## Positioning

**Level 2** is for learners who can code and want to deliver LLM capabilities as real systems. This level focuses on:

*   **System Design**: embedding AI capabilities into product/service architecture (APIs, data, permissions, observability, cost)
*   **AI Application Engineering**: RAG, agent workflows, multi-tool orchestration
*   **AI-Assisted Delivery**: Vibe Coding / agentic coding methods and quality control

## Target Learners

*   Junior/mid-level developers with a technical background
*   Learners who completed Level 1 and want “deployable system” capability

## Prerequisites

*   Can independently complete a Python project (dependency management, modularization, basic tests)
*   Understand basic web concepts (HTTP/JSON) and engineering concepts (configuration, logging, exceptions)
*   Has experience making stable LLM calls (if not, complete the Level 1 LLM API engineering portion first)

## Beginner Bridge (If Level 2 Feels Too Steep)

If you are new to web backends or system design, Level 2 will be much easier if you can already do the following without help:

*   Build and run a FastAPI app locally
*   Explain request/response JSON and basic HTTP status codes
*   Use `.env` for configuration (API keys, model names)
*   Read logs and locate where a request failed (ingestion vs retrieval vs generation)

If you cannot yet do these reliably, you should first revisit Level 1 Week 6–10 topics (LLM client reliability + project engineering).

## Default Implementation Choices (Recommended)

To reduce decision overhead for learners, use these defaults unless you have a reason to change:

*   Web framework: FastAPI
*   Vector DB for local development: Chroma
*   RAG framework: pick exactly one (LangChain or LlamaIndex) and stick to it throughout Level 2

## Key Terms (Quick Glossary)

*   **System design**: designing components, boundaries, data flow, and failure modes of a system.
*   **HTTP / JSON**: web protocol and data format used by most APIs.
*   **API contract**: what endpoints exist and what request/response formats they accept/return.
*   **SLA**: service level agreement; a target for reliability/latency/availability.
*   **RAG**: Retrieval-Augmented Generation (retrieve relevant context then generate an answer).
*   **ETL**: Extract/Transform/Load (ingest data into your system).
*   **Chunking**: splitting documents into smaller pieces for indexing and retrieval.
*   **Embedding**: turning text into vectors so you can retrieve by semantic similarity.
*   **Vector DB**: a database optimized for storing/searching embeddings.
*   **Top-k**: retrieve the top k most similar chunks.
*   **Re-ranking (rerank)**: reorder retrieved results using a stronger model/scorer to improve precision.
*   **Citation**: showing which source snippets support an answer.
*   **Agent workflow**: a multi-step process (often with tool calling) with state, retries, and fallbacks.
*   **Tool calling**: letting a model request a tool/function with structured inputs.
*   **Observability**: logs/metrics/traces that let you understand what happened in a request.
*   **Request ID**: an identifier you propagate through logs to trace one request end-to-end.
*   **Tracing**: recording spans/steps across components to debug slow or failing requests.
*   **Health check**: an endpoint that reports whether the service is running and ready.
*   **Rate limiting**: restricting request volume to protect the service and control cost.
*   **Fallback**: a safe alternative path when the primary path fails (e.g., refuse/clarify, simpler retrieval, smaller model).
*   **CRUD**: Create/Read/Update/Delete; basic API operations for managing data.
*   **CI**: continuous integration; automatically run tests/checks on each change.

## Duration & Weekly Hours

*   **10 weeks** (can be compressed to 8 weeks or extended to 12 weeks)
*   **5 class hours per week** (recommended: 2 hours architecture lecture + 1 hour case study + 2 hours engineering workshop)

## Pillar Coverage

*   **System Design (Core)**: RAG layering, ingestion and indexing, serviceization, scalability, and observability
*   **AI Engineering (Advanced)**: LangChain/LlamaIndex, vector databases (Chroma/Milvus, etc.), re-ranking (rerank), tool calling
*   **Meta-Learning (Engineering)**: read framework source/docs to locate key APIs; debug with logs and traces
*   **AI Concepts (Applied)**: retrieval quality and hallucination causes; basics of evaluation and feedback loops

## Learning Outcomes

After completing Level 2, you should be able to:

1. Design and implement an end-to-end RAG system: ETL -> Chunk -> Embedding -> Vector DB -> Retrieval -> Generation
2. Add explainability and quality controls: citations, refusal/clarification, minimal offline evaluation
3. Implement at least one agent workflow: planning/tool calling/state management/failure recovery
4. Package the system as a runnable service (API + config + logs + basic tests) and deliver a demo
5. Use AI-assisted development to speed up delivery while maintaining quality through tests/review

## Recommended Tech Stack (Level 2)

*   Python web: FastAPI (recommended)
*   RAG framework: LangChain or LlamaIndex (choose one)
*   Vector DB: Chroma (local/lightweight) or Milvus (more scalable/production-oriented)
*   Evaluation: Ragas (RAG evaluation) or a minimal custom evaluation script
*   Observability: structured logs + request IDs + basic tracing (implementation is flexible)

## Assessment (Suggested)

*   Homework: 35%
*   Labs/Workshops: 25%
*   Capstone: 40%

## Exit Criteria

*   Deliver a runnable web app demo with end-to-end RAG + an agent workflow
*   The system has basic explainability and failure strategies (citations/refusal/fallback)
*   Includes a minimal evaluation set and a reproducible evaluation script

## Document Navigation

*   Weekly plan: see [weekly_plan_10w.md](weekly_plan_10w.md)
*   Assignments: see [assignments.md](assignments.md)
*   Capstone: see [capstone.md](capstone.md)

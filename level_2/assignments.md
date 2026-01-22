# Level 2 Assignments & Assessment

## Submission Guidelines (Recommended)

Each assignment submission should include:

*   How to run (README + commands)
*   Key configuration notes (env vars / config files)
*   Log examples (enough to locate which stage failed)

Each assignment should also include at least one “failure path” note: how you discovered, investigated, and fixed it.

## Assignment List (Suggested: 6 assignments + 1 Capstone)

### B1: FastAPI Service Skeleton (Engineering Minimum)

*   **Goal**: put the AI app into a service-ready engineering skeleton
*   **Requirements**: health check, structured logging, request ID, basic error handling
*   **Acceptance**: clear startup instructions; invalid input returns understandable errors

### B2: RAG Ingestion Pipeline (ETL/Indexing)

*   **Goal**: make the knowledge base maintainable and updatable
*   **Requirements**: implement `ingest.py` with incremental ingestion (strategy notes are sufficient)
*   **Acceptance**: repeated ingestion should not cause obvious duplication pollution (dedup/version/hash are all acceptable)

### B3: Chunking Comparison Experiment

*   **Goal**: understand how chunking impacts retrieval quality
*   **Requirements**: implement and compare two chunking strategies; submit a comparison report
*   **Acceptance**: report includes failure cases and root-cause hypotheses

### B4: RAG v1 (Citations + Refusal/Clarification)

*   **Goal**: make answers explainable and controllable
*   **Requirements**: answers must include citations; when context is insufficient, refuse or ask clarifying questions
*   **Acceptance**: provide 5 test questions covering in-KB, out-of-KB, and edge cases

### B5: Minimal Evaluation Set + Evaluation Script

*   **Goal**: establish a quality baseline and iteration basis
*   **Requirements**: 20–50 QA pairs; script outputs at least two metrics (e.g., hit rate, citation coverage)
*   **Acceptance**: evaluation is reproducible and outputs a list of failure cases

### B6: Agent Workflow (Tool Calling + Failure Recovery)

*   **Goal**: give the system the ability to act
*   **Requirements**: at least 2 tools (e.g., search/summarize/write); must have fallbacks
*   **Acceptance**: provide 3 task examples and run logs demonstrating failure recovery

---

## Capstone

See [capstone.md](capstone.md) for Capstone requirements.

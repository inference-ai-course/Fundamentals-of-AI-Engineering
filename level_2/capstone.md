# Level 2 Capstone: Vertical Domain Assistant System (RAG + Agents)

## Project Goal

Deliver an end-to-end, demo-ready, reproducible vertical domain assistant system with:

*   A domain knowledge base (ingestable and updatable)
*   RAG Q&A (citations, refusal/clarification)
*   Agent tool calling (at least one workflow)
*   A minimal evaluation + feedback loop (evidence the system improves)

## Topic Suggestions (Pick One)

*   Legal assistant (based on statutes/case snippets)
*   Medication knowledge assistant (based on public labels/guidelines)
*   Teaching assistant (based on course notes/assignments/FAQ)
*   Financial product assistant (based on product docs/terms/risk disclosures)

## MVP Scope

*   **User side**:
    *   Chat Q&A
    *   Citation display (source document + snippet)
    *   Feedback buttons (good/bad + optional text)
*   **Admin side**:
    *   Upload/ingest knowledge base
    *   Trigger index rebuild
    *   View evaluation results or failure cases
*   **Agent capability (at least one)**:
    *   Research style: plan -> search/retrieve -> synthesize -> conclude
    *   Or work style: draft -> self-check -> rewrite -> deliver

## Non-Functional Requirements

*   **Reproducibility**: one-command startup instructions (local or containerized)
*   **Observability**: logs can trace a full request lifecycle (retrieval/generation/tool calls)
*   **Control**: do not make things up for out-of-KB questions (refusal/clarification/fallback)
*   **Evaluability**: minimal eval set + eval script that reproduces claimed improvements

## Deliverables

*   Architecture diagram (components and data flow)
*   API documentation (at minimum: chat, ingest, eval endpoints)
*   Knowledge base samples (if copyright restricted, use synthetic/public materials)
*   Evaluation set and evaluation script
*   Demo recording or a live demo script (demo story)

## Acceptance Criteria

*   For in-KB questions, answers include citations traceable to source snippets
*   For out-of-KB questions, refusal/clarification is triggered (provide test cases)
*   Agent workflows run reliably; tool failures have fallback strategies
*   Evaluation is reproducible and demonstrates at least one iteration that improves metrics and/or reduces failure cases

## Rubric (Suggested)

*   Architecture and engineering quality: 35%
*   RAG quality and explainability: 30%
*   Agent design and stability: 20%
*   Evaluation and iteration evidence: 15%

## Stretch Goals

*   Hybrid retrieval (BM25 + vectors) and rerank
*   Prompt-injection defenses and stronger tool allowlist strategies
*   Basic load testing and p95 latency reporting
*   Feedback-driven automated data collection and re-indexing strategy

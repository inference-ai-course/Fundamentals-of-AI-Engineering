# Level 2 (System Building & Engineering) 10-Week Plan (5 class hours/week)

## Weekly Teaching Rhythm (Recommended)

*   **2 class hours**: architecture and design (system decomposition, edge cases, risks, tradeoffs)
*   **1 class hour**: case study (open-source projects, reference architectures, failure retrospectives)
*   **2 class hours**: workshop (make the system runnable; handle edge cases and observability)

---

## 10-Week Baseline Plan

### Week 1: From Requirements to Architecture (AI Application System View)

*   **Lecture (3h)**: requirement decomposition, module boundaries, SLA/cost/privacy; API contracts and error codes
*   **Workshop (2h)**: bootstrap a FastAPI skeleton (configuration, logging, health check, base routes)
*   **Deliverable**: runnable service skeleton + README

### Week 2: RAG End-to-End Overview + Ingestion (ETL)

*   **Lecture (3h)**: RAG pipeline and failure modes; data import/cleaning/denoising; document structuring
*   **Workshop (2h)**: implement ingestion pipeline: files -> parsing -> chunking -> indexing
*   **Deliverable**: `ingest.py` (repeatable runs + incremental update strategy notes)

### Week 3: Chunking & Embeddings (The First Key to Retrieval Quality)

*   **Lecture (3h)**: chunk size/overlap/structure; embedding choice and dimensionality intuition
*   **Workshop (2h)**: compare two chunking strategies; measure retrieval hits and answer quality differences
*   **Deliverable**: chunking experiment report + reproducible experiment scripts

### Week 4: Vector DB & Retrieval (Recall and Filtering)

*   **Lecture (3h)**: vector DB basics, metadata filters, top-k; recall vs precision tradeoffs
*   **Workshop (2h)**: connect Chroma/Milvus; implement a retrieval API (with filtering + pagination strategy notes)
*   **Deliverable**: `/search` API + minimal dataset demo

### Week 5: Re-Ranking (Rerank) and Citations (Make Answers Explainable)

*   **Lecture (3h)**: when hybrid search and rerank are necessary; product/compliance value of citations
*   **Workshop (2h)**: add rerank (optional) + enforce citations (answers must include source snippets)
*   **Deliverable**: RAG v1: answer + citations + failure strategy (refusal/clarification)

### Week 6: RAG Evaluation + Feedback Loop (Minimum Viable)

*   **Lecture (3h)**: offline evaluation (hit/coverage/consistency) vs online feedback; how to build a small but effective eval set
*   **Workshop (2h)**: build a minimal eval set (20–50 items) + eval script (reproducible metrics)
*   **Deliverable**: `eval_rag.py` + failure case set

### Week 7: Agent Workflows (Tool Calling and State Management)

*   **Lecture (3h)**: ReAct/Planning/Reflection; tool contracts (schema/retries/timeouts/fallback)
*   **Workshop (2h)**: implement a Research Agent: plan -> search -> summarize -> conclude
*   **Deliverable**: Agent v1 (runnable) + workflow design doc

### Week 8: Multi-Agent Collaboration & Task Decomposition (Controlled Complexity)

*   **Lecture (3h)**: multi-agent roles, conflicts, and consistency; when you should NOT use multi-agent
*   **Workshop (2h)**: implement a three-role pipeline (retrieval/writing/review), plus failure recovery
*   **Deliverable**: Agent v2 (with failure recovery)

### Week 9: Productize RAG + Agents (Service + Front-End)

*   **Lecture (3h)**: session management, permissions/auditing, cost control; front-end/back-end boundary
*   **Workshop (2h)**: package as a demo: chat endpoint + admin ingestion + feedback button
*   **Deliverable**: Capstone baseline version (demo-ready)

### Week 10: Capstone Sprint & Defense (Assessable Delivery)

*   **Lecture (3h)**: demo story, risks and limitations, next-iteration roadmap
*   **Workshop (2h)**: load testing/stability fixes, rerun evaluation, final defense and walkthrough
*   **Deliverable**: final Capstone delivery + retrospective notes

---

## 8-Week Compression Guidance

*   **Merge Week 2–3**: ingestion + chunking/embeddings in one week; prioritize “usable” over “perfect”
*   **Merge Week 4–5**: retrieval + citations in one week; treat rerank as a stretch goal
*   **Week 8 (multi-agent)**: optional; if compressing, keep it as a Capstone extension feature

---

## 12-Week Expansion Guidance

*   Add 1 week: **Security & prompt-injection defenses** (tool allowlists, content filtering, retrieval poisoning defenses)
*   Add 1 week: **Observability & operations** (tracing, metrics, alerting, cost monitoring and replay)
*   Add 1 Capstone week: a **feedback-driven iteration** (adjust chunking/retrieval/prompt based on failure cases)

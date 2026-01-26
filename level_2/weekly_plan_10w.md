# Level 2 (System Building & Engineering) 10-Week Plan (5 class hours/week)

## Weekly Teaching Rhythm (Recommended)

*   **2 class hours**: architecture and design (system decomposition, edge cases, risks, tradeoffs)
*   **1 class hour**: case study (open-source projects, reference architectures, failure retrospectives)
*   **2 class hours**: workshop (make the system runnable; handle edge cases and observability)

---

## 10-Week Baseline Plan

Weekly concept notes (self-study + citations) and practice notebooks:

*   Week 1: [week_01/README.md](week_01/README.md) | [week_01/practice.ipynb](week_01/practice.ipynb)
*   Week 2: [week_02/README.md](week_02/README.md) | [week_02/practice.ipynb](week_02/practice.ipynb)
*   Week 3: [week_03/README.md](week_03/README.md) | [week_03/practice.ipynb](week_03/practice.ipynb)
*   Week 4: [week_04/README.md](week_04/README.md) | [week_04/practice.ipynb](week_04/practice.ipynb)
*   Week 5: [week_05/README.md](week_05/README.md) | [week_05/practice.ipynb](week_05/practice.ipynb)
*   Week 6: [week_06/README.md](week_06/README.md) | [week_06/practice.ipynb](week_06/practice.ipynb)
*   Week 7: [week_07/README.md](week_07/README.md) | [week_07/practice.ipynb](week_07/practice.ipynb)
*   Week 8: [week_08/README.md](week_08/README.md) | [week_08/practice.ipynb](week_08/practice.ipynb)
*   Week 9: [week_09/README.md](week_09/README.md) | [week_09/practice.ipynb](week_09/practice.ipynb)
*   Week 10: [week_10/README.md](week_10/README.md) | [week_10/practice.ipynb](week_10/practice.ipynb)

### Week 1: From Requirements to Architecture (AI Application System View)

*   **Lecture (3h)**: requirement decomposition, module boundaries, SLA/cost/privacy; API contracts and error codes; choose one RAG framework (LangChain or LlamaIndex)
*   **Workshop (2h)**: bootstrap a FastAPI skeleton (configuration, logging, health check, base routes) + request/response models
*   **Deliverable**: runnable service skeleton + README + framework choice noted

### Week 2: RAG + Vector DB Foundations (Ingestion to Index)

*   **Lecture (3h)**: RAG pipeline and failure modes; how vector DBs store embeddings; metadata schema design; what “upsert/query/delete” means in practice
*   **Workshop (2h)**: implement ingestion end-to-end into a vector store (Chroma default): files -> parsing -> chunking -> embeddings -> upsert + basic dedup strategy
*   **Deliverable**: `ingest.py` (repeatable runs + incremental update strategy notes) + a minimal `query.py` that retrieves top-k chunks by text query

### Week 3: Retrieval API + Debuggable Retrieval Metrics (RAG Without Generation Yet)

*   **Lecture (3h)**: filters and query constraints (metadata, top-k); what “good retrieval” means; retrieval failure taxonomy; retrieval metrics (hit rate/recall@k) and how to build a small query set
*   **Workshop (2h)**: implement `/search` API with filtering + pagination strategy notes; add structured logs so you can inspect retrieved chunks per query
*   **Deliverable**: `/search` API + a small query set + `eval_retrieval.py` that outputs retrieval metrics and a list of misses

### Week 4: RAG v1 (Chat + Citations + Refusal/Clarification)

*   **Lecture (3h)**: prompt/context assembly; grounding and citation formatting; refusal/clarification strategies when context is insufficient
*   **Workshop (2h)**: implement `/chat` using `/search` results; enforce citations (source + snippet) and a failure strategy
*   **Deliverable**: RAG v1: chat endpoint + citations + refusal/clarification + minimal test questions

### Week 5: RAG Quality Iteration + Minimal Evaluation (Compressed)

*   **Lecture (3h)**: chunk size/overlap tradeoffs; embedding choice intuition; when rerank or hybrid retrieval helps; latency/cost tradeoffs; offline evaluation concepts (hit/coverage/consistency)
*   **Workshop (2h)**: run controlled experiments (one variable at a time): compare chunking and/or embedding configs; optionally add rerank or query rewriting; build a minimal eval set (10–20 items) + a small reproducible eval script
*   **Deliverable**: RAG v1.1 with one documented quality improvement + `eval_rag.py` (minimal) + updated failure case notes

### Week 6: Agent Foundations (Tool Calling, State, and Reliability)

*   **Lecture (3h)**: what an agent is (vs a prompt); the agent loop (plan -> act -> observe -> reflect); state and memory (conversation state vs working memory vs long-term memory); tool contracts (schema, validation, timeouts, retries, fallbacks)
*   **Workshop (2h)**: implement an Agent v1 that calls at least 2 tools (e.g., retrieve/search + summarize/write) with typed inputs/outputs, structured logs, and one failure recovery path
*   **Deliverable**: Agent v1 (runnable) + tool interface definitions + workflow design doc

### Week 7: Agent Design Patterns (Planning, Guardrails, and Multi-Step Tasks)

*   **Lecture (3h)**: task decomposition, role prompting, and planning depth control; guardrails (allowlists, refusal conditions, budget limits); how to debug agents (trace per-step decisions); when to use (and not use) multi-agent
*   **Workshop (2h)**: add one agent capability: multi-step research report, self-check/rewrite, or a reviewer role; add a trace-style log view of agent steps
*   **Deliverable**: Agent v1.1 with one reliability/guardrail improvement + 3 demo tasks + logs showing a failure and recovery

### Week 8: Productize RAG + Agents (Service + Front-End)

*   **Lecture (3h)**: session management, permissions/auditing, cost control; front-end/back-end boundary
*   **Workshop (2h)**: package as a demo: chat endpoint + admin ingestion + feedback button
*   **Deliverable**: Capstone baseline version (demo-ready)

### Week 9: Hardening & Operations (Reliability, Security, and Scale)

*   **Lecture (3h)**: observability (structured logs, request IDs, basic tracing), permissions and auditing, prompt-injection defenses, and cost controls; when (not) to add multi-agent
*   **Workshop (2h)**: add one hardening feature (choose one): tracing spans, basic rate limiting, auth/roles for ingestion, prompt-injection guardrails, or multi-agent extension with failure recovery
*   **Deliverable**: Capstone hardened version + a short ops checklist (what to monitor, what can fail, how to debug)

### Week 10: Capstone Sprint & Defense (Assessable Delivery)

*   **Lecture (3h)**: demo story, risks and limitations, next-iteration roadmap
*   **Workshop (2h)**: load testing/stability fixes, rerun evaluation, final defense and walkthrough
*   **Deliverable**: final Capstone delivery + retrospective notes

---

## 8-Week Compression Guidance

*   **Merge Week 2–3**: ingestion + retrieval API + retrieval metrics in one week; prioritize “usable” over “perfect”
*   **Merge Week 4–5**: RAG v1 + quality iteration + minimal evaluation in one week
*   **Agents start**: if compressing, treat Week 6 (agents) as the start of the second half; keep multi-agent as optional
*   **Rerank**: optional; if compressing, treat it as a stretch goal (focus on chunking and clean citations first)

---

## 12-Week Expansion Guidance

*   Add 1 week: **Security & prompt-injection defenses** (tool allowlists, content filtering, retrieval poisoning defenses)
*   Add 1 week: **Observability & operations** (tracing, metrics, alerting, cost monitoring and replay)
*   Add 1 Capstone week: a **feedback-driven iteration** (adjust chunking/retrieval/prompt based on failure cases)

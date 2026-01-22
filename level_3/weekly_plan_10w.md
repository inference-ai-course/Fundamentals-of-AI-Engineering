# Level 3 (Deep Optimization & Expert Track) 10-Week Plan (5 class hours/week)

## Weekly Teaching Rhythm (Recommended)

*   **2 class hours**: principles and design tradeoffs (why we do it, and where the boundaries are)
*   **1 class hour**: case study (open-source implementations, production incident retrospectives, paper ideas)
*   **2 class hours**: experiment/deployment workshop (run it, record it, compare it, find bottlenecks)

---

## 10-Week Baseline Plan

### Week 1: Reproducibility & Data Versioning (Preparing for Fine-Tuning)

*   **Lecture (3h)**: experiment logging standards, data versions and leakage, training logs and rollback; minimal controlled experiment design
*   **Workshop (2h)**: build an experiment template: config files + log directories + result summarization scripts
*   **Deliverable**: an `experiments/` template (can run one baseline inference evaluation)

### Week 2: Fine-Tuning Landscape (SFT/LoRA/QLoRA) + Data Formats

*   **Lecture (3h)**: SFT and alignment intuition; parameter efficiency and boundaries of LoRA/QLoRA
*   **Workshop (2h)**: prepare instruction data format (instruction/input/output); build a data audit script
*   **Deliverable**: data audit report (length distribution/duplication/sensitive-data checking strategy notes)

### Week 3: SFT in Practice (First Reproducible Training Run)

*   **Lecture (3h)**: hyperparameters, overfitting signals, checkpoint strategy; common training failures
*   **Workshop (2h)**: run one LoRA fine-tune; export adapters and validate via inference
*   **Deliverable**: a complete experiment record (configs, curves, samples, failure points)

### Week 4: Fine-Tuning Evaluation (Prove Whether It Improved)

*   **Lecture (3h)**: evaluation design (benchmark/controls/blind tests); risks and calibration for LLM-as-a-Judge
*   **Workshop (2h)**: build an evaluation script comparing base vs fine-tuned; output metrics + failure cases
*   **Deliverable**: `eval_compare.py` + failure case analysis

### Week 5: Preference Optimization & Data Iteration (Optional; Light DPO)

*   **Lecture (3h)**: preference data; intuition for DPO/RLHF; when you should/should not use them
*   **Workshop (2h)**: iterate once based on failure cases (add data / adjust templates / retrain)
*   **Deliverable**: iteration evidence pack (problem -> data changes -> result comparison)

### Week 6: Quantization (Quality–Performance–Cost Triangle)

*   **Lecture (3h)**: differences between GGUF/AWQ/GPTQ; quantization error and task sensitivity
*   **Workshop (2h)**: run one quantization comparison: quality regression + VRAM/speed gains
*   **Deliverable**: quantization comparison report (gains and tradeoffs)

### Week 7: Inference Service & Concurrency (vLLM or Equivalent)

*   **Lecture (3h)**: throughput/latency/p95/p99; batching, KV cache, streaming output; rate limiting and circuit breakers
*   **Workshop (2h)**: deploy an inference service + write a load test script to measure latency distributions and throughput
*   **Deliverable**: load test results + initial bottleneck analysis

### Week 8: Production Readiness (Monitoring, Replay, Fallback)

*   **Lecture (3h)**: minimum observability set (logs/metrics/tracing); incident replay; fallback strategies (model/retrieval/features)
*   **Workshop (2h)**: add health checks, basic metrics output, and retry/fallback strategies to the inference service
*   **Deliverable**: a runnable “minimum viable production” deployment notes

### Week 9: Meta-Learning Intensive (Source Reading + Complex Debugging)

*   **Lecture (3h)**: source reading paths; minimal reproduction/binary search; OOM and performance bottleneck playbooks
*   **Workshop (2h)**: complete one “issue dossier”: error -> reproduction -> investigation -> fix -> regression
*   **Deliverable**: Issue Dossier (reproducible and regression-tested)

### Week 10: Capstone Defense (Enterprise End-to-End Solution)

*   **Lecture (3h)**: presenting “quality evidence + performance evidence + risk notes”; writing a technical proposal
*   **Workshop (2h)**: final defense and walkthrough: reproduce pipeline, rerun evaluation, reproduce load testing
*   **Deliverable**: final Capstone delivery + retrospective and next-step roadmap

---

## 8-Week Compression Guidance

*   **Merge Week 2–3**: data preparation + one LoRA fine-tuning run
*   **Merge Week 4–5**: evaluation + lightweight iteration; keep “evidence-driven” as the baseline
*   **Week 8 (production readiness)**: compress to “minimum monitoring + health checks + fallback strategy notes”

---

## 12-Week Expansion Guidance

*   Add 1 week: **Data quality and alignment risks** (bias, sensitive content, red-teaming, compliance)
*   Add 1 week: **Deep performance profiling** (profiling, GPU utilization, batching strategies, KV cache tuning)
*   Add 1 Capstone week: **replay-based evaluation** and **failure-case-driven data iteration**

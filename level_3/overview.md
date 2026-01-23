# Level 3 (Deep Optimization & Expert Track) Overview

## Positioning

**Level 3** is for learners who want to “open the black box” and gain enterprise-grade delivery and optimization skills. It covers:

*   Fine-tuning and data engineering (SFT/LoRA/QLoRA, data quality gates)
*   Evaluation systems and iteration evidence (offline/online evaluation; risks and calibration for LLM-as-a-Judge)
*   Inference optimization and deployment (quantization, concurrency, throughput/latency, cost and stability)
*   Meta-learning (reading source code, paper-to-code reproduction, complex debugging)

## Target Learners

*   Experienced senior developers
*   Learners who completed Level 2 and want “quality evidence + performance/cost optimization + production operations” capability

## Prerequisites

*   Can deliver a complete LLM application system (RAG/agents/APIs/engineering practices)
*   Has basic experimentation and evaluation habits (baseline comparisons, config logging, failure case analysis)
*   Comfortable with Linux/CLI/log-based debugging

## Key Terms (Quick Glossary)

*   **Fine-tuning**: training a base model on your task data to change its behavior.
*   **SFT (Supervised Fine-Tuning)**: fine-tuning on instruction-response pairs.
*   **Preference optimization**: training to follow human preferences (helpfulness/harmlessness/style).
*   **RLHF**: reinforcement learning from human feedback; a family of methods for preference optimization.
*   **DPO**: Direct Preference Optimization; a simpler preference-optimization method that avoids full RL loops.
*   **LoRA**: Low-Rank Adaptation; trains small adapter weights instead of updating all model weights.
*   **QLoRA**: LoRA with quantization to reduce VRAM during training.
*   **Checkpoint**: a saved training state you can resume from or compare.
*   **Offline evaluation**: evaluating with a fixed dataset and scripts (reproducible).
*   **LLM-as-a-Judge**: using an LLM to score outputs; useful but requires calibration and spot checks.
*   **Quantization**: reducing numerical precision to speed up inference and reduce memory usage.
*   **Throughput / latency (p95/p99)**: how many requests you can serve vs how long requests take; tail latency matters in production.

## Duration & Weekly Hours

*   **8 weeks** (can be expanded to 10 weeks or extended to 12 weeks)
*   **5 class hours per week** (recommended: 2 hours theory + 1 hour case study + 2 hours experiment/deployment workshop)

## Pillar Coverage

*   **AI Concepts (Advanced)**: intuition for SFT/RLHF/DPO; boundaries of quantization and inference acceleration
*   **AI Engineering (Expert)**: end-to-end pipeline for fine-tuning, evaluation, quantization, deployment, and load testing
*   **Meta-Learning (Core)**: source reading, paper-to-code, complex debugging (OOM/CUDA/performance bottlenecks)
*   **System Design (Expert)**: high-concurrency inference services, observability, fallback strategies, cost governance

## Learning Outcomes

After completing Level 3, you should be able to:

1. Build a high-quality dataset and complete a reproducible fine-tuning run (including failure retrospective and regression verification)
2. Build an evaluation system to prove whether things improved, and iterate based on failure cases
3. Master at least one quantization path and evaluate quality regression vs performance gains
4. Deploy an inference service and run a minimal load test, producing throughput/latency distributions and bottleneck analysis
5. Handle unfamiliar errors or new techniques by quickly locating key references and shipping validation demos

## Recommended Tech Stack (Level 3)

*   Fine-tuning: Unsloth or Llama-Factory (choose one)
*   Inference deployment: vLLM (or an equivalent high-performance inference solution)
*   Evaluation: Ragas/DeepEval (or a minimal custom evaluation script + LLM-as-a-Judge)
*   Quantization: GGUF/AWQ/GPTQ (choose one path and run a complete experiment)
*   Engineering: structured logging, basic metrics (p95/p99), load testing scripts

## Assessment (Suggested)

*   Homework and experiment logs: 40%
*   Workshop completion: 20%
*   Capstone (full lifecycle): 40%

## Exit Criteria

*   Independently complete a reproducible fine-tuning experiment and prove results via evaluation
*   Handle common deployment performance and stability issues (latency, throughput, VRAM, concurrency)
*   Produce a meta-learning evidence pack (source reading / paper reproduction / debugging dossier)

## Document Navigation

*   Weekly plan: see [weekly_plan_10w.md](weekly_plan_10w.md)
*   Assignments: see [assignments.md](assignments.md)
*   Capstone: see [capstone.md](capstone.md)

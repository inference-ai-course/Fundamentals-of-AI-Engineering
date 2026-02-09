# Week 8 — Part 03: Preparing for Level 2 (what changes)

## Overview

Foundamental Course is mostly:

- a single-project pipeline
- mostly offline, script-based
- focusing on reproducibility and reliability basics

Level 2 shifts toward **systems thinking**:

- retrieval (RAG)
- evaluation loops
- multi-step agent workflows
- knowledge bases

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on the overall roadmap and prerequisites:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn Schedule](../../self_learn/Schedule.md)

Why it matters here (Week 8):

- Level 2 introduces new failure surfaces (retrieval + multi-step workflows) and requires tighter observability and evaluation.

---

## Practical mindset shifts

### Shift 1: Script → Service
**Foundamental Course**: Single-file scripts, run once and inspect output  
**Level 2**: FastAPI services, handle concurrent requests, expose APIs

**What changes**: You'll deploy as a web service, not just a CLI tool

### Shift 2: Prompt → Retrieval
**Foundamental Course**: Static prompts with compressed data  
**Level 2**: Dynamic prompts assembled from retrieved documents

**What changes**: You'll implement vector search, chunking, and reranking

### Shift 3: Manual inspection → Evaluation sets
**Foundamental Course**: Read output, judge quality manually  
**Level 2**: Automated metrics (precision@k, recall, F1) on labeled test sets

**What changes**: You'll build eval harnesses and track metrics over time

### Shift 4: Single call → Multi-step workflows
**Foundamental Course**: One LLM call per run  
**Level 2**: Chains (plan → retrieve → answer), loops (refine until valid)

**What changes**: You'll orchestrate multiple LLM calls with control flow

---

## Level 2 preview: What you'll build

### Week 1-2: RAG Foundation
- Vector database setup (Pinecone/Chroma/Weaviate)
- Document chunking and embedding
- Semantic search over your own documents
- **Output**: API endpoint that answers questions using your knowledge base

### Week 3-4: Retrieval Quality
- Chunking strategies (semantic vs fixed-size)
- Hybrid search (dense + sparse)
- Reranking retrieved results
- **Output**: Measurably better retrieval (precision/recall metrics)

### Week 5-6: Production RAG
- Streaming responses
- Citation tracking (which docs were used)
- Context assembly and grounding
- **Output**: Production-ready RAG service with citations

### Week 7-8: Evaluation + Iteration
- Golden question-answer pairs
- Automated eval pipeline
- A/B testing retrieval strategies
- **Output**: Data-driven improvements to retrieval quality

---

## Skills to practice before Level 2

### Strong foundation (you already have these)
- Python functions, classes, error handling
- Working with APIs (requests, timeouts, retries)
- JSON parsing and validation
- File I/O and data pipelines
- Testing with pytest

### Review if rusty

**Vector/embedding concepts**:
```python
# You'll work with embeddings (numeric representations of text)
import numpy as np

# Embeddings are just arrays of floats
embedding = [0.23, -0.45, 0.12, ...]  # typically 768 or 1536 dimensions

# Similarity = dot product (or cosine similarity)
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
```

**SQL basics** (for structured retrieval):
```sql
-- You'll query metadata filters
SELECT * FROM documents 
WHERE category = 'technical' 
  AND date > '2024-01-01'
LIMIT 10;
```

**Async Python** (for concurrent API calls):
```python
import asyncio

# Level 2 uses async for parallel retrieval
async def fetch_many(queries):
    tasks = [fetch_one(q) for q in queries]
    return await asyncio.gather(*tasks)
```

### New concepts to learn

1. **Vector databases** - Specialized DBs for similarity search
2. **Embeddings** - Converting text to numeric vectors
3. **Semantic search** - Finding similar meaning, not just keywords
4. **Reranking** - Two-stage retrieval (fast recall, then precise ranking)
5. **FastAPI** - Building REST APIs in Python

---

## Level 2 readiness checklist

### Code skills
- [ ] Can write Python functions with type hints
- [ ] Comfortable with async/await (or willing to learn quickly)
- [ ] Can read API documentation and try examples
- [ ] Can write pytest tests without scaffolding
- [ ] Understand JSON schemas and validation

### Systems thinking
- [ ] Can debug with logs and intermediate artifacts
- [ ] Understand the difference between dev/staging/prod
- [ ] Know when to cache vs recompute
- [ ] Can estimate token costs and latency budgets

### Tools
- [ ] Comfortable with git (clone, commit, push, pull)
- [ ] Can run Docker containers (or willing to learn)
- [ ] Familiar with environment variables and secrets management
- [ ] Can use curl or Postman to test APIs

### Mindset
- [ ] Treat failures as data (not roadblocks)
- [ ] Build evaluation before optimization
- [ ] Save artifacts for later inspection
- [ ] Embrace incremental improvement over perfection

---

## Bridge project (optional, before Level 2)

Build a simple RAG prototype to get familiar:

**Project**: "Ask questions about your own documents"

```python
# Minimal RAG in ~50 lines
import openai
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 1. Embed your documents
docs = ["Python is a programming language.", "Cats are mammals.", ...]
embeddings = [get_embedding(doc) for doc in docs]  # Call OpenAI API

# 2. Embed user question
question = "What is Python?"
q_embedding = get_embedding(question)

# 3. Find most similar docs
similarities = cosine_similarity([q_embedding], embeddings)[0]
top_k = np.argsort(similarities)[-3:][::-1]  # Top 3

# 4. Build context from retrieved docs
context = "\n".join([docs[i] for i in top_k])

# 5. Ask LLM with context
prompt = f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
answer = call_llm(prompt)
```

**What you'll learn**:
- How embeddings work
- Why retrieval helps (LLM sees relevant docs only)
- How to assemble context from chunks

**Time investment**: 1-2 days

---

## Common Level 2 pitfalls (and how to avoid them)

### Pitfall 1: Retrieval returns irrelevant docs
**Symptom**: LLM answers are wrong or off-topic  
**Prevention**: Start with eval set, measure precision@k before building full system

### Pitfall 2: Context window overflow
**Symptom**: Retrieved too many docs, prompt exceeds limit  
**Prevention**: Budget tokens (metadata + top-k + instructions + output)

### Pitfall 3: Slow retrieval
**Symptom**: API responses take 5+ seconds  
**Prevention**: Use approximate nearest neighbor search, not brute force

### Pitfall 4: No way to measure improvement
**Symptom**: "This retrieval strategy seems better" but no data  
**Prevention**: Build eval dataset first (golden Q&A pairs)

---

## Resources to review

### Before Level 2 starts
- FastAPI tutorial (https://fastapi.tiangolo.com/tutorial/)
- Vector database concepts (https://www.pinecone.io/learn/vector-database/)
- Embeddings explained (https://platform.openai.com/docs/guides/embeddings)

### Optional deep dives
- RAG patterns: https://arxiv.org/abs/2005.11401
- Evaluation metrics: Precision, Recall, F1
- Async Python: https://realpython.com/async-io-python/

---

## Practice notebook

For Level 2 preparation exercises, see:
- **[03_preparing_for_level2.ipynb](./03_preparing_for_level2.ipynb)** - RAG preview and skills assessment
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- Can you explain what RAG is in one sentence?
- Do you understand the difference between embeddings and prompts?
- Are you comfortable with the idea of measuring retrieval quality?
- Can you run a FastAPI "Hello World" example?

**If yes to all**: You're ready for Level 2!

---

## References

- RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/
- FastAPI: https://fastapi.tiangolo.com/
- Vector databases: https://www.pinecone.io/learn/vector-database/
- Embeddings guide: https://platform.openai.com/docs/guides/embeddings

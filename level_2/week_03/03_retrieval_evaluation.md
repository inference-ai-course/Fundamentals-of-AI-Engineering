# Week 3 — Part 03: Minimal retrieval evaluation (hit rate, recall@k)

## Overview

Without a saved query set, improvements are subjective.

A minimal eval loop:

- define 10–20 queries
- run `/search` for each query
- compute:
  - hit rate
  - recall@k
- save misses for inspection

---

## Definitions

- **Hit rate**: did we retrieve at least one correct chunk?
- **Recall@k**: if a correct chunk exists, was it in top-k?

---

## Metric definitions (more formal)

Assume:

- a query has a set of relevant chunk ids $R$
- your retriever returns an ordered list of top-k chunk ids $L_k = [\ell_1, \ldots, \ell_k]$
- define $\text{hits}_k = R \cap \{\ell_1, \ldots, \ell_k\}$

### Recall@k

$$
\mathrm{Recall@k} = \frac{|\text{hits}_k|}{|R|}
$$

Intuition:

- “Of all the relevant chunks that exist, how many did we retrieve in top-k?”
- High recall@k is important when missing evidence is costly.

### Precision@k

$$
\mathrm{Precision@k} = \frac{|\text{hits}_k|}{k}
$$

Intuition:

- “Of the k chunks we retrieved, how many are actually relevant?”
- Precision matters because too many irrelevant chunks add noise and can cause hallucinations.

### Hit rate (a.k.a. success@k)

For a single query:

$$
\mathrm{Hit@k} = \mathbb{1}[|\text{hits}_k| > 0]
$$

Over a dataset, hit rate is the mean of $\mathrm{Hit@k}$.

Intuition:

- “Did we get *at least one* correct chunk?”
- This is a good early metric because it’s easy to interpret.

### MRR (Mean Reciprocal Rank)

Define the rank of the first relevant item:

- $\mathrm{rank} = \min\{i : \ell_i \in R\}$ (or $\infty$ if none)

Reciprocal rank for one query:

$$
\mathrm{RR} = \begin{cases}
\frac{1}{\mathrm{rank}} & \text{if a relevant item is retrieved}\\
0 & \text{otherwise}
\end{cases}
$$

Then $\mathrm{MRR}$ is the mean of $\mathrm{RR}$ over all queries.

Intuition:

- MRR rewards “getting the right chunk early” (rank 1 is best).

---

## Worked example (k=5)

Suppose:

- relevant set $R = \{A, B\}$
- retrieved top-5 list $L_5 = [X, A, Y, Z, W]$

Then:

- $\text{hits}_5 = \{A\}$
- Recall@5 = $|\{A\}| / |\{A, B\}| = 1/2 = 0.5$
- Precision@5 = $|\{A\}| / 5 = 0.2$
- Hit@5 = 1 (because we retrieved at least one relevant)
- RR = 1/2 (first relevant is at rank 2)

This example shows why you want multiple metrics:

- Hit@k says “success!”
- precision shows the noise level
- recall shows you still missed relevant evidence

A practical implementation detail:

- for each query, store a list of acceptable `chunk_id` answers
- score a run by checking whether retrieved ids contain any acceptable id

---

## How to build an eval set

Include:

- easy in-KB questions
- confusing near-duplicates
- out-of-KB questions (should retrieve low-signal)

For each item, record:

- the query string
- expected `doc_id` or `chunk_id` (one or more)
- (optional) a short note explaining why it should be answerable

---

## Minimal eval artifact format

Store your eval set as JSONL (easy to diff and append):

```json
{"query": "What is RAG?", "relevant_chunk_ids": ["rag_intro#02"]}
{"query": "How do I start the API?", "relevant_chunk_ids": ["fastapi#001", "uvicorn#003"]}
```

---

## Minimal evaluation script (shape)

```python
import json
from pathlib import Path

def recall_at_k(retrieved: list[str], relevant: set[str]) -> float:
    if not relevant:
        return 0.0
    return 1.0 if any(r in relevant for r in retrieved) else 0.0

def main() -> None:
    items = [json.loads(line) for line in Path("eval_set.jsonl").read_text().splitlines() if line.strip()]

    # TODO: call your real /search endpoint or vector DB client here
    def run_search(query: str, top_k: int) -> list[str]:
        return []

    k = 5
    scores = []
    misses = []
    for item in items:
        retrieved_ids = run_search(item["query"], k)
        relevant = set(item.get("relevant_chunk_ids", []))
        s = recall_at_k(retrieved_ids, relevant)
        scores.append(s)
        if s == 0.0:
            misses.append({"query": item["query"], "retrieved": retrieved_ids, "relevant": list(relevant)})

    avg = sum(scores) / max(len(scores), 1)
    Path("output").mkdir(exist_ok=True)
    Path("output/metrics.json").write_text(json.dumps({"recall_at_k": avg, "k": k}, indent=2))
    Path("output/misses.json").write_text(json.dumps(misses, indent=2))
    print({"recall_at_k": avg, "k": k, "n": len(scores)})

if __name__ == "__main__":
    main()
```

This is enough to:

- establish a baseline
- test one change
- prove improvement (or regression)

---

## References

- IR evaluation concepts: https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html
- RAG overview: https://www.pinecone.io/learn/retrieval-augmented-generation/
- JSON Lines format: https://jsonlines.org/
- Precision and recall (definitions): https://en.wikipedia.org/wiki/Precision_and_recall
- Mean reciprocal rank (MRR): https://en.wikipedia.org/wiki/Mean_reciprocal_rank

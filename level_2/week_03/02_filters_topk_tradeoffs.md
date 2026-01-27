# Week 3 — Part 02: Filters + top-k tradeoffs and failure modes

## Overview

Filters and top-k are your primary retrieval controls.

- Filters improve precision.
- Higher `top_k` improves recall but increases noise.

---

## The tradeoff (with a concrete numeric example)

Assume for a given query there are $|R| = 4$ relevant chunks in your KB.

You run three retrieval settings:

### Case A: small `top_k`

- `filters = {"source": "docs"}` (correct)
- `top_k = 3`
- retrieved: $[A, B, X]$ where $A, B$ are relevant and $X$ is not

Metrics:

- $|\text{hits}_3| = 2$
- Precision@3 = $2/3 \approx 0.67$
- Recall@3 = $2/4 = 0.5$

Interpretation:

- great precision
- you are missing half the relevant evidence

### Case B: larger `top_k`

- same filter
- `top_k = 8`
- retrieved: $[A, B, X, Y, C, Z, W, V]$ where $A, B, C$ are relevant

Metrics:

- $|\text{hits}_8| = 3$
- Precision@8 = $3/8 = 0.375$
- Recall@8 = $3/4 = 0.75$

Interpretation:

- you improved recall (better chance the LLM sees the needed sentence)
- you added noise (risk of confusing the generator)

### Case C: wrong filter (precision may look fine, but you lose recall)

- `filters = {"source": "tickets"}` (wrong)
- `top_k = 3`
- retrieved: $[P, Q, R]$, none are relevant

Metrics:

- Hit@3 = 0
- Recall@3 = 0

Interpretation:

- the system is “confidently wrong” because retrieval is searching the wrong subset

---

## Practical tuning workflow

- Start with a baseline: `top_k = 5`, minimal filters.
- If you see consistent misses (Hit@k low):
  - increase `top_k` gradually (5 → 8 → 12)
  - reduce restrictive filters
- If you see the right doc but wrong passage:
  - keep filters, increase `top_k`
  - improve chunking/overlap (Week 2)
- If you see lots of irrelevant chunks:
  - add or tighten filters
  - reduce `top_k`

---

## Debugging checklist (fast)

- Confirm you embed queries and chunks with the same model.
- Log `top_k` and filters for every request.
- Log the retrieved list with:
  - `chunk_id`
  - `score`
  - `source/doc_id`
- For misses, inspect the top-10 texts directly.
- Validate metadata normalization (case, whitespace, missing fields).

## Common retrieval failure modes

- wrong filter → retrieves irrelevant subset
- no filter → retrieves “similar but irrelevant” content
- too small top_k → misses the relevant chunk
- too large top_k → chat receives too much noise
- filters stored inconsistently (e.g., `source` sometimes "Docs" and sometimes "docs")

---

## Practical filter design: keep it boring

Start with a small set of filters you know you need, for example:

- `source` ("docs", "tickets", "notion")
- `doc_id` (specific document)
- `version` (optional)

Avoid exposing complex boolean filter DSLs in Week 3. You can always evolve later.

Example request:

```json
{
  "query": "how do I run the service?",
  "top_k": 5,
  "filters": {"source": "docs"}
}
```

---

## Debugging habit

Always log:

- query text
- filters
- top_k
- list of retrieved chunk ids and sources

This makes failures inspectable.

Extra credit habit:

- print/log the first ~200 characters of each retrieved chunk
- include the `url` or `section` field if you store it

---

## References

- Chroma docs: https://docs.trychroma.com/
- Pinecone filtering concepts: https://www.pinecone.io/learn/metadata-filtering/
 - Precision and recall (definitions): https://en.wikipedia.org/wiki/Precision_and_recall

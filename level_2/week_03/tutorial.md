# Level 2 — Week 3 Tutorials

## Overview

Week 3 turns retrieval into a debuggable service component:

- expose `/search`
- support filters + top-k
- log retrieved chunks
- build a small query set and compute retrieval metrics

## Navigation

- [01 — Retrieval as an API (separate from chat)](01_retrieval_as_api.md)
- [02 — Filters + top-k tradeoffs and failure modes](02_filters_topk_tradeoffs.md)
- [03 — Minimal retrieval evaluation (hit rate, recall@k)](03_retrieval_evaluation.md)

## Recommended order

1. Read 01 and define `/search` request/response.
2. Read 02 and implement filters and logs.
3. Read 03 and build an eval set + script.

## What “done” looks like

- `/search` is a real endpoint with typed request/response models.
- You can pass `top_k` and optional `filters` and see them applied.
- Each `/search` call logs:
  - query
  - filters
  - top_k
  - returned `chunk_id` + `doc_id` (+ `url` if available)
- You have a small eval set (10–20 queries) saved to disk.
- You can run an eval script that writes `output/metrics.json` and `output/misses.json`.

## References

- FastAPI docs: https://fastapi.tiangolo.com/
- OpenAPI spec: https://spec.openapis.org/oas/latest.html
- Stanford IR book (evaluation): https://nlp.stanford.edu/IR-book/

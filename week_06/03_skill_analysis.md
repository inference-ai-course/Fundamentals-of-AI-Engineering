# Week 6 — Part 03: How the job-skill analysis works (evidence → LLM → report)

## Overview

The Week 6 capstone is a **Job Posting Skill Analyzer**, but the actual
"analysis" — identifying skills, clustering roles, ranking learning priorities —
does **not** happen with keyword counting. It happens in the **LLM stage**. Every
earlier stage exists to gather and compress *skill-relevant evidence* so the
model can reason over it cheaply and reproducibly.

Pipeline, viewed through a skill lens:

```text
job postings CSV
  -> profile             (which roles dominate? how much is missing?)
  -> compress            (cheap skill evidence: title counts, skill strings,
                          keyword frequency hints, sampled descriptions)
  -> LLM interpretation  (extract skills/tools, cluster roles,
                          rank learning priorities, suggest a path)
  -> report.json + report.md
```

**Lab notebook**: [03_skill_analysis.ipynb](./03_skill_analysis.ipynb) — runs the whole flow on the real 60-row sample.

---

## Where the skill analysis happens

| Stage | What it contributes to skill analysis |
|-------|----------------------------------------|
| **Load** | Brings in `job_description` (most skill signal) and `job_skills` (explicit skills, often empty). |
| **Profile** | Context, not skills: `top_job_titles`, missing rates, row counts. Tells the model what kind of roles dominate. |
| **Compress** | The "evidence-gathering" step: title/location counts, sampled `job_skills` strings, **keyword frequency hints**, and short representative descriptions. |
| **LLM** | The real analysis: extract and de-duplicate skills/tools, cluster roles, rank learning priorities, build a beginner path, propose projects. |
| **Report** | Maps the model's structured skill output into a stable `report.json` / `report.md`. |

The "intelligence" (extract → cluster → rank → sequence) lives in the LLM stage.
The pipeline's job is to make sure the model sees the **right evidence**, within
the token budget, every run.

---

## Step 1 — Gather skill evidence (cheap and deterministic)

Most skill signal is buried in `job_description` free text (e.g. "build
dashboards, write SQL queries"). A cheap first pass is a **keyword frequency
hint**: scan descriptions for a list of known skills and count how many postings
mention each one.

```python
import re

SKILL_KEYWORDS = [
    "python", "sql", "excel", "tableau", "power bi", "aws", "azure",
    "spark", "airflow", "docker", "kubernetes", "pandas", "scikit-learn",
    "tensorflow", "pytorch", "machine learning", "nlp", "etl",
    "data visualization", "statistics", "git", "communication", "dashboard",
]


def skill_frequency_hints(df, text_col="job_description", keywords=SKILL_KEYWORDS, top_k=15):
    texts = df[text_col].dropna().astype(str).str.lower()
    counts = {}
    for kw in keywords:
        pattern = r"\b" + re.escape(kw) + r"\b"
        n = int(texts.str.contains(pattern, regex=True).sum())
        if n:
            counts[kw] = n
    return dict(sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:top_k])
```

This is fast, free, and explainable. But it can only count **known terms**: it
cannot recognize synonyms ("writing SQL" vs "SQL queries"), cluster roles, or
build a learning path. Those need the LLM. So we use the hints as *evidence to
hand the model*, not as the final answer.

---

## Step 2 — Compress the evidence under the token budget

You cannot send 60 full descriptions to the model. Combine the cheap evidence
into a small, bounded object:

- `top_job_titles` (role distribution)
- `skill_keyword_hints` (from Step 1)
- a few **truncated** representative descriptions
- existing `job_skills` strings, if present

Then estimate tokens (~4 chars/token) and keep it well under ~2,000 tokens.
See [02_sampling_compression.md](./02_sampling_compression.md) for the
compression mechanics.

---

## Step 3 — Ask the LLM for structured skill analysis

The prompt instructs the model to return **JSON only**, grounded in the supplied
evidence. For this theme (see
[capstone_template/theme_examples/job_posting_schema.md](./capstone_template/theme_examples/job_posting_schema.md))
ask for:

| Field | Meaning | What the model is doing |
|-------|---------|--------------------------|
| `common_skills` | High-frequency technical skills | Generalize repeated skills across postings |
| `common_tools` | Tools / platforms / frameworks | Extract and de-duplicate tool names |
| `role_clusters` | Role families | Group similar titles + descriptions |
| `learning_priorities` | What a beginner should learn first | Rank by frequency + complementarity |
| `beginner_learning_path` | Ordered path | Sequence skills into a sensible order |
| `portfolio_project_ideas` | Practice projects | Map skills to buildable projects |

**Key rule:** tell the model to use *only the given evidence* and to report
uncertainty (small sample, truncated text) in `risk_notes`. This is what keeps a
"skill analyzer" from drifting into generic career advice.

---

## Step 4 — Validate the model output

Never trust raw model text. Parse and validate before using it:

- parse JSON from the raw response,
- check the required keys are present,
- coerce missing optional lists to `[]`,
- try **one** repair attempt, then fail with a clear error.

This is the same contract as
[capstone_template/src/llm_interpretation.py](./capstone_template/src/llm_interpretation.py)
(`validate_llm_output`).

---

## Step 5 — Map into the stable report schema

The skill fields live **inside** `llm_interpretation`; the top-level report keys
stay fixed so every run looks the same to a reviewer:

```text
report.json (top level, always present):
  metadata, dataset_summary, data_quality, compression_summary,
  llm_interpretation, recommendations, risk_notes, errors_or_warnings

llm_interpretation:
  common_skills, common_tools, role_clusters,
  learning_priorities, beginner_learning_path, portfolio_project_ideas
```

---

## Keyword frequency vs LLM: use both

| | Keyword frequency | LLM interpretation |
|---|---|---|
| Cost | Free | API cost + latency |
| Explainable | Yes (you can see the count) | Partially |
| Finds synonyms / new skills | No | Yes |
| Clusters roles, ranks, sequences | No | Yes |
| Can hallucinate | No | Yes |

The pipeline combines them: keyword hints are cheap, grounded evidence; the LLM
turns that evidence into clustered, ranked, human-readable guidance — and is
asked to stay within the evidence.

---

## Common failure points

- Compression drops tool names or rare roles → skills are under-counted. Keep
  edge-case samples.
- Descriptions truncated too aggressively → missing signal. Tune the truncation
  length.
- The model gives generic career advice instead of using the evidence → enforce
  "use only the supplied evidence" in the prompt.
- `job_skills` is empty but treated as populated → fall back to inferring skills
  from `job_description`.

---

## Self-check

- Which stage actually identifies the skills — and which stages only prepare
  evidence?
- If you removed the keyword hints, what could the LLM no longer ground its
  answer on?
- Are your skill fields nested inside `llm_interpretation` with the top-level
  report keys unchanged?
- Does your prompt force the model to stay within the supplied evidence?
- What does your project do when `job_skills` is empty?

---

## References

- Theme schema: [capstone_template/theme_examples/job_posting_schema.md](./capstone_template/theme_examples/job_posting_schema.md)
- Compression mechanics: [02_sampling_compression.md](./02_sampling_compression.md)
- LLM client + validation: [capstone_template/src/llm_interpretation.py](./capstone_template/src/llm_interpretation.py)

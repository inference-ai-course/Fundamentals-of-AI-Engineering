# Week 8 — Part 02: Retrospective / postmortem template

## Overview

A retrospective is a structured reflection:

- what went wrong
- why it went wrong
- what you changed
- what you’d do next

In engineering culture, “blameless postmortems” emphasize learning.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on the overall roadmap and prerequisites:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 Schedule](../../level_0/Schedule.md)

Why it matters here (Week 8):

- Retrospectives turn one-off failures into reusable rules you can apply in future systems.
- Keep it evidence-based: cite artifacts/logs and name concrete fixes.

---

## Complete retrospective template

Create `RETROSPECTIVE.md`:

````markdown
# Capstone Retrospective

**Date**: 2026-01-30  
**Duration**: 8 weeks  
**Project**: Data analysis pipeline with LLM insights

---

## What I built

Describe your system in 3–6 sentences:

**Example**:
> Built an automated data profiling pipeline that analyzes CSV files and generates insights using GPT-4. The system loads data, computes statistical profiles, compresses the representation to fit LLM context windows, calls the API with retry/backoff logic, and produces both JSON and Markdown reports. Key innovation: hierarchical compression that preserves distributions while staying under 2k tokens. The pipeline is reproducible (deterministic seeds), robust (handles failures gracefully), and production-ready (one-command runner with comprehensive logging).

**Your version**:
- What problem it solves:
- Input/output format:
- Pipeline stages (5-step flow):
- Key artifacts produced:

---

## What went well (with evidence)

### Success 1: Reproducible artifacts
**What**: Running the same CSV twice produces identical compressed inputs  
**Evidence**: `diff output_run1/03_compressed.json output_run2/03_compressed.json` shows no differences  
**Why it matters**: Makes debugging deterministic and results comparable

### Success 2: Graceful failure handling
**What**: Invalid CSV inputs produce clear error messages  
**Evidence**: Error logs show "Missing required columns: [age, email]" instead of cryptic stack traces  
**Why it matters**: Reduces support burden and speeds up user debugging

### Success 3: [Add your success]
**What**:  
**Evidence**:  
**Why it matters**:

---

## What went wrong (top 3)

### Issue 1: LLM returned invalid JSON

**Symptom**: Pipeline crashed with `json.JSONDecodeError` during report generation  
**When**: First 3 test runs with real data  
**Frequency**: 2 out of 10 calls (20% failure rate)  
**Evidence**: `output/04_llm_raw.json` contains partial JSON with trailing text  
**Impact**: Entire pipeline fails, losing all work up to that point

**Example error**:
```
JSONDecodeError: Expecting ',' delimiter: line 12 column 5 (char 234)
```

### Issue 2: Rate limit hit during benchmarking

**Symptom**: `429 Too Many Requests` errors  
**When**: Running benchmark with 10 models × 20 prompts  
**Frequency**: After ~50 requests  
**Evidence**: Logs show: `HTTP 429 at 2026-01-25 14:32:18`  
**Impact**: Benchmark incomplete, had to restart manually

### Issue 3: [Your issue]

**Symptom**:  
**When**:  
**Frequency**:  
**Evidence**:  
**Impact**:

---

## Root cause analysis

### Issue 1 root cause
**Surface cause**: LLM didn't follow JSON format instructions  
**Deeper cause**: Prompt didn't emphasize "return ONLY valid JSON, no extra text"  
**Generalizable lesson**: LLMs need explicit output format constraints, not just schema descriptions

### Issue 2 root cause
**Surface cause**: Exceeded OpenAI rate limits (60 RPM)  
**Deeper cause**: No client-side throttling, fired requests as fast as possible  
**Generalizable lesson**: Always implement client-side rate limiting before batch operations

### Issue 3 root cause
**Surface cause**:  
**Deeper cause**:  
**Generalizable lesson**:

---

## Fixes implemented

### Fix for Issue 1: JSON validation + repair
```python
# Before: naive parsing
result = json.loads(llm_response)

# After: validation with retry
try:
    result = json.loads(llm_response)
    validate_schema(result)  # Pydantic validation
except (json.JSONDecodeError, ValidationError):
    # Retry with stronger prompt
    result = retry_with_repair(llm_response, max_attempts=2)
```

**Files changed**: `src/llm_client.py` (lines 45-68)  
**Tests added**: `test_json_repair()` in `tests/test_llm.py`  
**Result**: 0/10 parse failures in subsequent runs

### Fix for Issue 2: Rate limiter
```python
# Added client-side rate limiting
from ratelimit import RateLimiter

limiter = RateLimiter(max_calls=50, period=60)  # 50 calls per minute

@limiter.limited
def call_llm(prompt):
    # API call here
```

**Files changed**: `src/llm_client.py`, `requirements.txt`  
**Tests added**: `test_rate_limiting()` - verifies delays  
**Result**: Benchmark completes without 429 errors

### Fix for Issue 3:
**Code changes**:  
**Files changed**:  
**Tests added**:  
**Result**:

---

## Metrics summary

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Success rate | 70% | 98% | +40% |
| Avg latency | 45s | 42s | -7% |
| JSON parse failures | 20% | 0% | -100% |
| Test coverage | 45% | 78% | +73% |
| Lines of code | 450 | 680 | +51% |

---

## What I would do next (Level 2 direction)

### Improvement 1: Evaluation dataset
**Problem**: No way to measure if changes improve quality  
**Solution**: Create 20-30 sample CSVs with known patterns (missing data, outliers, etc.)  
**Success metric**: Track how many issues the LLM correctly identifies  
**Effort**: 1 week

### Improvement 2: Multi-model comparison
**Problem**: Locked into single model/provider  
**Solution**: Abstract LLM interface, add Claude/Gemini support  
**Success metric**: Can swap models with 1 CLI flag  
**Effort**: 3 days

### Improvement 3: [Your improvement]
**Problem**:  
**Solution**:  
**Success metric**:  
**Effort**:

---

## Key lessons (reusable rules)

1. **Save intermediate artifacts at every stage**  
   → Debugging becomes inspection, not guesswork

2. **Validate LLM outputs before using them**  
   → Structured output ≠ guaranteed valid output

3. **Client-side rate limiting prevents 429s**  
   → Don't trust "rate limit should be enough"

4. **Dry-run mode enables fast iteration**  
   → Mock LLM responses for testing pipeline logic

5. **Deterministic compression aids debugging**  
   → Same input + same seed = same compressed output

6. **[Your lesson]**  
   → 

---

## Time breakdown

| Week | Focus | Hours | Notes |
|------|-------|-------|-------|
| 1 | Environment + profiling | 8 | Fought with pandas versions |
| 2 | ML baseline | 10 | Week 2 content, good foundation |
| 3 | LLM integration | 12 | Most time on prompt engineering |
| 4 | Robustness (retry/cache) | 15 | Added retry logic, caching |
| 5 | Local inference | 6 | Ollama setup straightforward |
| 6 | Pipeline refactor | 14 | Rewrote as staged pipeline |
| 7 | CLI + testing | 10 | Added pytest suite |
| 8 | Demo prep + polish | 9 | README, smoke tests |

**Total**: ~84 hours over 8 weeks (~10.5 hrs/week)

---

## Reflection

**What surprised me**:  
LLM reliability was lower than expected - needed multiple layers of validation and retry logic.

**What I underestimated**:  
Time spent on error handling and edge cases (40% of total dev time).

**What I'd tell past-me**:  
"Start with artifact saving from day 1. You'll thank yourself when debugging."

**Proudest moment**:  
When the pipeline handled a 50MB CSV gracefully through smart sampling and compression.

---

## Appendix: Artifacts

- Code: `https://github.com/username/capstone`
- Demo video: `demo.mp4` (5 min)
- Sample outputs: `examples/` directory
- Test coverage report: `htmlcov/index.html`

---

## Analysis framework (5 Whys)

For each issue, ask "why" 5 times:

**Example**:
1. **Why did pipeline crash?** → JSON parse error
2. **Why JSON parse error?** → LLM returned text after JSON
3. **Why did LLM add extra text?** → Prompt wasn't explicit about format
4. **Why wasn't prompt explicit?** → Assumed "return JSON" was clear enough
5. **Why make that assumption?** → Didn't test with enough diverse prompts

**Root cause**: Insufficient prompt testing + validation

---

## Practice notebook

For retrospective writing exercises, see:
- **[02_retrospective_template.ipynb](./02_retrospective_template.ipynb)** - Interactive retrospective guide
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## References

- Google SRE postmortem culture: https://sre.google/sre-book/postmortem-culture/

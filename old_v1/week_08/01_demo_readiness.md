# Week 8 — Part 01: Demo readiness checklist + README polishing

## Overview

A demo is successful when another person can reproduce it.

---

## Pre-study (Self-learn)

Foundations Course assumes Self-learn is complete. If you need a refresher on the overall roadmap and prerequisites:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn Schedule](../self_learn/Schedule.md)

Why it matters here (Week 8):

- A demo is a reproducibility test: “fresh clone + README steps” should work without magic steps.
- A failure-case story with saved artifacts/logs increases credibility and shows system understanding.

---

## Demo readiness checklist

### ✅ Repository setup
- [ ] README.md exists with clear instructions
- [ ] `.gitignore` includes `.env`, `__pycache__`, `*.pyc`, output directories
- [ ] `requirements.txt` with pinned versions
- [ ] `.env.example` with all required variables (no actual secrets)
- [ ] Sample data included (or clear instructions to generate)
- [ ] All code is committed and pushed

### ✅ Fresh clone test
- [ ] Clone to new directory
- [ ] Follow README from scratch
- [ ] All commands work without modification
- [ ] Outputs match expectations

### ✅ Documentation
- [ ] Setup section (environment, dependencies, secrets)
- [ ] Run section (one command to run pipeline)
- [ ] Expected outputs listed with file paths
- [ ] Troubleshooting section with common issues
- [ ] Performance notes (expected runtime)

### ✅ Demonstration script
- [ ] Demo runs without code editing
- [ ] Happy path works reliably
- [ ] One failure case prepared (with clear recovery)
- [ ] Logs/artifacts available for inspection

---

## Complete README template

````markdown
# Data Analysis Capstone

**Goal**: Automated data profiling and analysis using LLMs.

## Quick Start

```bash
# 1. Clone and enter directory
git clone <your-repo>
cd capstone

# 2. Create environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure secrets
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Run on sample data
python run_capstone.py --input data/sample.csv
```

## Expected Output

The pipeline creates these artifacts in `output/`:

```
output/
  01_loaded.parquet      # Loaded data (82.5 KB)
  02_profile.json        # Data profile (2.1 KB)
  03_compressed.json     # Compressed input for LLM (1.8 KB)
  04_llm_raw.json        # Raw LLM response (3.4 KB)
  05_report.json         # Final structured report (4.2 KB)
  05_report.md           # Human-readable report
```

**Sample `05_report.md`**:
```markdown
# Data Analysis Report

Dataset: 1,247 rows × 8 columns

## Key Insights
- Missing data in 'email' column (23% of rows)
- Purchase amounts range $5-$1,204
- Top 3 categories: Electronics (42%), Books (31%), Home (18%)

## Recommendations
1. Investigate missing email addresses
2. Review outlier purchases >$1000
3. Consider targeted campaigns for underrepresented categories
```

## Performance

**Typical runtime**: 45-60 seconds
- Data loading: <1s
- Profiling: 2-3s  
- LLM call: 30-40s (first call slower due to model loading)
- Report generation: <1s

**Hardware tested**: MacBook Pro M1, 16GB RAM

## Options

```bash
python run_capstone.py --help
```

Key flags:
- `--input FILE` - Input CSV (required)
- `--output_dir DIR` - Output directory (default: output)
- `--model NAME` - LLM model (default: gpt-4o-mini)
- `--sample-size N` - Sample rows for compression (default: 5)
- `--dry-run` - Test pipeline without calling LLM

## Troubleshooting

### Error: "File not found: .env"
**Solution**: Copy `.env.example` to `.env` and add your API key

```bash
cp .env.example .env
# Edit .env and set OPENAI_API_KEY=your_key_here
```

### Error: "Missing required columns"
**Solution**: Your CSV must have these columns: `id`, `value`, `category`

Check sample data format:
```bash
head -5 data/sample.csv
```

### Slow performance
**Causes**:
- First LLM call (model loading): expected
- Large dataset: reduce `--sample-size`
- Slow network: check internet connection

## Project Structure

```
capstone/
  src/
    pipeline.py         # Main pipeline logic
    profile.py          # Data profiling
    compress.py         # Compression for LLM
    llm_client.py       # LLM API wrapper
  tests/
    test_pipeline.py    # Unit tests
  data/
    sample.csv          # Sample data
  run_capstone.py       # CLI entry point
  requirements.txt      # Dependencies
  .env.example          # Environment template
  README.md             # This file
```

## Development

**Run tests**:
```bash
pytest
```

**Run with coverage**:
```bash
pytest --cov=src
```

**Smoke test** (quick validation):
```bash
bash smoke_test.sh
```

## Dependencies

Key packages (see `requirements.txt` for full list):
- `pandas==2.1.3` - Data manipulation
- `openai==1.6.1` - LLM API client
- `python-dotenv==1.0.0` - Environment management
- `pydantic==2.5.2` - Data validation

## License

MIT
````

---

## Demo script (what to show)

### 1. Fresh setup (2 min)
```bash
# Show README
cat README.md | head -20

# Show environment setup
python -m venv demo_env
source demo_env/bin/activate
pip install -r requirements.txt

# Show .env configuration
cat .env.example
# (mention: "In real demo, I already have API key configured")
```

### 2. Happy path run (1 min)
```bash
# Show input data
head -10 data/sample.csv

# Run pipeline
python run_capstone.py --input data/sample.csv

# Show outputs
ls -lh output/
cat output/05_report.md
```

### 3. Show artifacts (1 min)
```bash
# Compressed input (what we send to LLM)
cat output/03_compressed.json | jq .

# Raw LLM response
cat output/04_llm_raw.json | jq .
```

### 4. Failure case demonstration (1 min)
```bash
# Missing file error
python run_capstone.py --input nonexistent.csv
# Show clear error message

# Empty CSV error  
touch empty.csv
python run_capstone.py --input empty.csv
# Show validation error
```

### 5. Show tests (30 sec)
```bash
pytest -v
# Show passing tests
```

**Total demo time**: ~5-6 minutes

---

## Pre-demo checklist (day before)

- [ ] Test fresh clone on different machine
- [ ] Verify API key works
- [ ] Test with stable internet connection
- [ ] Prepare backup sample data
- [ ] Take screenshots of expected outputs
- [ ] Rehearse demo script (time it)
- [ ] Prepare answers to likely questions:
  - "What if the LLM returns invalid JSON?"
  - "How do you handle rate limits?"
  - "Can it work with different data schemas?"

---

## Common demo mistakes to avoid

❌ **Don't**:
- Edit code during demo
- Use hardcoded paths specific to your machine
- Rely on cached data from previous runs
- Skip error handling demonstration
- Forget to show actual LLM output

✅ **Do**:
- Run from scratch (fresh clone if possible)
- Show both success and failure cases
- Explain design decisions briefly
- Have artifacts ready to inspect
- Keep demo under 10 minutes

---

## Exercise: Write demo notes

Goal:

- Implement `demo_notes_todo()`.
- Save the result to `output/DEMO_NOTES.md`.

Checkpoint:

- The file includes a "Happy path" section and a "Failure case" section.

---

## Self-check

- Can a teammate run your demo without asking you questions?
- Can you demo without editing code live?
- Does your demo complete in <10 minutes?
- Have you tested on a fresh machine/environment?
- Do you have a backup plan if API fails during demo?

---

## References

- GitHub on READMEs: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- Demo best practices: https://github.com/readme/guides/technical-demos

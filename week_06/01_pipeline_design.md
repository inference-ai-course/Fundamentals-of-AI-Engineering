# Week 6 — Part 01: From scripts to pipelines (stages + artifacts)

## Overview

A pipeline is a sequence of stages.

For Week 6, the pipeline powers a **Job Posting Skill Analyzer**:

```text
job postings CSV -> profile -> compressed skill summary -> LLM interpretation -> report.json + report.md
```

Each stage should have:

- clear inputs
- clear outputs
- a single responsibility

This structure improves:

- debugging (you can isolate failures)
- reproducibility (you save intermediate artifacts)

---


**Lab notebook**: [01_pipeline_design.ipynb](./01_pipeline_design.ipynb) - Interactive coding practice

## Pre-study (Self-learn)

Self-learn is optional. If you want a refresher on pipeline structure, artifacts, and basic AI engineering workflow:

- [Pre-study index (Foundations Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)

Why it matters here (Week 6):

- The project becomes debuggable when you can isolate stages and inspect intermediate artifacts.
- Explicit stage contracts make it easier to re-run only what changed (faster iteration).

---

## Suggested project stages

For each stage, aim to make the contract explicit.

1. **Load**
    - **Inputs**: a job postings CSV such as `data/sample_job_postings.csv`
    - **Outputs**: an in-memory dataframe/table OR a saved intermediate like `output/loaded.parquet`
    - **Common pitfalls**: silent dtype changes, unexpected delimiters/encodings, missing columns that only fail later.

2. **Profile**
    - **Inputs**: loaded table
    - **Outputs**: `output/profile.json` (machine-readable) and optionally `output/profile.md` (human-readable)
    - **What “profile” means**: row/column counts, missing values per column, top job titles, top locations, text-length notes, and any basic numeric/categorical stats.

3. **Compress**
    - **Inputs**: table + profiling results
    - **Outputs**: `output/compressed_input.json`
    - **Goal**: fit the most decision-relevant job-skill evidence into a bounded context window.
    - **Common pitfalls**: sending full job descriptions in bulk; sampling that drops rare-but-important roles; summaries that remove tool names or role context.

4. **LLM**
    - **Inputs**: prompt template + `output/compressed_input.json`
    - **Outputs**: `output/llm_prompt.txt` and `output/llm_raw_response.txt`; validated parsed output feeds the report stage
    - **Common pitfalls**: asking for generic career advice instead of evidence from the compressed job postings; calling the model without saving the exact prompt/context; not handling timeouts/429s.

5. **Report**
    - **Inputs**: validated LLM output + (optional) original profile
    - **Outputs**: `output/report.json` and `output/report.md`
    - **Goal**: produce a stable, demo-friendly artifact with predictable keys/sections.

A useful rule of thumb: if a stage fails, you should still have the previous stage’s artifact saved so you can debug without re-running everything.

For Foundations Course, this can all be in one script, but you should treat these stages explicitly.

Artifact mindset (recommended):

- every stage writes an output file in a predictable location
- later stages read those files instead of re-computing silently

This makes your pipeline debuggable even when the LLM call fails or is rate-limited.

---

## Concrete implementation example

```python
from pathlib import Path
from typing import Optional
import json
import pandas as pd


class ProjectRunner:
    """
    Pipeline coordinator with stage isolation.
    """
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def run_all(self, input_csv: Path) -> None:
        """
        Run all stages in sequence, saving artifacts at each step.
        """
        print("Stage 1: Load")
        df = self.stage_load(input_csv)
        
        print("Stage 2: Profile")
        profile = self.stage_profile(df)
        
        print("Stage 3: Compress")
        compressed = self.stage_compress(df, profile)
        
        print("Stage 4: LLM")
        llm_output = self.stage_llm(compressed)
        
        print("Stage 5: Report")
        self.stage_report(llm_output, profile)
        
        print(f"\nPipeline complete. Outputs in: {self.output_dir}")
    
    def stage_load(self, input_csv: Path) -> pd.DataFrame:
        """
        Load CSV and save intermediate artifact.
        """
        if not input_csv.exists():
            raise FileNotFoundError(f"Input not found: {input_csv}")
        
        df = pd.read_csv(input_csv)
        
        # Save intermediate artifact
        artifact_path = self.output_dir / "01_loaded.parquet"
        df.to_parquet(artifact_path)
        print(f"  → Saved: {artifact_path}")
        
        return df
    
    def stage_profile(self, df: pd.DataFrame) -> dict:
        """
        Profile data and save results.
        """
        profile = {
            "row_count": len(df),
            "column_count": len(df.columns),
            "columns": list(df.columns),
            "missing_values": df.isna().sum().to_dict(),
            # Job Posting Skill Analyzer: a cheap, decision-relevant summary.
            "top_job_titles": (
                df["job_title"].value_counts().head(10).to_dict()
                if "job_title" in df.columns
                else {}
            ),
        }
        
        artifact_path = self.output_dir / "profile.json"
        artifact_path.write_text(json.dumps(profile, indent=2))
        print(f"  → Saved: {artifact_path}")
        
        return profile
    
    def stage_compress(self, df: pd.DataFrame, profile: dict) -> dict:
        """
        Create compressed representation for LLM.
        """
        sample = df.sample(n=min(5, len(df)), random_state=42)
        
        compressed = {
            "profile_summary": {
                "dataset_shape": [profile["row_count"], profile["column_count"]],
                "columns": profile["columns"],
            },
            "sample_rows": sample.to_dict(orient="records"),
        }
        
        artifact_path = self.output_dir / "compressed_input.json"
        artifact_path.write_text(json.dumps(compressed, indent=2))
        print(f"  → Saved: {artifact_path}")
        
        return compressed
    
    def stage_llm(self, compressed: dict) -> dict:
        """
        Call LLM with compressed input.
        """
        # Debug-only placeholder. Final capstone submissions must call a real LLM.
        prompt = f"Analyze these job postings and identify common skills:\n{json.dumps(compressed, indent=2)}"
        
        # Save the prompt
        (self.output_dir / "llm_prompt.txt").write_text(prompt)
        
        # Simulate LLM response for local pipeline debugging only.
        llm_response = {
            "summary": "Example job skill analysis",
            "insights": ["Python and SQL appear across several roles", "Dashboards and communication are recurring requirements"],
            "recommendations": ["Prioritize SQL, Python, dashboarding, and project documentation"],
            "risk_notes": ["Small sample; do not treat this as a full labor-market study"],
        }
        
        # Save raw response
        artifact_path = self.output_dir / "llm_raw_response.txt"
        artifact_path.write_text(json.dumps(llm_response, indent=2))
        print(f"  → Saved: {artifact_path}")
        
        return llm_response
    
    def stage_report(self, llm_output: dict, profile: dict) -> None:
        """
        Generate final report.
        """
        report = {
            "metadata": {},
            "dataset_summary": {
                "rows": profile["row_count"],
                "columns": profile["column_count"],
            },
            "data_quality": {},
            "compression_summary": {},
            "llm_interpretation": {
                "summary": llm_output.get("summary", ""),
                "insights": llm_output.get("insights", []),
            },
            "recommendations": llm_output.get("recommendations", []),
            "risk_notes": llm_output.get("risk_notes", []),
            "errors_or_warnings": [],
        }
        
        # JSON report
        json_path = self.output_dir / "report.json"
        json_path.write_text(json.dumps(report, indent=2))
        
        # Markdown report
        md_lines = [
            "# Job Posting Skill Analysis Report",
            "",
            f"- Rows: {profile['row_count']}",
            f"- Columns: {profile['column_count']}",
            "",
            "## LLM Interpretation",
            "",
            llm_output.get("summary", ""),
        ]
        
        md_path = self.output_dir / "report.md"
        md_path.write_text("\n".join(md_lines))
        
        print(f"  → Saved: {json_path}")
        print(f"  → Saved: {md_path}")


# Usage
if __name__ == "__main__":
    runner = ProjectRunner(output_dir=Path("output"))
    runner.run_all(input_csv=Path("data/sample_job_postings.csv"))
```

---

## Debugging with artifacts

**Scenario 1: LLM call fails**

Because each stage saves artifacts, you can:

```python
# Re-run only the LLM stage
compressed = json.loads(Path("output/compressed_input.json").read_text())
llm_output = runner.stage_llm(compressed)
```

**Scenario 2: Profile looks wrong**

Inspect the intermediate artifact:

```bash
cat output/profile.json
# Check if columns/missing values match expectations
```

**Scenario 3: Want to modify compression**

```python
# Load from stage 1 artifact
df = pd.read_parquet("output/01_loaded.parquet")

# Modify compression logic
compressed = stage_compress(df, profile)  # with new logic

# Continue from stage 4
llm_output = stage_llm(compressed)
```

---

## Artifact naming convention

Use the same filenames as the capstone template so lessons and final project match:

```text
output/
  profile.json             # Stage 2 output
  compressed_input.json    # Stage 3 output
  llm_prompt.txt           # Stage 4 input
  llm_raw_response.txt     # Stage 4 output
  report.json              # Stage 5 output (final)
  report.md                # Stage 5 output (final)
```

**Why stable names help:**
- They match `capstone_template/README.md`
- Students can re-run one command and know which files to inspect
- Reviewers can check the same output contract across projects

---

## Isolation benefits

**Development velocity:**
- Change compression logic without re-profiling
- Iterate on prompts without re-loading data
- Test report generation without calling LLM

**Cost control:**
- Don't re-call expensive LLM on every debug iteration
- Cache artifacts from successful stages

**Debuggability:**
- Each artifact is inspectable
- Can trace failures to specific stage
- Evidence survives crashes

---

## Practice notebook

For hands-on pipeline building exercises, see:
- **[01_pipeline_design.ipynb](./01_pipeline_design.ipynb)** - Interactive pipeline implementation

---

## Self-check

- If the LLM call fails, do you still have the profiling artifact?
- Can you re-run only the LLM stage with the saved compressed input?
- Can you trace each artifact back to its generating stage?
- If you modify stage 3 logic, can you skip stages 1-2?

---

## References

- Twelve-Factor logs/config mindset: https://12factor.net/
- Pipeline patterns: https://en.wikipedia.org/wiki/Pipeline_(software)

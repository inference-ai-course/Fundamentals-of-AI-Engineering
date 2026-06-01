# Week 6 — Simplified Data Analysis Project

## Overview

This is a simplified end-to-end project that integrates knowledge from Weeks 1-5. You'll build a complete data analysis pipeline that:

1. Loads and profiles data (Week 4 skills)
2. Compresses data for LLM consumption (Week 6 skills)
3. Calls LLM with structured prompts (Week 3 + Week 6 skills)
4. Generates reports (Week 4 skills)

## Project Requirements

### Functional Requirements

- Accept a CSV file as input
- Generate a data profile (rows, columns, missing values, basic stats)
- Compress the data to fit within LLM context window
- Call LLM to analyze the data
- Produce structured output (JSON) and human-readable report (Markdown)

### Technical Requirements

- Use the LLM client built in Week 3 (with timeout, retry, caching)
- Implement pipeline stages with clear inputs/outputs
- Save intermediate artifacts at each stage
- Handle errors gracefully
- Validate LLM outputs against a schema

## Suggested Pipeline Stages

### Stage 1: Load
- **Input**: CSV file path
- **Output**: DataFrame + `output/01_loaded.parquet`
- **Validation**: Check file exists, not empty

### Stage 2: Profile
- **Input**: DataFrame
- **Output**: Profile dict + `output/02_profile.json`
- **Contents**: Row count, column count, dtypes, missing values, numeric summaries

### Stage 3: Compress
- **Input**: DataFrame + Profile
- **Output**: Compressed representation + `output/03_compressed.json`
- **Strategy**: Sample rows + summary statistics + categorical frequencies
- **Constraint**: Must fit within ~2000 tokens

### Stage 4: LLM Analysis
- **Input**: Compressed data + prompt template
- **Output**: Raw LLM response + `output/04_llm_raw.json`
- **Processing**: Parse JSON, validate schema, retry if invalid

### Stage 5: Report
- **Input**: Validated LLM output + Profile
- **Output**: Final reports `output/05_report.json` and `output/05_report.md`

## Prompt Template

```
You are a data analysis assistant.

Task:
Analyze the provided dataset and identify:
1. Key patterns or trends
2. Potential data quality issues
3. Actionable insights

Input Data:
{{compressed_data}}

Output Format:
Return ONLY valid JSON with exactly these keys:
{
  "summary": "string - one paragraph overview",
  "patterns": ["string - list of 3-5 patterns observed"],
  "quality_issues": ["string - list of data quality issues"],
  "insights": ["string - list of actionable insights"],
  "confidence": "number 0-1 - confidence in analysis"
}

Constraints:
- No markdown
- No additional keys
- Use empty arrays [] if no issues/insights found
- Confidence must be between 0 and 1
```

## Output Schema (Pydantic)

```python
from typing import List
from pydantic import BaseModel

class DataAnalysisReport(BaseModel):
    summary: str
    patterns: List[str]
    quality_issues: List[str]
    insights: List[str]
    confidence: float
```

## Project Structure

```
project/
├── README.md              # Setup and usage instructions
├── requirements.txt       # pandas, pydantic, requests, etc.
├── config.py             # Configuration (model name, timeouts, etc.)
├── main.py               # Entry point
├── pipeline.py           # Pipeline orchestration
├── stages/
│   ├── __init__.py
│   ├── load.py          # Stage 1
│   ├── profile.py       # Stage 2
│   ├── compress.py      # Stage 3
│   ├── llm_analysis.py  # Stage 4
│   └── report.py        # Stage 5
├── llm_client.py        # From Week 3
└── prompts.py           # Prompt templates
```

## Acceptance Criteria

- [ ] Can process a CSV file end-to-end
- [ ] All 5 stages produce artifacts in `output/`
- [ ] LLM output is validated against schema
- [ ] Reports are generated (JSON + Markdown)
- [ ] Pipeline can resume from any stage (reads previous artifacts)
- [ ] Handles errors gracefully (missing file, invalid CSV, LLM failure)
- [ ] Includes at least 3 retry attempts for LLM calls
- [ ] Uses caching to avoid redundant LLM calls

## Evaluation Criteria (25% of total grade)

### Project Completion (40%)
- Complete end-to-end workflow
- Functions run normally
- Output results meet expectations

### Prompt Design Quality (20%)
- Clear and effective prompts
- Well-structured output schema
- Proper constraints and validation

### Project Presentation (20%)
- Clear expression
- Complete demonstration
- Ability to answer questions

### Project Reflection (20%)
- Summary of learning gains
- Identification of shortcomings
- Proposal of improvement directions

## Sample Datasets

For testing, use these sample datasets:

1. **Small Dataset** (50 rows, 5 columns)
   - For quick iteration and testing

2. **Medium Dataset** (1000 rows, 10 columns)
   - Tests compression and sampling logic

3. **Dataset with Issues**
   - Missing values, outliers, inconsistent types
   - Tests error handling and quality detection

## Tips for Success

1. **Start Simple**: Get basic pipeline working first, then add features
2. **Test Incrementally**: Verify each stage before moving to next
3. **Save Everything**: Intermediate artifacts are your debugging lifeline
4. **Handle Errors**: Think about what can go wrong at each stage
5. **Document**: Write clear README so others can run your project

## References

- Week 3: LLM client with retry/caching
- Week 4: Data profiling techniques
- Week 6: Tokens/context, prompt contracts, structured outputs, pipeline design, sampling/compression

---

**Estimated Time**: 4-6 hours
**Due**: End of Week 6

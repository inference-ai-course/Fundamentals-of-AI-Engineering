# Week 6 — Part 04: End-to-end capstone runner (one command)

## Overview

Your capstone should run with **one command**.

That means:

- clear CLI flags
- predictable outputs
- stable artifact locations

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on reproducibility and pipeline contracts:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Chapter 2: Python and Environment Management](../self_learn/Chapters/2/Chapter2.md)
- [Self-learn — Chapter 3: AI Engineering Fundamentals](../self_learn/Chapters/3/Chapter3.md)

Why it matters here (Week 6):

- A one-command runner is the practical test of reproducibility for your capstone.
- Stable inputs/config → predictable artifact locations makes demos and smoke tests feasible.

---

## Complete CLI implementation

```python
import argparse
import sys
from pathlib import Path
import json
import pandas as pd


def build_parser() -> argparse.ArgumentParser:
    """
    Build argument parser with clear help text.
    """
    parser = argparse.ArgumentParser(
        description="Run data analysis capstone pipeline end-to-end",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python run_capstone.py --input data.csv
  python run_capstone.py --input data.csv --output_dir results --model gpt-4
  
Output artifacts:
  - output/01_loaded.parquet
  - output/02_profile.json
  - output/03_compressed.json
  - output/04_llm_raw.json
  - output/05_report.json
  - output/05_report.md
""")
    
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Input CSV file path"
    )
    parser.add_argument(
        "--output_dir",
        type=Path,
        default=Path("output"),
        help="Output directory for artifacts (default: output)"
    )
    parser.add_argument(
        "--model",
        default="gpt-4o-mini",
        help="Model name for LLM call (default: gpt-4o-mini)"
    )
    parser.add_argument(
        "--sample_size",
        type=int,
        default=5,
        help="Number of sample rows for compression (default: 5)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run without calling LLM (for testing pipeline)"
    )
    
    return parser


def validate_args(args) -> None:
    """
    Validate arguments and fail early with clear errors.
    """
    if not args.input.exists():
        raise FileNotFoundError(
            f"Input file not found: {args.input}\n"
            f"Please provide a valid CSV file path."
        )
    
    if args.input.suffix.lower() != '.csv':
        raise ValueError(
            f"Input file must be CSV, got: {args.input.suffix}\n"
            f"File: {args.input}"
        )
    
    if args.sample_size < 1:
        raise ValueError(
            f"Sample size must be >= 1, got: {args.sample_size}"
        )


def main() -> int:
    """
    Main entry point. Returns 0 on success, 1 on error.
    """
    parser = build_parser()
    args = parser.parse_args()
    
    try:
        # Validate arguments
        validate_args(args)
        
        # Create output directory
        args.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Run pipeline
        from capstone_pipeline import CapstoneRunner
        
        runner = CapstoneRunner(
            output_dir=args.output_dir,
            model=args.model,
            sample_size=args.sample_size,
            seed=args.seed,
            dry_run=args.dry_run
        )
        
        print(f"Running capstone pipeline...")
        print(f"  Input: {args.input}")
        print(f"  Output: {args.output_dir}")
        print(f"  Model: {args.model}")
        if args.dry_run:
            print(f"  Mode: DRY RUN (no LLM call)")
        print()
        
        runner.run_all(args.input)
        
        print("\n✓ Pipeline completed successfully")
        print(f"  Results in: {args.output_dir}")
        return 0
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        print("\nIntermediate artifacts may be in:", args.output_dir)
        return 1


if __name__ == "__main__":
    sys.exit(main())
```

---

## Example usage patterns

### Basic run
```bash
python run_capstone.py --input data.csv
```

### Custom output location
```bash
python run_capstone.py --input data.csv --output_dir results/experiment_01
```

### Different model
```bash
python run_capstone.py --input data.csv --model gpt-4
```

### Dry run (test pipeline without LLM)
```bash
python run_capstone.py --input data.csv --dry-run
```

### Full customization
```bash
python run_capstone.py \
  --input data.csv \
  --output_dir results/exp_$(date +%Y%m%d_%H%M%S) \
  --model gpt-4o-mini \
  --sample_size 10 \
  --seed 123
```

---

## Output contract

### Required outputs
The command **must** write:
- `output/05_report.json` - Final structured report
- `output/05_report.md` - Human-readable report

### Recommended intermediate artifacts
For debuggability:
- `output/01_loaded.parquet` - Loaded data
- `output/02_profile.json` - Data profile
- `output/03_compressed.json` - Compressed input for LLM
- `output/04_llm_prompt.txt` - Exact prompt sent to LLM
- `output/04_llm_raw.json` - Raw LLM response

**Why intermediate artifacts matter:**
- LLM call fails → still have profile + compressed input
- Prompt needs tuning → can inspect exact text sent
- Results look wrong → can trace back through pipeline

---

## Graceful failure patterns

### Pattern 1: Early validation
```python
def validate_input_early(input_path: Path) -> None:
    """
    Fail fast with clear error before expensive operations.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input not found: {input_path}")
    
    # Load just header to check schema
    df_head = pd.read_csv(input_path, nrows=0)
    
    if len(df_head.columns) == 0:
        raise ValueError(f"CSV has no columns: {input_path}")
```

### Pattern 2: Partial success
```python
def run_with_checkpoints(input_csv: Path, output_dir: Path) -> None:
    """
    Save artifacts at each stage so partial progress is visible.
    """
    try:
        # Stage 1
        df = stage_load(input_csv)
        (output_dir / "01_loaded.parquet").write(...)  # ✓ Saved
        
        # Stage 2
        profile = stage_profile(df)
        (output_dir / "02_profile.json").write(...)  # ✓ Saved
        
        # Stage 3
        compressed = stage_compress(df, profile)
        (output_dir / "03_compressed.json").write(...)  # ✓ Saved
        
        # Stage 4 (may fail)
        llm_output = stage_llm(compressed)  # ← Fails here
        
    except Exception as e:
        print(f"\nPipeline failed at stage 4: {e}")
        print(f"Intermediate artifacts saved to: {output_dir}")
        print("You can debug using the saved artifacts")
        raise
```

### Pattern 3: Dry run mode
```python
class CapstoneRunner:
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
    
    def stage_llm(self, compressed: dict) -> dict:
        """
        LLM call with dry-run support.
        """
        if self.dry_run:
            # Return mock response for testing
            return {
                "analysis": "DRY RUN - No actual LLM call made",
                "insights": ["This is a test run"],
            }
        
        # Real LLM call
        return call_real_llm(compressed)
```

---

## README template

Your repo should include this information:

````markdown
# Data Analysis Capstone

## Setup

```bash
# Create environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure secrets
cp .env.example .env
# Edit .env and add your API key
```

## Run

```bash
python run_capstone.py --input data/sample.csv
```

## Outputs

- `output/05_report.json` - Structured analysis
- `output/05_report.md` - Human-readable report

## Options

```bash
python run_capstone.py --help
```

## Troubleshooting

**Error: "Input file not found"**
- Check file path is correct
- Ensure file exists: `ls data/sample.csv`

**Error: "LLM call failed"**
- Check `.env` has valid API key
- Check network connection
- Intermediate artifacts saved to `output/` for debugging
````

---

## Practice notebook

For hands-on runner implementation and CLI exercises, see:
- **[04_capstone_runner.ipynb](./04_capstone_runner.ipynb)** - Interactive runner development
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- Can you run from a fresh folder after following README steps?
- If the model call fails, do you still get intermediate outputs?
- Does `--help` provide clear usage instructions?
- Can a teammate run your pipeline without asking questions?

---

## References

- Python `argparse`: https://docs.python.org/3/library/argparse.html
- Python `sys.exit()`: https://docs.python.org/3/library/sys.html#sys.exit
- Click (alternative CLI library): https://click.palletsprojects.com/

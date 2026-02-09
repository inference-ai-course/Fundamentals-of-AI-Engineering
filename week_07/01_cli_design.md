# Week 7 — Part 01: CLI design (argparse) + good defaults

## Overview

Your CLI is an interface like an API.

A good CLI:

- makes correct usage easy
- makes incorrect usage obvious
- documents itself via `--help`

---

## Pre-study (Self-learn)

Foundamental Course assumes Self-learn is complete. If you need a refresher on Python modules, exceptions, and CLI-adjacent habits:

- [Pre-study index (Foundamental Course → Self-learn)](../PRESTUDY.md)
- [Self-learn — Modules and exception handling](../../self_learn/Chapters/2/02_modules_exceptions.md)

Why it matters here (Week 7):

- A stable CLI makes demos, smoke tests, and README instructions repeatable.
- Good defaults and clear errors reduce “support time” and speed up debugging.

## Minimum CLI checklist

- descriptive help text
- sensible defaults
- explicit inputs/outputs
- clear error when input file missing

---

## Example `argparse` pattern

```python
import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run capstone pipeline end-to-end")
    p.add_argument("--input", required=True, help="Input CSV")
    p.add_argument("--output_dir", default="output", help="Where to write artifacts")
    p.add_argument("--model", default="gpt-4o-mini", help="Model name")
    p.add_argument("--seed", type=int, default=42)
    return p
```

Practical tips:

- keep flag names consistent across scripts (`--input`, `--output_dir`, `--seed`)
- choose defaults that make “copy/paste from README” work
- include enough info in `--help` that a teammate can run without opening code

---

## Advanced CLI patterns

### Pattern 1: Type validation

```python
from pathlib import Path

def existing_file(path_str: str) -> Path:
    """
    Custom argparse type for validating existing files.
    """
    path = Path(path_str)
    if not path.exists():
        raise argparse.ArgumentTypeError(f"File not found: {path}")
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"Not a file: {path}")
    return path


parser.add_argument(
    "--input",
    type=existing_file,  # Validates at parse time
    required=True,
    help="Input CSV file (must exist)"
)
```

### Pattern 2: Mutually exclusive options

```python
parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--local", action="store_true", help="Use local model")
group.add_argument("--api", action="store_true", help="Use API model")

# User must choose exactly one:
# python script.py --local    ✓
# python script.py --api      ✓
# python script.py            ✗ (neither specified)
# python script.py --local --api  ✗ (both specified)
```

### Pattern 3: Choices/enums

```python
parser.add_argument(
    "--mode",
    choices=["train", "eval", "predict"],
    default="eval",
    help="Operation mode (default: eval)"
)

# Only accepts valid choices:
# python script.py --mode train  ✓
# python script.py --mode test   ✗ (invalid choice)
```

### Pattern 4: Flag with default behavior

```python
# Boolean flags
parser.add_argument(
    "--verbose",
    action="store_true",  # False by default, True if flag present
    help="Enable verbose logging"
)

parser.add_argument(
    "--no-cache",
    action="store_true",
    help="Disable caching"
)

# Usage:
args = parser.parse_args()
use_cache = not args.no_cache
```

### Pattern 5: Multiple values

```python
parser.add_argument(
    "--models",
    nargs="+",  # One or more values
    default=["gpt-4o-mini"],
    help="Models to benchmark (space-separated)"
)

# Usage:
# python script.py --models gpt-4 claude-3  → ["gpt-4", "claude-3"]
```

---

## Subcommands (advanced)

For complex tools with multiple modes:

```python
import argparse


def build_parser_with_subcommands() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capstone tools")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Subcommand: profile
    profile_parser = subparsers.add_parser(
        "profile",
        help="Profile a dataset"
    )
    profile_parser.add_argument("--input", required=True)
    profile_parser.add_argument("--output", default="profile.json")
    
    # Subcommand: run
    run_parser = subparsers.add_parser(
        "run",
        help="Run full pipeline"
    )
    run_parser.add_argument("--input", required=True)
    run_parser.add_argument("--model", default="gpt-4o-mini")
    
    return parser


def main():
    parser = build_parser_with_subcommands()
    args = parser.parse_args()
    
    if args.command == "profile":
        run_profile(args.input, args.output)
    elif args.command == "run":
        run_pipeline(args.input, args.model)


# Usage:
# python cli.py profile --input data.csv
# python cli.py run --input data.csv --model gpt-4
# python cli.py --help  → shows available subcommands
```

---

## Help text best practices

```python
parser = argparse.ArgumentParser(
    description="Capstone data analysis pipeline",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Examples:
  Basic run:
    python run.py --input data.csv
  
  Custom output:
    python run.py --input data.csv --output_dir results
  
  Dry run (no LLM call):
    python run.py --input data.csv --dry-run

For more info, see README.md
"""
)

parser.add_argument(
    "--input",
    required=True,
    metavar="FILE",  # Shows as --input FILE in help
    help="Input CSV file path"
)

parser.add_argument(
    "--sample-size",
    type=int,
    default=5,
    metavar="N",
    help="Number of sample rows (default: %(default)s)"  # Shows actual default
)
```

**Output when user runs `--help`:**
```
usage: run.py --input FILE [--sample-size N]

Capstone data analysis pipeline

optional arguments:
  --input FILE        Input CSV file path
  --sample-size N     Number of sample rows (default: 5)

Examples:
  Basic run:
    python run.py --input data.csv
  ...
```

---

## Environment variable fallbacks

```python
import os

parser.add_argument(
    "--model",
    default=os.getenv("DEFAULT_MODEL", "gpt-4o-mini"),
    help="Model name (env: DEFAULT_MODEL, default: gpt-4o-mini)"
)

# User can:
# 1. Set env var: export DEFAULT_MODEL=gpt-4
# 2. Or override: python run.py --model claude-3
# 3. Or use default: python run.py  → gpt-4o-mini
```

---

## Validation after parsing

```python
def validate_args(args) -> None:
    """
    Custom validation logic after argparse parsing.
    """
    # Check file extension
    if not args.input.suffix == ".csv":
        raise ValueError(
            f"Input must be CSV file, got: {args.input.suffix}"
        )
    
    # Check combinations
    if args.dry_run and args.model != "gpt-4o-mini":
        print("Warning: --model ignored in dry-run mode")
    
    # Check ranges
    if args.sample_size < 1 or args.sample_size > 1000:
        raise ValueError(
            f"Sample size must be 1-1000, got: {args.sample_size}"
        )


args = parser.parse_args()
validate_args(args)  # Fail fast with clear errors
```

---

## Practice notebook

For hands-on CLI design exercises, see:
- **[01_cli_design.ipynb](./01_cli_design.ipynb)** - Interactive CLI development
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- Can a teammate run `python run_capstone.py --help` and understand how to use it?
- Do error messages tell the user exactly what went wrong and how to fix it?
- Are defaults chosen to make the "copy from README" case work?
- Does the CLI validate inputs early and fail with clear messages?

---

## References

- Python `argparse`: https://docs.python.org/3/library/argparse.html
- argparse tutorial: https://docs.python.org/3/howto/argparse.html
- Click: https://click.palletsprojects.com/
- Typer: https://typer.tiangolo.com/

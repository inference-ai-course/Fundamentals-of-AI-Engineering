#!/usr/bin/env python3
"""
End-to-end Capstone Runner.

Runs the full pipeline from CSV input to final report with one command.

Pipeline stages:
1. Load - Read CSV file
2. Profile - Generate data profile (shape, columns, types, missing values)
3. Compress - Sample/compress data to fit context window
4. LLM - Call LLM with compressed input
5. Report - Generate JSON and Markdown reports

Usage:
    python run_capstone.py --input data.csv --output_dir output --model llama3.1

Output artifacts:
    - output/profile.json
    - output/compressed_input.json
    - output/llm_raw.txt
    - output/llm_validated.json
    - output/report.json
    - output/report.md
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import random
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import pandas as pd
except ImportError:
    pd = None
    print("Error: pandas is required. Install with: pip install pandas")
    sys.exit(1)

# Try to import llm_client from week_04, with fallback options
LLMClient = None
LLMRequest = None
LLMResponse = None

# Option 1: Try importing from installed package (if llm_client is in the same directory)
try:
    from llm_client import LLMClient, LLMRequest, LLMResponse
except ImportError:
    pass

# Option 2: Try importing from week_04 relative path
if LLMClient is None:
    week_04_path = Path(__file__).parent.parent / "week_04"
    if week_04_path.exists():
        sys.path.insert(0, str(week_04_path))
        try:
            from llm_client import LLMClient, LLMRequest, LLMResponse
        except ImportError:
            pass

# Option 3: Check if llm_client.py exists in current directory
if LLMClient is None:
    local_llm_client = Path(__file__).parent / "llm_client.py"
    if local_llm_client.exists():
        try:
            from llm_client import LLMClient, LLMRequest, LLMResponse
        except ImportError:
            pass


logger = logging.getLogger(__name__)


# ============================================================================
# Configuration
# ============================================================================


@dataclass
class Config:
    """Pipeline configuration."""
    input_path: Path
    output_dir: Path
    model: str
    seed: int
    sample_n: int
    timeout_s: float
    max_retries: int
    
    @classmethod
    def from_args(cls, args: argparse.Namespace) -> "Config":
        return cls(
            input_path=Path(args.input).expanduser(),
            output_dir=Path(args.output_dir),
            model=args.model,
            seed=args.seed,
            sample_n=args.sample_n,
            timeout_s=args.timeout,
            max_retries=args.max_retries,
        )


# ============================================================================
# Stage 1: Load
# ============================================================================


def load_csv(path: Path) -> pd.DataFrame:
    """Load CSV file with validation."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if path.stat().st_size == 0:
        raise ValueError(f"Input file is empty: {path}")
    
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"CSV has no rows: {path}")
    
    logger.info(f"Loaded {len(df)} rows from {path}")
    return df


# ============================================================================
# Stage 2: Profile
# ============================================================================


@dataclass
class DataProfile:
    """Data profile artifact."""
    shape: Tuple[int, int]
    columns: List[str]
    dtypes: Dict[str, str]
    missing: Dict[str, int]
    missing_pct: Dict[str, float]
    sample_seed: int
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "shape": list(self.shape),
            "columns": self.columns,
            "dtypes": self.dtypes,
            "missing": self.missing,
            "missing_pct": self.missing_pct,
            "sample_seed": self.sample_seed,
        }


def profile_data(df: pd.DataFrame, seed: int) -> DataProfile:
    """Generate data profile."""
    profile = DataProfile(
        shape=(int(df.shape[0]), int(df.shape[1])),
        columns=list(df.columns),
        dtypes={c: str(t) for c, t in df.dtypes.to_dict().items()},
        missing={c: int(v) for c, v in df.isna().sum().to_dict().items()},
        missing_pct={
            c: round(float(v) / len(df) * 100, 2) 
            for c, v in df.isna().sum().to_dict().items()
        },
        sample_seed=seed,
    )
    logger.info(f"Profiled data: {profile.shape[0]} rows, {profile.shape[1]} columns")
    return profile


# ============================================================================
# Stage 3: Compress
# ============================================================================


@dataclass
class CompressedTable:
    """Compressed table representation for LLM input."""
    shape: Tuple[int, int]
    columns: List[str]
    dtypes: Dict[str, str]
    missing: Dict[str, int]
    sample_rows: List[Dict[str, Any]]
    sample_seed: int
    numeric_summary: Optional[Dict[str, Dict[str, float]]] = None
    top_categories: Optional[Dict[str, List[Dict[str, Any]]]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "shape": list(self.shape),
            "columns": self.columns,
            "dtypes": self.dtypes,
            "missing": self.missing,
            "sample_rows": self.sample_rows,
            "sample_seed": self.sample_seed,
            "numeric_summary": self.numeric_summary,
            "top_categories": self.top_categories,
        }


def compress_table(
    df: pd.DataFrame, 
    *, 
    sample_n: int = 6, 
    seed: int = 7,
    include_numeric_summary: bool = True,
    include_top_categories: bool = True,
) -> CompressedTable:
    """Compress table to fit in LLM context window."""
    # Sample rows
    if len(df) > sample_n:
        sample = df.sample(n=sample_n, random_state=seed)
    else:
        sample = df
    
    # Numeric summary
    numeric_summary = None
    if include_numeric_summary:
        numeric = df.select_dtypes(include="number")
        if numeric.shape[1] > 0:
            numeric_summary = {}
            for col in numeric.columns:
                s = numeric[col].dropna()
                if len(s) > 0:
                    numeric_summary[str(col)] = {
                        "min": float(s.min()),
                        "mean": float(s.mean()),
                        "max": float(s.max()),
                    }
    
    # Top categories
    top_categories = None
    if include_top_categories:
        obj = df.select_dtypes(include=["object", "category"])
        if obj.shape[1] > 0:
            top_categories = {}
            for col in obj.columns:
                vc = obj[col].fillna("<NA>").astype(str).value_counts(dropna=False)
                top = vc.head(3)
                top_categories[str(col)] = [
                    {"value": str(idx), "count": int(cnt)} 
                    for idx, cnt in top.items()
                ]
    
    return CompressedTable(
        shape=(int(df.shape[0]), int(df.shape[1])),
        columns=list(df.columns),
        dtypes={c: str(t) for c, t in df.dtypes.to_dict().items()},
        missing={c: int(v) for c, v in df.isna().sum().to_dict().items()},
        sample_rows=sample.to_dict(orient="records"),
        sample_seed=seed,
        numeric_summary=numeric_summary,
        top_categories=top_categories,
    )


# ============================================================================
# Stage 4: LLM Call
# ============================================================================


def build_prompt(compressed: CompressedTable) -> str:
    """Build LLM prompt from compressed table."""
    prompt_parts = [
        "You are a data analyst. Analyze the following dataset and provide insights.",
        "",
        "## Dataset Overview",
        f"- Shape: {compressed.shape[0]} rows × {compressed.shape[1]} columns",
        f"- Columns: {', '.join(compressed.columns)}",
        "",
        "## Column Types",
    ]
    
    for col, dtype in compressed.dtypes.items():
        missing = compressed.missing.get(col, 0)
        prompt_parts.append(f"- {col}: {dtype} ({missing} missing)")
    
    prompt_parts.append("")
    prompt_parts.append("## Sample Rows")
    prompt_parts.append("```json")
    prompt_parts.append(json.dumps(compressed.sample_rows[:3], indent=2, default=str))
    prompt_parts.append("```")
    
    if compressed.numeric_summary:
        prompt_parts.append("")
        prompt_parts.append("## Numeric Summary")
        for col, stats in compressed.numeric_summary.items():
            prompt_parts.append(
                f"- {col}: min={stats['min']:.2f}, mean={stats['mean']:.2f}, max={stats['max']:.2f}"
            )
    
    if compressed.top_categories:
        prompt_parts.append("")
        prompt_parts.append("## Top Categories")
        for col, cats in compressed.top_categories.items():
            cats_str = ", ".join(f"{c['value']}({c['count']})" for c in cats)
            prompt_parts.append(f"- {col}: {cats_str}")
    
    prompt_parts.append("")
    prompt_parts.append("## Task")
    prompt_parts.append(
        "Provide a brief analysis of this dataset including:\n"
        "1. Data quality assessment\n"
        "2. Key insights\n"
        "3. Recommendations"
    )
    
    return "\n".join(prompt_parts)


def call_llm(
    compressed: CompressedTable,
    model: str,
    *,
    timeout_s: float = 60.0,
    max_retries: int = 3,
    output_dir: Path = Path("output"),
) -> Tuple[str, Dict[str, Any]]:
    """Call LLM with compressed table and return raw + validated output."""
    prompt = build_prompt(compressed)
    
    # Save raw prompt
    (output_dir / "llm_prompt.txt").write_text(prompt, encoding="utf-8")
    
    if LLMClient is None:
        # Fallback: return placeholder
        logger.warning("llm_client not available, returning placeholder")
        raw = "LLM client not available. Install dependencies and ensure Ollama is running."
        validated = {"summary": raw, "error": "llm_client_unavailable"}
    else:
        client = LLMClient(
            timeout_s=timeout_s,
            max_retries=max_retries,
            output_dir=output_dir,
        )
        response = client.call(LLMRequest(
            model=model,
            prompt=prompt,
            temperature=0.0,
        ))
        
        if response.ok:
            raw = response.text
            validated = {
                "summary": raw[:500] + "..." if len(raw) > 500 else raw,
                "model": model,
                "latency_s": response.latency_s,
            }
        else:
            raw = ""
            validated = {
                "error": response.error,
                "error_type": response.error_type,
            }
            client.persist_failure(LLMRequest(model=model, prompt=prompt), response)
    
    # Save outputs
    (output_dir / "llm_raw.txt").write_text(raw, encoding="utf-8")
    (output_dir / "llm_validated.json").write_text(
        json.dumps(validated, indent=2), encoding="utf-8"
    )
    
    return raw, validated


# ============================================================================
# Stage 5: Report
# ============================================================================


@dataclass
class Report:
    """Final report artifact."""
    input_file: str
    model: str
    shape: Tuple[int, int]
    columns: List[str]
    missing_summary: Dict[str, int]
    llm_summary: str
    generated_at: str
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    
    def to_markdown(self) -> str:
        lines = [
            "# Data Analysis Report",
            "",
            f"**Generated:** {self.generated_at}",
            f"**Model:** {self.model}",
            f"**Input:** {self.input_file}",
            "",
            "## Dataset Overview",
            "",
            f"- **Shape:** {self.shape[0]} rows × {self.shape[1]} columns",
            f"- **Columns:** {len(self.columns)}",
            "",
            "### Column Summary",
            "",
            "| Column | Missing Values |",
            "|--------|---------------|",
        ]
        for col, missing in self.missing_summary.items():
            lines.append(f"| {col} | {missing} |")
        
        lines.append("")
        lines.append("## Analysis")
        lines.append("")
        lines.append(self.llm_summary)
        
        return "\n".join(lines)


def generate_report(
    input_path: Path,
    profile: DataProfile,
    llm_validated: Dict[str, Any],
    model: str,
    output_dir: Path,
) -> Report:
    """Generate final report."""
    report = Report(
        input_file=str(input_path),
        model=model,
        shape=profile.shape,
        columns=profile.columns,
        missing_summary=profile.missing,
        llm_summary=llm_validated.get("summary", "No summary available"),
        generated_at=time.strftime("%Y-%m-%d %H:%M:%S"),
    )
    
    # Save JSON report
    (output_dir / "report.json").write_text(
        json.dumps(report.to_dict(), indent=2), encoding="utf-8"
    )
    
    # Save Markdown report
    (output_dir / "report.md").write_text(
        report.to_markdown(), encoding="utf-8"
    )
    
    logger.info(f"Generated report: {output_dir / 'report.json'}")
    return report


# ============================================================================
# Pipeline Runner
# ============================================================================


def run_pipeline(config: Config) -> Dict[str, Any]:
    """Run the full pipeline."""
    config.output_dir.mkdir(parents=True, exist_ok=True)
    
    results: Dict[str, Any] = {"config": asdict(config)}
    results["config"]["input_path"] = str(config.input_path)
    results["config"]["output_dir"] = str(config.output_dir)
    
    try:
        # Stage 1: Load
        print(f"[1/5] Loading data from {config.input_path}...")
        df = load_csv(config.input_path)
        results["load"] = {"rows": len(df), "columns": list(df.columns)}
        
        # Stage 2: Profile
        print("[2/5] Profiling data...")
        profile = profile_data(df, config.seed)
        (config.output_dir / "profile.json").write_text(
            json.dumps(profile.to_dict(), indent=2), encoding="utf-8"
        )
        results["profile"] = profile.to_dict()
        
        # Stage 3: Compress
        print("[3/5] Compressing data...")
        compressed = compress_table(df, sample_n=config.sample_n, seed=config.seed)
        (config.output_dir / "compressed_input.json").write_text(
            json.dumps(compressed.to_dict(), indent=2, default=str), encoding="utf-8"
        )
        results["compressed"] = {"sample_rows": len(compressed.sample_rows)}
        
        # Stage 4: LLM
        print(f"[4/5] Calling LLM ({config.model})...")
        raw, validated = call_llm(
            compressed,
            config.model,
            timeout_s=config.timeout_s,
            max_retries=config.max_retries,
            output_dir=config.output_dir,
        )
        results["llm"] = validated
        
        # Stage 5: Report
        print("[5/5] Generating report...")
        report = generate_report(
            config.input_path,
            profile,
            validated,
            config.model,
            config.output_dir,
        )
        results["report"] = report.to_dict()
        
        results["success"] = True
        print(f"\n✓ Pipeline completed successfully!")
        print(f"  Report: {config.output_dir / 'report.md'}")
        
    except Exception as e:
        results["success"] = False
        results["error"] = str(e)
        results["error_type"] = type(e).__name__
        
        # Save failure record
        failure_path = config.output_dir / "pipeline_failure.json"
        failure_path.write_text(
            json.dumps({
                "error": str(e),
                "error_type": type(e).__name__,
                "stage": list(results.keys())[-1] if len(results) > 1 else "unknown",
            }, indent=2),
            encoding="utf-8"
        )
        
        print(f"\n✗ Pipeline failed: {e}")
        logger.error(f"Pipeline failed: {e}", exc_info=True)
    
    return results


# ============================================================================
# CLI
# ============================================================================


def build_parser() -> argparse.ArgumentParser:
    """Build CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="run_capstone",
        description="Run the capstone pipeline end-to-end",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_capstone.py --input data.csv --model llama3.1
  python run_capstone.py --input data.csv --output_dir results --model gpt-4

Output artifacts:
  - output/profile.json        Data profile
  - output/compressed_input.json  Compressed table for LLM
  - output/llm_raw.txt         Raw LLM response
  - output/llm_validated.json  Validated LLM output
  - output/report.json         Final report (JSON)
  - output/report.md           Final report (Markdown)
        """,
    )
    
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Input CSV file path",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="output",
        dest="output_dir",
        help="Output directory for artifacts (default: output)",
    )
    parser.add_argument(
        "--model", "-m",
        required=True,
        help="LLM model name (e.g., llama3.1, gpt-4)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility (default: 42)",
    )
    parser.add_argument(
        "--sample-n",
        type=int,
        default=6,
        dest="sample_n",
        help="Number of sample rows to include (default: 6)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="LLM request timeout in seconds (default: 60)",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        dest="max_retries",
        help="Maximum LLM retry attempts (default: 3)",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging",
    )
    
    return parser


def validate_args(args: argparse.Namespace) -> None:
    """Validate CLI arguments."""
    input_path = Path(args.input).expanduser()
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    if input_path.stat().st_size == 0:
        raise ValueError(f"Input file is empty: {input_path}")
    
    if args.seed < 0:
        raise ValueError("Seed must be non-negative")
    
    if args.sample_n < 1:
        raise ValueError("Sample size must be at least 1")
    
    if args.timeout <= 0:
        raise ValueError("Timeout must be positive")


def main() -> int:
    """Main entry point."""
    parser = build_parser()
    args = parser.parse_args()
    
    # Setup logging
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    
    try:
        validate_args(args)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        return 1
    
    config = Config.from_args(args)
    
    results = run_pipeline(config)
    
    # Save full results
    results_path = config.output_dir / "pipeline_results.json"
    results_path.write_text(
        json.dumps(results, indent=2, default=str), encoding="utf-8"
    )
    
    return 0 if results.get("success") else 1


if __name__ == "__main__":
    sys.exit(main())

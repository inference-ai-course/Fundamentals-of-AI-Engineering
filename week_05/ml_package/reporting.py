"""
Reporting utilities for ML experiments.

This module provides functions to generate markdown reports
and summaries for ML training runs and comparisons.
"""

from pathlib import Path
from typing import Any, Dict, List

from .comparison import RunInfo, compare_two_runs, find_improvements, summarize_runs


def write_comparison_report(output_path: Path, runs: List[RunInfo]) -> None:
    """Write a comprehensive comparison report for multiple runs.
    
    Args:
        output_path: Path to write the markdown report
        runs: List of runs to compare
    """
    if not runs:
        output_path.write_text("# No runs to compare\n")
        return
    
    summary = summarize_runs(runs)
    
    lines = [
        "# ML Experiment Comparison Report",
        "",
        f"**Total runs analyzed:** {summary['n']}",
        "",
    ]
    
    # Summary statistics
    lines.append("## Summary Statistics")
    lines.append("")
    
    for key, value in summary.items():
        if key.startswith("avg_"):
            metric = key.replace("avg_", "")
            lines.append(f"- **Average {metric}:** {value}")
        elif key.startswith("best_"):
            metric = key.replace("best_", "")
            lines.append(f"- **Best {metric}:** {value['value']} (run: {value['run_id']})")
    
    lines.append("")
    
    # Individual run details
    lines.append("## Individual Runs")
    lines.append("")
    
    for run in runs:
        lines.append(f"### {run.run_id}")
        lines.append("")
        
        # Config
        lines.append("**Configuration:**")
        for key, value in run.config.items():
            lines.append(f"- {key}: {value}")
        lines.append("")
        
        # Metrics
        lines.append("**Metrics:**")
        for metric, value in run.metrics.items():
            if isinstance(value, float):
                lines.append(f"- {metric}: {value:.4f}")
            else:
                lines.append(f"- {metric}: {value}")
        lines.append("")
    
    # Improvements over time
    improvements = find_improvements(runs)
    if improvements:
        lines.append("## Improvements Over Time")
        lines.append("")
        for baseline, improved in improvements:
            baseline_acc = baseline.metrics.get("accuracy", "N/A")
            improved_acc = improved.metrics.get("accuracy", "N/A")
            lines.append(f"- **{baseline.run_id}** → **{improved.run_id}**: "
                        f"accuracy {baseline_acc} → {improved_acc}")
        lines.append("")
    
    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_experiment_report(
    output_path: Path,
    goal: str,
    baseline_run: RunInfo,
    variant_run: RunInfo,
    interpretation: str,
    failure_retrospective: str,
    next_experiment: str,
    risk_caveat: str = ""
) -> None:
    """Write a structured experiment report comparing two runs.
    
    Args:
        output_path: Path to write the report
        goal: What you tried to improve
        baseline_run: Baseline experiment run
        variant_run: Variant experiment run
        interpretation: Why you think it changed
        failure_retrospective: One failure + what you learned
        next_experiment: Next experiment idea
        risk_caveat: Optional caveat about limitations
    """
    comparison = compare_two_runs(baseline_run, variant_run)
    
    lines = [
        "# Experiment Report",
        "",
        "## Goal",
        goal,
        "",
        "## Baseline",
        f"**Run ID:** {baseline_run.run_id}",
        f"**Command:** python train.py --input {baseline_run.config['input_csv']} "
        f"--label_col {baseline_run.config['label_col']} --seed {baseline_run.config['random_state']} "
        f"--max_iter {baseline_run.config['max_iter']}",
        "",
        "**Metrics:**"
    ]
    
    for metric, value in baseline_run.metrics.items():
        if isinstance(value, float):
            lines.append(f"- {metric}: {value:.4f}")
        else:
            lines.append(f"- {metric}: {value}")
    
    lines.extend([
        "",
        "## Variant",
        f"**Run ID:** {variant_run.run_id}",
        f"**Command:** python train.py --input {variant_run.config['input_csv']} "
        f"--label_col {variant_run.config['label_col']} --seed {variant_run.config['random_state']} "
        f"--max_iter {variant_run.config['max_iter']}",
        "",
        "**Metrics:**"
    ])
    
    for metric, value in variant_run.metrics.items():
        if isinstance(value, float):
            lines.append(f"- {metric}: {value:.4f}")
        else:
            lines.append(f"- {metric}: {value}")
    
    lines.extend([
        "",
        "## What Changed and Why",
        interpretation,
        "",
        "## Differences",
        ""
    ])
    
    for metric, diff in comparison["differences"].items():
        if diff["relative"] is not None:
            lines.append(f"- **{metric}:** {diff['absolute']:+.4f} "
                        f"({diff['relative']*100:+.1f}%)")
        else:
            lines.append(f"- **{metric}:** {diff['absolute']:+.4f}")
    
    lines.extend([
        "",
        "## One Failure + Lesson",
        failure_retrospective,
        "",
        "## Next Experiment",
        next_experiment,
        ""
    ])
    
    if risk_caveat:
        lines.extend([
            "## Risk / Caveat",
            risk_caveat,
            ""
        ])
    
    lines.extend([
        "---",
        "",
        f"*Report generated using artifacts from:*",
        f"- Baseline: {baseline_run.run_id}",
        f"- Variant: {variant_run.run_id}"
    ])
    
    output_path.write_text("\n".join(lines), encoding="utf-8")


def generate_experiment_summary(
    runs: List[RunInfo],
    output_dir: Path
) -> Dict[str, Path]:
    """Generate a complete experiment summary with multiple reports.
    
    Args:
        runs: List of runs to analyze
        output_dir: Directory to save reports
        
    Returns:
        Dictionary mapping report names to file paths
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    reports = {}
    
    # Main comparison report
    comparison_path = output_dir / "comparison_report.md"
    write_comparison_report(comparison_path, runs)
    reports["comparison"] = comparison_path
    
    # Summary statistics
    summary = summarize_runs(runs)
    summary_path = output_dir / "summary.json"
    import json
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    reports["summary"] = summary_path
    
    # Runs list
    runs_data = []
    for run in runs:
        runs_data.append({
            "run_id": run.run_id,
            "config": run.config,
            "metrics": run.metrics
        })
    
    runs_path = output_dir / "runs.json"
    runs_path.write_text(json.dumps(runs_data, indent=2), encoding="utf-8")
    reports["runs"] = runs_path
    
    return reports


def write_quick_summary(output_path: Path, runs: List[RunInfo]) -> None:
    """Write a quick summary of runs for dashboard display.
    
    Args:
        output_path: Path to write the summary
        runs: List of runs to summarize
    """
    if not runs:
        output_path.write_text("No runs available\n")
        return
    
    summary = summarize_runs(runs)
    
    lines = [
        "# ML Training Dashboard",
        "",
        f"**Total Runs:** {summary['n']}",
        ""
    ]
    
    # Best runs for key metrics
    key_metrics = ["accuracy", "f1_macro"]
    for metric in key_metrics:
        best_key = f"best_{metric}"
        if best_key in summary:
            best = summary[best_key]
            lines.append(f"**Best {metric}:** {best['value']:.4f} (run: {best['run_id']})")
    
    lines.append("")
    lines.append("## Recent Runs")
    lines.append("")
    
    # Show last 5 runs
    recent_runs = runs[-5:] if len(runs) > 5 else runs
    for run in reversed(recent_runs):  # Most recent first
        acc = run.metrics.get("accuracy", "N/A")
        f1 = run.metrics.get("f1_macro", "N/A")
        acc_str = f"{acc:.4f}" if isinstance(acc, float) else str(acc)
        f1_str = f"{f1:.4f}" if isinstance(f1, float) else str(f1)
        lines.append(f"- **{run.run_id}**: accuracy={acc_str}, f1={f1_str}")
    
    output_path.write_text("\n".join(lines), encoding="utf-8")

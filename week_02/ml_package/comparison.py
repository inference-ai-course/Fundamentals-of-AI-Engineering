"""
Run comparison utilities for ML experiments.

This module provides functions to load, compare, and analyze
multiple training runs to identify the best performing models.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .trainer import TrainResult


@dataclass
class RunInfo:
    """Information about a training run."""
    run_id: str
    config: Dict[str, Any]
    metrics: Dict[str, Any]
    model_path: Optional[Path] = None
    report_path: Optional[Path] = None


def load_run(run_dir: Path) -> RunInfo:
    """Load a single run from its artifacts directory.
    
    Args:
        run_dir: Path to the run directory containing artifacts
        
    Returns:
        RunInfo with loaded data
        
    Raises:
        FileNotFoundError: If required files are missing
    """
    # Load config
    config_path = run_dir / "config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Load metrics
    metrics_path = run_dir / "metrics.json"
    if not metrics_path.exists():
        raise FileNotFoundError(f"Metrics file not found: {metrics_path}")
    
    with open(metrics_path, 'r') as f:
        metrics = json.load(f)
    
    # Check for optional files
    model_path = run_dir / "model.joblib" if (run_dir / "model.joblib").exists() else None
    report_path = run_dir / "val_report.txt" if (run_dir / "val_report.txt").exists() else None
    
    return RunInfo(
        run_id=run_dir.name,
        config=config,
        metrics=metrics,
        model_path=model_path,
        report_path=report_path
    )


def load_runs(artifacts_dir: str) -> List[RunInfo]:
    """Load all runs from an artifacts directory.
    
    Args:
        artifacts_dir: Directory containing run subdirectories
        
    Returns:
        List of RunInfo objects
    """
    artifacts_path = Path(artifacts_dir)
    runs = []
    
    for run_dir in artifacts_path.iterdir():
        if run_dir.is_dir() and run_dir.name.startswith("run_"):
            try:
                run_info = load_run(run_dir)
                runs.append(run_info)
            except FileNotFoundError as e:
                print(f"Warning: Skipping {run_dir.name}: {e}")
    
    # Sort by run_id (timestamp)
    runs.sort(key=lambda r: r.run_id)
    return runs


def select_best_run(runs: List[RunInfo], metric: str = "accuracy") -> RunInfo:
    """Select the best run based on a specific metric.
    
    Args:
        runs: List of runs to compare
        metric: Metric to use for selection (default: accuracy)
        
    Returns:
        Best performing run
        
    Raises:
        ValueError: If metric is not found in any run
    """
    if not runs:
        raise ValueError("No runs provided")
    
    # Filter runs that have the metric
    valid_runs = [r for r in runs if metric in r.metrics]
    if not valid_runs:
        raise ValueError(f"Metric '{metric}' not found in any run")
    
    # Select run with highest metric value
    best_run = max(valid_runs, key=lambda r: r.metrics[metric])
    return best_run


def summarize_runs(runs: List[RunInfo]) -> Dict[str, Any]:
    """Generate summary statistics for a list of runs.
    
    Args:
        runs: List of runs to summarize
        
    Returns:
        Dictionary with summary statistics
    """
    if not runs:
        return {"n": 0}
    
    # Find all available metrics
    all_metrics = set()
    for run in runs:
        all_metrics.update(run.metrics.keys())
    
    # Calculate averages for numeric metrics
    summary = {"n": len(runs)}
    
    for metric in all_metrics:
        values = [r.metrics.get(metric) for r in runs if r.metrics.get(metric) is not None]
        if values and all(isinstance(v, (int, float)) for v in values):
            summary[f"avg_{metric}"] = round(sum(values) / len(values), 4)
            summary[f"min_{metric}"] = min(values)
            summary[f"max_{metric}"] = max(values)
    
    # Add best run for each metric
    for metric in all_metrics:
        try:
            best = select_best_run(runs, metric)
            summary[f"best_{metric}"] = {
                "run_id": best.run_id,
                "value": best.metrics[metric]
            }
        except ValueError:
            pass  # Skip if metric not comparable
    
    return summary


def compare_two_runs(run1: RunInfo, run2: RunInfo) -> Dict[str, Any]:
    """Compare two runs side by side.
    
    Args:
        run1: First run
        run2: Second run
        
    Returns:
        Dictionary with comparison results
    """
    comparison = {
        "run1": {
            "run_id": run1.run_id,
            "config": run1.config,
            "metrics": run1.metrics
        },
        "run2": {
            "run_id": run2.run_id,
            "config": run2.config,
            "metrics": run2.metrics
        }
    }
    
    # Calculate differences for numeric metrics
    differences = {}
    for metric in run1.metrics:
        if metric in run2.metrics:
            val1 = run1.metrics[metric]
            val2 = run2.metrics[metric]
            if isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
                differences[metric] = {
                    "absolute": val2 - val1,
                    "relative": (val2 - val1) / val1 if val1 != 0 else None
                }
    
    comparison["differences"] = differences
    return comparison


def find_improvements(runs: List[RunInfo], baseline_metric: str = "accuracy") -> List[Tuple[RunInfo, RunInfo]]:
    """Find pairs of runs where the later run improved over the earlier run.
    
    Args:
        runs: List of runs ordered by time
        baseline_metric: Metric to check for improvement
        
    Returns:
        List of (baseline_run, improved_run) tuples
    """
    improvements = []
    
    for i in range(1, len(runs)):
        baseline = runs[i-1]
        current = runs[i]
        
        if (baseline_metric in baseline.metrics and 
            baseline_metric in current.metrics):
            
            baseline_val = baseline.metrics[baseline_metric]
            current_val = current.metrics[baseline_metric]
            
            if current_val > baseline_val:
                improvements.append((baseline, current))
    
    return improvements

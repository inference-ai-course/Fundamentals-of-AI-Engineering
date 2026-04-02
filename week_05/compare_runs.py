#!/usr/bin/env python3
"""
Compare ML training runs and generate reports.

Usage:
    python compare_runs.py --artifacts_dir artifacts --output_dir reports
"""

import argparse
from pathlib import Path

from ml_package import comparison, reporting


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare ML training runs and generate reports"
    )
    parser.add_argument(
        "--artifacts_dir",
        default="artifacts",
        help="Directory containing run artifacts"
    )
    parser.add_argument(
        "--output_dir", 
        default="reports",
        help="Directory to save comparison reports"
    )
    parser.add_argument(
        "--metric",
        default="accuracy",
        help="Metric to use for selecting best run"
    )
    parser.add_argument(
        "--dashboard",
        action="store_true",
        help="Generate quick dashboard summary"
    )
    args = parser.parse_args()

    # Load all runs
    print(f"Loading runs from {args.artifacts_dir}...")
    runs = comparison.load_runs(args.artifacts_dir)
    
    if not runs:
        print("No runs found!")
        return
    
    print(f"Found {len(runs)} runs")
    
    # Generate summary
    summary = comparison.summarize_runs(runs)
    print(f"Average accuracy: {summary.get('avg_accuracy', 'N/A')}")
    
    # Select best run
    try:
        best = comparison.select_best_run(runs, args.metric)
        print(f"Best run by {args.metric}: {best.run_id} "
              f"({best.metrics[args.metric]:.4f})")
    except ValueError as e:
        print(f"Could not select best run: {e}")
    
    # Generate reports
    output_dir = Path(args.output_dir)
    reports = reporting.generate_experiment_summary(runs, output_dir)
    
    print(f"\nReports generated:")
    for name, path in reports.items():
        print(f"  {name}: {path}")
    
    # Generate dashboard if requested
    if args.dashboard:
        dashboard_path = output_dir / "dashboard.md"
        reporting.write_quick_summary(dashboard_path, runs)
        print(f"  dashboard: {dashboard_path}")


if __name__ == "__main__":
    main()

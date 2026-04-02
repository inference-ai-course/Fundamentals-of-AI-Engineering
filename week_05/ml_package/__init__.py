"""
ML Training Package - A reproducible machine learning training framework.

This package provides modular components for:
- Training ML models with reproducible workflows
- Comparing experiment runs
- Generating reports
- Managing dependencies and configurations

Example usage:
    from ml_package import trainer, comparison, reporting
    
    # Train a model
    result = trainer.train_model(...)
    
    # Compare runs
    best = comparison.select_best_run(runs)
    
    # Generate report
    reporting.write_comparison_report(...)
"""

__version__ = "0.1.0"
__all__ = ["trainer", "comparison", "reporting", "reproducibility"]

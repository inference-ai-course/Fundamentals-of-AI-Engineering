#!/usr/bin/env python3
"""
ML Training Loop - Baseline Classifier

A reproducible baseline classifier that demonstrates the complete ML training loop:
1. Load data
2. Split train/validation
3. Build preprocessing pipeline
4. Train model
5. Evaluate on validation
6. Save artifacts

Usage:
    python train.py --input data.csv --label_col label --seed 42
"""

import argparse
import json
from pathlib import Path

from ml_package import trainer, reproducibility


def main() -> None:
    """Main entry point for training pipeline."""
    parser = argparse.ArgumentParser(
        description="Train a reproducible baseline classifier"
    )
    parser.add_argument("--input", required=True, help="Input CSV")
    parser.add_argument("--label_col", required=True, help="Label column name")
    parser.add_argument("--test_size", type=float, default=0.2)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_iter", type=int, default=500)
    parser.add_argument("--artifacts_dir", default="artifacts")
    parser.add_argument("--create_sample", choices=["iris", "synthetic"], 
                       help="Create sample dataset instead of using existing file")
    args = parser.parse_args()

    # Create sample dataset if requested
    if args.create_sample:
        trainer.create_sample_dataset(args.input, args.create_sample)

    # Create training configuration
    cfg = trainer.TrainConfig(
        input_csv=args.input,
        label_col=args.label_col,
        test_size=float(args.test_size),
        random_state=int(args.seed),
        max_iter=int(args.max_iter),
    )

    try:
        # Train the model
        print("🎯 Starting training pipeline...")
        result = trainer.train(cfg, args.artifacts_dir)
        
        # Get the run directory from the most recent run
        import time
        run_id = time.strftime("run_%Y%m%d_%H%M%S")
        artifacts_path = Path(args.artifacts_dir) / run_id
        
        # Capture dependencies for reproducibility
        requirements_path = artifacts_path / "requirements.txt"
        reproducibility.capture_dependencies(requirements_path)
        
        # Create run metadata
        env_info = reproducibility.validate_environment([
            "pandas", "scikit-learn", "joblib", "numpy"
        ])
        metadata = reproducibility.create_run_metadata(
            config=result.config.__dict__,
            environment_info=env_info
        )
        reproducibility.save_run_metadata(metadata, artifacts_path / "run_metadata.json")

        # Output results
        print("\n✅ Training completed successfully!")
        print(f"📁 Artifacts saved to: {artifacts_path}")
        print("\n📊 Results:")
        print(json.dumps(result.metrics, indent=2))
        print(f"⏱️  Training time: {result.train_seconds:.2f} seconds")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()

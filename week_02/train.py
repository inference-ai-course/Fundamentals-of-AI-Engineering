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
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris, make_classification
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


@dataclass
class TrainConfig:
    input_csv: str
    label_col: str
    test_size: float
    random_state: int
    max_iter: int


def create_sample_dataset(output_path: str, dataset_type: str = "iris") -> None:
    """Create a sample dataset for testing.
    
    Args:
        output_path: Where to save the CSV file
        dataset_type: Either 'iris' or 'synthetic'
    """
    if dataset_type == "iris":
        # Load iris dataset and convert to DataFrame
        iris = load_iris()
        df = pd.DataFrame(
            data=iris.data,
            columns=iris.feature_names
        )
        df['label'] = iris.target
        df['label'] = df['label'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        
    elif dataset_type == "synthetic":
        # Create synthetic classification dataset
        X, y = make_classification(
            n_samples=200,
            n_features=5,
            n_informative=3,
            n_redundant=1,
            n_classes=3,
            random_state=42
        )
        
        # Create feature names
        feature_names = [f'feature_{i}' for i in range(X.shape[1])]
        df = pd.DataFrame(X, columns=feature_names)
        df['label'] = y
        df['label'] = df['label'].map({0: 'class_0', 1: 'class_1', 2: 'class_2'})
        
        # Add some missing values to test imputation
        import numpy as np
        for col in feature_names[:2]:
            mask = np.random.random(len(df)) < 0.1  # 10% missing
            df.loc[mask, col] = np.nan
    
    else:
        raise ValueError(f"Unknown dataset type: {dataset_type}")
    
    df.to_csv(output_path, index=False)
    print(f"Created sample dataset: {output_path}")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Label distribution:\n{df['label'].value_counts()}")


def load_data(cfg: TrainConfig) -> Tuple[pd.DataFrame, pd.Series]:
    """Load CSV and separate features from label.
    
    Raises:
        ValueError: If label column is not found in the CSV.
    """
    df = pd.read_csv(cfg.input_csv)
    if cfg.label_col not in df.columns:
        raise ValueError(f"label_col not found: {cfg.label_col}")
    
    y = df[cfg.label_col]
    X = df.drop(columns=[cfg.label_col])
    return X, y


def split_data(
    X: pd.DataFrame, 
    y: pd.Series, 
    cfg: TrainConfig
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split data into train and validation sets.
    
    Uses stratification if more than one class is present.
    """
    stratify = y if y.nunique() > 1 else None
    return train_test_split(
        X, y,
        test_size=cfg.test_size,
        random_state=cfg.random_state,
        stratify=stratify,
    )


def build_preprocessor(X_train: pd.DataFrame) -> ColumnTransformer:
    """Build preprocessing pipeline for numeric and categorical columns."""
    numeric_cols = [c for c in X_train.columns 
                    if pd.api.types.is_numeric_dtype(X_train[c])]
    categorical_cols = [c for c in X_train.columns 
                        if c not in numeric_cols]

    numeric_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ])
    categorical_pipe = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer(transformers=[
        ("num", numeric_pipe, numeric_cols),
        ("cat", categorical_pipe, categorical_cols),
    ])


def train_model(
    X_train: pd.DataFrame, 
    y_train: pd.Series, 
    preprocessor: ColumnTransformer,
    cfg: TrainConfig
) -> Tuple[Pipeline, float]:
    """Train the model and return the fitted pipeline with training time."""
    model = LogisticRegression(max_iter=cfg.max_iter, random_state=cfg.random_state)
    clf = Pipeline(steps=[("preprocess", preprocessor), ("model", model)])

    t0 = time.time()
    clf.fit(X_train, y_train)
    train_seconds = time.time() - t0

    return clf, train_seconds


def evaluate_model(
    clf: Pipeline, 
    X_val: pd.DataFrame, 
    y_val: pd.Series
) -> Dict[str, Any]:
    """Evaluate model on validation set and return metrics."""
    y_pred = clf.predict(X_val)

    metrics = {
        "accuracy": float(accuracy_score(y_val, y_pred)),
        "f1_macro": float(f1_score(y_val, y_pred, average="macro")) 
                    if y_val.nunique() > 1 else None,
        "n_val": int(len(X_val)),
    }
    
    report = classification_report(y_val, y_pred)
    return metrics, report


def save_artifacts(
    clf: Pipeline,
    cfg: TrainConfig,
    metrics: Dict[str, Any],
    train_seconds: float,
    n_train: int,
    report: str,
    artifacts_dir: str,
) -> Path:
    """Save all artifacts to a per-run folder.
    
    Returns:
        Path to the output directory.
    """
    run_id = time.strftime("run_%Y%m%d_%H%M%S")
    out_dir = Path(artifacts_dir) / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    # Save config
    (out_dir / "config.json").write_text(
        json.dumps(asdict(cfg), indent=2, sort_keys=True)
    )
    
    # Save metrics with training metadata
    full_metrics = {
        **metrics,
        "train_seconds": float(train_seconds),
        "n_train": int(n_train),
    }
    (out_dir / "metrics.json").write_text(
        json.dumps(full_metrics, indent=2, sort_keys=True)
    )
    
    # Save classification report
    (out_dir / "val_report.txt").write_text(report)
    
    # Save model
    joblib.dump(clf, out_dir / "model.joblib")

    return out_dir


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
        create_sample_dataset(args.input, args.create_sample)

    cfg = TrainConfig(
        input_csv=args.input,
        label_col=args.label_col,
        test_size=float(args.test_size),
        random_state=int(args.seed),
        max_iter=int(args.max_iter),
    )

    try:
        # Stage 1: Load data
        print("📊 Loading data...")
        X, y = load_data(cfg)
        print(f"   Loaded {len(X)} rows, {len(X.columns)} features")
        
        # Stage 2: Split
        print("🔄 Splitting data...")
        X_train, X_val, y_train, y_val = split_data(X, y, cfg)
        print(f"   Train: {len(X_train)} samples")
        print(f"   Val: {len(X_val)} samples")
        
        # Stage 3: Build preprocessor
        print("🔧 Building preprocessor...")
        preprocessor = build_preprocessor(X_train)
        numeric_cols = [c for c in X_train.columns 
                        if pd.api.types.is_numeric_dtype(X_train[c])]
        categorical_cols = [c for c in X_train.columns 
                            if c not in numeric_cols]
        print(f"   Numeric features: {len(numeric_cols)}")
        print(f"   Categorical features: {len(categorical_cols)}")
        
        # Stage 4: Train
        print("🎯 Training model...")
        clf, train_seconds = train_model(X_train, y_train, preprocessor, cfg)
        print(f"   Training completed in {train_seconds:.2f} seconds")
        
        # Stage 5: Evaluate
        print("📈 Evaluating model...")
        metrics, report = evaluate_model(clf, X_val, y_val)
        print(f"   Accuracy: {metrics['accuracy']:.3f}")
        if metrics['f1_macro']:
            print(f"   F1-macro: {metrics['f1_macro']:.3f}")
        
        # Stage 6: Save artifacts
        print("💾 Saving artifacts...")
        out_dir = save_artifacts(
            clf, cfg, metrics, train_seconds, 
            len(X_train), report, args.artifacts_dir
        )
        print(f"   Artifacts saved to: {out_dir}")

        # Output results
        print("\n✅ Training completed successfully!")
        print("\n📊 Results:")
        print(json.dumps({
            **metrics,
            "train_seconds": train_seconds,
            "n_train": len(X_train),
        }, indent=2))
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        raise


if __name__ == "__main__":
    main()

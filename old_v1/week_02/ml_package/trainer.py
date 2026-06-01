"""
Core training module for reproducible ML experiments.

This module provides the main training pipeline with modular functions
that match the ML training loop stages:
1. Load data
2. Split train/validation
3. Build preprocessing pipeline
4. Train model
5. Evaluate on validation
6. Save artifacts
"""

import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Tuple

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
    """Configuration for training runs."""
    input_csv: str
    label_col: str
    test_size: float
    random_state: int
    max_iter: int


@dataclass
class TrainResult:
    """Results from a training run."""
    metrics: Dict[str, Any]
    model: Pipeline
    config: TrainConfig
    train_seconds: float
    n_train: int
    n_val: int


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
) -> Tuple[Dict[str, Any], str]:
    """Evaluate model on validation set and return metrics and report."""
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


def train(cfg: TrainConfig, artifacts_dir: str = "artifacts") -> TrainResult:
    """Complete training pipeline.
    
    Args:
        cfg: Training configuration
        artifacts_dir: Directory to save artifacts
        
    Returns:
        TrainResult with metrics, model, and metadata
    """
    # Stage 1: Load data
    X, y = load_data(cfg)
    
    # Stage 2: Split
    X_train, X_val, y_train, y_val = split_data(X, y, cfg)
    
    # Stage 3: Build preprocessor
    preprocessor = build_preprocessor(X_train)
    
    # Stage 4: Train
    clf, train_seconds = train_model(X_train, y_train, preprocessor, cfg)
    
    # Stage 5: Evaluate
    metrics, report = evaluate_model(clf, X_val, y_val)
    
    # Stage 6: Save artifacts
    out_dir = save_artifacts(
        clf, cfg, metrics, train_seconds, 
        len(X_train), report, artifacts_dir
    )

    return TrainResult(
        metrics=metrics,
        model=clf,
        config=cfg,
        train_seconds=train_seconds,
        n_train=len(X_train),
        n_val=len(X_val)
    )

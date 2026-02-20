"""
Reproducibility utilities for ML experiments.

This module provides functions to capture dependencies, validate environments,
and ensure experiments can be reproduced consistently.
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional


def capture_dependencies(output_path: Path, include_versions: bool = True) -> Path:
    """Capture current Python dependencies to a requirements.txt file.
    
    Args:
        output_path: Path to write requirements.txt
        include_versions: Whether to include version pinning
        
    Returns:
        Path to the written requirements file
    """
    if include_versions:
        # Use pip freeze to get exact versions
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "freeze"],
                capture_output=True,
                text=True,
                check=True
            )
            dependencies = result.stdout.strip()
        except subprocess.CalledProcessError:
            # Fallback to basic dependencies
            dependencies = get_basic_dependencies()
    else:
        dependencies = get_basic_dependencies()
    
    output_path.write_text(dependencies + "\n", encoding="utf-8")
    return output_path


def get_basic_dependencies() -> str:
    """Get basic dependencies for ML training without version pinning.
    
    Returns:
        String with basic dependencies
    """
    deps = [
        "pandas",
        "scikit-learn", 
        "joblib",
        "numpy"
    ]
    return "\n".join(deps)


def validate_environment(required_packages: List[str]) -> Dict[str, Dict[str, str]]:
    """Validate that required packages are installed and get versions.
    
    Args:
        required_packages: List of package names to check
        
    Returns:
        Dictionary mapping package names to status info
    """
    results = {}
    
    for package in required_packages:
        try:
            # Try to import and get version
            if package == "sklearn":
                import sklearn
                version = sklearn.__version__
            elif package == "pandas":
                import pandas
                version = pandas.__version__
            elif package == "joblib":
                import joblib
                version = joblib.__version__
            elif package == "numpy":
                import numpy
                version = numpy.__version__
            else:
                # Generic import attempt
                module = __import__(package)
                version = getattr(module, "__version__", "unknown")
            
            results[package] = {
                "status": "installed",
                "version": version,
                "error": None
            }
            
        except ImportError as e:
            results[package] = {
                "status": "missing",
                "version": None,
                "error": str(e)
            }
    
    return results


def create_run_metadata(
    config: Dict[str, any],
    python_version: Optional[str] = None,
    git_hash: Optional[str] = None,
    environment_info: Optional[Dict] = None
) -> Dict[str, any]:
    """Create comprehensive run metadata for reproducibility.
    
    Args:
        config: Training configuration
        python_version: Python version (auto-detected if None)
        git_hash: Git commit hash (auto-detected if None)
        environment_info: Environment validation info
        
    Returns:
        Dictionary with run metadata
    """
    import platform
    
    metadata = {
        "config": config,
        "python_version": python_version or platform.python_version(),
        "platform": platform.platform(),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    
    # Add git info if available
    if git_hash is None:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=True
            )
            git_hash = result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            git_hash = "not_available"
    
    metadata["git_hash"] = git_hash
    
    # Add environment info if provided
    if environment_info:
        metadata["environment"] = environment_info
    
    return metadata


def save_run_metadata(
    metadata: Dict[str, any],
    output_path: Path
) -> Path:
    """Save run metadata to a JSON file.
    
    Args:
        metadata: Metadata dictionary
        output_path: Path to save the metadata
        
    Returns:
        Path to the saved metadata file
    """
    output_path.write_text(
        json.dumps(metadata, indent=2, sort_keys=True),
        encoding="utf-8"
    )
    return output_path


def check_reproducibility(run_dir: Path) -> Dict[str, any]:
    """Check if a run can be reproduced based on its artifacts.
    
    Args:
        run_dir: Directory containing run artifacts
        
    Returns:
        Dictionary with reproducibility check results
    """
    results = {
        "has_config": False,
        "has_metrics": False,
        "has_model": False,
        "has_requirements": False,
        "config_valid": False,
        "environment_matches": False,
        "overall_score": 0
    }
    
    # Check required files
    config_path = run_dir / "config.json"
    metrics_path = run_dir / "metrics.json"
    model_path = run_dir / "model.joblib"
    requirements_path = run_dir / "requirements.txt"
    
    results["has_config"] = config_path.exists()
    results["has_metrics"] = metrics_path.exists()
    results["has_model"] = model_path.exists()
    results["has_requirements"] = requirements_path.exists()
    
    # Validate config structure
    if results["has_config"]:
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            required_fields = ["input_csv", "label_col", "random_state", "max_iter"]
            results["config_valid"] = all(field in config for field in required_fields)
        except (json.JSONDecodeError, IOError):
            results["config_valid"] = False
    
    # Check environment (basic check)
    if results["has_requirements"]:
        try:
            with open(requirements_path, 'r') as f:
                requirements = f.read()
            
            # Check if key packages are mentioned
            key_packages = ["pandas", "scikit-learn", "joblib"]
            results["environment_matches"] = any(pkg in requirements for pkg in key_packages)
        except IOError:
            results["environment_matches"] = False
    
    # Calculate overall score
    score = 0
    if results["has_config"]: score += 25
    if results["has_metrics"]: score += 25
    if results["has_model"]: score += 25
    if results["has_requirements"]: score += 15
    if results["config_valid"]: score += 5
    if results["environment_matches"]: score += 5
    
    results["overall_score"] = score
    
    return results


def create_reproducibility_package(
    run_dir: Path,
    output_dir: Path,
    include_model: bool = True
) -> Path:
    """Create a complete reproducibility package from a run.
    
    Args:
        run_dir: Directory containing run artifacts
        output_dir: Directory to create the package
        include_model: Whether to include the model file
        
    Returns:
        Path to the created package directory
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy essential files
    files_to_copy = ["config.json", "metrics.json", "val_report.txt"]
    if include_model:
        files_to_copy.append("model.joblib")
    
    for filename in files_to_copy:
        src = run_dir / filename
        if src.exists():
            dst = output_dir / filename
        dst.write_bytes(src.read_bytes())
    
    # Generate requirements.txt
    requirements_path = output_dir / "requirements.txt"
    capture_dependencies(requirements_path)
    
    # Create README with reproduction instructions
    readme_path = output_dir / "README.md"
    readme_content = generate_reproducibility_readme(output_dir)
    readme_path.write_text(readme_content, encoding="utf-8")
    
    return output_dir


def generate_reproducibility_readme(package_dir: Path) -> str:
    """Generate README content for reproducing the experiment.
    
    Args:
        package_dir: Path to the package directory
        
    Returns:
        README content as string
    """
    lines = [
        "# ML Experiment Reproducibility Package",
        "",
        "This package contains all artifacts needed to reproduce an ML experiment.",
        "",
        "## Files",
        "",
        "- `config.json` - Training configuration",
        "- `metrics.json` - Results and metrics", 
        "- `val_report.txt` - Detailed validation report",
        "- `requirements.txt` - Python dependencies",
        "- `model.joblib` - Trained model (if included)",
        "",
        "## Reproduction Steps",
        "",
        "1. Set up environment:",
        "   ```bash",
        "   python -m venv repro_env",
        "   source repro_env/bin/activate  # On Windows: repro_env\\Scripts\\activate",
        "   pip install -r requirements.txt",
        "   ```",
        "",
        "2. Run the experiment:",
        "   ```bash",
        "   # Extract command from config.json and run",
        "   ```",
        "",
        "## Expected Results",
        "",
        "Refer to `metrics.json` for the expected performance metrics.",
        "",
        "## Notes",
        "",
        "- Results may vary slightly due to numerical precision differences",
        "- Ensure the same data file is used as specified in config.json",
        "- Random seed is controlled via the config for reproducibility"
    ]
    
    return "\n".join(lines)

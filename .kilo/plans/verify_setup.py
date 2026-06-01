#!/usr/bin/env python3
"""
Environment verification script for AI Engineering Fundamentals course.

Run this script to verify your environment is correctly set up.

Usage:
    python verify_setup.py
"""

import sys
import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


def check_python_version() -> Tuple[bool, str]:
    """Check Python version is 3.10 or higher."""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor}.{version.micro} (need 3.10+)"


def check_package(package_name: str, import_name: str = None) -> Tuple[bool, str]:
    """Check if a package is installed and get its version."""
    import_name = import_name or package_name
    try:
        module = __import__(import_name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, "not installed"


def check_ollama() -> Tuple[bool, str]:
    """Check if Ollama is running locally."""
    try:
        import requests
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        if resp.status_code == 200:
            models = resp.json().get("models", [])
            model_names = [m.get("name", "unknown") for m in models]
            return True, f"Running ({len(models)} models: {', '.join(model_names[:3])}{'...' if len(model_names) > 3 else ''})"
        return False, f"HTTP {resp.status_code}"
    except Exception as e:
        return False, f"Not running or not installed ({type(e).__name__})"


def run_verification() -> Dict[str, Tuple[bool, str]]:
    """Run all verification checks."""
    results = {}
    
    # Python version
    results["python"] = check_python_version()
    
    # Core packages
    core_packages = [
        ("numpy", "numpy"),
        ("pandas", "pandas"),
        ("requests", "requests"),
        ("matplotlib", "matplotlib"),
    ]
    
    for pkg, import_name in core_packages:
        results[pkg] = check_package(pkg, import_name)
    
    # ML packages
    ml_packages = [
        ("scikit-learn", "sklearn"),
        ("joblib", "joblib"),
    ]
    
    for pkg, import_name in ml_packages:
        results[pkg] = check_package(pkg, import_name)
    
    # LLM packages
    results["openai"] = check_package("openai", "openai")
    
    # Development packages
    results["pytest"] = check_package("pytest", "pytest")
    results["jupyter"] = check_package("jupyter", "jupyter")
    
    # Ollama (optional)
    results["ollama"] = check_ollama()
    
    return results


def print_results(results: Dict[str, Tuple[bool, str]]) -> None:
    """Print verification results."""
    print("\n" + "=" * 60)
    print("AI Engineering Fundamentals - Environment Verification")
    print("=" * 60 + "\n")
    
    # Core checks
    print("## Core Requirements\n")
    core_keys = ["python", "numpy", "pandas", "requests", "matplotlib"]
    for key in core_keys:
        status, info = results.get(key, (False, "not checked"))
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {key:15} {info}")
    
    # ML checks
    print("\n## ML Requirements\n")
    ml_keys = ["scikit-learn", "joblib"]
    for key in ml_keys:
        status, info = results.get(key, (False, "not checked"))
        symbol = "✓" if status else "✗"
        print(f"  {symbol} {key:15} {info}")
    
    # LLM checks
    print("\n## LLM Requirements\n")
    llm_keys = ["openai", "ollama"]
    for key in llm_keys:
        status, info = results.get(key, (False, "not checked"))
        symbol = "✓" if status else "○" if key == "ollama" else "✗"
        note = " (optional)" if key == "ollama" and not status else ""
        print(f"  {symbol} {key:15} {info}{note}")
    
    # Development checks
    print("\n## Development Tools\n")
    dev_keys = ["pytest", "jupyter"]
    for key in dev_keys:
        status, info = results.get(key, (False, "not checked"))
        symbol = "✓" if status else "○"
        print(f"  {symbol} {key:15} {info}")
    
    # Summary
    print("\n" + "-" * 60)
    
    required_keys = ["python", "numpy", "pandas", "requests", "scikit-learn", "joblib"]
    passed = sum(1 for k in required_keys if results.get(k, (False, ""))[0])
    total = len(required_keys)
    
    if passed == total:
        print(f"\n✓ All core requirements met ({passed}/{total})")
        print("\nYou're ready to start the course!")
    else:
        print(f"\n✗ Some requirements missing ({passed}/{total})")
        print("\nInstall missing packages with:")
        print("  pip install -r requirements.txt")
    
    print("\n" + "=" * 60 + "\n")


def main():
    """Main entry point."""
    results = run_verification()
    print_results(results)
    
    # Return exit code
    required_keys = ["python", "numpy", "pandas", "requests", "scikit-learn", "joblib"]
    passed = sum(1 for k in required_keys if results.get(k, (False, ""))[0])
    return 0 if passed == len(required_keys) else 1


if __name__ == "__main__":
    sys.exit(main())
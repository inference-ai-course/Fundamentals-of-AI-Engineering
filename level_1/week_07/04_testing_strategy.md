# Week 7 — Part 04: Testing strategy (pytest vs smoke tests)

## Overview

Tests are executable checks that protect you from regressions.

---

## Pre-study (Level 0)

Level 1 assumes Level 0 is complete. If you need a refresher on project structure, environments, and reproducibility:

- [Pre-study index (Level 1 → Level 0)](../PRESTUDY.md)
- [Level 0 — Chapter 2: Python and Environment Management](../../level_0/Chapters/2/Chapter2.md)

Why it matters here (Week 7):

- Interfaces are now stable enough (CLI/config/error behavior) that tests can protect you from regressions.
- For LLM projects, assert contracts (valid JSON/required keys/artifacts), not exact text.

---

## Minimal test plan (3+ cases)

You should have at least:

- **happy path**: normal input works
- **edge case**: missing values or tiny CSV
- **failure case**: missing file / invalid schema

Practical tip: smoke tests can be “one command” checks that run in CI later. The key is making them deterministic enough to be repeatable.

---

## Testing setup

```bash
pip install pytest pytest-cov
```

**Project structure:**
```
capstone/
  src/
    __init__.py
    pipeline.py
    profile.py
  tests/
    __init__.py
    test_pipeline.py
    test_profile.py
    fixtures/
      sample.csv
      empty.csv
  pytest.ini
```

**pytest.ini:**
```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = --verbose --strict-markers
```

---

## Basic test examples

### Test 1: Happy path

```python
import pytest
import pandas as pd
from pathlib import Path
from src.profile import compute_profile


def test_profile_normal_csv(tmp_path):
    """
    Test profiling with a normal CSV.
    """
    # Create test data
    csv_path = tmp_path / "test.csv"
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": [10, 20, 30],
        "name": ["A", "B", "C"],
    })
    df.to_csv(csv_path, index=False)
    
    # Run profiling
    profile = compute_profile(csv_path)
    
    # Assertions
    assert profile["n_rows"] == 3
    assert profile["n_cols"] == 3
    assert "id" in profile["columns"]
    assert profile["missing"]["id"] == 0
```

### Test 2: Edge case - missing values

```python
def test_profile_with_missing_values(tmp_path):
    """
    Test that missing values are counted correctly.
    """
    csv_path = tmp_path / "test_missing.csv"
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": [10, None, 30],
    })
    df.to_csv(csv_path, index=False)
    
    profile = compute_profile(csv_path)
    
    assert profile["missing"]["value"] == 1
```

### Test 3: Failure case

```python
from src.pipeline import InputValidationError


def test_load_nonexistent_file():
    """
    Test that missing file raises clear error.
    """
    with pytest.raises(InputValidationError) as exc_info:
        load_csv(Path("does_not_exist.csv"))
    
    # Check error message is helpful
    assert "not found" in str(exc_info.value).lower()
```

---

## Testing LLM code (without calling LLM)

### Pattern 1: Mock the LLM call

```python
import pytest
from unittest.mock import Mock, patch


def test_pipeline_with_mock_llm(tmp_path):
    """
    Test pipeline logic without calling real LLM.
    """
    # Setup test data
    csv_path = tmp_path / "test.csv"
    pd.DataFrame({"col": [1, 2, 3]}).to_csv(csv_path, index=False)
    
    # Mock LLM response
    mock_llm_response = {
        "analysis": "Test analysis",
        "insights": ["Insight 1"]
    }
    
    with patch('src.pipeline.call_llm') as mock_llm:
        mock_llm.return_value = mock_llm_response
        
        # Run pipeline
        result = run_pipeline(csv_path, output_dir=tmp_path)
        
        # Verify LLM was called
        assert mock_llm.called
        # Verify output uses mock response
        assert result["analysis"] == "Test analysis"
```

### Pattern 2: Test prompt construction

```python
def test_build_prompt():
    """
    Test prompt is built correctly (no LLM call needed).
    """
    compressed_data = {
        "shape": [100, 5],
        "columns": ["a", "b", "c", "d", "e"],
    }
    
    prompt = build_analysis_prompt(compressed_data)
    
    # Check prompt contains key info
    assert "100" in prompt  # Row count
    assert "5" in prompt    # Column count
    assert "a" in prompt    # Column name
    assert len(prompt) < 5000  # Not too long
```

### Pattern 3: Test output validation

```python
import json


def test_validate_llm_response():
    """
    Test that response validation catches bad outputs.
    """
    # Valid response
    valid = {"analysis": "text", "insights": ["item"]}
    assert validate_llm_response(valid) is True
    
    # Invalid responses
    invalid_cases = [
        {},  # Missing keys
        {"analysis": "text"},  # Missing insights
        {"analysis": "", "insights": []},  # Empty values
        {"analysis": 123, "insights": ["item"]},  # Wrong type
    ]
    
    for invalid in invalid_cases:
        with pytest.raises(ValueError):
            validate_llm_response(invalid)
```

---

## Fixtures for reusable test data

```python
import pytest
import pandas as pd


@pytest.fixture
def sample_csv(tmp_path):
    """
    Create a sample CSV for testing.
    """
    csv_path = tmp_path / "sample.csv"
    df = pd.DataFrame({
        "id": [1, 2, 3, 4, 5],
        "value": [10, 20, None, 40, 50],
        "category": ["A", "B", "A", None, "C"],
    })
    df.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def empty_csv(tmp_path):
    """
    Create an empty CSV.
    """
    csv_path = tmp_path / "empty.csv"
    pd.DataFrame().to_csv(csv_path, index=False)
    return csv_path


# Use fixtures in tests
def test_with_fixture(sample_csv):
    profile = compute_profile(sample_csv)
    assert profile["n_rows"] == 5
```

---

## Integration test (end-to-end)

```python
import pytest
import json
from pathlib import Path


@pytest.mark.integration
def test_full_pipeline_dry_run(sample_csv, tmp_path):
    """
    Test full pipeline in dry-run mode (no real LLM).
    """
    output_dir = tmp_path / "output"
    
    # Run with dry_run=True
    run_pipeline(
        input_csv=sample_csv,
        output_dir=output_dir,
        dry_run=True
    )
    
    # Check all artifacts exist
    assert (output_dir / "01_loaded.parquet").exists()
    assert (output_dir / "02_profile.json").exists()
    assert (output_dir / "03_compressed.json").exists()
    assert (output_dir / "05_report.json").exists()
    
    # Check report has expected structure
    report = json.loads((output_dir / "05_report.json").read_text())
    assert "dataset_summary" in report
    assert "llm_analysis" in report
```

---

## Smoke test script

```bash
#!/bin/bash
# smoke_test.sh - Quick validation that pipeline runs

set -e  # Exit on error

echo "Running smoke test..."

# Create test data
echo "id,value" > test_data.csv
echo "1,10" >> test_data.csv
echo "2,20" >> test_data.csv

# Run pipeline in dry-run mode
python run_capstone.py \
  --input test_data.csv \
  --output_dir smoke_test_output \
  --dry-run

# Check outputs exist
test -f smoke_test_output/05_report.json || exit 1
test -f smoke_test_output/05_report.md || exit 1

echo "✓ Smoke test passed"

# Cleanup
rm -rf smoke_test_output test_data.csv
```

---

## Test organization

```python
# tests/test_pipeline.py
import pytest

class TestDataLoading:
    """Tests for data loading stage."""
    
    def test_load_valid_csv(self, sample_csv):
        df = load_csv(sample_csv)
        assert len(df) > 0
    
    def test_load_missing_file(self):
        with pytest.raises(InputValidationError):
            load_csv(Path("missing.csv"))


class TestProfileStage:
    """Tests for profiling stage."""
    
    def test_profile_output_schema(self, sample_csv):
        profile = compute_profile(sample_csv)
        required_keys = ["n_rows", "n_cols", "columns", "missing"]
        for key in required_keys:
            assert key in profile
    
    def test_profile_deterministic(self, sample_csv):
        """Profile should be same on repeat runs."""
        p1 = compute_profile(sample_csv)
        p2 = compute_profile(sample_csv)
        assert p1 == p2
```

---

## Running tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_pipeline.py

# Run specific test
pytest tests/test_pipeline.py::test_profile_normal_csv

# Run only integration tests
pytest -m integration

# Run fast tests only (skip slow ones)
pytest -m "not slow"

# Verbose output
pytest -v

# Stop on first failure
pytest -x
```

---

## Test markers

```python
import pytest

@pytest.mark.slow
def test_large_dataset():
    """Skip this in quick test runs."""
    pass

@pytest.mark.integration
def test_full_pipeline():
    """Mark as integration test."""
    pass

@pytest.mark.skipif(not has_api_key(), reason="No API key")
def test_real_llm_call():
    """Skip if API key not available."""
    pass
```

---

## Coverage goals

**Minimum coverage targets:**
- Data loading/validation: 100% (critical path)
- Profiling logic: 90%+
- Compression: 80%+
- LLM integration: 60%+ (hard to test without mocks)
- Report generation: 80%+

**Focus on:**
- Input validation (prevent bad data)
- Error paths (ensure graceful failures)
- Output contracts (stable schemas)

---

## Practice notebook

For hands-on testing exercises, see:
- **[04_testing_strategy.ipynb](./04_testing_strategy.ipynb)** - Interactive test development
- **[practice.ipynb](./practice.ipynb)** - Extended exercises

---

## Self-check

- Can you run tests without calling real LLM APIs?
- Do your tests catch regression errors (e.g., breaking changes)?
- Can you run tests quickly (<10s for unit tests)?
- Do tests fail with clear messages when something breaks?
- Have you tested both success and failure paths?

---

## References

- pytest docs: https://docs.pytest.org/
- pytest fixtures: https://docs.pytest.org/en/stable/how-to/fixtures.html
- unittest.mock: https://docs.python.org/3/library/unittest.mock.html
- pytest-cov: https://pytest-cov.readthedocs.io/

# Testing Guide

## Overview

Circuit-Bench uses automated testing to ensure code quality, benchmark reproducibility, and dataset integrity. Contributors should run the full test suite before opening a pull request.

---

# Test Categories

## Unit Tests

Validate individual functions and modules.

Example:

```bash
pytest tests/unit
```

---

## Integration Tests

Verify interactions between components such as the CLI, datasets, benchmark runners, and metrics.

```bash
pytest tests/integration
```

---

## Dataset Validation

Checks:

* Required files exist
* Metadata schema validation
* Label consistency
* Ground-truth integrity
* Duplicate detection

Example:

```bash
python -m circuit_bench validate datasets/
```

---

## Benchmark Tests

Ensure benchmark execution produces reproducible results.

Checks include:

* Successful execution
* Metric generation
* Result reproducibility
* Output formatting

---

## Performance Tests

Measure:

* Runtime
* Memory usage
* Dataset loading speed
* Benchmark throughput

---

## Regression Tests

Prevent previously fixed bugs from reappearing.

Every bug fix should include a regression test.

---

## Continuous Integration

GitHub Actions automatically execute:

* Formatting checks
* Ruff
* Flake8
* Pytest
* Documentation validation

All checks must pass before merging.

---

# Running the Full Test Suite

```bash
pytest
```

or

```bash
pytest tests
```

---

# Coverage

Generate a coverage report:

```bash
pytest --cov=src --cov-report=term
```

HTML report:

```bash
pytest --cov=src --cov-report=html
```

---

# Writing New Tests

Guidelines:

* One behavior per test
* Descriptive test names
* Independent execution
* Deterministic outputs
* Avoid hidden dependencies

Example naming:

* test_dataset_loading.py
* test_cli.py
* test_metrics.py
* test_validation.py

---

# Dataset Testing Checklist

* Metadata valid
* Schema valid
* Labels complete
* Ground truths present
* Required files exist
* Licenses documented
* Checksums verified

---

# Benchmark Validation Checklist

* Benchmark completes successfully
* Metrics generated correctly
* Results reproducible
* Runtime acceptable
* Documentation updated

---

# Best Practices

* Keep tests fast.
* Keep tests deterministic.
* Add tests for every new feature.
* Update regression tests when fixing bugs.
* Ensure CI passes before submitting changes.

---

# Troubleshooting

Common issues include:

* Missing dependencies
* Incorrect dataset paths
* Invalid metadata
* Failed schema validation
* Missing benchmark assets

Review CI logs for detailed error messages.

---

# References

* Pytest Documentation
* GitHub Actions Documentation
* Ruff Documentation
* Flake8 Documentation

Following this guide helps maintain the reliability, reproducibility, and scientific quality of Circuit-Bench.


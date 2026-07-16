# Adding Benchmarks

## Overview

This guide explains how to add new benchmark tasks to Circuit-Bench. Benchmarks are the core of the project and should be reproducible, well documented, scientifically meaningful, and easy for the community to use.

Circuit-Bench supports benchmarks for analog, digital, RF, power electronics, passive, mixed-signal, and emerging circuit technologies.

---

# Benchmark Design Principles

Every benchmark should be:

* Reproducible
* Clearly defined
* Scientifically relevant
* Well documented
* Fair
* Extensible
* Easy to evaluate

A benchmark should measure a specific capability and provide objective evaluation criteria.

---

# Before Creating a Benchmark

Verify that the benchmark includes:

* A clearly defined research problem
* Appropriate datasets
* Ground-truth labels (if applicable)
* Evaluation metrics
* Baseline methods
* Documentation
* Licensing information

---

# Recommended Directory Structure

```text
benchmarks/
└── <benchmark_name>/
    ├── README.md
    ├── benchmark.yaml
    ├── metadata.yaml
    ├── evaluation.md
    ├── metrics.md
    ├── baselines.md
    ├── citation.bib
    ├── LICENSE
    ├── datasets/
    ├── examples/
    ├── scripts/
    ├── results/
    ├── reports/
    ├── validation/
    └── tests/
```

---

# Required Documentation

## README.md

Describe:

* Benchmark objective
* Scientific motivation
* Supported circuit categories
* Inputs
* Outputs
* Evaluation workflow
* Example usage

---

## benchmark.yaml

Recommended fields:

* Benchmark name
* Version
* Authors
* Maintainers
* Categories
* Dataset dependencies
* Evaluation protocol
* Supported metrics
* License
* Release date

---

## metadata.yaml

Include:

* Identifier
* Version
* Description
* Citation
* Related publications
* Tags
* Status
* Dependencies

---

# Evaluation Protocol

Every benchmark should define:

* Input format
* Expected output
* Evaluation procedure
* Scoring method
* Acceptance criteria
* Reproducibility requirements

Evaluation procedures should be deterministic whenever practical.

---

# Metrics

Document all reported metrics.

Examples include:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Runtime
* Memory usage
* Throughput
* Power consumption
* Area
* Delay

Clearly explain how each metric is computed.

---

# Baseline Methods

Whenever possible, include reference baselines.

For each baseline provide:

* Description
* Implementation
* Configuration
* Results
* Citation

Baseline methods provide useful points of comparison for future work.

---

# Datasets

Document every dataset used by the benchmark, including:

* Source
* Version
* License
* Citation
* Preprocessing steps
* Train/validation/test split
* Metadata

---

# Validation

Before publishing a benchmark:

* Validate datasets
* Verify benchmark scripts
* Confirm metric calculations
* Review documentation
* Check reproducibility
* Ensure examples execute successfully

---

# Results

Include representative benchmark outputs where appropriate.

Recommended contents:

* Summary tables
* Performance metrics
* Runtime information
* Hardware configuration
* Reproducibility notes

---

# Testing

Each benchmark should include automated tests covering:

* Configuration validation
* Dataset loading
* Metric computation
* Benchmark execution
* Report generation

---

# Naming Conventions

Use lowercase names with underscores.

Examples:

* analog_fault_detection
* digital_logic_synthesis
* rf_signal_classification
* power_converter_efficiency

---

# Pull Requests

Benchmark contributions should include:

* Complete documentation
* Benchmark configuration
* Metadata
* Evaluation protocol
* Baseline information
* Tests
* Validation results

---

# Best Practices

* Focus each benchmark on a clearly defined problem.
* Prefer publicly available datasets when possible.
* Document all assumptions.
* Report reproducible results.
* Cite original datasets and methods.
* Keep benchmark configurations versioned.
* Update documentation whenever the benchmark changes.

Following these practices helps ensure that Circuit-Bench remains a rigorous, transparent, and reproducible benchmarking platform for the circuit research community.


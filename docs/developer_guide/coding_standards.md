# Coding Standards

## Overview

This document defines the coding standards for Circuit-Bench. Consistent coding practices improve readability, maintainability, reproducibility, and long-term sustainability.

---

# Guiding Principles

All code should be:

* Readable
* Maintainable
* Modular
* Well documented
* Tested
* Reproducible
* Consistent

Code is written for future contributors as much as for current developers.

---

# Python Version

Circuit-Bench targets supported Python versions as defined in the project's CI configuration.

Avoid using features that are incompatible with the supported versions.

---

# Code Style

Follow the PEP 8 style guide.

General recommendations:

* Four spaces per indentation level.
* Maximum practical line length as defined by the project's formatter configuration.
* One statement per line.
* Consistent spacing around operators.
* Meaningful variable names.

---

# Formatting

Source code should be formatted automatically before committing.

Formatting should remain consistent across the repository.

---

# Linting

All code should pass the configured static analysis tools before submission.

Common issues include:

* Unused imports
* Unused variables
* Shadowed names
* Dead code
* Undefined variables

Resolve all reported issues before opening a pull request.

---

# Naming Conventions

## Variables

Use descriptive snake_case names.

Example:

* dataset_path
* benchmark_results
* evaluation_metrics

Avoid abbreviations unless they are widely understood.

---

## Functions

Function names should clearly describe their behavior.

Examples:

* load_dataset()
* validate_metadata()
* calculate_metrics()
* generate_report()

Functions should perform one logical task.

---

## Classes

Use PascalCase.

Examples:

* DatasetLoader
* BenchmarkRunner
* MetricsCalculator

---

## Constants

Use uppercase with underscores.

Examples:

* DEFAULT_TIMEOUT
* MAX_DATASET_SIZE

---

# Imports

Group imports in the following order:

1. Standard library
2. Third-party packages
3. Local project modules

Remove unused imports.

---

# Documentation

Public classes and functions should include docstrings describing:

* Purpose
* Parameters
* Return values
* Exceptions (when applicable)

Complex algorithms should include explanatory comments where helpful.

---

# Error Handling

Handle errors explicitly.

Prefer informative exceptions over silent failures.

Error messages should help users identify and resolve problems.

---

# Logging

Use structured logging where appropriate.

Avoid excessive logging.

Do not expose sensitive information in logs.

---

# Testing

Every new feature should include appropriate tests whenever practical.

Tests should be:

* Independent
* Deterministic
* Easy to understand
* Fast to execute

---

# Performance

Optimize only after correctness.

Avoid unnecessary complexity.

Document significant performance trade-offs.

---

# Security

Never commit:

* Passwords
* API keys
* Tokens
* Private credentials

Validate external inputs whenever possible.

---

# Documentation Updates

Code changes should be accompanied by documentation updates when applicable.

Examples include:

* User guides
* Developer guides
* API documentation
* Examples
* Benchmark documentation

---

# Pull Request Checklist

Before submitting code:

* Formatting completed
* Linting passed
* Tests passed
* Documentation updated
* No unnecessary files included
* Commit messages are descriptive

---

# Continuous Improvement

These coding standards may evolve as Circuit-Bench grows. Contributors are encouraged to suggest improvements that enhance code quality, maintainability, and reproducibility while preserving consistency across the project.

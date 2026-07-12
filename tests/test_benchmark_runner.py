"""
Unit tests for BenchmarkRunner.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.benchmark.benchmark_runner import BenchmarkRunner


# ---------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------

def test_runner_initialization():

    runner = BenchmarkRunner()

    assert runner.name == "CircuitBench"
    assert runner.number_of_models == 0
    assert runner.number_of_datasets == 0
    assert runner.number_of_metrics == 0


def test_random_seed():

    runner = BenchmarkRunner(random_state=123)

    assert runner.random_state == 123


# ---------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------

def test_add_dataset(dataset):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    assert runner.number_of_datasets == 1


def test_add_model(model):

    runner = BenchmarkRunner()

    runner.add_model(model)

    assert runner.number_of_models == 1


def test_add_metric():

    runner = BenchmarkRunner()

    runner.add_metric(
        "MAE",
        lambda y, p: np.mean(np.abs(y - p)),
    )

    assert "MAE" in runner.metrics


# ---------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------

def test_validation_requires_dataset(model):

    runner = BenchmarkRunner()

    runner.add_model(model)

    runner.add_metric(
        "MAE",
        lambda y, p: 0,
    )

    with pytest.raises(RuntimeError):

        runner.validate()


def test_validation_requires_model(dataset):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_metric(
        "MAE",
        lambda y, p: 0,
    )

    with pytest.raises(RuntimeError):

        runner.validate()


def test_validation_requires_metric(dataset, model):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_model(model)

    with pytest.raises(RuntimeError):

        runner.validate()


# ---------------------------------------------------------------------
# Inspection
# ---------------------------------------------------------------------

def test_dataset_inspection(dataset):

    runner = BenchmarkRunner()

    info = runner.inspect_dataset(dataset)

    assert info["samples"] == 200

    assert info["targets"] == 200


def test_model_inspection(model):

    runner = BenchmarkRunner()

    info = runner.inspect_model(model)

    assert info["name"] == "Linear Regression"

    assert "LinearRegression" in info["type"]


# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------

def test_registration_summary(dataset, model):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_model(model)

    runner.add_metric(
        "MAE",
        lambda y, p: 0,
    )

    summary = runner.registration_summary()

    assert len(summary["datasets"]) == 1

    assert len(summary["models"]) == 1

    assert len(summary["metrics"]) == 1


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


# ---------------------------------------------------------------------
# Timing
# ---------------------------------------------------------------------

def test_timer():

    runner = BenchmarkRunner()

    runner.start_timer()

    elapsed = runner.stop_timer()

    assert elapsed >= 0


# ---------------------------------------------------------------------
# History
# ---------------------------------------------------------------------

def test_history_logging():

    runner = BenchmarkRunner()

    runner.log_history(
        model="Dummy",
        dataset="Dummy",
        accuracy=0.95,
    )

    assert len(runner.history) == 1

    assert runner.history[0]["model"] == "Dummy"


# ---------------------------------------------------------------------
# Result Recording
# ---------------------------------------------------------------------

def test_add_result(model, dataset):

    runner = BenchmarkRunner()

    runner.add_result(
        model,
        dataset,
        {
            "RMSE": 0.10,
            "MAE": 0.05,
        },
    )

    assert len(runner.results) == 1

    result = runner.results[0]

    assert result["RMSE"] == 0.10

    assert result["MAE"] == 0.05


# ---------------------------------------------------------------------
# Results DataFrame
# ---------------------------------------------------------------------

def test_results_dataframe(model, dataset):

    runner = BenchmarkRunner()

    runner.add_result(
        model,
        dataset,
        {
            "RMSE": 0.10,
        },
    )

    df = runner.results_dataframe()

    assert isinstance(df, pd.DataFrame)

    assert len(df) == 1

    assert "RMSE" in df.columns


# ---------------------------------------------------------------------
# Clear Results
# ---------------------------------------------------------------------

def test_clear_results(model, dataset):

    runner = BenchmarkRunner()

    runner.add_result(
        model,
        dataset,
        {
            "RMSE": 1.0,
        },
    )

    runner.clear_results()

    assert len(runner.results) == 0

    assert len(runner.history) == 0

    assert runner.statistics == {}


# ---------------------------------------------------------------------
# Callback
# ---------------------------------------------------------------------

def test_callback_execution():

    runner = BenchmarkRunner()

    called = []

    def callback(event, **kwargs):

        called.append(event)

    runner.add_callback(callback)

    runner._execute_callbacks("before_run")

    assert called == ["before_run"]


# ---------------------------------------------------------------------
# Benchmark Summary
# ---------------------------------------------------------------------

def test_summary_dictionary():

    runner = BenchmarkRunner()

    summary = runner.benchmark_summary()

    assert isinstance(summary, dict)

    assert summary["benchmark"] == "CircuitBench"


# ---------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------

def test_metadata():

    runner = BenchmarkRunner()

    metadata = runner.benchmark_metadata()

    assert isinstance(metadata, dict)

    assert "system" in metadata

    assert "runner" in metadata


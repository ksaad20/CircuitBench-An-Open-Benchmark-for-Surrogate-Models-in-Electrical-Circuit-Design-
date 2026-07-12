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


# ---------------------------------------------------------------------
# Metric Evaluation
# ---------------------------------------------------------------------


def test_evaluate_metrics():

    runner = BenchmarkRunner()

    runner.add_metric(
        "MAE",
        lambda y, p: np.mean(np.abs(y - p)),
    )

    y_true = np.array([1.0, 2.0, 3.0])

    y_pred = np.array([1.1, 2.1, 2.9])

    metrics = runner._evaluate_metrics(
        y_true,
        y_pred,
    )

    assert "MAE" in metrics

    assert metrics["MAE"] >= 0.0


def test_metric_failure_returns_nan():

    runner = BenchmarkRunner()

    def bad_metric(y, p):
        raise RuntimeError("Intentional failure")

    runner.add_metric(
        "Broken",
        bad_metric,
    )

    metrics = runner._evaluate_metrics(
        np.array([1]),
        np.array([1]),
    )

    assert np.isnan(metrics["Broken"])


# ---------------------------------------------------------------------
# Model Fit / Predict
# ---------------------------------------------------------------------


def test_fit_model(model, dataset):

    runner = BenchmarkRunner()

    elapsed = runner._fit_model(
        model,
        dataset.X_train,
        dataset.y_train,
    )

    assert elapsed >= 0


def test_predict(model, dataset):

    runner = BenchmarkRunner()

    model.fit(
        dataset.X_train,
        dataset.y_train,
    )

    predictions, elapsed = runner._predict(
        model,
        dataset.X_test,
    )

    assert len(predictions) == len(dataset.X_test)

    assert elapsed >= 0


# ---------------------------------------------------------------------
# Single Benchmark
# ---------------------------------------------------------------------


def test_run_single(dataset, model):

    runner = BenchmarkRunner()

    runner.add_metric(
        "MAE",
        lambda y, p: np.mean(np.abs(y - p)),
    )

    metrics = runner.run_single(
        model,
        dataset,
    )

    assert "MAE" in metrics

    assert len(runner.results) == 1


# ---------------------------------------------------------------------
# Complete Benchmark
# ---------------------------------------------------------------------


def test_complete_run(dataset, model):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_model(model)

    runner.add_metric(
        "MAE",
        lambda y, p: np.mean(np.abs(y - p)),
    )

    df = runner.run()

    assert isinstance(df, pd.DataFrame)

    assert len(df) == 1


# ---------------------------------------------------------------------
# Cross Validation Configuration
# ---------------------------------------------------------------------


def test_cv_configuration():

    runner = BenchmarkRunner()

    runner.configure_cross_validation(
        strategy="kfold",
        folds=10,
    )

    assert runner.cv_strategy == "kfold"

    assert runner.cv_folds == 10


# ---------------------------------------------------------------------
# Checkpoint
# ---------------------------------------------------------------------


def test_checkpoint_cycle(tmp_path):

    runner = BenchmarkRunner(
        output_directory=str(tmp_path),
    )

    runner.history.append({"epoch": 1})

    runner.save_checkpoint()

    runner.history = []

    runner.load_checkpoint()

    assert len(runner.history) == 1


# ---------------------------------------------------------------------
# Resource Profiling
# ---------------------------------------------------------------------


def test_profile_system():

    runner = BenchmarkRunner()

    profile = runner.profile_system()

    assert isinstance(profile, dict)

    assert "cpu_count" in profile

    assert "memory_gb" in profile

    assert profile["cpu_count"] >= 1


def test_memory_usage():

    runner = BenchmarkRunner()

    memory = runner.memory_usage_mb()

    assert isinstance(memory, float)

    assert memory > 0


def test_model_size(model):

    runner = BenchmarkRunner()

    size = runner.model_size_mb(model)

    assert isinstance(size, float)

    assert size >= 0


# ---------------------------------------------------------------------
# Export Results
# ---------------------------------------------------------------------


def test_export_results(tmp_path, model, dataset):

    runner = BenchmarkRunner(
        output_directory=str(tmp_path),
    )

    runner.add_result(
        model,
        dataset,
        {
            "RMSE": 0.25,
        },
    )

    runner.export_results()

    assert (tmp_path / "results.csv").exists()


def test_save_configuration(tmp_path):

    runner = BenchmarkRunner(
        output_directory=str(tmp_path),
    )

    runner.save_configuration()

    assert (tmp_path / "configuration.json").exists()


def test_export_all(tmp_path):

    runner = BenchmarkRunner(
        output_directory=str(tmp_path),
    )

    runner.export_all()

    assert (tmp_path / "results.csv").exists()

    assert (tmp_path / "configuration.json").exists()

    assert (tmp_path / "checkpoint.json").exists()


# ---------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------


def test_runner_summary():

    runner = BenchmarkRunner()

    summary = runner.summary()

    assert summary is None


def test_benchmark_summary_fields():

    runner = BenchmarkRunner()

    summary = runner.benchmark_summary()

    required = {
        "benchmark",
        "models",
        "datasets",
        "metrics",
        "runs",
        "output_directory",
    }

    assert required.issubset(summary.keys())


# ---------------------------------------------------------------------
# Utility Properties
# ---------------------------------------------------------------------


def test_property_counts(dataset, model):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_model(model)

    runner.add_metric(
        "MAE",
        lambda y, p: 0,
    )

    assert runner.number_of_datasets == 1

    assert runner.number_of_models == 1

    assert runner.number_of_metrics == 1


# ---------------------------------------------------------------------
# Empty Results
# ---------------------------------------------------------------------


def test_empty_dataframe():

    runner = BenchmarkRunner()

    df = runner.results_dataframe()

    assert df.empty


# ---------------------------------------------------------------------
# Framework Integration
# ---------------------------------------------------------------------

from src.benchmark.leaderboard import Leaderboard
from src.benchmark.reporting import BenchmarkReport

try:
    from src.benchmark.experiment import Experiment
except ImportError:
    Experiment = None


def test_attach_leaderboard():

    runner = BenchmarkRunner()

    leaderboard = Leaderboard()

    runner.attach_leaderboard(leaderboard)

    assert runner.leaderboard is leaderboard


def test_attach_report():

    runner = BenchmarkRunner()

    report = BenchmarkReport("Unit Test")

    runner.attach_report(report)

    assert runner.report is report


def test_attach_experiment():

    if Experiment is None:
        pytest.skip("Experiment class not implemented.")

    runner = BenchmarkRunner()

    experiment = Experiment("Unit Test")

    runner.attach_experiment(experiment)

    assert runner.experiment is experiment


# ---------------------------------------------------------------------
# Leaderboard Integration
# ---------------------------------------------------------------------


def test_update_leaderboard(dataset, model):

    runner = BenchmarkRunner()

    leaderboard = Leaderboard()

    runner.attach_leaderboard(leaderboard)

    runner.add_result(
        model,
        dataset,
        {
            "MAE": 0.2,
            "RMSE": 0.3,
        },
    )

    ranking = runner.update_leaderboard("MAE")

    assert ranking is not None


# ---------------------------------------------------------------------
# Report Integration
# ---------------------------------------------------------------------


def test_generate_report(tmp_path, dataset, model):

    report = BenchmarkReport("Benchmark Test")

    runner = BenchmarkRunner(
        output_directory=str(tmp_path),
    )

    runner.attach_report(report)

    runner.add_result(
        model,
        dataset,
        {
            "RMSE": 0.25,
        },
    )

    runner.generate_report()

    assert (tmp_path / "benchmark_report.json").exists()


# ---------------------------------------------------------------------
# Callback Lifecycle
# ---------------------------------------------------------------------


def test_multiple_callbacks():

    runner = BenchmarkRunner()

    calls = []

    def callback_a(event, **kwargs):

        calls.append(("A", event))

    def callback_b(event, **kwargs):

        calls.append(("B", event))

    runner.add_callback(callback_a)

    runner.add_callback(callback_b)

    runner._execute_callbacks("benchmark_start")

    assert len(calls) == 2

    assert calls[0][1] == "benchmark_start"


# ---------------------------------------------------------------------
# Error Recovery
# ---------------------------------------------------------------------


class BrokenModel:
    name = "Broken Model"

    def fit(self, X, y):

        raise RuntimeError("Intentional failure")

    def predict(self, X):

        return np.zeros(len(X))


def test_continue_on_error(dataset):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_model(BrokenModel())

    runner.add_metric(
        "MAE",
        lambda y, p: 0,
    )

    df = runner.run(
        continue_on_error=True,
    )

    assert isinstance(
        df,
        pd.DataFrame,
    )


# ---------------------------------------------------------------------
# Smoke Test
# ---------------------------------------------------------------------


def test_end_to_end(dataset, model):

    runner = BenchmarkRunner()

    runner.add_dataset(dataset)

    runner.add_model(model)

    runner.add_metric(
        "MAE",
        lambda y, p: np.mean(np.abs(y - p)),
    )

    results = runner.run()

    assert len(results) == 1

    assert "MAE" in results.columns


# ---------------------------------------------------------------------
# Framework Integration
# ---------------------------------------------------------------------

try:
    from src.benchmark.experiment import Experiment
except ImportError:
    Experiment = None

# ---------------------------------------------------------------------
# Report Integration
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Callback Lifecycle
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Error Recovery
# ---------------------------------------------------------------------


# Smoke Test
# ---------------------------------------------------------------------

    

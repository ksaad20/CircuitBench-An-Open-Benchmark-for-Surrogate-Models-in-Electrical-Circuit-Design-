"""
CircuitBench Benchmark Runner
=============================

Central engine responsible for training, evaluating and comparing
all registered models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import time
from typing import Any, Dict, List

import numpy as np

from src.models.factory import ModelFactory


class BenchmarkRunner:
    """
    Central benchmark engine.
    """

    def __init__(self):

        self.results = []

    # -------------------------------------------------------

    def evaluate_model(
        self,
        model,
        X_train,
        y_train,
        X_test,
        y_test,
    ) -> Dict[str, Any]:

        start = time.perf_counter()

        model.fit(X_train, y_train)

        train_time = time.perf_counter() - start

        start = time.perf_counter()

        predictions = model.predict(X_test)

        inference_time = time.perf_counter() - start

        score = model.score(
            X_test,
            y_test,
        )

        result = {

            "model": model.name,

            "score": float(score),

            "train_time": train_time,

            "inference_time": inference_time,

            "n_train": len(y_train),

            "n_test": len(y_test),

        }

        self.results.append(result)

        return result

    # -------------------------------------------------------

    def evaluate_models(

        self,

        model_names: List[str],

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        results = []

        for name in model_names:

            model = ModelFactory.create(name)

            results.append(

                self.evaluate_model(

                    model,

                    X_train,

                    y_train,

                    X_test,

                    y_test,

                )

            )

        return results

    # -------------------------------------------------------

    def leaderboard(self):

        return sorted(

            self.results,

            key=lambda x: x["score"],

            reverse=True,

        )

    # -------------------------------------------------------

    def clear(self):

        self.results.clear()

    # -------------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Benchmark Summary")

        print("=" * 70)

        for row in self.leaderboard():

            print(

                f"{row['model']:25}"

                f"{row['score']:.4f}"

            )

        print("=" * 70)


    ####################################################################
    # Validation
    ####################################################################

    def validate(self):

        """
        Validate benchmark configuration before execution.
        """

        if len(self.models) == 0:

            raise RuntimeError(
                "No models have been registered."
            )

        if len(self.datasets) == 0:

            raise RuntimeError(
                "No datasets have been registered."
            )

        if len(self.metrics) == 0:

            raise RuntimeError(
                "No evaluation metrics have been registered."
            )

        self.logger.info(
            "Benchmark validation successful."
        )

    ####################################################################
    # Dataset Inspection
    ####################################################################

    def inspect_dataset(self, dataset):

        info = {}

        if hasattr(dataset, "X"):

            info["samples"] = len(dataset.X)

            if hasattr(dataset.X, "shape"):

                info["shape"] = dataset.X.shape

        if hasattr(dataset, "y"):

            info["targets"] = len(dataset.y)

        if hasattr(dataset, "feature_names"):

            info["features"] = len(dataset.feature_names)

        return info

    ####################################################################
    # Model Inspection
    ####################################################################

    def inspect_model(self, model):

        return {

            "name": getattr(

                model,

                "name",

                model.__class__.__name__,

            ),

            "type": model.__class__.__name__,

            "module": model.__class__.__module__,

        }

    ####################################################################
    # Registration Summary
    ####################################################################

    def registration_summary(self):

        return {

            "datasets":

                [

                    self.inspect_dataset(d)

                    for d in self.datasets

                ],

            "models":

                [

                    self.inspect_model(m)

                    for m in self.models

                ],

            "metrics":

                list(

                    self.metrics.keys()

                ),

        }

    ####################################################################
    # Cross Validation
    ####################################################################

    def configure_cross_validation(

        self,

        strategy="kfold",

        folds=5,

        shuffle=True,

    ):

        self.cv_strategy = strategy

        self.cv_folds = folds

        self.cv_shuffle = shuffle

        self.logger.info(

            "Cross-validation: %s (%d folds)",

            strategy,

            folds,

        )

    ####################################################################
    # Timing
    ####################################################################

    def start_timer(self):

        self._benchmark_start = time.perf_counter()

    def stop_timer(self):

        elapsed = (

            time.perf_counter()

            -

            self._benchmark_start

        )

        return elapsed

    ####################################################################
    # History
    ####################################################################

    def log_history(

        self,

        **kwargs,

    ):

        self.history.append(kwargs)

    ####################################################################
    # Result Recording
    ####################################################################

    def add_result(

        self,

        model,

        dataset,

        metric_values,

    ):

        record = {

            "model":

                getattr(

                    model,

                    "name",

                    str(model),

                ),

            "dataset":

                getattr(

                    dataset,

                    "name",

                    str(dataset),

                ),

        }

        record.update(metric_values)

        self.results.append(record)

    ####################################################################
    # Result DataFrame
    ####################################################################

    def results_dataframe(self):

        import pandas as pd

        return pd.DataFrame(

            self.results

        )

    ####################################################################
    # Export Results
    ####################################################################

    def export_results(

        self,

        filename="results.csv",

    ):

        self.results_dataframe().to_csv(

            self.output_directory / filename,

            index=False,

        )

        self.logger.info(

            "Results written to %s",

            filename,

        )


    ####################################################################
    # Internal Execution Helpers
    ####################################################################

    def _fit_model(
        self,
        model,
        X_train,
        y_train,
    ):

        start = time.perf_counter()

        model.fit(
            X_train,
            y_train,
        )

        elapsed = time.perf_counter() - start

        return elapsed

    # ------------------------------------------------------------------

    def _predict(
        self,
        model,
        X_test,
    ):

        start = time.perf_counter()

        predictions = model.predict(
            X_test,
        )

        elapsed = time.perf_counter() - start

        return predictions, elapsed

    # ------------------------------------------------------------------

    def _evaluate_metrics(
        self,
        y_true,
        y_pred,
    ):

        results = {}

        for name, metric in self.metrics.items():

            try:

                results[name] = float(

                    metric(

                        y_true,

                        y_pred,

                    )

                )

            except Exception as e:

                self.logger.exception(e)

                results[name] = np.nan

        return results

    ####################################################################
    # Single Benchmark
    ####################################################################

    def run_single(

        self,

        model,

        dataset,

    ):

        self.logger.info(

            "Running %s on %s",

            getattr(

                model,

                "name",

                model.__class__.__name__,

            ),

            getattr(

                dataset,

                "name",

                "dataset",

            ),

        )

        X_train = dataset.X_train

        X_test = dataset.X_test

        y_train = dataset.y_train

        y_test = dataset.y_test

        train_time = self._fit_model(

            model,

            X_train,

            y_train,

        )

        predictions, inference_time = self._predict(

            model,

            X_test,

        )

        metrics = self._evaluate_metrics(

            y_test,

            predictions,

        )

        metrics["train_time"] = train_time

        metrics["inference_time"] = inference_time

        self.add_result(

            model,

            dataset,

            metrics,

        )

        self.log_history(

            model=getattr(

                model,

                "name",

                model.__class__.__name__,

            ),

            dataset=getattr(

                dataset,

                "name",

                "dataset",

            ),

            metrics=metrics,

        )

        return metrics

    ####################################################################
    # Complete Benchmark Loop
    ####################################################################

    def run(

        self,

        continue_on_error=True,

    ):

        self.validate()

        self.start_timer()

        self.summary()

        total = (

            len(self.models)

            *

            len(self.datasets)

        )

        completed = 0

        self.logger.info(

            "Beginning benchmark (%d jobs)",

            total,

        )

        for dataset in self.datasets:

            for model in self.models:

                completed += 1

                self.logger.info(

                    "[%d/%d]",

                    completed,

                    total,

                )

                try:

                    self._execute_callbacks(

                        "before_run",

                        model=model,

                        dataset=dataset,

                    )

                    self.run_single(

                        model,

                        dataset,

                    )

                    self._execute_callbacks(

                        "after_run",

                        model=model,

                        dataset=dataset,

                    )

                except Exception as e:

                    self.logger.exception(e)

                    if not continue_on_error:

                        raise

        elapsed = self.stop_timer()

        self.logger.info(

            "Benchmark completed in %.3f seconds",

            elapsed,

        )

        return self.results_dataframe()


    ####################################################################
    # Cross Validation
    ####################################################################

    def _get_cv_splitter(self):

        from sklearn.model_selection import (
            KFold,
            RepeatedKFold,
            StratifiedKFold,
            GroupKFold,
            LeaveOneOut,
            TimeSeriesSplit,
        )

        strategy = getattr(self, "cv_strategy", "kfold").lower()

        folds = getattr(self, "cv_folds", 5)

        shuffle = getattr(self, "cv_shuffle", True)

        random_state = self.random_state

        if strategy == "kfold":

            return KFold(
                n_splits=folds,
                shuffle=shuffle,
                random_state=random_state,
            )

        if strategy == "repeatedkfold":

            return RepeatedKFold(
                n_splits=folds,
                n_repeats=5,
                random_state=random_state,
            )

        if strategy == "stratified":

            return StratifiedKFold(
                n_splits=folds,
                shuffle=shuffle,
                random_state=random_state,
            )

        if strategy == "group":

            return GroupKFold(
                n_splits=folds,
            )

        if strategy == "timeseries":

            return TimeSeriesSplit(
                n_splits=folds,
            )

        if strategy == "leaveoneout":

            return LeaveOneOut()

        raise ValueError(
            f"Unknown CV strategy: {strategy}"
        )

    ####################################################################
    # Cross Validation Execution
    ####################################################################

    def cross_validate(
        self,
        model,
        X,
        y,
        groups=None,
    ):

        splitter = self._get_cv_splitter()

        fold_results = []

        for fold, (train_idx, test_idx) in enumerate(

            splitter.split(

                X,

                y,

                groups,

            ),

            start=1,

        ):

            self.logger.info(

                "Fold %d",

                fold,

            )

            X_train = X[train_idx]

            X_test = X[test_idx]

            y_train = y[train_idx]

            y_test = y[test_idx]

            train_time = self._fit_model(

                model,

                X_train,

                y_train,

            )

            predictions, inference_time = self._predict(

                model,

                X_test,

            )

            metrics = self._evaluate_metrics(

                y_test,

                predictions,

            )

            metrics["train_time"] = train_time

            metrics["inference_time"] = inference_time

            metrics["fold"] = fold

            fold_results.append(

                metrics

            )

        return fold_results

    ####################################################################
    # Aggregate Fold Results
    ####################################################################

    def aggregate_cv_results(
        self,
        fold_results,
    ):

        import pandas as pd

        df = pd.DataFrame(

            fold_results

        )

        summary = {}

        for column in df.columns:

            if column == "fold":

                continue

            summary[column] = {

                "mean": float(df[column].mean()),

                "std": float(df[column].std()),

                "min": float(df[column].min()),

                "max": float(df[column].max()),

            }

        return summary


    ####################################################################
    # Resource Profiling
    ####################################################################

    def profile_system(self):

        import platform
        import psutil

        return {

            "cpu_count": psutil.cpu_count(),

            "logical_cpu_count": psutil.cpu_count(logical=True),

            "memory_gb": round(

                psutil.virtual_memory().total

                / 1024**3,

                2,

            ),

            "python_version": platform.python_version(),

            "platform": platform.platform(),

        }

    # ------------------------------------------------------------------

    def memory_usage_mb(self):

        import os
        import psutil

        process = psutil.Process(

            os.getpid()

        )

        return (

            process.memory_info().rss

            / 1024**2

        )

    # ------------------------------------------------------------------

    def model_size_mb(

        self,

        model,

    ):

        import pickle
        import tempfile
        import os

        with tempfile.NamedTemporaryFile(

            delete=False,

        ) as f:

            pickle.dump(

                model,

                f,

            )

            path = f.name

        size = (

            os.path.getsize(path)

            / 1024**2

        )

        os.remove(path)

        return size

    ####################################################################
    # Parallel Execution
    ####################################################################

    def run_parallel(

        self,

        n_jobs=-1,

    ):

        from joblib import Parallel
        from joblib import delayed

        jobs = []

        for dataset in self.datasets:

            for model in self.models:

                jobs.append(

                    delayed(

                        self.run_single

                    )(

                        model,

                        dataset,

                    )

                )

        return Parallel(

            n_jobs=n_jobs,

            backend="loky",

        )(jobs)

    ####################################################################
    # Timeout Wrapper
    ####################################################################

    def run_with_timeout(

        self,

        model,

        dataset,

        timeout=3600,

    ):

        import concurrent.futures

        with concurrent.futures.ThreadPoolExecutor(

            max_workers=1,

        ) as executor:

            future = executor.submit(

                self.run_single,

                model,

                dataset,

            )

            return future.result(

                timeout=timeout,

            )

    ####################################################################
    # Progress
    ####################################################################

    def progress_iterator(

        self,

        iterable,

    ):

        try:

            from tqdm import tqdm

            return tqdm(iterable)

        except ImportError:

            return iterable

    ####################################################################
    # Benchmark Metadata
    ####################################################################

    def benchmark_metadata(self):

        return {

            "runner": self.name,

            "random_seed": self.random_state,

            "models": self.number_of_models,

            "datasets": self.number_of_datasets,

            "metrics": self.number_of_metrics,

            "system": self.profile_system(),

        }


    ####################################################################
    # Experiment Tracking
    ####################################################################

    def attach_experiment(
        self,
        experiment,
    ):

        """
        Attach an Experiment object.
        """

        self.experiment = experiment

        self.logger.info(
            "Experiment attached."
        )

    ####################################################################
    # Leaderboard
    ####################################################################

    def attach_leaderboard(
        self,
        leaderboard,
    ):

        self.leaderboard = leaderboard

        self.logger.info(
            "Leaderboard attached."
        )

    ####################################################################
    # Report Generator
    ####################################################################

    def attach_report(
        self,
        report,
    ):

        self.report = report

        self.logger.info(
            "Report generator attached."
        )

    ####################################################################
    # Statistical Analysis
    ####################################################################

    def statistical_summary(self):

        try:

            from .statistical_analysis.descriptive_statistics import (
                DescriptiveStatistics,
            )

        except Exception:

            self.logger.warning(
                "Statistical package unavailable."
            )

            return {}

        df = self.results_dataframe()

        statistics = {}

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            values = df[column].dropna().values

            if len(values) == 0:

                continue

            statistics[column] = (

                DescriptiveStatistics.summary(
                    values
                )

            )

        self.statistics = statistics

        return statistics

    ####################################################################
    # Leaderboard Update
    ####################################################################

    def update_leaderboard(

        self,

        primary_metric,

    ):

        if not hasattr(

            self,

            "leaderboard",

        ):

            return

        for result in self.results:

            metrics = result.copy()

            model = metrics.pop("model")

            dataset = metrics.pop("dataset")

            self.leaderboard.add_result(

                model=model,

                dataset=dataset,

                metrics=metrics,

            )

        return self.leaderboard.average_rank(

            primary_metric

        )

    ####################################################################
    # Report Generation
    ####################################################################

    def generate_report(

        self,

        title="CircuitBench Benchmark",

    ):

        if not hasattr(

            self,

            "report",

        ):

            return

        self.report.set_metadata(

            benchmark=self.name,

            random_seed=self.random_state,

        )

        self.report.add_section(

            "Overview",

            "Automatically generated benchmark report.",

        )

        self.report.add_table(

            "Results",

            self.results_dataframe(),

        )

        self.report.add_statistics(

            "Summary",

            self.statistical_summary(),

        )

        self.report.export_json()

        self.report.export_markdown()

        self.report.export_csv()

        self.logger.info(

            "Benchmark report generated."

        )

    ####################################################################
    # Finalize
    ####################################################################

    def finalize(

        self,

        primary_metric=None,

    ):

        if hasattr(

            self,

            "experiment",

        ):

            for result in self.results:

                self.experiment.add_result(

                    result

                )

            self.experiment.save()

        if (

            primary_metric is not None

            and

            hasattr(

                self,

                "leaderboard",

            )

        ):

            self.update_leaderboard(

                primary_metric

            )

        if hasattr(

            self,

            "report",

        ):

            self.generate_report()

        self.logger.info(

            "Benchmark finalized."

        )


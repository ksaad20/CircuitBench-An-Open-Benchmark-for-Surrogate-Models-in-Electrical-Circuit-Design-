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


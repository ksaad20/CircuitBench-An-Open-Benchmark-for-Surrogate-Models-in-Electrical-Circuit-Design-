"""
CircuitBench Benchmark Runner
=============================

Core benchmark execution engine.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass
from time import perf_counter

import numpy as np


@dataclass
class BenchmarkResult:

    model_name: str

    fit_time: float

    predict_time: float

    metrics: dict


class BenchmarkRunner:

    """
    Core benchmarking engine.
    """

    def __init__(

        self,

        metrics,

    ):

        self.metrics = metrics


    def evaluate(

        self,

        model,

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        start = perf_counter()

        model.fit(

            X_train,

            y_train,

        )

        fit_time = perf_counter() - start


        start = perf_counter()

        predictions = model.predict(

            X_test,

        )

        predict_time = perf_counter() - start


        results = {}

        for name, metric in self.metrics.items():

            try:

                results[name] = metric(

                    y_test,

                    predictions,

                )

            except Exception:

                results[name] = np.nan


        return BenchmarkResult(

            model_name=model.__class__.__name__,

            fit_time=float(fit_time),

            predict_time=float(predict_time),

            metrics=results,

        )


    def evaluate_many(

        self,

        models,

        X_train,

        y_train,

        X_test,

        y_test,

    ):

        output = []

        for model in models:

            output.append(

                self.evaluate(

                    model,

                    X_train,

                    y_train,

                    X_test,

                    y_test,

                )

            )

        return output


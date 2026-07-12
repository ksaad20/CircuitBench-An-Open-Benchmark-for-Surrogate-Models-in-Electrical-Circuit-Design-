"""
CircuitBench Benchmark Suite
============================

High-level orchestration for benchmarking multiple models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

import pandas as pd

from .advanced_runner import AdvancedBenchmarkRunner


@dataclass
class BenchmarkSuiteResult:
    dataset_name: str
    leaderboard: pd.DataFrame
    raw_results: list = field(default_factory=list)


class BenchmarkSuite:

    def __init__(
        self,
        metrics: dict,
    ):
        self.runner = AdvancedBenchmarkRunner(metrics)

    def run(
        self,
        models: Sequence,
        X_train,
        y_train,
        X_test,
        y_test,
        dataset_name="Dataset",
    ):

        results = []

        for model in models:

            results.append(

                self.runner.evaluate(

                    model,

                    X_train,

                    y_train,

                    X_test,

                    y_test,

                )

            )

        leaderboard = self.runner.results_dataframe(
            results
        )

        return BenchmarkSuiteResult(

            dataset_name=dataset_name,

            leaderboard=leaderboard,

            raw_results=results,

        )

    @staticmethod
    def rank(
        leaderboard,
        metric,
        ascending=False,
    ):

        return (

            leaderboard

            .sort_values(

                metric,

                ascending=ascending,

            )

            .reset_index(

                drop=True,

            )

        )

    @staticmethod
    def summarize(
        suite_result,
    ):

        df = suite_result.leaderboard

        summary = {

            "Dataset":

                suite_result.dataset_name,

            "Models":

                len(df),

            "Columns":

                list(df.columns),

        }

        if "FitTime" in df.columns:

            summary["AverageFitTime"] = float(

                df["FitTime"].mean()

            )

        if "PredictTime" in df.columns:

            summary["AveragePredictTime"] = float(

                df["PredictTime"].mean()

            )

        return summary

    @staticmethod
    def save(
        suite_result,
        output_csv,
    ):

        suite_result.leaderboard.to_csv(

            output_csv,

            index=False,

        )


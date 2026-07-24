"""
CircuitBench Experiment Manager
===============================

Manage benchmark experiments and generate leaderboards.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime

import pandas as pd


@dataclass
class Experiment:
    name: str

    created: str = field(default_factory=lambda: datetime.now().isoformat())

    results: list = field(default_factory=list)


class ExperimentManager:
    def __init__(self):

        self.experiments = []

    def create_experiment(
        self,
        name,
    ):

        experiment = Experiment(name=name)

        self.experiments.append(experiment)

        return experiment

    @staticmethod
    def add_result(
        experiment,
        result,
    ):

        experiment.results.append(result)

    @staticmethod
    def leaderboard(
        experiment,
        metric,
        ascending=False,
    ):

        rows = []

        for result in experiment.results:
            row = {
                "Model": result.model_name,
                "FitTime": result.fit_time,
                "PredictTime": result.predict_time,
            }

            if hasattr(
                result,
                "memory_mb",
            ):
                row["MemoryMB"] = result.memory_mb

            row.update(result.metrics)

            rows.append(row)

        df = pd.DataFrame(rows)

        if metric in df.columns:
            df = df.sort_values(
                metric,
                ascending=ascending,
            ).reset_index(
                drop=True,
            )

        return df

    @staticmethod
    def export_csv(
        leaderboard,
        filename,
    ):

        leaderboard.to_csv(
            filename,
            index=False,
        )

    @staticmethod
    def export_json(
        leaderboard,
        filename,
    ):

        leaderboard.to_json(
            filename,
            orient="records",
            indent=4,
        )

    @staticmethod
    def metadata(
        experiment,
    ):

        return {
            "name": experiment.name,
            "created": experiment.created,
            "models": len(experiment.results),
        }

    @staticmethod
    def save_metadata(
        experiment,
        filename,
    ):

        with open(
            filename,
            "w",
        ) as f:
            json.dump(
                ExperimentManager.metadata(experiment),
                f,
                indent=4,
            )

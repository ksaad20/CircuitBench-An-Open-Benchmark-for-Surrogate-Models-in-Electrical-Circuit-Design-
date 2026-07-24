"""
CircuitBench Leaderboard
========================

Automatic ranking and leaderboard generation.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
import pandas as pd


class Leaderboard:
    """
    Benchmark leaderboard manager.
    """

    def __init__(self):

        self._results = []

    # ----------------------------------------------------------

    def add_result(
        self,
        model: str,
        dataset: str,
        metrics: dict,
    ):

        record = {
            "model": model,
            "dataset": dataset,
        }

        record.update(metrics)

        self._results.append(record)

    # ----------------------------------------------------------

    def dataframe(self):

        return pd.DataFrame(self._results)

    # ----------------------------------------------------------

    def rank(
        self,
        metric: str,
        ascending: bool = False,
    ):

        df = self.dataframe()

        df = df.sort_values(
            metric,
            ascending=ascending,
        )

        df["Rank"] = np.arange(
            1,
            len(df) + 1,
        )

        return df

    # ----------------------------------------------------------

    def average_metric(
        self,
        metric: str,
    ):

        df = self.dataframe()

        return df.groupby("model")[metric].mean().sort_values(ascending=False)

    # ----------------------------------------------------------

    def average_rank(
        self,
        metric: str,
    ):

        df = self.dataframe()

        df["rank"] = df.groupby("dataset")[metric].rank(
            ascending=False,
            method="average",
        )

        return df.groupby("model")["rank"].mean().sort_values()

    # ----------------------------------------------------------

    def top_models(
        self,
        metric: str,
        n: int = 10,
    ):

        return self.average_metric(metric).head(n)

    # ----------------------------------------------------------

    def export_csv(
        self,
        filename="leaderboard.csv",
    ):

        self.dataframe().to_csv(
            filename,
            index=False,
        )

    # ----------------------------------------------------------

    def export_markdown(
        self,
        filename="leaderboard.md",
    ):

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as f:
            f.write("# CircuitBench Leaderboard\n\n")

            f.write(self.dataframe().to_markdown(index=False))

    # ----------------------------------------------------------

    def summary(self):

        df = self.dataframe()

        return {
            "results": len(df),
            "datasets": df.dataset.nunique() if not df.empty else 0,
            "models": df.model.nunique() if not df.empty else 0,
        }

    # ----------------------------------------------------------

    def clear(self):

        self._results.clear()


__all__ = [
    "Leaderboard",
]

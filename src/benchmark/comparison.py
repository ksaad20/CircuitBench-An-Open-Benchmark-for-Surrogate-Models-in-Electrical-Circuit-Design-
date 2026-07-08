"""
comparison.py
=============

Model comparison utilities for CircuitBench.

Author: Asif Kazi
License: MIT
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class Comparison:
    """
    Compare surrogate models across benchmark metrics.
    """

    def __init__(self):
        self.results = pd.DataFrame()

    def add_result(self,
                   model: str,
                   metrics: dict) -> None:
        """
        Add evaluation metrics for one model.

        Parameters
        ----------
        model : str
            Model name.

        metrics : dict
            Dictionary of benchmark metrics.
        """

        row = {"Model": model}

        row.update(metrics)

        self.results = pd.concat(
            [
                self.results,
                pd.DataFrame([row])
            ],
            ignore_index=True
        )

    def dataframe(self) -> pd.DataFrame:
        """
        Return comparison dataframe.
        """

        return self.results.copy()

    def sort(self,
             metric="Score",
             ascending=False) -> pd.DataFrame:
        """
        Sort models by any metric.
        """

        return self.results.sort_values(
            metric,
            ascending=ascending
        ).reset_index(drop=True)

    def rank(self,
             metric="Score",
             ascending=False):

        df = self.sort(metric, ascending)

        df.insert(
            0,
            "Rank",
            np.arange(1, len(df)+1)
        )

        return df

    def winner(self,
               metric="Score",
               ascending=False):
        """
        Return best performing model.
        """

        return self.rank(
            metric,
            ascending
        ).iloc[0]

    def summary(self):
        """
        Statistical summary.
        """

        return self.results.describe()

    def pairwise_difference(self,
                            model1,
                            model2):
        """
        Difference between two models.
        """

        m1 = self.results[
            self.results.Model == model1
        ].iloc[0]

        m2 = self.results[
            self.results.Model == model2
        ].iloc[0]

        diff = {}

        for col in self.results.columns:

            if col == "Model":
                continue

            diff[col] = m1[col] - m2[col]

        return pd.Series(diff)

    def remove(self,
               model):
        """
        Remove a model.
        """

        self.results = self.results[
            self.results.Model != model
        ].reset_index(drop=True)

    def clear(self):
        """
        Clear all results.
        """

        self.results = pd.DataFrame()

    def save_csv(self,
                 filename):
        """
        Save comparison table.
        """

        self.results.to_csv(
            filename,
            index=False
        )

    def save_excel(self,
                   filename):
        """
        Save comparison table.
        """

        self.results.to_excel(
            filename,
            index=False
        )

    def __len__(self):
        return len(self.results)

    def __repr__(self):
        return (
            f"Comparison("
            f"{len(self.results)} models)"
        )

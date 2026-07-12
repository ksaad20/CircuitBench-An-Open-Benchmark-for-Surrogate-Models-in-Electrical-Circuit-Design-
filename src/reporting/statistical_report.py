"""
CircuitBench Statistical Report
===============================

Automatic statistical summaries for benchmark results.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import pandas as pd
import numpy as np


class StatisticalReport:

    @staticmethod
    def summary(
        leaderboard,
    ):
        """
        Summary statistics.
        """

        numeric = leaderboard.select_dtypes(
            include=np.number
        )

        return numeric.describe().T


    @staticmethod
    def ranking(
        leaderboard,
        metric,
        ascending=False,
    ):
        """
        Rank models.
        """

        df = leaderboard.sort_values(
            metric,
            ascending=ascending,
        ).reset_index(drop=True)

        df.insert(
            0,
            "Rank",
            np.arange(
                1,
                len(df) + 1,
            ),
        )

        return df


    @staticmethod
    def top_models(
        leaderboard,
        metric,
        top_n=5,
        ascending=False,
    ):
        """
        Return top models.
        """

        return (

            leaderboard

            .sort_values(
                metric,
                ascending=ascending,
            )

            .head(top_n)

            .reset_index(drop=True)

        )


    @staticmethod
    def metric_summary(
        leaderboard,
    ):
        """
        Mean, std, min and max for all metrics.
        """

        numeric = leaderboard.select_dtypes(
            include=np.number
        )

        rows = []

        for column in numeric.columns:

            rows.append(

                {

                    "Metric": column,

                    "Mean": numeric[column].mean(),

                    "Std": numeric[column].std(),

                    "Minimum": numeric[column].min(),

                    "Maximum": numeric[column].max(),

                }

            )

        return pd.DataFrame(
            rows
        )


    @staticmethod
    def save_summary(
        leaderboard,
        filename,
    ):

        StatisticalReport.summary(

            leaderboard

        ).to_csv(

            filename,

            index=True,

        )


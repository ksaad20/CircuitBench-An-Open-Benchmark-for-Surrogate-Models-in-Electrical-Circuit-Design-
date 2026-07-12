"""
CircuitBench Critical Difference Analysis
=========================================

Critical Difference analysis for comparing multiple machine learning
models across multiple datasets.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Dict

import numpy as np

from scipy.stats import rankdata, friedmanchisquare
from scipy.stats import studentized_range


class CriticalDifference:

    """
    Friedman + Nemenyi Critical Difference analysis.
    """

    @staticmethod
    def average_ranks(scores):

        scores = np.asarray(scores)

        n_datasets, n_models = scores.shape

        ranks = np.zeros_like(
            scores,
            dtype=float,
        )

        for i in range(n_datasets):

            ranks[i] = rankdata(
                -scores[i],
                method="average",
            )

        return np.mean(
            ranks,
            axis=0,
        )

    # -----------------------------------------------------

    @staticmethod
    def friedman(scores):

        scores = np.asarray(scores)

        groups = [

            scores[:, i]

            for i in range(scores.shape[1])

        ]

        statistic, p = friedmanchisquare(
            *groups
        )

        return {

            "statistic": float(statistic),

            "p_value": float(p),

            "significant": bool(
                p < 0.05
            ),

        }

    # -----------------------------------------------------

    @staticmethod
    def critical_difference(
        n_models,
        n_datasets,
        alpha=0.05,
    ):

        q = studentized_range.ppf(
            1 - alpha,
            n_models,
            np.inf,
        ) / np.sqrt(2)

        cd = (

            q

            * np.sqrt(

                n_models
                * (n_models + 1)

                / (6 * n_datasets)

            )

        )

        return float(cd)

    # -----------------------------------------------------

    @staticmethod
    def compare(scores):

        scores = np.asarray(scores)

        avg_ranks = CriticalDifference.average_ranks(
            scores
        )

        cd = CriticalDifference.critical_difference(

            scores.shape[1],

            scores.shape[0],

        )

        return {

            "average_ranks": avg_ranks,

            "critical_difference": cd,

            "friedman":

                CriticalDifference.friedman(

                    scores

                ),

        }

    # -----------------------------------------------------

    @staticmethod
    def significant_pairs(
        average_ranks,
        cd,
    ):

        average_ranks = np.asarray(
            average_ranks
        )

        significant = []

        n = len(
            average_ranks
        )

        for i in range(n):

            for j in range(i + 1, n):

                diff = abs(

                    average_ranks[i]

                    - average_ranks[j]

                )

                if diff > cd:

                    significant.append(

                        (

                            i,

                            j,

                            diff,

                        )

                    )

        return significant

    # -----------------------------------------------------

    @classmethod
    def summary(
        cls,
        scores,
    ) -> Dict:

        results = cls.compare(
            scores
        )

        results[
            "significant_pairs"
        ] = cls.significant_pairs(

            results[
                "average_ranks"
            ],

            results[
                "critical_difference"
            ],

        )

        return results


__all__ = [
    "CriticalDifference",
]


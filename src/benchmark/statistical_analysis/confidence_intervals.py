"""
CircuitBench Confidence Intervals
=================================

Confidence interval estimation utilities.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from scipy import stats


class ConfidenceIntervals:
    """
    Confidence interval calculations.
    """

    @staticmethod
    def mean_confidence_interval(
        x,
        confidence: float = 0.95,
    ) -> tuple[float, float]:

        x = np.asarray(x, dtype=float)

        n = len(x)

        mean = np.mean(x)

        sem = stats.sem(x)

        margin = sem * stats.t.ppf(
            (1 + confidence) / 2.0,
            n - 1,
        )

        return (
            float(mean - margin),
            float(mean + margin),
        )

    # ------------------------------------------------------

    @staticmethod
    def prediction_interval(
        x,
        confidence: float = 0.95,
    ) -> tuple[float, float]:

        x = np.asarray(x, dtype=float)

        mean = np.mean(x)

        std = np.std(
            x,
            ddof=1,
        )

        n = len(x)

        t = stats.t.ppf(
            (1 + confidence) / 2,
            n - 1,
        )

        margin = t * std * np.sqrt(1 + 1 / n)

        return (
            float(mean - margin),
            float(mean + margin),
        )

    # ------------------------------------------------------

    @staticmethod
    def proportion_confidence_interval(
        successes: int,
        trials: int,
        confidence: float = 0.95,
    ):

        p = successes / trials

        z = stats.norm.ppf((1 + confidence) / 2)

        margin = z * np.sqrt(p * (1 - p) / trials)

        return (
            max(0.0, p - margin),
            min(1.0, p + margin),
        )

    # ------------------------------------------------------

    @staticmethod
    def variance_confidence_interval(
        x,
        confidence: float = 0.95,
    ):

        x = np.asarray(x)

        n = len(x)

        variance = np.var(
            x,
            ddof=1,
        )

        alpha = 1 - confidence

        lower = (
            (n - 1)
            * variance
            / stats.chi2.ppf(
                1 - alpha / 2,
                n - 1,
            )
        )

        upper = (
            (n - 1)
            * variance
            / stats.chi2.ppf(
                alpha / 2,
                n - 1,
            )
        )

        return (
            float(lower),
            float(upper),
        )

    # ------------------------------------------------------

    @staticmethod
    def median_confidence_interval(
        x,
        confidence: float = 0.95,
    ):

        x = np.sort(np.asarray(x))

        n = len(x)

        alpha = 1 - confidence

        z = stats.norm.ppf(1 - alpha / 2)

        k = int(np.floor((n / 2) - z * np.sqrt(n) / 2))

        lower = int(np.ceil((n / 2) + z * np.sqrt(n) / 2))

        k = max(
            0,
            k,
        )

        lower = min(
            n - 1,
            lower,
        )

        return (
            float(x[k]),
            float(x[lower]),
        )

    # ------------------------------------------------------

    @classmethod
    def summary(
        cls,
        x,
        confidence: float = 0.95,
    ) -> dict:

        return {
            "mean_ci": cls.mean_confidence_interval(
                x,
                confidence,
            ),
            "prediction_interval": cls.prediction_interval(
                x,
                confidence,
            ),
            "variance_ci": cls.variance_confidence_interval(
                x,
                confidence,
            ),
            "median_ci": cls.median_confidence_interval(
                x,
                confidence,
            ),
        }


__all__ = [
    "ConfidenceIntervals",
]

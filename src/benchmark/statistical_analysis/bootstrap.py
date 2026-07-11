"""
CircuitBench Bootstrap Statistics
=================================

Bootstrap resampling utilities.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Callable, Dict, Tuple

import numpy as np


class Bootstrap:
    """
    Bootstrap statistical analysis.
    """

    @staticmethod
    def resample(
        x,
        n_bootstrap: int = 1000,
        random_state: int = 42,
    ):

        rng = np.random.default_rng(random_state)

        x = np.asarray(x)

        n = len(x)

        samples = np.empty(
            (n_bootstrap, n),
            dtype=x.dtype,
        )

        for i in range(n_bootstrap):

            index = rng.integers(
                0,
                n,
                size=n,
            )

            samples[i] = x[index]

        return samples

    # ---------------------------------------------------------

    @staticmethod
    def statistic_distribution(
        x,
        statistic: Callable = np.mean,
        n_bootstrap: int = 1000,
        random_state: int = 42,
    ):

        samples = Bootstrap.resample(
            x,
            n_bootstrap,
            random_state,
        )

        values = np.asarray(
            [
                statistic(sample)
                for sample in samples
            ],
            dtype=float,
        )

        return values

    # ---------------------------------------------------------

    @staticmethod
    def confidence_interval(
        x,
        statistic: Callable = np.mean,
        confidence: float = 0.95,
        n_bootstrap: int = 1000,
        random_state: int = 42,
    ) -> Tuple[float, float]:

        values = Bootstrap.statistic_distribution(
            x,
            statistic,
            n_bootstrap,
            random_state,
        )

        alpha = 1.0 - confidence

        lower = np.percentile(
            values,
            alpha / 2 * 100,
        )

        upper = np.percentile(
            values,
            (1 - alpha / 2) * 100,
        )

        return (
            float(lower),
            float(upper),
        )

    # ---------------------------------------------------------

    @staticmethod
    def standard_error(
        x,
        statistic: Callable = np.mean,
        n_bootstrap: int = 1000,
        random_state: int = 42,
    ):

        values = Bootstrap.statistic_distribution(
            x,
            statistic,
            n_bootstrap,
            random_state,
        )

        return float(
            np.std(
                values,
                ddof=1,
            )
        )

    # ---------------------------------------------------------

    @staticmethod
    def bias(
        x,
        statistic: Callable = np.mean,
        n_bootstrap: int = 1000,
        random_state: int = 42,
    ):

        original = statistic(x)

        values = Bootstrap.statistic_distribution(
            x,
            statistic,
            n_bootstrap,
            random_state,
        )

        return float(
            np.mean(values) - original
        )

    # ---------------------------------------------------------

    @classmethod
    def summary(
        cls,
        x,
        statistic: Callable = np.mean,
        n_bootstrap: int = 1000,
        confidence: float = 0.95,
    ) -> Dict:

        return {

            "estimate": float(statistic(x)),

            "bootstrap_standard_error":
                cls.standard_error(
                    x,
                    statistic,
                    n_bootstrap,
                ),

            "bootstrap_bias":
                cls.bias(
                    x,
                    statistic,
                    n_bootstrap,
                ),

            "confidence_interval":
                cls.confidence_interval(
                    x,
                    statistic,
                    confidence,
                    n_bootstrap,
                ),

        }


__all__ = [
    "Bootstrap",
]

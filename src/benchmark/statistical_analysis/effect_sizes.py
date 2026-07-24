"""
CircuitBench Effect Sizes
=========================

Computation of common effect size statistics for benchmark comparison.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np


class EffectSizes:
    """
    Collection of effect size calculations.
    """

    @staticmethod
    def cohens_d(x, y) -> float:

        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)

        nx = len(x)
        ny = len(y)

        dof = nx + ny - 2

        pooled_std = np.sqrt(
            (((nx - 1) * np.var(x, ddof=1)) + ((ny - 1) * np.var(y, ddof=1))) / dof
        )

        return float((np.mean(x) - np.mean(y)) / pooled_std)

    # -----------------------------------------------------

    @staticmethod
    def hedges_g(x, y) -> float:

        d = EffectSizes.cohens_d(x, y)

        n = len(x) + len(y)

        correction = 1 - (3 / (4 * n - 9))

        return float(d * correction)

    # -----------------------------------------------------

    @staticmethod
    def glass_delta(x, y) -> float:

        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)

        return float((np.mean(x) - np.mean(y)) / np.std(y, ddof=1))

    # -----------------------------------------------------

    @staticmethod
    def cliffs_delta(x, y) -> float:

        x = np.asarray(x)
        y = np.asarray(y)

        greater = 0
        lower = 0

        for xi in x:
            greater += np.sum(xi > y)
            lower += np.sum(xi < y)

        delta = (greater - lower) / (len(x) * len(y))

        return float(delta)

    # -----------------------------------------------------

    @staticmethod
    def rank_biserial(x, y) -> float:

        x = np.asarray(x)
        y = np.asarray(y)

        greater = 0
        lower = 0

        for xi in x:
            greater += np.sum(xi > y)
            lower += np.sum(xi < y)

        return float((greater - lower) / (greater + lower))

    # -----------------------------------------------------

    @staticmethod
    def common_language_effect_size(x, y):

        x = np.asarray(x)
        y = np.asarray(y)

        wins = 0

        for xi in x:
            wins += np.sum(xi > y)

        return float(wins / (len(x) * len(y)))

    # -----------------------------------------------------

    @staticmethod
    def interpret_cohens_d(d: float):

        d = abs(d)

        if d < 0.2:
            return "negligible"

        if d < 0.5:
            return "small"

        if d < 0.8:
            return "medium"

        return "large"

    # -----------------------------------------------------

    @classmethod
    def summary(cls, x, y) -> dict:

        d = cls.cohens_d(x, y)

        return {
            "cohens_d": d,
            "hedges_g": cls.hedges_g(x, y),
            "glass_delta": cls.glass_delta(x, y),
            "cliffs_delta": cls.cliffs_delta(x, y),
            "rank_biserial": cls.rank_biserial(x, y),
            "common_language": cls.common_language_effect_size(x, y),
            "interpretation": cls.interpret_cohens_d(d),
        }


__all__ = [
    "EffectSizes",
]

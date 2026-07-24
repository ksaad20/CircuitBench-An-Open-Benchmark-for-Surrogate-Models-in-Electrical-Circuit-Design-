"""
CircuitBench Hypothesis Testing
===============================

Statistical hypothesis testing utilities for benchmark comparison.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from scipy.stats import (
    friedmanchisquare,
    levene,
    mannwhitneyu,
    normaltest,
    shapiro,
    ttest_ind,
    ttest_rel,
    wilcoxon,
)


class HypothesisTesting:
    """
    Statistical hypothesis testing methods.
    """

    @staticmethod
    def paired_t_test(x, y) -> dict:

        statistic, p = ttest_rel(x, y)

        return {
            "test": "paired_t_test",
            "statistic": float(statistic),
            "p_value": float(p),
            "significant": bool(p < 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def independent_t_test(x, y) -> dict:

        statistic, p = ttest_ind(
            x,
            y,
            equal_var=False,
        )

        return {
            "test": "independent_t_test",
            "statistic": float(statistic),
            "p_value": float(p),
            "significant": bool(p < 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def wilcoxon_signed_rank(x, y) -> dict:

        statistic, p = wilcoxon(x, y)

        return {
            "test": "wilcoxon_signed_rank",
            "statistic": float(statistic),
            "p_value": float(p),
            "significant": bool(p < 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def mann_whitney(x, y) -> dict:

        statistic, p = mannwhitneyu(
            x,
            y,
            alternative="two-sided",
        )

        return {
            "test": "mann_whitney",
            "statistic": float(statistic),
            "p_value": float(p),
            "significant": bool(p < 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def friedman(*groups) -> dict:

        statistic, p = friedmanchisquare(*groups)

        return {
            "test": "friedman",
            "statistic": float(statistic),
            "p_value": float(p),
            "significant": bool(p < 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def shapiro_test(x) -> dict:

        statistic, p = shapiro(x)

        return {
            "test": "shapiro",
            "statistic": float(statistic),
            "p_value": float(p),
            "normal": bool(p >= 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def normality_test(x) -> dict:

        statistic, p = normaltest(x)

        return {
            "test": "dagostino",
            "statistic": float(statistic),
            "p_value": float(p),
            "normal": bool(p >= 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def levene_test(*groups) -> dict:

        statistic, p = levene(*groups)

        return {
            "test": "levene",
            "statistic": float(statistic),
            "p_value": float(p),
            "equal_variance": bool(p >= 0.05),
        }

    # ----------------------------------------------------

    @staticmethod
    def recommend_test(x, y):

        x = np.asarray(x)
        y = np.asarray(y)

        normal_x = shapiro(x).pvalue >= 0.05
        normal_y = shapiro(y).pvalue >= 0.05

        if normal_x and normal_y:
            return "paired_t_test"

        return "wilcoxon_signed_rank"


__all__ = [
    "HypothesisTesting",
]

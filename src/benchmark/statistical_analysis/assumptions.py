"""
CircuitBench Statistical Assumption Tests
=========================================

Automatic assumption checking for statistical analyses.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from scipy.stats import (
    anderson,
    bartlett,
    fligner,
    jarque_bera,
    kurtosis,
    levene,
    normaltest,
    shapiro,
    skew,
)


class Assumptions:
    """
    Statistical assumption checking utilities.
    """

    # -----------------------------------------------------

    @staticmethod
    def shapiro_test(x):

        statistic, p = shapiro(x)

        return {
            "test": "Shapiro-Wilk",
            "statistic": float(statistic),
            "p_value": float(p),
            "normal": bool(p >= 0.05),
        }

    # -----------------------------------------------------

    @staticmethod
    def dagostino_test(x):

        statistic, p = normaltest(x)

        return {
            "test": "D'Agostino K²",
            "statistic": float(statistic),
            "p_value": float(p),
            "normal": bool(p >= 0.05),
        }

    # -----------------------------------------------------

    @staticmethod
    def jarque_bera_test(x):

        statistic, p = jarque_bera(x)

        return {
            "test": "Jarque-Bera",
            "statistic": float(statistic),
            "p_value": float(p),
            "normal": bool(p >= 0.05),
        }

    # -----------------------------------------------------

    @staticmethod
    def anderson_test(x):

        result = anderson(x)

        return {
            "test": "Anderson-Darling",
            "statistic": float(result.statistic),
            "critical_values": result.critical_values.tolist(),
            "significance_levels": result.significance_level.tolist(),
        }

    # -----------------------------------------------------

    @staticmethod
    def levene_test(*groups):

        statistic, p = levene(*groups)

        return {
            "test": "Levene",
            "statistic": float(statistic),
            "p_value": float(p),
            "equal_variance": bool(p >= 0.05),
        }

    # -----------------------------------------------------

    @staticmethod
    def bartlett_test(*groups):

        statistic, p = bartlett(*groups)

        return {
            "test": "Bartlett",
            "statistic": float(statistic),
            "p_value": float(p),
            "equal_variance": bool(p >= 0.05),
        }

    # -----------------------------------------------------

    @staticmethod
    def fligner_test(*groups):

        statistic, p = fligner(*groups)

        return {
            "test": "Fligner-Killeen",
            "statistic": float(statistic),
            "p_value": float(p),
            "equal_variance": bool(p >= 0.05),
        }

    # -----------------------------------------------------

    @staticmethod
    def skewness(x):

        return float(skew(x))

    # -----------------------------------------------------

    @staticmethod
    def kurtosis(x):

        return float(kurtosis(x))

    # -----------------------------------------------------

    @classmethod
    def report(cls, x, *groups) -> dict:

        report = {
            "sample_size": len(x),
            "shapiro": cls.shapiro_test(x),
            "dagostino": cls.dagostino_test(x),
            "jarque_bera": cls.jarque_bera_test(x),
            "anderson": cls.anderson_test(x),
            "skewness": cls.skewness(x),
            "kurtosis": cls.kurtosis(x),
        }

        if len(groups) >= 2:
            report["levene"] = cls.levene_test(*groups)

            report["bartlett"] = cls.bartlett_test(*groups)

            report["fligner"] = cls.fligner_test(*groups)

        return report


__all__ = [
    "Assumptions",
]

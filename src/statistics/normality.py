"""
Normality tests.
"""

from scipy.stats import shapiro

from scipy.stats import normaltest


class NormalityTest:

    @staticmethod
    def shapiro(values):

        statistic, p = shapiro(values)

        return {

            "test": "Shapiro-Wilk",

            "statistic": statistic,

            "p_value": p,

            "normal": p > 0.05

        }

    @staticmethod
    def dagostino(values):

        statistic, p = normaltest(values)

        return {

            "test": "D'Agostino",

            "statistic": statistic,

            "p_value": p,

            "normal": p > 0.05

        }

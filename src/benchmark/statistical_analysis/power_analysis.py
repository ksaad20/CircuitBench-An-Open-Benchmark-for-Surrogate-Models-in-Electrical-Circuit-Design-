"""
CircuitBench Statistical Power Analysis
=======================================

Power analysis utilities for benchmark experiments.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from statsmodels.stats.power import (
    FTestAnovaPower,
    TTestIndPower,
    TTestPower,
)


class PowerAnalysis:
    """
    Statistical power analysis utilities.
    """

    @staticmethod
    def paired_ttest_power(
        effect_size: float,
        n_samples: int,
        alpha: float = 0.05,
    ) -> float:

        analysis = TTestPower()

        return float(
            analysis.power(
                effect_size=effect_size,
                nobs=n_samples,
                alpha=alpha,
            )
        )

    # ------------------------------------------------------

    @staticmethod
    def independent_ttest_power(
        effect_size: float,
        n_samples: int,
        alpha: float = 0.05,
    ) -> float:

        analysis = TTestIndPower()

        return float(
            analysis.power(
                effect_size=effect_size,
                nobs1=n_samples,
                alpha=alpha,
            )
        )

    # ------------------------------------------------------

    @staticmethod
    def required_sample_size(
        effect_size: float,
        power: float = 0.80,
        alpha: float = 0.05,
    ) -> float:

        analysis = TTestIndPower()

        return float(
            analysis.solve_power(
                effect_size=effect_size,
                power=power,
                alpha=alpha,
            )
        )

    # ------------------------------------------------------

    @staticmethod
    def anova_power(
        effect_size: float,
        n_groups: int,
        n_samples: int,
        alpha: float = 0.05,
    ) -> float:

        analysis = FTestAnovaPower()

        return float(
            analysis.power(
                effect_size=effect_size,
                nobs=n_samples,
                alpha=alpha,
                k_groups=n_groups,
            )
        )

    # ------------------------------------------------------

    @staticmethod
    def detectable_effect_size(
        n_samples: int,
        power: float = 0.80,
        alpha: float = 0.05,
    ) -> float:

        analysis = TTestIndPower()

        return float(
            analysis.solve_power(
                nobs1=n_samples,
                power=power,
                alpha=alpha,
            )
        )

    # ------------------------------------------------------

    @classmethod
    def summary(
        cls,
        effect_size: float,
        n_samples: int,
        alpha: float = 0.05,
    ) -> dict:

        return {
            "paired_ttest_power": cls.paired_ttest_power(
                effect_size,
                n_samples,
                alpha,
            ),
            "independent_ttest_power": cls.independent_ttest_power(
                effect_size,
                n_samples,
                alpha,
            ),
            "required_sample_size_80_power": cls.required_sample_size(
                effect_size,
                power=0.80,
                alpha=alpha,
            ),
            "required_sample_size_90_power": cls.required_sample_size(
                effect_size,
                power=0.90,
                alpha=alpha,
            ),
        }


__all__ = [
    "PowerAnalysis",
]

"""
CircuitBench Bayesian Statistics
================================

Bayesian statistical analysis utilities.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Dict

import numpy as np

from scipy.stats import t


class BayesianStatistics:
    """
    Bayesian statistical utilities.
    """

    # -------------------------------------------------------------

    @staticmethod
    def posterior_mean(
        data,
        prior_mean=0.0,
        prior_variance=1.0,
    ):

        data = np.asarray(data, dtype=float)

        n = len(data)

        sample_mean = np.mean(data)

        sample_variance = np.var(
            data,
            ddof=1,
        )

        posterior_variance = 1.0 / ((1.0 / prior_variance) + (n / sample_variance))

        posterior_mean = posterior_variance * (
            (prior_mean / prior_variance) + (n * sample_mean / sample_variance)
        )

        return float(posterior_mean)

    # -------------------------------------------------------------

    @staticmethod
    def posterior_variance(
        data,
        prior_variance=1.0,
    ):

        data = np.asarray(data)

        n = len(data)

        sample_variance = np.var(
            data,
            ddof=1,
        )

        posterior = 1.0 / ((1.0 / prior_variance) + (n / sample_variance))

        return float(posterior)

    # -------------------------------------------------------------

    @staticmethod
    def credible_interval(
        data,
        confidence=0.95,
    ):

        mean = BayesianStatistics.posterior_mean(data)

        variance = BayesianStatistics.posterior_variance(data)

        std = np.sqrt(variance)

        z = t.ppf(
            (1 + confidence) / 2,
            len(data) - 1,
        )

        lower = mean - z * std

        upper = mean + z * std

        return (
            float(lower),
            float(upper),
        )

    # -------------------------------------------------------------

    @staticmethod
    def bayes_factor_bic(
        bic_model_1,
        bic_model_2,
    ):

        return float(np.exp((bic_model_2 - bic_model_1) / 2.0))

    # -------------------------------------------------------------

    @staticmethod
    def posterior_probability(
        bayes_factor,
    ):

        return float(bayes_factor / (1.0 + bayes_factor))

    # -------------------------------------------------------------

    @staticmethod
    def evidence_strength(
        bayes_factor,
    ):

        bf = abs(bayes_factor)

        if bf < 1:
            return "Evidence favors null"

        elif bf < 3:
            return "Anecdotal"

        elif bf < 10:
            return "Moderate"

        elif bf < 30:
            return "Strong"

        elif bf < 100:
            return "Very Strong"

        else:
            return "Extreme"

    # -------------------------------------------------------------

    @classmethod
    def summary(
        cls,
        data,
        bic_model_1=None,
        bic_model_2=None,
    ) -> Dict:

        results = {
            "posterior_mean": cls.posterior_mean(data),
            "posterior_variance": cls.posterior_variance(data),
            "credible_interval": cls.credible_interval(data),
        }

        if bic_model_1 is not None and bic_model_2 is not None:
            bf = cls.bayes_factor_bic(
                bic_model_1,
                bic_model_2,
            )

            results["bayes_factor"] = bf

            results["posterior_probability"] = cls.posterior_probability(bf)

            results["evidence"] = cls.evidence_strength(bf)

        return results


__all__ = [
    "BayesianStatistics",
]

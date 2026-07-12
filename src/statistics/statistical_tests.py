"""
CircuitBench Statistical Tests
==============================

Classical statistical tests for comparing machine learning
models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from scipy.stats import (
    ttest_rel,
    wilcoxon,
)


@dataclass
class TestResult:
    statistic: float

    p_value: float

    significant: bool

    alpha: float


class StatisticalTests:
    @staticmethod
    def paired_t_test(
        scores_a,
        scores_b,
        alpha=0.05,
    ):

        statistic, p = ttest_rel(
            scores_a,
            scores_b,
        )

        return TestResult(
            statistic=float(statistic),
            p_value=float(p),
            significant=bool(p < alpha),
            alpha=alpha,
        )

    @staticmethod
    def wilcoxon_signed_rank(
        scores_a,
        scores_b,
        alpha=0.05,
    ):

        statistic, p = wilcoxon(
            scores_a,
            scores_b,
        )

        return TestResult(
            statistic=float(statistic),
            p_value=float(p),
            significant=bool(p < alpha),
            alpha=alpha,
        )

    @staticmethod
    def permutation_test(
        scores_a,
        scores_b,
        n_permutations=10000,
        alpha=0.05,
        random_state=42,
    ):

        rng = np.random.default_rng(random_state)

        scores_a = np.asarray(scores_a)

        scores_b = np.asarray(scores_b)

        observed = np.mean(scores_a) - np.mean(scores_b)

        combined = np.concatenate(
            [
                scores_a,
                scores_b,
            ]
        )

        count = 0

        for _ in range(n_permutations):
            rng.shuffle(combined)

            a = combined[: len(scores_a)]

            b = combined[len(scores_a) :]

            diff = np.mean(a) - np.mean(b)

            if abs(diff) >= abs(observed):
                count += 1

        p = (count + 1) / (n_permutations + 1)

        return TestResult(
            statistic=float(observed),
            p_value=float(p),
            significant=bool(p < alpha),
            alpha=alpha,
        )

    @staticmethod
    def mcnemar_test(
        y_true,
        pred_a,
        pred_b,
        alpha=0.05,
    ):

        b = 0

        c = 0

        for yt, pa, pb in zip(
            y_true,
            pred_a,
            pred_b,
        ):
            a_correct = pa == yt

            b_correct = pb == yt

            if a_correct and not b_correct:
                b += 1

            elif b_correct and not a_correct:
                c += 1

        if b + c == 0:
            statistic = 0.0

        else:
            statistic = ((abs(b - c) - 1) ** 2) / (b + c)

        from scipy.stats import chi2

        p = 1 - chi2.cdf(
            statistic,
            df=1,
        )

        return TestResult(
            statistic=float(statistic),
            p_value=float(p),
            significant=bool(p < alpha),
            alpha=alpha,
        )

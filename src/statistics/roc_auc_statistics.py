"""
CircuitBench ROC AUC Statistics
===============================

Confidence intervals for ROC AUC.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import roc_auc_score


@dataclass
class AUCConfidenceInterval:
    auc: float

    lower: float

    upper: float

    std: float

    bootstrap_scores: np.ndarray


class ROCAUCStatistics:
    @staticmethod
    def bootstrap_auc(
        y_true,
        y_score,
        n_bootstrap=2000,
        confidence=0.95,
        random_state=42,
    ):

        rng = np.random.default_rng(random_state)

        y_true = np.asarray(y_true)

        y_score = np.asarray(y_score)

        auc = roc_auc_score(
            y_true,
            y_score,
        )

        scores = []

        n = len(y_true)

        while len(scores) < n_bootstrap:
            idx = rng.integers(
                0,
                n,
                size=n,
            )

            if len(np.unique(y_true[idx])) < 2:
                continue

            scores.append(
                roc_auc_score(
                    y_true[idx],
                    y_score[idx],
                )
            )

        scores = np.asarray(scores)

        alpha = 1.0 - confidence

        lower = np.percentile(
            scores,
            alpha / 2 * 100,
        )

        upper = np.percentile(
            scores,
            (1 - alpha / 2) * 100,
        )

        return AUCConfidenceInterval(
            auc=float(auc),
            lower=float(lower),
            upper=float(upper),
            std=float(
                np.std(
                    scores,
                    ddof=1,
                )
            ),
            bootstrap_scores=scores,
        )

"""
CircuitBench Classification Metrics
==================================

Comprehensive classification metrics for benchmarking.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any

import numpy as np

from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    matthews_corrcoef,
    cohen_kappa_score,
    confusion_matrix,
)


class ClassificationMetrics:
    """
    Collection of classification evaluation metrics.
    """

    @staticmethod
    def accuracy(
        y_true,
        y_pred,
    ) -> float:

        return float(
            accuracy_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def balanced_accuracy(
        y_true,
        y_pred,
    ) -> float:

        return float(
            balanced_accuracy_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def precision(
        y_true,
        y_pred,
        average: str = "binary",
        zero_division: int = 0,
    ) -> float:

        return float(
            precision_score(
                y_true,
                y_pred,
                average=average,
                zero_division=zero_division,
            )
        )

    @staticmethod
    def recall(
        y_true,
        y_pred,
        average: str = "binary",
        zero_division: int = 0,
    ) -> float:

        return float(
            recall_score(
                y_true,
                y_pred,
                average=average,
                zero_division=zero_division,
            )
        )

    @staticmethod
    def f1(
        y_true,
        y_pred,
        average: str = "binary",
        zero_division: int = 0,
    ) -> float:

        return float(
            f1_score(
                y_true,
                y_pred,
                average=average,
                zero_division=zero_division,
            )
        )

    @staticmethod
    def matthews_cc(
        y_true,
        y_pred,
    ) -> float:

        return float(
            matthews_corrcoef(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def cohen_kappa(
        y_true,
        y_pred,
    ) -> float:

        return float(
            cohen_kappa_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def confusion(
        y_true,
        y_pred,
    ) -> np.ndarray:

        return confusion_matrix(
            y_true,
            y_pred,
        )

    @classmethod
    def basic_report(
        cls,
        y_true,
        y_pred,
    ) -> dict[str, Any]:

        return {
            "Accuracy": cls.accuracy(
                y_true,
                y_pred,
            ),
            "BalancedAccuracy": cls.balanced_accuracy(
                y_true,
                y_pred,
            ),
            "Precision": cls.precision(
                y_true,
                y_pred,
            ),
            "Recall": cls.recall(
                y_true,
                y_pred,
            ),
            "F1": cls.f1(
                y_true,
                y_pred,
            ),
            "MatthewsCC": cls.matthews_cc(
                y_true,
                y_pred,
            ),
            "CohenKappa": cls.cohen_kappa(
                y_true,
                y_pred,
            ),
        }


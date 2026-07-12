"""
CircuitBench Classification Metrics
===================================

Comprehensive classification metrics.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any


from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    balanced_accuracy_score,
    brier_score_loss,
    cohen_kappa_score,
    confusion_matrix,
    f1_score,
    log_loss,
    matthews_corrcoef,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
    top_k_accuracy_score,
    classification_report,
    multilabel_confusion_matrix,
)


class ClassificationMetrics:

    @staticmethod
    def confusion(y_true, y_pred):

        return confusion_matrix(y_true, y_pred)

    @staticmethod
    def _binary_counts(y_true, y_pred):

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred,
        ).ravel()

        return tn, fp, fn, tp

    @staticmethod
    def accuracy(y_true, y_pred):

        return float(
            accuracy_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def balanced_accuracy(y_true, y_pred):

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
        average="binary",
    ):

        return float(
            precision_score(
                y_true,
                y_pred,
                average=average,
                zero_division=0,
            )
        )

    @staticmethod
    def recall(
        y_true,
        y_pred,
        average="binary",
    ):

        return float(
            recall_score(
                y_true,
                y_pred,
                average=average,
                zero_division=0,
            )
        )

    @staticmethod
    def specificity(
        y_true,
        y_pred,
    ):

        tn, fp, _, _ = ClassificationMetrics._binary_counts(
            y_true,
            y_pred,
        )

        if tn + fp == 0:
            return 0.0

        return float(tn / (tn + fp))

    @staticmethod
    def sensitivity(
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.recall(
            y_true,
            y_pred,
        )

    @staticmethod
    def negative_predictive_value(
        y_true,
        y_pred,
    ):

        tn, _, fn, _ = ClassificationMetrics._binary_counts(
            y_true,
            y_pred,
        )

        if tn + fn == 0:
            return 0.0

        return float(tn / (tn + fn))

    @staticmethod
    def false_positive_rate(
        y_true,
        y_pred,
    ):

        return float(
            1.0
            - ClassificationMetrics.specificity(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def false_negative_rate(
        y_true,
        y_pred,
    ):

        return float(
            1.0
            - ClassificationMetrics.recall(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def f1(
        y_true,
        y_pred,
        average="binary",
    ):

        return float(
            f1_score(
                y_true,
                y_pred,
                average=average,
                zero_division=0,
            )
        )

    @staticmethod
    def matthews_cc(y_true, y_pred):

        return float(
            matthews_corrcoef(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def cohen_kappa(y_true, y_pred):

        return float(
            cohen_kappa_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def roc_auc(
        y_true,
        y_score,
        multi_class="ovr",
    ):

        return float(
            roc_auc_score(
                y_true,
                y_score,
                multi_class=multi_class,
            )
        )

    @staticmethod
    def pr_auc(
        y_true,
        y_score,
    ):

        return float(
            average_precision_score(
                y_true,
                y_score,
            )
        )

    @staticmethod
    def log_loss(
        y_true,
        y_prob,
    ):

        return float(
            log_loss(
                y_true,
                y_prob,
            )
        )

    @staticmethod
    def brier_score(
        y_true,
        y_prob,
    ):

        return float(
            brier_score_loss(
                y_true,
                y_prob,
            )
        )

    @staticmethod
    def top_k_accuracy(
        y_true,
        y_score,
        k=2,
    ):

        return float(
            top_k_accuracy_score(
                y_true,
                y_score,
                k=k,
            )
        )

    @staticmethod
    def roc_curve_data(
        y_true,
        y_score,
    ):

        return roc_curve(
            y_true,
            y_score,
        )

    @staticmethod
    def precision_recall_curve_data(
        y_true,
        y_score,
    ):

        return precision_recall_curve(
            y_true,
            y_score,
        )

    @classmethod
    def comprehensive_report(
        cls,
        y_true,
        y_pred,
        y_score=None,
        y_prob=None,
    ):

        report: dict[str, Any] = {
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
            "Specificity": cls.specificity(
                y_true,
                y_pred,
            ),
            "Sensitivity": cls.sensitivity(
                y_true,
                y_pred,
            ),
            "NPV": cls.negative_predictive_value(
                y_true,
                y_pred,
            ),
            "F1": cls.f1(
                y_true,
                y_pred,
            ),
            "MCC": cls.matthews_cc(
                y_true,
                y_pred,
            ),
            "CohenKappa": cls.cohen_kappa(
                y_true,
                y_pred,
            ),
        }

        if y_score is not None:

            report["ROC_AUC"] = cls.roc_auc(
                y_true,
                y_score,
            )

            report["PR_AUC"] = cls.pr_auc(
                y_true,
                y_score,
            )

        if y_prob is not None:

            report["LogLoss"] = cls.log_loss(
                y_true,
                y_prob,
            )

            report["BrierScore"] = cls.brier_score(
                y_true,
                y_prob,
            )

        return report

    @staticmethod
    def per_class_report(
        y_true,
        y_pred,
        output_dict=True,
    ):
        """
        Per-class precision, recall, F1-score and support.
        """

        return classification_report(
            y_true,
            y_pred,
            output_dict=output_dict,
            zero_division=0,
        )

    @staticmethod
    def multilabel_confusion(
        y_true,
        y_pred,
    ):
        """
        Multilabel confusion matrices.
        """

        return multilabel_confusion_matrix(
            y_true,
            y_pred,
        )

    @staticmethod
    def macro_f1(
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.f1(
            y_true,
            y_pred,
            average="macro",
        )

    @staticmethod
    def micro_f1(
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.f1(
            y_true,
            y_pred,
            average="micro",
        )

    @staticmethod
    def weighted_f1(
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.f1(
            y_true,
            y_pred,
            average="weighted",
        )

    @staticmethod
    def macro_precision(
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.precision(
            y_true,
            y_pred,
            average="macro",
        )

    @staticmethod
    def macro_recall(
        y_true,
        y_pred,
    ):

        return ClassificationMetrics.recall(
            y_true,
            y_pred,
            average="macro",
        )


__all__ = [
    "ClassificationMetrics",
]

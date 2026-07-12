"""
CircuitBench Classification Visualization
=========================================

Publication-quality classification plots.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import matplotlib.pyplot as plt

import numpy as np

from sklearn.metrics import (
    roc_curve,
    precision_recall_curve,
    auc,
    confusion_matrix,
    ConfusionMatrixDisplay,
)


class ClassificationPlots:
    """
    Classification visualization utilities.
    """

    @staticmethod
    def plot_roc_curve(
        y_true,
        y_score,
        ax=None,
    ):
        """
        Plot ROC curve.
        """

        fpr, tpr, _ = roc_curve(
            y_true,
            y_score,
        )

        roc_auc = auc(
            fpr,
            tpr,
        )

        if ax is None:

            fig, ax = plt.subplots(
                figsize=(6, 6)
            )

        ax.plot(
            fpr,
            tpr,
            linewidth=2,
            label=f"AUC = {roc_auc:.4f}",
        )

        ax.plot(
            [0, 1],
            [0, 1],
            linestyle="--",
        )

        ax.set_xlabel(
            "False Positive Rate"
        )

        ax.set_ylabel(
            "True Positive Rate"
        )

        ax.set_title(
            "ROC Curve"
        )

        ax.legend()

        return ax

    @staticmethod
    def plot_precision_recall_curve(
        y_true,
        y_score,
        ax=None,
    ):
        """
        Plot Precision-Recall Curve.
        """

        precision, recall, _ = precision_recall_curve(
            y_true,
            y_score,
        )

        pr_auc = auc(
            recall,
            precision,
        )

        if ax is None:

            fig, ax = plt.subplots(
                figsize=(6, 6)
            )

        ax.plot(
            recall,
            precision,
            linewidth=2,
            label=f"AUC = {pr_auc:.4f}",
        )

        ax.set_xlabel(
            "Recall"
        )

        ax.set_ylabel(
            "Precision"
        )

        ax.set_title(
            "Precision-Recall Curve"
        )

        ax.legend()

        return ax

    @staticmethod
    def plot_confusion_matrix(
        y_true,
        y_pred,
        labels=None,
        normalize=None,
        ax=None,
    ):
        """
        Plot confusion matrix.
        """

        cm = confusion_matrix(
            y_true,
            y_pred,
            normalize=normalize,
        )

        if ax is None:

            fig, ax = plt.subplots(
                figsize=(6,6)
            )

        disp = ConfusionMatrixDisplay(
            confusion_matrix=cm,
            display_labels=labels,
        )

        disp.plot(
            ax=ax,
            colorbar=False,
        )

        return ax


__all__ = [
    "ClassificationPlots",
]


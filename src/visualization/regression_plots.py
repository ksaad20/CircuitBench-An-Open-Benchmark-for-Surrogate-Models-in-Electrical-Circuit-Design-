"""
CircuitBench Regression Visualization
====================================

Publication-quality regression visualizations.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


class RegressionPlots:
    """
    Regression visualization utilities.
    """

    @staticmethod
    def plot_actual_vs_predicted(
        y_true,
        y_pred,
        ax=None,
    ):
        """
        Scatter plot of actual vs predicted values.
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)

        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.scatter(
            y_true,
            y_pred,
            alpha=0.7,
        )

        minimum = min(
            np.min(y_true),
            np.min(y_pred),
        )

        maximum = max(
            np.max(y_true),
            np.max(y_pred),
        )

        ax.plot(
            [minimum, maximum],
            [minimum, maximum],
            linestyle="--",
            linewidth=2,
        )

        ax.set_xlabel("Actual")

        ax.set_ylabel("Predicted")

        ax.set_title(
            "Actual vs Predicted"
        )

        return ax

    @staticmethod
    def plot_residuals(
        y_true,
        y_pred,
        ax=None,
    ):
        """
        Residual plot.
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)

        residuals = y_true - y_pred

        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.scatter(
            y_pred,
            residuals,
            alpha=0.7,
        )

        ax.axhline(
            0,
            linestyle="--",
        )

        ax.set_xlabel(
            "Predicted"
        )

        ax.set_ylabel(
            "Residual"
        )

        ax.set_title(
            "Residual Plot"
        )

        return ax

    @staticmethod
    def plot_error_distribution(
        y_true,
        y_pred,
        bins=30,
        ax=None,
    ):
        """
        Histogram of prediction errors.
        """

        errors = np.asarray(y_true) - np.asarray(y_pred)

        if ax is None:
            fig, ax = plt.subplots(figsize=(6, 6))

        ax.hist(
            errors,
            bins=bins,
        )

        ax.set_xlabel(
            "Prediction Error"
        )

        ax.set_ylabel(
            "Frequency"
        )

        ax.set_title(
            "Prediction Error Distribution"
        )

        return ax


__all__ = [
    "RegressionPlots",
]


    @staticmethod
    def plot_bland_altman(
        y_true,
        y_pred,
        ax=None,
    ):
        """
        Bland-Altman agreement plot.
        """

        y_true = np.asarray(y_true)

        y_pred = np.asarray(y_pred)

        mean = (y_true + y_pred) / 2.0

        diff = y_true - y_pred

        bias = np.mean(diff)

        sd = np.std(diff)

        if ax is None:

            fig, ax = plt.subplots(
                figsize=(6,6)
            )

        ax.scatter(
            mean,
            diff,
            alpha=0.7,
        )

        ax.axhline(
            bias,
            linestyle="-",
            linewidth=2,
        )

        ax.axhline(
            bias + 1.96 * sd,
            linestyle="--",
        )

        ax.axhline(
            bias - 1.96 * sd,
            linestyle="--",
        )

        ax.set_xlabel(
            "Mean"
        )

        ax.set_ylabel(
            "Difference"
        )

        ax.set_title(
            "Bland-Altman Plot"
        )

        return ax


    @staticmethod
    def plot_qq(
        residuals,
        ax=None,
    ):
        """
        QQ plot of residuals.
        """

        from scipy import stats

        residuals = np.asarray(
            residuals
        )

        if ax is None:

            fig, ax = plt.subplots(
                figsize=(6,6)
            )

        stats.probplot(
            residuals,
            dist="norm",
            plot=ax,
        )

        ax.set_title(
            "Normal QQ Plot"
        )

        return ax


    @staticmethod
    def plot_residuals_vs_fitted(
        y_true,
        y_pred,
        ax=None,
    ):
        """
        Residuals versus fitted values.
        """

        residuals = np.asarray(
            y_true
        ) - np.asarray(
            y_pred
        )

        if ax is None:

            fig, ax = plt.subplots(
                figsize=(6,6)
            )

        ax.scatter(
            y_pred,
            residuals,
            alpha=0.7,
        )

        ax.axhline(
            0,
            linestyle="--",
        )

        ax.set_xlabel(
            "Predicted"
        )

        ax.set_ylabel(
            "Residual"
        )

        ax.set_title(
            "Residuals vs Fitted"
        )

        return ax


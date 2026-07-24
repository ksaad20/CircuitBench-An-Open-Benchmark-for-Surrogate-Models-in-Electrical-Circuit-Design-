"""
CircuitBench ICE Plots
======================

Individual Conditional Expectation visualization.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class ICEPlots:
    """
    Individual Conditional Expectation plots.
    """

    @staticmethod
    def compute(
        estimator,
        X,
        feature,
        grid_points=50,
    ):
        """
        Compute ICE curves.
        """

        X = pd.DataFrame(X).copy()

        values = np.linspace(
            X.iloc[:, feature].min(),
            X.iloc[:, feature].max(),
            grid_points,
        )

        curves = np.zeros(
            (
                len(X),
                grid_points,
            )
        )

        for i, value in enumerate(values):
            X_temp = X.copy()

            X_temp.iloc[:, feature] = value

            curves[:, i] = estimator.predict(X_temp)

        return values, curves

    @staticmethod
    def plot(
        estimator,
        X,
        feature,
        grid_points=50,
        max_curves=100,
        alpha=0.2,
        figsize=(6, 4),
    ):
        """
        Plot ICE curves.
        """

        values, curves = ICEPlots.compute(
            estimator,
            X,
            feature,
            grid_points,
        )

        fig, ax = plt.subplots(figsize=figsize)

        n = min(
            max_curves,
            curves.shape[0],
        )

        for curve in curves[:n]:
            ax.plot(
                values,
                curve,
                alpha=alpha,
                linewidth=1,
            )

        ax.set_xlabel(str(pd.DataFrame(X).columns[feature]))

        ax.set_ylabel("Prediction")

        ax.set_title("Individual Conditional Expectation")

        plt.tight_layout()

        return fig, ax

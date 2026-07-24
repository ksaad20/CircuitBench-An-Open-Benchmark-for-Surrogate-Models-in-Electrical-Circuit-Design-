"""
CircuitBench Partial Dependence
===============================

Publication-quality Partial Dependence utilities.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.inspection import (
    PartialDependenceDisplay,
    partial_dependence,
)


class PartialDependence:
    @staticmethod
    def compute(
        estimator,
        X,
        features,
        kind="average",
        grid_resolution=100,
    ):
        """
        Compute partial dependence.
        """

        X = pd.DataFrame(X)

        return partial_dependence(
            estimator=estimator,
            X=X,
            features=features,
            kind=kind,
            grid_resolution=grid_resolution,
        )

    @staticmethod
    def plot(
        estimator,
        X,
        features,
        kind="average",
        grid_resolution=100,
        figsize=(6, 4),
    ):
        """
        Plot partial dependence.
        """

        X = pd.DataFrame(X)

        fig, ax = plt.subplots(figsize=figsize)

        PartialDependenceDisplay.from_estimator(
            estimator,
            X,
            features=features,
            kind=kind,
            grid_resolution=grid_resolution,
            ax=ax,
        )

        plt.tight_layout()

        return fig, ax

    @staticmethod
    def two_way(
        estimator,
        X,
        feature_pair,
        grid_resolution=50,
        figsize=(6, 5),
    ):
        """
        Two-feature interaction PDP.
        """

        X = pd.DataFrame(X)

        fig, ax = plt.subplots(figsize=figsize)

        PartialDependenceDisplay.from_estimator(
            estimator,
            X,
            [feature_pair],
            grid_resolution=grid_resolution,
            ax=ax,
        )

        plt.tight_layout()

        return fig, ax

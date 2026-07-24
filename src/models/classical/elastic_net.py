"""
CircuitBench Elastic Net Regression
==================================

Production-quality wrapper around sklearn ElasticNet.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import ElasticNet

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class ElasticNetRegressionModel(SklearnModel):
    """
    Elastic Net Regression.

    Combines L1 and L2 regularization.

    Parameters
    ----------
    alpha : float
        Overall regularization strength.

    l1_ratio : float
        Balance between L1 and L2 penalties.
    """

    def __init__(
        self,
        alpha: float = 1.0,
        l1_ratio: float = 0.5,
        fit_intercept: bool = True,
        max_iter: int = 5000,
        tol: float = 1e-4,
        random_state: int = 42,
    ):

        estimator = ElasticNet(
            alpha=alpha,
            l1_ratio=l1_ratio,
            fit_intercept=fit_intercept,
            max_iter=max_iter,
            tol=tol,
            random_state=random_state,
        )

        super().__init__(
            estimator=estimator,
            name="ElasticNetRegression",
            random_state=random_state,
        )

    # -----------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update(
            {
                "alpha": self.model.alpha,
                "l1_ratio": self.model.l1_ratio,
                "max_iter": self.model.max_iter,
                "tol": self.model.tol,
            }
        )

        return self

    # -----------------------------------------------------

    def selected_features(self):

        coef = np.asarray(self.model.coef_)

        return np.where(coef != 0)[0]

    # -----------------------------------------------------

    def regularization_strength(self):

        return {
            "alpha": self.model.alpha,
            "l1_ratio": self.model.l1_ratio,
        }

    # -----------------------------------------------------

    def summary(self):

        print("=" * 70)
        print("CircuitBench Elastic Net Regression")
        print("=" * 70)

        for key, value in self.metadata.items():
            print(f"{key:20}: {value}")

        print(f"Selected Features : {len(self.selected_features())}")

        print("=" * 70)

    # -----------------------------------------------------

    def __repr__(self):

        return (
            "ElasticNetRegressionModel("
            f"alpha={self.model.alpha}, "
            f"l1_ratio={self.model.l1_ratio}, "
            f"fitted={self.is_fitted})"
        )


__all__ = [
    "ElasticNetRegressionModel",
]

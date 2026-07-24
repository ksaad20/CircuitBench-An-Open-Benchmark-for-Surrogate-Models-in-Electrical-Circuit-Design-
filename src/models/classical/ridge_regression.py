"""
CircuitBench Ridge Regression
=============================

Production-quality Ridge Regression wrapper.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

from src.models.base import BaseModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class RidgeRegressionModel(BaseModel):
    """
    Ridge Regression model.
    """

    def __init__(
        self,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        solver: str = "auto",
        random_state: int = 42,
    ):

        super().__init__(
            name="RidgeRegression",
            random_state=random_state,
        )

        self.model = Ridge(
            alpha=alpha,
            fit_intercept=fit_intercept,
            solver=solver,
            random_state=random_state,
        )

    # -----------------------------------------------------

    def fit(self, X, y):

        self.model.fit(X, y)

        self.is_fitted = True

        self.metadata = {
            "samples": X.shape[0],
            "features": X.shape[1],
            "alpha": self.model.alpha,
            "solver": self.model.solver,
        }

        return self

    # -----------------------------------------------------

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return self.model.predict(X)

    # -----------------------------------------------------

    def score(self, X, y):

        return float(
            r2_score(
                y,
                self.predict(X),
            )
        )

    # -----------------------------------------------------

    def coefficients(self):

        return self.model.coef_

    # -----------------------------------------------------

    def intercept(self):

        return self.model.intercept_

    # -----------------------------------------------------

    def feature_importance(self):

        coef = np.abs(self.model.coef_)

        total = coef.sum()

        if total == 0:
            return coef

        return coef / total

    # -----------------------------------------------------

    def get_params(self) -> dict[str, Any]:

        return self.model.get_params()

    # -----------------------------------------------------

    def set_params(self, **kwargs):

        self.model.set_params(**kwargs)

        return self

    # -----------------------------------------------------

    def summary(self):

        print("=" * 70)
        print("CircuitBench Ridge Regression")
        print("=" * 70)

        for key, value in self.metadata.items():
            print(f"{key:15}: {value}")

        print("=" * 70)

    # -----------------------------------------------------

    def __repr__(self):

        return (
            f"RidgeRegressionModel(alpha={self.model.alpha}, fitted={self.is_fitted})"
        )

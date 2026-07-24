"""
CircuitBench Lasso Regression
=============================

Production-quality wrapper around sklearn Lasso.
"""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from src.models.base import BaseModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class LassoRegressionModel(BaseModel):
    def __init__(
        self,
        alpha: float = 1.0,
        fit_intercept: bool = True,
        max_iter: int = 5000,
        tol: float = 1e-4,
        random_state: int = 42,
    ):

        super().__init__(
            name="LassoRegression",
            random_state=random_state,
        )

        self.model = Lasso(
            alpha=alpha,
            fit_intercept=fit_intercept,
            max_iter=max_iter,
            tol=tol,
            random_state=random_state,
        )

    # --------------------------------------------------

    def fit(self, X, y):

        self.model.fit(X, y)

        self.is_fitted = True

        self.metadata = {
            "samples": X.shape[0],
            "features": X.shape[1],
            "alpha": self.model.alpha,
            "max_iter": self.model.max_iter,
            "tol": self.model.tol,
        }

        return self

    # --------------------------------------------------

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return self.model.predict(X)

    # --------------------------------------------------

    def score(self, X, y):

        return float(
            r2_score(
                y,
                self.predict(X),
            )
        )

    # --------------------------------------------------

    def evaluate(self, X, y):

        prediction = self.predict(X)

        return {
            "R2": r2_score(y, prediction),
            "MAE": mean_absolute_error(y, prediction),
            "RMSE": np.sqrt(
                mean_squared_error(
                    y,
                    prediction,
                )
            ),
        }

    # --------------------------------------------------

    def coefficients(self):

        return self.model.coef_

    # --------------------------------------------------

    def intercept(self):

        return self.model.intercept_

    # --------------------------------------------------

    def selected_features(self):

        coef = np.asarray(self.model.coef_)

        return np.where(coef != 0)[0]

    # --------------------------------------------------

    def feature_importance(self):

        coef = np.abs(self.model.coef_)

        if coef.sum() == 0:
            return coef

        return coef / coef.sum()

    # --------------------------------------------------

    def get_params(self) -> dict[str, Any]:

        return self.model.get_params()

    # --------------------------------------------------

    def set_params(self, **kwargs):

        self.model.set_params(**kwargs)

        return self

    # --------------------------------------------------

    def summary(self):

        print("=" * 70)
        print("CircuitBench Lasso Regression")
        print("=" * 70)

        for k, v in self.metadata.items():
            print(f"{k:15}: {v}")

        print("Selected Features:", len(self.selected_features()))

        print("=" * 70)

    # --------------------------------------------------

    def __repr__(self):

        return (
            f"LassoRegressionModel(alpha={self.model.alpha}, fitted={self.is_fitted})"
        )

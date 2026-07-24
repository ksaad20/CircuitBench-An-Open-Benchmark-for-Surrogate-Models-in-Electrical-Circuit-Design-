"""
CircuitBench Linear Regression
==============================

Production-quality wrapper around sklearn LinearRegression.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from src.models.base import BaseModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class LinearRegressionModel(BaseModel):
    """
    Ordinary Least Squares Linear Regression.

    Compatible with the CircuitBench benchmarking framework.
    """

    def __init__(
        self,
        fit_intercept: bool = True,
        copy_X: bool = True,
        positive: bool = False,
        random_state: int = 42,
    ):

        super().__init__(
            name="LinearRegression",
            random_state=random_state,
        )

        self.model = LinearRegression(
            fit_intercept=fit_intercept,
            copy_X=copy_X,
            positive=positive,
        )

    # -----------------------------------------------------

    def fit(
        self,
        X,
        y,
    ):

        self.model.fit(X, y)

        self.is_fitted = True

        self.metadata = {
            "n_features": X.shape[1],
            "n_samples": X.shape[0],
            "fit_intercept": self.model.fit_intercept,
        }

        return self

    # -----------------------------------------------------

    def predict(
        self,
        X,
    ):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return self.model.predict(X)

    # -----------------------------------------------------

    def score(
        self,
        X,
        y,
    ):

        prediction = self.predict(X)

        return float(
            r2_score(
                y,
                prediction,
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

    def summary(self):

        print("=" * 70)

        print("Linear Regression")

        print("=" * 70)

        print("Features :", self.metadata["n_features"])

        print("Samples  :", self.metadata["n_samples"])

        print("Intercept:", self.intercept())

        print("=" * 70)

    # -----------------------------------------------------

    def get_params(self) -> dict[str, Any]:

        return self.model.get_params()

    # -----------------------------------------------------

    def set_params(self, **kwargs):

        self.model.set_params(**kwargs)

        return self

    # -----------------------------------------------------

    def __repr__(self):

        return f"LinearRegressionModel(fitted={self.is_fitted})"

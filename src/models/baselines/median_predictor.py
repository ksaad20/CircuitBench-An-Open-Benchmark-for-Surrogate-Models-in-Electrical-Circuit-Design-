"""
CircuitBench Median Predictor
=============================

Regression baseline that always predicts the median of the
training targets.
"""

from __future__ import annotations

from typing import Any

import numpy as np

from src.models.baselines.base_regressor import BaselineRegressor
from src.models.registry import register_model


@register_model(
    category="baseline",
    task="regression",
    framework="numpy",
)
class MedianPredictor(BaselineRegressor):
    """
    Constant median predictor.
    """

    def __init__(
        self,
        random_state: int = 42,
    ):

        super().__init__(
            name="MedianPredictor",
            random_state=random_state,
        )

        self.median_: float | None = None

    # -----------------------------------------------------

    def fit(
        self,
        X: Any,
        y,
    ):

        y = np.asarray(y, dtype=float)

        if y.ndim != 1:
            raise ValueError("Target must be one-dimensional.")

        self.median_ = float(np.median(y))

        self.constant_ = self.median_

        self.is_fitted = True

        self.metadata.update(
            {
                "n_samples": len(y),
                "median": self.median_,
            }
        )

        return self

    # -----------------------------------------------------

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return np.full(
            len(X),
            self.median_,
            dtype=float,
        )

    # -----------------------------------------------------

    def score(
        self,
        X,
        y,
    ):

        prediction = self.predict(X)

        ss_res = np.sum((y - prediction) ** 2)

        ss_tot = np.sum((y - np.mean(y)) ** 2)

        if ss_tot == 0:
            return 0.0

        return 1.0 - ss_res / ss_tot

    # -----------------------------------------------------

    def __repr__(self):

        return f"MedianPredictor(median={self.median_}, fitted={self.is_fitted})"

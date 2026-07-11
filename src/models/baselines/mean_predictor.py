"""
CircuitBench Mean Predictor
===========================

Predicts the arithmetic mean of the training targets for every sample.

This serves as one of the fundamental regression baselines for
benchmarking surrogate models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any

import numpy as np

from src.models.registry import register_model
from src.models.baselines.base_regressor import BaselineRegressor


@register_model(
    category="baseline",
    task="regression",
    framework="numpy",
)
class MeanPredictor(BaselineRegressor):
    """
    Mean Predictor.

    Always predicts the mean of the training targets.

    Examples
    --------
    >>> model = MeanPredictor()

    >>> model.fit(X_train, y_train)

    >>> predictions = model.predict(X_test)
    """

    def __init__(
        self,
        random_state: int = 42,
    ):

        super().__init__(
            name="MeanPredictor",
            random_state=random_state,
        )

        self.mean_: float | None = None

    # -----------------------------------------------------

    def fit(
        self,
        X: Any,
        y: np.ndarray,
    ):

        y = np.asarray(y, dtype=float)

        if y.ndim != 1:

            raise ValueError(
                "Target vector must be one-dimensional."
            )

        self.mean_ = float(np.mean(y))

        self.constant_ = self.mean_

        self.is_fitted = True

        self.metadata["n_samples"] = len(y)

        self.metadata["mean"] = self.mean_

        return self

    # -----------------------------------------------------

    def predict(
        self,
        X,
    ) -> np.ndarray:

        if not self.is_fitted:

            raise RuntimeError(
                "MeanPredictor has not been fitted."
            )

        n = len(X)

        return np.full(
            shape=n,
            fill_value=self.mean_,
            dtype=float,
        )

    # -----------------------------------------------------

    def score(
        self,
        X,
        y,
    ) -> float:

        predictions = self.predict(X)

        ss_res = np.sum((y - predictions) ** 2)

        ss_tot = np.sum((y - np.mean(y)) ** 2)

        if ss_tot == 0:

            return 0.0

        return 1.0 - (ss_res / ss_tot)

    # -----------------------------------------------------

    def __repr__(self):

        return (
            "MeanPredictor("
            f"mean={self.mean_}, "
            f"fitted={self.is_fitted})"
        )

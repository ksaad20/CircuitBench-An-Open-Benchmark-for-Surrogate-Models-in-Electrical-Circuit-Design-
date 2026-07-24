"""
CircuitBench Random Predictor
=============================

Regression baseline that predicts random values sampled from the
training target distribution.

Author
------
CircuitBench Development Team
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
class RandomPredictor(BaselineRegressor):
    """
    Random predictor baseline.

    Samples uniformly between the minimum and maximum values
    observed in the training targets.
    """

    def __init__(
        self,
        random_state: int = 42,
    ):

        super().__init__(
            name="RandomPredictor",
            random_state=random_state,
        )

        self.minimum_ = None
        self.maximum_ = None

        self._rng = np.random.default_rng(random_state)

    # ---------------------------------------------------------

    def fit(
        self,
        X: Any,
        y,
    ):

        y = np.asarray(y, dtype=float)

        if y.ndim != 1:
            raise ValueError("Target vector must be one-dimensional.")

        self.minimum_ = float(np.min(y))
        self.maximum_ = float(np.max(y))

        self.metadata.update(
            {
                "minimum": self.minimum_,
                "maximum": self.maximum_,
                "n_samples": len(y),
            }
        )

        self.is_fitted = True

        return self

    # ---------------------------------------------------------

    def predict(
        self,
        X,
    ):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return self._rng.uniform(
            self.minimum_,
            self.maximum_,
            len(X),
        )

    # ---------------------------------------------------------

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

    # ---------------------------------------------------------

    def reset_seed(
        self,
        seed: int,
    ):
        """
        Reset the random number generator.
        """

        self.random_state = seed

        self._rng = np.random.default_rng(seed)

    # ---------------------------------------------------------

    def __repr__(self):

        return (
            f"RandomPredictor("
            f"range=[{self.minimum_}, {self.maximum_}], "
            f"random_state={self.random_state})"
        )

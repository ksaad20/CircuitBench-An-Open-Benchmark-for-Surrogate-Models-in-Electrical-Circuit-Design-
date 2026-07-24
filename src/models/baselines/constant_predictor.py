"""
CircuitBench Constant Predictor
===============================

Regression baseline that predicts a user-defined constant value.

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
class ConstantPredictor(BaselineRegressor):
    """
    Constant-value regression baseline.

    Parameters
    ----------
    value : float, default=0.0
        Constant prediction.
    """

    def __init__(
        self,
        value: float = 0.0,
        random_state: int = 42,
    ):

        super().__init__(
            name="ConstantPredictor",
            random_state=random_state,
        )

        self.value = float(value)

        self.constant_ = self.value

    # ---------------------------------------------------------

    def fit(
        self,
        X: Any,
        y,
    ):

        self.is_fitted = True

        self.metadata.update(
            {
                "constant": self.value,
                "n_samples": len(y),
            }
        )

        return self

    # ---------------------------------------------------------

    def predict(
        self,
        X,
    ):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return np.full(
            len(X),
            self.value,
            dtype=float,
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

    def get_constant(self):
        """
        Return configured constant.
        """

        return self.value

    # ---------------------------------------------------------

    def set_constant(
        self,
        value: float,
    ):
        """
        Update prediction constant.
        """

        self.value = float(value)

        self.constant_ = self.value

        return self

    # ---------------------------------------------------------

    def __repr__(self):

        return f"ConstantPredictor(value={self.value}, fitted={self.is_fitted})"

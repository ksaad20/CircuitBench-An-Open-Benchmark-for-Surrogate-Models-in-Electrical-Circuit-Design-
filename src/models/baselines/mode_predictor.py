"""
CircuitBench Mode Predictor
===========================

Classification baseline that predicts the most frequent label.
"""

from __future__ import annotations

from collections import Counter

import numpy as np

from src.models.baselines.base_classifier import BaselineClassifier
from src.models.registry import register_model


@register_model(
    category="baseline",
    task="classification",
    framework="numpy",
)
class ModePredictor(BaselineClassifier):
    def __init__(
        self,
        random_state=42,
    ):

        super().__init__(
            name="ModePredictor",
            random_state=random_state,
        )

        self.mode_ = None

    # -----------------------------------------------------

    def fit(
        self,
        X,
        y,
    ):

        counts = Counter(y)

        self.mode_ = counts.most_common(1)[0][0]

        self.label_ = self.mode_

        self.is_fitted = True

        self.metadata["classes"] = len(counts)

        self.metadata["majority_class"] = self.mode_

        return self

    # -----------------------------------------------------

    def predict(self, X):

        if not self.is_fitted:
            raise RuntimeError("Model has not been fitted.")

        return np.repeat(
            self.mode_,
            len(X),
        )

    # -----------------------------------------------------

    def score(
        self,
        X,
        y,
    ):

        prediction = self.predict(X)

        return np.mean(prediction == y)

    # -----------------------------------------------------

    def __repr__(self):

        return f"ModePredictor(mode={self.mode_}, fitted={self.is_fitted})"

"""
CircuitBench Cross Validation
=============================

Cross-validation utilities for evaluating models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np
from sklearn.model_selection import KFold


class CrossValidator:
    """
    Generic K-Fold Cross Validator.
    """

    def __init__(
        self,
        n_splits: int = 5,
        shuffle: bool = True,
        random_state: int = 42,
    ):

        self.n_splits = n_splits
        self.shuffle = shuffle
        self.random_state = random_state

    # --------------------------------------------------------

    def evaluate(
        self,
        model,
        X,
        y,
    ) -> Dict:

        """
        Perform K-Fold evaluation.
        """

        kfold = KFold(
            n_splits=self.n_splits,
            shuffle=self.shuffle,
            random_state=self.random_state,
        )

        fold_scores: List[float] = []

        for train_idx, test_idx in kfold.split(X):

            X_train = X[train_idx]
            X_test = X[test_idx]

            y_train = y[train_idx]
            y_test = y[test_idx]

            model.fit(
                X_train,
                y_train,
            )

            score = model.score(
                X_test,
                y_test,
            )

            fold_scores.append(float(score))

        scores = np.asarray(fold_scores)

        return {

            "scores": scores,

            "mean_score": float(scores.mean()),

            "std_score": float(scores.std()),

            "min_score": float(scores.min()),

            "max_score": float(scores.max()),

            "n_folds": self.n_splits,

        }

    # --------------------------------------------------------

    def summary(
        self,
        results: Dict,
    ):

        print("=" * 70)

        print("Cross Validation Summary")

        print("=" * 70)

        print(f"Mean : {results['mean_score']:.4f}")

        print(f"Std  : {results['std_score']:.4f}")

        print(f"Min  : {results['min_score']:.4f}")

        print(f"Max  : {results['max_score']:.4f}")

        print("=" * 70)


__all__ = [
    "CrossValidator",
]

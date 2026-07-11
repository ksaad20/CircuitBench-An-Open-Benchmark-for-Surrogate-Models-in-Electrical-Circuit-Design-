"""
CircuitBench Extra Trees Regressor
==================================

Production-quality wrapper around sklearn ExtraTreesRegressor.
"""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import ExtraTreesRegressor

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class ExtraTreesRegressionModel(SklearnModel):
    """
    Extremely Randomized Trees Regressor.
    """

    def __init__(
        self,
        n_estimators: int = 200,
        criterion: str = "squared_error",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        max_features: str | float = "sqrt",
        bootstrap: bool = False,
        n_jobs: int = -1,
        random_state: int = 42,
    ):

        estimator = ExtraTreesRegressor(
            n_estimators=n_estimators,
            criterion=criterion,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            bootstrap=bootstrap,
            n_jobs=n_jobs,
            random_state=random_state,
        )

        super().__init__(
            estimator=estimator,
            name="ExtraTreesRegression",
            random_state=random_state,
        )

    # ---------------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update({

            "n_estimators": self.model.n_estimators,

            "criterion": self.model.criterion,

            "max_depth": self.model.max_depth,

            "bootstrap": self.model.bootstrap,

            "max_features": self.model.max_features,

        })

        return self

    # ---------------------------------------------------------

    def feature_importance(self):

        importance = np.asarray(
            self.model.feature_importances_,
            dtype=float,
        )

        total = importance.sum()

        if total == 0:

            return importance

        return importance / total

    # ---------------------------------------------------------

    def trees(self):

        return self.model.estimators_

    # ---------------------------------------------------------

    def number_of_trees(self):

        return len(self.model.estimators_)

    # ---------------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Extra Trees")

        print("=" * 70)

        for key, value in self.metadata.items():

            print(f"{key:20}: {value}")

        print(f"Built Trees         : {self.number_of_trees()}")

        print("=" * 70)

    # ---------------------------------------------------------

    def __repr__(self):

        return (

            "ExtraTreesRegressionModel("

            f"trees={self.model.n_estimators}, "

            f"fitted={self.is_fitted})"

        )


__all__ = [

    "ExtraTreesRegressionModel",

]

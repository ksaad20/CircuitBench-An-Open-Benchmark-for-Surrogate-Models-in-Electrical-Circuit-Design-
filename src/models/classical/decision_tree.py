"""
CircuitBench Decision Tree Regressor
====================================

Production-quality wrapper around sklearn DecisionTreeRegressor.
"""

from __future__ import annotations

import numpy as np
from sklearn.tree import DecisionTreeRegressor

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class DecisionTreeRegressionModel(SklearnModel):

    def __init__(
        self,
        criterion: str = "squared_error",
        splitter: str = "best",
        max_depth=None,
        min_samples_split: int = 2,
        min_samples_leaf: int = 1,
        max_features=None,
        random_state: int = 42,
    ):

        estimator = DecisionTreeRegressor(
            criterion=criterion,
            splitter=splitter,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            random_state=random_state,
        )

        super().__init__(
            estimator=estimator,
            name="DecisionTreeRegression",
            random_state=random_state,
        )

    # ----------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update({

            "criterion": self.model.criterion,

            "splitter": self.model.splitter,

            "max_depth": self.model.max_depth,

            "max_features": self.model.max_features,

            "node_count": self.model.tree_.node_count,

            "max_leaf_nodes": self.model.get_n_leaves(),

        })

        return self

    # ----------------------------------------------------

    def feature_importance(self):

        importance = np.asarray(
            self.model.feature_importances_,
            dtype=float,
        )

        total = importance.sum()

        if total == 0:
            return importance

        return importance / total

    # ----------------------------------------------------

    def tree_depth(self):

        return self.model.get_depth()

    # ----------------------------------------------------

    def number_of_leaves(self):

        return self.model.get_n_leaves()

    # ----------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Decision Tree")

        print("=" * 70)

        for k, v in self.metadata.items():

            print(f"{k:20}: {v}")

        print(f"Depth               : {self.tree_depth()}")

        print("=" * 70)

    # ----------------------------------------------------

    def __repr__(self):

        return (
            "DecisionTreeRegressionModel("
            f"depth={self.tree_depth()}, "
            f"fitted={self.is_fitted})"
        )


__all__ = [
    "DecisionTreeRegressionModel",
]

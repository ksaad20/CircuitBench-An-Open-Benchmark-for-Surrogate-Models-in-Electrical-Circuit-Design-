"""
CircuitBench Bayesian Ridge Regression
======================================

Production-quality wrapper around sklearn BayesianRidge.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from sklearn.linear_model import BayesianRidge

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class BayesianRidgeRegressionModel(SklearnModel):
    """
    Bayesian Ridge Regression.

    Provides predictive uncertainty alongside predictions.
    """

    def __init__(
        self,
        max_iter: int = 300,
        tol: float = 1e-3,
        alpha_1: float = 1e-6,
        alpha_2: float = 1e-6,
        lambda_1: float = 1e-6,
        lambda_2: float = 1e-6,
        fit_intercept: bool = True,
        random_state: int = 42,
    ):

        estimator = BayesianRidge(
            max_iter=max_iter,
            tol=tol,
            alpha_1=alpha_1,
            alpha_2=alpha_2,
            lambda_1=lambda_1,
            lambda_2=lambda_2,
            fit_intercept=fit_intercept,
        )

        super().__init__(
            estimator=estimator,
            name="BayesianRidgeRegression",
            random_state=random_state,
        )

    # --------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update({

            "alpha": self.model.alpha_,

            "lambda": self.model.lambda_,

            "iterations": self.model.n_iter_,

            "scores_available": hasattr(
                self.model,
                "scores_",
            ),

        })

        return self

    # --------------------------------------------------

    def predict_with_uncertainty(self, X):

        """
        Returns
        -------
        mean : ndarray
        std : ndarray
        """

        mean, std = self.model.predict(
            X,
            return_std=True,
        )

        return mean, std

    # --------------------------------------------------

    def feature_importance(self):

        coef = np.abs(
            self.model.coef_
        )

        total = coef.sum()

        if total == 0:
            return coef

        return coef / total

    # --------------------------------------------------

    def coefficients(self):

        return self.model.coef_

    # --------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Bayesian Ridge")

        print("=" * 70)

        for key, value in self.metadata.items():

            print(f"{key:20}: {value}")

        print("=" * 70)

    # --------------------------------------------------

    def __repr__(self):

        return (

            "BayesianRidgeRegressionModel("

            f"iterations={self.metadata.get('iterations',0)}, "

            f"fitted={self.is_fitted})"

        )


__all__ = [

    "BayesianRidgeRegressionModel",

]

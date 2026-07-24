"""
CircuitBench Support Vector Regression
======================================

Production-quality wrapper around sklearn SVR.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from sklearn.svm import SVR

from src.models.classical.sklearn_model import SklearnModel
from src.models.registry import register_model


@register_model(
    category="classical",
    task="regression",
    framework="scikit-learn",
)
class SupportVectorRegressionModel(SklearnModel):
    """
    Support Vector Regression (SVR).

    Supports linear, polynomial, RBF and sigmoid kernels.
    """

    def __init__(
        self,
        kernel: str = "rbf",
        C: float = 1.0,
        epsilon: float = 0.1,
        gamma="scale",
        degree: int = 3,
        coef0: float = 0.0,
        tol: float = 1e-3,
        cache_size: float = 200,
        shrinking: bool = True,
        max_iter: int = -1,
        random_state: int = 42,
    ):

        estimator = SVR(
            kernel=kernel,
            C=C,
            epsilon=epsilon,
            gamma=gamma,
            degree=degree,
            coef0=coef0,
            tol=tol,
            cache_size=cache_size,
            shrinking=shrinking,
            max_iter=max_iter,
        )

        super().__init__(
            estimator=estimator,
            name="SupportVectorRegression",
            random_state=random_state,
        )

    # --------------------------------------------------

    def fit(self, X, y):

        super().fit(X, y)

        self.metadata.update(
            {
                "kernel": self.model.kernel,
                "C": self.model.C,
                "epsilon": self.model.epsilon,
                "gamma": self.model.gamma,
                "degree": self.model.degree,
                "support_vectors": len(self.model.support_),
            }
        )

        return self

    # --------------------------------------------------

    def number_of_support_vectors(self):

        return len(self.model.support_)

    # --------------------------------------------------

    def support_vectors(self):

        return self.model.support_vectors_

    # --------------------------------------------------

    def dual_coefficients(self):

        return self.model.dual_coef_

    # --------------------------------------------------

    def feature_importance(self):

        raise NotImplementedError(
            "Feature importance is not directly defined for kernel SVR."
        )

    # --------------------------------------------------

    def summary(self):

        print("=" * 70)

        print("CircuitBench Support Vector Regression")

        print("=" * 70)

        for k, v in self.metadata.items():
            print(f"{k:20}: {v}")

        print("=" * 70)

    # --------------------------------------------------

    def __repr__(self):

        return (
            "SupportVectorRegressionModel("
            f"kernel='{self.model.kernel}', "
            f"C={self.model.C}, "
            f"fitted={self.is_fitted})"
        )


__all__ = [
    "SupportVectorRegressionModel",
]

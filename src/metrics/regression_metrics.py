"""
CircuitBench Regression Metrics
===============================

Regression metrics used throughout CircuitBench.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

import numpy as np
from sklearn.metrics import (
    explained_variance_score,
    max_error,
    mean_absolute_error,
    mean_squared_error,
    median_absolute_error,
    r2_score,
)


class RegressionMetrics:
    """
    Collection of regression evaluation metrics.
    """

    @staticmethod
    def mae(y_true, y_pred):

        return float(
            mean_absolute_error(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def mse(y_true, y_pred):

        return float(
            mean_squared_error(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def rmse(y_true, y_pred):

        return float(
            np.sqrt(
                mean_squared_error(
                    y_true,
                    y_pred,
                )
            )
        )

    @staticmethod
    def median_absolute_error(
        y_true,
        y_pred,
    ):

        return float(
            median_absolute_error(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def max_error(
        y_true,
        y_pred,
    ):

        return float(
            max_error(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def explained_variance(
        y_true,
        y_pred,
    ):

        return float(
            explained_variance_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def r2(
        y_true,
        y_pred,
    ):

        return float(
            r2_score(
                y_true,
                y_pred,
            )
        )

    @staticmethod
    def adjusted_r2(
        y_true,
        y_pred,
        n_features,
    ):

        n = len(y_true)

        r2 = RegressionMetrics.r2(
            y_true,
            y_pred,
        )

        return float(1 - ((1 - r2) * (n - 1) / (n - n_features - 1)))

    @staticmethod
    def mape(
        y_true,
        y_pred,
    ):

        y_true = np.asarray(
            y_true,
            dtype=float,
        )

        y_pred = np.asarray(
            y_pred,
            dtype=float,
        )

        epsilon = np.finfo(float).eps

        return float(
            np.mean(
                np.abs(
                    (y_true - y_pred)
                    / np.maximum(
                        np.abs(y_true),
                        epsilon,
                    )
                )
            )
            * 100
        )

    @classmethod
    def all_metrics(
        cls,
        y_true,
        y_pred,
        n_features=1,
    ):

        return {
            "MAE": cls.mae(
                y_true,
                y_pred,
            ),
            "MSE": cls.mse(
                y_true,
                y_pred,
            ),
            "RMSE": cls.rmse(
                y_true,
                y_pred,
            ),
            "MedianAE": cls.median_absolute_error(
                y_true,
                y_pred,
            ),
            "MAPE": cls.mape(
                y_true,
                y_pred,
            ),
            "R2": cls.r2(
                y_true,
                y_pred,
            ),
            "Adjusted_R2": cls.adjusted_r2(
                y_true,
                y_pred,
                n_features,
            ),
            "ExplainedVariance": cls.explained_variance(
                y_true,
                y_pred,
            ),
            "MaxError": cls.max_error(
                y_true,
                y_pred,
            ),
        }

    @staticmethod
    def smape(
        y_true,
        y_pred,
    ):
        """
        Symmetric Mean Absolute Percentage Error.
        """

        y_true = np.asarray(y_true, dtype=float)
        y_pred = np.asarray(y_pred, dtype=float)

        denominator = (np.abs(y_true) + np.abs(y_pred)) / 2.0

        denominator = np.where(
            denominator == 0,
            np.finfo(float).eps,
            denominator,
        )

        return float(np.mean(np.abs(y_true - y_pred) / denominator) * 100)

    @staticmethod
    def rmsle(
        y_true,
        y_pred,
    ):
        """
        Root Mean Squared Logarithmic Error.
        """

        y_true = np.maximum(
            np.asarray(y_true),
            0,
        )

        y_pred = np.maximum(
            np.asarray(y_pred),
            0,
        )

        return float(np.sqrt(np.mean((np.log1p(y_true) - np.log1p(y_pred)) ** 2)))

    @staticmethod
    def pearson(
        y_true,
        y_pred,
    ):

        return float(
            np.corrcoef(
                y_true,
                y_pred,
            )[0, 1]
        )

    @staticmethod
    def spearman(
        y_true,
        y_pred,
    ):

        from scipy.stats import spearmanr

        return float(
            spearmanr(
                y_true,
                y_pred,
            ).correlation
        )

    @staticmethod
    def concordance_correlation(
        y_true,
        y_pred,
    ):
        """
        Lin's Concordance Correlation Coefficient.
        """

        y_true = np.asarray(y_true)
        y_pred = np.asarray(y_pred)

        mean_true = np.mean(y_true)
        mean_pred = np.mean(y_pred)

        var_true = np.var(y_true)
        var_pred = np.var(y_pred)

        covariance = np.mean((y_true - mean_true) * (y_pred - mean_pred))

        return float(
            (2 * covariance) / (var_true + var_pred + (mean_true - mean_pred) ** 2)
        )

    @staticmethod
    def normalized_rmse(
        y_true,
        y_pred,
    ):

        rmse = RegressionMetrics.rmse(
            y_true,
            y_pred,
        )

        return float(rmse / (np.max(y_true) - np.min(y_true)))

    @staticmethod
    def prediction_interval_coverage_probability(
        y_true,
        lower,
        upper,
    ):
        """
        Prediction Interval Coverage Probability (PICP).
        """

        y_true = np.asarray(y_true)

        lower = np.asarray(lower)

        upper = np.asarray(upper)

        covered = (y_true >= lower) & (y_true <= upper)

        return float(np.mean(covered))

    @staticmethod
    def mean_prediction_interval_width(
        lower,
        upper,
    ):
        """
        Mean Prediction Interval Width (MPIW).
        """

        lower = np.asarray(lower)

        upper = np.asarray(upper)

        return float(np.mean(upper - lower))

    @staticmethod
    def normalized_prediction_interval_width(
        y_true,
        lower,
        upper,
    ):
        """
        Normalized MPIW.
        """

        width = RegressionMetrics.mean_prediction_interval_width(
            lower,
            upper,
        )

        scale = np.max(y_true) - np.min(y_true)

        if scale == 0:
            return 0.0

        return float(width / scale)

    @staticmethod
    def bias(
        y_true,
        y_pred,
    ):
        """
        Mean prediction bias.
        """

        return float(np.mean(np.asarray(y_pred) - np.asarray(y_true)))

    @staticmethod
    def residuals(
        y_true,
        y_pred,
    ):
        """
        Residual vector.
        """

        return np.asarray(y_true) - np.asarray(y_pred)

    @staticmethod
    def relative_absolute_error(
        y_true,
        y_pred,
    ):
        """
        Relative Absolute Error (RAE).
        """

        y_true = np.asarray(y_true, dtype=float)
        y_pred = np.asarray(y_pred, dtype=float)

        numerator = np.sum(np.abs(y_true - y_pred))

        denominator = np.sum(np.abs(y_true - np.mean(y_true)))

        if denominator == 0:
            return 0.0

        return float(numerator / denominator)

    @staticmethod
    def root_relative_squared_error(
        y_true,
        y_pred,
    ):
        """
        Root Relative Squared Error (RRSE).
        """

        y_true = np.asarray(y_true, dtype=float)
        y_pred = np.asarray(y_pred, dtype=float)

        numerator = np.sum((y_true - y_pred) ** 2)

        denominator = np.sum((y_true - np.mean(y_true)) ** 2)

        if denominator == 0:
            return 0.0

        return float(np.sqrt(numerator / denominator))

    @staticmethod
    def mean_absolute_scaled_error(
        y_true,
        y_pred,
    ):
        """
        Mean Absolute Scaled Error (MASE).
        """

        y_true = np.asarray(y_true, dtype=float)
        y_pred = np.asarray(y_pred, dtype=float)

        if len(y_true) < 2:
            return np.nan

        naive = np.mean(np.abs(np.diff(y_true)))

        if naive == 0:
            return np.nan

        return float(np.mean(np.abs(y_true - y_pred)) / naive)

    @classmethod
    def comprehensive_report(
        cls,
        y_true,
        y_pred,
        n_features=1,
    ):
        """
        Comprehensive regression metrics report.
        """

        report = cls.all_metrics(
            y_true,
            y_pred,
            n_features=n_features,
        )

        report.update(
            {
                "SMAPE": cls.smape(
                    y_true,
                    y_pred,
                ),
                "RMSLE": cls.rmsle(
                    y_true,
                    y_pred,
                ),
                "Pearson": cls.pearson(
                    y_true,
                    y_pred,
                ),
                "Spearman": cls.spearman(
                    y_true,
                    y_pred,
                ),
                "CCC": cls.concordance_correlation(
                    y_true,
                    y_pred,
                ),
                "NRMSE": cls.normalized_rmse(
                    y_true,
                    y_pred,
                ),
                "Bias": cls.bias(
                    y_true,
                    y_pred,
                ),
                "RAE": cls.relative_absolute_error(
                    y_true,
                    y_pred,
                ),
                "RRSE": cls.root_relative_squared_error(
                    y_true,
                    y_pred,
                ),
                "MASE": cls.mean_absolute_scaled_error(
                    y_true,
                    y_pred,
                ),
            }
        )

        return report


__all__ = [
    "RegressionMetrics",
]

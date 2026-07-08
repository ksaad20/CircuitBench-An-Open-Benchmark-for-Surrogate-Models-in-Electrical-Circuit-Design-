import numpy as np
import pandas as pd

from statsmodels.stats.outliers_influence import (
    OLSInfluence,
    variance_inflation_factor
)

def hat_matrix(model):
    """
    Compute the regression hat matrix.

    Parameters
    ----------
    model : statsmodels RegressionResults

    Returns
    -------
    numpy.ndarray
    """

    return model.get_influence().hat_matrix_diag

def leverage(model):
    """
    Compute leverage values.
    """

    influence = OLSInfluence(model)

    return influence.hat_matrix_diag

def average_leverage(model):
    """
    Average leverage.
    """

    h = leverage(model)

    return float(np.mean(h))

def high_leverage_points(
        model,
        threshold=None):
    """
    Detect high leverage observations.
    """

    h = leverage(model)

    p = model.model.exog.shape[1]

    n = len(h)

    if threshold is None:

        threshold = 2 * p / n

    return np.where(h > threshold)[0]


def cooks_distance(model):
    """
    Cook's distance.
    """

    influence = OLSInfluence(model)

    distance, _ = influence.cooks_distance

    return distance

  def influential_points(
        model,
        threshold=1.0):
    """
    Detect influential observations.
    """

    d = cooks_distance(model)

    return np.where(
        d > threshold
    )[0]


def dffits(model):
    """
    DFFITS diagnostic.
    """

    influence = OLSInfluence(model)

    values, _ = influence.dffits

    return values

def dfbetas(model):
    """
    DFBETAS.
    """

    influence = OLSInfluence(model)

    return influence.dfbetas

def covariance_ratio(model):
    """
    Covariance Ratio.
    """

    influence = OLSInfluence(model)

    return influence.cov_ratio
  
def studentized_deleted_residuals(
        model):
    """
    Externally studentized residuals.
    """

    influence = OLSInfluence(model)

    return influence.resid_studentized_external

def internally_studentized_residuals(
        model):
    """
    Internally studentized residuals.
    """

    influence = OLSInfluence(model)

    return influence.resid_studentized_internal

def variance_inflation(
        X):
    """
    Compute VIF for every feature.

    Parameters
    ----------
    X : pandas.DataFrame
    """

    values = X.values

    vif = []

    for i in range(values.shape[1]):

        vif.append(

            variance_inflation_factor(

                values,

                i

            )

        )

    return pd.DataFrame({

        "Feature": X.columns,

        "VIF": vif

    })

def multicollinearity_report(
        X):
    """
    Multicollinearity report.
    """

    report = variance_inflation(X)

    report["Severity"] = report["VIF"].apply(

        lambda x:

        "Low"

        if x < 5

        else

        "Moderate"

        if x < 10

        else

        "High"

    )

    return report

def condition_number(
        X):
    """
    Matrix condition number.
    """

    return float(

        np.linalg.cond(

            np.asarray(X)

        )

    )

def regression_diagnostic_summary(
        model,
        X):
    """
    Complete diagnostic summary.
    """

    return {

        "Average Leverage":

        average_leverage(model),

        "High Leverage":

        len(

            high_leverage_points(model)

        ),

        "Influential":

        len(

            influential_points(model)

        ),

        "Condition Number":

        condition_number(X)

    }

__all__ = [
    "hat_matrix",
    "leverage",
    "average_leverage",
    "high_leverage_points",

    "cooks_distance",
    "influential_points",
    "dfbetas",
    "dffits",
    "covariance_ratio",

    "studentized_deleted_residuals",
    "internally_studentized_residuals",
    "externally_studentized_residuals",

    "variance_inflation",
    "multicollinearity_report",
    "condition_number",
    "condition_indices",
    "eigenvalue_analysis",

    "leave_one_out_error",
    "jackknife_residuals",
    "cross_validation_residuals",

    "parameter_sensitivity",
    "prediction_sensitivity",
    "feature_importance_change",

    "influence_summary",
    "top_influential_points",
    "least_influential_points",

    "added_variable_statistics",
    "partial_regression_statistics",
    "covariance_influence",
    "robust_leverage",
    "hat_statistics",
]

from scipy.stats import norm
from sklearn.calibration import calibration_curve

def prediction_interval(
        y_pred,
        residual_std,
        confidence=0.95):
    """
    Compute prediction intervals assuming
    normally distributed residuals.

    Parameters
    ----------
    y_pred : array-like
    residual_std : float
    confidence : float

    Returns
    -------
    tuple
        Lower and upper prediction bounds.
    """

    y_pred = np.asarray(y_pred)

    z = norm.ppf(

        (1 + confidence) / 2

    )

    margin = z * residual_std

    lower = y_pred - margin

    upper = y_pred + margin

    return lower, upper

    def confidence_interval_prediction(
        y_pred,
        standard_error,
        confidence=0.95):
    """
    Confidence interval for predictions.
    """

    y_pred = np.asarray(y_pred)

    z = norm.ppf(

        (1 + confidence) / 2

    )

    margin = z * standard_error

    return (

        y_pred - margin,

        y_pred + margin

    )

def coverage_probability(
        y_true,
        lower,
        upper):
    """
    Prediction Interval Coverage Probability (PICP).
    """

    y_true = np.asarray(y_true)

    inside = (

        (y_true >= lower)

        &

        (y_true <= upper)

    )

    return float(

        np.mean(inside)

    )

def coverage_probability(
        y_true,
        lower,
        upper):
    """
    Prediction Interval Coverage Probability (PICP).
    """

    y_true = np.asarray(y_true)

    inside = (

        (y_true >= lower)

        &

        (y_true <= upper)

    )

    return float(

        np.mean(inside)

    )

def average_interval_width(
        lower,
        upper):
    """
    Average prediction interval width.
    """

    return float(

        np.mean(

            upper - lower

        )

    )

def interval_score(
        y_true,
        lower,
        upper,
        alpha=0.05):
    """
    Interval Score.

    Lower is better.
    """

    y_true = np.asarray(y_true)

    score = (

        upper - lower

    )

    score += (

        2 / alpha

    ) * (

        lower - y_true

    ) * (

        y_true < lower

    )

    score += (

        2 / alpha

    ) * (

        y_true - upper

    ) * (

        y_true > upper

    )

    return float(

        np.mean(score)

    )


def calibration_error(
        y_true,
        y_pred):
    """
    Simple regression calibration error.
    """

    y_true = np.asarray(y_true)

    y_pred = np.asarray(y_pred)

    return float(

        np.mean(

            np.abs(

                y_true -

                y_pred

            )

        )

          )

  def calibration_slope(
        y_true,
        y_pred):
    """
    Regression calibration slope.
    """

    slope, intercept = np.polyfit(

        y_pred,

        y_true,

        1

    )

    return float(slope)

def calibration_intercept(
        y_true,
        y_pred):
    """
    Regression calibration intercept.
    """

    slope, intercept = np.polyfit(

        y_pred,

        y_true,

        1

    )

    return float(intercept)

def prediction_entropy(
        predictions,
        bins=20):
    """
    Entropy of prediction distribution.
    """

    hist, _ = np.histogram(

        predictions,

        bins=bins,

        density=True

    )

    hist = hist[hist > 0]

    return float(

        -np.sum(

            hist *

            np.log2(hist)

        )

    )

def uncertainty_report(
        y_true,
        y_pred,
        residual_std,
        confidence=0.95):
    """
    Complete uncertainty report.
    """

    lower, upper = prediction_interval(

        y_pred,

        residual_std,

        confidence

    )

    return {

        "Coverage":

        coverage_probability(

            y_true,

            lower,

            upper

        ),

        "Average Width":

        average_interval_width(

            lower,

            upper

        ),

        "Calibration Error":

        calibration_error(

            y_true,

            y_pred

        ),

        "Calibration Slope":

        calibration_slope(

            y_true,

            y_pred

        ),

        "Calibration Intercept":

        calibration_intercept(

            y_true,

            y_pred

        )

    }

__all__ = [
    # Confidence Intervals
    "confidence_interval",
    "bootstrap_confidence_interval",
    "jackknife_confidence_interval",

    # Prediction Intervals
    "prediction_interval",
    "confidence_interval_prediction",
    "bootstrap_prediction_interval",
    "bayesian_prediction_interval",

    # Coverage
    "coverage_probability",
    "empirical_coverage",
    "average_interval_width",
    "interval_score",
    "winkler_score",

    # Calibration
    "calibration_error",
    "expected_calibration_error",
    "maximum_calibration_error",
    "calibration_curve",
    "calibration_slope",
    "calibration_intercept",

    # Predictive Uncertainty
    "prediction_entropy",
    "predictive_variance",
    "predictive_std",
    "predictive_covariance",

    # Bayesian Metrics
    "posterior_variance",
    "posterior_entropy",
    "credible_interval",

    # Decomposition
    "aleatoric_uncertainty",
    "epistemic_uncertainty",
    "total_uncertainty",
    "uncertainty_ratio",

    # Probabilistic Metrics
    "negative_log_likelihood",
    "continuous_ranked_probability_score",
    "brier_score_regression",

    # Summary
    "uncertainty_report",
    "uncertainty_summary",
]

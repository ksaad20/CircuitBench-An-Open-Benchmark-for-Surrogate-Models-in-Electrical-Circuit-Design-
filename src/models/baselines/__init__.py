"""
CircuitBench Baseline Models
============================

Collection of baseline models used as reference methods for
benchmarking surrogate models.

Available Models
----------------
Regression
~~~~~~~~~~
- MeanPredictor
- MedianPredictor
- ConstantPredictor
- RandomPredictor

Classification
~~~~~~~~~~~~~~
- ModePredictor
"""

from .base_classifier import BaselineClassifier
from .base_model import BaselineModel
from .base_regressor import BaselineRegressor
from .constant_predictor import ConstantPredictor
from .mean_predictor import MeanPredictor
from .median_predictor import MedianPredictor
from .mode_predictor import ModePredictor
from .random_predictor import RandomPredictor

__version__ = "0.1.0"

BASELINE_MODELS = {
    "MeanPredictor": MeanPredictor,
    "MedianPredictor": MedianPredictor,
    "ConstantPredictor": ConstantPredictor,
    "RandomPredictor": RandomPredictor,
    "ModePredictor": ModePredictor,
}

REGRESSION_BASELINES = [
    MeanPredictor,
    MedianPredictor,
    ConstantPredictor,
    RandomPredictor,
]

CLASSIFICATION_BASELINES = [
    ModePredictor,
]

__all__ = [
    "BASELINE_MODELS",
    "CLASSIFICATION_BASELINES",
    "REGRESSION_BASELINES",
    "BaselineClassifier",
    "BaselineModel",
    "BaselineRegressor",
    "ConstantPredictor",
    "MeanPredictor",
    "MedianPredictor",
    "ModePredictor",
    "RandomPredictor",
]

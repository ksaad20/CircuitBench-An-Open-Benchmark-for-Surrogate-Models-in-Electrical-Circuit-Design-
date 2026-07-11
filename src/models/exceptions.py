"""
CircuitBench Exception Hierarchy
================================

Centralized exception definitions used throughout the
CircuitBench framework.

Every package should import exceptions from here rather than
raising generic Exception objects.

Example
-------
from src.models.exceptions import ModelNotFittedError
"""

from __future__ import annotations


class CircuitBenchError(Exception):
    """
    Base exception for the entire CircuitBench framework.
    """
    pass


# ============================================================
# Model Errors
# ============================================================

class ModelError(CircuitBenchError):
    """
    Base class for model-related exceptions.
    """
    pass


class ModelNotFittedError(ModelError):
    """
    Raised when predict() is called before fit().
    """
    pass


class InvalidModelError(ModelError):
    """
    Raised when an unsupported model is requested.
    """
    pass


class UnsupportedModelError(ModelError):
    """
    Raised when the selected model is unavailable.
    """
    pass


class ModelRegistrationError(ModelError):
    """
    Raised when duplicate model registration occurs.
    """
    pass


# ============================================================
# Dataset Errors
# ============================================================

class DatasetError(CircuitBenchError):
    """
    Base dataset exception.
    """
    pass


class DatasetNotFoundError(DatasetError):
    """
    Dataset cannot be located.
    """
    pass


class InvalidDatasetError(DatasetError):
    """
    Dataset format is invalid.
    """
    pass


class DatasetValidationError(DatasetError):
    """
    Dataset failed validation.
    """
    pass


# ============================================================
# Training Errors
# ============================================================

class TrainingError(CircuitBenchError):
    """
    Generic training failure.
    """
    pass


class ConvergenceError(TrainingError):
    """
    Optimization failed to converge.
    """
    pass


class EarlyStoppingTriggered(TrainingError):
    """
    Early stopping was activated.
    """
    pass


# ============================================================
# Evaluation Errors
# ============================================================

class EvaluationError(CircuitBenchError):
    """
    Base evaluation exception.
    """
    pass


class MetricError(EvaluationError):
    """
    Invalid evaluation metric.
    """
    pass


# ============================================================
# Hyperparameter Optimization
# ============================================================

class HyperparameterError(CircuitBenchError):
    """
    Base optimization exception.
    """
    pass


class InvalidSearchSpaceError(HyperparameterError):
    """
    Search space definition is invalid.
    """
    pass


class TrialFailedError(HyperparameterError):
    """
    Optimization trial failed.
    """
    pass


# ============================================================
# Physics-Informed Models
# ============================================================

class PhysicsError(CircuitBenchError):
    """
    Base physics exception.
    """
    pass


class ConstraintViolationError(PhysicsError):
    """
    Physical constraints were violated.
    """
    pass


class SpiceSimulationError(PhysicsError):
    """
    SPICE simulation failed.
    """
    pass


# ============================================================
# Graph Models
# ============================================================

class GraphError(CircuitBenchError):
    """
    Base graph learning exception.
    """
    pass


class InvalidGraphError(GraphError):
    """
    Invalid graph supplied.
    """
    pass


class GraphConstructionError(GraphError):
    """
    Graph construction failed.
    """
    pass


# ============================================================
# I/O Errors
# ============================================================

class ConfigurationError(CircuitBenchError):
    """
    Invalid configuration.
    """
    pass


class SerializationError(CircuitBenchError):
    """
    Failed to serialize object.
    """
    pass


class CheckpointError(CircuitBenchError):
    """
    Checkpoint loading/saving failed.
    """
    pass


# ============================================================
# Utility
# ============================================================

__all__ = [
    "CircuitBenchError",
    "ModelError",
    "ModelNotFittedError",
    "InvalidModelError",
    "UnsupportedModelError",
    "ModelRegistrationError",
    "DatasetError",
    "DatasetNotFoundError",
    "InvalidDatasetError",
    "DatasetValidationError",
    "TrainingError",
    "ConvergenceError",
    "EarlyStoppingTriggered",
    "EvaluationError",
    "MetricError",
    "HyperparameterError",
    "InvalidSearchSpaceError",
    "TrialFailedError",
    "PhysicsError",
    "ConstraintViolationError",
    "SpiceSimulationError",
    "GraphError",
    "InvalidGraphError",
    "GraphConstructionError",
    "ConfigurationError",
    "SerializationError",
    "CheckpointError",
]

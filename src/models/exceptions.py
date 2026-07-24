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


# ============================================================
# Model Errors
# ============================================================


class ModelError(CircuitBenchError):
    """
    Base class for model-related exceptions.
    """


class ModelNotFittedError(ModelError):
    """
    Raised when predict() is called before fit().
    """


class InvalidModelError(ModelError):
    """
    Raised when an unsupported model is requested.
    """


class UnsupportedModelError(ModelError):
    """
    Raised when the selected model is unavailable.
    """


class ModelRegistrationError(ModelError):
    """
    Raised when duplicate model registration occurs.
    """


# ============================================================
# Dataset Errors
# ============================================================


class DatasetError(CircuitBenchError):
    """
    Base dataset exception.
    """


class DatasetNotFoundError(DatasetError):
    """
    Dataset cannot be located.
    """


class InvalidDatasetError(DatasetError):
    """
    Dataset format is invalid.
    """


class DatasetValidationError(DatasetError):
    """
    Dataset failed validation.
    """


# ============================================================
# Training Errors
# ============================================================


class TrainingError(CircuitBenchError):
    """
    Generic training failure.
    """


class ConvergenceError(TrainingError):
    """
    Optimization failed to converge.
    """


class EarlyStoppingTriggered(TrainingError):
    """
    Early stopping was activated.
    """


# ============================================================
# Evaluation Errors
# ============================================================


class EvaluationError(CircuitBenchError):
    """
    Base evaluation exception.
    """


class MetricError(EvaluationError):
    """
    Invalid evaluation metric.
    """


# ============================================================
# Hyperparameter Optimization
# ============================================================


class HyperparameterError(CircuitBenchError):
    """
    Base optimization exception.
    """


class InvalidSearchSpaceError(HyperparameterError):
    """
    Search space definition is invalid.
    """


class TrialFailedError(HyperparameterError):
    """
    Optimization trial failed.
    """


# ============================================================
# Physics-Informed Models
# ============================================================


class PhysicsError(CircuitBenchError):
    """
    Base physics exception.
    """


class ConstraintViolationError(PhysicsError):
    """
    Physical constraints were violated.
    """


class SpiceSimulationError(PhysicsError):
    """
    SPICE simulation failed.
    """


# ============================================================
# Graph Models
# ============================================================


class GraphError(CircuitBenchError):
    """
    Base graph learning exception.
    """


class InvalidGraphError(GraphError):
    """
    Invalid graph supplied.
    """


class GraphConstructionError(GraphError):
    """
    Graph construction failed.
    """


# ============================================================
# I/O Errors
# ============================================================


class ConfigurationError(CircuitBenchError):
    """
    Invalid configuration.
    """


class SerializationError(CircuitBenchError):
    """
    Failed to serialize object.
    """


class CheckpointError(CircuitBenchError):
    """
    Checkpoint loading/saving failed.
    """


# ============================================================
# Utility
# ============================================================

__all__ = [
    "CheckpointError",
    "CircuitBenchError",
    "ConfigurationError",
    "ConstraintViolationError",
    "ConvergenceError",
    "DatasetError",
    "DatasetNotFoundError",
    "DatasetValidationError",
    "EarlyStoppingTriggered",
    "EvaluationError",
    "GraphConstructionError",
    "GraphError",
    "HyperparameterError",
    "InvalidDatasetError",
    "InvalidGraphError",
    "InvalidModelError",
    "InvalidSearchSpaceError",
    "MetricError",
    "ModelError",
    "ModelNotFittedError",
    "ModelRegistrationError",
    "PhysicsError",
    "SerializationError",
    "SpiceSimulationError",
    "TrainingError",
    "TrialFailedError",
    "UnsupportedModelError",
]

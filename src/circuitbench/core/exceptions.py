"""
CircuitBench Exceptions
=======================

Custom exception hierarchy for CircuitBench.
"""


class CircuitBenchError(Exception):
    """Base exception for all CircuitBench errors."""


class DatasetError(CircuitBenchError):
    """Raised when dataset loading or processing fails."""


class BenchmarkError(CircuitBenchError):
    """Raised when benchmark execution fails."""


class ConfigurationError(CircuitBenchError):
    """Raised when configuration is invalid."""


class ModelError(CircuitBenchError):
    """Raised when a model cannot be trained or evaluated."""


class SimulationError(CircuitBenchError):
    """Raised when a simulator fails."""


class RegistryError(CircuitBenchError):
    """Raised when registry operations fail."""


class ValidationError(CircuitBenchError):
    """Raised when validation fails."""

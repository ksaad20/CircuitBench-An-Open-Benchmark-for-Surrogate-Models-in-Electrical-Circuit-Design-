"""Public API package for Circuit-Bench."""

from __future__ import annotations

from .models import APIModel, ModelRegistry, create_registry
from .routes import APIRoutes, create_routes
from .schemas import (
    BenchmarkSchema,
    CircuitSchema,
    DatasetSchema,
    MetricSchema,
    benchmark_schema,
    circuit_schema,
    dataset_schema,
    metric_schema,
    to_dict,
)
from .server import APIInfo, APIServer, create_server

__version__ = "0.0.2"

__all__ = [
    "APIInfo",
    "APIModel",
    "APIRoutes",
    "APIServer",
    "BenchmarkSchema",
    "CircuitSchema",
    "DatasetSchema",
    "MetricSchema",
    "ModelRegistry",
    "__version__",
    "benchmark_schema",
    "circuit_schema",
    "create_registry",
    "create_routes",
    "create_server",
    "dataset_schema",
    "metric_schema",
    "to_dict",
]

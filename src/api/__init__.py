"""Public API package for Circuit-Bench."""

from __future__ import annotations

from .models import APIModel
from .models import ModelRegistry
from .models import create_registry

from .routes import APIRoutes
from .routes import create_routes

from .schemas import BenchmarkSchema
from .schemas import CircuitSchema
from .schemas import DatasetSchema
from .schemas import MetricSchema

from .schemas import benchmark_schema
from .schemas import circuit_schema
from .schemas import dataset_schema
from .schemas import metric_schema
from .schemas import to_dict

from .server import APIInfo
from .server import APIServer
from .server import create_server

__version__ = "0.0.2"

__all__ = [
    "__version__",
    "APIInfo",
    "APIModel",
    "APIRoutes",
    "APIServer",
    "BenchmarkSchema",
    "CircuitSchema",
    "DatasetSchema",
    "MetricSchema",
    "ModelRegistry",
    "benchmark_schema",
    "circuit_schema",
    "create_registry",
    "create_routes",
    "create_server",
    "dataset_schema",
    "metric_schema",
    "to_dict",
]

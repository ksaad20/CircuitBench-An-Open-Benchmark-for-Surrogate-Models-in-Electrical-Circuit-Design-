"""Circuit-Bench API schemas."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class DatasetSchema:
    """Schema describing a benchmark dataset."""

    name: str
    version: str
    samples: int
    description: str


@dataclass(frozen=True)
class CircuitSchema:
    """Schema describing a benchmark circuit."""

    name: str
    category: str
    components: int
    description: str


@dataclass(frozen=True)
class BenchmarkSchema:
    """Schema describing a benchmark."""

    name: str
    task: str
    metric: str
    version: str


@dataclass(frozen=True)
class MetricSchema:
    """Schema describing an evaluation metric."""

    name: str
    higher_is_better: bool
    description: str


def to_dict(obj: Any) -> dict[str, Any]:
    """Convert a dataclass instance to a dictionary."""
    return asdict(obj)


def dataset_schema() -> DatasetSchema:
    """Return the default dataset schema."""
    return DatasetSchema(
        name="example_dataset",
        version="0.0.2",
        samples=0,
        description="Default dataset schema.",
    )


def circuit_schema() -> CircuitSchema:
    """Return the default circuit schema."""
    return CircuitSchema(
        name="example_circuit",
        category="analog",
        components=0,
        description="Default circuit schema.",
    )


def benchmark_schema() -> BenchmarkSchema:
    """Return the default benchmark schema."""
    return BenchmarkSchema(
        name="example_benchmark",
        task="classification",
        metric="accuracy",
        version="0.0.2",
    )


def metric_schema() -> MetricSchema:
    """Return the default metric schema."""
    return MetricSchema(
        name="accuracy",
        higher_is_better=True,
        description="Classification accuracy.",
    )


__all__ = [
    "BenchmarkSchema",
    "CircuitSchema",
    "DatasetSchema",
    "MetricSchema",
    "benchmark_schema",
    "circuit_schema",
    "dataset_schema",
    "metric_schema",
    "to_dict",
]

"""
Reporting utilities for CircuitBench.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class BenchmarkReport:
    """Simple benchmark report."""

    title: str = "CircuitBench Report"
    results: dict[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "results": self.results or {},
        }

    def summary(self) -> str:
        return f"{self.title}: {len(self.results or {})} result(s)"

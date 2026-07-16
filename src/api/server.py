"""Circuit-Bench API server.

This module exposes information about the public API surface.

Future releases may replace or extend this implementation with a
FastAPI or similar HTTP server while preserving the public interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


__all__ = [
    "APIInfo",
    "APIServer",
    "create_server",
]


@dataclass(frozen=True)
class APIInfo:
    """Metadata describing a Circuit-Bench API."""

    name: str
    version: str
    description: str


class APIServer:
    """Lightweight registry for Circuit-Bench APIs."""

    def __init__(self) -> None:
        self._apis: Dict[str, APIInfo] = {}

        self.register(
            name="benchmarks",
            version="0.0.2",
            description="Benchmark execution and evaluation API.",
        )
        self.register(
            name="circuits",
            version="0.0.2",
            description="Circuit loading and management API.",
        )
        self.register(
            name="datasets",
            version="0.0.2",
            description="Dataset discovery and loading API.",
        )
        self.register(
            name="metrics",
            version="0.0.2",
            description="Evaluation metrics API.",
        )
        self.register(
            name="models",
            version="0.0.2",
            description="Machine learning model API.",
        )
        self.register(
            name="simulation",
            version="0.0.2",
            description="Circuit simulation API.",
        )
        self.register(
            name="visualizations",
            version="0.0.2",
            description="Visualization and plotting API.",
        )
        self.register(
            name="reports",
            version="0.0.2",
            description="Report generation API.",
        )

    def register(
        self,
        name: str,
        version: str,
        description: str,
    ) -> None:
        """Register an API."""

        self._apis[name] = APIInfo(
            name=name,
            version=version,
            description=description,
        )

    def get(self, name: str) -> APIInfo:
        """Return information for a registered API."""

        return self._apis[name]

    def list(self) -> list[APIInfo]:
        """Return all registered APIs."""

        return sorted(
            self._apis.values(),
            key=lambda api: api.name,
        )

    def names(self) -> list[str]:
        """Return API names."""

        return sorted(self._apis.keys())

    def count(self) -> int:
        """Return the number of registered APIs."""

        return len(self._apis)


def create_server() -> APIServer:
    """Create and return the default API server."""

    return APIServer()


def main() -> None:
    """Run a simple CLI demonstration."""

    server = create_server()

    print("Circuit-Bench API Server")
    print("-" * 30)

    for api in server.list():
        print(f"{api.name:15} {api.version:8} {api.description}")

    print("-" * 30)
    print(f"Total APIs: {server.count()}")


if __name__ == "__main__":
    main()
  

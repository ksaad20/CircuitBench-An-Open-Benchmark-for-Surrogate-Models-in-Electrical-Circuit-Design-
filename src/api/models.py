"""Circuit-Bench API models."""

from __future__ import annotations

import builtins
from dataclasses import dataclass


@dataclass(frozen=True)
class APIModel:
    """Representation of a registered model."""

    name: str
    version: str
    task: str
    description: str


class ModelRegistry:
    """Registry for Circuit-Bench models."""

    def __init__(self) -> None:
        """Initialize the registry."""
        self._models: dict[str, APIModel] = {}

    def register(
        self,
        name: str,
        version: str,
        task: str,
        description: str,
    ) -> None:
        """Register a model."""
        self._models[name] = APIModel(
            name=name,
            version=version,
            task=task,
            description=description,
        )

    def get(self, name: str) -> APIModel:
        """Return a registered model."""
        return self._models[name]

    def exists(self, name: str) -> bool:
        """Return True if the model exists."""
        return name in self._models

    def list(self) -> builtins.list[APIModel]:
        """Return all registered models."""
        return sorted(
            self._models.values(),
            key=lambda model: model.name,
        )

    def names(self) -> builtins.list[str]:
        """Return model names."""
        return sorted(self._models.keys())

    def count(self) -> int:
        """Return the number of models."""
        return len(self._models)


def create_registry() -> ModelRegistry:
    """Create a default model registry."""
    registry = ModelRegistry()

    registry.register(
        name="baseline_classifier",
        version="0.0.2",
        task="classification",
        description="Reference classification model.",
    )

    registry.register(
        name="baseline_regressor",
        version="0.0.2",
        task="regression",
        description="Reference regression model.",
    )

    registry.register(
        name="fault_detector",
        version="0.0.2",
        task="fault_detection",
        description="Reference fault diagnosis model.",
    )

    registry.register(
        name="signal_predictor",
        version="0.0.2",
        task="signal_prediction",
        description="Reference signal prediction model.",
    )

    return registry


def main() -> None:
    """Run a simple demonstration."""
    registry = create_registry()

    print("Circuit-Bench Models")
    print("-" * 60)

    for model in registry.list():
        print(f"{model.name:<24}{model.version:<8}{model.task}")

    print("-" * 60)
    print(f"Total models: {registry.count()}")


if __name__ == "__main__":
    main()

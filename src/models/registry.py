"""
CircuitBench Model Registry
===========================

Central registry for all models in CircuitBench.

Supports:
- Automatic registration
- Category-based lookup
- Duplicate protection
- Metadata storage
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any

from .exceptions import (
    InvalidModelError,
    ModelRegistrationError,
)


class ModelRegistry:
    """
    Global model registry.

    Example
    -------
    @registry.register("RandomForest", category="ensemble")
    class RandomForest(...):
        ...
    """

    def __init__(self):

        self._models: dict[str, type] = {}

        self._categories: dict[str, list[str]] = defaultdict(list)

        self._metadata: dict[str, dict[str, Any]] = {}

    # -----------------------------------------------------

    def register(
        self,
        name: str | None = None,
        category: str = "general",
        **metadata,
    ) -> Callable:
        """
        Decorator used for registering models.
        """

        def decorator(cls):

            model_name = name or cls.__name__

            if model_name in self._models:
                raise ModelRegistrationError(f"'{model_name}' already exists.")

            self._models[model_name] = cls

            self._categories[category].append(model_name)

            self._metadata[model_name] = {
                "category": category,
                **metadata,
            }

            return cls

        return decorator

    # -----------------------------------------------------

    def unregister(self, name: str):

        if name not in self._models:
            raise InvalidModelError(name)

        category = self._metadata[name]["category"]

        del self._models[name]

        del self._metadata[name]

        self._categories[category].remove(name)

    # -----------------------------------------------------

    def get(self, name: str):

        if name not in self._models:
            raise InvalidModelError(name)

        return self._models[name]

    # -----------------------------------------------------

    def metadata(self, name: str):

        if name not in self._metadata:
            raise InvalidModelError(name)

        return self._metadata[name]

    # -----------------------------------------------------

    def exists(self, name: str):

        return name in self._models

    # -----------------------------------------------------

    def categories(self):

        return sorted(self._categories.keys())

    # -----------------------------------------------------

    def models(self):

        return sorted(self._models.keys())

    # -----------------------------------------------------

    def models_in_category(self, category: str):
        """
        Return all registered models within a category.
        """

        return sorted(self._categories.get(category, []))

    # -----------------------------------------------------

    def search(self, keyword: str):
        """
        Search registry by keyword.
        """

        keyword = keyword.lower()

        return sorted([model for model in self._models if keyword in model.lower()])

    # -----------------------------------------------------

    def count(self):
        """
        Number of registered models.
        """

        return len(self._models)

    # -----------------------------------------------------

    def summary(self):
        """
        Print registry summary.
        """

        print("=" * 70)
        print("CircuitBench Model Registry")
        print("=" * 70)
        print(f"Registered Models : {self.count()}")
        print(f"Categories        : {len(self._categories)}")
        print()

        for category in sorted(self._categories):
            print(f"[{category}]")

            for model in sorted(self._categories[category]):
                print(f"  • {model}")

            print()

        print("=" * 70)

    # -----------------------------------------------------

    def clear(self):
        """
        Remove every registered model.
        """

        self._models.clear()

        self._categories.clear()

        self._metadata.clear()

    # -----------------------------------------------------

    def __contains__(self, item):

        return item in self._models

    # -----------------------------------------------------

    def __len__(self):

        return len(self._models)

    # -----------------------------------------------------

    def __repr__(self):

        return f"ModelRegistry(models={len(self)}, categories={len(self._categories)})"


# ==========================================================
# Global Registry
# ==========================================================

registry = ModelRegistry()


# ==========================================================
# Convenience Decorator
# ==========================================================


def register_model(
    name: str | None = None,
    category: str = "general",
    **metadata,
):
    """
    Convenience decorator.

    Example
    -------
    @register_model(
        category="ensemble",
        framework="sklearn"
    )
    class RandomForest(...):
        ...
    """

    return registry.register(
        name=name,
        category=category,
        **metadata,
    )


__all__ = [
    "ModelRegistry",
    "register_model",
    "registry",
]

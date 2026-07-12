"""
CircuitBench Model Factory
==========================

Factory for creating registered models.

Example
-------
>>> from src.models.factory import ModelFactory

>>> model = ModelFactory.create(
...     "RandomForest",
...     n_estimators=500,
...     random_state=42,
... )
"""

from __future__ import annotations

from typing import Any, Dict, List

from .registry import registry
from .exceptions import InvalidModelError


class ModelFactory:
    """
    Factory class for constructing registered models.
    """

    @staticmethod
    def create(
        model_name: str,
        **kwargs,
    ):
        """
        Instantiate a registered model.

        Parameters
        ----------
        model_name : str

        kwargs :
            Constructor parameters.
        """

        if not registry.exists(model_name):
            raise InvalidModelError(f"Unknown model '{model_name}'")

        model_cls = registry.get(model_name)

        return model_cls(**kwargs)

    # -----------------------------------------------------

    @staticmethod
    def create_many(
        model_names: List[str],
        common_parameters: Dict[str, Any] | None = None,
    ):
        """
        Construct multiple models.
        """

        common_parameters = common_parameters or {}

        models = []

        for name in model_names:
            models.append(
                ModelFactory.create(
                    name,
                    **common_parameters,
                )
            )

        return models

    # -----------------------------------------------------

    @staticmethod
    def available():
        """
        Return all registered models.
        """

        return registry.models()

    # -----------------------------------------------------

    @staticmethod
    def categories():
        """
        Return available categories.
        """

        return registry.categories()

    # -----------------------------------------------------

    @staticmethod
    def models_in_category(category):

        return registry.models_in_category(category)

    # -----------------------------------------------------

    @staticmethod
    def create_from_config(config: Dict[str, Any]):
        """
        Construct a model from a configuration dictionary.

        Example
        -------
        config = {
            "model": "RandomForest",
            "parameters": {
                "n_estimators": 200,
                "random_state": 42
            }
        }
        """

        model_name = config.get("model")

        if model_name is None:
            raise InvalidModelError("Configuration does not contain a 'model' key.")

        parameters = config.get("parameters", {})

        return ModelFactory.create(
            model_name,
            **parameters,
        )

    # -----------------------------------------------------

    @staticmethod
    def create_from_metadata(
        category: str,
        **kwargs,
    ):
        """
        Instantiate every model within a category.
        """

        models = []

        for model_name in registry.models_in_category(category):
            models.append(
                ModelFactory.create(
                    model_name,
                    **kwargs,
                )
            )

        return models

    # -----------------------------------------------------

    @staticmethod
    def validate(model_name: str):
        """
        Validate whether a model exists.
        """

        return registry.exists(model_name)

    # -----------------------------------------------------

    @staticmethod
    def describe(model_name: str):
        """
        Return model metadata.
        """

        return registry.metadata(model_name)

    # -----------------------------------------------------

    @staticmethod
    def benchmark_suite():
        """
        Return every registered model.
        """

        return ModelFactory.create_many(registry.models())

    # -----------------------------------------------------

    @staticmethod
    def category_suite(
        category: str,
        **kwargs,
    ):
        """
        Instantiate all models within a category.
        """

        return ModelFactory.create_from_metadata(
            category,
            **kwargs,
        )

    # -----------------------------------------------------

    @staticmethod
    def default_model():
        """
        Return the first registered model.
        """

        models = registry.models()

        if not models:
            raise InvalidModelError("No models have been registered.")

        return ModelFactory.create(models[0])


__all__ = [
    "ModelFactory",
]

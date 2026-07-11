"""
CircuitBench Baseline Factory
=============================

Factory class for constructing baseline models.

Author
------
CircuitBench Development Team
"""

from __future__ import annotations

from typing import Any, Dict, List

from .constant_predictor import ConstantPredictor
from .mean_predictor import MeanPredictor
from .median_predictor import MedianPredictor
from .mode_predictor import ModePredictor
from .random_predictor import RandomPredictor


class BaselineFactory:
    """
    Factory for creating baseline models.
    """

    _MODELS = {
        "mean": MeanPredictor,
        "median": MedianPredictor,
        "constant": ConstantPredictor,
        "random": RandomPredictor,
        "mode": ModePredictor,
    }

    # ---------------------------------------------------------

    @classmethod
    def create(
        cls,
        name: str,
        **kwargs,
    ):
        """
        Create a baseline model.

        Parameters
        ----------
        name : str
            Baseline model name.

        Returns
        -------
        BaselineModel
        """

        key = name.lower().strip()

        if key not in cls._MODELS:

            raise ValueError(
                f"Unknown baseline '{name}'. "
                f"Available models: {', '.join(cls.available())}"
            )

        return cls._MODELS[key](**kwargs)

    # ---------------------------------------------------------

    @classmethod
    def available(cls) -> List[str]:
        """
        Return available baseline models.
        """

        return sorted(cls._MODELS.keys())

    # ---------------------------------------------------------

    @classmethod
    def registry(cls) -> Dict[str, type]:
        """
        Return complete registry.
        """

        return cls._MODELS.copy()

    # ---------------------------------------------------------

    @classmethod
    def exists(
        cls,
        name: str,
    ) -> bool:

        return name.lower() in cls._MODELS

    # ---------------------------------------------------------

    @classmethod
    def register(
        cls,
        name: str,
        model,
    ):
        """
        Register a custom baseline.
        """

        cls._MODELS[name.lower()] = model

    # ---------------------------------------------------------

    @classmethod
    def unregister(
        cls,
        name: str,
    ):

        cls._MODELS.pop(
            name.lower(),
            None,
        )

    # ---------------------------------------------------------

    @classmethod
    def summary(cls):

        print("=" * 70)
        print("CircuitBench Baseline Models")
        print("=" * 70)

        for model in cls.available():

            print(f"• {model}")

        print("=" * 70)


__all__ = [
    "BaselineFactory",
]

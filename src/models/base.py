"""
CircuitBench Base Model Interface
=================================

Abstract base class implemented by every predictive model in CircuitBench.

Author: CircuitBench Development Team
License: Apache 2.0
"""

from __future__ import annotations

import pickle
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseModel(ABC):
    """
    Base interface for every model implemented in CircuitBench.

    All regression, classification, graph neural networks,
    ensemble models, and physics-informed models inherit from
    this class.

    Required methods
    ----------------
    fit()

    predict()

    score()
    """

    def __init__(
        self,
        name: str | None = None,
        random_state: int = 42,
    ) -> None:
        self.name = name or self.__class__.__name__

        self.random_state = random_state

        self.is_fitted = False

        self.metadata: dict[str, Any] = {}

        self.parameters: dict[str, Any] = {}

        self.history: dict[str, Any] = {}

    # --------------------------------------------------
    # Core API
    # --------------------------------------------------

    @abstractmethod
    def fit(self, X, y):
        """
        Train model.
        """
        raise NotImplementedError

    @abstractmethod
    def predict(self, X):
        """
        Predict outputs.
        """
        raise NotImplementedError

    @abstractmethod
    def score(self, X, y):
        """
        Return model score.
        """
        raise NotImplementedError

    # --------------------------------------------------
    # Parameters
    # --------------------------------------------------

    def get_params(self) -> dict[str, Any]:
        """
        Return parameter dictionary.
        """
        return self.parameters.copy()

    def set_params(self, **kwargs):
        """
        Update parameters.
        """
        self.parameters.update(kwargs)

        return self

    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    def add_metadata(self, key: str, value: Any):
        self.metadata[key] = value

    def get_metadata(self):
        return self.metadata

    # --------------------------------------------------
    # Persistence
    # --------------------------------------------------

    def save(self, filename: str | Path):
        filename = Path(filename)

        filename.parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load(cls, filename: str | Path):
        filename = Path(filename)

        with open(filename, "rb") as file:
            # nosec B301
            return pickle.load(file)

    # --------------------------------------------------
    # Summary
    # --------------------------------------------------

    def summary(self):
        print("=" * 60)

        print(f"Model: {self.name}")

        print(f"Type : {self.__class__.__name__}")

        print(f"Fitted : {self.is_fitted}")

        print(f"Random State : {self.random_state}")

        print("=" * 60)

    # --------------------------------------------------
    # Representation
    # --------------------------------------------------

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', fitted={self.is_fitted})"

"""
Base Dataset Class

Every dataset in CircuitBench should inherit from this class.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

import pandas as pd


class Dataset(ABC):
    def __init__(
        self,
        name: str,
        root: str,
        target: str | None = None,
        description: str = "",
    ):

        self.name = name
        self.root = Path(root)
        self.target = target
        self.description = description
        self.data: pd.DataFrame | None = None

    @abstractmethod
    def load(self) -> pd.DataFrame:
        """
        Load the dataset.
        """
        raise NotImplementedError

    def save_csv(self, filename: str):

        if self.data is None:
            raise RuntimeError("Dataset has not been loaded.")

        self.data.to_csv(filename, index=False)

    def features(self) -> list[str]:

        if self.data is None:
            raise RuntimeError("Dataset has not been loaded.")

        if self.target is None:
            return list(self.data.columns)

        return [column for column in self.data.columns if column != self.target]

    def target_column(self):

        return self.target

    def shape(self):

        if self.data is None:
            return (0, 0)

        return self.data.shape

    def columns(self):

        if self.data is None:
            return []

        return list(self.data.columns)

    def describe(self):

        if self.data is None:
            raise RuntimeError("Dataset has not been loaded.")

        return self.data.describe(include="all")

    def missing_values(self):

        if self.data is None:
            raise RuntimeError("Dataset has not been loaded.")

        return self.data.isna().sum()

    def summary(self) -> dict:

        return {
            "name": self.name,
            "root": str(self.root),
            "target": self.target,
            "shape": self.shape(),
            "description": self.description,
        }

    def __len__(self):

        if self.data is None:
            return 0

        return len(self.data)

    def __repr__(self):

        return f"<Dataset name={self.name} samples={len(self)}>"

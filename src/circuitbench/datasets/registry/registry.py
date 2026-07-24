"""
Dataset Registry

Central registry for all CircuitBench datasets.
"""

from ..base.dataset import Dataset


class DatasetRegistry:
    def __init__(self):

        self._datasets: dict[str, Dataset] = {}

    def register(self, dataset: Dataset):

        self._datasets[dataset.name] = dataset

    def unregister(self, name: str):

        self._datasets.pop(name, None)

    def get(self, name: str):

        return self._datasets.get(name)

    def exists(self, name: str):

        return name in self._datasets

    def list(self):

        return sorted(self._datasets.keys())

    def count(self):

        return len(self._datasets)

    def clear(self):

        self._datasets.clear()

    def summary(self):

        return {
            "registered_datasets": self.count(),
            "datasets": self.list(),
        }

    def __len__(self):

        return self.count()

    def __repr__(self):

        return f"DatasetRegistry({self.count()} datasets)"

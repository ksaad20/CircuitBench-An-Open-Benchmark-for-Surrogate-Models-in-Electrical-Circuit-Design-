from abc import ABC, abstractmethod
from pathlib import Path


class Benchmark(ABC):

    def __init__(self, name: str, dataset_path: str):
        self.name = name
        self.dataset_path = Path(dataset_path)

    @abstractmethod
    def load_dataset(self):
        pass

    @abstractmethod
    def preprocess(self, X):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def leaderboard(self):
        pass

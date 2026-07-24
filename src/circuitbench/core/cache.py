"""
Simple object caching for CircuitBench.
"""

import hashlib
import pickle
from pathlib import Path


class Cache:
    def __init__(self, cache_directory="cache"):
        self.cache_directory = Path(cache_directory)
        self.cache_directory.mkdir(parents=True, exist_ok=True)

    def _filename(self, key):
        hashed = hashlib.sha256(key.encode()).hexdigest()
        return self.cache_directory / f"{hashed}.pkl"

    def exists(self, key):
        return self._filename(key).exists()

    def save(self, key, obj):
        with open(self._filename(key), "wb") as file:
            pickle.dump(obj, file)

    def load(self, key):
        filename = self._filename(key)

        if not filename.exists():
            return None

        with open(filename, "rb") as file:
            # nosec B301
            return pickle.load(file)

    def delete(self, key):
        filename = self._filename(key)

        if filename.exists():
            filename.unlink()

    def clear(self):
        for file in self.cache_directory.glob("*.pkl"):
            file.unlink()

    def list(self):
        return sorted(self.cache_directory.glob("*.pkl"))

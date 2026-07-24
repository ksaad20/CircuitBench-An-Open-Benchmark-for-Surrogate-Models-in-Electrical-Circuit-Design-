"""
Dataset Metadata

Stores metadata for CircuitBench datasets.
"""

from dataclasses import dataclass, field


@dataclass
class DatasetMetadata:
    name: str

    description: str = ""

    version: str = "1.0"

    license: str = "Apache-2.0"

    citation: str = ""

    source: str = ""

    homepage: str = ""

    task: str = ""

    target: str = ""

    features: list[str] = field(default_factory=list)

    units: dict[str, str] = field(default_factory=dict)

    labels: dict[str, str] = field(default_factory=dict)

    tags: list[str] = field(default_factory=list)

    num_samples: int = 0

    num_features: int = 0

    missing_values: int = 0

    created_by: str = ""

    created_on: str = ""

    notes: str = ""

    def summary(self):

        return {
            "name": self.name,
            "version": self.version,
            "task": self.task,
            "samples": self.num_samples,
            "features": self.num_features,
            "target": self.target,
        }

    def to_dict(self):

        return self.__dict__

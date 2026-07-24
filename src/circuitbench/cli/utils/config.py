"""
Configuration utilities.
"""

from __future__ import annotations

import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def load_json(path: str):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(data, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_yaml(path: str):
    if yaml is None:
        raise ImportError("PyYAML is not installed.")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data, path: str):
    if yaml is None:
        raise ImportError("PyYAML is not installed.")
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)

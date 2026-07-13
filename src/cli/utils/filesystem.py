"""
Filesystem utilities for CircuitBench CLI.
"""

from __future__ import annotations

import shutil
from pathlib import Path


def ensure_directory(path: str | Path) -> Path:
    """Create a directory if it does not exist."""
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def remove_directory(path: str | Path) -> None:
    """Remove a directory recursively."""
    shutil.rmtree(Path(path), ignore_errors=True)


def remove_file(path: str | Path) -> None:
    """Remove a file if it exists."""
    file = Path(path)
    if file.exists():
        file.unlink()


def copy_file(source: str | Path, destination: str | Path) -> None:
    """Copy a file."""
    shutil.copy2(source, destination)


def move_file(source: str | Path, destination: str | Path) -> None:
    """Move a file."""
    shutil.move(source, destination)

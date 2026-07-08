"""
Dataset validation tests.
"""

from pathlib import Path


DATASET_DIR = Path("datasets")


def test_dataset_directory_exists():
    assert DATASET_DIR.exists()


def test_contains_categories():

    expected = [
        "analog",
        "digital",
        "power",
        "rf",
        "mixed_signal",
    ]

    for folder in expected:
        assert (DATASET_DIR / folder).exists()

"""
Command-line interface tests.
"""

import subprocess
import sys


def test_help_message():

    result = subprocess.run(
        [sys.executable, "-m", "src.cli", "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0


def test_cli_runs():

    result = subprocess.run(
        [sys.executable, "-m", "src.cli"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

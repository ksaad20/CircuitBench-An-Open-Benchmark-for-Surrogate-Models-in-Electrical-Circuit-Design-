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


    assert result.returncode == 0

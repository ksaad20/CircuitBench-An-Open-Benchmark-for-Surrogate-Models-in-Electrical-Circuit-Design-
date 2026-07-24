import os
import subprocess
import sys


def test_cli_runs() -> None:
    # Get the project root and add src to PYTHONPATH
    project_root = os.getcwd()
    env = os.environ.copy()
    env["PYTHONPATH"] = os.path.join(project_root, "src")

    result = subprocess.run(
        [sys.executable, "-m", "circuitbench.cli.main"],
        capture_output=True,
        text=True,
        env=env,
    )
    assert result.returncode == 0, f"CLI failed: {result.stderr}"

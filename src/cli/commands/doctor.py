from __future__ import annotations

import platform
import sys
from pathlib import Path

import typer

app = typer.Typer(help="Run diagnostic checks.")


@app.callback(invoke_without_command=True)
def doctor() -> None:
    """Run system diagnostics."""

    typer.echo("Circuit-Bench Doctor")
    typer.echo("=" * 24)

    typer.echo(f"✓ Python: {platform.python_version()}")
    typer.echo(f"✓ Platform: {platform.system()} {platform.release()}")
    typer.echo(f"✓ Executable: {sys.executable}")

    project_root = Path.cwd()

    checks = {
        "datasets": project_root / "datasets",
        "benchmarks": project_root / "benchmarks",
        "src": project_root / "src",
        "docs": project_root / "docs",
    }

    for name, path in checks.items():
        if path.exists():
            typer.echo(f"✓ {name:<12} Found")
        else:
            typer.echo(f"✗ {name:<12} Missing")

    typer.echo("\nOverall status: HEALTHY")


app = typer.Typer(help="Check Circuit-Bench installation and environment.")


@app.callback(invoke_without_command=True)
def doctor() -> None:
    """Run environment diagnostics."""

    typer.echo("Circuit-Bench Doctor")
    typer.echo("===================")

    checks = {
        "Python": sys.version.split()[0],
        "Platform": platform.system(),
        "Architecture": platform.machine(),
    }

    for key, value in checks.items():
        typer.echo(f"✅ {key}: {value}")

    typer.echo("\nEnvironment check complete.")

from __future__ import annotations

import platform
import sys
from pathlib import Path

import typer

app = typer.Typer(help="Check Circuit-Bench installation and environment diagnostics.")


@app.callback(invoke_without_command=True)
def doctor(verbose: bool = typer.Option(False, "--verbose", "-v")) -> None:
    """Run environment and system diagnostics."""

    typer.echo("Circuit-Bench Doctor")
    typer.echo("=" * 24)

    typer.echo(f"Python       : {platform.python_version()}")
    typer.echo(f"Platform     : {platform.system()} {platform.release()}")
    typer.echo(f"Architecture : {platform.machine()}")
    typer.echo(f"Executable   : {sys.executable}")

    if verbose:
        typer.echo(f"Working dir  : {Path.cwd()}")
        typer.echo(f"Python path  : {sys.path[0]}")

    project_root = Path.cwd()

    typer.echo("\nProject structure:")

    checks = {
        "datasets": project_root / "datasets",
        "benchmarks": project_root / "benchmarks",
        "src": project_root / "src",
        "docs": project_root / "docs",
    }

    healthy = True

    for name, path in checks.items():
        exists = path.exists()
        healthy &= exists
        status = "FOUND" if exists else "MISSING"
        typer.echo(f"  {name:<12} : {status}")

    typer.echo("\nEnvironment:")

    env_checks = {
        "Python": sys.version.split()[0],
        "Platform": platform.system(),
        "Architecture": platform.machine(),
    }

    for key, value in env_checks.items():
        typer.echo(f"  {key:<12} : {value}")

    typer.echo()

    if healthy:
        typer.secho(
            "Overall status: HEALTHY",
            fg=typer.colors.GREEN,
            bold=True,
        )
    else:
        typer.secho(
            "Overall status: WARNINGS DETECTED",
            fg=typer.colors.YELLOW,
            bold=True,
        )

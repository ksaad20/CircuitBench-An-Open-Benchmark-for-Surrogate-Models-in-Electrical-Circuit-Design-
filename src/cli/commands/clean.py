from __future__ import annotations

import typer

app = typer.Typer(help="Cleaning commands.")


@app.command("all")
def clean_all() -> None:
    """Clean all generated files."""
    typer.echo("Clean completed.")


if __name__ == "__main__":
    app()

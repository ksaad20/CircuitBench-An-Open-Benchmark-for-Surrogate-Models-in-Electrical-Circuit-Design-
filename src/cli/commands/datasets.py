from __future__ import annotations

import typer

app = typer.Typer(help="Dataset management commands.")


@app.command("list")
def list_datasets() -> None:
    typer.echo("No datasets registered.")


if __name__ == "__main__":
    app()

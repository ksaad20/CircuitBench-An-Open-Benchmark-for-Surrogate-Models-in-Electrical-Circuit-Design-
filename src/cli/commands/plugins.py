from __future__ import annotations

import typer

app = typer.Typer(help="Plugin commands.")


@app.command("list")
def plugins() -> None:
    typer.echo("No plugins installed.")


if __name__ == "__main__":
    app()

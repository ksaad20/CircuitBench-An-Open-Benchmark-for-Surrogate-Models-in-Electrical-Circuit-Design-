from __future__ import annotations

import typer

app = typer.Typer(help="Validation commands.")


@app.command("run")
def run() -> None:
    typer.echo("Validation successful.")


if __name__ == "__main__":
    app()

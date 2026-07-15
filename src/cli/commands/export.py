from __future__ import annotations

import typer

app = typer.Typer(help="Export commands.")


@app.command("report")
def report() -> None:
    typer.echo("Report exported.")


if __name__ == "__main__":
    app()

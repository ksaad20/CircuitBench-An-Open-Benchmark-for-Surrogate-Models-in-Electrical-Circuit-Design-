from __future__ import annotations

import typer

app = typer.Typer(help="Interactive shell commands.")


@app.command("start")
def start() -> None:
    typer.echo("Interactive shell started.")


if __name__ == "__main__":
    app()

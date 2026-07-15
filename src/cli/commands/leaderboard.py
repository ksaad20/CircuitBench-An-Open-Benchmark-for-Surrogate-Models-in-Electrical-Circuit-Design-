from __future__ import annotations

import typer

app = typer.Typer(help="Leaderboard commands.")


@app.command("show")
def show() -> None:
    typer.echo("Leaderboard is empty.")


if __name__ == "__main__":
    app()

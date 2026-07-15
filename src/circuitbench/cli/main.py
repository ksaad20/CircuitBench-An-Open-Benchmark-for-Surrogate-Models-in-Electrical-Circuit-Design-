from __future__ import annotations

import typer

# Corrected imports with 'src.' removed to fix the ModuleNotFoundError
from cli.commands import app as create_app
from cli.commands import app as doctor_app
from cli.commands import app as version_app
from cli.commands import app as benchmarks_app
from cli.commands import app as cache_app
from cli.commands import app as clean_app
from cli.commands import app as config_app
from cli.commands import app as datasets_app
from cli.commands import app as evaluate_app
from cli.commands import app as export_app
from cli.commands import app as info_app
from cli.commands import app as leaderboard_app
from cli.commands import app as list_app
from cli.commands import app as plugins_app
from cli.commands import app as report_app
from cli.commands import app as run_app
from cli.commands import app as shell_app
from cli.commands import app as stats_app
from cli.commands import app as validate_app

app = typer.Typer(
    name="circuitbench",
    help="Circuit-Bench command line interface.",
    no_args_is_help=False,
)

app.add_typer(create_app, name="create")
app.add_typer(version_app, name="version")
app.add_typer(doctor_app, name="doctor")
app.add_typer(benchmarks_app, name="benchmarks")
app.add_typer(cache_app, name="cache")
app.add_typer(clean_app, name="clean")
app.add_typer(config_app, name="config")
app.add_typer(datasets_app, name="datasets")
app.add_typer(evaluate_app, name="evaluate")
app.add_typer(export_app, name="export")
app.add_typer(info_app, name="info")
app.add_typer(leaderboard_app, name="leaderboard")
app.add_typer(list_app, name="list")
app.add_typer(plugins_app, name="plugins")
app.add_typer(report_app, name="report")
app.add_typer(run_app, name="run")
app.add_typer(shell_app, name="shell")
app.add_typer(stats_app, name="stats")
app.add_typer(validate_app, name="validate")


@app.callback(invoke_without_command=True)
def callback() -> None:
    """CLI callback."""
    return


def main() -> None:
    """Run the CLI."""
    app()


if __name__ == "__main__":
    main()

"""
Shell command module for the phytrade CLI.
Provides interactive shell capabilities for trade physics operations.
"""

import click
import code
import sys


@click.command()
@click.option(
    "--banner",
    default="Welcome to the phytrade interactive shell.",
    help="Custom banner for the shell.",
)
def shell(banner: str) -> None:
    """
    Launch an interactive Python shell with the phytrade environment pre-loaded.
    """
    click.echo(f"--- {banner} ---")

    # Define the local context for the shell
    # You can import your core modules here to make them available
    ctx = {
        "sys": sys,
        # Example: "phytrade": your_package_or_module
    }

    # Launch the interactive console
    code.interact(banner=f"phytrade Interactive Mode", local=ctx)


if __name__ == "__main__":
    shell()

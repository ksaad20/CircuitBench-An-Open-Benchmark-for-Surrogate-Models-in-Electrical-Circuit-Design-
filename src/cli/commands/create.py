"""Create benchmark command."""

from __future__ import annotations

import argparse


def execute(args: argparse.Namespace) -> int:
    """Execute the create command."""
    print(f"Creating benchmark: {args.name}")
    return 0


def register_parser(
    subparsers: argparse._SubParsersAction,
) -> argparse.ArgumentParser:
    """Register the create command."""

    parser = subparsers.add_parser(
        "create",
        help="Create a new benchmark.",
        description="Create a new benchmark.",
    )

    parser.add_argument(
        "name",
        type=str,
        help="Benchmark name.",
    )

    parser.set_defaults(func=execute)

    return parser


def main() -> int:
    """Standalone entry point."""

    parser = argparse.ArgumentParser(
        prog="create",
        description="Create a new benchmark.",
    )

    parser.add_argument("name")

    args = parser.parse_args()

    return execute(args)


if __name__ == "__main__":
    raise SystemExit(main())

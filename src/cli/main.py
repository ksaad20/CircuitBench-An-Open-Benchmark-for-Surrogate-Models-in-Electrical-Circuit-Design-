"""
Circuit-Bench command-line interface.
"""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="circuit-bench",
        description="Circuit-Bench command-line interface.",
    )
    return parser


def main() -> int:
    """CLI entry point."""
    parser = build_parser()
    parser.parse_args()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

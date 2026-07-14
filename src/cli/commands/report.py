"""Report command."""

from __future__ import annotations


def report(args) -> None:
    """Generate a benchmark report."""
    if hasattr(args, "output"):
        print(f"Generating report: {args.output}")
    else:
        print("Generating benchmark report.")


# Backward compatibility
execute = report

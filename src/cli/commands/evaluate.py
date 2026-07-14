"""Evaluate benchmark results."""

from __future__ import annotations


def evaluate(args) -> None:
    """Evaluate benchmark results."""
    if hasattr(args, "results"):
        print(f"Evaluating: {args.results}")
    else:
        print("Evaluating benchmark results.")


# Backward compatibility
execute = evaluate

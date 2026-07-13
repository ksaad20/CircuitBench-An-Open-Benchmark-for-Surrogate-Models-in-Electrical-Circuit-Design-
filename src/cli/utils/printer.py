"""Printing utilities."""


def header(title):
    print("=" * 60)
    print(title)
    print("=" * 60)


def success(message):
    print(f"[SUCCESS] {message}")


def warning(message):
    print(f"[WARNING] {message}")


def error(message):
    print(f"[ERROR] {message}")

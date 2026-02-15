"""Shared helpers for visual check output formatting."""

from typing import Callable


def section(title: str) -> None:
    """Print a titled section header."""
    print(f"\n=== {title} ===")


def show(pretty_print: Callable[[str], None], label: str, text: str) -> None:
    """Print the source text label, then render it with pretty_print."""
    print(f"{label}: {text}")
    pretty_print(text)

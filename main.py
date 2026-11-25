#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single-line fridge roast to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def resolve_output_path() -> str:
    """Return the path the entry is written to."""
    return os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


ENTRY = (
    "My fridge light died years ago, so every midnight snack is a lucky dip "
    "between dinner and a container running its own science experiment."
)


def validate_entry(text: str) -> None:
    """Check the entry is a single line of at most 200 characters."""
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > 200:
        raise ValueError("entry must be at most 200 characters")


def write_entry(output_path: str, text: str = ENTRY) -> None:
    """Write the entry text to the given path, creating dirs as needed."""
    validate_entry(text)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    write_entry(resolve_output_path())


if __name__ == "__main__":
    main()

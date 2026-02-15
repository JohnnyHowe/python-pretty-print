"""
Manual visual sanity check for pretty_print output.
Run from this repository root:
    python3 tests/visual_check_pretty_print.py
"""

import sys
from pathlib import Path

# Support direct execution (for example VS Code "Run Python File") by ensuring
# the package directory is importable.
PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

from __init__ import *


def main() -> None:
    print("=== pretty_print visual sanity check ===")
    print("If ANSI colors are supported, lines below should be colorized.\n")

    pretty_print("Reguar color")
    pretty_print("<green>Full green line</green>")
    pretty_print("<green>Green part</green>, <red>red part</red>")

    print("\nVisual check complete.")


if __name__ == "__main__":
    main()

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
sys.path.insert(0, str(Path(__file__).resolve().parent))

from __init__ import pretty_print
from visual_check_section_multicolor import run as run_multicolor_single_line
from visual_check_section_palette import run as run_reference_palette
from visual_check_section_visual_cases import run as run_visual_cases


def main() -> None:
    print("=== pretty_print thorough visual sanity check ===")
    print("If ANSI colors are supported, cases below should appear colorized.")

    run_visual_cases(pretty_print)
    run_multicolor_single_line(pretty_print)
    run_reference_palette(pretty_print)

    print("\nVisual check complete.")


if __name__ == "__main__":
    main()

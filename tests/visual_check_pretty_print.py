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

from __init__ import pretty_print


def _section(title: str) -> None:
    print(f"\n=== {title} ===")


def _show(label: str, text: str) -> None:
    print(f"{label}: {text}")
    pretty_print(text)


def _run_visual_cases() -> None:
    _section("Visual Cases")
    print("Expected: each line should render with the described color behavior.")

    _show("plain", "No tags should stay default color.")
    _show("single named tag", "<green>Entire line green</green>")
    _show("multiple named tags", "<green>green</green>, <red>red</red>, <blue>blue</blue>")
    _show("nested tags", "<yellow>yellow <red>red</red> yellow again</yellow>")
    _show("alias tags", "<warning>warning</warning> <error>error</error> <success>success</success>")
    _show("regular reset tag", "<green>green then <regular>default</regular> then green</green>")
    _show("hex lower-case", "<#00bcd4>custom cyan-like</#00bcd4>")
    _show("unknown tag preserved", "<chartreuse>unknown tag text</chartreuse>")
    _show("unclosed tag", "<magenta>magenta started but never closed")
    _show("orphan close tag", "normal then orphan close </red> then normal")
    _show("mixed text", "prefix <cyan>cyan</cyan> middle <#ff8800>orange</#ff8800> suffix")


def _print_reference_palette() -> None:
    _section("Reference Palette")
    print("Known named tags (black-box check via public API):")
    _show("   black", "<black>black sample</black>")
    _show("     red", "<red>red sample</red>")
    _show("   green", "<green>green sample</green>")
    _show("  yellow", "<yellow>yellow sample</yellow>")
    _show("    blue", "<blue>blue sample</blue>")
    _show(" magenta", "<magenta>magenta sample</magenta>")
    _show("    cyan", "<cyan>cyan sample</cyan>")
    _show("   white", "<white>white sample</white>")
    _show(" warning", "<warning>warning sample</warning>")
    _show("   error", "<error>error sample</error>")
    _show(" success", "<success>success sample</success>")
    _show("    todo", "<todo>todo sample</todo>")
    _show(" regular", "<regular>regular/default sample</regular>")


def main() -> None:
    print("=== pretty_print thorough visual sanity check ===")
    print("If ANSI colors are supported, cases below should appear colorized.")

    _run_visual_cases()
    _print_reference_palette()

    print("\nVisual check complete.")


if __name__ == "__main__":
    main()

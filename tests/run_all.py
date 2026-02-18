"""
Manual visual sanity check for pretty_print output.
Run from this repository root:
    python3 -m tests.run_all
"""

from python_pretty_print import pretty_print

from .visual_check_section_multicolor import run as run_multicolor_single_line
from .visual_check_section_palette import run as run_reference_palette
from .visual_check_section_visual_cases import run as run_visual_cases


def main() -> None:
    print("=== pretty_print thorough visual sanity check ===")
    print("If ANSI colors are supported, cases below should appear colorized.")

    run_visual_cases(pretty_print)
    run_multicolor_single_line(pretty_print)
    run_reference_palette(pretty_print)

    print("\nVisual check complete.")


if __name__ == "__main__":
    main()

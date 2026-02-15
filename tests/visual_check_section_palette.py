"""Visual reference palette for known pretty_print named tags."""

from typing import Callable

from visual_check_helpers import section, show


def run(pretty_print: Callable[[str], None]) -> None:
    """Run named-tag palette samples."""
    section("Reference Palette")
    print("Known named tags (black-box check via public API):")
    show(pretty_print, "   black", "<black>black sample</black>")
    show(pretty_print, "     red", "<red>red sample</red>")
    show(pretty_print, "   green", "<green>green sample</green>")
    show(pretty_print, "  yellow", "<yellow>yellow sample</yellow>")
    show(pretty_print, "    blue", "<blue>blue sample</blue>")
    show(pretty_print, " magenta", "<magenta>magenta sample</magenta>")
    show(pretty_print, "    cyan", "<cyan>cyan sample</cyan>")
    show(pretty_print, "   white", "<white>white sample</white>")
    show(pretty_print, " warning", "<warning>warning sample</warning>")
    show(pretty_print, "   error", "<error>error sample</error>")
    show(pretty_print, " success", "<success>success sample</success>")
    show(pretty_print, "    todo", "<todo>todo sample</todo>")
    show(pretty_print, " regular", "<regular>regular/default sample</regular>")

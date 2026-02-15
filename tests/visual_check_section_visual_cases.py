"""General visual check cases for pretty_print tag behavior."""

from typing import Callable

from visual_check_helpers import section, show


def run(pretty_print: Callable[[str], None]) -> None:
    """Run core visual behavior checks."""
    section("Visual Cases")
    print("Expected: each line should render with the described color behavior.")

    show(pretty_print, "plain", "No tags should stay default color.")
    show(pretty_print, "single named tag", "<green>Entire line green</green>")
    show(pretty_print, "multiple named tags", "<green>green</green>, <red>red</red>, <blue>blue</blue>")
    show(pretty_print, "nested tags", "<yellow>yellow <red>red</red> yellow again</yellow>")
    show(pretty_print, "alias tags", "<warning>warning</warning> <error>error</error> <success>success</success>")
    show(pretty_print, "regular reset tag", "<green>green then <regular>default</regular> then green</green>")
    show(pretty_print, "hex lower-case", "<#00bcd4>custom cyan-like</#00bcd4>")
    show(pretty_print, "unknown tag preserved", "<chartreuse>unknown tag text</chartreuse>")
    show(pretty_print, "unclosed tag", "<magenta>magenta started but never closed")
    show(pretty_print, "orphan close tag", "normal then orphan close </red> then normal")
    show(pretty_print, "mixed text", "prefix <cyan>cyan</cyan> middle <#ff8800>orange</#ff8800> suffix")

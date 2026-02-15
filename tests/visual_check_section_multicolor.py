"""Visual checks focused on multiple colors within a single output line."""

from typing import Callable

from visual_check_helpers import section, show


def run(pretty_print: Callable[[str], None]) -> None:
    """Run single-line multi-color rendering checks."""
    section("Multi-Color Single-Line Checks")
    print("Expected: each sample below shows multiple colors within one line.")
    show(
        pretty_print,
        "rainbow words",
        "<red>red</red> <yellow>yellow</yellow> <green>green</green> <cyan>cyan</cyan> <blue>blue</blue> <magenta>magenta</magenta>",
    )
    show(
        pretty_print,
        "alternating segments",
        "A:<warning>warn</warning> B:<success>ok</success> C:<error>bad</error> D:<todo>todo</todo>",
    )
    show(
        pretty_print,
        "named + hex mix",
        "<green>green</green> -> <#00bcd4>hex cyan</#00bcd4> -> <red>red</red> -> <#ff8800>hex orange</#ff8800>",
    )

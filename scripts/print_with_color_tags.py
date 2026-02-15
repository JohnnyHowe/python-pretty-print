import re
from typing import Optional
from .colors import COLORS


TAG_PATTERN = re.compile(r"</?([a-zA-Z0-9_#]+)>")


def print_with_color_tags(text: str) -> None:
    """
    Print text, colouring sections in <color> tags.
    So "<red>Red Text. </red>White (default) Text. <green>Green Text.</green>" would print in those colors.
    """
    stack: list[Optional[str]] = [None]
    output: list[str] = []
    cursor = 0

    for match in TAG_PATTERN.finditer(text):
        output.append(text[cursor:match.start()])

        raw_tag = match.group(0)
        tag_name = match.group(1).lower()
        is_close_tag = raw_tag.startswith("</")

        color = COLORS.get(tag_name)
        if color is None and re.fullmatch(r"#[0-9a-f]{6}", tag_name):
            color = tag_name

        if is_close_tag:
            if len(stack) > 1:
                stack.pop()
            output.append(_color_to_ansi(stack[-1]))
        else:
            if color is None and tag_name not in COLORS:
                output.append(raw_tag)
            else:
                stack.append(color)
                output.append(_color_to_ansi(color))

        cursor = match.end()

    output.append(text[cursor:])
    output.append("\033[0m")
    print("".join(output))


def _color_to_ansi(color: Optional[str]) -> str:
    if not color:
        return "\033[0m"
    color = color.lstrip("#")
    r, g, b = (int(color[i:i+2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m"


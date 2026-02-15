"""Render `<color>...</color>` tags into ANSI foreground color escapes.

Supported tags come from `scripts.colors.COLORS`, for example `<red>`,
`<warning>`, and `<regular>`. Literal hex tags are also supported in the
format `<#rrggbb>`.
"""

import re
from typing import Any
from typing import Optional

from .colors import COLORS


TAG_PATTERN = re.compile(r"</?([a-zA-Z0-9_#]+)>")
HEX_COLOR_PATTERN = re.compile(r"#[0-9a-f]{6}")
ANSI_RESET = "\033[0m"


def print_with_color_tags(*args: object, **kwargs: Any) -> None:
    """Print values with color-tag rendering, mirroring `print` arguments.

    Supports `sep`, `end`, `file`, and `flush` like the built-in `print()`.
    """
    sep = kwargs.pop("sep", " ")
    end = kwargs.pop("end", "\n")

    if sep is None:
        sep = " "
    elif not isinstance(sep, str):
        raise TypeError(f"sep must be None or a string, not {type(sep).__name__}")

    if end is None:
        end = "\n"
    elif not isinstance(end, str):
        raise TypeError(f"end must be None or a string, not {type(end).__name__}")

    text = sep.join(str(arg) for arg in args)
    rendered_text = _render_ansi_text(text)
    print(rendered_text, end=end, **kwargs)


def _render_ansi_text(text: str) -> str:
    """Convert color-tagged text into a single ANSI-escaped string.

    The renderer keeps a color stack so nested tags can restore the parent
    color when a child tag closes.
    """
    active_colors: list[Optional[str]] = [None]
    rendered_parts: list[str] = []
    cursor = 0

    for match in TAG_PATTERN.finditer(text):
        rendered_parts.append(text[cursor:match.start()])

        raw_tag = match.group(0)
        tag_name = match.group(1).lower()

        if raw_tag.startswith("</"):
            _apply_close_tag(active_colors, rendered_parts)
        else:
            _apply_open_tag(tag_name, raw_tag, active_colors, rendered_parts)

        cursor = match.end()

    rendered_parts.append(text[cursor:])
    rendered_parts.append(ANSI_RESET)
    return "".join(rendered_parts)


def _apply_open_tag(
    tag_name: str,
    raw_tag: str,
    active_colors: list[Optional[str]],
    rendered_parts: list[str],
) -> None:
    """Handle an opening tag by pushing a resolved color or preserving text."""
    color = _resolve_tag_color(tag_name)
    if color is None and tag_name not in COLORS:
        rendered_parts.append(raw_tag)
        return

    active_colors.append(color)
    rendered_parts.append(_color_to_ansi(color))


def _apply_close_tag(active_colors: list[Optional[str]], rendered_parts: list[str]) -> None:
    """Handle a closing tag by restoring the previous color in the stack."""
    if len(active_colors) > 1:
        active_colors.pop()
    rendered_parts.append(_color_to_ansi(active_colors[-1]))


def _resolve_tag_color(tag_name: str) -> Optional[str]:
    """Resolve a tag name to a hex color string or `None` for regular/reset."""
    color = COLORS.get(tag_name)
    if color is not None:
        return color
    if HEX_COLOR_PATTERN.fullmatch(tag_name):
        return tag_name
    return None


def _color_to_ansi(color: Optional[str]) -> str:
    """Convert a hex color to an ANSI truecolor sequence, or reset when empty."""
    if not color:
        return ANSI_RESET
    color = color.lstrip("#")
    r, g, b = (int(color[i : i + 2], 16) for i in (0, 2, 4))
    return f"\033[38;2;{r};{g};{b}m"

# python-pretty-print

Lightweight pretty-print helper that renders inline color tags into ANSI truecolor output.

## Install

Install directly from GitHub:

```bash
pip install "python-pretty-print @ git+https://github.com/JohnnyHowe/python-pretty-print.git"
```

Note: this uses a PEP 508 direct reference (`name @ git+url`), so `pip` installs the package as `python-pretty-print` while sourcing it from GitHub.

## Usage

```python
from python_pretty_print import pretty_print

pretty_print("<green>Success</green> and <error>Error</error> in one line.")
pretty_print("Custom hex: <#00bcd4>cyan-ish</#00bcd4>")
```

## Supported tags

Named tags:
- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `warning`
- `error`
- `success`
- `todo`
- `regular` (reset/default color)
- `dull`

Custom hex tags:
- `<#rrggbb>text</#rrggbb>` (lowercase hex format)

Unknown tags are preserved as text.

## Development checks

Run the visual sanity checks:

```bash
python3 -m tests.run_all
```

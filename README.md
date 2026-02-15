# python-pretty-print

Tag-based ANSI pretty printer with color tags.

## Use as a package

Install in your active environment:

```bash
python3 -m pip install.
```

If this repo is embedded as a submodule, install from that path instead:

```bash
python3 -m pip install third_party/python_pretty_print
```

Import and use:

```python
from python_pretty_print import pretty_print

pretty_print("<green>This text is green!</green> <red>This text is red!</red>")
```

## Run examples/tests from repo root

From this repository root:

```bash
python3 -m examples.basic
python3 -m tests.visual_check_pretty_print
```

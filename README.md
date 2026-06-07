# Clues

**Clues investigates Python exceptions and produces human-readable reports with likely causes, supporting clues, confidence, and recommended fixes.**

```python
from clues import investigate

try:
    process_data()
except Exception as exc:
    report = investigate(exc)
    print(report)
```

Example output:

```text
Investigation Report
====================

Likely Cause
------------
The requested file does not exist.

Confidence
----------
95%

Clues
-----
✓ FileNotFoundError detected.
✓ Missing path: data/users.csv

Recommendations
---------------
1. Check that the file path is spelled correctly.
2. Verify your current working directory.
3. Consider using an absolute path while debugging.
```

## Philosophy

Debugging is not about certainty. It is about gathering clues.

Clues does not pretend to magically fix every bug. It surfaces useful evidence and suggests likely next steps.

## Current MVP

Version `0.1.0` includes investigators for:

- `KeyError`
- `FileNotFoundError`
- `ModuleNotFoundError`

## Installation for local development

```bash
python -m venv .venv
.venv\Scripts\python.exe -m pip install -U pip
.venv\Scripts\python.exe -m pip install -e .[dev]
```

On macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .[dev]
```

## Run tests

```bash
.venv\Scripts\python.exe -m pytest
```

On macOS/Linux:

```bash
pytest
```

## Example

```python
from clues import investigate

try:
    user = {"name": "Ada"}
    print(user["email"])
except Exception as exc:
    report = investigate(exc)
    print(report)
```

## Roadmap

- Add `TypeError`, `AttributeError`, `IndexError`, `JSONDecodeError`
- Add traceback-aware investigation
- Add local-variable clues where safe and explicit
- Add framework-specific investigators: Pandas, SQLAlchemy, FastAPI
- Add CLI: `clues traceback.txt`
- Add plugin system for custom investigators

## License

MIT License.

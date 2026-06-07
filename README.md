# 🕵️ Clues

![Tests](https://img.shields.io/badge/tests-25%20passing-brightgreen.svg)
![Investigators](https://img.shields.io/badge/investigators-25-purple.svg)
![Status](https://img.shields.io/badge/status-v0.1.0--alpha-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Human-readable Python exception investigations.**

Clues transforms Python exceptions into structured investigation reports containing:

* 🔎 Likely cause
* 🧩 Supporting clues
* 📊 Confidence score
* 💡 Practical recommendations

Instead of reading a raw traceback, Clues helps developers understand **what probably happened and what to do next.**

---

## Philosophy

Debugging is rarely about certainty.

It is about collecting evidence.

Clues does not claim to know the answer. It investigates the exception and surfaces the strongest clues.

---

## Example

```python
from clues import investigate

try:
    {}["user_id"]
except Exception as exc:
    report = investigate(exc)
    print(report)
```

Output:

```text
Investigation Report
====================

Likely Cause
------------
A dictionary-like object does not contain the key 'user_id'.

Confidence
----------
95%

Clues
-----
✓ KeyError detected.
✓ Missing key: 'user_id'.

Recommendations
---------------
1. Print or inspect the available keys with data.keys().
2. Check whether the key name is misspelled.
3. Use data.get(key) when the key is optional.
4. Verify that upstream data contains the expected field.
```

---

## Current Investigators

### Core Python

* ✅ KeyError
* ✅ FileNotFoundError
* ✅ ModuleNotFoundError
* ✅ ImportError
* ✅ IndexError
* ✅ AttributeError
* ✅ TypeError
* ✅ ValueError
* ✅ NameError
* ✅ ZeroDivisionError
* ✅ PermissionError
* ✅ JSONDecodeError
* ✅ UnicodeDecodeError
* ✅ NotImplementedError

---

## Installation

```bash
pip install clues
```

Or directly from GitHub:

```bash
pip install git+https://github.com/MinervaRose/clues.git
```

---

## Roadmap

### v0.1.0-alpha

* Core Python exception investigators
* Human-readable reports
* Automated test suite

### v1.0

* 25 investigators
* Data science investigators
* AI/ML investigators
* Improved report formatting

### v2.0

Runtime-aware investigations:

```python
report = investigate(
    exc,
    locals=locals()
)
```

### v3.0

Plugin architecture:

```python
@clues.investigator
class CustomInvestigator:
    ...
```

### v4.0

Optional AI-assisted investigations for unknown exceptions.

---

## Project Goals

Clues is designed to support:

* Python learners
* Students
* Bootcamps
* Mentors
* Educators
* Developers who want more human-readable debugging

---

## Contributing

New investigators are welcome.

Every investigator should provide:

* likely cause
* supporting clues
* confidence score
* practical recommendations

---

## License

MIT License.

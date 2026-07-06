# neo-demo

A deliberately tiny Python library whose job is to be a real consumer of the
[neo](https://github.com/psumiya/neo) autonomous coding harness. Feature requests are filed as
GitHub issues with the `neo:build` label; the harness produces the tested, risk-gated PR.

The app itself: `neo_demo` exposes small text utilities (`slugify`, `word_count`, `truncate`).

- Build: `pip install -e '.[dev]'`
- Test: `pytest`

The neo wiring lives in `.neo/` and `.github/workflows/neo.yml` (see the neo README for how the
pipeline works).

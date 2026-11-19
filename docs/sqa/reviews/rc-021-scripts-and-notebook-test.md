# Review Record: Scripts and notebook test against QC-PY-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-021 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [8955974] |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Criterion 3 records the explained `# nosemgrep` suppression that the pull request check made necessary; verdict stays Go | pending |

---

## Artifact Under Review

- Instance reviewed: `scripts/make_screenshots.py` and `tests/integration/test_notebook.py` (type PY), the notebook and the README of [MIL-004]
- Checklist used: [QC-PY-001]; the README has no checklist, so it is checked against the Go/No-Go criteria of [MIL-004] and by `check-readme.sh`
- Scope: full review
- Language and domain: n/a (source code)
- Language reviewer: none
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Pass | `snake_case` functions and modules, `UPPER_SNAKE` constants, `PascalCase` for the dataclass `Step`. |
| 2 | Pass | Names state purpose (`run_in_container`, `render`, `load_font`); no unexplained abbreviation. |
| 3 | Pass | `ruff format --check` and `ruff check` pass on `src tests scripts`. One suppression exists, `# nosemgrep` on the `subprocess.run` call of `run_in_container`: the pull request check flagged a non-static command list, but every command is a constant of `STEPS` in the same file and no outside input reaches the call; the comment above the call says so. |
| 4 | Pass | All signatures are annotated; `mypy --strict` passes on 22 files. One override in `pyproject.toml` allows an untyped call in `test_notebook.py` because `nbformat.read` has no type hints; it is commented. |
| 5 | Pass | No bare `except`; `load_font` catches `OSError` only to try the next font and ends with `SystemExit` and a message when none is found. |
| 6 | Pass | No default argument and no shadowed builtin. |
| 7 | Pass | The script writes files with `Path.write_text` and `Image.save`; no handle stays open. |
| 8 | Pass | The module, `Step` and every function have a docstring that says what, not how. |
| 9 | Pass | `print` reports to the user which image was written (the output of a command-line script); no secret or personal data; the script never reads `.env`. |
| 10 | N-A | `scripts/` and the notebook test are tooling tasks without a class in [DCD-001]; they call only the public names `text_to_morse`, `MORSE_CODE_DICT` and `python -m morse_converter`. |
| 11 | Pass | `test_notebook.py` runs the notebook headlessly and checks three of its outputs; it needs no GUI and no network. The script itself is exercised by running it (the four images and `results/*.txt`). |
| 12 | Pass | Strict mode passes; `Any` is not used. |
| 13 | Pass | Pillow, nbclient and nbformat are development extras in `pyproject.toml` and all are used; the runtime dependencies stay empty. |
| 14 | Pass | The steps and their commands are written once in `STEPS`; the notebook calls the same public names. |
| 15 | Pass | The script and the test import the package from outside; no layer imports them. |
| 16 | Pass | `Step` holds data; `run_in_container`, `render` and `main` each do one thing. |
| 17 | Pass | The script is in `scripts/` and the test in `tests/integration/`, as the layout of the plan says. |
| 18 | Pass | The names are English, `snake_case`, without space; the notebook name `Text_to_Morse_Code_Converter.ipynb` has no space and no character outside the allowed set. |

## Go / No-Go Criteria of MIL-004

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Pass | `python -m jupyter nbconvert --to notebook --execute notebooks/Text_to_Morse_Code_Converter.ipynb` exits 0; the test `test_notebook_runs_from_top_to_bottom` passes. |
| 2 | Pass | `docs/images/` holds `step-1-the-road.png`, `step-2-morse-table.png`, `step-3-convert-text.png` and `step-4-command-line.png`, written by `scripts/make_screenshots.py`. |
| 3 | Pass | All four images are drawn from the output of the program run in a `python:3.13-slim` container; no image of the lecture or the course platform exists in the repository. |
| 4 | Pass | `bash framework/scripts/check-readme.sh` exits 0. |
| 5 | Pass | The README documents `.venv`, `python -m pip install --upgrade pip`, running the program, the tests and `doxygen Doxyfile`. |
| 6 | Pass | `bash scripts/scan.sh`: 187 rules, 0 findings. |
| 7 | Pass | `python -m pytest`: 39 passed. |

## Overall Verdict

Go: no criterion fails; criterion 10 of the checklist is not applicable.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[MIL-004]: ../../milestones/mil-004-notebook-and-readme.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[DCD-001]: ../../dcd.md
[8955974]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/89559746d1d33c8f30d9a1e2fc3b7737ccfa5abd

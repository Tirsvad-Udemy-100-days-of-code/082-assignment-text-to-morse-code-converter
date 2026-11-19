# Review Record: Python source code against QC-PY-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-020 |
| CrossReference | [DCD-001], [ADR-0001], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [8261e67] |

---

## Artifact Under Review

- Instance reviewed: `src/morse_converter/` (type PY, 20 files with the tests), realising [DCD-001]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a (source code)
- Language reviewer: none
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Pass | Modules, functions, variables and constants use `snake_case` and `UPPER_SNAKE`; the one class `UnsupportedCharacterError` uses `PascalCase`. |
| 2 | Pass | Names come from [DICT-001] (`char`, `code` in `signal_pattern_for`, `text`, `word`, `morse`); no unexplained abbreviation and no single-letter name is used. |
| 3 | Pass | `ruff format --check src tests` reports 20 files formatted and `ruff check src tests` reports no finding; no suppression comment exists. |
| 4 | Pass | Every function and method has annotated parameters and return type; `mypy --strict` passes (criterion 12). |
| 5 | Pass | The only `except` clause is `except KeyError as err` in `signal_pattern_for`, which raises `UnsupportedCharacterError(char) from err`; the command catches the narrow `UnsupportedCharacterError` and returns `EXIT_ERROR`; nothing is swallowed. |
| 6 | Pass | No default argument and no shadowed builtin (the parameter is `char`, not `chr`; `text` and `word` are not builtins). |
| 7 | N-A | The program opens no file, lock or connection. |
| 8 | Pass | Every module, class and function has a Doxygen docstring that says what it does; `doxygen Doxyfile` reports 0 warnings (warnings are errors in the `Doxyfile`). |
| 9 | Pass | `print` appears only in `ConvertTextCommand.run`, where it is the program's output (the `morse` on the output stream, the error message on the error stream), not diagnostics; the program logs nothing and holds no secret or personal data. |
| 10 | Pass | Every function traces to a method of [DCD-001] (table below); the extra `__init__` export of `text_to_morse` and `MORSE_CODE_DICT` and `__main__.py` are stated in [DCD-001] and [MIL-003]. No deviation. |
| 11 | Pass | 38 tests in `tests/unit` and `tests/integration` pass, one behaviour per test, named for the behaviour; none depends on order or the network; the postconditions and the exception of [OC-001] and the flows of [UC-001] are covered. |
| 12 | Pass | `mypy` in strict mode (`pyproject.toml`) reports no issue in 20 files; `Any` is not used. |
| 13 | Pass | `dependencies` is empty; development tools are in the `dev` extra and all are used. |
| 14 | Pass | The Morse table is defined once in `domain/constants.py`, the separators once, the command line texts once in `presentation/constants.py`; the error message of the Domain and the text of the command line are worded differently on purpose, because they answer different readers. |
| 15 | Pass | Imports point inward: Domain imports no other layer, Application imports the Domain only, Presentation imports Application and Domain; no cycle (the tests import and run). |
| 16 | Pass | Each module has one reason to change; no type test chain; the exception honours the contract of `ValueError`. |
| 17 | Pass | `src/morse_converter/{domain,application,presentation}` and `tests/{unit,integration}`, all `snake_case`; no Infrastructure layer exists because the design has none ([DCD-001], Dependency Check); there is no `e2e` folder because the integration tests already run the whole program as a subprocess and the program has no user interface beyond the command line. |
| 18 | Pass | All file and folder names are English, without space, in `snake_case` with `.py`. |

## Method Traceability

| Code | Method of [DCD-001] |
| --- | --- |
| `presentation/commands/convert_text_command.py` `run(arguments: Sequence[str]) -> int` | `ConvertTextCommand.run` |
| `presentation/commands/convert_text_command.py` `read_text(arguments: Sequence[str]) -> str` | `ConvertTextCommand.read_text` |
| `presentation/commands/convert_text_command.py` `main() -> int` | `ConvertTextCommand.main` |
| `presentation/constants.py` `PROMPT_TEXT`, `ERROR_MESSAGE`, `EXIT_OK`, `EXIT_ERROR` | `PresentationConstants` |
| `application/use_cases/text_to_morse.py` `text_to_morse(text: str) -> str` | `TextToMorseUseCase.text_to_morse` |
| `domain/morse_table.py` `signal_pattern_for(char: str) -> str` | `MorseTable.signal_pattern_for` |
| `domain/constants.py` `MORSE_CODE_DICT`, `LETTER_SEPARATOR`, `WORD_SEPARATOR` | `DomainConstants` |
| `domain/errors/unsupported_character_error.py` `UnsupportedCharacterError.__init__(char: str)` | `UnsupportedCharacterError.__init__` |

All 6 classes and 6 methods of the design exist, and no function exists that the design does not name.

## Overall Verdict

Go: 17 criteria pass, 1 is not applicable, none fails.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DCD-001]: ../../dcd.md
[ADR-0001]: ../../adr/adr-0001-unsupported-characters-are-rejected.md
[MIL-003]: ../../milestones/mil-003-converter.md
[OC-001]: ../../use-cases/uc-001/oc.md
[UC-001]: ../../use-cases/uc-001/uc.md
[DICT-001]: ../../dictionary.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[8261e67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/8261e6760bce4babfd8e112dde2d55291b47ba53

# MIL-003 Converter

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [US-001], [MIL-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-006: Go | [ba98d67] |

---

## Purpose

Decides whether the converter works, is tested and follows the design: the Morse table, `text_to_morse` and the command-line program, written only from [UC-001], [SD-001] and [DCD-001].

## Deliverable

The package `src/morse_converter` with the layers `domain`, `application` and `presentation` as [DCD-001] draws them, the unit and integration tests, and the review record of the code. Each function traces to a method of [DCD-001]; code that is not in the design is not written.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `text_to_morse("SOS")` returns `... --- ...` and `text_to_morse("Hello World")` returns `.... . .-.. .-.. --- / .-- --- .-. .-.. -..` | Both equal | Any difference |
| 2 | `python -m morse_converter "SOS"` prints `... --- ...` and exits with 0 | Equal | Any difference |
| 3 | A text with an unsupported character is rejected with a message that names the character, a non-zero exit code and no Morse code on the standard output | Rejected | Dropped, replaced or a traceback |
| 4 | `python -m pytest` | Exit code 0, all tests pass | Any failure |
| 5 | Every function in `src/` appears in the method traceability table of [DCD-001] and the tests cover every postcondition and the exception of [OC-001] | 100 % | Any function or postcondition not covered |
| 6 | `ruff check`, `ruff format --check` and `mypy --strict` | Exit code 0 | Any finding |
| 7 | `doxygen Doxyfile` | 0 warnings | Any warning |
| 8 | The code is reviewed against `qc-programming-python.md` and the review record says `Go` | `Go` | `No-Go` |
| 9 | `bash scripts/scan.sh` (opengrep) | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The code follows the accepted design |
| [MIL-002] | The configuration and the scan script |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 1 to 4 and 8, success criteria 1, 2, 7 and 8; story [US-001] | CN-001, CN-004 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-20 — inside the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Define the Morse table in domain constants | Create `domain/constants.py` with `MORSE_CODE_DICT` (A to Z, 0 to 9 and the punctuation of the business rule), `LETTER_SEPARATOR` and `WORD_SEPARATOR`, as the class `DomainConstants` of the design. | Yes | [UC-001], [DCD-001] |
| 2 | Implement the unsupported character error | Create `UnsupportedCharacterError` (a `ValueError` that holds the character), the `create(char)` message of the sequence, as [ADR-0001] decides. | Yes | [OC-001], [SD-001], [ADR-0001] |
| 3 | Implement MorseTable | Create `signal_pattern_for(char)` in the Domain: the code of a character (upper and lower case alike), or `UnsupportedCharacterError`. | Yes | [SD-001], [DCD-001] |
| 4 | Implement text_to_morse | Create the use case `text_to_morse(text)` in the Application: split into words, join the codes of a word with one space and the words with ` / `; export it and `MORSE_CODE_DICT` from the package. | Yes | [UC-001], [OC-001], [SD-001], [DCD-001] |
| 5 | Implement the command | Create `ConvertTextCommand` (`run`, `read_text`, `main`) and its constants in the Presentation, and `__main__.py`, so `python -m morse_converter` takes the text from the arguments or a prompt and exits with 0 or 1. | Yes | [UC-001], [SD-001], [DCD-001] |
| 6 | Write unit tests | Test the table, `signal_pattern_for`, `text_to_morse` (every postcondition and the exception of the contract) and the error, with pytest. | Yes | [OC-001] |
| 7 | Write integration tests | Run `python -m morse_converter` as a subprocess for the main scenario, the empty text, the prompt and the exception flow 2a of the use case. | Yes | [UC-001] |
| 8 | Add Doxygen comments and build the documentation | Every module, class and function has a Doxygen comment; `doxygen Doxyfile` reports no warning. | No | |
| 9 | Lint and type-check | `ruff` and `mypy --strict` pass on `src/` and `tests/`. | No | |
| 10 | Review the code against the Python checklist | Review against `qc-programming-python.md`, check the method traceability of [DCD-001] and record the result as an `RC-*` before the pull request. | No | |

---

[ADR-0001]: ../adr/adr-0001-unsupported-characters-are-rejected.md
[BC-001]: ../business-case.md
[DCD-001]: ../dcd.md
[MIL-001]: ./mil-001-use-case-and-design.md
[MIL-002]: ./mil-002-foundation.md
[OC-001]: ../use-cases/uc-001/oc.md
[SD-001]: ../use-cases/uc-001/sd.md
[UC-001]: ../use-cases/uc-001/uc.md
[US-001]: ../user-stories.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

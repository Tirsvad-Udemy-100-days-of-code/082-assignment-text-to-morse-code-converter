# ADR-0001 Unsupported characters are rejected

## Metadata
| Key | Value |
| --- | --- |
| ID | ADR-0001 |
| CrossReference | [UC-001], [OC-001], [SD-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-018: Go | pending |

---

## Context

A text may hold a character that has no Morse code (for example `#`, `é` or an emoji). The assignment does not say what the converter must do. Three options exist: skip the character (the solutions that fellow participants share do this), replace it by a marker such as `?`, or reject the text. Skipping loses information without telling the user and can change the meaning of a message. A marker mixes a real Morse code (`..--..` is the question mark) with an error sign, so the result cannot be told from a correct one. The forces are correctness (S01), a result that S02 can trust, and a simple use case.

## Decision

The converter rejects the whole text with an `UnsupportedCharacterError` that names the first unsupported character; it never skips or replaces a character and gives no partial Morse code.

## Consequences

**Positive:**

- The user always knows whether the Morse code is complete.
- The behaviour is easy to test: one error, one named character.
- The error is specific, so callers do not need to catch every `ValueError`.

**Negative:**

- A text with one unsupported character gives no Morse code at all, which is stricter than the solutions that S02 shares.
- A user who wants to skip unsupported characters must remove them first.

## Affected Artifacts

- [UC-001] — extension 2a and the business rule for step 2a follow this decision
- [OC-001] — the exception of `convertTextToMorse`
- [SD-001] — the `create(char)` message

---

[UC-001]: ../use-cases/uc-001/uc.md
[OC-001]: ../use-cases/uc-001/oc.md
[SD-001]: ../use-cases/uc-001/sd.md

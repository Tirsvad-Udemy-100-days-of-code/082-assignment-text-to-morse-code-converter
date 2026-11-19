# Operation Contract

## Metadata
| Key | Value |
| --- | --- |
| ID | OC-001 |
| CrossReference | [SSD-001], [DM-001], [SD-001], [DICT-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-015: Go | pending |

---

## Contract: convertTextToMorse

| Item | Value |
| --- | --- |
| Operation | `convertTextToMorse(text: str): str` |
| Traces to | message 1 `convertTextToMorse` in [SSD-001] |
| Domain Model concepts | `text`, `word`, `char`, `code`, `morse`; associations "is made of", "is spelled with", "is represented by", "is written with", "is translated into" ([DM-001]) |

**Preconditions**

- A `text` exists; it may be empty.

**Postconditions**

- A `morse` instance was created.
- `morse` was associated with `text` ("is translated into").
- For each `char` of each `word` of `text`, `morse` was associated with the `code` that represents the `char` ("is written with").
- `morse.notation` was set to the `code` values in the order of the `chars`, the `codes` of one `word` separated by one space and the `words` separated by ` / `, with no leading and no trailing space; it is empty when `text` has no `word`.

**Exceptions**

| Condition (failing precondition) | Outcome |
| --- | --- |
| A `char` of `text` has no `code` (the `char` is not a letter, a digit or one of the supported punctuation marks) | No `morse` instance was created, nothing was associated, and an `UnsupportedCharacterError` that names the `char` was signalled ([ADR-0001]) |

---

[SSD-001]: ./ssd.md
[DM-001]: ../../domain-model.md
[SD-001]: ./sd.md
[DICT-001]: ../../dictionary.md
[ADR-0001]: ../../adr/adr-0001-unsupported-characters-are-rejected.md

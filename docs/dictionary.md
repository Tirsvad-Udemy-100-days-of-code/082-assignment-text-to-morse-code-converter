# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001], [DM-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-013: Go | [ba98d67] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional IT term. PO language: English (`en`); domain: IT (`it`). The dictionary covers every concept of [DM-001] and the actor of [UCD-001].

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Character | en | `char` | One letter, digit or punctuation mark of a Word; in the code, a string of length one | DM, UC, US | OC, SD, DCD |
| Converter User | en | `caller` | The person who runs the program and gives it a Text | UCD, UC, US, SSD | SD |
| Morse Code | en | `morse` | The Text written as Signal Patterns; in the code, a string | DM, UC, US | OC, SD, DCD |
| Signal Pattern | en | `code` | The dots and dashes of one Character; in the code, a string of `.` and `-` | DM, UC, US | OC, SD, DCD |
| Text | en | `text` | The words a Converter User wants to send; in the code, a string | DM, UC, US | OC, SD, DCD |
| Word | en | `word` | A group of Characters between two spaces of a Text | DM, UC, US | OC, SD |

## Rules

- The Domain Model, use cases and user stories use the PO term; the Operation Contract, Sequence Diagram, Design Class Diagram and ERD use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- Rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language), so a term is found without searching.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[DM-001]: ./domain-model.md
[UCD-001]: ./use-case-diagram.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

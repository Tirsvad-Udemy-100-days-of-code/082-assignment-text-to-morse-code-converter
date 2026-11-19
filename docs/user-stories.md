# User Stories

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [BC-001], [UCD-001], [UC-001], [MIL-003] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-009: Go | pending |

---

## Purpose and Scope

This document holds the candidate user story of the Text-to-Morse-Code converter. It covers the epic "convert a text into Morse code" of the Day 82 assignment, delivered by [MIL-003] and traced to the objectives 1 to 4 of [BC-001].

## Story List

### US-001.01 — Convert a text into Morse code

- **Statement:** **As a** Converter User (S01, S02), **I want** to convert a text into Morse code, **so that** I can read or send the text as dots and dashes.
- **Acceptance Criteria:**
  - Given the text `SOS`, when the user converts it, then the Morse code is `... --- ...`.
  - Given the text `Hello World`, when the user converts it, then the Morse code is `.... . .-.. .-.. --- / .-- --- .-. .-.. -..` (the characters of a word are separated by one space and the words by ` / `).
  - Given the text `sos` in lower case, when the user converts it, then the Morse code equals the one of `SOS`.
  - Given a text with a character that has no Morse code (for example `#`), when the user converts it, then the user is told which character is not supported and gets no Morse code.
  - Given an empty text, when the user converts it, then the Morse code is empty.
- **Traces to:** [UC-001]; epic [MIL-003].
- **Priority (MoSCoW):** Must — it is the whole assignment.
- **Size:** fits one iteration.

## INVEST Check

Independent (the only story), Negotiable (the punctuation set and the separators are open to S01), Valuable (the assignment's goal), Estimable, Small (one use case, one operation), Testable (every acceptance criterion is a given/when/then). No exception.

---

[BC-001]: ./business-case.md
[UCD-001]: ./use-case-diagram.md
[UC-001]: ./use-cases/uc-001/uc.md
[MIL-003]: ./milestones/mil-003-converter.md

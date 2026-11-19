# UC-001 Convert Text to Morse Code

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001], [DM-001], [SSD-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-011: Go | pending |

---

**Format:** Fully Dressed

## Fully Dressed

- **Scope:** Morse converter system
- **Level:** user-goal
- **Primary Actor:** Converter User, as named in [UCD-001]
- **Stakeholders and Interests:**
  - S01 — gets a correct, finished assignment that is worth sharing
  - S02 — runs the converter and compares it with their own; expects the assignment's function name
  - S03 — browses the repository; expects it to explain itself and to need no dependency
- **Preconditions:** The Converter User has a Text.
- **Postconditions (success guarantee):** The Converter User has the Morse Code of the Text. Nothing is stored.

### Main Success Scenario

1. The Converter User gives a Text to the system.
2. The system checks that every Character of the Text has a Signal Pattern.
3. The system builds the Morse Code: the Signal Patterns of the Characters of a Word follow each other, separated by one space, and the Words are separated by ` / `.
4. The system gives the Morse Code to the Converter User.

### Extensions (Alternative / Exception Flows)

- 2a. A Character of the Text has no Signal Pattern:
  1. The system tells the Converter User which Character is not supported.
  2. The system gives no Morse Code, and the use case ends without success.
- 1a. The Text is empty or holds only spaces:
  1. The system gives an empty Morse Code, and the use case ends with success.

### Special Requirements / Business Rules

| Step | Rule |
| --- | --- |
| 2 | The Signal Patterns are those of International Morse code: the letters A to Z, the digits 0 to 9 and the punctuation marks `. , ? ' ! / ( ) & : ; = + - _ " $ @` |
| 2 | Upper case and lower case letters have the same Signal Pattern |
| 2a | A Text with an unsupported Character is rejected as a whole; a Character is never skipped or replaced silently (decision [ADR-0001]) |
| 3 | A run of spaces, tabs or line breaks between Words counts as one Word separator; spaces at the start and the end of the Text are ignored |
| 3 | The Morse Code has no trailing space and no leading space |

### Open Issues

None.

---

[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md
[SA-001]: ../../stakeholder-analysis.md
[DM-001]: ../../domain-model.md
[SSD-001]: ./ssd.md
[ADR-0001]: ../../adr/adr-0001-unsupported-characters-are-rejected.md

# Review Record: UCD-001 against QC-UCD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [UCD-001], [QC-UCD-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | pending |

---

## Artifact Under Review

- Instance reviewed: [UCD-001]
- Checklist used: [QC-UCD-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Actors are defined with correct UML stereotypes (e.g. `<<System>>`, `<<Actor>>`) | Pass | The actor has `<<Actor>>` and the boundary has `<<System>>` in the diagram and the Actor Table. |
| 2 | System boundary is clearly drawn and labeled | Pass | The rectangle "Morse Converter" is drawn and labelled as the system boundary. |
| 3 | Include/extend relationships are used correctly per UML 2.5.1, not as generic "uses" arrows | N-A | The system has one use case, so no include or extend relationship is used. |
| 4 | Every actor participates in at least one use case (no orphan actors) | Pass | The actor Converter User takes part in the use case Convert Text to Morse Code. |
| 5 | Diagram is traceable to a documented stakeholder need | Pass | The Actor Table maps the actor to S01 and S02 of [SA-001]. |
| 6 | Use case names are verb phrases describing actor goals, not internal system operations | Pass | "Convert Text to Morse Code" is a verb phrase that states the actor's goal. |
| 7 | Diagram is free of implementation detail (e.g. UI widgets, database tables) | Pass | The diagram shows no screen, command or file. |
| 8 | Actor and use case naming is consistent with corresponding Use Case and User Story documents | Pass | The actor and the use case have the same names in [UC-001] and [US-001]. |
| 9 | Each use case lists the user story it comes from and its priority (MoSCoW) with a reason | Pass | The Use Case Table gives the source story [US-001] and the priority Must with a reason. |
| 10 | When there is more than one primary actor, a role matrix (use case by role) is present and marked as a suggestion for the Product Owner to approve | N-A | There is one primary actor, so no role matrix is needed; the document says so. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table of UCD-001 has `Language | en` and `Domain | it`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `it` is a row of the domain list of `docs/artifact-registry.md`. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only IDs, file names, commands and code names are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Professional English` for this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The PO terms Text, Word, Character, Signal Pattern, Morse Code and Converter User are used as [DICT-001] gives them, with no synonym. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | This is the first version, so there is no earlier language or domain to compare; the Version History row records it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer reads English and knows the IT domain and checked the terms against the dictionary [DICT-001]; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out where first used (Product Owner, SQA, QC, CI) or are established names (README, Doxygen, pytest). |

## Overall Verdict

Go — every Mandatory criterion of [QC-UCD-001] and [QC-LANG-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DICT-001]: ../../dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-UCD-001]: ../../../framework/qc/artifacts/qc-use-case-diagram.md
[SA-001]: ../../stakeholder-analysis.md
[UC-001]: ../../use-cases/uc-001/uc.md
[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md

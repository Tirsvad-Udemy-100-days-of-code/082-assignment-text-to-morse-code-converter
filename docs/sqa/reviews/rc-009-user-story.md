# Review Record: US-001 against QC-US-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [US-001], [QC-US-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [ba98d67] |

---

## Artifact Under Review

- Instance reviewed: [US-001]
- Checklist used: [QC-US-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Follows INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) | Pass | The INVEST Check confirms all six properties with no exception: one story, one use case, five given/when/then criteria. |
| 2 | Written in "As a / I want / So that" form | Pass | US-001.01 is written as "As a Converter User, I want to convert a text into Morse code, so that I can read or send it as dots and dashes". |
| 3 | Clear, testable acceptance criteria are included | Pass | Five acceptance criteria are given in given/when/then form, with exact expected values. |
| 4 | Traceable to a use case or epic | Pass | The story traces to [UC-001] and to the epic [MIL-003]. |
| 5 | Story is sized to fit within a single iteration | Pass | The story fits one iteration: one use case with one operation. |
| 6 | Story statement avoids technical implementation detail | Pass | The statement names no technology: no function, file or command. |
| 7 | Role named in the story matches an actor defined in the Use Case Diagram | Pass | The role "Converter User" is the actor of [UCD-001]. |
| 8 | A story with more than one actor goal is split into use cases, one per actor goal, and each use case names the story it comes from | Pass | The story has one actor goal, so it is not split; it has one use case, [UC-001], which names it as its source. |
| 9 | The story has a priority (MoSCoW: Must, Should, Could, Won't now) with the reason beside it | Pass | The story has the priority Must with a reason (it is the whole assignment). |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table of US-001 has `Language | en` and `Domain | it`; neither is a placeholder. |
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

Go — every Mandatory criterion of [QC-US-001] and [QC-LANG-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DICT-001]: ../../dictionary.md
[MIL-003]: ../../milestones/mil-003-converter.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-US-001]: ../../../framework/qc/artifacts/qc-user-story.md
[UC-001]: ../../use-cases/uc-001/uc.md
[UCD-001]: ../../use-case-diagram.md
[US-001]: ../../user-stories.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

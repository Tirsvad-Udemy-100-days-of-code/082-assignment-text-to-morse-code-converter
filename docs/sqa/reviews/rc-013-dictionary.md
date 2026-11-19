# Review Record: DICT-001 against QC-DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [ba98d67] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | Each of the six rows has a PO term, the language `en`, an IT term and a definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Each PO term has one IT term and the reverse; no synonym exists. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | Pass | Every concept of [DM-001] (Text, Word, Character, Signal Pattern, Morse Code) has a row, and [DM-001] uses the PO term. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | Pass | [OC-001], [SD-001] and [DCD-001] use `text`, `word`, `char`, `code`, `morse` and `caller`, not the PO terms. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Each definition is one sentence in English. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | The columns name the types DM, UC, US, UCD, SSD, OC, SD and DCD, which all exist in the project. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | The `Language` row is `en` and the `Domain` row is `it`, as in the registry; every row is English. |
| 8 | The dictionary rows are in ascending order of the PO term (case-insensitive, by the alphabet of the PO language) | Pass | The rows run in ascending order: Character, Converter User, Morse Code, Signal Pattern, Text, Word. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table of DICT-001 has `Language | en` and `Domain | it`; neither is a placeholder. |
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

Go — every Mandatory criterion of [QC-DICT-001] and [QC-LANG-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DCD-001]: ../../dcd.md
[DICT-001]: ../../dictionary.md
[DM-001]: ../../domain-model.md
[OC-001]: ../../use-cases/uc-001/oc.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[SD-001]: ../../use-cases/uc-001/sd.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

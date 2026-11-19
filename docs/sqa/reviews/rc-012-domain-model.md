# Review Record: DM-001 against QC-DM-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [DM-001], [QC-DM-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [ba98d67] |

---

## Artifact Under Review

- Instance reviewed: [DM-001]
- Checklist used: [QC-DM-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Uses ubiquitous/business language throughout; no technical or implementation jargon (e.g. no "table", "class", "pointer") | Pass | The concepts are Text, Word, Character, Signal Pattern and Morse Code; no technical word is used. |
| 2 | Multiplicities on associations are correct and complete (e.g. `1..*`, `0..1`) | Pass | Every association has a multiplicity at both ends in the diagram and the Association Table. |
| 3 | No operation/method signatures shown — attributes and associations only | Pass | The diagram shows attributes and associations only, with no operation. |
| 4 | Associations are named with an unambiguous reading direction | Pass | Each association has a name with a reading direction (`is made of >`). |
| 5 | Generalization/specialization used correctly, reflecting true "is-a" relationships, not misused for code reuse | N-A | There is no generalization. |
| 6 | Every concept traces to a noun phrase found in the use cases or glossary | Pass | Every concept has a source noun phrase in [UC-001] in the Concept Table. |
| 7 | Attributes are simple domain data (no foreign-key-like references or object pointers modeled as attributes) | Pass | The attributes (content, spelling, symbol, signals, notation) are simple domain data; no attribute is a reference. |
| 8 | The Purpose names the concerns (`CN-NNN`) the Domain Model answers and the stakeholders it serves, so its viewpoint is stated | Pass | The Purpose names the concern CN-001 of [SA-001] and the stakeholders served. |
| 9 | No technical solution names: only conceptual classes of the Product Owner's world, never a file, an environment variable, a setting source, a database, a table, an API, a service, a cache or any other mechanism | Pass | No file, setting, database, table, API or other mechanism is a concept; the Morse table is a set of Signal Patterns, not a concept. |
| 10 | No empty concept: every concept has at least one attribute and at least one association | Pass | Each concept has one attribute and at least one association. |
| 11 | A Domain Model written for one use case reuses the concepts, attributes, associations and names of the project Domain Model, and its additions and changes are added to the project Domain Model | Pass | This is the first use case and the first model, so the document is the project Domain Model; no other model exists to reuse. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table of DM-001 has `Language | en` and `Domain | it`; neither is a placeholder. |
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

Go — every Mandatory criterion of [QC-DM-001] and [QC-LANG-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DICT-001]: ../../dictionary.md
[DM-001]: ../../domain-model.md
[QC-DM-001]: ../../../framework/qc/artifacts/qc-domain-model.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[SA-001]: ../../stakeholder-analysis.md
[UC-001]: ../../use-cases/uc-001/uc.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

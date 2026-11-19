# Review Record: SSD-001 against QC-SSD-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-014 |
| CrossReference | [SSD-001], [QC-SSD-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial review record; verdict Go (autonomous, not independent) | [ba98d67] |

---

## Artifact Under Review

- Instance reviewed: [SSD-001]
- Checklist used: [QC-SSD-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Input/output messages match the corresponding Use Case's main success scenario step-for-step | Pass | The one message `convertTextToMorse` covers steps 1 to 4 of the main success scenario; the table justifies why one message covers four steps. |
| 2 | Actor and System are treated strictly as black boxes (system shown as `:System`) | Pass | The system is shown only as `:System`; no internal object appears. |
| 3 | Object creation/destruction of the System instance handled explicitly where relevant | Pass | The Lifecycle Notes say the system has no state between two calls. |
| 4 | Return values are shown for operations that produce one, using dashed return arrows | Pass | The diagram has a dashed return arrow `morse`. |
| 5 | Alternate/exceptional flows are represented separately (or explicitly out of scope noted) | Pass | The exception flow 2a is not drawn as a second diagram; the Source Use Case section says it is a failure of the same operation and is described in [OC-001]. |
| 6 | Message names are verb phrases consistent with the use case's system responsibilities | Pass | `convertTextToMorse` is a verb phrase and is the system's responsibility in [UC-001]. |
| 7 | Diagram references the specific Use Case (name and ID) it depicts | Pass | The Source Use Case section names [UC-001] and its main success scenario. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table of SSD-001 has `Language | en` and `Domain | it`; neither is a placeholder. |
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

Go — every Mandatory criterion of [QC-SSD-001] and [QC-LANG-001] passes or does not apply; the document is Accepted. Full review.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | | |

---

[DICT-001]: ../../dictionary.md
[OC-001]: ../../use-cases/uc-001/oc.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[QC-SSD-001]: ../../../framework/qc/artifacts/qc-ssd.md
[SSD-001]: ../../use-cases/uc-001/ssd.md
[UC-001]: ../../use-cases/uc-001/uc.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

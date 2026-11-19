# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's cross-artifact traceability success criterion is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [UCD-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [DCD-001] | [RC-002] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-003] |
| [MIL-001] | MIL | en | it | [PP-001], [BC-001] | [MIL-003] | [RC-004] |
| [MIL-002] | MIL | en | it | [PP-001], [BC-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [MIL-001], [MIL-002] | [MIL-004] | [RC-006] |
| [MIL-004] | MIL | en | it | [MIL-003] | [MIL-005] | [RC-007] |
| [MIL-005] | MIL | en | it | [MIL-004] | - | [RC-008] |
| [US-001] | US | en | it | [BC-001] | [UC-001] | [RC-009] |
| [UCD-001] | UCD | en | it | [BC-001], [SA-001], [US-001] | [UC-001] | [RC-010] |
| [UC-001] | UC | en | it | [UCD-001], [US-001] | [DM-001], [SSD-001], [ADR-0001] | [RC-011] |
| [DM-001] | DM | en | it | [UC-001] | [SSD-001], [DICT-001] | [RC-012] |
| [DICT-001] | DICT | en | it | [DM-001] | [OC-001], [SD-001], [DCD-001] | [RC-013] |
| [SSD-001] | SSD | en | it | [UC-001], [DM-001] | [OC-001] | [RC-014] |
| [OC-001] | OC | - | - | [SSD-001] | [SD-001] | [RC-015] |
| [SD-001] | SD | - | - | [OC-001] | [DCD-001] | [RC-016] |
| [DCD-001] | DCD | - | - | [SD-001], [DM-001] | source code (MIL-003) | [RC-017] |
| [ADR-0001] | ADR | - | - | [UC-001] | [OC-001], [SD-001] | [RC-018] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | [UC-001], [OC-001], [SD-001], [DCD-001] | [ADR-0001] | - | Covered by the design; verified at MIL-003 |
| CN-002 | [PP-001], [MIL-001] | - | - | Covered by the plan and the review records |
| CN-003 | [MIL-004], [MIL-005] | - | - | Covered by plan; verified at the gateway |
| CN-004 | [DCD-001], [DICT-001] | - | - | Covered by the design; verified at MIL-003 |
| CN-005 | [MIL-002], [MIL-005] | - | - | Covered by plan; verified at the gateway |
| CN-006 | [MIL-002] | - | - | Covered by plan; verified at the gateway |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

## Coverage Notes

- No Test Plan, Entity Relationship Diagram or Architecture Description exists: the program stores nothing, and the tests follow the Operation Contract. The source code (`PY`) and the wiki have no row yet; they get one when MIL-003 and MIL-005 are reviewed.
- `-` in Upstream means foundational; in Downstream, nothing is built on it yet.

---

[ADR-0001]: ../adr/adr-0001-unsupported-characters-are-rejected.md
[BC-001]: ../business-case.md
[DCD-001]: ../dcd.md
[DICT-001]: ../dictionary.md
[DM-001]: ../domain-model.md
[MIL-001]: ../milestones/mil-001-use-case-and-design.md
[MIL-002]: ../milestones/mil-002-foundation.md
[MIL-003]: ../milestones/mil-003-converter.md
[MIL-004]: ../milestones/mil-004-notebook-and-readme.md
[MIL-005]: ../milestones/mil-005-wiki.md
[OC-001]: ../use-cases/uc-001/oc.md
[PP-001]: ../project-plan.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001-use-case-and-design.md
[RC-005]: ./reviews/rc-005-mil-002-foundation.md
[RC-006]: ./reviews/rc-006-mil-003-converter.md
[RC-007]: ./reviews/rc-007-mil-004-notebook-and-readme.md
[RC-008]: ./reviews/rc-008-mil-005-wiki.md
[RC-009]: ./reviews/rc-009-user-story.md
[RC-010]: ./reviews/rc-010-use-case-diagram.md
[RC-011]: ./reviews/rc-011-use-case.md
[RC-012]: ./reviews/rc-012-domain-model.md
[RC-013]: ./reviews/rc-013-dictionary.md
[RC-014]: ./reviews/rc-014-ssd.md
[RC-015]: ./reviews/rc-015-operation-contract.md
[RC-016]: ./reviews/rc-016-sequence-diagram.md
[RC-017]: ./reviews/rc-017-dcd.md
[RC-018]: ./reviews/rc-018-adr-0001-unsupported-characters.md
[SA-001]: ../stakeholder-analysis.md
[SD-001]: ../use-cases/uc-001/sd.md
[SSD-001]: ../use-cases/uc-001/ssd.md
[UC-001]: ../use-cases/uc-001/uc.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md

# MIL-001 Use case and design

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [US-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-004: Go | [ba98d67] |

---

## Purpose

Decides whether the design is complete enough for code to be written: the user story, the use case and the artifacts that lead from the use case to the Design Class Diagram. No code is written before this gateway is passed.

## Deliverable

The user story [US-001], the Use Case Diagram [UCD-001], the use case [UC-001], the Domain Model [DM-001], the Domain Dictionary [DICT-001], the System Sequence Diagram [SSD-001], the Operation Contract [OC-001], the Sequence Diagram [SD-001], the Design Class Diagram [DCD-001] and the decision record [ADR-0001], each with its review record. The project needs no Entity Relationship Diagram, because the program stores nothing.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Each design artifact has a review record with the verdict `Go` and its latest Version History row is `Accepted` | All ten artifacts | Any artifact without `Go` |
| 2 | Every diagram renders on the PlantUML server (`bash framework/scripts/render-diagrams.sh`) | 0 failed | Any failed diagram |
| 3 | Every method of the Design Class Diagram appears in its method traceability table and traces to a message of the Sequence Diagram | 100 % | Any method without a trace |
| 4 | Every postcondition of the Operation Contract is covered in the Postcondition Coverage table of the Sequence Diagram | 100 % | Any postcondition not covered |
| 5 | Every concept of the Domain Model has a row in the Domain Dictionary | 100 % | Any concept missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| none | First gateway; the Business Case, the Stakeholder Analysis and the Project Plan are accepted before it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objective 3, success criterion 2; story [US-001] | CN-001, CN-004 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-19 — inside the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the user story and the use case diagram | Write [US-001] with its acceptance criteria and [UCD-001] with the one actor and the one use case, so that the use case has a source and a boundary. | No | |
| 2 | Write the use case | Write [UC-001] Convert Text to Morse Code in the fully dressed format, with the extension for an unsupported character and the business rules. | No | |
| 3 | Write the Domain Model and the dictionary | Write [DM-001] with the concepts Text, Word, Character, Signal Pattern and Morse Code, and [DICT-001] with the PO term and the IT term of each. | No | |
| 4 | Write the System Sequence Diagram and the Operation Contract | Write [SSD-001] with the one system operation `convertTextToMorse` and [OC-001] with its postconditions and its exception. | No | |
| 5 | Write the Sequence Diagram and the decision record | Write [SD-001], which realises the contract across the layers Presentation, Application and Domain, and [ADR-0001], which records that unsupported characters are rejected. | No | |
| 6 | Write the Design Class Diagram | Write [DCD-001] with the classes, the method traceability and the dependency check, so that code can follow it method by method. | No | |
| 7 | Render the diagrams | Check every PlantUML diagram on the PlantUML server and fix syntax errors. | No | |
| 8 | Review the artifacts | Review each artifact against its QC checklist and record an `RC-*`; fix findings until each says `Go`. | No | |

---

[ADR-0001]: ../adr/adr-0001-unsupported-characters-are-rejected.md
[BC-001]: ../business-case.md
[DCD-001]: ../dcd.md
[DICT-001]: ../dictionary.md
[DM-001]: ../domain-model.md
[OC-001]: ../use-cases/uc-001/oc.md
[SD-001]: ../use-cases/uc-001/sd.md
[SSD-001]: ../use-cases/uc-001/ssd.md
[UC-001]: ../use-cases/uc-001/uc.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

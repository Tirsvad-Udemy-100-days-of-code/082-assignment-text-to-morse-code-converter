# MIL-005 Three-language wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [MIL-004] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version<br>Reviewed in RC-008: Go | [ba98d67] |

---

## Purpose

Decides whether the wiki explains the project and what each lecture step taught, in English, Danish and Bahasa Malaysia, and whether the repository is complete enough to be published and compared by S02 and S03.

## Deliverable

`docs/wiki/` with the same page set in three languages (`Home`, `Getting-Started` with a Linux guide and a Windows guide, `Step-1-The-Road` to `Step-4-Command-Line`, `Summary`, and `_Sidebar`), each step page with its screenshot and an explanation of what was gained; the traceability matrix; the review records; the checked published wiki.

The structure follows the wiki of the 074 LEGO project (Getting Started with a Linux guide and a Windows guide, one page per step). English pages have no suffix, Danish pages have `-da` and Bahasa Malaysia pages have `-ms` (`framework/process/wiki.md`).

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/wiki/` holds the same page set in `en`, `da` and `ms` | Same pages in three languages | A page is missing |
| 2 | `Getting-Started` in each language has a Linux guide and a Windows guide, each with the `.venv` commands | Both guides in all three | Either missing |
| 3 | Each step page has its screenshot and a section on what was gained | All steps in all three languages | Any missing |
| 4 | No image or text is taken from the lecture | Lecture only summarised | Any copy |
| 5 | The wiki is reviewed against `QC-WIKI-001` and `QC-LANG-001` and recorded as an `RC-*` | Verdict `Go` | `No-Go` |
| 6 | `bash framework/scripts/check-languages.sh`, `check-qc-tags.sh`, `check-readme.sh` and `check-editorconfig.sh` | Exit code 0 | Any finding |
| 7 | After the merge the published wiki shows the sidebar and every page | Pages present on the host | A page is missing |
| 8 | `bash scripts/scan.sh` (opengrep) | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] | The wiki uses the screenshots and the set-up instructions of the README |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 7 and 9, success criteria 4 and 5 | CN-003, CN-005 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-22 — inside the Business Case constraint (completion by 2026-11-22).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write the English wiki | `Home`, `Getting-Started` (Linux and Windows), the four step pages, `Summary` and `_Sidebar`, with what was gained in each step and its screenshot. | No | |
| 2 | Write the Danish wiki | The same pages in Danish (`-da`), with the language line on each page. | No | |
| 3 | Write the Bahasa Malaysia wiki | The same pages in Bahasa Malaysia (`-ms`), with the language line on each page. | No | |
| 4 | Review the wiki | Review against `QC-WIKI-001` and `QC-LANG-001` and record the `RC-*`; fix findings. | No | |
| 5 | Write the traceability matrix | Create `docs/sqa/traceability-matrix.md` that lists every document and its latest review. | No | |
| 6 | Run the framework checks | Run the check scripts and opengrep and fix findings. | No | |
| 7 | Verify the published wiki | After the merge, read the wiki on the git host and check that the sidebar and all pages are there. | No | |

---

[BC-001]: ../business-case.md
[MIL-004]: ./mil-004-notebook-and-readme.md
[ba98d67]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/ba98d6725280ec49e8e215622959ea535d58843c

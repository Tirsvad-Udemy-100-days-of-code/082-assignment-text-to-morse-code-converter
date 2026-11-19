# Review Record: Wiki against QC-WIKI-001 and QC-LANG-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-022 |
| CrossReference | [MIL-005], [QC-WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-19 | Deprecated | Jens Tirsvad Nielsen | S01 | Records the check on the published wiki (criterion 14 and MIL-005 criterion 7); verdict stays Go | [0d2d01a] |
| 2026-11-19 | Accepted | Jens Tirsvad Nielsen | S01 | Records S01's confirmation of the Danish and Bahasa Malaysia texts (QC-LANG-001 criterion 9); no open item remains; verdict stays Go | [6115bd9] |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (22 files: 7 pages in each of `en`, `da` and `ms`, and the sidebar)
- Checklist used: [QC-WIKI-001] and [QC-LANG-001] (the language checklist is applied where a wiki page can meet it)
- Scope: full review
- Language and domain: en, da and ms / it
- Language reviewer: S01 for `da` and `ms` (confirmed in chat on 2026-11-19)
- Mode: autonomous, not independent (the author and the reviewer are both S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | Pass | The sidebar starts with `**Text to Morse Code Converter**` and then one list of the English pages, `Home` first. |
| 3 | Pass | All 7 English pages are in the list (Home, Getting-Started, Step-1 to Step-4, Summary); a script that resolved all 94 relative links of the wiki found no link to a missing page. |
| 4 | N-A | The wiki has no related wiki, so it has no `**Related**` section. |
| 5 | Pass | `**Languages**` is the last section: `English: [Home](Home)`, `Dansk: [Hjem](Home-da)`, `Bahasa Melayu: [Utama](Home-ms)`. |
| 6 | Pass | The page list appears once. |
| 7 | N-A | The sidebar is written by hand and carries no generator comment. |
| 8 | Pass | Each page has the language line. |
| 9 | Pass | The wiki exists in English (the PO language) and, on top of it, in Danish and Bahasa Malaysia, as the registry's `Wiki languages` row says. |
| 10 | Pass | 7 pages in `en`, 7 in `da` and 7 in `ms` plus the one sidebar; the file lists match page by page. |
| 11 | Pass | Every page starts with `**English** · [Dansk](...) · [Bahasa Malaysia](...)` with the current language in bold. |
| 12 | Pass | Danish pages end in `-da.md`, Bahasa Malaysia pages in `-ms.md`, English pages have no suffix. |
| 13 | Pass | Commands, code names, file names and IDs (`.venv`, `python -m morse_converter`, `UnsupportedCharacterError`, `ADR-0001`) are English in all three languages. |
| 14 | Pass | After the merge the wiki on the host lists 22 pages (21 pages and the sidebar); 11 pages in the three languages answer with HTTP 200, the sidebar links of `Home` and the language links are present, and the four screenshots answer with HTTP 200. |
| 15 | N-A | No change to the layout rules. |
| 16 | Pass | `docs/wiki/` holds the 22 files directly and has no subfolder. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 3 | Pass | The pages are written in the language of their file; code, commands and file names stay English, as the wiki checklist allows. |
| 6 | Pass | The page names, file names and IDs are English; the page headings are in the language of the page, as the wiki is read by readers of that language (a wiki page has no Metadata table). |
| 9 | Pass | S01 confirmed the Danish and Bahasa Malaysia texts in chat on 2026-11-19; the author wrote them, so the confirmation is by the Product Owner, not by a second reviewer. |
| 10 | Pass | Abbreviations are spelled out or are established names (Docker, Doxygen, pytest, ADR is linked to its document). |
| 1, 2, 4, 5, 7, 8 | N-A | A wiki page is documentation for readers, not an artifact with an ID and a Metadata table (`framework/process/wiki.md`), so the Metadata, register, dictionary and Version History criteria do not apply. |

## MIL-005 Go / No-Go Evidence

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Same page set in three languages | Pass | See QC-WIKI-001 criterion 10. |
| 2 | `Getting-Started` has a Linux guide and a Windows guide with the `.venv` commands | Pass | Each language has a "Windows" and a "Linux and macOS" section with `python -m venv .venv`, the activation and `python -m pip install --upgrade pip`. |
| 3 | Each step page has its screenshot and a section on what was gained | Pass | The four step pages in each language have an image of `docs/images/` and a "What you gained" list. |
| 4 | No image or text is taken from the lecture | Pass | The lecture is summarised in one sentence of the own words of the author; the images are the program's output. |
| 6 | The framework checks | Pass | `check-languages.sh`, `check-qc-tags.sh`, `check-readme.sh` and `check-editorconfig.sh` exit 0. |
| 8 | opengrep | Pass | `bash scripts/scan.sh` with the CI rules: 783 rules, 0 findings. |
| 7 | The published wiki | Pass | See QC-WIKI-001 criterion 14. |

## Overall Verdict

Go: no criterion fails and no item is open.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the sidebar, every page and every link on the published wiki and record the result here | S01 | Done 2026-11-19 (criterion 14) |
| Have a reader of Danish and a reader of Bahasa Malaysia confirm the translations | S01 | Done 2026-11-19 (confirmed in chat) |

---

[MIL-005]: ../../milestones/mil-005-wiki.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[3a2b2c3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/3a2b2c318bd53aa3f234539380420be4f17c3f78
[0d2d01a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/0d2d01a03dad770e567886efc953165b4da6896a
[6115bd9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/082-assignment-text-to-morse-code-converter/commit/6115bd9d1fd379b0efc2d5f0d96cc3be36da4c14

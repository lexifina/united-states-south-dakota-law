# How this repository was made (United States (South Dakota))

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| South Dakota Legislature: Constitution and Codified Laws (public JSON API) | <https://sdlegislature.gov/Statutes> | 2026-10-30 | Statute text is not copyrightable (Georgia v. Public.Resource.Org, 2020). |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the State of South Dakota | 1 | 2026-09-03 to 2026-09-03 |
| `title-22-crimes` | SDCL Title 22: Crimes | 1 | 2026-09-03 to 2026-09-03 |
| `chapter-47-1a-business-corporations` | SDCL chapter 47-1A: South Dakota Business Corporation Act | 1 | 2026-09-03 to 2026-09-03 |
| `chapter-43-32-residential-landlord-tenant` | SDCL chapter 43-32: Landlord and Tenant | 1 | 2026-09-03 to 2026-09-03 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (America/Chicago) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Legislative Research Council publishes only the current text; its API gives the last statute effective date, which dates the single version. https://sdlegislature.gov/api/Statutes/LastStatuesEffectiveDate

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `e155a87148d9c73e3dc2463a50ca8a1c4c24b547f0cb899c06c1972aa3a15e96` (1338580 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Only the current text is online, so each act has one version, the oldest version available, dated 2026-09-03 from the API's last statute effective date.
- Scope: the Constitution, SDCL Title 22 (Crimes), chapter 47-1A (Business Corporation Act) and chapter 43-32 (Landlord and Tenant). Other titles are not included.
- The "Source:" line of each section (session law citations) and anything after it is dropped; so are constitutional article headings.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none

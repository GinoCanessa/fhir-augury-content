# Artifact Ballot Note Draft: List (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `List` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 0 (250 commits in window overall, none touching `List` source files) |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T13:36:10Z |

## Source Files

Files considered part of `List` for this run (FhirCore conventions, folder
`source/list/`; sibling `list-ccda-cognitivestatuses-introduction.xml` and
`list-fivews-mapping-exceptions.xml` live in the same folder but belong to
other artifacts and are excluded):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/list/structuredefinition-List.xml` | StructureDefinition (canonical) | no |
| `source/list/list-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/list/list-notes.xml` | Supplementary narrative | no |
| `source/list/bundle-List-search-params.xml` | Search parameters bundle | no |
| `source/list/list-List-operations.xml` | Operations list | no |
| `source/list/list-List-examples.xml` | Examples list | no |
| `source/list/list-List-packs.xml` | Resource packs list | no |
| `source/list/list-examples-header.xml` | Examples header narrative | no |
| `source/list/implementationguide-List-core.xml` | Core IG declaration | no |
| `source/list/list-example.xml` | Example | no |
| `source/list/list-example-allergies.xml` | Example | no |
| `source/list/list-example-double-cousin-relationship-pedigree.xml` | Example | no |
| `source/list/list-example-empty.xml` | Example | no |
| `source/list/list-example-familyhistory-f201-roel.xml` | Example | no |
| `source/list/list-example-familyhistory-genetics-profile-annie.xml` | Example | no |
| `source/list/list-example-familyhistory-genetics-profile.xml` | Example | no |
| `source/list/list-example-long.xml` | Example | no |
| `source/list/list-example-medlist.xml` | Example | no |
| `source/list/list-example-simple-empty.xml` | Example | no |
| `source/list/list-example-socialhistory.xml` | Example | no |
| `source/list/list-example-xds.xml` | Example | no |
| `source/list/codesystem-list-item-flag.xml` | Artifact-scoped CodeSystem (3 total) | no |
| `source/list/codesystem-list-mode.xml` | Artifact-scoped CodeSystem | no |
| `source/list/codesystem-list-status.xml` | Artifact-scoped CodeSystem | no |
| `source/list/valueset-list-empty-reason.xml` | Artifact-scoped ValueSet (7 total) | no |
| `source/list/valueset-list-example-codes.xml` | Artifact-scoped ValueSet | no |
| `source/list/valueset-list-item-flag.xml` | Artifact-scoped ValueSet | no |
| `source/list/valueset-list-listpurposecodes.xml` | Artifact-scoped ValueSet | no |
| `source/list/valueset-list-mode.xml` | Artifact-scoped ValueSet | no |
| `source/list/valueset-list-order.xml` | Artifact-scoped ValueSet | no |
| `source/list/valueset-list-status.xml` | Artifact-scoped ValueSet | no |

Patterns from the briefing/standard FhirCore layout that produced no match in the clone:

- `source/list/List-spreadsheet.xml` — no legacy spreadsheet (SD is authoritative).
- Sibling `structuredefinition-*.xml` not matching the folder name — none present.

## Current Ballot Note

No existing ballot note. The intro file (`source/list/list-introduction.xml`)
at HEAD contains only the **Scope and Usage** and **Boundaries and
Relationships** sections; no `<blockquote class="ballot-note" …>` block is
present.

## Tickets Applied in Window

None. No commits in the `5d67a34a13a5..db79dcdfe196` window touched any file
in the `List` artifact's source set.

## Per-Ticket Detail

None — see above.

## Roll-up Summary (after-applied state)

**No changes to artifact in window.**

`git diff 5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd..HEAD --
source/list/structuredefinition-List.xml source/list/list-introduction.xml
source/list/list-notes.xml source/list/bundle-List-search-params.xml
source/list/list-List-operations.xml source/list/list-List-examples.xml
source/list/list-List-packs.xml source/list/implementationguide-List-core.xml
source/list/list-example*.xml source/list/list-examples-header.xml
source/list/valueset-list-*.xml source/list/codesystem-list-*.xml`
returns an empty diff. The 250 commits applied to `HL7/fhir` between the
since-commit (`5d67a34a13a5` — *"bump version for publication"*) and HEAD
(`db79dcdfe196`) all landed in other artifacts; the `List` resource, its
search parameters, operations, examples, and artifact-scoped terminology
were untouched.

- **StructureDefinition (`structuredefinition-List.xml`):** unchanged.
- **Intro / narrative (`list-introduction.xml`, `list-notes.xml`):** unchanged.
- **Search parameters (`bundle-List-search-params.xml`):** unchanged.
- **Operations (`list-List-operations.xml`):** unchanged.
- **Examples:** unchanged (no examples added or removed).
- **Terminology (sibling `valueset-list-*` / `codesystem-list-*`):** unchanged.

## Proposed Ballot Note (HTML)

No ballot note is proposed. Because nothing in the `List` artifact changed
since the since-commit, there are no balloter-relevant deltas to summarise
and no existing ballot note to revise. If a fresh note is desired anyway
(e.g., to flag normative status or carry-forward context), it should be
authored against substantive prior-cycle changes — not against this
(empty) window.

## Notes for Reviewer

- HEAD (`db79dcdfe196`) is a direct descendant of the since-commit
  (`5d67a34a13a5`); the linear `since..HEAD` range applies and no symmetric
  difference fallback was needed.
- The cache clone resolved the since-commit locally; no `gh api` fallback
  was required.
- The briefing meta records `clone_head_sha = 1b369ff4e28e695908ed97d802bbad1e8ff32874`
  while the working clone is now at `db79dcdfe196d35bd0e74c58c655a4c1c8f534f7`.
  This is a clone fast-forward that post-dates the briefing snapshot but
  does not affect this report — none of the intervening commits touch the
  `List` source set, so the briefing's Artifact Map for `List` is still
  authoritative.
- Two files in `source/list/` (`list-ccda-cognitivestatuses-introduction.xml`
  and `list-fivews-mapping-exceptions.xml`) share the folder but belong to
  CCDA/5W cross-cutting artifacts and were intentionally excluded from the
  `List` file set. Neither was touched in the window either.
- The since-commit subject (`bump version for publication`) suggests this
  window starts at a publication snapshot; for the next ballot cycle, any
  `List` work would appear here once landed.

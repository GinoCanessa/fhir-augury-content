# Artifact Ballot Note Draft: Task (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Task` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 2 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `Task` for this run (resolved from `source/task/` per the briefing's FhirCore Artifact Map conventions):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/task/structuredefinition-Task.xml` | StructureDefinition (canonical SD) | no |
| `source/task/task-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/task/task-notes.xml` | Supplementary narrative | no |
| `source/task/bundle-Task-search-params.xml` | Search parameters | no |
| `source/task/list-Task-operations.xml` | Operations | no |
| `source/task/list-Task-examples.xml` | Examples list | no |
| `source/task/list-Task-packs.xml` | Packs list | no |
| `source/task/implementationguide-Task-core.xml` | Core IG entry | no |
| `source/task/codesystem-task-status.xml` | Artifact-scoped CodeSystem (Task.status) | yes |
| `source/task/codesystem-task-code.xml` | Artifact-scoped CodeSystem (Task.code) | yes |
| `source/task/codesystem-task-inputoutput-parameter-type.xml` | Artifact-scoped CodeSystem (input/output parameter type) | yes |
| `source/task/codesystem-task-business-status.xml` | Artifact-scoped CodeSystem | no |
| `source/task/codesystem-task-intent.xml` | Artifact-scoped CodeSystem | no |
| `source/task/codesystem-task-performer-function-code.xml` | Artifact-scoped CodeSystem | no |
| `source/task/codesystem-task-reason.xml` | Artifact-scoped CodeSystem | no |
| `source/task/codesystem-task-stage.xml` | Artifact-scoped CodeSystem | no |
| `source/task/codesystem-task-status-reason.xml` | Artifact-scoped CodeSystem | no |
| `source/task/valueset-task-*.xml` | Artifact-scoped ValueSets (8) | no |
| `source/task/task-example*.xml`, `source/task/task-cpg-example-1.xml` | Examples | no |
| `source/task/task-*-mapping-exceptions.xml`, `source/task/task-examples-header.xml` | Mapping / examples ancillary | no |
| `source/task/invariant-tests/` | Invariant tests | no |
| `source/task/task.svg` | Diagram | no |

Patterns from the briefing that produced no match in the clone:

- `source/task/task-spreadsheet.xml` — no file matched (legacy spreadsheet not present; SD is authoritative).
- Sibling `structuredefinition-*.xml` other than `structuredefinition-Task.xml` — none present.

## Current Ballot Note

The intro file at HEAD contains one `class="ballot-note"` block plus an additional ad-hoc `lightblue` "Release Notes (pending alternative process review with FMG)" blockquote that was added during the window (not a `ballot-note` block).

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
  <ul>
    <li>Removed the Task.instantiatesCanonical and Task.instantiatesURI; and advise implementers to use the <a href="workflow-extensions.html">workflow instantiates extensions</a></li>
    <li>Made the Task.focus element a new backbone</li>
    <li>Consolidated the Task State Machine sections to the Notes section:<a href="task.html#statemachine">task.html#statemachine</a></li>
  </ul>
</blockquote>
```

In addition, the following non-`ballot-note` block was added in the window (commits `d2dde0c4a093` + `c8deb117c4ca`) and is currently present at HEAD:

```html
<blockquote style="background-color: lightblue">
  <p><b>Release Notes (pending alternative process review with FMG):</b></p>
  <ul>
    <li><a href="https://jira.hl7.org/browse/FHIR-55280">FHIR-55280</a></li>
    <li><a href="https://jira.hl7.org/browse/FHIR-56060">FHIR-56060</a></li>
  </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55280](https://jira.hl7.org/browse/FHIR-55280) | Task.status has no escape valve | [`a829e63bd1a5`](https://github.com/HL7/fhir/commit/a829e63bd1a52a6d7bbb16153de7dcaa3984a19d), [`c8deb117c4ca`](https://github.com/HL7/fhir/commit/c8deb117c4caf563836a7606f5dbd1739a9af49e) |
| [FHIR-56060](https://jira.hl7.org/browse/FHIR-56060) | Minor cleanup to value set display names | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) |

The `d2dde0c4a093` commit message also references FHIR-55277, FHIR-54961, FHIR-54593, FHIR-54450, FHIR-54323 and FHIR-53457 as part of an "OO tickets first draft" batch, but those tickets did not touch any files under `source/task/` and so are not attributed to this artifact.

## Per-Ticket Detail

### [FHIR-55280](https://jira.hl7.org/browse/FHIR-55280) — Task.status has no escape valve

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only substantive comments on the ticket are the implementing PR link (HL7/fhir#4013) and an applier note from `jdlnolen`: "Loosen Cardinality on Task.status was discussed and discarded because it does not align to the patterns."

- **Disposition summary:** The ticket reported that `Task.status` is a mandatory element with a required binding but lacked an `unknown` / `other` "escape valve", making the element impossible to populate in some cases. The agreed fix was to add an `unknown` concept to the `task-status` value set / code system rather than loosening cardinality on `Task.status`.
- **Commits applying this ticket:**
  - [`a829e63bd1a5`](https://github.com/HL7/fhir/commit/a829e63bd1a52a6d7bbb16153de7dcaa3984a19d) — FHIR-55280: Add 'unknown' status code to Task.status value set (2026-02-28)
  - [`c8deb117c4ca`](https://github.com/HL7/fhir/commit/c8deb117c4caf563836a7606f5dbd1739a9af49e) — updated header (2026-03-29) — added the FHIR-55280 entry to the lightblue Release Notes blockquote in `task-introduction.xml`.
- **Changes applied (per Step 5b, scoped to this artifact):** A single new concept `unknown` (display "Unknown") was appended to `codesystem-task-status.xml` with the standard "the authoring/source system does not know which of the status values currently applies" definition (and the `Note: This concept is not to be used for "other"` clarification). The companion `valueset-task-status.xml` was not touched in the window — it includes the entire CodeSystem by reference, so the new code is picked up automatically. No cardinality change was made on `Task.status` itself; the StructureDefinition is unchanged. The intro file was updated only to list FHIR-55280 in the new Release Notes blockquote.

### [FHIR-56060](https://jira.hl7.org/browse/FHIR-56060) — Minor cleanup to value set display names

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only substantive comment on the ticket is the implementing PR link (HL7/fhir#4037).

- **Disposition summary:** Local builds were emitting `INFORMATION` messages of the form "Display Names must be TitleCase" for several Task-related code system displays. The agreed fix was a low-risk cosmetic correction: capitalize the first letter (or full title-case where appropriate) of the affected `display` values so that they conform to the publisher's title-case rule.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24).
  - [`c8deb117c4ca`](https://github.com/HL7/fhir/commit/c8deb117c4caf563836a7606f5dbd1739a9af49e) — updated header (2026-03-29) — added the FHIR-56060 entry to the lightblue Release Notes blockquote in `task-introduction.xml`.
- **Changes applied (per Step 5b, scoped to this artifact):** In `codesystem-task-code.xml`, the `data-request` concept's display changed from `data request task` to `Data request task` (sentence-case for an extensible-binding code). In `codesystem-task-inputoutput-parameter-type.xml`, the displays for `data-query`, `data-code` and `data-value` were title-cased to `Data Query Input`, `Data Code Input` and `Data Values Output` respectively (full title-case for an example-binding code). Definitions, codes, hierarchy and concept counts are unchanged; the companion ValueSets, the StructureDefinition and any examples were not touched.

## Roll-up Summary (after-applied state)

The window touched four files in `source/task/`; the net diff is small (`+16 / -4` lines across 4 files, no SD changes).

- **StructureDefinition (`structuredefinition-Task.xml`):** No changes in the window. Snapshot regeneration is **not** required for these edits (only display strings on artifact-scoped CodeSystems and a new code on the `task-status` CodeSystem).
- **Intro / narrative (`task-introduction.xml`):** A new ad-hoc `<blockquote style="background-color: lightblue">` titled "Release Notes (pending alternative process review with FMG)" was inserted immediately after the existing `ballot-note` (`bn1`). It currently lists FHIR-55280 and FHIR-56060 as bare links and is explicitly flagged as pending an alternative-process review with FMG. `task-notes.xml` is unchanged.
- **Search parameters (`bundle-Task-search-params.xml`):** No changes.
- **Operations (`list-Task-operations.xml`):** No changes.
- **Examples (`list-Task-examples.xml`, `task-example*.xml`, `task-cpg-example-1.xml`):** No changes.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - `codesystem-task-status.xml` — added the `unknown` concept (display "Unknown") with the standard "authoring system does not know which status applies / not for use as 'other'" definition (FHIR-55280). `valueset-task-status.xml` is unchanged but now includes the new code transitively.
  - `codesystem-task-code.xml` — display for `data-request` changed from `data request task` → `Data request task` (FHIR-56060).
  - `codesystem-task-inputoutput-parameter-type.xml` — displays for `data-query`, `data-code`, `data-value` title-cased to `Data Query Input`, `Data Code Input`, `Data Values Output` (FHIR-56060).
  - All affected CodeSystems are core HL7 FHIR canonicals (`http://hl7.org/fhir/CodeSystem/task-...`) authored in `HL7/fhir`; they are not duplicated in UTG, so no cross-repo touch points are required for these edits.

## Proposed Ballot Note (HTML)

The existing `bn1` bullets remain accurate in the after-applied state and are carried forward verbatim. Two new bullets cover the changes that landed in the window. The ad-hoc lightblue "Release Notes" blockquote that was added during the window is **not** a `ballot-note` and is left in place; reviewers may consider folding it into `bn1` (or removing it, since the same tickets are now cited inline below) as part of the FMG process review it explicitly defers to.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
  <ul>
    <li>Removed the Task.instantiatesCanonical and Task.instantiatesURI; and advise implementers to use the <a href="workflow-extensions.html">workflow instantiates extensions</a></li>
    <li>Made the Task.focus element a new backbone</li>
    <li>Consolidated the Task State Machine sections to the Notes section: <a href="task.html#statemachine">task.html#statemachine</a></li>
    <li>Added an <code>unknown</code> concept to the <a href="codesystem-task-status.html">Task status</a> CodeSystem (and, transitively, the required <a href="valueset-task-status.html">Task status</a> value set), giving authoring systems an escape valve when no other status is known to apply (<a href="https://jira.hl7.org/browse/FHIR-55280">FHIR-55280</a>). <code>Task.status</code> remains <code>1..1</code>; loosening cardinality was considered and rejected as inconsistent with the workflow pattern.</li>
    <li>Title-cased the display names of several Task-related CodeSystem concepts to satisfy the publisher's display-name rules: <code>data-request</code> in <a href="codesystem-task-code.html">Task code</a>, and <code>data-query</code>, <code>data-code</code> and <code>data-value</code> in <a href="codesystem-task-inputoutput-parameter-type.html">Task input/output parameter type</a>. Codes and definitions are unchanged (<a href="https://jira.hl7.org/browse/FHIR-56060">FHIR-56060</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The intro file currently carries an ad-hoc `<blockquote style="background-color: lightblue">` "Release Notes (pending alternative process review with FMG)" block listing FHIR-55280 and FHIR-56060. The proposed `bn1` revision above absorbs both tickets as substantive bullets; if accepted, the lightblue blockquote can be removed (or kept as a pure pointer) at the WG's discretion. It was added by `d2dde0c4a093` (FHIR-56060) and extended by `c8deb117c4ca` (FHIR-55280); it is not a `ballot-note` block and so was not edited mechanically here.
- The "OO tickets first draft" commit (`d2dde0c4a093`) also references FHIR-55277, FHIR-54961, FHIR-54593, FHIR-54450, FHIR-54323 and FHIR-53457 in its message, but none of those touch files under `source/task/`. They presumably apply to other Orders & Observations artifacts (e.g., DiagnosticReport, ServiceRequest, Specimen, Observation) and are out of scope for this report.
- `valueset-task-status.xml` was not touched in the window; the new `unknown` concept reaches the value set via its include-by-system reference. No re-publication of the value set file is required, but downstream tooling that snapshots the value set's expansion will need to re-expand.
- `cross-referenced` returned no hits for any of the three commit SHAs in the window; ticket attribution above is derived purely from commit-message Jira keys and the per-commit file diffs. `gh` was not needed — the cache clone resolves both the since-commit and HEAD.
- Both tickets' Jira `resolution_description` fields and any explicit "applied vote" disposition comments were empty; the verbatim disposition entries above reflect the only comments actually recorded on the tickets.

# Artifact Ballot Note Draft: PlanDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `PlanDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T17:04:23Z |

## Source Files

Files considered part of `PlanDefinition` for this run (resolved from
`source/plandefinition/` per the FhirCore conventions in the
`notes-artifact` skill; the saved briefing's Artifact Map does not
emit a per-resource sub-section, so the FhirCore patterns were
applied directly against the cached clone):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/plandefinition/structuredefinition-PlanDefinition.xml` | StructureDefinition (canonical) | no |
| `source/plandefinition/plandefinition-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/plandefinition/plandefinition-notes.xml` | Supplementary narrative | no |
| `source/plandefinition/bundle-PlanDefinition-search-params.xml` | Search parameters bundle | no |
| `source/plandefinition/list-PlanDefinition-operations.xml` | Operations list | no |
| `source/plandefinition/list-PlanDefinition-examples.xml` | Examples list | no |
| `source/plandefinition/list-PlanDefinition-packs.xml` | Packs list | no |
| `source/plandefinition/operationdefinition-PlanDefinition-apply.xml` | `$apply` OperationDefinition | no |
| `source/plandefinition/operationdefinition-PlanDefinition-data-requirements.xml` | `$data-requirements` OperationDefinition | no |
| `source/plandefinition/valueset-action-*.xml` (12 files) | Artifact-scoped ValueSets | no |
| `source/plandefinition/codesystem-action-*.xml` (12 files) | Artifact-scoped CodeSystems | no |
| `source/plandefinition/conceptmap-{start,end}-relationship-type.xml` (2 files) | Artifact-scoped ConceptMaps | no |
| `source/plandefinition/plandefinition-example*.xml` (5 files) | Examples | no |
| `source/plandefinition/plandefinition-opioidcds-04.xml` | Example (CDC opioid CDS) | **yes** |
| `source/plandefinition/plandefinition-opioidcds-05.xml` | Example (CDC opioid CDS) | **yes** |
| `source/plandefinition/plandefinition-opioidcds-07.xml` | Example (CDC opioid CDS) | **yes** |
| `source/plandefinition/plandefinition-opioidcds-08.xml` | Example (CDC opioid CDS) | **yes** |
| `source/plandefinition/plandefinition-opioidcds-10.xml` | Example (CDC opioid CDS) | **yes** |
| `source/plandefinition/plandefinition-opioidcds-11.xml` | Example (CDC opioid CDS) | **yes** |
| `source/plandefinition/plandefinition-exclusive-breastfeeding-intervention-0{1..4}.xml` | Examples | no |
| `source/plandefinition/plandefinition-chlamydia-screening-intervention.xml` | Example | no |
| `source/plandefinition/plandefinition-zika-virus-intervention.xml` | Example | no |
| `source/plandefinition/plandefinition-{options,predecessor,protocol,protocol-study}-example.xml` | Examples | no |
| `source/plandefinition/plandefinition-{definition,fivews}-mapping-exceptions.xml` | Mapping examples | no |
| `source/plandefinition/apply-operation-response-example.xml` | `$apply` example | no |
| `source/plandefinition/plandefinition-examples-header.xml` | Examples narrative header | no |

Patterns from the FhirCore conventions that produced no match in the
clone:

- `source/plandefinition/structuredefinition-*.xml` (other than the
  canonical) — no match (no sibling profile artifacts ship inside the
  PlanDefinition folder).
- `source/plandefinition/plandefinition-spreadsheet.xml` — no match
  (no legacy spreadsheet ships for this resource).

## Current Ballot Note

No existing ballot note. `plandefinition-introduction.xml` at HEAD
contains no `<blockquote class="ballot-note" …>` element.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) — display names have changed for US and GB (2026-03-28, JohnMoehrke) |

The single commit in the window does not reference any `FHIR-####`
key in its subject or body, and `fhir-augury-cli cross-referenced`
returned zero hits for the SHA. It is treated as unattributed and
listed below.

## Per-Ticket Detail

### (unattributed) — display-name cleanup for ISO-3166 jurisdiction codings

- **Work group:** n/a
- **Resolution:** n/a
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (commit not associated with a ticket).

- **Disposition summary:** Author-driven housekeeping, applied across
  multiple resources at once. The commit message ("display names have
  changed for US and GB") indicates the change reflects a refresh of
  the ISO 3166 country-name display values; the PlanDefinition slice
  is the example-only fallout for that sweep.
- **Commits applying this ticket:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) — display names have changed for US and GB (2026-03-28T11:07:18-05:00, JohnMoehrke)
- **Changes applied (per Step 5b, scoped to this artifact):** In each
  of the six CDC opioid-CDS example PlanDefinitions
  (`plandefinition-opioidcds-04.xml`, `-05.xml`, `-07.xml`, `-08.xml`,
  `-10.xml`, `-11.xml`), the `<jurisdiction>` coding for
  `urn:iso:std:iso:3166`/`US` had its `<display>` value changed from
  `"United States of America (the)"` to `"United States of America"`.
  No element values, codes, action structures, conditions, dynamic
  values, or other content were modified. The PlanDefinition resource
  definition itself, its operations, search parameters, narrative,
  and bound terminology were not touched in the window.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-PlanDefinition.xml`):**
  No changes. No element additions, removals, cardinality, type,
  binding, or constraint edits in either the differential or the
  snapshot. Snapshot regeneration is **not** required as a result of
  changes in this window.
- **Intro / narrative
  (`plandefinition-introduction.xml`, `plandefinition-notes.xml`):**
  No changes.
- **Search parameters
  (`bundle-PlanDefinition-search-params.xml`):** No changes.
- **Operations (`list-PlanDefinition-operations.xml`,
  `operationdefinition-PlanDefinition-apply.xml`,
  `operationdefinition-PlanDefinition-data-requirements.xml`):** No
  changes.
- **Examples:** Six existing CDC opioid-CDS examples
  (`plandefinition-opioidcds-04|05|07|08|10|11.xml`) had the ISO-3166
  jurisdiction `<display>` text refreshed from
  `"United States of America (the)"` to `"United States of America"`.
  No examples added or removed; no other example content changed.
- **Terminology (sibling `valueset-action-*.xml`,
  `codesystem-action-*.xml`,
  `conceptmap-{start,end}-relationship-type.xml`):** No changes. The
  jurisdiction display update is in example data only and does not
  affect any ValueSet / CodeSystem authored in this folder. (The
  ISO-3166 country code system is maintained externally and is out of
  scope for this artifact.)

## Proposed Ballot Note (HTML)

The only material change to PlanDefinition in this window is a
display-text refresh in six example PlanDefinitions
(`urn:iso:std:iso:3166#US` jurisdiction display: `"United States of
America (the)"` → `"United States of America"`). No commits touched
the StructureDefinition, narrative, search parameters, operations, or
artifact-scoped terminology, and no Jira ticket is associated with
the change. There is therefore nothing balloter-relevant to flag for
this resource since the prior ballot, and a ballot note is arguably
not warranted; the draft below is offered only so editors can choose
to publish a "no substantive change" advisory if desired. Editors may
also reasonably elect to skip publishing a ballot note for this
window — see the Notes for Reviewer.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to
  PlanDefinition since the previous ballot. The only edits in this
  window were a display-text refresh of the ISO&#160;3166 <code>US</code>
  jurisdiction coding (<code>"United States of America (the)"</code> →
  <code>"United States of America"</code>) in six existing CDC
  opioid-CDS example PlanDefinitions; no normative or definitional
  content was affected.</p>
</blockquote>
```

## Notes for Reviewer

- **No existing ballot note dropped or revised.** The intro file did
  not carry a ballot note at the since-commit either, so nothing was
  carried forward or removed.
- **Consider omitting the ballot note entirely.** The window contains
  zero commits against the StructureDefinition, narrative, search
  parameters, operations, or artifact-scoped terminology. The lone
  change is an example-only display-text refresh with no Jira ticket.
  Publishing a "no substantive change" note is editorially optional;
  if the editor's policy is to omit ballot notes when nothing
  balloter-relevant has changed, leave `plandefinition-introduction.xml`
  unchanged.
- **Cross-resource sweep.** Commit
  [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224)
  is described as a global "display names have changed for US and GB"
  sweep. Only the six PlanDefinition examples listed above are within
  this artifact's scope; the same commit almost certainly touched
  example files for other resources (handled by their own
  `notes-artifact` runs).
- **Briefing freshness.** The saved repo-analysis briefing was
  generated against clone HEAD `1b369ff4e28e` (2026-04-20); the
  current cache clone HEAD is `db79dcdfe196`. The since-commit
  `5d67a34a13a5` is an ancestor of the current HEAD (fast-forward
  range used; symmetric difference not required). The briefing was
  used only for layout/conventions, which have not shifted between
  those two SHAs for the `source/plandefinition/` folder, so no
  staleness issue affects this report.
- **No `gh` fall-back required.** All commit metadata, diffs, and
  file contents were resolved from the cached clone via `git`.

# Artifact Ballot Note Draft: DeviceMetric (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `DeviceMetric` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `DeviceMetric` for this run (resolved from
the `source/devicemetric/` folder; the briefing's Artifact Map does
not provide a DeviceMetric-specific override, so the standard
FhirCore patterns from the skill were applied):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/devicemetric/structuredefinition-DeviceMetric.xml` | StructureDefinition | yes |
| `source/devicemetric/devicemetric-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/devicemetric/devicemetric-notes.xml` | Supplementary narrative | no |
| `source/devicemetric/devicemetric-fivews-mapping-exceptions.xml` | 5W mapping exceptions | no |
| `source/devicemetric/bundle-DeviceMetric-search-params.xml` | Search parameters | no |
| `source/devicemetric/list-DeviceMetric-operations.xml` | Operations | no |
| `source/devicemetric/list-DeviceMetric-examples.xml` | Examples list | no |
| `source/devicemetric/list-DeviceMetric-packs.xml` | Implementation packs list | no |
| `source/devicemetric/devicemetric-examples-header.xml` | Examples header | no |
| `source/devicemetric/devicemetric-example.xml` | Example instance | no |
| `source/devicemetric/valueset-devicemetric-type.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/valueset-metric-availability.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/valueset-metric-calibration-state.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/valueset-metric-calibration-type.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/valueset-metric-category.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/valueset-metric-operational-status.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/valueset-metric-status.xml` | Artifact-scoped ValueSet | no |
| `source/devicemetric/codesystem-metric-availability.xml` | Artifact-scoped CodeSystem | no |
| `source/devicemetric/codesystem-metric-calibration-state.xml` | Artifact-scoped CodeSystem | no |
| `source/devicemetric/codesystem-metric-calibration-type.xml` | Artifact-scoped CodeSystem | no |
| `source/devicemetric/codesystem-metric-category.xml` | Artifact-scoped CodeSystem | no |
| `source/devicemetric/codesystem-metric-operational-status.xml` | Artifact-scoped CodeSystem | no |
| `source/devicemetric/codesystem-metric-status.xml` | Artifact-scoped CodeSystem | no |

Patterns from the standard FhirCore skill list that produced no match
in the clone:

- `source/devicemetric/devicemetric-spreadsheet.xml` — no file matched (no legacy spreadsheet shipped for this resource).
- `source/devicemetric/devicemetric-examples.xml` — no file matched (examples are listed via `list-DeviceMetric-examples.xml` and the singular `devicemetric-example.xml`).
- Sibling `structuredefinition-*.xml` other than the canonical — no extra profile artifacts ship in this folder.

## Current Ballot Note

No existing ballot note. The `devicemetric-introduction.xml` file at
HEAD contains no `<blockquote class="ballot-note" …>` block.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

No `(FHIR|UTG)-\d+` keys appear in the commit subject or body, and
`fhir-augury-cli cross-referenced` for SHA `a9658ed97c2a…` returned
zero hits. The single in-window commit is therefore unattributed.

## Per-Ticket Detail

### (unattributed)

- **Commits applying this work:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — "typos and bump kindling" (2026-03-18T13:14:07+11:00, Grahame Grieve)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-DeviceMetric.xml`, the `<publisher>` value
  was updated from `HL7 International / Health Care Devices` to
  `HL7 International / Devices`. This is metadata-only and does not
  alter the StructureDefinition's `<differential>`, `<snapshot>`, or
  any conformance-bearing element. The same commit ("typos and bump
  kindling") touched many other files across the repo, but only this
  single line changed in any DeviceMetric file.

## Roll-up Summary (after-applied state)

The full `5d67a34a13a5..db79dcdfe196` diff scoped to
`source/devicemetric/` is a single one-line change:

- **StructureDefinition (`structuredefinition-DeviceMetric.xml`):**
  - `<publisher>` renamed from `HL7 International / Health Care Devices`
    to `HL7 International / Devices` (work-group/publisher label
    realignment). No element additions, removals, cardinality, type,
    binding, constraint, or invariant changes. `<differential>` is
    unchanged; snapshot regeneration is **not** required for this
    edit (publisher metadata is not part of the snapshot element
    tree).
- **Intro / narrative (`devicemetric-introduction.xml`, `devicemetric-notes.xml`):**
  - No changes.
- **Search parameters (`bundle-DeviceMetric-search-params.xml`):**
  - No changes.
- **Operations (`list-DeviceMetric-operations.xml`):**
  - No changes.
- **Examples (`list-DeviceMetric-examples.xml`, `devicemetric-example.xml`, `devicemetric-examples-header.xml`):**
  - No changes.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - No changes to any of the 7 ValueSets or 6 CodeSystems shipped in
    the folder.

There are **no balloter-relevant substantive changes** to DeviceMetric
in this window. The only diff is a publisher-label correction.

## Proposed Ballot Note (HTML)

No substantive changes occurred in the window, so adding a ballot note
is not warranted. A ballot-note block is included below only as a
placeholder if the editor still wishes to acknowledge the publisher
relabel; recommendation is to **omit** it.

```html
<!-- Recommendation: do NOT add a ballot note for this window.
     The only change to DeviceMetric since 5d67a34a13a5 is a
     publisher-label correction in structuredefinition-DeviceMetric.xml
     (HL7 International / Health Care Devices → HL7 International /
     Devices). This is not a balloter-relevant substantive change. -->

<!-- Placeholder, only if editorial policy requires acknowledgement: -->
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made
  to DeviceMetric since the previous ballot. The only edit in this
  window is a publisher-label correction
  (<code>HL7 International / Health Care Devices</code> →
  <code>HL7 International / Devices</code>) in the
  StructureDefinition metadata; no elements, cardinalities, bindings,
  search parameters, operations, examples, or bound terminologies
  have changed.</p>
</blockquote>
```

## Notes for Reviewer

- **No ticket attribution.** The single in-window commit
  (`a9658ed97c2a`, "typos and bump kindling") carries no `FHIR-…` /
  `UTG-…` keys in subject or body, and `cross-referenced` returns no
  hits. This is consistent with an editorial sweep across many
  resources rather than a tracked work item.
- **Briefing staleness.** The briefing's recorded `clone_head_sha`
  (`1b369ff4e28e`) is behind the current clone HEAD
  (`db79dcdfe196`), but no DeviceMetric files were touched between
  those two SHAs (the only DeviceMetric edit in the full window is
  the publisher commit above), so the staleness does not affect this
  report. Consider refreshing the briefing if it ages further.
- **Recommendation.** No ballot-note insertion is warranted for this
  window. If the work group wishes to call out the publisher relabel,
  use the placeholder block above; otherwise leave
  `devicemetric-introduction.xml` unchanged.

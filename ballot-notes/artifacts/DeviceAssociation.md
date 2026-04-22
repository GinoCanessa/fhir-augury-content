# Artifact Ballot Note Draft: DeviceAssociation (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `DeviceAssociation` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 2 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `DeviceAssociation` for this run (resolved from
the briefing's authoring layout — `source/<name>/` per FhirCore
convention; folder name is lowercased per the repo's casing rules).

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/deviceassociation/structuredefinition-DeviceAssociation.xml` | StructureDefinition (canonical) | yes |
| `source/deviceassociation/deviceassociation-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/deviceassociation/deviceassociation-notes.xml` | Supplementary narrative | no |
| `source/deviceassociation/bundle-DeviceAssociation-search-params.xml` | Search parameters | no |
| `source/deviceassociation/list-DeviceAssociation-operations.xml` | Operations | no |
| `source/deviceassociation/list-DeviceAssociation-examples.xml` | Examples list | no |
| `source/deviceassociation/list-DeviceAssociation-packs.xml` | Resource packs list | no |
| `source/deviceassociation/deviceassociation-examples-header.xml` | Examples header | no |
| `source/deviceassociation/deviceassociation-example.xml` | Example | no |
| `source/deviceassociation/deviceassociation-bp-monitor-association.xml` | Example | no |
| `source/deviceassociation/deviceassociation-implant-association.xml` | Example | no |
| `source/deviceassociation/deviceassociation-lab-device-association.xml` | Example | no |
| `source/deviceassociation/deviceassociation-robot-association.xml` | Example | no |
| `source/deviceassociation/deviceassociation-tablet-association.xml` | Example | no |
| `source/deviceassociation/deviceassociation-wheelchair-association.xml` | Example | no |
| `source/deviceassociation/valueset-*.xml` | Artifact-scoped ValueSets (4) | no |
| `source/deviceassociation/codesystem-deviceassociation-association-status.xml` | Artifact-scoped CodeSystem | no |
| `source/deviceassociation/codesystem-deviceassociation-relationship.xml` | Artifact-scoped CodeSystem | no |
| `source/deviceassociation/codesystem-deviceassociation-status-reason.xml` | Artifact-scoped CodeSystem | yes |
| `source/deviceassociation/codesystem-deviceassociation-status.xml` | Artifact-scoped CodeSystem | no |
| `source/deviceassociation/deviceassociation.svg` | Diagram asset | no |

Patterns from the briefing that produced no match in the clone:

- `source/deviceassociation/deviceassociation-spreadsheet.xml` — no
  legacy spreadsheet present (StructureDefinition is authoritative).

## Current Ballot Note

The artifact's intro (`deviceassociation-introduction.xml`) carries a
single ballot note (`bn1`) at HEAD. A separate `stu-note` blockquote
was added in the window (it is not a ballot note and is reproduced
under the roll-up summary, not here).

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the DeviceAssociation resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Collapsed the DeviceAssociation.operation backbone into the other elements (e.g., DeviceAssociation.relationship now includes the operator role).</li>
<li>DeviceAssociation.category was renamed DeviceAssociation.relationship and given an extensible value set.</li>
<li>Added DeviceAssociation.associationStatus.</li>
<li>Updated search parameters to address the changes.</li>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53677](https://jira.hl7.org/browse/FHIR-53677) | .subject short description | [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) |
| [FHIR-53678](https://jira.hl7.org/browse/FHIR-53678) | value capitalization | [`aadb8b2a7870`](https://github.com/HL7/fhir/commit/aadb8b2a78701db164f8ad51952d9a240d8c9dda) |

The `b62975d9` commit ("More OO tickets") also references FHIR-55272,
FHIR-55257, and FHIR-54999 in its body, but the diff scoped to
`source/deviceassociation/` only contains FHIR-53677 work; the other
three tickets in that batch touch DeviceDefinition / Identifier /
BiologicallyDerivedProduct rather than DeviceAssociation and are out
of scope for this report.

## Per-Ticket Detail

### [FHIR-53677](https://jira.hl7.org/browse/FHIR-53677) — .subject short description

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Motion to:
  >
  > - Change in short description on DeviceAssociation.subject "The entity(ies) that the device is on or associated with" to: "The entity or group that the device is on or associated with"
  > - Also add in comments a statement indicating "if the device is associated with multiple individuals at the same time, that it has to be part of a Group or CareTeam resource".
  >
  > Integrate with updates resulting from FHIR-54470 and FHIR-53680 (which cannot drop the reference to "group").
  >
  > QA note: editorialized the comment to be "If the device is associated with multiple individuals at the same time the Group or CareTeam resource should be utilized."

- **Disposition summary:** Reword the `DeviceAssociation.subject`
  short label so it reflects the 0..1 cardinality (singular entity or
  Group), and append a comment clarifying that multi-individual
  associations should be expressed via `Group` or `CareTeam` rather
  than by repeating the element. Coordinate with FHIR-54470 and
  FHIR-53680 to avoid wording conflicts.
- **Commits applying this ticket:**
  - [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) — More OO tickets (2026-03-11)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-DeviceAssociation.xml`, the differential
  element `DeviceAssociation.subject` had its `short` updated from
  *"The entity(ies) that the device is on or associated with"* to
  *"The entity or group that the device is on or associated with"*,
  and an extra sentence was appended to its `comment`: *"If the
  device is associated with multiple individuals at the same time the
  Group or CareTeam resource should be utilized."* The intro file
  also gained a `stu-note` (`background-color: lightblue`) flagging
  this change as a release note pending FMG review (single bullet
  linking to FHIR-53677). No cardinality, type, binding, or
  invariant changes were made; snapshot regeneration is required to
  pick up the differential text.

### [FHIR-53678](https://jira.hl7.org/browse/FHIR-53678) — value capitalization

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will fix.

- **Disposition summary:** Capitalize the display of the `placed`
  concept in the DeviceAssociation status-reason CodeSystem so it
  matches the casing used by the other concepts in the value set.
- **Commits applying this ticket:**
  - [`aadb8b2a7870`](https://github.com/HL7/fhir/commit/aadb8b2a78701db164f8ad51952d9a240d8c9dda) — FHIR-53678 (2026-02-20)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `codesystem-deviceassociation-status-reason.xml`, the `display` of
  the `placed` concept was changed from `"placed"` to `"Placed"` (one
  line, +1/-1). The concept code, definition, and the rest of the
  CodeSystem are unchanged. The dependent `valueset-deviceassociation-status-reason.xml`
  uses code-system inclusion rather than enumerating displays, so no
  matching ValueSet edit is required.

## Roll-up Summary (after-applied state)

Window stats:

```
codesystem-deviceassociation-status-reason.xml | 2 +-
deviceassociation-introduction.xml             | 6 ++++++
structuredefinition-DeviceAssociation.xml      | 4 ++--
3 files changed, 9 insertions(+), 3 deletions(-)
```

- **StructureDefinition (`structuredefinition-DeviceAssociation.xml`):**
  Single differential edit on `DeviceAssociation.subject` — `short`
  reworded ("entity(ies)" → "entity or group") and `comment` extended
  with a sentence directing multi-individual cases to `Group` /
  `CareTeam`. No element added or removed; no cardinality, type,
  binding, or constraint changes. Snapshot must be regenerated by the
  publisher.
- **Intro / narrative (`deviceassociation-introduction.xml`,
  `deviceassociation-notes.xml`):** A new `stu-note` blockquote
  (light-blue background, marked *"Release Notes (pending alternative
  process review with FMG)"*) was added immediately after the
  existing `bn1` ballot note, listing FHIR-53677. The existing ballot
  note (`bn1`) and the rest of the narrative (Scope and Usage,
  Boundaries and Relationships) are unchanged. `deviceassociation-notes.xml`
  is unchanged.
- **Search parameters (`bundle-DeviceAssociation-search-params.xml`):**
  No changes in window.
- **Operations (`list-DeviceAssociation-operations.xml`):** No changes
  in window.
- **Examples:** No example added, removed, or modified; the
  `subject` wording change does not affect example instances.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** Display
  capitalization fix in `codesystem-deviceassociation-status-reason.xml`
  (`placed` → `Placed`). The other three CodeSystems
  (`association-status`, `relationship`, `status`) and all four
  artifact-scoped ValueSets are unchanged. No cross-repo terminology
  movement to UTG is implied.

## Proposed Ballot Note (HTML)

The existing `bn1` summarises the R5→R6 substantive shape of the
resource and remains accurate; it is preserved verbatim. A new `bn2`
records the in-window touch-ups (subject wording + status-reason
display capitalization) so balloters reviewing this draft can see
what changed since the previous ballot.

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the DeviceAssociation resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Collapsed the DeviceAssociation.operation backbone into the other elements (e.g., DeviceAssociation.relationship now includes the operator role).</li>
<li>DeviceAssociation.category was renamed DeviceAssociation.relationship and given an extensible value set.</li>
<li>Added DeviceAssociation.associationStatus.</li>
<li>Updated search parameters to address the changes.</li>
</ul>
</blockquote>
<blockquote class="ballot-note" id="bn2">
<p><b>Note to Balloters:</b> Since the previous ballot snapshot, the only changes to DeviceAssociation are minor clarifications &mdash; no elements, cardinalities, types, bindings, search parameters, operations, or examples have been added or removed. Specifically:</p>
<ul>
<li>Reworded the <code>DeviceAssociation.subject</code> short label from &ldquo;The entity(ies) that the device is on or associated with&rdquo; to &ldquo;The entity or group that the device is on or associated with&rdquo; to better reflect its 0..1 cardinality, and extended the element comment to direct implementers to use <code>Group</code> or <code>CareTeam</code> when a device is associated with multiple individuals at the same time (<a href="https://jira.hl7.org/browse/FHIR-53677">FHIR-53677</a>).</li>
<li>Corrected the display of the <code>placed</code> concept in the DeviceAssociation status-reason CodeSystem to <code>Placed</code> so its capitalization matches the other concepts in the value set (<a href="https://jira.hl7.org/browse/FHIR-53678">FHIR-53678</a>).</li>
</ul>
</blockquote>
```

## Notes for Reviewer

- The intro file currently also carries a `stu-note` blockquote
  (light-blue background) listing FHIR-53677 as a "Release Notes
  (pending alternative process review with FMG)" entry. It is not a
  ballot note and is left in place; if FMG decides the alternative
  process governs this release-note channel, the proposed `bn2`
  bullet for FHIR-53677 may become redundant and could be dropped.
- Commit `b62975d9` ("More OO tickets") references three additional
  tickets in its body — FHIR-55272, FHIR-55257, FHIR-54999 — but the
  diff scoped to `source/deviceassociation/` is empty for all three.
  Those tickets apply to other Orders & Observations artifacts (the
  Identifier element on a sibling resource, DeviceDefinition's
  regulatoryIdentifier value set, and BiologicallyDerivedProduct
  grouping identifiers respectively) and are deliberately not cited
  in the proposed ballot note.
- `cross-referenced` returned no hits for either commit SHA; ticket
  attribution above is taken from the commit messages themselves
  (`(FHIR|UTG)-\d+` regex) and confirmed by inspecting the
  per-commit diffs.
- The clone HEAD (`db79dcdfe196`) is a descendant of the
  since-commit; the standard `since..HEAD` range was used (no
  symmetric-difference fallback required).
- `gh` was not needed; all data came from the cached clone via `git`
  and from `fhir-augury-cli`.

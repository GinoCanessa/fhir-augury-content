# Artifact Ballot Note Draft: BodyStructure (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `BodyStructure` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 2 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `BodyStructure` for this run (resolved from the
FhirCore `source/<name>/` convention; the briefing's Artifact Map does
not enumerate per-resource paths for `BodyStructure`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/bodystructure/structuredefinition-BodyStructure.xml` | StructureDefinition | yes |
| `source/bodystructure/bodystructure-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/bodystructure/bodystructure-notes.xml` | Supplementary narrative | no |
| `source/bodystructure/bodystructure-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/bodystructure/bundle-BodyStructure-search-params.xml` | Search parameters | no |
| `source/bodystructure/list-BodyStructure-operations.xml` | Operations | no |
| `source/bodystructure/list-BodyStructure-examples.xml` | Examples list | no |
| `source/bodystructure/list-BodyStructure-packs.xml` | Packs list | no |
| `source/bodystructure/bodystructure-examples-header.xml` | Examples header | no |
| `source/bodystructure/bodystructure-example.xml` | Example | no |
| `source/bodystructure/bodystructure-example-fetus.xml` | Example | no |
| `source/bodystructure/bodystructure-example-skin-patch.xml` | Example | no |
| `source/bodystructure/bodystructure-example-tumor.xml` | Example | no |
| `source/bodystructure/bodystructure-example-dicom-includedStructure.xml` | Example | no |
| `source/bodystructure/valueset-body-site.xml` | Artifact-scoped ValueSet | no |
| `source/bodystructure/valueset-bodystructure-bodylandmarkorientation-clockface-position.xml` | Artifact-scoped ValueSet | no |
| `source/bodystructure/valueset-bodystructure-bodylandmarkorientation-distancefromlandmark-device.xml` | Artifact-scoped ValueSet | no |
| `source/bodystructure/valueset-bodystructure-code.xml` | Artifact-scoped ValueSet | no |
| `source/bodystructure/valueset-bodystructure-laterality.xml` | Artifact-scoped ValueSet | no |
| `source/bodystructure/valueset-bodystructure-relative-location.xml` | Artifact-scoped ValueSet | no |

Patterns that produced no match in the clone:

- `source/bodystructure/bodystructure-spreadsheet.xml` — no legacy spreadsheet (SD is authoritative).
- `source/bodystructure/codesystem-*.xml` — no artifact-scoped CodeSystems.
- Sibling `structuredefinition-*.xml` other than the canonical SD — none.

## Current Ballot Note

Two ballot-note-style blockquotes exist at HEAD inside
`bodystructure-introduction.xml`. Only the first carries the
`class="ballot-note"` marker; the second is an interim
"Release Notes" placeholder added during this window:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
<ul>
 <li>BodyStructure.morphology has been moved to BodyStructure.includedStructure.morphology</li>
 <li>Added BodyStructure.includedStructure.image to provide an image of the includedStructure or excludedStructure.</li>
</ul>
</blockquote>
<blockquote style="background-color: lightblue">
    <p><b>Release Notes (pending alternative process review with FMG):</b></p>
    <ul>
        <li><a href="https://jira.hl7.org/browse/FHIR-54844">FHIR-54844</a></li>
        <li><a href="https://jira.hl7.org/browse/FHIR-54450">FHIR-54450</a></li>
   </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54450](https://jira.hl7.org/browse/FHIR-54450) | Allow BodyStructure.patient to be omitted | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) |
| [FHIR-54844](https://jira.hl7.org/browse/FHIR-54844) | Typo - remove double "the" | [`48f5a88a6a46`](https://github.com/HL7/fhir/commit/48f5a88a6a460d9acde9ba4c42cd2fc0d37d6135), [`fe97e98cd529`](https://github.com/HL7/fhir/commit/fe97e98cd529ad0810fbabb99b18cf0b75e5c7cb) |

`fhir-augury-cli cross-referenced` returned no hits for any of the three
commit SHAs; ticket attribution is derived from the commit messages and
from the explicit Jira links added to the intro file by each commit.

## Per-Ticket Detail

### [FHIR-54450](https://jira.hl7.org/browse/FHIR-54450) — Allow BodyStructure.patient to be omitted

- **Work group:** Orders & Observations
- **Specification:** FHIR Core (FHIR)
- **Type / Priority:** Change Request / Highest
- **Status / Resolution:** Applied / Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only ticket comment is a
  > pointer to the implementing PR ([HL7/fhir#4037](https://github.com/HL7/fhir/pull/4037)).
  > Reporter rationale (from the description): some uses of BodyStructure
  > (e.g., imaging protocols / procedure definitions) are not patient-
  > specific, and resources that reference BodyStructure (Observation,
  > ImagingStudy, …) already carry their own Patient reference, so the
  > inner reference is duplicative or potentially conflicting. Suggested
  > to relax `BodyStructure.patient` from `1..1` to `0..1`.

- **Disposition summary:** Persuasive — the work group accepted the
  request to make `BodyStructure.patient` optional so that BodyStructure
  instances can describe protocol- or definition-scoped anatomy that is
  not bound to a single patient.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — "OO tickets first draft" (2026-03-24)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-BodyStructure.xml`, the differential entry
  for `BodyStructure.patient` had its `<min>` lowered from `1` to `0`
  (max remains `1`); the element's `short` ("Who this is about") and
  `definition` are unchanged. The same commit also added an interim
  "Release Notes" `<blockquote class="stu-note">` to
  `bodystructure-introduction.xml` listing this ticket; that placeholder
  was later restyled by `fe97e98c` (see FHIR-54844 / Notes for
  Reviewer). Snapshot regeneration is required to propagate the new
  cardinality.

### [FHIR-54844](https://jira.hl7.org/browse/FHIR-54844) — Typo - remove double "the"

- **Work group:** Orders & Observations
- **Specification:** FHIR Core (FHIR)
- **Type / Priority:** Technical Correction / Medium
- **Status / Resolution:** Applied / Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only ticket comment is a
  > pointer to the implementing PR ([HL7/fhir#4017](https://github.com/HL7/fhir/pull/4017)).
  > Description: remove one "the" from "*When needed, it allows the the
  > representation …*" in the BodyStructure scope text.

- **Disposition summary:** Persuasive — accept the typo fix in the
  Scope and Usage paragraph of `bodystructure-introduction.xml`.
- **Commits applying this ticket:**
  - [`48f5a88a6a46`](https://github.com/HL7/fhir/commit/48f5a88a6a460d9acde9ba4c42cd2fc0d37d6135) — "FHIR-54844: Remove duplicate 'the' in BodyStructure scope text" (2026-02-28)
  - [`fe97e98cd529`](https://github.com/HL7/fhir/commit/fe97e98cd529ad0810fbabb99b18cf0b75e5c7cb) — "added headers" (2026-03-31)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Commit `48f5a88a6a46` deletes the duplicated "the" so the sentence
  now reads "*it allows the representation of complex body structures
  …*". Commit `fe97e98c` re-shapes the interim release-notes blockquote
  that `d2dde0c4` had introduced (see FHIR-54450), promoting it to a
  generic `<blockquote style="background-color: lightblue">` carrying
  the Jira link for FHIR-54844 alongside the existing FHIR-54450 link.
  No element-level changes are made by either commit.

## Roll-up Summary (after-applied state)

Authoritative summary derived from the `5d67a34a13a5..db79dcdfe196`
diff scoped to `source/bodystructure/`. Two files changed; nine
insertions, two deletions overall.

- **StructureDefinition (`structuredefinition-BodyStructure.xml`):**
  - `BodyStructure.patient` cardinality relaxed from `1..1` to `0..1`
    in the differential. Type, short, and definition are unchanged.
    Snapshot regeneration is required.
  - No other element / type / binding / constraint changes.
- **Intro / narrative (`bodystructure-introduction.xml`):**
  - Existing `class="ballot-note"` `bn1` (R5 → Normative summary
    bullets about `morphology` moving to
    `includedStructure.morphology` and the new
    `includedStructure.image`) is unchanged in the after-applied
    state — those R5 changes are still in effect for the Normative
    ballot.
  - A new `<blockquote style="background-color: lightblue">` titled
    "Release Notes (pending alternative process review with FMG)" was
    added immediately below `bn1`, listing FHIR-54844 and FHIR-54450
    as bare Jira links. This is interim editorial scaffolding rather
    than a finished ballot note.
  - Scope-and-Usage paragraph: duplicated "the" removed
    ("*allows the the representation*" → "*allows the
    representation*").
- **Supplementary narrative (`bodystructure-notes.xml`):** no changes.
- **Search parameters (`bundle-BodyStructure-search-params.xml`):**
  no changes.
- **Operations (`list-BodyStructure-operations.xml`):** no changes.
- **Examples (`list-BodyStructure-examples.xml` and the
  `bodystructure-example*.xml` files):** no changes; no example
  updates required because the only SD change is a relaxation of an
  existing cardinality (existing examples that populate `patient`
  remain valid; no example needs to demonstrate the omitted-patient
  case).
- **Terminology (artifact-scoped `valueset-*.xml`):** no changes;
  no cross-repo (UTG) terminology touch points triggered by this
  window.

## Proposed Ballot Note (HTML)

The proposed update keeps the existing `bn1` framing (still
applicable to the Normative ask) and adds a substantive bullet for the
`patient` cardinality relaxation. The pure typo fix (FHIR-54844) is
not surfaced in the ballot note — it is a non-substantive technical
correction and balloters do not need to be alerted to it. The interim
"Release Notes" blockquote should be removed in favour of folding the
real change into `bn1`.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes since R5 include:</p>
  <ul>
    <li><code>BodyStructure.morphology</code> has been moved to <code>BodyStructure.includedStructure.morphology</code>.</li>
    <li>Added <code>BodyStructure.includedStructure.image</code> to provide an image of the included or excluded structure.</li>
    <li><code>BodyStructure.patient</code> has been relaxed from <code>1..1</code> to <code>0..1</code> so that BodyStructure instances can describe protocol- or definition-scoped anatomy (for example, an imaging protocol or procedure definition) that is not bound to a specific patient. Resources that reference BodyStructure already carry their own patient context where one is required (<a href="https://jira.hl7.org/browse/FHIR-54450">FHIR-54450</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The interim `<blockquote style="background-color: lightblue">`
  ("Release Notes (pending alternative process review with FMG)")
  added by commits `d2dde0c4` and `fe97e98c` should be **removed**
  when the proposed `bn1` revision above is applied — its only
  substantive content (the FHIR-54450 link) is now folded into the
  ballot note bullet, and FHIR-54844 is a non-substantive typo fix
  that does not warrant a balloter callout.
- `FHIR-54844` (typo) is intentionally **not** surfaced as a bullet in
  the proposed ballot note. If the work group prefers to retain a
  full release-notes log separate from the balloter note, restore the
  blockquote with both Jira links but keep `bn1` focused on
  substantive change.
- `cross-referenced` returned no hits for any of the three commits,
  so ticket attribution relies on the commit subjects and on the
  Jira links inserted into `bodystructure-introduction.xml`. Commit
  `d2dde0c4` ("OO tickets first draft") lists seven Jira keys in its
  body (FHIR-56060, FHIR-55277, FHIR-54961, FHIR-54593, FHIR-54450,
  FHIR-54323, FHIR-53457); only FHIR-54450 actually touches
  BodyStructure files in that commit, so the others are out of
  scope for this artifact and are listed here only for traceability.
- Neither ticket has a recorded applied-vote / disposition comment in
  Jira; the only comments are PR pointers
  ([#4017](https://github.com/HL7/fhir/pull/4017) for FHIR-54844,
  [#4037](https://github.com/HL7/fhir/pull/4037) for FHIR-54450).
- The cached briefing
  (`cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @
  clone `1b369ff4e28e`) is slightly behind the current cache HEAD
  (`db79dcdfe196`); it remains within the FhirCore staleness
  tolerance and was used as-is. The briefing does not contain a
  per-resource Artifact Map entry for BodyStructure, so the source
  file list above was resolved from the standard
  `source/<name>/` FhirCore patterns.
- The roll-up window is a clean fast-forward range
  (`5d67a34a13a5..db79dcdfe196`); no symmetric-difference fallback
  was needed, and `gh` was not invoked.

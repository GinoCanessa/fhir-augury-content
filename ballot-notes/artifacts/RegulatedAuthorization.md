# Artifact Ballot Note Draft: RegulatedAuthorization (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `RegulatedAuthorization` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 1 (FHIR-55053) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `RegulatedAuthorization` for this run. The
briefing's Artifact Map does not contain an explicit entry for
`RegulatedAuthorization`, so the standard FhirCore folder layout
(`source/regulatedauthorization/`) was applied; every file below
exists in the cache clone at HEAD.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/regulatedauthorization/structuredefinition-RegulatedAuthorization.xml` | StructureDefinition (canonical) | yes |
| `source/regulatedauthorization/regulatedauthorization-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/regulatedauthorization/regulatedauthorization-notes.xml` | Supplementary narrative | no |
| `source/regulatedauthorization/bundle-RegulatedAuthorization-search-params.xml` | Search parameters bundle | no |
| `source/regulatedauthorization/list-RegulatedAuthorization-operations.xml` | Operations list | no |
| `source/regulatedauthorization/list-RegulatedAuthorization-examples.xml` | Examples list | no |
| `source/regulatedauthorization/list-RegulatedAuthorization-packs.xml` | Packs list | no |
| `source/regulatedauthorization/regulatedauthorization-example.xml` | Example | no |
| `source/regulatedauthorization/regulatedauthorization-example-basic-drug-auth.xml` | Example (basic drug auth) | no |
| `source/regulatedauthorization/regulatedauthorization-examples-header.xml` | Examples header narrative | no |
| `source/regulatedauthorization/regulatedauthorization-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/regulatedauthorization/codesystem-product-intended-use.xml` | Artifact-scoped CodeSystem | no |
| `source/regulatedauthorization/codesystem-regulated-authorization-basis.xml` | Artifact-scoped CodeSystem | no |
| `source/regulatedauthorization/codesystem-regulated-authorization-case-type.xml` | Artifact-scoped CodeSystem | no |
| `source/regulatedauthorization/codesystem-regulated-authorization-type.xml` | Artifact-scoped CodeSystem | no |
| `source/regulatedauthorization/valueset-product-intended-use.xml` | Artifact-scoped ValueSet | no |
| `source/regulatedauthorization/valueset-regulated-authorization-basis.xml` | Artifact-scoped ValueSet | no |
| `source/regulatedauthorization/valueset-regulated-authorization-case-type.xml` | Artifact-scoped ValueSet | no |
| `source/regulatedauthorization/valueset-regulated-authorization-type.xml` | Artifact-scoped ValueSet | no |

Patterns from the standard layout that produced no match in the clone:

- `source/regulatedauthorization/regulatedauthorization-spreadsheet.xml` — no file matched (this resource is SD-authoritative; no legacy spreadsheet is shipped).
- Sibling `structuredefinition-*.xml` files whose stem differs from the folder name — none present.

## Current Ballot Note

A ballot note (`bn1`) was added to the introduction file inside this
window — i.e., HEAD already carries an updated ballot note. The
verbatim block is:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since the last R6 ballot are:</p>
<ul>
    <li>Updates to the following elements:</li>
        <ul>
            <li>RegulatedAuthorization.case.identifier, which was made 0..* (previously 0..1)</li>
        </ul>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55053](https://jira.hl7.org/browse/FHIR-55053) | RegulatedAuthorization.case.identifier should repeat | [`d9f80a31f5a0`](https://github.com/HL7/fhir/commit/d9f80a31f5a0ba45ab943bc69fd5e4d04ea4dcf0), [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) |

Commits `f0c7b541c736` and `d9f80a31f5a0` both reference FHIR-55053.
The same intro-file commit (`f0c7b541c736`) also names FHIR-55057
(SubstanceDefinition) and FHIR-55046 (Ingredient), but those tickets
do not change any file under `source/regulatedauthorization/`; they
only land in the ballot-note paragraph for `RegulatedAuthorization`
because the author co-located the per-resource narrative updates in
one commit. Their per-resource impact is captured in the
SubstanceDefinition and Ingredient artifact reports, not here.

No commits in the window are unattributed.

## Per-Ticket Detail

### [FHIR-55053](https://jira.hl7.org/browse/FHIR-55053) — RegulatedAuthorization.case.identifier should repeat

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive (Resolved - change required, 2026-04-07)
- **Disposition (verbatim):**

  > change maximal cardinality of identifier to *

  (Disposition recorded as the Jira `resolution_description`; no
  applied-vote comment is present on the issue.)

- **Disposition summary:** The reporter (Lloyd McKenzie) noted that
  identifiers can almost always be assigned by multiple entities over
  time, yet `RegulatedAuthorization.case.identifier` was constrained
  to 0..1. The work group accepted the change request as Persuasive
  and asked for the upper cardinality of the element to be widened
  from `1` to `*`.
- **Commits applying this ticket:**
  - [`d9f80a31f5a0`](https://github.com/HL7/fhir/commit/d9f80a31f5a0ba45ab943bc69fd5e4d04ea4dcf0) — FHIR-55053 RegulatedAuthorization.case.identifier to 0..* for 0..1 (2026-04-16T17:14:10+01:00, riksmithies)
  - [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) — resource introduction updates for FHIR-55057 / FHIR-55053 / FHIR-55046 (2026-04-16T19:28:02+01:00, riksmithies)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Commit `d9f80a31f5a0` edits the `<differential>` of
  `structuredefinition-RegulatedAuthorization.xml` for the
  `RegulatedAuthorization.case.identifier` element, changing
  `<max value="1"/>` to `<max value="*"/>`. The element's `short`,
  `definition`, and `type` (Identifier) are unchanged. Commit
  `f0c7b541c736` adds the new `bn1` `<blockquote class="ballot-note">`
  to `regulatedauthorization-introduction.xml`, calling out this same
  cardinality change for balloters. The SD `<snapshot>` is derived
  and will need regeneration to mirror the differential change.

## Roll-up Summary (after-applied state)

Across `source/regulatedauthorization/`, only two files are touched
between `5d67a34a13a5` and `db79dcdfe196`:

- **StructureDefinition (`structuredefinition-RegulatedAuthorization.xml`):**
  - `RegulatedAuthorization.case.identifier` — upper cardinality
    relaxed from `0..1` to `0..*`. No other element-level changes
    (no type changes, no binding changes, no new or removed
    constraints, no `mustSupport` flips). Snapshot regeneration is
    required so that the published snapshot mirrors the differential.
- **Intro / narrative (`regulatedauthorization-introduction.xml`):**
  - A new `<blockquote class="ballot-note" id="bn1">` is inserted
    immediately after the Medication Definition module banner. It
    frames the artifact as targeting Normative status for this ballot
    cycle and lists the `case.identifier` cardinality change as the
    only substantive change since the prior R6 ballot. It does **not**
    cite the FHIR-55053 ticket inline.
  - No prose outside the new ballot-note block is changed.
- **Supplementary narrative (`regulatedauthorization-notes.xml`):** no
  changes.
- **Search parameters (`bundle-RegulatedAuthorization-search-params.xml`):**
  no changes.
- **Operations (`list-RegulatedAuthorization-operations.xml`):** no
  changes.
- **Examples (`list-RegulatedAuthorization-examples.xml`,
  `regulatedauthorization-example*.xml`,
  `regulatedauthorization-examples-header.xml`):** no changes. The
  existing examples already use single `case.identifier` values, so
  the relaxed cardinality does not require example updates, but
  reviewers may want to add an example illustrating multiple
  identifiers for a single case.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** no changes.
- **Other (`list-RegulatedAuthorization-packs.xml`,
  `regulatedauthorization-fivews-mapping-exceptions.xml`,
  `regulatedauthorization.svg`):** no changes.

## Proposed Ballot Note (HTML)

The existing `bn1` already reflects the only after-applied change in
the window. The proposed note retains its substance and its framing
("ready for Normative status, seeking ballot comment on the
substantive content"), tightens the bullet structure (the previous
nested `<ul>` inside an `<li>` is not valid HTML), and adds an inline
Jira citation to FHIR-55053 against the bullet it supports.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. Since the previous R6 ballot the only substantive change is the relaxation of a single cardinality:</p>
  <ul>
    <li><code>RegulatedAuthorization.case.identifier</code> upper cardinality changed from <code>0..1</code> to <code>0..*</code>, allowing multiple identifiers to be assigned to the same case (e.g., by different regulators or over time) (<a href="https://jira.hl7.org/browse/FHIR-55053">FHIR-55053</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The current `bn1` block in `regulatedauthorization-introduction.xml`
  contains a nested `<ul>` placed directly inside an `<li>` whose own
  text reads "Updates to the following elements:". This produces
  invalid HTML structure (a `<ul>` is not phrasing content for an
  `<li>`'s text run). The proposed note flattens this into a single
  bullet to fix the structure and to make the ticket citation
  inline-readable.
- The ballot note cites only FHIR-55053 because that is the only
  ticket whose changes land in `source/regulatedauthorization/`
  in the window. Commit `f0c7b541c736` co-locates intro updates for
  FHIR-55057 (SubstanceDefinition) and FHIR-55046 (Ingredient); those
  belong in the corresponding SubstanceDefinition and Ingredient
  ballot-note drafts, not here.
- The snapshot inside `structuredefinition-RegulatedAuthorization.xml`
  was not edited in either commit; per the FhirCore convention the
  snapshot is derived from the differential and will be regenerated
  by the publisher. No narration of snapshot edits is included.
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit
  (`5d67a34a13a5`); the standard `since..HEAD` range was used and no
  symmetric-difference fallback was needed.
- `fhir-augury-cli cross-referenced` returned zero hits for both
  commit SHAs, so ticket attribution relied entirely on the
  `(FHIR|UTG)-\d+` regex against the commit subjects/bodies.
- Jira FHIR-55053 has no comments recorded in the snapshot, so the
  applied-vote disposition text was unavailable; the
  `resolution_description` field is quoted instead.

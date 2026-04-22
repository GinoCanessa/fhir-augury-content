# Artifact Ballot Note Draft: SpecimenDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `SpecimenDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `SpecimenDefinition` for this run (based on the
FhirCore authoring layout under `source/specimendefinition/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/specimendefinition/structuredefinition-SpecimenDefinition.xml` | StructureDefinition (canonical) | yes |
| `source/specimendefinition/specimendefinition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/specimendefinition/specimendefinition-notes.xml` | Supplementary narrative | no |
| `source/specimendefinition/bundle-SpecimenDefinition-search-params.xml` | Search parameters bundle | no |
| `source/specimendefinition/list-SpecimenDefinition-operations.xml` | Operations list | no |
| `source/specimendefinition/operationdefinition-SpecimenDefinition-apply.xml` | `$apply` OperationDefinition | no |
| `source/specimendefinition/list-SpecimenDefinition-examples.xml` | Examples list | no |
| `source/specimendefinition/list-SpecimenDefinition-packs.xml` | Packs list | no |
| `source/specimendefinition/specimendefinition-example.xml` | Example | no |
| `source/specimendefinition/specimendefinition-example-serum-plasma.xml` | Example | no |
| `source/specimendefinition/specimen-example-serum-plasma.xml` | Companion Specimen example | no |
| `source/specimendefinition/apply-operation-response-example.xml` | `$apply` response example | no |
| `source/specimendefinition/specimendefinition-examples-header.xml` | Examples page header | no |
| `source/specimendefinition/specimendefinition-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | no |
| `source/specimendefinition/codesystem-specimen-contained-preference.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/specimendefinition/valueset-*.xml` | Artifact-scoped ValueSets (8) | no |

Patterns from the FhirCore briefing that produced no match in the clone:

- `source/specimendefinition/specimendefinition-spreadsheet.xml` — no file matched (artifact uses the SD as the sole authoritative source).
- `source/specimendefinition/specimendefinition-notes-*.xml` — no additional notes files matched.

## Current Ballot Note

No existing `<blockquote class="ballot-note">` is present in
`source/specimendefinition/specimendefinition-introduction.xml` at HEAD.
The file currently carries a `stu-note` "Release Notes" block (added in
this window) that lists the single relevant Jira ticket but is not
formatted as a ballot note:

```html
<blockquote class="stu-note" style="background-color: lightblue">
        <p><b>Release Notes (pending alternative process review with FMG):</b></p>
        <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55277">FHIR-55277</a></li>
        </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55277](https://jira.hl7.org/browse/FHIR-55277) | SpecimenDefinition.identifier should repeat | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) |

The single commit in the window (`d2dde0c4a093` — "OO tickets first
draft") references seven Orders & Observations tickets in its body
(FHIR-56060, FHIR-55277, FHIR-54961, FHIR-54593, FHIR-54450,
FHIR-54323, FHIR-53457). Of these, only **FHIR-55277** edits files
under `source/specimendefinition/`; the remaining tickets touched
sibling OO artifacts (e.g., Specimen, ServiceRequest, Observation) and
are out of scope for this artifact.

## Per-Ticket Detail

### [FHIR-55277](https://jira.hl7.org/browse/FHIR-55277) — SpecimenDefinition.identifier should repeat

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only comment captured
  > on the ticket is the implementation PR link
  > (<https://github.com/HL7/fhir/pull/4037>). The committed change
  > matches the ticket's stated request — promote
  > `SpecimenDefinition.identifier` from a single value to a repeating
  > element — consistent with a "Persuasive with Modification"
  > resolution and the `R6-Release-note` label.

- **Disposition summary:** Identifiers can be assigned to a
  SpecimenDefinition by multiple stewards over time (laboratory,
  catalog publisher, regulator, etc.), so the element should not be
  constrained to a single occurrence. The disposition raises
  `SpecimenDefinition.identifier` cardinality from `0..1` to `0..*` and
  updates the `short`/`definition` text to describe a collection of
  business identifiers rather than a single one.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — "OO tickets first draft" (2026-03-24, ssi-db)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-SpecimenDefinition.xml`, the
  `SpecimenDefinition.identifier` element's `max` cardinality was
  changed from `1` to `*`; its `short` text was updated from
  "Business identifier" to "Business identifiers of the
  SpecimenDefinition"; and its `definition` was updated from "A
  business identifier assigned to this SpecimenDefinition." to
  "Business identifiers assigned to this SpecimenDefinition." In
  `specimendefinition-introduction.xml`, a `stu-note` "Release Notes"
  block was prepended that links to FHIR-55277 (no balloter-facing
  content beyond the link). The SD's `<snapshot>` was not regenerated
  in this commit and will need to be rebuilt before publication.

## Roll-up Summary (after-applied state)

The window contains a single substantive change to the
SpecimenDefinition resource:

- **StructureDefinition (`structuredefinition-SpecimenDefinition.xml`):**
  - `SpecimenDefinition.identifier` differential: `max` raised from
    `1` to `*` (now `0..*`); `short` updated to "Business identifiers
    of the SpecimenDefinition"; `definition` updated to the plural
    "Business identifiers assigned to this SpecimenDefinition." Type
    (`Identifier`) and `min` (`0`) are unchanged. No other elements
    were modified in the differential.
  - `<snapshot>` was not edited in this commit — snapshot
    regeneration is required before publication.
- **Intro / narrative (`specimendefinition-introduction.xml`,
  `specimendefinition-notes.xml`):** A `stu-note` "Release Notes
  (pending alternative process review with FMG)" block was added at
  the top of the introduction, listing FHIR-55277 only. Scope and
  Usage and Boundaries and Relationships content is unchanged. The
  notes file was not modified.
- **Search parameters (`bundle-SpecimenDefinition-search-params.xml`):**
  No changes. (Note: the existing `identifier` search parameter, which
  is already defined as a token search across the resource, continues
  to work for the now-repeating element without modification.)
- **Operations (`list-SpecimenDefinition-operations.xml`,
  `operationdefinition-SpecimenDefinition-apply.xml`):** No changes.
- **Examples:** No changes. None of the bundled examples
  (`specimendefinition-example.xml`,
  `specimendefinition-example-serum-plasma.xml`, the companion
  Specimen example, or the `$apply` response example) needed updates,
  as a `0..1` instance remains valid under `0..*`.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No
  changes to any of the eight artifact-scoped ValueSets or to
  `codesystem-specimen-contained-preference`.

## Proposed Ballot Note (HTML)

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Since the previous ballot, the only
  substantive change to SpecimenDefinition is to allow more than one
  business identifier on a SpecimenDefinition instance. Catalog,
  scope-and-usage, search-parameter, operation, example, and
  terminology content are otherwise unchanged.</p>
  <ul>
    <li><code>SpecimenDefinition.identifier</code> has been changed
    from <code>0..1</code> to <code>0..*</code>, with the
    <code>short</code> and <code>definition</code> text updated to
    refer to identifiers in the plural. This recognises that
    identifiers for a SpecimenDefinition may be assigned by multiple
    stewards (publishing laboratory, catalog publisher, regulator,
    etc.) over the artifact's lifecycle
    (<a href="https://jira.hl7.org/browse/FHIR-55277">FHIR-55277</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- There was no previous `ballot-note` block on this artifact, so no
  prior bullets needed to be carried forward, revised, or dropped.
- The single commit in the window (`d2dde0c4a093` — "OO tickets first
  draft") bundles work for seven OO tickets. Only **FHIR-55277**
  touched files under `source/specimendefinition/`; the other six
  tickets (FHIR-56060, FHIR-54961, FHIR-54593, FHIR-54450, FHIR-54323,
  FHIR-53457) modified sibling OO artifacts and have been excluded
  from this artifact's report. They should appear in the ballot notes
  for the resources they actually modified (e.g., Specimen,
  ServiceRequest, Observation) where applicable.
- The committed `stu-note` "Release Notes" block in the introduction
  is a tracking aid pending FMG review of an alternative release-notes
  process; it is not a ballot note and is not a substitute for the
  proposed `ballot-note` block above. The two can coexist, or the
  `stu-note` block can be removed once the formal ballot note is in
  place — that decision is for the work group and FMG.
- The `<snapshot>` in `structuredefinition-SpecimenDefinition.xml` was
  not regenerated as part of this change; snapshot regeneration is
  required before publication.
- `fhir-augury-cli cross-referenced` returned no hits for the commit
  SHA, so ticket attribution was derived from the Jira links listed in
  the commit body (verified against the per-file diff).
- The Jira ticket's "applied vote" / disposition text is not present
  in the captured ticket payload (only a PR link comment was
  recorded); the disposition summary above is reconstructed from the
  ticket title, description, resolution (`Persuasive with
  Modification`), and the after-applied diff.

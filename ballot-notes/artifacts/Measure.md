# Artifact Ballot Note Draft: Measure (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Measure` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 7 |
| Tickets attributed | 5 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `Measure` for this run (folder `source/measure/`,
patterns from the FhirCore briefing's Artifact Map). "Touched in window"
indicates whether the file changed between the since-commit and HEAD.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/measure/structuredefinition-Measure.xml` | StructureDefinition (canonical) | yes |
| `source/measure/measure-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/measure/measure-notes.xml` | Supplementary narrative | no |
| `source/measure/bundle-Measure-search-params.xml` | Search parameters bundle | yes |
| `source/measure/list-Measure-operations.xml` | Operations list | no |
| `source/measure/list-Measure-examples.xml` | Examples list | no |
| `source/measure/list-Measure-packs.xml` | Implementation guide pack list | no |
| `source/measure/operationdefinition-Measure-care-gaps.xml` | OperationDefinition `$care-gaps` | yes |
| `source/measure/operationdefinition-Measure-collect-data.xml` | OperationDefinition `$collect-data` | yes |
| `source/measure/operationdefinition-Measure-data-requirements.xml` | OperationDefinition `$data-requirements` | no |
| `source/measure/operationdefinition-Measure-evaluate.xml` | OperationDefinition `$evaluate` | yes |
| `source/measure/operationdefinition-Measure-evaluate-measure.xml` | OperationDefinition `$evaluate-measure` (legacy) | no |
| `source/measure/operationdefinition-Measure-submit-data.xml` | OperationDefinition `$submit-data` | no |
| `source/measure/measure-*example*.xml`, `measure-cms146-example.xml`, `measure-EXM55-FHIR.xml`, `measure-BCSComponent.xml`, `measure-exclusive-breastfeeding.xml`, `measure-hiv-indicators.xml`, `measure-hybrid-hospital-wide-mortality.xml` | Resource examples | no |
| `source/measure/codesystem-measure-stratifier-type-example.xml` | Artifact-scoped CodeSystem (added in window) | yes (added) |
| `source/measure/codesystem-measure-definition-example.xml`, `codesystem-measure-group-example.xml`, `codesystem-measure-supplemental-data-example.xml` | Artifact-scoped CodeSystems (3 unchanged) | no |
| `source/measure/valueset-measure-stratifier-type-example.xml` | Artifact-scoped ValueSet (added in window) | yes (added) |
| `source/measure/valueset-measure-supplemental-data-example.xml` | Artifact-scoped ValueSet | yes |
| `source/measure/valueset-measure-definition-example.xml`, `valueset-measure-group-example.xml`, `valueset-measure-stratifier-age-range-example.xml`, `valueset-measure-stratifier-type-example.xml`, `valueset-measure-report-evaluation-type.xml`, `valueset-measure-scoring-unit.xml`, `valueset-frequency-unit.xml` | Artifact-scoped ValueSets (others) | no |
| `source/measure/measure.svg` | Class diagram | yes |
| `source/measure/measure-definition-mapping-exceptions.xml`, `measure-fivews-mapping-exceptions.xml`, `measure-examples-header.xml` | Mapping/render helpers | no |
| `source/measure/$*-request*.txt`, `$*-response.txt`, `*.json`, `care-gaps-response.xml`, `evaluate-measure-operation-response*.xml`, `cms146_data_requirements.json` | Operation request/response examples | no |
| `source/measure/invariant-tests/` | Invariant test fixtures | no |

Patterns from the briefing that produced no match in the clone: none —
no spreadsheet (`measure-spreadsheet.xml`) is present for this resource;
the StructureDefinition is authoritative.

## Current Ballot Note

Present at HEAD (`db79dcdfe196`), inside `source/measure/measure-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> Key changes made since FHIR 6.0.0-ballot4:</p>
    <ul>
        <li>Non-compatible Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55967">FHIR-55967</a>: Align reporter parameters in $evaluate, $care-gaps, and $collect-data</li>
            </ul>
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-51028">FHIR-51028</a>: Clarified examples are experimental content</li>
            </ul>
        </li>
        <li>Compatible, Substantive Changes
            <ul>
                <li>None</li>
            </ul>
        </li>
        <li>Non-substantive Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55080">FHIR-55080</a>: Potentially re-useable THO-candidate value sets in resource Measure</li>
            </ul>
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55436">FHIR-55436</a>: Remove deprecated Measure.topic</li>
            </ul>
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55437">FHIR-55437</a>: Remove deprecated Measure.guidance</li>
            </ul>
        </li>
    </ul>
    <p></p>
</blockquote>
```

A sibling `<blockquote style="background-color: lightblue">` "All Changes
(including Technical Corrections not listed above)" lists "None" — no
unattributed technical corrections are claimed.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55967](https://jira.hl7.org/browse/FHIR-55967) | Align reporter parameters in $evaluate, $care-gaps, and $collect-data | [`8bfe2548a112`](https://github.com/HL7/fhir/commit/8bfe2548a11217d954d6b5785577f18e5ba4931f) |
| [FHIR-55437](https://jira.hl7.org/browse/FHIR-55437) | Remove deprecated Measure.guidance | [`61c317adde0f`](https://github.com/HL7/fhir/commit/61c317adde0f6e0cd4cab98130244bb07aeffc04) |
| [FHIR-55436](https://jira.hl7.org/browse/FHIR-55436) | Remove deprecated Measure.topic | [`06ab81280ad5`](https://github.com/HL7/fhir/commit/06ab81280ad55b6232b7acf245ed9fbc014b41d4) |
| [FHIR-55080](https://jira.hl7.org/browse/FHIR-55080) | Potentially re-useable THO-candidate value sets in resource Measure | [`4084e3db5e66`](https://github.com/HL7/fhir/commit/4084e3db5e66a35006da1f5378d53662045bd373) |
| [FHIR-51028](https://jira.hl7.org/browse/FHIR-51028) | Change measure-stratifier code system and value set to a non-example | [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) |
| (unattributed) | Introduction reformat + ballot-note authoring | [`c83599e70004`](https://github.com/HL7/fhir/commit/c83599e70004bfd658b51ef62426524eb948df6c), [`f43fbf565a77`](https://github.com/HL7/fhir/commit/f43fbf565a77bf872216d73bce2ef961e739462c) |

## Per-Ticket Detail

### [FHIR-55967](https://jira.hl7.org/browse/FHIR-55967) — Align reporter parameters in $evaluate, $care-gaps, and $collect-data

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Copy the IN parameters 'reporter' and 'reporterResource' on $evaluate to $care-gaps.
  >
  > Remove the IN parameters 'organization' on $care-gaps, and the parameter 'organizationResource' on $collect-data and $care-gaps.
  >
  > In $evaluate, $care-gaps, and $collect-data
  > Update the 'reporterResource' description's first sentence to:
  >
  > "The provider for which the report will be run, provided as a Practitioner, PractitionerRole, or Organization resource."
  >
  > Make 'reporterResource' type Organization or Practitioner or PractitionerRole

- **Disposition summary:** Harmonise the "who is reporting" parameters
  across the three measure operations. `$care-gaps` gains the
  `reporter` / `reporterResource` IN pair; the older `organization` /
  `organizationResource` parameters are retired from `$care-gaps` and
  `$collect-data`. On all three operations, `reporterResource` is
  re-typed from `Organization` to a multi-typed reference accepting
  `Practitioner`, `PractitionerRole`, or `Organization`, with its
  description updated accordingly.
- **Commits applying this ticket:**
  - [`8bfe2548a112`](https://github.com/HL7/fhir/commit/8bfe2548a11217d954d6b5785577f18e5ba4931f) — `[FHIR-55967]: Align reporter parameters in $evaluate, $care-gaps, and $collect-data` (2026-04-21)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `operationdefinition-Measure-care-gaps.xml`: the `organization`
    and `organizationResource` IN parameters are deleted; new
    `reporter` (string / reference) and `reporterResource` IN
    parameters are added, with `reporterResource` carrying three
    `operationdefinition-allowed-type` extensions for `Practitioner`,
    `PractitionerRole`, and `Organization` and a `type` of
    `DomainResource`. The new `reporterResource` documentation matches
    the disposition wording.
  - In `operationdefinition-Measure-collect-data.xml`: the
    `organizationResource` IN parameter is deleted; the existing
    `reporterResource` parameter is re-typed from `string` to
    `DomainResource` and gains the same three `allowed-type`
    extensions; its documentation is updated to the new wording.
  - In `operationdefinition-Measure-evaluate.xml`: `reporterResource`
    is re-typed from `string` to `DomainResource` and gains the same
    three `allowed-type` extensions; its documentation is updated to
    match.
  - The intro file gains the matching ballot-note bullet (the
    structural rewrite of the intro is attributed to the unattributed
    commits below).

### [FHIR-55437](https://jira.hl7.org/browse/FHIR-55437) — Remove deprecated Measure.guidance

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Remove Measure.guidance as proposed.

- **Disposition summary:** `Measure.guidance` was carried with a
  `deprecated` standards-status flag and a NOTE pointing implementers
  to `Measure.usage` instead. Per the broader R6 deprecated-element
  cleanup (parent FHIR-53722), the element is removed in this ballot.
- **Commits applying this ticket:**
  - [`61c317adde0f`](https://github.com/HL7/fhir/commit/61c317adde0f6e0cd4cab98130244bb07aeffc04) — `[FHIR-55437]: Remove deprecated Measure.guidance` (2026-04-20)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `structuredefinition-Measure.xml`: the entire
    `<element id="Measure.guidance">` differential block (path,
    short, definition, deprecated comment, requirements, 0..1 type
    `markdown`, `isSummary=true`, RIM mapping) is removed. Snapshot
    regeneration is required.
  - In `measure.svg`: the `Measure.guidance` row of the class diagram
    is dropped (the residual `[0..1]` text fragment in the diff is
    leftover whitespace from the regenerated SVG and will be cleaned
    up on the next diagram rebuild).
  - In `measure-introduction.xml`: the matching ballot-note bullet is
    added.

### [FHIR-55436](https://jira.hl7.org/browse/FHIR-55436) — Remove deprecated Measure.topic

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Remove Measure.topic as proposed because this element was deprecated in R5.

- **Disposition summary:** `Measure.topic` was deprecated in R5 in
  favour of using `useContext` with the `topic` usage-context-type;
  per the same R6 deprecated-element cleanup, the element is removed
  from the resource (and from its dependent search parameter and
  diagram).
- **Commits applying this ticket:**
  - [`06ab81280ad5`](https://github.com/HL7/fhir/commit/06ab81280ad55b6232b7acf245ed9fbc014b41d4) — `[FHIR-55436]: Remove deprecated Measure.topic. Also removed element references from Measure bundle search params and measure.svg.` (2026-04-20)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `structuredefinition-Measure.xml`: the entire
    `<element id="Measure.topic">` differential block (0..*
    `CodeableConcept`, `example` binding to
    `http://hl7.org/fhir/ValueSet/definition-topic`, the
    `DefinitionTopic` binding name, the migration-comment text, RIM
    mapping) is removed. Snapshot regeneration is required.
  - In `bundle-Measure-search-params.xml`: the `Measure-topic`
    `<SearchParameter>` entry (token, `Measure.topic` expression) is
    removed.
  - In `measure.svg`: the `Measure.topic` row (with its
    `DefinitionTopic` binding link) is removed from the class
    diagram.
  - In `measure-introduction.xml`: the matching ballot-note bullet is
    added.

### [FHIR-55080](https://jira.hl7.org/browse/FHIR-55080) — Potentially re-useable THO-candidate value sets in resource Measure

- **Work group:** Clinical Quality Information
- **Resolution:** Not Persuasive with Modification
- **Disposition (verbatim):**

  > We will mark these value sets as experimental (set flag to true) as they are example content that is not intended to be used in production but rather illustrative of how to use the resource.
  >
  > measure-group-example
  >
  > measure-stratifier-example
  >
  > measure-definition-example
  >
  > measure-supplemental-data-example

- **Disposition summary:** The work group declined to migrate the
  four candidate measure-scoped example value sets to THO; instead,
  they are to be (re)affirmed as `experimental=true` to make their
  illustrative-only intent unambiguous.
- **Commits applying this ticket:**
  - [`4084e3db5e66`](https://github.com/HL7/fhir/commit/4084e3db5e66a35006da1f5378d53662045bd373) — `[FHIR-55080]: Potentially re-useable THO-candidate value sets in resource Measure` (2026-04-17)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `valueset-measure-supplemental-data-example.xml`: only the
    `<description>` is reworded from "Supplemental data in a
    population for measuring purposes." to "Example codes of
    Supplemental data in a population for measuring purposes." to
    foreground the example-only nature.
  - **No-op for the other three named value sets** — at the
    since-commit, `valueset-measure-group-example.xml`,
    `valueset-measure-stratifier-example.xml`, and
    `valueset-measure-definition-example.xml` already carried
    `experimental=true`, so the disposition's "set flag to true" was
    a no-op for them; only the description-clarity tightening
    applied. (FHIR-51028 separately renamed
    `valueset-measure-stratifier-example` → `…-stratifier-type-example`
    in the same window — see that ticket.)
  - In `measure-introduction.xml`: the matching ballot-note bullet
    is added.

### [FHIR-51028](https://jira.hl7.org/browse/FHIR-51028) — Change measure-stratifier code system and value set to a non-example

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will align the example in the base specification, so it is clear that it is a Measure Stratifier Type example.
  >
  > For this example, Codesystem-measure-stratifier-example.json - FHIR v6.0.0-ballot3
  >
  > 1. Change the code "age" to "age-range"
  > 2. Change the code "region" to "facility" as the code and "Facility" as the description.
  > 3. In the CodeSystem definition, update any instance of "measure-stratifier-example"/"Measure Stratifier Example"/etc. to "measure-stratifier-type-example"/"Measure Stratifier Type Example"/etc., including its id, name, etc.

- **Disposition summary:** Rename the stratifier example
  CodeSystem/ValueSet pair so its name makes clear it is illustrating
  *types* of stratification, and tighten the example codes
  (`age` → `age-range`, `region` → `facility`).
- **Commits applying this ticket:**
  - [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) — `[FHIR-51028]: Change measure-stratifier code system and value set to a non-example. …` (2026-04-15)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - The `codesystem-measure-stratifier-example.xml` and
    `valueset-measure-stratifier-example.xml` files are renamed to
    `codesystem-measure-stratifier-type-example.xml` and
    `valueset-measure-stratifier-type-example.xml` (git records this
    as add+similarity rename; the new files appear in the diff). The
    canonical URLs become `…/measure-stratifier-type-example`, the
    name becomes `MeasureStratifierTypeExample`, the title becomes
    "Measure Stratifier Type Example", and the codes are
    `age-range`, `gender`, `facility`.
  - In `structuredefinition-Measure.xml`: the bindings on
    `Measure.group.stratifier.code` and
    `Measure.group.stratifier.component.code` are repointed from
    `…/ValueSet/measure-stratifier-example` (`MeasureStratifierExample`)
    to `…/ValueSet/measure-stratifier-type-example`
    (`MeasureStratifierTypeExample`). Snapshot regeneration is
    required.
  - In `operationdefinition-Measure-evaluate.xml`: the `stratifier`
    OUT part's `valueSet` is repointed to
    `…/ValueSet/measure-stratifier-type-example`.
  - In `measure.svg`: the diagram link/title for the stratifier
    binding is updated to `MeasureStratifierTypeExample`.
  - In `measure-introduction.xml`: the matching ballot-note bullet
    is added.

### (unattributed) — Introduction reformat + ballot-note authoring

- **Commits:**
  - [`c83599e70004`](https://github.com/HL7/fhir/commit/c83599e70004bfd658b51ef62426524eb948df6c) — `Updating Measure and MeasureReport introduction notes` (2026-04-17)
  - [`f43fbf565a77`](https://github.com/HL7/fhir/commit/f43fbf565a77bf872216d73bce2ef961e739462c) — `Adding update note to Measure and MeasureReport per PR request` (2026-04-16)
- **Changes applied:** These two commits (no FHIR-/UTG- key in the
  message and no cross-reference matches in FhirAugury) authored the
  ballot-note `<blockquote class="ballot-note" id="bn1">` block in
  `measure-introduction.xml` and reformatted the surrounding
  Scope-and-Usage / Boundaries-and-Relationships narrative. The
  narrative content is preserved verbatim — only whitespace,
  indentation, and outer `<div>` wrapping changed; the ballot-note
  block itself is the substantive addition. No SD, search-params,
  operation, example, or terminology files are touched by these two
  commits.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-Measure.xml`):**
  - Removed the deprecated `Measure.topic` element block (FHIR-55436)
    and the deprecated `Measure.guidance` element block (FHIR-55437)
    from the differential.
  - Repointed the bindings on `Measure.group.stratifier.code` and
    `Measure.group.stratifier.component.code` from
    `MeasureStratifierExample`
    (`…/ValueSet/measure-stratifier-example`) to
    `MeasureStratifierTypeExample`
    (`…/ValueSet/measure-stratifier-type-example`) (FHIR-51028).
  - Snapshot regeneration is required to reflect the element removals
    and binding URL changes.
- **Intro / narrative (`measure-introduction.xml`):**
  - Added a new `<blockquote class="ballot-note" id="bn1">` summarising
    the changes since 6.0.0-ballot4, plus a sibling
    `<blockquote>` for "All Changes (including Technical Corrections
    not listed above)" with "None".
  - Reformatted (whitespace/indent only) the existing Scope-and-Usage
    and Boundaries-and-Relationships sections; substantive narrative
    is unchanged.
  - `measure-notes.xml` is untouched in the window.
- **Search parameters (`bundle-Measure-search-params.xml`):**
  - Removed the `Measure-topic` `SearchParameter` entry (token over
    `Measure.topic`) consequent to the element removal (FHIR-55436).
  - No additions or other changes.
- **Operations:**
  - `$evaluate` (`operationdefinition-Measure-evaluate.xml`):
    `reporterResource` re-typed from `string` → `DomainResource` with
    three `operationdefinition-allowed-type` extensions
    (`Practitioner`, `PractitionerRole`, `Organization`) and the
    documentation rewritten; the `stratifier` OUT part's binding is
    repointed to `…/ValueSet/measure-stratifier-type-example`
    (FHIR-55967, FHIR-51028).
  - `$care-gaps` (`operationdefinition-Measure-care-gaps.xml`):
    `organization` and `organizationResource` IN parameters removed;
    new `reporter` and `reporterResource` IN parameters added with
    the same `allowed-type` set as `$evaluate` and matching
    documentation (FHIR-55967).
  - `$collect-data` (`operationdefinition-Measure-collect-data.xml`):
    `organizationResource` IN parameter removed; existing
    `reporterResource` re-typed and its `allowed-type` extensions and
    documentation aligned with `$evaluate` (FHIR-55967).
  - `list-Measure-operations.xml` is untouched (no operation added or
    removed at the resource level).
  - `$data-requirements`, `$evaluate-measure` (legacy), and
    `$submit-data` are unchanged.
- **Examples:**
  - No example resources added, removed, or edited. The element
    removals (`Measure.topic`, `Measure.guidance`) have no impact on
    the existing examples in the clone (none referenced those
    elements).
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - Added `codesystem-measure-stratifier-type-example.xml` and
    `valueset-measure-stratifier-type-example.xml` (the renamed
    "stratifier type example" pair, with codes `age-range`, `gender`,
    `facility`) — FHIR-51028.
  - The previously-present `codesystem-measure-stratifier-example.xml`
    / `valueset-measure-stratifier-example.xml` are dropped as part of
    the rename. (No promotion of any of these CodeSystems/ValueSets
    to UTG occurred in this window — per FHIR-55080's disposition
    they remain in-spec example content.)
  - `valueset-measure-supplemental-data-example.xml`: description
    reworded to call out the example-only intent (FHIR-55080); no
    change to membership or `experimental` flag (already `true`).
- **Diagram (`measure.svg`):** Regenerated to drop `Measure.topic` and
  `Measure.guidance` rows and to relabel the stratifier binding to
  `MeasureStratifierTypeExample`.

## Proposed Ballot Note (HTML)

The existing `bn1` block already covers all five tickets with the
correct categorisation and links. The only refinements proposed are
(a) tighter bullet wording reflecting the after-applied effect rather
than the ticket title, and (b) collapsing each category's
sibling `<ul>` blocks into a single `<ul>`.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Key changes made to the Measure
  resource since FHIR 6.0.0-ballot4:</p>
  <ul>
    <li>Non-compatible Changes
      <ul>
        <li>Aligned the "who is reporting" IN parameters across
          <code>$evaluate</code>, <code>$care-gaps</code>, and
          <code>$collect-data</code>: <code>$care-gaps</code> gains
          <code>reporter</code> / <code>reporterResource</code>;
          the older <code>organization</code> /
          <code>organizationResource</code> parameters are removed
          from <code>$care-gaps</code> and <code>$collect-data</code>;
          on all three operations, <code>reporterResource</code> now
          accepts <code>Practitioner</code>,
          <code>PractitionerRole</code>, or <code>Organization</code>
          (<a href="https://jira.hl7.org/browse/FHIR-55967">FHIR-55967</a>).</li>
        <li>Renamed the in-spec stratifier example terminology to
          <code>measure-stratifier-type-example</code>
          (CodeSystem and ValueSet) with codes
          <code>age-range</code>, <code>gender</code>, and
          <code>facility</code>; the bindings on
          <code>Measure.group.stratifier.code</code> and
          <code>Measure.group.stratifier.component.code</code>
          (and the corresponding OUT part of <code>$evaluate</code>)
          are repointed accordingly
          (<a href="https://jira.hl7.org/browse/FHIR-51028">FHIR-51028</a>).</li>
        <li>Removed the R5-deprecated <code>Measure.topic</code>
          element and its <code>topic</code> SearchParameter
          (<a href="https://jira.hl7.org/browse/FHIR-55436">FHIR-55436</a>).</li>
        <li>Removed the R5-deprecated <code>Measure.guidance</code>
          element; implementers should use <code>Measure.usage</code>
          (<a href="https://jira.hl7.org/browse/FHIR-55437">FHIR-55437</a>).</li>
      </ul>
    </li>
    <li>Compatible, Substantive Changes
      <ul>
        <li>None.</li>
      </ul>
    </li>
    <li>Non-substantive Changes
      <ul>
        <li>Clarified that the measure-scoped example value sets
          remain illustrative-only (description tightened on
          <code>measure-supplemental-data-example</code>; the other
          named example value sets were already
          <code>experimental=true</code>)
          (<a href="https://jira.hl7.org/browse/FHIR-55080">FHIR-55080</a>).</li>
      </ul>
    </li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The categorisation of FHIR-55436 (`Measure.topic`) and FHIR-55437
  (`Measure.guidance`) was moved from "Non-substantive Changes" in
  the existing `bn1` to "Non-compatible Changes" in the proposal:
  these commits delete elements (and, for `Measure.topic`, the
  associated SearchParameter), which is breaking for any R5 client
  still populating those elements even though both were marked
  `deprecated`. If CQI prefer to keep them under "Non-substantive"
  on the basis that they were deprecated since R5, swap the bullets
  back — the surrounding wording still reads correctly.
- Two commits in the window
  ([`c83599e70004`](https://github.com/HL7/fhir/commit/c83599e70004bfd658b51ef62426524eb948df6c),
  [`f43fbf565a77`](https://github.com/HL7/fhir/commit/f43fbf565a77bf872216d73bce2ef961e739462c))
  did the actual ballot-note authoring and the indentation rewrite of
  the intro narrative. They have no Jira key in the message and no
  cross-reference hits in FhirAugury, so they are reported under
  "(unattributed)". They are intentionally **not** cited from the
  proposed ballot note.
- FHIR-55080's disposition asked that
  `valueset-measure-group-example`,
  `valueset-measure-stratifier-example`,
  `valueset-measure-definition-example`, and
  `valueset-measure-supplemental-data-example` be marked
  `experimental=true`; at the since-commit all four already carried
  `experimental=true`. The applied commit only tightened the
  description on `valueset-measure-supplemental-data-example`. If
  the disposition was understood to also require an explicit
  *re-affirmation* in the description of the other three, that work
  is not present in the window.
- FHIR-51028 effected a file rename of the stratifier example
  CodeSystem/ValueSet pair. `git diff` shows them as add/delete
  rather than `R` (rename) because some hunks edit content inside
  the rename below the default similarity threshold; the underlying
  intent is a rename.
- The `measure.svg` diff for FHIR-55437 leaves a stray
  `<text … class="diagram-class-detail"> [0..1]</text>` row where
  the `Measure.guidance` link/title was previously stripped — likely
  a regenerator artifact rather than authored content. Worth
  flagging to the editor before publication.
- Companion changes for the same operation/parameter rework on the
  `MeasureReport` resource appear in the same commits (out of scope
  for this artifact's roll-up); the per-commit stats above are
  already scoped to `source/measure/`.
- HEAD (`db79dcdfe196`) is a descendant of the since-commit; the
  symmetric-difference fallback was not needed.
- All data was sourced from the cached clone via `git` and from
  Jira via `fhir-augury-cli`; `gh` was not invoked.

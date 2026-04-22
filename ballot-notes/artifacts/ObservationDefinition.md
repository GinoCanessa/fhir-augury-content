# Artifact Ballot Note Draft: ObservationDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `ObservationDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 4 (FHIR-55272, FHIR-54594, FHIR-54593, FHIR-51028) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `ObservationDefinition` for this run (resolved
from the FhirCore briefing's Artifact Map; folder is
`source/observationdefinition/`, lowercase per repo convention):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/observationdefinition/structuredefinition-ObservationDefinition.xml` | Canonical StructureDefinition | yes |
| `source/observationdefinition/observationdefinition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/observationdefinition/observationdefinition-notes.xml` | Supplementary narrative | no |
| `source/observationdefinition/observationdefinition-definition-mapping-exceptions.xml` | Workflow `Definition` pattern divergences | yes |
| `source/observationdefinition/observationdefinition-fivews-mapping-exceptions.xml` | 5 Ws mapping divergences | no |
| `source/observationdefinition/bundle-ObservationDefinition-search-params.xml` | Search parameters | no |
| `source/observationdefinition/list-ObservationDefinition-operations.xml` | Operations | no |
| `source/observationdefinition/list-ObservationDefinition-examples.xml` | Examples list | no |
| `source/observationdefinition/list-ObservationDefinition-packs.xml` | Packs list | no |
| `source/observationdefinition/observationdefinition-example-ck-panel.xml` | Example (CK panel) | no |
| `source/observationdefinition/observationdefinition-examples-header.xml` | Examples header narrative | no |
| `source/observationdefinition/codesystem-observation-range-category.xml` | Artifact-scoped CodeSystem | no |
| `source/observationdefinition/codesystem-permitted-data-type.xml` | Artifact-scoped CodeSystem | no |
| `source/observationdefinition/valueset-observation-range-category.xml` | Artifact-scoped ValueSet | no |
| `source/observationdefinition/valueset-observation-subject-type.xml` | Artifact-scoped ValueSet (**new**) | yes |
| `source/observationdefinition/valueset-permitted-data-type.xml` | Artifact-scoped ValueSet | no |
| `source/observationdefinition/observationdefinition.svg` | Diagram | no |
| `source/observationdefinition/invariant-tests/` | Invariant test fixtures | no |

No legacy `observationdefinition-spreadsheet.xml` exists in the folder; the
StructureDefinition is the sole authoring source for resource shape (per
the FhirCore briefing's gotcha note).

## Current Ballot Note

A single existing `ballot-note` block was found at HEAD (R5→R6 framing,
still accurate); a sibling `stu-note` block listing the in-flight
release notes for this cycle is present but is not a ballot note:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the ObservationDefinition resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Updated ObservationDefinition.bodySite (CodeableConcept) to ObservationDefinition.bodyStructure (CodeableReference).</li>
<li>Updated ObservationDefinition.device for the canonical DeviceDefinition.</li>
<li>Added ObservationDefinition.qualifiedValue.interpretation.</li>
<li>Jurisdiction has been reinstated (it was marked "Deprecated" in R5).</li>
</ul>
</blockquote>
```

For context, the adjacent (non-ballot-note) release-notes block at HEAD is:

```html
<blockquote class="stu-note" style="background-color: lightblue">
    <p><b>Release Notes (pending alternative process review with FMG):</b></p>
    <ul>
        <li><a href="https://jira.hl7.org/browse/FHIR-55272">FHIR-55272</a></li>
        <li><a href="https://jira.hl7.org/browse/FHIR-54594">FHIR-54594</a></li>
        <li><a href="https://jira.hl7.org/browse/FHIR-54593">FHIR-54593</a></li>
    </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55272](https://jira.hl7.org/browse/FHIR-55272) | ObservationDefinition.identifier should repeat | [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) |
| [FHIR-54594](https://jira.hl7.org/browse/FHIR-54594) | Missing valueset binding for ObservationDefinition.subjectType | [`6f8201567999`](https://github.com/HL7/fhir/commit/6f8201567999a86a3730e50739e7954c4862143e), [`ec3127c1a39e`](https://github.com/HL7/fhir/commit/ec3127c1a39edb646d5d7fff54443995073b69b6), [`79af4db87c26`](https://github.com/HL7/fhir/commit/79af4db87c261e1fa6d0476140779004e754af90) |
| [FHIR-54593](https://jira.hl7.org/browse/FHIR-54593) | Missing valueset binding for codedConcept in ObservationDefinition.performerType | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658), [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) |
| [FHIR-51028](https://jira.hl7.org/browse/FHIR-51028) | Change measure-stratifier code system and value set to a non-example | [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) |

The two `ssi-db` "OO tickets" commits are bulk drops; their commit
messages list additional ticket keys (FHIR-56060, FHIR-55277,
FHIR-54961, FHIR-54450, FHIR-54323, FHIR-53457, FHIR-55257, FHIR-53677,
FHIR-54999) but the diff hunks that landed inside ObservationDefinition's
file scope are limited to the FHIR-55272 / FHIR-54593 work shown
above. The other listed tickets target sibling artifacts
(SpecimenDefinition, BodyStructure, Observation, DeviceDefinition,
BiologicallyDerivedProduct, the 5 Ws mapping refresh, value-set display
cleanups) and are out of scope for this artifact's ballot note. See
"Notes for Reviewer" for the full list.

The two unattributed-by-subject commits (`ec3127c1` "added headers" and
`79af4db8` "Update observationdefinition-definition-mapping-exceptions.xml")
both apply follow-up edits supporting the FHIR-54594 binding work
(introduction stu-note bullet and mapping-exceptions cleanup,
respectively); they are attributed to FHIR-54594 above on that basis.

## Per-Ticket Detail

### [FHIR-55272](https://jira.hl7.org/browse/FHIR-55272) — ObservationDefinition.identifier should repeat

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only ticket comment is a
  > pointer to PR [HL7/fhir#4029](https://github.com/HL7/fhir/pull/4029).

- **Disposition summary:** Allow `ObservationDefinition.identifier` to
  repeat (max → `*`), aligning the resource with the workflow
  `Definition` pattern and with the parallel change for
  `SpecimenDefinition.identifier` (FHIR-55277). Includes a wording
  cleanup of the `short`/`definition` text so it reads as a plural and
  drops a stray period.
- **Commits applying this ticket:**
  - [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) — More OO tickets (2026-03-11)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ObservationDefinition.xml`, the
  `ObservationDefinition.identifier` element's upper cardinality is
  changed from `1` to `*`, the `short` text is changed from "Business
  identifier of the ObservationDefinition" to "Business identifiers of
  the ObservationDefinition", and the `definition` text is corrected
  ("…ObservationDefinition. by the…" → "…ObservationDefinition by
  the…"). The `observationdefinition-definition-mapping-exceptions.xml`
  divergence file picks up the matching plural wording and (in a later
  commit attributed to FHIR-51028, see below) drops the
  `<upperCardinality _pattern="*" _resource="1"/>` divergence row,
  because the resource now matches the `Definition` pattern's `*`. A
  matching stu-note bullet linking to FHIR-55272 is added to the
  introduction.

### [FHIR-54594](https://jira.hl7.org/browse/FHIR-54594) — Missing valueset binding for ObservationDefinition.subjectType

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only ticket comment is a
  > pointer to PR [HL7/fhir#4019](https://github.com/HL7/fhir/pull/4019/).

- **Disposition summary:** Add an example-strength binding to
  `ObservationDefinition.subject` (currently `CodeableConcept` with no
  binding), and ship a fresh artifact-scoped ValueSet that lists the
  candidate subject types (organisms and physical objects, sourced
  from SNOMED CT). Brings the resource into line with the
  `Definition.subject` pattern, which carries an example binding.
- **Commits applying this ticket:**
  - [`6f8201567999`](https://github.com/HL7/fhir/commit/6f8201567999a86a3730e50739e7954c4862143e) — FHIR-54594: Add example binding for ObservationDefinition.subject (2026-03-07)
  - [`ec3127c1a39e`](https://github.com/HL7/fhir/commit/ec3127c1a39edb646d5d7fff54443995073b69b6) — added headers (2026-03-31) — adds the FHIR-54594 entry to the introduction stu-note list
  - [`79af4db87c26`](https://github.com/HL7/fhir/commit/79af4db87c261e1fa6d0476140779004e754af90) — Update observationdefinition-definition-mapping-exceptions.xml (2026-03-24) — drops the now-stale `<bindingExistence _pattern="true" _resource="false"/>` divergence row for `subject`
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ObservationDefinition.xml`, an example-strength
  `<binding>` is added to the `ObservationDefinition.subject` element
  (`bindingName` `ObservationSubjectType`, valueSet
  `http://hl7.org/fhir/ValueSet/observation-subject-type`,
  description "Codes identifying the type of subject for an
  observation definition, such as organisms or physical objects."). A
  new artifact-scoped ValueSet
  `valueset-observation-subject-type.xml`
  (`http://hl7.org/fhir/ValueSet/observation-subject-type`,
  status `draft`, OO work group, trial-use) is added; its compose
  includes SNOMED CT subsumption filters under `410607006` (Organism)
  and `260787004` (Physical object). The mapping-exceptions file is
  updated to remove the corresponding `bindingExistence` divergence
  for `subject` against the workflow `Definition` pattern, and the
  introduction stu-note picks up an FHIR-54594 reference.

### [FHIR-54593](https://jira.hl7.org/browse/FHIR-54593) — Missing valueset binding for codedConcept in ObservationDefinition.performerType

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. Ticket comments capture a
  > design discussion (suggesting that the example value set cover
  > concepts from `practitioner-role`, `organization-type`,
  > `CMSPlaceOfServiceCodes`, plus Patient / RelatedPerson) and a
  > pointer to PR [HL7/fhir#4037](https://github.com/HL7/fhir/pull/4037).

- **Disposition summary:** Add an example-strength binding to
  `ObservationDefinition.performerType` (`CodeableConcept`, currently
  unbound), pointing at an existing care-team participant role value
  set so the element is no longer the sole codeable concept on the
  resource without binding guidance.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24)
  - [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) — incidental cleanup of the matching mapping-exceptions row (commit subject is FHIR-51028; see below)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ObservationDefinition.xml`, an example-strength
  `<binding>` is added to `ObservationDefinition.performerType`
  (`bindingName` `ObservationDefinitionParticipantRole`, valueSet
  `http://hl7.org/fhir/ValueSet/participant-role`, description
  "Indicates specific responsibility of an individual within the care
  team, such as 'Primary physician', 'Team coordinator',
  'Caregiver', etc."). The ticket-comment design discussion floated a
  bespoke example value set covering practitioner role +
  organization-type + place-of-service + Patient/RelatedPerson; the
  applied implementation instead reuses the existing
  `participant-role` value set. The introduction stu-note picks up
  an FHIR-54593 reference, and the mapping-exceptions file later drops
  the corresponding `bindingExistence` divergence row for
  `performerType` (incidental change carried by commit `18df653`).

### [FHIR-51028](https://jira.hl7.org/browse/FHIR-51028) — Change measure-stratifier code system and value set to a non-example

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution_description and
  > Jira comments returned no applied-vote text via fhir-augury-cli).

- **Disposition summary:** This is a CQI ticket about promoting the
  `measure-stratifier` code system / value set from example to
  non-example; its primary scope is the Measure-related artifacts, not
  ObservationDefinition. The single-line edit it carries inside the
  `ObservationDefinition` file scope is incidental cleanup.
- **Commits applying this ticket:**
  - [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) — FHIR-51028: Change measure-stratifier code system and value set to a non-example (2026-04-15)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `observationdefinition-definition-mapping-exceptions.xml`, the
  `<bindingExistence _pattern="true" _resource="false"/>` divergence
  row for `Definition.performerType` is removed. This is bookkeeping
  caused by the FHIR-54593 binding having landed earlier (commit
  `d2dde0c4`), not part of the measure-stratifier work itself; on its
  own this hunk would be misleading — see the roll-up summary for the
  authoritative "after-applied" picture of the mapping-exceptions
  file.

## Roll-up Summary (after-applied state)

Authoritative summary derived from the
`5d67a34a13a5..db79dcdfe196` diff scoped to the artifact's files. Four
files changed; one is a new ValueSet.

- **StructureDefinition (`structuredefinition-ObservationDefinition.xml`):**
  - `ObservationDefinition.identifier`: upper cardinality changed
    from `1` to `*` (now repeating); `short` reworded as the plural
    "Business identifiers of the ObservationDefinition"; stray period
    removed from the `definition` text. (FHIR-55272)
  - `ObservationDefinition.subject`: new example-strength `<binding>`
    added — `bindingName` `ObservationSubjectType`, valueSet
    `http://hl7.org/fhir/ValueSet/observation-subject-type`. No type,
    cardinality, or summary-flag changes. (FHIR-54594)
  - `ObservationDefinition.performerType`: new example-strength
    `<binding>` added — `bindingName`
    `ObservationDefinitionParticipantRole`, valueSet
    `http://hl7.org/fhir/ValueSet/participant-role`. No type,
    cardinality, or summary-flag changes. (FHIR-54593)
  - Snapshot regeneration is required for this SD; snapshot edits
    are derived and not narrated here.
- **Intro / narrative (`observationdefinition-introduction.xml`):**
  - The existing `ballot-note` (`bn1`, R5→R6 framing) is unchanged
    and remains accurate at HEAD.
  - A new `stu-note` block titled "Release Notes (pending alternative
    process review with FMG)" is added, listing FHIR-55272,
    FHIR-54594, and FHIR-54593. This is intentionally a `stu-note`
    rather than a `ballot-note`; the proposed `ballot-note` below is a
    new, separate `bn2` summarising the same set of changes for
    balloter consumption.
- **Mapping exceptions (`observationdefinition-definition-mapping-exceptions.xml`):**
  - Three divergence rows against the workflow `Definition` pattern
    are removed because the resource now matches the pattern:
    `<upperCardinality _pattern="*" _resource="1"/>` for `identifier`
    (FHIR-55272), and `<bindingExistence _pattern="true" _resource="false"/>`
    for `subject` (FHIR-54594) and `performerType` (FHIR-54593).
  - The `shortUnmatched`/`definitionUnmatched` text for `identifier`
    is realigned with the SD's revised wording.
- **Search parameters (`bundle-ObservationDefinition-search-params.xml`):**
  No change.
- **Operations (`list-ObservationDefinition-operations.xml`):** No
  change.
- **Examples (`list-ObservationDefinition-examples.xml`,
  `observationdefinition-example-ck-panel.xml`,
  `observationdefinition-examples-header.xml`):** No change. None of
  the SD edits required example regeneration (no element rename, type
  change, or required-binding addition).
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - **New** ValueSet `valueset-observation-subject-type.xml`
    (`http://hl7.org/fhir/ValueSet/observation-subject-type`,
    name `ObservationSubjectType`, status `draft`, experimental
    `false`, OO work group, standards-status `trial-use`). Compose
    is two SNOMED CT subsumption filters: `is-a 410607006` (Organism)
    and `is-a 260787004` (Physical object). Includes the standard
    SNOMED CT IHTSDO copyright. (FHIR-54594) Because the binding
    uses an external (SNOMED) terminology hosted in the FHIR core
    spec, no UTG move is implied at this time.
  - The reused `participant-role` value set referenced by the new
    `performerType` binding is owned outside this artifact's folder
    and was not edited in this window.
  - `codesystem-observation-range-category.xml`,
    `codesystem-permitted-data-type.xml`,
    `valueset-observation-range-category.xml`, and
    `valueset-permitted-data-type.xml` are unchanged.

## Proposed Ballot Note (HTML)

The existing `bn1` block describes R5→R6 changes and is preserved
verbatim. A new `bn2` block is proposed to summarise the changes
applied since `5d67a34a13a5` for balloters; it is derived from the
roll-up summary above and supersedes the informational `stu-note`
block currently in the intro (the `stu-note` may be removed once this
ballot note is in place).

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the ObservationDefinition resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Updated ObservationDefinition.bodySite (CodeableConcept) to ObservationDefinition.bodyStructure (CodeableReference).</li>
<li>Updated ObservationDefinition.device for the canonical DeviceDefinition.</li>
<li>Added ObservationDefinition.qualifiedValue.interpretation.</li>
<li>Jurisdiction has been reinstated (it was marked "Deprecated" in R5).</li>
</ul>
</blockquote>
<blockquote class="ballot-note" id="bn2">
<p><b>Note to Balloters:</b> The following substantive changes have been applied since the previous ballot. Reviewers are asked to confirm that the revised cardinality and the newly bound elements are appropriate, and that the new ObservationSubjectType example value set covers the expected range of subject types (organisms and physical objects).</p>
<ul>
<li><code>ObservationDefinition.identifier</code> is now repeating (max changed from <code>1</code> to <code>*</code>) so a single definition can carry multiple business identifiers across systems; the short and definition wording has been reworded accordingly (<a href="https://jira.hl7.org/browse/FHIR-55272">FHIR-55272</a>).</li>
<li><code>ObservationDefinition.subject</code> now carries an <em>example</em>-strength binding to a new value set <a href="valueset-observation-subject-type.html">ObservationSubjectType</a> covering organisms and physical objects from SNOMED CT, in line with the workflow <code>Definition.subject</code> pattern (<a href="https://jira.hl7.org/browse/FHIR-54594">FHIR-54594</a>).</li>
<li><code>ObservationDefinition.performerType</code> now carries an <em>example</em>-strength binding (<code>ObservationDefinitionParticipantRole</code>) to the existing <a href="valueset-participant-role.html">participant-role</a> value set, providing implementer guidance for the responsible role within the care team (<a href="https://jira.hl7.org/browse/FHIR-54593">FHIR-54593</a>).</li>
<li>The corresponding rows in the workflow <code>Definition</code> pattern divergence file have been removed because the resource now matches the pattern for <code>identifier</code> cardinality and for the presence of bindings on <code>subject</code> and <code>performerType</code> (<a href="https://jira.hl7.org/browse/FHIR-55272">FHIR-55272</a>, <a href="https://jira.hl7.org/browse/FHIR-54594">FHIR-54594</a>, <a href="https://jira.hl7.org/browse/FHIR-54593">FHIR-54593</a>).</li>
</ul>
</blockquote>
```

## Notes for Reviewer

- The `stu-note` block currently in `observationdefinition-introduction.xml`
  ("Release Notes (pending alternative process review with FMG)") is
  not a ballot note. The proposed `bn2` covers the same three tickets
  with balloter-oriented wording and inline rationale; once `bn2` is
  adopted, the `stu-note` block can be removed (or left as an
  editor-internal pointer until the alternative-process review with
  FMG concludes).
- Existing `bn1` bullets were kept verbatim — the R5→R6 changes they
  describe (`bodySite`→`bodyStructure`, `device`→canonical
  DeviceDefinition, `qualifiedValue.interpretation`, jurisdiction
  reinstated) are still present in the HEAD SD. None were reverted in
  this window.
- The two `ssi-db` "OO tickets" commits (`d2dde0c4`, `b62975d9`)
  reference additional tickets in their commit messages that landed
  outside the ObservationDefinition file scope and so do not appear
  in the per-ticket detail above. For traceability:
  - **FHIR-55277** — SpecimenDefinition.identifier should repeat
    (parallel to FHIR-55272; SpecimenDefinition artifact)
  - **FHIR-56060** — Minor cleanup to value set display names
    (cross-cutting terminology touch-up)
  - **FHIR-54961** — Update 5 Ws Mappings (cross-cutting fivews
    mapping refresh)
  - **FHIR-54450** — Allow BodyStructure.patient to be omitted
    (BodyStructure artifact)
  - **FHIR-54323** — Change definition of `.biologicalSourceEvent`
    (BiologicallyDerivedProduct artifact)
  - **FHIR-53457** — Remove `.bodySite` from Terminology Bindings in
    Observation (Observation artifact)
  - **FHIR-55257** — DeviceDefinition.regulatoryIdentifier.type has
    no escape valve (DeviceDefinition artifact)
  - **FHIR-53677** — `.subject` short description (Observation
    artifact)
  - **FHIR-54999** — BiologicallyDerivedProduct grouping identifier
    (BiologicallyDerivedProduct artifact)
- Commit `18df653` is a CQI ticket (FHIR-51028, measure-stratifier);
  its only ObservationDefinition-scoped hunk is incidental cleanup of
  a now-stale `bindingExistence` divergence row that was made
  redundant by the FHIR-54593 binding addition. The per-ticket entry
  flags this so FHIR-51028 is not mistakenly characterised as an
  ObservationDefinition change.
- No commits in the window touched the search-parameters bundle, the
  operations list, the examples, or the existing artifact-scoped
  CodeSystems / ValueSets (`observation-range-category`,
  `permitted-data-type`).
- The new `ObservationSubjectType` value set is an artifact-local
  intensional definition over SNOMED CT subsumption hierarchies
  (`410607006` Organism, `260787004` Physical object). Reviewers may
  wish to confirm whether this should remain artifact-local or move
  to UTG; the FhirCore briefing's cross-repo touch-points list
  artifact-scoped value sets as a candidate for UTG migration when
  they have broader applicability.
- No fallback to `gh api` was needed: the since-commit
  `5d67a34a13a5` is reachable from the cache clone HEAD
  `db79dcdfe196` (linear ancestor; no symmetric-difference fallback
  used). Cross-reference lookups via `fhir-augury-cli` returned no
  hits for any of the six commits, so ticket attribution relied on
  `(FHIR|UTG)-\d+` extraction from commit subjects/bodies.

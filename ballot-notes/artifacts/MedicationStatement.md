# Artifact Ballot Note Draft: MedicationStatement (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `MedicationStatement` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 5 |
| Tickets attributed | 3 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `MedicationStatement` for this run (FhirCore folder
`source/medicationstatement/`; the briefing's Artifact Map does not list a
bespoke MedicationStatement entry, so the standard FhirCore patterns were
applied against the clone):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/medicationstatement/structuredefinition-MedicationStatement.xml` | StructureDefinition (canonical SD) | yes |
| `source/medicationstatement/medicationstatement-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/medicationstatement/medicationstatement-notes.xml` | Supplementary narrative | no |
| `source/medicationstatement/bundle-MedicationStatement-search-params.xml` | Search parameters bundle | no |
| `source/medicationstatement/list-MedicationStatement-operations.xml` | Operations list | no |
| `source/medicationstatement/list-MedicationStatement-examples.xml` | Examples list | no |
| `source/medicationstatement/list-MedicationStatement-packs.xml` | Packs list | no |
| `source/medicationstatement/medicationstatement-html.xml` | Rendered HTML fragment | no |
| `source/medicationstatement/medicationstatement-event-mapping-exceptions.xml` | Event-pattern mapping exceptions | yes |
| `source/medicationstatement/medicationstatement-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/medicationstatement/medicationstatement-examples-header.xml` | Examples header | no |
| `source/medicationstatement/medicationstatementexample{1..10}.xml` | Examples (10 instances) | yes (example4 only) |
| `source/medicationstatement/codesystem-medication-statement-status.xml` | Artifact-scoped CodeSystem (status) | yes |
| `source/medicationstatement/codesystem-medication-statement-adherence.xml` | Artifact-scoped CodeSystem (adherence) | no |
| `source/medicationstatement/valueset-medication-statement-status.xml` | Artifact-scoped ValueSet (status) | no |
| `source/medicationstatement/valueset-medication-statement-adherence.xml` | Artifact-scoped ValueSet (adherence) | no |
| `source/medicationstatement/valueset-medication-statement-category.xml` | Artifact-scoped ValueSet (category) | no |
| `source/medicationstatement/valueset-medication-statement-medication-codes.xml` | Artifact-scoped ValueSet (medication codes) | no |
| `source/medicationstatement/valueset-reason-medication-not-taken-codes.xml` | Artifact-scoped ValueSet (reason not taken) | no |
| `source/medicationstatement/valueset-reason-medication-status-codes.xml` | Artifact-scoped ValueSet (reason status) | no |
| `source/medicationstatement/_changelog.txt` | Per-resource changelog (newly added) | yes |
| `source/medicationstatement/medicationstatement.svg` | Diagram | no |

Patterns from the standard FhirCore set that produced no match in the clone:

- `source/medicationstatement/medicationstatement-spreadsheet.xml` — no legacy
  spreadsheet exists for MedicationStatement (SD is authoritative).
- Sibling `structuredefinition-*.xml` other than the canonical SD — none present.

## Current Ballot Note

Three ballot notes are present at HEAD in
`source/medicationstatement/medicationstatement-introduction.xml`. None of them
were modified in the window (the intro file is unchanged between
`5d67a34a13a5` and `db79dcdfe196`):

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b>
  The <code>MedicationStatement.medication</code> element now explicitly supports representing statements such as 'no medications are known / taken.'
  </p>
  <p>
  Balloters are invited to comment on this approach, impact and possible limitations.
  </p>
  </blockquote>
```

```html
<blockquote class="ballot-note" id="bn2">
  <p><b>Note to Balloters:</b>
  The elements around Dosage have been subject to breaking changes in R6:
  </p>
  <ul>
   <li>A new data type <a href="dosage.html#DosageDetails"> DosageDetails</a> is introduced, containing rendered instructions and simple or structured <a href="dosage.html#Dosage"> Dosage</a>. </li>
   <li><code>dosageInstruction</code> is now 0..1, and uses the new data type. The composition of complex dosages (with segments, repetitions etc.) can be done using the structure in that data type.</li>
   <li><code>renderedDosageInstruction</code> is removed from the resource and placed in <code>DosageDetails.renderedInstruction</code> in the <a href="dosage.html#DosageDetails"> DosageDetails</a> data type.</li>
   <li>A set of <a href="dosage-examples.html"> examples</a> is provided to show how structured dosages can be represented.</li>
  </ul>
  </blockquote>
```

```html
<blockquote class="ballot-note" id="bn3">
  <p><b>Note to Balloters:</b>
  The code system used in medication statement category is presented here but is expected to move to <a href="http://terminology.fhr.org">terminology.hl7.org</a>.
  </p>
  </blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) | Dosage redesign could be improved by requiring renderedInstruction | [`b641e8e249fa`](https://github.com/HL7/fhir/commit/b641e8e249fac89aeac83d6e3f5e0e275ccb1058) |
| [FHIR-54451](https://jira.hl7.org/browse/FHIR-54451) | When to use reason vs relatedClinicalInformation | [`84c55f6b66ee`](https://github.com/HL7/fhir/commit/84c55f6b66eedb0c7341526f2cbf4a914ec4ed7a) |
| [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) | MedicationStatement[.status] codes are incorrect | [`358c5eb203b3`](https://github.com/HL7/fhir/commit/358c5eb203b35c6326e060566926db8aeda12352) |
| (unattributed) | n/a | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224), [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd) |

## Per-Ticket Detail

### [FHIR-54451](https://jira.hl7.org/browse/FHIR-54451) — When to use reason vs relatedClinicalInformation

- **Work group:** Pharmacy
- **Resolution:** Not Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** The submitter flagged that
  `MedicationStatement.reason` and `.relatedClinicalInformation` overlap
  (both can reference Condition / Observation, the "why" vs "relevant to"
  distinction is subtle, and the examples given for
  `relatedClinicalInformation` could plausibly be a reason). Pharmacy
  declined to merge the elements but agreed to add definitional guidance
  distinguishing the two and clarifying that `.relatedClinicalInformation`
  is **not** the indication for the medication.
- **Commits applying this ticket:**
  - [`84c55f6b66ee`](https://github.com/HL7/fhir/commit/84c55f6b66eedb0c7341526f2cbf4a914ec4ed7a) — `FHIR-54451Clarify MedicationStatement.reason vs .relatedClinicalInformation` (2026-03-05)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-MedicationStatement.xml` the `definition` text on
  two elements was rewritten:
  - `MedicationStatement.reason` — old: *"A concept, Condition or
    observation that supports why the medication is being/was taken."*;
    new: *"The concept(s), Condition(s) or observation(s) that lead to the
    medication being taken (or not taken)."* (broadens the scope to
    explicitly cover reasons for **not** taking, in line with the existing
    `valueset-reason-medication-not-taken-codes` binding).
  - `MedicationStatement.relatedClinicalInformation` — appended
    *"This is normally not the actual indication for the medication being
    used - that indication would be represented with .reason."* to
    disambiguate from `.reason`.

  The same wording change to `.reason` was mirrored into
  `medicationstatement-event-mapping-exceptions.xml` (the `<resource>` text
  under the unmatched `<definitionUnmatched>` block) by commit
  `a287d6eb0592` — see the unattributed section below for context. No
  cardinality, type, binding, or constraint changes; snapshot regeneration
  is required.

### [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) — MedicationStatement[.status] codes are incorrect

- **Work group:** Pharmacy
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** The submitter pointed out that the
  `entered-in-error` definition in the MedicationStatement status code
  system was misleading — it described a partially-occurred event rather
  than an erroneous record. Pharmacy accepted the change to align
  `entered-in-error` with the standard FHIR semantics ("the resource was
  entered in error and is not valid").
- **Commits applying this ticket:**
  - [`358c5eb203b3`](https://github.com/HL7/fhir/commit/358c5eb203b35c6326e060566926db8aeda12352) — `FHIR-54903Fix entered-in-error status definitions for MedicationStatement and MedicationRequest` (2026-03-05)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `codesystem-medication-statement-status.xml` the `entered-in-error`
  concept's `definition` was replaced from *"Some of the actions that are
  implied by the medication usage may have occurred. For example, the
  patient may have taken some of the medication. Clinical decision support
  systems should take this status into account."* to *"The statement was
  entered in error and is not valid."* No code added/removed; the bound
  ValueSet (`valueset-medication-statement-status.xml`) is unchanged.
  The companion fix to MedicationRequest was applied in the same commit
  but lives outside this artifact's scope.

### [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) — Dosage redesign could be improved by requiring renderedInstruction

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** The submitter argued that the R6 Dosage
  redesign (new `DosageDetails` data type) should require
  `renderedInstruction` so consumers always have a reliable plain-text
  rendering even when the structured dosage is computationally complex or
  inconsistently implemented. Pharmacy did not change the cardinality of
  `renderedInstruction` itself, but accepted the spirit of the comment by
  ensuring the published examples consistently populate it — the actual
  cardinality / type work for `DosageDetails` itself is covered by the
  pre-existing `bn2` ballot note on Dosage and is out of scope for this
  artifact's window.
- **Commits applying this ticket:**
  - [`b641e8e249fa`](https://github.com/HL7/fhir/commit/b641e8e249fac89aeac83d6e3f5e0e275ccb1058) — `FHIR-54014update examples with renderedinstruction` (2026-03-05)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `medicationstatementexample4.xml`, a `<renderedInstruction
  value="One capsule three times daily by mouth."/>` element was added to
  the `<dosage>` block (alongside the existing free-text `<text>` element).
  No other example files in MedicationStatement's scope were modified by
  this commit; the bulk of the renderedInstruction backfill landed in
  other resources (MedicationRequest, MedicationDispense, …). Snapshot is
  unaffected — examples only.

### (unattributed)

- **Commits without a Jira key in the message or in cross-refs:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) — `display names have changed for US and GB` (JohnMoehrke, 2026-03-28). In MedicationStatement scope this commit edited
    `medicationstatement-event-mapping-exceptions.xml` to keep the
    `<resource>` text under the `MedicationStatement.reason`
    `<definitionUnmatched>` block in sync with the new SD definition
    introduced by FHIR-54451 — i.e., it replaces *"A concept, Condition
    or observation that supports why the medication is being/was taken."*
    with *"The concept(s), Condition(s) or observation(s) that lead to
    the medication being taken (or not taken)."*. The commit subject is
    misleading in this context (the change has nothing to do with US/GB
    display names — that is the bulk of the commit, which lives in other
    resources); the MedicationStatement hunk is essentially a follow-up
    consistency fix for FHIR-54451.
  - [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd) — `separate changelogs per resource type` (Jose Costa Teixeira, 2026-03-21). Adds a new per-resource
    `source/medicationstatement/_changelog.txt` capturing the
    `FHIR-54903` and `FHIR-54451` entries that previously lived in the
    repo-wide changelog. Tooling / housekeeping; no resource-content
    impact.

## Roll-up Summary (after-applied state)

Authoritative summary of what changed in `source/medicationstatement/`
between `5d67a34a13a5` and `db79dcdfe196` (5 commits, 5 files, +13/-4):

- **StructureDefinition (`structuredefinition-MedicationStatement.xml`):**
  - `MedicationStatement.reason` — `definition` rewritten to "The
    concept(s), Condition(s) or observation(s) that lead to the medication
    being taken (or not taken)." Broadens the wording to explicitly cover
    *not-taken* reasons (already supported by the existing
    `reason-medication-not-taken-codes` ValueSet binding) and removes the
    softer "supports why" phrasing.
  - `MedicationStatement.relatedClinicalInformation` — `definition`
    appended with: "This is normally not the actual indication for the
    medication being used - that indication would be represented with
    .reason." Clarifies the boundary against `.reason` without changing
    cardinality, type, or binding.
  - No element additions / removals, no cardinality / type / binding /
    constraint changes, no slicing changes. Snapshot regeneration is
    required to pick up the differential text.
- **Intro / narrative (`medicationstatement-introduction.xml`,
  `medicationstatement-notes.xml`):** Unchanged. The three existing ballot
  notes (`bn1` re. `medication` representing "no medications known /
  taken", `bn2` re. the Dosage / `DosageDetails` redesign, `bn3` re. the
  category code system expected to move to terminology.hl7.org) remain in
  place verbatim.
- **Search parameters (`bundle-MedicationStatement-search-params.xml`):**
  Unchanged.
- **Operations (`list-MedicationStatement-operations.xml`):** Unchanged.
- **Examples:** No additions or removals.
  `medicationstatementexample4.xml` was updated to add a
  `Dosage.renderedInstruction` ("One capsule three times daily by mouth.")
  alongside the existing free-text `Dosage.text`, demonstrating the
  R6 expectation that structured dosages also publish a human-readable
  rendering. The other nine examples are untouched.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - `codesystem-medication-statement-status.xml` —
    `entered-in-error.definition` rewritten to "The statement was entered
    in error and is not valid.", aligning with the standard FHIR
    `entered-in-error` semantics. Code list, ValueSet binding, and
    `valueset-medication-statement-status.xml` itself are unchanged.
  - All other artifact-scoped ValueSets and CodeSystems
    (`-adherence`, `-category`, `-medication-codes`,
    `-reason-medication-not-taken-codes`,
    `-reason-medication-status-codes`) are unchanged. Per the existing
    `bn3` ballot note, the category code system is still flagged as
    expected to move to terminology.hl7.org; nothing in this window
    advances or reverses that.
- **Other:** A new `source/medicationstatement/_changelog.txt` was added
  as part of a repo-wide split of the monolithic changelog into
  per-resource files; it currently lists only the two SD/CS changes above.
  `medicationstatement-event-mapping-exceptions.xml` was kept in sync with
  the new `.reason` definition (see unattributed section).

## Proposed Ballot Note (HTML)

The three existing ballot notes (`bn1`, `bn2`, `bn3`) describe earlier
ballot-cycle changes that are still accurate at HEAD and should be
**retained verbatim**. The new note below (`bn4`) covers the substantive
changes in this window. It is derived from the roll-up summary; per-ticket
descriptions are supporting evidence only.

```html
<blockquote class="ballot-note" id="bn4">
  <p><b>Note to Balloters:</b>
  Since the previous ballot, the Pharmacy work group has applied a
  small set of clarifying changes to MedicationStatement. None of these
  alter the resource's structure (no cardinality, type, or binding
  changes), but balloters are asked to confirm the revised wording and
  status semantics:</p>
  <ul>
    <li>The definition of <code>MedicationStatement.reason</code> has been
    rewritten to read "The concept(s), Condition(s) or observation(s) that
    lead to the medication being taken (or not taken).", making it explicit
    that <code>.reason</code> covers reasons for <em>not</em> taking a
    medication as well as for taking it
    (<a href="https://jira.hl7.org/browse/FHIR-54451">FHIR-54451</a>).</li>
    <li>The definition of
    <code>MedicationStatement.relatedClinicalInformation</code> now
    explicitly states that this element is <em>not</em> the actual
    indication for the medication &mdash; the indication belongs in
    <code>.reason</code>
    (<a href="https://jira.hl7.org/browse/FHIR-54451">FHIR-54451</a>).</li>
    <li>The <code>entered-in-error</code> concept in the
    MedicationStatement status code system has been corrected. Its
    definition is now "The statement was entered in error and is not
    valid.", aligning with the standard FHIR meaning of
    <code>entered-in-error</code> and replacing the previous wording that
    incorrectly described a partially-occurred event
    (<a href="https://jira.hl7.org/browse/FHIR-54903">FHIR-54903</a>).</li>
    <li>Example 4 has been updated to populate
    <code>Dosage.renderedInstruction</code> alongside the structured
    dosage, illustrating the expectation under the R6 Dosage redesign
    (see ballot note above) that structured dosages also publish a
    reliable human-readable rendering
    (<a href="https://jira.hl7.org/browse/FHIR-54014">FHIR-54014</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Existing ballot notes carried forward unchanged.** `bn1`, `bn2`, and
  `bn3` were not touched in this window and remain accurate at HEAD; no
  bullets were dropped or revised. The new draft is appended as `bn4`.
- **Disposition text is not available in Jira** for any of the three
  attributed tickets (no comments returned by `fhir-augury-cli get`,
  including no Pharmacy applied-vote comment). The "Disposition summary"
  paragraphs in each per-ticket section are the agent's neutral summary
  of the ticket description plus the resolution status, **not** verbatim
  workgroup text.
- **`a287d6eb0592` is misleadingly subjected.** Its commit subject
  ("display names have changed for US and GB") describes a different bulk
  change that touches many other resources; within MedicationStatement
  scope the commit is in fact a consistency follow-up that propagates the
  new `.reason` wording from FHIR-54451 into
  `medicationstatement-event-mapping-exceptions.xml`. It is therefore
  treated as unattributed for ticket-roll-up purposes but should be read
  alongside FHIR-54451.
- **Cross-resource touch points outside this artifact's scope:**
  FHIR-54903's commit also fixed the `entered-in-error` definition in
  MedicationRequest's status code system; FHIR-54014's
  `renderedInstruction` backfill landed in other Medication-* resources as
  well. These are noted only so reviewers understand the full reach of
  the underlying tickets.
- **Briefing freshness.** The repo-analysis briefing was generated
  against clone HEAD `1b369ff4e28e` while the current clone HEAD is
  `db79dcdfe196`. The briefing did not contain a bespoke MedicationStatement
  Artifact Map entry, so the standard FhirCore patterns were applied
  directly against the clone; no inferences were drawn from briefing
  content that could have been invalidated by the drift.
- **No `gh` fallback was needed**; all SHAs in the window resolved
  cleanly against the cached clone.

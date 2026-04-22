# Artifact Ballot Note Draft: MedicationRequest (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `MedicationRequest` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 2 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `MedicationRequest` for this run, resolved against
the briefing's Artifact Map and the `source/medicationrequest/` folder
in the cache clone:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/medicationrequest/structuredefinition-MedicationRequest.xml` | StructureDefinition (canonical) | no |
| `source/medicationrequest/medicationrequest-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/medicationrequest/medicationrequest-notes.xml` | Supplementary narrative | no |
| `source/medicationrequest/bundle-MedicationRequest-search-params.xml` | Search parameters bundle | no |
| `source/medicationrequest/list-MedicationRequest-operations.xml` | Operations list | no |
| `source/medicationrequest/list-MedicationRequest-examples.xml` | Examples list | no |
| `source/medicationrequest/list-MedicationRequest-packs.xml` | Packs list | no |
| `source/medicationrequest/medicationrequest-html.xml` | HTML fragment for resource page | no |
| `source/medicationrequest/medicationrequest-fivews-mapping-exceptions.xml` | 5W mapping exceptions | no |
| `source/medicationrequest/medicationrequest-request-mapping-exceptions.xml` | Request pattern mapping exceptions | no |
| `source/medicationrequest/medicationrequest-examples-header.xml` | Examples header | no |
| `source/medicationrequest/medicationrequest-example.xml` | Primary example | no |
| `source/medicationrequest/medicationrequest0302.xml` | Example | yes |
| `source/medicationrequest/medicationrequest0303.xml` | Example | yes |
| `source/medicationrequest/medicationrequest0317.xml` | Example | yes |
| `source/medicationrequest/medicationrequest0321.xml` | Example | yes |
| `source/medicationrequest/medicationrequest0339.xml` | Example | yes |
| `source/medicationrequest/medicationrequest03{01,04..16,18..20,22..38,40..43a,43b,49,50}.xml` | Examples (other) | no |
| `source/medicationrequest/medicationrequestexample{1..4}.xml` | Examples (named) | no |
| `source/medicationrequest/codesystem-medicationrequest-status.xml` | Artifact-scoped CodeSystem (status codes) | yes |
| `source/medicationrequest/codesystem-medicationrequest-intent.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationrequest/codesystem-medicationrequest-category.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationrequest/codesystem-medicationrequest-dispenser-instructions.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationrequest/codesystem-medication-dose-aid.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationrequest/codesystem-medication-intended-performer-role.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationrequest/codesystem-performer-role.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationrequest/valueset-*.xml` (16 files) | Artifact-scoped ValueSets | no |

Patterns from the artifact map that produced no match in the clone:

- `source/medicationrequest/MedicationRequest-spreadsheet.xml` — no
  legacy spreadsheet present (SD is authoritative, per the FhirCore
  briefing convention).

## Current Ballot Note

Two ballot notes exist at HEAD inside
`source/medicationrequest/medicationrequest-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
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
<blockquote class="ballot-note" id="bn2">
  <p><b>Note to Balloters:</b>
  The code system used in medication request category is presented here but is expected to move to <a href="http://terminology.fhr.org">terminology.hl7.org</a>.
  </p>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) | Dosage redesign could be improved by requiring renderedInstruction | [`b641e8e249fa`](https://github.com/HL7/fhir/commit/b641e8e249fac89aeac83d6e3f5e0e275ccb1058) |
| [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) | MedicationStatement[.status] codes are incorrect | [`358c5eb203b3`](https://github.com/HL7/fhir/commit/358c5eb203b35c6326e060566926db8aeda12352) |

No unattributed commits in the window.

## Per-Ticket Detail

### [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) — Dosage redesign could be improved by requiring renderedInstruction

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will make DosageInstruction.renderedInstructions 1..1. We will
  > remove the text from the definition:
  > ~~To be used when multiple dosage instructions are included to
  > represent complex dosing such as increasing or tapering doses.~~
  > We will add "The renderedInstructions element must always be
  > present to ensure the full dosage intent is communicated in every
  > case."
  >
  > We will change the comment to: The content of the
  > renderedInstructions SHALL contain the information found in the
  > structured dosage, and may contain additional information not
  > found in the structured dosage content, if applicable.

- **Disposition summary:** Make `renderedInstructions` mandatory (1..1)
  on the new `DosageInstruction` / `DosageDetails` shape so balloters
  and implementers always have a deterministic human-readable
  representation of the dose alongside the structured form. The
  binding-side text (definition + comment) is reworded to make the
  "rendered text MUST cover the structured dose" obligation explicit.
- **Commits applying this ticket:**
  - [`b641e8e249fa`](https://github.com/HL7/fhir/commit/b641e8e249fac89aeac83d6e3f5e0e275ccb1058) — `FHIR-54014` — update examples with renderedinstruction (2026-03-05)
- **Changes applied (per Step 5b, scoped to this artifact):** The
  commit adds a `<renderedInstruction value="…"/>` child to the
  `<dosageInstruction>` element in five MedicationRequest examples —
  `medicationrequest0302.xml`, `medicationrequest0303.xml`,
  `medicationrequest0317.xml`, `medicationrequest0321.xml`, and
  `medicationrequest0339.xml` — bringing each example into compliance
  with the new "rendered text MUST be present" rule. The
  cardinality / definition / comment changes themselves live on
  `DosageInstruction` in the datatypes layer and do not appear in
  `MedicationRequest`'s own files in this window. The MedicationRequest
  StructureDefinition was not edited; only the example bodies changed.

### [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) — MedicationStatement[.status] codes are incorrect

- **Work group:** Pharmacy
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will change the definition of the status entered-in-error, from:
  > _Some of the actions that are implied by the medication usage may
  > have occurred. For example, the patient may have taken some of
  > the medication. Clinical decision support systems should take
  > this status into account._
  > to
  > **The statement was entered in error and is not valid.**
  >
  > We will also change the definition for "entered-in-error" for
  > medicationrequest, changing
  > _The request was recorded against the wrong patient or for some
  > reason should not have been recorded (e.g. wrong medication,
  > wrong dose, etc.). Some of the actions that are implied by the
  > medication request may have occurred. For example, the medication
  > may have been dispensed and the patient may have taken some of
  > the medication._
  > to
  > **The request was entered in error and is not valid.**

- **Disposition summary:** Replace the over-broad
  `entered-in-error` definitions on both `MedicationStatement.status`
  and `MedicationRequest.status` with a short, unambiguous
  "entered in error and is not valid" statement. The previous wording
  conflated "data quality error" with "the action partially happened",
  which contradicted the intent of `entered-in-error` across the
  request/event family.
- **Commits applying this ticket:**
  - [`358c5eb203b3`](https://github.com/HL7/fhir/commit/358c5eb203b35c6326e060566926db8aeda12352) — `FHIR-54903` — Fix entered-in-error status definitions for MedicationStatement and MedicationRequest (2026-03-05)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `codesystem-medicationrequest-status.xml`, the `entered-in-error`
  concept's `<definition value="…"/>` is replaced wholesale: the long
  "wrong patient / wrong medication / actions may have occurred"
  paragraph is removed and replaced with `"The request was entered in
  error and is not valid."`. No other concepts in the code system
  change, and the parallel edit to `MedicationStatement.status` lives
  outside this artifact's scope.

## Roll-up Summary (after-applied state)

The window is small and the artifact's StructureDefinition itself is
unchanged. All edits land in the example bodies and one
artifact-scoped CodeSystem:

- **StructureDefinition (`structuredefinition-MedicationRequest.xml`):**
  No changes in window. The renderedInstruction obligation introduced
  by FHIR-54014 takes effect through the `Dosage` / `DosageDetails`
  datatype (out of this artifact's scope) — `MedicationRequest`'s SD
  inherits the new shape without an in-place edit. No snapshot
  regeneration is required from changes in this window's
  MedicationRequest files alone, but a global snapshot regeneration
  will be needed because the underlying datatype changed.
- **Intro / narrative
  (`medicationrequest-introduction.xml`, `medicationrequest-notes.xml`):**
  No changes in window. The existing ballot notes (`bn1`, `bn2`) are
  unmodified — see "Notes for Reviewer" below for the carry-forward
  decision.
- **Search parameters
  (`bundle-MedicationRequest-search-params.xml`):** No changes.
- **Operations (`list-MedicationRequest-operations.xml`):** No changes.
- **Examples:** Five examples updated by FHIR-54014 to add the now
  required `Dosage.renderedInstruction` element — `0302`, `0303`,
  `0317`, `0321`, `0339`. The remaining MedicationRequest examples
  (~50 files) were not touched in this window; many of them either
  already carried a rendered instruction or do not exercise
  `dosageInstruction`. A subsequent sweep may be needed to confirm
  every example with a `<dosageInstruction>` carries a
  `<renderedInstruction>`.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  `codesystem-medicationrequest-status.xml` — definition of
  `entered-in-error` rewritten to `"The request was entered in error
  and is not valid."` (FHIR-54903). All other artifact-scoped value
  sets / code systems are unchanged. No new or removed concepts.
  This code system is artifact-scoped and not (yet) in UTG; the
  parallel definition fix on the MedicationStatement status code
  system is tracked in that artifact.

## Proposed Ballot Note (HTML)

Carry forward `bn1` (still accurate after the renderedInstruction
change) with one new bullet, retain `bn2` unchanged, and add a new
`bn3` for the `entered-in-error` definition fix.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b>
  The elements around Dosage have been subject to breaking changes in R6:
  </p>
  <ul>
   <li>A new data type <a href="dosage.html#DosageDetails"> DosageDetails</a> is introduced, containing rendered instructions and simple or structured <a href="dosage.html#Dosage"> Dosage</a>.</li>
   <li><code>dosageInstruction</code> is now 0..1, and uses the new data type. The composition of complex dosages (with segments, repetitions etc.) can be done using the structure in that data type.</li>
   <li><code>renderedDosageInstruction</code> is removed from the resource and placed in <code>DosageDetails.renderedInstruction</code> in the <a href="dosage.html#DosageDetails"> DosageDetails</a> data type.</li>
   <li><code>DosageInstruction.renderedInstructions</code> is now <b>1..1</b> and SHALL convey the full dose intent in human-readable form, even when the structured dose is also populated. The MedicationRequest examples have been updated accordingly (<a href="https://jira.hl7.org/browse/FHIR-54014">FHIR-54014</a>).</li>
   <li>A set of <a href="dosage-examples.html"> examples</a> is provided to show how structured dosages can be represented.</li>
  </ul>
</blockquote>

<blockquote class="ballot-note" id="bn2">
  <p><b>Note to Balloters:</b>
  The code system used in medication request category is presented here but is expected to move to <a href="http://terminology.hl7.org">terminology.hl7.org</a>.
  </p>
</blockquote>

<blockquote class="ballot-note" id="bn3">
  <p><b>Note to Balloters:</b>
  The definition of <code>MedicationRequest.status = entered-in-error</code> has been tightened to <em>"The request was entered in error and is not valid."</em> The previous wording conflated a data-entry error with the possibility that some implied actions had still occurred, which contradicted the meaning of <code>entered-in-error</code> elsewhere in the request/event pattern. Reviewers should confirm the new, narrower meaning matches local guidance for handling cancelled-versus-erroneous orders. A parallel change has been applied to <code>MedicationStatement.status</code> (<a href="https://jira.hl7.org/browse/FHIR-54903">FHIR-54903</a>).</p>
</blockquote>
```

## Notes for Reviewer

- `bn1` was retained because every existing bullet still describes the
  after-applied state at HEAD; the only addition is the new bullet
  recording that `DosageInstruction.renderedInstructions` is now
  mandatory (FHIR-54014). The actual cardinality/definition/comment
  edit to `DosageInstruction` itself lives in the datatypes layer and
  is not visible in MedicationRequest's own files in this window — the
  evidence inside this artifact is the five updated examples.
- `bn2` was retained verbatim. The typo `terminology.fhr.org` in the
  existing note has been corrected to `terminology.hl7.org` in the
  proposed text — this is editorial only and not driven by a ticket.
  If editorial changes are out of scope for the current ballot, drop
  that fix and keep the existing href.
- `bn3` is new. It cites only FHIR-54903 because that is the only
  ticket in the window that affects the MedicationRequest status code
  system.
- FHIR-54014's per-ticket changes inside this artifact are limited to
  five examples; the remaining ~50 MedicationRequest examples were not
  touched in this window. A follow-up audit may be warranted to
  confirm that every example with a `<dosageInstruction>` block now
  carries a `<renderedInstruction>` consistent with the new 1..1
  obligation.
- Cross-reference lookups (`fhir-augury-cli cross-referenced`) for
  both commit SHAs returned zero hits; ticket attribution was derived
  from the `FHIR-XXXXX` prefix in each commit subject. Both tickets
  have empty `comments` arrays in Jira, so the disposition text was
  taken from `metadata.resolution_description` (surfaced via the
  ticket snapshot). No applied-vote comment was available for either
  ticket.
- `git` against the cache clone resolved the since-commit and HEAD
  cleanly; `gh` was not needed.

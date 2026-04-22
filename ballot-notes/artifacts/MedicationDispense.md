# Artifact Ballot Note Draft: MedicationDispense (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `MedicationDispense` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `MedicationDispense` for this run (folder `source/medicationdispense/`, lowercased per the FhirCore briefing's authoring convention):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/medicationdispense/structuredefinition-MedicationDispense.xml` | StructureDefinition | no |
| `source/medicationdispense/medicationdispense-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/medicationdispense/medicationdispense-notes.xml` | Supplementary narrative | no |
| `source/medicationdispense/bundle-MedicationDispense-search-params.xml` | Search parameters | no |
| `source/medicationdispense/list-MedicationDispense-operations.xml` | Operations | no |
| `source/medicationdispense/list-MedicationDispense-examples.xml` | Examples list | no |
| `source/medicationdispense/list-MedicationDispense-packs.xml` | Packs list | no |
| `source/medicationdispense/implementationguide-MedicationDispense-core.xml` | IG manifest fragment | no |
| `source/medicationdispense/medicationdispense-event-mapping-exceptions.xml` | EventPattern mapping exceptions | no |
| `source/medicationdispense/medicationdispense-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/medicationdispense/medicationdispense-examples-header.xml` | Examples table header | no |
| `source/medicationdispense/medicationdispense-example.xml`, `medicationdispense03NN.xml`, `medicationdispenseexample8.xml` | Example instances (47 files) | yes (5 of 47 — see roll-up) |
| `source/medicationdispense/codesystem-medicationdispense-category.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationdispense/codesystem-medicationdispense-status-reason.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationdispense/codesystem-medicationdispense-status.xml` | Artifact-scoped CodeSystem | no |
| `source/medicationdispense/valueset-medication-dispense-type-codes.xml` | Artifact-scoped ValueSet | no |
| `source/medicationdispense/valueset-medicationdispense-category.xml` | Artifact-scoped ValueSet | no |
| `source/medicationdispense/valueset-medicationdispense-performer-function.xml` | Artifact-scoped ValueSet | no |
| `source/medicationdispense/valueset-medicationdispense-status-reason.xml` | Artifact-scoped ValueSet | no |
| `source/medicationdispense/valueset-medicationdispense-status.xml` | Artifact-scoped ValueSet | no |
| `source/medicationdispense/invariant-tests/` | FHIRPath invariant test fixtures | no |
| `source/medicationdispense/medicationdispense.svg` | Resource diagram | no |

Patterns from the FhirCore briefing that produced no match in the clone for this artifact:

- `source/medicationdispense/medicationdispense-spreadsheet.xml` — no file matched (no legacy spreadsheet shipped for this resource).
- Sibling `structuredefinition-*.xml` whose stem differs from the folder name — none exist.

## Current Ballot Note

Two existing ballot notes are present at HEAD in `medicationdispense-introduction.xml`:

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
The code system used in medication dispense category is presented here but is expected to move to <a href="http://terminology.fhr.org">terminology.hl7.org</a>.
</p>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) | Dosage redesign could be improved by requiring renderedInstruction | [`b641e8e249fa`](https://github.com/HL7/fhir/commit/b641e8e249fac89aeac83d6e3f5e0e275ccb1058) |

## Per-Ticket Detail

### [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) — Dosage redesign could be improved by requiring renderedInstruction

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will make DosageInstruction.renderedInstructions 1..1. We will remove the text from the definition: ~~To be used when multiple dosage instructions are included to represent complex dosing such as increasing or tapering doses.~~ We will add "The renderedInstructions element must always be present to ensure the full dosage intent is communicated in every case."
  >
  > We will change the comment to: The content of the renderedInstructions SHALL contain the information found in the structured dosage, and may contain additional information not found in the structured dosage content, if applicable.

- **Disposition summary:** The Pharmacy work group accepted the request that `renderedInstructions` be mandatory on `DosageInstruction`, raising the cardinality to 1..1 and updating the element's definition / comment to clarify that the rendered text must always carry the full dosage intent and must agree with (and may extend) the structured content. The structural change itself lives on the `Dosage` / `DosageDetails` datatype, not on `MedicationDispense`; this artifact's update is to bring its examples into compliance with the new requirement.
- **Commits applying this ticket:**
  - [`b641e8e249fa`](https://github.com/HL7/fhir/commit/b641e8e249fac89aeac83d6e3f5e0e275ccb1058) — `FHIR-54014` "update examples with renderedinstruction" (2026-03-05, Jose Costa Teixeira)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Five MedicationDispense example instances were edited. In `medicationdispense0302.xml`, `medicationdispense0305.xml`, `medicationdispense0306.xml`, and `medicationdispense0319.xml`, a new `<renderedInstruction value="…"/>` child was prepended to `<dosageInstruction>` so each example now satisfies the upcoming `DosageInstruction.renderedInstructions 1..1` requirement; the rendered text in each case paraphrases the existing structured `<step>` content (e.g., insulin sliding-scale, tapering tablet schedule, IV escalation, two-then-one tablet course). `medicationdispense0311.xml` received a cosmetic fix only — the NDC `<display>` value `"ACEPHEN  (product)"` lost its double space. The StructureDefinition, narrative intro, notes, search-parameter bundle, operations list, examples list, and artifact-scoped terminology were **not** modified in this window; the data-type change that backs this ticket lives in the Dosage datatype source rather than under `source/medicationdispense/`.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-MedicationDispense.xml`):** No changes in window. No element additions/removals, no cardinality, type, binding, or constraint edits, and no snapshot regeneration is required from MedicationDispense itself. (The mandatory `renderedInstructions` lives on the Dosage datatype; MedicationDispense inherits it transitively via `dosageInstruction` typed as `DosageDetails`.)
- **Intro / narrative (`medicationdispense-introduction.xml`, `medicationdispense-notes.xml`):** No changes in window. The existing `bn1` ballot note about the R6 Dosage redesign and the `bn2` note about the category code system remain in place verbatim.
- **Search parameters (`bundle-MedicationDispense-search-params.xml`):** No changes in window.
- **Operations (`list-MedicationDispense-operations.xml`):** No changes in window.
- **Examples:** Four examples (`medicationdispense0302`, `0305`, `0306`, `0319`) gained a `Dosage.renderedInstruction` value so that they conform to the now-mandatory rendered-instruction requirement coming in via the Dosage datatype. One example (`medicationdispense0311`) was given a minor display-value whitespace fix unrelated to dosage. No examples were added or removed; `list-MedicationDispense-examples.xml` is unchanged.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes in window. The pre-existing `bn2` ballot note continues to flag that `codesystem-medicationdispense-category.xml` is expected to migrate to terminology.hl7.org per the FhirCore briefing's UTG cross-repo touch points.

## Proposed Ballot Note (HTML)

The window contains only example updates that ride along with a Dosage-datatype change (`renderedInstructions` becoming 1..1). MedicationDispense itself was not restructured. The existing `bn1` bullets are all still accurate after applying the window, so they are carried forward and a new bullet is added to surface the mandatory-rendered-instruction requirement that balloters will now see in every MedicationDispense example. `bn2` is unchanged.

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b>
The elements around Dosage have been subject to breaking changes in R6:
</p>
<ul>
 <li>A new data type <a href="dosage.html#DosageDetails"> DosageDetails</a> is introduced, containing rendered instructions and simple or structured <a href="dosage.html#Dosage"> Dosage</a>. </li>
 <li><code>dosageInstruction</code> is now 0..1, and uses the new data type. The composition of complex dosages (with segments, repetitions etc.) can be done using the structure in that data type.</li>
 <li><code>renderedDosageInstruction</code> is removed from the resource and placed in <code>DosageDetails.renderedInstruction</code> in the <a href="dosage.html#DosageDetails"> DosageDetails</a> data type.</li>
 <li><code>DosageInstruction.renderedInstructions</code> is now mandatory (1..1) and must convey the full dosage intent — it must contain the information present in the structured dosage and may add anything that cannot be expressed structurally. The MedicationDispense examples have been updated to include a <code>renderedInstruction</code> alongside their structured <code>step</code> content (<a href="https://jira.hl7.org/browse/FHIR-54014">FHIR-54014</a>).</li>
 <li>A set of <a href="dosage-examples.html"> examples</a> is provided to show how structured dosages can be represented.</li>
</ul>
</blockquote>
```

```html
<blockquote class="ballot-note" id="bn2">
<p><b>Note to Balloters:</b>
The code system used in medication dispense category is presented here but is expected to move to <a href="http://terminology.fhr.org">terminology.hl7.org</a>.
</p>
</blockquote>
```

## Notes for Reviewer

- The substantive structural change behind FHIR-54014 (raising `DosageInstruction.renderedInstructions` to 1..1 and revising its definition / comment) is implemented in the Dosage datatype source, not under `source/medicationdispense/`. Reviewers comparing this artifact's SD between ballots should not expect to see it here; the dispense-side impact in this window is limited to example conformance.
- `cross-referenced` for commit `b641e8e249fa` returned no Jira hits; the `FHIR-54014` attribution is taken from the commit subject (`FHIR-54014 update examples with renderedinstruction`), which matches the ticket's resolution and applied state.
- The clone's `briefing.md` was generated against clone HEAD `1b369ff4e28e`; this run was executed against clone HEAD `db79dcdfe196`. The artifact-map patterns from the briefing still resolve cleanly against the current HEAD, so the briefing was used as-is.
- No existing ballot-note bullets were dropped — every item in the prior `bn1` and `bn2` notes remains accurate in the after-applied state.
- `bn2` flags a planned UTG migration for `codesystem-medicationdispense-category`; no commits in this window acted on that migration.

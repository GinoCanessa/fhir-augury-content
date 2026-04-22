# Artifact Ballot Note Draft: Immunization (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Immunization` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 4 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T20:00:00Z |

## Source Files

Files considered part of `Immunization` for this run (under `source/immunization/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/immunization/structuredefinition-Immunization.xml` | StructureDefinition | yes |
| `source/immunization/immunization-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/immunization/immunization-notes.xml` | Supplementary narrative | no |
| `source/immunization/bundle-Immunization-search-params.xml` | Search parameters | no |
| `source/immunization/list-Immunization-operations.xml` | Operations | no |
| `source/immunization/list-Immunization-examples.xml` | Examples list | no |
| `source/immunization/list-Immunization-packs.xml` | Packs list | no |
| `source/immunization/immunization-event-mapping-exceptions.xml` | Workflow Event mapping exceptions | yes |
| `source/immunization/immunization-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/immunization/implementationguide-Immunization-core.xml` | IG manifest | no |
| `source/immunization/immunization-example*.xml` | Examples (6 files) | no |
| `source/immunization/immunization-examples-header.xml` | Examples header | no |
| `source/immunization/valueset-immunization-origin.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-reason.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-route.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-site.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-status-reason.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-status.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-target-disease.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-vaccine-funding-program.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-vaccine-code.xml` | Artifact-scoped ValueSet | no |
| `source/immunization/valueset-immunization-function.xml` | Artifact-scoped ValueSet (deleted in window) | yes (deleted) |
| `source/immunization/invariant-tests/imm-{1,2}.{p1.pass,f1.fail}.json` | Invariant test fixtures (added in window) | yes (added) |

No `*-spreadsheet.xml`, `*-notes.xml` change, sibling `structuredefinition-*.xml`, or `codesystem-*.xml` matched in this window.

## Current Ballot Note

The current ballot note at HEAD (`source/immunization/immunization-introduction.xml`):

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure that the Immunization resource is ready for Normative status, we are seeking ballot comments on the substantive content.</p>
<ul>
<li>The key changes made since the January 2026 R6 ballot include:</li>
  <ul>
  <li>Updated Immunization.performer.function value set to use a value set defined in THO rather than in the FHIR base standard. - <a href="https://jira.hl7.org/browse/FHIR-53465">FHIR-53465</a></li>
  <li>Updated Immunization.statusReason to clarify usage and add an invariant. - <a href="https://jira.hl7.org/browse/FHIR-54325">FHIR-54325</a></li>
  <li>Updated narrative text to reference changed names of data elements in the Medication resource. - <a href="https://jira.hl7.org/browse/FHIR-55486">FHIR-55486</a></li>
  <li>Added invariant to .subpotentReason. - <a href="https://jira.hl7.org/browse/FHIR-54326">FHIR-54326</a></li>
  </ul>
</ul>
</blockquote>
```

## Tickets Applied in Window

None of the four commits include a Jira key in their commit subject/body, and `cross-referenced` returned no hits for any of the SHAs. Ticket attribution below is therefore inferred from the commit content matched against the four tickets cited by the in-tree ballot note.

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53465](https://jira.hl7.org/browse/FHIR-53465) | Update Immunization.performer.function to THO value set | [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed) |
| [FHIR-54325](https://jira.hl7.org/browse/FHIR-54325) | Update the short name and comment in statusReason to align with the definition | [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed), [`35aac5918b52`](https://github.com/HL7/fhir/commit/35aac5918b520fda7bf1874a3cb85c546f64fc2c) |
| [FHIR-54326](https://jira.hl7.org/browse/FHIR-54326) | Missing constraint: An invariant should enforce: "subpotentReason SHALL only be present if isSubpotent is true." | [`35aac5918b52`](https://github.com/HL7/fhir/commit/35aac5918b520fda7bf1874a3cb85c546f64fc2c) |
| [FHIR-55486](https://jira.hl7.org/browse/FHIR-55486) | Update Immunization narrative to account for changes in Medication | [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed) |
| (unattributed) | Ballot-note authoring (meta) | [`2b1fe4c966ab`](https://github.com/HL7/fhir/commit/2b1fe4c966ab0534ff1397cb94e46f4a70e4c086), [`89dee5631672`](https://github.com/HL7/fhir/commit/89dee5631672c8015817245ebe832c5d11726ad1) |

## Per-Ticket Detail

### [FHIR-54325](https://jira.hl7.org/browse/FHIR-54325) — Update the short name and comment in statusReason to align with the definition

- **Work group:** Public Health
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (no comments returned by `fhir-augury-cli`).

- **Disposition summary:** The submitter argued that `Immunization.statusReason`'s short ("Reason for current status") and comment did not match its definition (only used when status = `not-done`). The proposal — adopted with modification — was to retitle the element, bold the "not performed" wording in the definition, and clarify that the comment applies only to the `not-done` status. As applied, the team broadened both the definition and comment to also cover `entered-in-error`, and added invariant `imm-1` to enforce the constraint.
- **Commits applying this ticket:**
  - [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed) — R6 ballot comment updates (2026-03-06)
  - [`35aac5918b52`](https://github.com/HL7/fhir/commit/35aac5918b520fda7bf1874a3cb85c546f64fc2c) — Adding invariants to Immunization (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-Immunization.xml`, the `Immunization.statusReason` element's `short` was changed from "Reason for current status" to "Reason not done"; the `definition` was rewritten to "Indicates the reason the immunization event was \*\*not performed\*\* or was \*\*entered in error\*\*."; and the `comment` was rewritten from "This is generally only used for the status of \"not-done\"…" to "This element is only used for the status of \"not-done\" or \"entered-in-error\". The reason for performing the immunization event is captured in reasonCode, not here." The matching `<shortUnmatched>` and updated `<definitionUnmatched>` / `<commentsUnmatched>` blocks were added to `immunization-event-mapping-exceptions.xml` to keep the workflow `Event` pattern mapping aligned. The follow-up commit added the `imm-1` constraint on the Immunization root (FHIRPath `statusReason.exists() implies status = 'not-done'`) plus passing/failing test fixtures under `invariant-tests/`. Note that the as-shipped definition/comment broaden the scope from the originally-proposed `not-done`-only wording to also include `entered-in-error`, while `imm-1` (correctly) still restricts statusReason to `status = 'not-done'`.

### [FHIR-53465](https://jira.hl7.org/browse/FHIR-53465) — Update Immunization.performer.function to THO value set

- **Work group:** Public Health
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (no comments returned by `fhir-augury-cli`).

- **Disposition summary:** The ticket asked to rebind `Immunization.performer.function` to the THO-hosted ValueSet `http://terminology.hl7.org/ValueSet/immunization-function` and to delete the FHIR-Core copy of the value set, as part of the broader effort to migrate static terminology out of the FHIR Core spec into THO.
- **Commits applying this ticket:**
  - [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed) — R6 ballot comment updates (2026-03-06)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-Immunization.xml` the binding for `Immunization.performer.function` was repointed from `http://hl7.org/fhir/ValueSet/immunization-function` to `http://terminology.hl7.org/ValueSet/immunization-function` (binding strength `extensible` is unchanged). The artifact-scoped `valueset-immunization-function.xml` (43 lines) was deleted. No companion edit to the resource's narrative was made for this change.

### [FHIR-54326](https://jira.hl7.org/browse/FHIR-54326) — Missing constraint: subpotentReason SHALL only be present if isSubpotent is true

- **Work group:** Public Health
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (no comments returned by `fhir-augury-cli`).

- **Disposition summary:** Add a resource-level invariant enforcing that `Immunization.subpotentReason` may only be populated when `isSubpotent` is `true`, mirroring the (separately-tracked) statusReason/status constraint.
- **Commits applying this ticket:**
  - [`35aac5918b52`](https://github.com/HL7/fhir/commit/35aac5918b520fda7bf1874a3cb85c546f64fc2c) — Adding invariants to Immunization (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** Added constraint `imm-2` (severity `error`) to the Immunization root in `structuredefinition-Immunization.xml`: human "subpotentReason SHALL only be present if isSubpotent is 'true'", FHIRPath `subpotentReason.exists() implies (isSubpotent.exists() and isSubpotent = true)`, source `http://hl7.org/fhir/StructureDefinition/Immunization`. Companion test fixtures `invariant-tests/imm-2.p1.pass.json` and `imm-2.f1.fail.json` were added.

### [FHIR-55486](https://jira.hl7.org/browse/FHIR-55486) — Update Immunization narrative to account for changes in Medication

- **Work group:** Public Health
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (no comments returned by `fhir-augury-cli`).

- **Disposition summary:** The Boundaries-and-Relationship section of the Immunization intro referenced the pre-R6 names `Medication.batch.lotNumber` and `Medication.batch.expirationDate`. With the R6 rename of that backbone element from `batch` to `instance`, the narrative had to be updated to `Medication.instance.lotNumber` / `Medication.instance.expirationDate`.
- **Commits applying this ticket:**
  - [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed) — R6 ballot comment updates (2026-03-06)
- **Changes applied (per Step 5b, scoped to this artifact):** In `immunization-introduction.xml`, the sentence describing the Medication-side analogues was updated to read "Medication.marketingAuthorizationHolder, Medication.instance.lotNumber and Medication.instance.expirationDate" (previously `Medication.batch.lotNumber` / `Medication.batch.expirationDate`). No SD or example changes were required.

### (unattributed) — Ballot-note authoring (meta)

- **Commits:**
  - [`2b1fe4c966ab`](https://github.com/HL7/fhir/commit/2b1fe4c966ab0534ff1397cb94e46f4a70e4c086) — Add Note to Balloters for Immunizations and Medications Module (2026-03-09)
  - [`89dee5631672`](https://github.com/HL7/fhir/commit/89dee5631672c8015817245ebe832c5d11726ad1) — Updates to Notes to Balloters (2026-03-09)
- **Changes applied:** Authored and then refined the in-tree `<blockquote class="ballot-note" id="bn1">` block at the top of `immunization-introduction.xml` that summarises the four substantive changes above. These commits do not themselves modify resource content; they are the existing ballot note that this draft is replacing/updating.

## Roll-up Summary (after-applied state)

Per `git diff 5d67a34a..HEAD -- source/immunization/`, four files are net-changed and two new groups of files are added:

- **StructureDefinition (`structuredefinition-Immunization.xml`):**
  - Added two root-level constraints: `imm-1` ("statusReason SHALL only be present if the immunization status is 'not-done'", FHIRPath `statusReason.exists() implies status = 'not-done'`) and `imm-2` ("subpotentReason SHALL only be present if isSubpotent is 'true'", FHIRPath `subpotentReason.exists() implies (isSubpotent.exists() and isSubpotent = true)`). Both `error` severity.
  - `Immunization.statusReason`: `short` → "Reason not done"; `definition` → "Indicates the reason the immunization event was \*\*not performed\*\* or was \*\*entered in error\*\*."; `comment` → "This element is only used for the status of \"not-done\" or \"entered-in-error\". The reason for performing the immunization event is captured in reasonCode, not here." Cardinality and type unchanged.
  - `Immunization.performer.function` binding repointed from `http://hl7.org/fhir/ValueSet/immunization-function` to `http://terminology.hl7.org/ValueSet/immunization-function`. Strength remains `extensible`.
  - Snapshot regeneration is required for all of the above; per skill rules, snapshot edits are not enumerated here.
- **Intro / narrative (`immunization-introduction.xml`):**
  - Inserted a new `<blockquote class="ballot-note" id="bn1">` at the top of the file summarising the four substantive R6-ballot changes (this is the note being revised by the present draft).
  - Updated the Medication-cross-reference paragraph in Scope-and-Usage to refer to `Medication.instance.lotNumber` / `Medication.instance.expirationDate` (was `Medication.batch.…`), tracking the R6 Medication rename.
  - `immunization-notes.xml` was not touched.
- **Search parameters (`bundle-Immunization-search-params.xml`):** No changes.
- **Operations (`list-Immunization-operations.xml`):** No changes.
- **Examples:** None of the existing `immunization-example*.xml` files were touched. New JSON test fixtures were added under `source/immunization/invariant-tests/` (`imm-1.p1.pass.json`, `imm-1.f1.fail.json`, `imm-2.p1.pass.json`, `imm-2.f1.fail.json`) that exercise the new invariants.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - Deleted `valueset-immunization-function.xml` (the FHIR-Core copy of the `immunization-function` ValueSet); its replacement now lives in THO at `http://terminology.hl7.org/ValueSet/immunization-function` (cross-repo touch point: `HL7/UTG`). Ensure UTG carries the migrated content before publication.
  - No other artifact-scoped value sets or code systems changed.
- **Workflow mapping (`immunization-event-mapping-exceptions.xml`):**
  - The `Event.statusReason` ↔ `Immunization.statusReason` divergence block was updated to reflect the new short ("Reason for current status" vs "Reason not done"), the broadened definition (now also covering `entered-in-error`), and the rewritten comment.

## Proposed Ballot Note (HTML)

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To progress the Immunization resource toward Normative status, the resource was updated for the R6 ballot with the substantive changes listed below. Comments are particularly welcomed on the new invariants and on the broadened scope of <code>Immunization.statusReason</code>.</p>
  <ul>
    <li>Rebound <code>Immunization.performer.function</code> from the FHIR-Core copy of the <em>Immunization Function Codes</em> value set to the THO-hosted value set (<code>http://terminology.hl7.org/ValueSet/immunization-function</code>); the FHIR-Core copy has been removed (<a href="https://jira.hl7.org/browse/FHIR-53465">FHIR-53465</a>).</li>
    <li>Clarified <code>Immunization.statusReason</code>: renamed the short to "Reason not done", rewrote the definition and comment to make explicit that the element applies when <code>status</code> is <code>not-done</code> <em>or</em> <code>entered-in-error</code>, and added invariant <code>imm-1</code> requiring <code>statusReason.exists() implies status = 'not-done'</code> (<a href="https://jira.hl7.org/browse/FHIR-54325">FHIR-54325</a>). Balloters are asked whether the new invariant should also permit <code>entered-in-error</code>, given the broadened narrative.</li>
    <li>Added invariant <code>imm-2</code> requiring <code>subpotentReason.exists() implies (isSubpotent.exists() and isSubpotent = true)</code>, so that a sub-potency reason can only be recorded when the dose is flagged sub-potent (<a href="https://jira.hl7.org/browse/FHIR-54326">FHIR-54326</a>).</li>
    <li>Updated the Boundaries and Relationships narrative to refer to <code>Medication.instance.lotNumber</code> and <code>Medication.instance.expirationDate</code>, tracking the R6 rename of <code>Medication.batch</code> to <code>Medication.instance</code> (<a href="https://jira.hl7.org/browse/FHIR-55486">FHIR-55486</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Inferred ticket attribution.** None of the four commits in the window carry a `FHIR-NNNNN` token in their subject or body, and `fhir-augury-cli cross-referenced` returned no hits for any of the SHAs. Ticket attribution is therefore inferred by matching commit content against the four tickets the in-tree ballot note already cites. The mapping is high-confidence (each ticket lines up with a distinct, unambiguous code change), but if the FhirCore working group has an internal authoritative mapping, that should override this report's table.
- **Carry-forward of existing bullets.** All four bullets in the existing `bn1` note describe changes that are still present in the after-applied diff, so all four are retained in the proposed note. Wording was tightened and made more specific (naming the new invariant keys, the new value-set canonical, and the renamed Medication element) per the skill's "be specific" rule. No bullets were dropped as superseded or reverted.
- **Broadened `statusReason` scope vs. invariant.** The applied changes for FHIR-54325 broaden `statusReason`'s narrative scope to include `entered-in-error`, but invariant `imm-1` only permits `status = 'not-done'`. The two will need to be reconciled (either tighten the narrative back to `not-done`, or relax `imm-1` to also allow `entered-in-error`); this is flagged in the proposed ballot-note bullet for FHIR-54325 as an explicit balloter question.
- **Cross-repo touch point.** Deletion of `valueset-immunization-function.xml` makes the binding dependent on `HL7/UTG`; confirm the THO value set at `http://terminology.hl7.org/ValueSet/immunization-function` is published and at the right version before R6 ballot freeze.
- **Disposition text unavailable.** `fhir-augury-cli get …` returned `comments.Count = 0` for all four tickets, so the verbatim work-group disposition text is not reproduced. The "Disposition summary" paragraphs are derived from each ticket's description (`metadata` + `content`) and the after-applied diff.
- **Snapshot regeneration.** Multiple SD changes (two new constraints, three edits to `statusReason`, one binding repoint) require regeneration of the Immunization snapshot; per skill rules the snapshot edits are not narrated.

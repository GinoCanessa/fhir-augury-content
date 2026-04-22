# Datatypes Ballot Note Draft (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/datatypes.html` |
| Source root | `source/datatypes/` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Datatypes touched | 2 (`Dosage`, `DosageDetails`) plus a shared changelog file |
| Focus datatypes | (all touched) |
| Commits in window | 10 |
| Tickets attributed | 7 (5 cited in the in-scope `_changelog.txt`; 2 additional referenced from in-window commit subjects but with primary edits outside `source/datatypes/`) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` (briefing slightly behind current HEAD `db79dcdfe196`) |
| Generated | 2026-04-21T00:00:00Z |

## Datatypes Touched

| Datatype | Files touched | Tickets | Page-level? |
|----------|---------------|---------|-------------|
| `Dosage` | 1 (`source/datatypes/dosage.xml`) | [FHIR-54848](https://jira.hl7.org/browse/FHIR-54848) | no |
| `DosageDetails` | 1 (`source/datatypes/dosagedetails.xml`) | [FHIR-54651](https://jira.hl7.org/browse/FHIR-54651), [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) | no |
| (Page-level / shared) | 1 (`source/datatypes/_changelog.txt`, **new file**) | [FHIR-54651](https://jira.hl7.org/browse/FHIR-54651), [FHIR-54848](https://jira.hl7.org/browse/FHIR-54848), [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014), [FHIR-56016](https://jira.hl7.org/browse/FHIR-56016), [FHIR-54523](https://jira.hl7.org/browse/FHIR-54523) | yes |

Note: `source/datatypes.html` itself was not touched in the window.

## Source Files

Files considered in this run, grouped by datatype bucket:

### `Dosage`

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/datatypes/dosage.xml` | Authoring spreadsheet (legacy SpreadsheetML; authoritative for this datatype — no separate StructureDefinition source) | yes |

### `DosageDetails`

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/datatypes/dosagedetails.xml` | Authoring spreadsheet (legacy SpreadsheetML; authoritative for this datatype) | yes |

### (Page-level / shared)

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/datatypes.html` | Datatypes page (ballot note would live here) | no |
| `source/datatypes/_changelog.txt` | Per-folder change log (added in this window; later split per resource) | yes |

## Current Ballot Note

No existing ballot note on `source/datatypes.html` at HEAD (`db79dcdfe196`). The proposed
note (below) would be inserted at the top of the page body, immediately after the
opening `<h1>Datatypes</h1>` / standards-status table block and before the
"Types Framework Cross Reference" paragraph, wrapped as
`<blockquote class="ballot-note" id="bn1">…</blockquote>`.

> Note for context: a related ballot note already exists on
> `source/dosage.html` (`<blockquote class="ballot-note">…`) covering the broader
> R6 Dosage / DosageDetails reorganisation. That note is **not** modified by this
> skill (its page is outside this skill's scope); see "Notes for Reviewer" below
> for a pointer to `notes-page`.

## Tickets Applied in Window

| Ticket | Title | Datatypes | Commits |
|--------|-------|-----------|---------|
| [FHIR-54651](https://jira.hl7.org/browse/FHIR-54651) | Dosage - remove "simple" an use step.component | `DosageDetails` | [`accc7b7f11fd`](https://github.com/HL7/fhir/commit/accc7b7f11fd24da385298c692cdd0304cc220ee), [`741be42b1e22`](https://github.com/HL7/fhir/commit/741be42b1e22361606d6eeea925341e6b5119560), [`fc2e165a096d`](https://github.com/HL7/fhir/commit/fc2e165a096de579254a1e00663de6ad22699ab7) |
| [FHIR-54848](https://jira.hl7.org/browse/FHIR-54848) | Dosage site lack of expressivity | `Dosage` | [`b33db10cfc75`](https://github.com/HL7/fhir/commit/b33db10cfc759e1be46677f7ee5fe8e76913b7d3) |
| [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) | Dosage redesign could be improved by requiring renderedInstruction | `DosageDetails` | [`efe537aa9a92`](https://github.com/HL7/fhir/commit/efe537aa9a928e9adbd54659c83cd02482cb34e9) |
| [FHIR-54451](https://jira.hl7.org/browse/FHIR-54451) | When to use reason vs relatedClinicalInformation | (changelog only — primary edits in `source/medicationstatement/`) | [`84c55f6b66ee`](https://github.com/HL7/fhir/commit/84c55f6b66eedb0c7341526f2cbf4a914ec4ed7a) |
| [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) | MedicationStatement[.status] codes are incorrect | (changelog only — primary edits in `source/medicationrequest/`, `source/medicationstatement/`) | [`358c5eb203b3`](https://github.com/HL7/fhir/commit/358c5eb203b35c6326e060566926db8aeda12352) |
| [FHIR-56016](https://jira.hl7.org/browse/FHIR-56016) | Dosage - examples have step.timing, should have step.component.timing | (changelog only — primary edits in `source/dosage-examples.html`) | (no in-scope commit; cited by curated `_changelog.txt`) |
| [FHIR-54523](https://jira.hl7.org/browse/FHIR-54523) | Textural representation does not match with structural representation | (changelog only — primary edits in `source/dosage-examples.html`) | (no in-scope commit; cited by curated `_changelog.txt`) |
| (unattributed) | "commit excel" — XML formatting by publisher after applying FHIR-54651 | `DosageDetails` | [`28a2ce8e42b9`](https://github.com/HL7/fhir/commit/28a2ce8e42b9ae19de4329d680cae82eb9dc8ba7) |
| (unattributed) | "add files to changelog" | (page-level / shared) | [`755c842235cd`](https://github.com/HL7/fhir/commit/755c842235cd0e66cc510c84231349343707fdf6) |
| (unattributed) | "separate changelogs per resource type" | (page-level / shared) | [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd) |

## Per-Ticket Detail

### [FHIR-54651](https://jira.hl7.org/browse/FHIR-54651) — Dosage - remove "simple" an use step.component

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Datatypes touched:** `DosageDetails`
- **Disposition (verbatim):**

  > We will remove the element Dosage.simple
  >
  > We will update the documentation:
  > *Dosages may contain renderedInstruction and/or structured data (as a simple dosage or a complex sequence of step elements).*
  > to
  > **Dosages may contain renderedInstruction and/or structured data.**
  >
  > and
  > *Either a simple dosage, or a complex dosage course with one or more step items, able to represent multiple dose regimes with tapering doses, and event relationships*
  > to
  > **Either a simple dosage expressed as a single step or a complex dosage course expressed with one or more steps, able to represent multiple dose regimes with tapering doses, and event relationships**
  >
  > We will add an invariant that says "if only one step is present, DosageDetails.step.safety shall not be populated"
  >
  > remove dosdet-1 invariant (or recycle it to the invariant above?)
  >
  > Update examples accordingly / where applicable

- **Disposition summary:** Eliminate the redundant `DosageDetails.simple` element, since a "simple" dosage is fully expressible as a single `step`. Replace the now-meaningless `dosdet-1` invariant ("complex" — `simple.empty() or step.empty()`) with a new invariant `no-safety-on-simple` enforcing that when only one step is present, `step.safety` is not populated (callers should use `DosageDetails.safety` for the whole-course safety in that case). Update prose accordingly.
- **Commits applying this ticket:**
  - [`accc7b7f11fd`](https://github.com/HL7/fhir/commit/accc7b7f11fd24da385298c692cdd0304cc220ee) — FHIR-54651 (2026-03-05)
  - [`741be42b1e22`](https://github.com/HL7/fhir/commit/741be42b1e22361606d6eeea925341e6b5119560) — FHIR-54651 (2026-03-05)
  - [`fc2e165a096d`](https://github.com/HL7/fhir/commit/fc2e165a096de579254a1e00663de6ad22699ab7) — FHIR-54651 - fix invariant (2026-03-05)
- **Changes applied (per Step 5c, scoped to the datatypes page):** In `source/datatypes/dosagedetails.xml` (the legacy authoring spreadsheet that *is* the source for `DosageDetails`):
  - The `DosageDetails.simple` row is renamed to `!DosageDetails.simple` (publisher convention for "removed" — the element is dropped from the rendered SD).
  - The `complex` invariant (id `1`, expression `simple.empty() or step.empty()`, "Can only have a simple dose, or one or more steps in a sequence") is replaced with a new invariant `no-safety-on-simple` (id `2`, expression `step.count() = 1 implies step.safety.empty()`, "If only one step is present, DosageDetails.step.safety shall not be populated").
  - A subsequent publisher pass ([`28a2ce8e42b9`](https://github.com/HL7/fhir/commit/28a2ce8e42b9ae19de4329d680cae82eb9dc8ba7), commit message "XML formatting by publisher after applying FHIR-54651") rewrote the spreadsheet's whitespace / row heights — no semantic change. Snapshot regeneration of `DosageDetails` is required at the next publisher run.
- **Note from reporter:** Per the [2026-04-08 Jira comment](https://jira.hl7.org/browse/FHIR-54651) on the ticket — "this was obviously DosageDetails, not Dosage. invariant was removed, a new one was created with a different ID" — the resolution targets `DosageDetails`, not the special-purpose `Dosage` datatype.

### [FHIR-54848](https://jira.hl7.org/browse/FHIR-54848) — Dosage site lack of expressivity

- **Work group:** Pharmacy
- **Resolution:** Persuasive
- **Datatypes touched:** `Dosage`
- **Disposition (verbatim):**

  > We will change dosage.site to CodeableReference(BodyStructure) and keep the same binding on the CodeableConcept part.

- **Disposition summary:** Promote `Dosage.site` from `CodeableConcept` to `CodeableReference(BodyStructure)` so callers can either keep using the existing example-bound coded concept or reference a `BodyStructure` resource for richer site descriptions (laterality, location qualifiers). The example binding to `MedicationAdministrationSite` is retained on the `CodeableConcept` half.
- **Commits applying this ticket:**
  - [`b33db10cfc75`](https://github.com/HL7/fhir/commit/b33db10cfc759e1be46677f7ee5fe8e76913b7d3) — FHIR-54848 (2026-03-05)
- **Changes applied (per Step 5c, scoped to the datatypes page):** In `source/datatypes/dosage.xml` (the legacy authoring spreadsheet that is the source for `Dosage`), a single cell is changed: the `Dosage.site` "Type" cell goes from `CodeableConcept` to `CodeableReference(BodyStructure)`. Cardinality (`0..1`) and the example binding (`MedicationAdministrationSite`) are unchanged. Snapshot regeneration of `Dosage` is required.

### [FHIR-54014](https://jira.hl7.org/browse/FHIR-54014) — Dosage redesign could be improved by requiring renderedInstruction

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Datatypes touched:** `DosageDetails`
- **Disposition (verbatim):**

  > We will make DosageInstruction.renderedInstructions 1..1. We will remove the text from the definition:
  > ~~To be used when multiple dosage instructions are included to represent complex dosing such as increasing or tapering doses.~~
  > We will add "The renderedInstructions element must always be present to ensure the full dosage intent is communicated in every case."
  >
  > We will change the comment to
  > The content of the renderedInstructions SHALL contain the information found in the structured dosage, and may contain additional information not found in the structured dosage content, if applicable.

- **Disposition summary:** Make `DosageDetails.renderedInstruction` mandatory (cardinality `1..1`) so a human-readable representation of the dose is always present, even where structured-dosing implementations may diverge. Tighten the definition and the SHALL-comment so the rendered text is required to convey the structured dosage's content (and may add to it), rather than merely "not disagree" with it.
- **Commits applying this ticket:**
  - [`efe537aa9a92`](https://github.com/HL7/fhir/commit/efe537aa9a928e9adbd54659c83cd02482cb34e9) — FHIR-54014 (2026-03-05)
- **Changes applied (per Step 5c, scoped to the datatypes page):** In `source/datatypes/dosagedetails.xml`, the `DosageDetails.renderedInstruction` row's cardinality cell is changed from `0..1` to `1..1`. The definition cell drops the old "To be used when multiple dosage instructions…" sentence and adds "The renderedInstructions element must always be present to ensure the full dosage intent is communicated in every case." The SHALL-comment is rewritten from "The content of the renderedInstructions SHALL not be disagree with the dose represented in the dosage structure content. It may contain additional information not found in the dosage content" to "The content of the renderedInstructions SHALL contain the information found in the structured dosage, and may contain additional information not found in the structured dosage content, if applicable." Snapshot regeneration of `DosageDetails` is required. (This is a **breaking change** for downstream resources whose `dosageInstruction` element refers to `DosageDetails`.)

### [FHIR-54451](https://jira.hl7.org/browse/FHIR-54451) — When to use reason vs relatedClinicalInformation

- **Work group:** Pharmacy
- **Resolution:** Not Persuasive with Modification
- **Datatypes touched:** (none — only `source/datatypes/_changelog.txt` was touched within scope; the substantive edits to `structuredefinition-MedicationStatement.xml` are out of scope for this skill)
- **Disposition summary:** Tightens guidance on when to populate `MedicationStatement.reason` vs `MedicationStatement.relatedClinicalInformation`. No change to any datatype.
- **Commits applying this ticket:**
  - [`84c55f6b66ee`](https://github.com/HL7/fhir/commit/84c55f6b66eedb0c7341526f2cbf4a914ec4ed7a) — FHIR-54451 (2026-03-05)
- **Changes applied (per Step 5c, scoped to the datatypes page):** Within `source/datatypes/_changelog.txt`, this ticket was originally listed alongside the Dosage entries. The later commit [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd) ("separate changelogs per resource type") removed the entry from `source/datatypes/_changelog.txt` and re-located it to `source/medicationstatement/_changelog.txt`, so as of HEAD this ticket has **no surviving impact** on the datatypes scope. No bullet is needed in the datatypes ballot note. See `notes-artifact` for `MedicationStatement`.

### [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) — MedicationStatement[.status] codes are incorrect

- **Work group:** Pharmacy
- **Resolution:** Persuasive
- **Datatypes touched:** (none — substantive edits to `codesystem-medication-statement-status.xml` and `codesystem-medicationrequest-status.xml`, both outside `source/datatypes/`)
- **Disposition summary:** Corrects the definition of the `entered-in-error` code in the MedicationStatement and MedicationRequest status code systems.
- **Commits applying this ticket:**
  - [`358c5eb203b3`](https://github.com/HL7/fhir/commit/358c5eb203b35c6326e060566926db8aeda12352) — FHIR-54903 (2026-03-05)
- **Changes applied (per Step 5c, scoped to the datatypes page):** Same pattern as FHIR-54451: only an entry in `source/datatypes/_changelog.txt`, removed and re-homed by [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd). No surviving datatype impact.

### [FHIR-56016](https://jira.hl7.org/browse/FHIR-56016) — Dosage - examples have step.timing, should have step.component.timing

- **Work group:** Pharmacy
- **Resolution:** Persuasive
- **Datatypes touched:** (none — primary edits to `source/dosage-examples.html`; only mentioned in the curated `_changelog.txt`)
- **Disposition summary:** Corrects multiple Dosage examples whose `step.timing` / `step.doseAndRate` elements were placed directly under `step` instead of under `step.component`. Pure example-correction, no datatype change.
- **Commits applying this ticket:** No commit in window touched any in-scope file for this ticket; the curated `_changelog.txt` references it for context.

### [FHIR-54523](https://jira.hl7.org/browse/FHIR-54523) — Textural representation does not match with structural representation

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Datatypes touched:** (none — primary edits to `source/dosage-examples.html`)
- **Disposition summary:** Fixes inconsistencies between the human-readable narrative and structured data in three Dosage examples (Example 1: 10 mg → 2.5 mg `doseQuantity`; Example 2: missing 5 mg `doseAndRate` on the PRN component in JSON, `safety` unit fixed, duplicate `safety` block removed in XML; Example 3: `safety` period 2 → 6 months in JSON and XML).
- **Commits applying this ticket:** No commit in window touched any in-scope file for this ticket.

### (unattributed) — Page-level / publisher-only commits

- [`28a2ce8e42b9`](https://github.com/HL7/fhir/commit/28a2ce8e42b9ae19de4329d680cae82eb9dc8ba7) — "commit excel" / "XML formatting by publisher after applying FHIR-54651". Mechanically reformats `source/datatypes/dosagedetails.xml` (1531 lines touched, no semantic change). Effectively belongs with FHIR-54651.
- [`755c842235cd`](https://github.com/HL7/fhir/commit/755c842235cd0e66cc510c84231349343707fdf6) — "add files to changelog". Editorial: appends `Files:` lines to the existing entries in `source/datatypes/_changelog.txt`.
- [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd) — "separate changelogs per resource type". Splits `source/datatypes/_changelog.txt` so that resource-specific entries (FHIR-54451, FHIR-54903, FHIR-54923) move to `source/medicationrequest/_changelog.txt` and `source/medicationstatement/_changelog.txt`, leaving the datatypes changelog focused on the five Dosage-related tickets.

## Per-Datatype Roll-up (after-applied state)

### `Dosage`

- **Source (`source/datatypes/dosage.xml`):**
  - `Dosage.site`: type changed from `CodeableConcept` to `CodeableReference(BodyStructure)` ([FHIR-54848](https://jira.hl7.org/browse/FHIR-54848)). Cardinality (`0..1`) and the example binding to `MedicationAdministrationSite` are unchanged. Snapshot regeneration required.
- **Examples / Terminology / Diagrams:** None changed within `source/datatypes/`. (Dosage examples were also fixed in this window — see FHIR-56016 / FHIR-54523 — but those edits live in `source/dosage-examples.html`, outside this skill's scope.)

### `DosageDetails`

- **Source (`source/datatypes/dosagedetails.xml`):**
  - `DosageDetails.simple` is removed ([FHIR-54651](https://jira.hl7.org/browse/FHIR-54651)). The element row is renamed to `!DosageDetails.simple` per the publisher's "removed-element" convention.
  - The `complex` invariant (id `1`, `simple.empty() or step.empty()`, "Can only have a simple dose, or one or more steps in a sequence") is replaced by a new invariant `no-safety-on-simple` (id `2`, `step.count() = 1 implies step.safety.empty()`, "If only one step is present, DosageDetails.step.safety shall not be populated") ([FHIR-54651](https://jira.hl7.org/browse/FHIR-54651)).
  - `DosageDetails.renderedInstruction` cardinality changed from `0..1` to `1..1` ([FHIR-54014](https://jira.hl7.org/browse/FHIR-54014)). Definition rewritten to require always-present rendered text; SHALL-comment rewritten so the rendered text must *contain* the structured dosage's content (and may add to it).
  - Mechanical publisher reformat of the spreadsheet ([`28a2ce8e42b9`](https://github.com/HL7/fhir/commit/28a2ce8e42b9ae19de4329d680cae82eb9dc8ba7)) — no semantic effect.
  - Snapshot regeneration required.
- **Examples / Terminology / Diagrams:** None changed within `source/datatypes/`.

### (Page-level / shared)

- **`source/datatypes/_changelog.txt` (new file):** Introduced as a per-folder, human-curated changelog of the Dosage / DosageDetails-related tickets applied in this window (FHIR-54651, FHIR-54848, FHIR-54014, FHIR-56016, FHIR-54523). After the [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd) split, the file at HEAD lists only those five Dosage-related tickets.
- **`source/datatypes.html`:** Not modified in this window; no existing ballot note.

## Page-level Roll-up Summary (after-applied state)

Across `source/datatypes/**` and `source/datatypes.html`, the after-applied state of
`5d67a34a13a5..db79dcdfe196` is:

- Two datatypes — both Dosage-family, both authored as legacy SpreadsheetML —
  received targeted, breaking-or-near-breaking changes:
  1. `Dosage.site` was widened from `CodeableConcept` to
     `CodeableReference(BodyStructure)`.
  2. `DosageDetails.simple` was removed, the redundant `complex` invariant was
     replaced by a focused `no-safety-on-simple` invariant
     (`step.count() = 1 implies step.safety.empty()`), and
     `DosageDetails.renderedInstruction` was promoted to mandatory (`1..1`) with
     tightened definition and SHALL-comment.
- A new per-folder change log (`source/datatypes/_changelog.txt`) was
  introduced and curated; it now lists the five Dosage-related tickets above.
- `source/datatypes.html` itself is unchanged; no ballot note exists there.
- No primitive types, no general-purpose complex types, no shared narrative,
  diagrams, value sets or code systems under `source/datatypes/` were touched
  in the window.

There are no cross-datatype changes (e.g., shared element type renames) in
this window.

## Proposed Ballot Note (HTML)

Insertion site: `source/datatypes.html`, immediately after the `<h1>Datatypes</h1>` /
standards-status `<table class="colsn">` block and before the
"Types Framework Cross Reference" paragraph. No prior `id` to preserve;
allocating `bn1`.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b>
    Since the previous ballot, the only datatype-source changes under
    <code>source/datatypes/</code> are targeted refinements to the
    Dosage-family special-purpose datatypes (<a href="dosage.html#Dosage">Dosage</a>
    and <a href="dosage.html#DosageDetails">DosageDetails</a>); no
    primitive or general-purpose complex datatype was modified. Balloters
    looking at the broader Dosage / Medication reorganisation should also
    review the ballot note on the <a href="dosage.html">Dosage</a> page
    and the <a href="dosage-examples.html">Dosage examples</a>.
  </p>
  <ul>
    <li><b>Dosage:</b> <code>Dosage.site</code> changed from
      <code>CodeableConcept</code> to
      <code>CodeableReference(BodyStructure)</code>, allowing callers to
      reference a <a href="bodystructure.html">BodyStructure</a> for richer
      site descriptions (laterality, location qualifiers) while keeping the
      existing example binding on the coded part
      (<a href="https://jira.hl7.org/browse/FHIR-54848">FHIR-54848</a>).</li>
    <li><b>DosageDetails:</b> the redundant
      <code>DosageDetails.simple</code> element has been removed (a "simple"
      dosage is fully expressible as a single <code>step</code>); the
      <code>dosdet-1</code> "complex" invariant has been replaced by a new
      invariant <code>no-safety-on-simple</code>
      (<code>step.count() = 1 implies step.safety.empty()</code>), so
      whole-course safety on a single-step dosage must be recorded on
      <code>DosageDetails.safety</code> rather than on
      <code>step.safety</code>
      (<a href="https://jira.hl7.org/browse/FHIR-54651">FHIR-54651</a>).</li>
    <li><b>DosageDetails (breaking):</b>
      <code>DosageDetails.renderedInstruction</code> is now mandatory
      (<code>1..1</code>), and its definition and SHALL-comment have been
      tightened so the rendered text must always be present and must
      <em>contain</em> the structured dosage's content (and may add to it),
      rather than merely "not disagree" with it. Resources whose
      <code>dosageInstruction</code> uses <code>DosageDetails</code> (e.g.,
      MedicationRequest, MedicationDispense, MedicationStatement) must
      always populate this element going forward
      (<a href="https://jira.hl7.org/browse/FHIR-54014">FHIR-54014</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **The "real" home of this ballot note is arguably `source/dosage.html`, not
  `source/datatypes.html`.** Both touched datatypes (`Dosage`,
  `DosageDetails`) are special-purpose datatypes that render to their own
  dedicated narrative page (`source/dosage.html`), which already carries an
  active ballot note covering the broader R6 Dosage / DosageDetails
  reorganisation. None of the other datatypes that render into
  `source/datatypes.html` (primitives, general-purpose complex types) were
  touched in this window. The proposed `bn1` above is a faithful "datatypes
  page" framing of the in-scope changes (since the skill always considers
  `source/datatypes.html` and the touched datatype source files live under
  `source/datatypes/`), but reviewers should also run **`notes-page`** on
  `source/dosage.html` to refresh the existing ballot note there with the
  same three bullets — that page is where balloters who care about Dosage
  will land.
- **Out-of-scope companion changes referenced by the in-scope changelog.**
  The new `source/datatypes/_changelog.txt` cites two further Pharmacy
  tickets ([FHIR-56016](https://jira.hl7.org/browse/FHIR-56016) and
  [FHIR-54523](https://jira.hl7.org/browse/FHIR-54523)) whose actual edits
  landed in `source/dosage-examples.html`. They are summarised above for
  context but are not represented in the proposed datatypes ballot note;
  use **`notes-page`** on `source/dosage-examples.html` to surface them.
- **Out-of-scope commits that briefly touched the in-scope changelog.**
  [FHIR-54451](https://jira.hl7.org/browse/FHIR-54451) (MedicationStatement
  guidance on `reason` vs `relatedClinicalInformation`) and
  [FHIR-54903](https://jira.hl7.org/browse/FHIR-54903) (MedicationStatement
  / MedicationRequest `entered-in-error` definitions) had their changelog
  entries added to `source/datatypes/_changelog.txt`, then re-homed into
  the per-resource changelogs by [`cd0ae4e75773`](https://github.com/HL7/fhir/commit/cd0ae4e75773fa9c19e05ad754a6bf7a7d46eedd).
  As of HEAD they leave **no datatype-scope footprint**. Use
  **`notes-artifact`** on `MedicationStatement` and `MedicationRequest`
  for those.
- **Spreadsheet authoring / snapshot regeneration.** Both `dosage.xml` and
  `dosagedetails.xml` are SpreadsheetML files (`<?mso-application
  progid="Excel.Sheet"?>` workbooks) — these *are* the authoritative
  source for these datatypes (no separate `structuredefinition-Dosage.xml`
  exists alongside). All semantic narration above is taken from the
  spreadsheet cells; the corresponding `<snapshot>` regeneration is
  expected to be done by the publisher and is intentionally not enumerated
  here.
- **Briefing staleness.** `cache/github/repos/HL7_fhir/repo-analysis/meta.json`
  records `clone_head_sha = 1b369ff4e28e695908ed97d802bbad1e8ff32874`
  (analyzed 2026-04-20T18:46:14Z). Current clone HEAD is
  `db79dcdfe196d35bd0e74c58c655a4c1c8f534f7`. The briefing is therefore
  slightly behind HEAD but well past the since-commit; no impact on this
  report's findings, but a refresh via the `repo-analysis` skill would be
  appropriate before further note runs.
- **Window integrity.** `5d67a34a13a5` is a strict ancestor of `db79dcdfe196`;
  no symmetric-difference fallback was needed.
- **Service health.** `fhir-augury-cli` was reachable (`services` `status`
  responded); the documented `services health` action is not implemented in
  this build.

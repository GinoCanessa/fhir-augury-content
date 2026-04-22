# Page Ballot Note Draft: dosage (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/dosage.html` |
| Resolution rule | FhirCore convention (`source/<page>.html` + conventional siblings) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 3 (FHIR-54651, FHIR-56016, FHIR-54523) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` (per `meta.json`) |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `dosage` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/dosage.html` | Page source (ballot note lives here) | yes |
| `source/dosage-examples.html` | Examples appendix (sibling page) | yes |
| `source/dosage-definitions.html` | Definitions appendix (sibling page) | no |
| `source/dosage-mappings.html` | Mappings appendix (sibling page) | no |
| `source/dosage-profiles.html` | Profiles appendix (sibling page) | no |

## Current Ballot Note

```html
<blockquote class="ballot-note">
  <p><b>Note to Balloters:</b>
    The way Medication dosage regimes are represented and used has undergone extensive reorganization with breaking changes in R6:
  </p>
  <ul>
    <li>The <code>dosageInstruction</code> element in MedicationRequest, MedicationDispense, and MedicationStatement has changed from multiple <code>Dosage</code> elements (0..*) to a single <code>DosageDetails</code> element (0..1)</li>
    <li>Complex dosing regimes are now represented within DosageDetails using steps and components rather than multiple Dosage instances</li>
    <li>The <code>DosageDetails</code> data type allows combining multiple dosages and replaces the use of <code>.sequence</code>.</li>
    <li>There are changes to the <a href="medicationrequest.html#bnr">Boundaries for MedicationRequest</a></li>
    <li>The <a href="datatypes.html#Timing">Timing</a> datatype has related changes - namely the addition of <code>startOffset</code> and <code>endOffset</code>.</li>
  </ul>
  <p>Balloters should pay careful attention to these structures and the <a href="dosage-examples.html">examples</a>.</p>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54651](https://jira.hl7.org/browse/FHIR-54651) | Dosage — remove "simple" and use step.component | [`accc7b7f11fd`](https://github.com/HL7/fhir/commit/accc7b7f11fd24da385298c692cdd0304cc220ee) |
| [FHIR-56016](https://jira.hl7.org/browse/FHIR-56016) | Dosage — examples have step.timing, should have step.component.timing | [`b5c35f6ea3e7`](https://github.com/HL7/fhir/commit/b5c35f6ea3e799a408023608279ce72ab62b4084), [`a566c33d62e0`](https://github.com/HL7/fhir/commit/a566c33d62e08b7daf02d4fe0f4abdb895693825) |
| [FHIR-54523](https://jira.hl7.org/browse/FHIR-54523) | Textual representation does not match with structural representation (dosage examples) | [`074fad2f3edd`](https://github.com/HL7/fhir/commit/074fad2f3edd694c8c41bc7e8280691b040063c8) |

No unattributed commits.

## Per-Ticket Detail

### [FHIR-54651](https://jira.hl7.org/browse/FHIR-54651) — Dosage — remove "simple" and use step.component

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
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

- **Disposition summary:** Eliminates the redundant `DosageDetails.simple` element on the grounds that a simple dosage is just a one-step dosage course; revises the page narrative to drop the "simple/complex" dichotomy; replaces the `dosdet-1` invariant with a new constraint forbidding `step.safety` when only a single step is present; and updates examples to match.
- **Commits applying this ticket:**
  - [`accc7b7f11fd`](https://github.com/HL7/fhir/commit/accc7b7f11fd24da385298c692cdd0304cc220ee) — `FHIR-54651 Remove DosageDetails.simple, express simple dosages as a single step` (2026-03-05)
- **Changes applied (per Step 5b, scoped to this page):** In `source/dosage.html`, the "Dosage text and structured Data" paragraph is shortened to `Dosages may contain renderedInstruction and/or structured data.` (the parenthetical "(as a `simple` dosage or a complex sequence of `step` elements)" is removed). In the "DosageDetails" container description, the bullet that read *"Either a `simple` dosage, or a complex dosage course with one or more `step` items …"* is rewritten to *"Either a simple dosage expressed as a single `step` or a complex dosage course expressed with one or more `step`s …"*. The same commit also rewrites several examples in `source/dosage-examples.html` to the single-step form (no `simple` element). Structural removal of `DosageDetails.simple` itself and the invariant rework live in `source/datatypes/dosagedetails.xml` (out of scope for this page — see Notes for reviewer).

### [FHIR-56016](https://jira.hl7.org/browse/FHIR-56016) — Dosage — examples have step.timing, should have step.component.timing

- **Work group:** Pharmacy
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. (Description states: "There is an element missing - component (which is the one that contains timing)".)

- **Disposition summary:** The dosage examples placed `timing` and `doseAndRate` directly under `step`, but per the DosageDetails structure these belong under `step.component`. The fix is to re-nest those elements in every affected example so the examples validate against the structure.
- **Commits applying this ticket:**
  - [`b5c35f6ea3e7`](https://github.com/HL7/fhir/commit/b5c35f6ea3e799a408023608279ce72ab62b4084) — `FHIR-56016 Fix dosage examples: put timing/doseandrate under step.component, instead of directly in step` (2026-03-05)
  - [`a566c33d62e0`](https://github.com/HL7/fhir/commit/a566c33d62e08b7daf02d4fe0f4abdb895693825) — `FHIR-56016 updates` (2026-03-06)
- **Changes applied (per Step 5b, scoped to this page):** Throughout `source/dosage-examples.html`, the JSON / XML / YAML snippets are rewritten so that `timing` and `doseAndRate` are nested inside `step.component` rather than appearing as direct children of `step`. This affects every multi-format example block in the page; the "Wrong" form previously visible in the rendered examples no longer appears.

### [FHIR-54523](https://jira.hl7.org/browse/FHIR-54523) — Textual representation does not match with structural representation

- **Work group:** Pharmacy
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Apply the requested fix to Example 1 (doseQuantity 10mg → 2.5mg in JSON and XML). Additionally, correct cross-format mismatches found in other examples:
  > - Example 2 JSON missing 5mg doseAndRate on PRN component, safety unit "s" should be "tablet";
  > - Example 2 XML has duplicate 150mg/week safety block;
  > - Example 3 JSON and XML have safety period of 2 months, should be 6 to match YAML.

- **Disposition summary:** The dosage example narrative said one thing while the JSON/XML structures said another, and several JSON/XML pairs disagreed with each other (and with YAML). The fix corrects Example 1's `doseQuantity` to match the rendered "1 tablet per day" instruction, and reconciles cross-format mismatches in Examples 2 and 3.
- **Commits applying this ticket:**
  - [`074fad2f3edd`](https://github.com/HL7/fhir/commit/074fad2f3edd694c8c41bc7e8280691b040063c8) — `FHIR-54523 Fix dosage example mismatches between text/structure and across formats` (2026-03-05)
- **Changes applied (per Step 5b, scoped to this page):** Numerical and structural corrections to the example payloads in `source/dosage-examples.html`: Example 1's `doseQuantity` is changed from 10 mg to 2.5 mg in JSON and XML; Example 2 JSON gains the missing 5 mg `doseAndRate` on the PRN component and the safety unit `s` is changed to `tablet`; Example 2 XML loses a duplicated 150 mg/week safety block; Example 3 JSON and XML safety `period` is changed from 2 to 6 months so the three formats agree. Because this commit and the FHIR-56016 commits both rewrite large portions of the same example blocks, the per-ticket diff overlaps with FHIR-56016 — the roll-up below is the authoritative description of the after-applied state of the examples page.

## Roll-up Summary (after-applied state)

Based on `git diff 5d67a34a..HEAD -- source/dosage.html source/dosage-examples.html` (5 lines changed in `dosage.html`; 483 lines changed in `dosage-examples.html`):

- **Section: `<h3>Dosage text and structured Data</h3>` (`dosage.html`):** The paragraph describing what a Dosage may contain is simplified to *"Dosages may contain `renderedInstruction` and/or structured data."* The previous parenthetical that called out "simple" dosages versus a "complex sequence of `step` elements" is gone. ([FHIR-54651](https://jira.hl7.org/browse/FHIR-54651))
- **DosageDetails container description (`dosage.html`):** The bullet that previously offered "Either a `simple` dosage, or a complex dosage course with one or more `step` items …" is replaced with "Either a simple dosage expressed as a single `step` or a complex dosage course expressed with one or more `step`s …". The page no longer presents `simple` as a distinct authoring path. ([FHIR-54651](https://jira.hl7.org/browse/FHIR-54651))
- **Examples — structural shape (`dosage-examples.html`):** Every example that previously placed `timing` and `doseAndRate` directly under `step` is rewritten so those elements live under `step.component`, matching the DosageDetails structure. ([FHIR-56016](https://jira.hl7.org/browse/FHIR-56016))
- **Examples — text/structure consistency (`dosage-examples.html`):** Cross-format mismatches are reconciled: Example 1's `doseQuantity` is corrected to 2.5 mg (matching "1 tablet per day"); Example 2 JSON gets the missing 5 mg PRN `doseAndRate` and safety unit `tablet` (was `s`); a duplicate 150 mg/week safety block is removed from Example 2 XML; Example 3's safety `period` is harmonised to 6 months across JSON, XML, and YAML. ([FHIR-54523](https://jira.hl7.org/browse/FHIR-54523))
- **Examples — `simple` element (`dosage-examples.html`):** Examples that previously used `DosageDetails.simple` are re-expressed as a single `step` (no `simple` element appears anywhere on the examples page in the after-applied state). ([FHIR-54651](https://jira.hl7.org/browse/FHIR-54651))
- **Diagrams / images:** None added, removed, or replaced.
- **Cross-page links:** No link targets changed; the existing link to `dosage-examples.html` from the ballot note is unaffected.
- **Editorial cleanup:** None of substance — all changes in the window have a Jira ticket behind them.

## Proposed Ballot Note

The existing ballot note's framing of the R6 reorganisation remains accurate; we keep all five existing bullets and add a new bullet for the in-window removal of `DosageDetails.simple` and the corresponding example cleanups.

```html
<blockquote class="ballot-note">
  <p><b>Note to Balloters:</b>
    The way Medication dosage regimes are represented and used has undergone extensive reorganization with breaking changes in R6:
  </p>
  <ul>
    <li>The <code>dosageInstruction</code> element in MedicationRequest, MedicationDispense, and MedicationStatement has changed from multiple <code>Dosage</code> elements (0..*) to a single <code>DosageDetails</code> element (0..1)</li>
    <li>Complex dosing regimes are now represented within DosageDetails using steps and components rather than multiple Dosage instances</li>
    <li>The <code>DosageDetails</code> data type allows combining multiple dosages and replaces the use of <code>.sequence</code>.</li>
    <li>The <code>DosageDetails.simple</code> element has been removed; a "simple" dosage is now expressed as a single <code>step</code>, and the page narrative no longer distinguishes a separate "simple" authoring path (<a href="https://jira.hl7.org/browse/FHIR-54651">FHIR-54651</a>)</li>
    <li>There are changes to the <a href="medicationrequest.html#bnr">Boundaries for MedicationRequest</a></li>
    <li>The <a href="datatypes.html#Timing">Timing</a> datatype has related changes - namely the addition of <code>startOffset</code> and <code>endOffset</code>.</li>
  </ul>
  <p>The <a href="dosage-examples.html">examples</a> have been substantially revised in this ballot cycle: <code>timing</code> and <code>doseAndRate</code> are now nested under <code>step.component</code> rather than directly under <code>step</code> (<a href="https://jira.hl7.org/browse/FHIR-56016">FHIR-56016</a>), several cross-format mismatches between the rendered text and the JSON/XML/YAML structures have been corrected (<a href="https://jira.hl7.org/browse/FHIR-54523">FHIR-54523</a>), and examples that previously used <code>DosageDetails.simple</code> are now expressed as a single <code>step</code> (<a href="https://jira.hl7.org/browse/FHIR-54651">FHIR-54651</a>). Balloters should pay careful attention to these structures and the examples.</p>
</blockquote>
```

## Notes for Reviewer

- Commit [`accc7b7f11fd`](https://github.com/HL7/fhir/commit/accc7b7f11fd24da385298c692cdd0304cc220ee) (FHIR-54651) also touches `source/datatypes/dosagedetails.xml` and `source/datatypes/_changelog.txt`. Those are part of the consolidated datatypes page and belong to **`notes-datatype`** (not this page). The structural removal of `DosageDetails.simple`, the deletion of the `dosdet-1` invariant, and the new "if only one step is present, `step.safety` shall not be populated" constraint should be summarised there; this page note covers only the narrative-prose and example-page consequences of that ticket.
- The existing ballot note's substance is fully preserved — no bullet has been reverted in the window. The new bullet for `DosageDetails.simple` is additive.
- The disposition text for FHIR-56016 was not separately recorded as an applied-vote comment in Jira; the ticket description was used to characterise the change and is shown verbatim above.
- HEAD is a descendant of the supplied since-commit (no symmetric-difference fallback was needed).
- The briefing's `meta.json` records `clone_head_sha = 1b369ff4e28e…` while the cache clone HEAD is currently `db79dcdfe196…`; the briefing is therefore slightly behind the clone but the FhirCore page-resolution convention (`source/<page>.html` plus `<page>-*.html` siblings) is stable and was applied directly. No briefing refresh was required for this run.
- `gh` was not needed; all commits and content were resolved from the cached clone.

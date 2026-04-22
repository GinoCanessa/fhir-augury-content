# Artifact Ballot Note Draft: MedicinalProductDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `MedicinalProductDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 2 (FHIR-53861, FHIR-53866) — plus 1 unattributed follow-up commit |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (no explicit Artifact Map entry for `MedicinalProductDefinition`; resolved via repo-convention patterns under `source/medicinalproductdefinition/`) |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `MedicinalProductDefinition` for this run (resolved by `source/medicinalproductdefinition/` convention; the briefing's Artifact Map has no explicit entry for this artifact, so the standard FhirCore patterns documented in the skill were applied):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/medicinalproductdefinition/structuredefinition-MedicinalProductDefinition.xml` | StructureDefinition (canonical) | no |
| `source/medicinalproductdefinition/medicinalproductdefinition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/medicinalproductdefinition/medicinalproductdefinition-notes.xml` | Supplementary narrative | no |
| `source/medicinalproductdefinition/bundle-MedicinalProductDefinition-search-params.xml` | Search parameters | no |
| `source/medicinalproductdefinition/list-MedicinalProductDefinition-operations.xml` | Operations list | no |
| `source/medicinalproductdefinition/operationdefinition-MedicinalProductDefinition-everything.xml` | OperationDefinition (`$everything`) | no |
| `source/medicinalproductdefinition/list-MedicinalProductDefinition-examples.xml` | Examples list | yes |
| `source/medicinalproductdefinition/list-MedicinalProductDefinition-packs.xml` | Packs list | no |
| `source/medicinalproductdefinition/medicinalproductdefinition-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | no |
| `source/medicinalproductdefinition/medicinalproductdefinition-*example*.xml`, `…-acetaminophen-*`, `…-with-contained-*` | Example instances (10 files) | no |
| `source/medicinalproductdefinition/valueset-*.xml` | Artifact-scoped ValueSets (15) | no |
| `source/medicinalproductdefinition/codesystem-*.xml` | Artifact-scoped CodeSystems (12); `codesystem-medicinal-product-type.xml` modified | yes (1 of 12) |

Patterns / files that produced no match:

- `source/medicinalproductdefinition/medicinalproductdefinition-spreadsheet.xml` — no legacy spreadsheet present (SD is authoritative; no spreadsheet to flag).

## Current Ballot Note

The ballot note as it exists at HEAD in `medicinalproductdefinition-introduction.xml` (introduced inside the window by commit [`0afc2d57`](https://github.com/HL7/fhir/commit/0afc2d577474a04f6672b05aa96e40e820932fe9)):

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since the last R6 ballot are:</p>
<ul>
    <li>Updates to the following elements:</li>
        <ul>
            <li>The definitions of the two values of MedicinalProductDefinition.type were improved</li>
        </ul>
</ul>
</blockquote>
```

There was no ballot note in the intro file at the since-commit (`5d67a34a13a5`).

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53861](https://jira.hl7.org/browse/FHIR-53861) | Update definitions for MedicinalProduct and InvestigationalProduct | [`b44c5c3d414b`](https://github.com/HL7/fhir/commit/b44c5c3d414bf339afb0c45d2da65fc5990ef692), [`0afc2d577474`](https://github.com/HL7/fhir/commit/0afc2d577474a04f6672b05aa96e40e820932fe9) |
| [FHIR-53866](https://jira.hl7.org/browse/FHIR-53866) | Update misspelling of "Acetaminophin" to "Acetaminophen" | [`cdb85a4d979e`](https://github.com/HL7/fhir/commit/cdb85a4d979e25bcc7dd98727b197a73364e46ed) |
| (unattributed) | Word-choice cleanup of definition text added by FHIR-53861 ("may or may not" → "might or might not") | [`ce7e999cc205`](https://github.com/HL7/fhir/commit/ce7e999cc205017fa795f29faf94ed79646403c8) |

## Per-Ticket Detail

### [FHIR-53861](https://jira.hl7.org/browse/FHIR-53861) — Update definitions for MedicinalProduct and InvestigationalProduct

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Changes definitions as suggested

  *(Disposition text taken from the ticket's `resolution_description` snapshot — the issue has no separate applied-vote comment recorded in Jira.)*

- **Disposition summary:** Replace the placeholder one-line definitions of the two `medicinal-product-type` concepts (`MedicinalProduct`, `InvestigationalProduct`) with full regulatory-style definitions that describe what each concept covers and the regulatory status it implies (authorised/marketed for commercial use vs. under evaluation in a clinical trial).
- **Commits applying this ticket:**
  - [`b44c5c3d414b`](https://github.com/HL7/fhir/commit/b44c5c3d414bf339afb0c45d2da65fc5990ef692) — *FHIR-53861: Update definitions for MedicinalProduct and InvestigationalProduct* (2026-04-16T17:16:17+01:00)
  - [`0afc2d577474`](https://github.com/HL7/fhir/commit/0afc2d577474a04f6672b05aa96e40e820932fe9) — *updated resource intro ballot comments for FHIR-53861* (2026-04-16T20:22:44+01:00)
- **Changes applied (per Step 5b, scoped to this artifact):** Commit `b44c5c3d` rewrote the two `<concept>/<definition>` strings in `codesystem-medicinal-product-type.xml`: `MedicinalProduct` moved from "A standard medicinal product." to the WHO-style definition ("Any substance or combination of substances that may be administered to human beings (or animals) for treating or preventing disease, … Its regulatory status is authorized/marketed for commercial use."), and `InvestigationalProduct` moved from "An investigational medicinal product." to "A medicinal product which is being tested or used as a reference, including as a placebo, in a clinical trial. Its regulatory status is under evaluation in a clinical trial; may or may not have marketing authorization." Commit `0afc2d57` then added a new `<blockquote class="ballot-note" id="bn1">` to `medicinalproductdefinition-introduction.xml` calling out the change for balloters. The StructureDefinition itself was not modified — only the bound CodeSystem's concept definitions and the intro narrative.

### [FHIR-53866](https://jira.hl7.org/browse/FHIR-53866) — Update misspelling of "Acetaminophin" to "Acetaminophen"

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > fix the typo

  *(From the ticket's `resolution_description` snapshot; no separate applied-vote comment in Jira.)*

- **Disposition summary:** Correct the misspelling of the analgesic in the example list — the example titled "Acetaminophin product, pack and tablet (using contained resources)" should read "Acetaminophen". The ticket's scope is purely the example title text; the underlying example file ids are not in scope.
- **Commits applying this ticket:**
  - [`cdb85a4d979e`](https://github.com/HL7/fhir/commit/cdb85a4d979e25bcc7dd98727b197a73364e46ed) — *FHIR-53866 changed spelling of Acetaminophin to Acetaminophen (and Acetaminopen fixed also)* (2026-04-16T16:32:58+01:00)
- **Changes applied (per Step 5b, scoped to this artifact):** Commit `cdb85a4d` updated two strings inside one entry of `list-MedicinalProductDefinition-examples.xml` for the `Acetamin-500-20-generic` example: the build-extension `description` was corrected from "Acetaminophin product, pack and tablet (using contained resources)" to "Acetaminophen product, pack and tablet (using contained resources)", and the entry's `<item>/<display>` was corrected from "Acetaminopen 500mg box of 20 tablets" to "Acetaminophen 500mg box of 20 tablets". The fix therefore covers both reported misspellings ("Acetaminophin" *and* the secondary "Acetaminopen" typo). The example resource files themselves and the `MedicinalProductDefinition.id`s they use were not renamed in the window — only the human-readable list entry text.

### (unattributed)

- **Commits with no ticket key in the message and no cross-reference hits:**
  - [`ce7e999cc205`](https://github.com/HL7/fhir/commit/ce7e999cc205017fa795f29faf94ed79646403c8) — *changed may or may not to might or might not to get around prohibition* (2026-04-16T20:28:40+01:00)
- **Changes applied:** Re-edits the `InvestigationalProduct` definition that FHIR-53861 had just inserted into `codesystem-medicinal-product-type.xml`, replacing "may or may not have marketing authorization" with "might or might not have marketing authorization." This is a stylistic follow-up to FHIR-53861's text (the commit author and date confirm it landed minutes after the ballot-note commit) and is folded into the after-applied wording captured in the roll-up. No Jira ticket was cited in the commit message and no cross-reference is recorded for the SHA.

## Roll-up Summary (after-applied state)

Authoritative summary of what changed across the artifact between [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd) and [`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7), grouped by file role:

- **StructureDefinition (`structuredefinition-MedicinalProductDefinition.xml`):** No changes. No element additions / removals, no cardinality / type / binding edits, no constraint edits. Snapshot regeneration is **not** required from changes in this window. (Snapshot may still be regenerated as part of a global build, but no SD authoring change drives it here.)
- **Intro / narrative (`medicinalproductdefinition-introduction.xml`):** A new `<blockquote class="ballot-note" id="bn1">` was inserted at the top of "Scope and Usage", framing the resource as "ready for Normative status" and flagging the `MedicinalProductDefinition.type` definition update for balloter attention. The body narrative of the intro (scope, boundaries, contained resources, etc.) was not modified. `medicinalproductdefinition-notes.xml` was not touched.
- **Search parameters (`bundle-MedicinalProductDefinition-search-params.xml`):** No changes — no parameters added, removed, or retyped.
- **Operations (`list-MedicinalProductDefinition-operations.xml`, `operationdefinition-MedicinalProductDefinition-everything.xml`):** No changes — `$everything` is unchanged and the operations list is unchanged.
- **Examples:** No example resource files were added or removed; no example payload was modified. Only the human-readable text in `list-MedicinalProductDefinition-examples.xml` was touched (FHIR-53866): the description and display strings for the `Acetamin-500-20-generic` entry were corrected from "Acetaminophin"/"Acetaminopen" to "Acetaminophen". The underlying example ids (`MedicinalProductDefinition/Acetamin-500-20-generic`, file `medicinalproductdefinition-acetaminophen-500mg-tablets-box-of-20.xml`) were not renamed.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** One CodeSystem changed — `codesystem-medicinal-product-type.xml` (FHIR-53861, refined by `ce7e999c`). The `MedicinalProduct` concept definition expanded from a one-line stub to a full WHO-style definition that asserts an "authorized/marketed for commercial use" regulatory status. The `InvestigationalProduct` concept definition expanded from a one-line stub to a clinical-trial definition ending "… its regulatory status is under evaluation in a clinical trial; might or might not have marketing authorization." (post-`ce7e999c` wording). The codes themselves (`MedicinalProduct`, `InvestigationalProduct`) and their displays are unchanged. The bound `valueset-medicinal-product-type.xml` is unchanged. No ValueSets or other CodeSystems in the artifact folder were modified. These two definitions are FHIR-Core canonicals authored by Biomedical Research & Regulation — they are not UTG-managed, so no UTG cross-repo touch is required.

## Proposed Ballot Note (HTML)

The existing bullet ("The definitions of the two values of MedicinalProductDefinition.type were improved") is retained as accurate, but rewritten to be specific about which definitions changed and to cite the underlying ticket. The example-typo fix (FHIR-53866) is added because it is balloter-visible in the published examples list. Mark-up indentation is normalised so the inner `<ul>` is a proper sibling list rather than a nested list under a parent `<li>` (the existing draft has an `<ul>` directly under another `<ul>` without an enclosing `<li>`, which most renderers will collapse). The existing `id="bn1"` is preserved.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since the last R6 ballot are:</p>
  <ul>
    <li>The definitions of the two concepts in the <code>MedicinalProductDefinition.type</code> CodeSystem (<code>medicinal-product-type</code>) have been replaced with full regulatory-style definitions: <code>MedicinalProduct</code> now describes any substance or combination of substances administered to humans (or animals) for treating or preventing disease, etc., with regulatory status "authorized/marketed for commercial use", and <code>InvestigationalProduct</code> now describes a medicinal product being tested or used as a reference (including as a placebo) in a clinical trial, whose regulatory status is "under evaluation in a clinical trial; might or might not have marketing authorization" (<a href="https://jira.hl7.org/browse/FHIR-53861">FHIR-53861</a>).</li>
    <li>Spelling correction in the published examples list: the "Acetaminophin product, pack and tablet (using contained resources)" entry has been corrected to "Acetaminophen" (and the secondary "Acetaminopen" typo in the same entry's display text was also fixed) (<a href="https://jira.hl7.org/browse/FHIR-53866">FHIR-53866</a>).</li>
  </ul>
  <p>The StructureDefinition, search parameters, operations (including <code>$everything</code>), and example payloads themselves are unchanged since the previous ballot.</p>
</blockquote>
```

## Notes for Reviewer

- **Existing ballot-note bullet retained.** The only bullet in the prior draft ("definitions of the two values of MedicinalProductDefinition.type were improved") is still accurate after-applied — it has been kept and made specific by naming the concepts and quoting the new regulatory-status language. No bullets were dropped due to revert/supersession.
- **Word-choice follow-up commit (`ce7e999c`).** Although this commit has no Jira key, it is a stylistic refinement of the text introduced by FHIR-53861 (replacing "may or may not" with "might or might not" in the `InvestigationalProduct` definition) and is captured by the FHIR-53861 bullet of the proposed ballot note, not as a separate bullet.
- **Disposition text source.** Neither FHIR-53861 nor FHIR-53866 has a separately recorded applied-vote comment in Jira; the verbatim disposition strings above are taken from each ticket's `resolution_description` snapshot. If the work group recorded a richer applied-vote write-up elsewhere, this note should be re-checked against that source before publication.
- **Cross-referenced index empty for window.** `fhir-augury-cli cross-referenced` returned zero hits for all four commit SHAs in the window; ticket attribution above is based solely on `(FHIR|UTG)-\d+` keys parsed from commit subjects/bodies.
- **Briefing Artifact Map gap.** The repo briefing under `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` does not enumerate `MedicinalProductDefinition` in its Artifact Map, so file resolution fell back to the FhirCore pattern set documented in this skill against `source/medicinalproductdefinition/`. Worth fixing in the next `repo-analysis` run.
- **Out-of-artifact touches.** No commits in the window touched files outside `source/medicinalproductdefinition/`, so there is no spillover into other artifacts to call out.
- **Window orientation.** HEAD (`db79dcdfe196`) is a descendant of the since-commit (`5d67a34a13a5`); the standard `since..HEAD` range was used. No symmetric-difference fallback was needed and `gh api` was not invoked — all data resolved against the cached clone.

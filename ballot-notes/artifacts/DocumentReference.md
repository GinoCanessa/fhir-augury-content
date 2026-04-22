# Artifact Ballot Note Draft: DocumentReference (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `DocumentReference` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 12 |
| Tickets attributed | 8 (5 named in commit messages; 3 additional named in the release-notes block added in this window) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T20:00:00Z |

## Source Files

Files considered part of `DocumentReference` for this run (folder `source/documentreference/` per the FhirCore Artifact Map):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/documentreference/structuredefinition-DocumentReference.xml` | StructureDefinition (canonical) | yes |
| `source/documentreference/documentreference-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/documentreference/documentreference-notes.xml` | Supplementary narrative | yes |
| `source/documentreference/bundle-DocumentReference-search-params.xml` | Search parameters bundle | yes |
| `source/documentreference/list-DocumentReference-operations.xml` | Operations list | no |
| `source/documentreference/list-DocumentReference-examples.xml` | Examples list | no |
| `source/documentreference/list-DocumentReference-packs.xml` | Packs list | no |
| `source/documentreference/operationdefinition-DocumentReference-docref.xml` | OperationDefinition `$docref` | no |
| `source/documentreference/operationdefinition-DocumentReference-generate.xml` | OperationDefinition `$generate` | no |
| `source/documentreference/implementationguide-DocumentReference-core.xml` | IG manifest | no |
| `source/documentreference/codesystem-document-reference-status.xml` | Artifact-scoped CodeSystem | no |
| `source/documentreference/codesystem-document-relationship-type.xml` | Artifact-scoped CodeSystem | no |
| `source/documentreference/valueset-c80-facilitycodes.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/valueset-clinical-speciality.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/valueset-doc-typecodes.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/valueset-document-related-artifact-type.xml` | Artifact-scoped ValueSet (NEW in window) | yes |
| `source/documentreference/valueset-document-relationship-type.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/valueset-referenced-item-category.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/valueset-xds-facilitycodes.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/valueset-xds-practice-codes.xml` | Artifact-scoped ValueSet | no |
| `source/documentreference/documentreference-event-mapping-exceptions.xml` | Mapping-exceptions vs. Event pattern | yes |
| `source/documentreference/documentreference-fivews-mapping-exceptions.xml` | Mapping-exceptions vs. FiveWs pattern | yes |
| `source/documentreference/documentreference-example*.xml` | Examples (28 files) | no |
| `source/documentreference/documentreference-examples-header.xml` | Examples header | no |
| `source/documentreference/xds-example.xml`, `source/documentreference/xds-notes.xml` | XDS profile narrative/example | no |

Patterns from the briefing that produced no match in the clone: none — the folder follows the standard FhirCore layout and every documented pattern resolved to at least one file.

The legacy `documentreference-spreadsheet.xml` does not exist in the folder; the StructureDefinition is authoritative for this resource (per the FhirCore briefing's spreadsheet-vs-SD gotcha).

## Current Ballot Note

A `ballot-note` block (`bn1`) is present at HEAD; a sibling `stu-note` "Release Notes" block was *added in this window* by commit [`a5af3a9ef639`](https://github.com/HL7/fhir/commit/a5af3a9ef639065214eb0d306d0e9adf27144afc) and is the closest thing to an in-progress balloter-facing change log. Both blocks are reproduced verbatim:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
<ul>
    <li>Addition of the following elements:</li>
        <ul>
            <li>DocumentReference.related</li>
        </ul>
    <li>Updates to the following elements:</li>
        <ul>
            <li>DocumentReference.bodySite has been changed to DocumentReference.bodyStructure</li>
        </ul>
</ul>
</blockquote>
<blockquote class="stu-note" style="background-color: lightblue">
    <p><b>Release Notes (pending alternative process review with FMG):</b></p>
    <ul>
      <li>DocumentReference.docStatus -&gt; modifier should be false. - <a href="https://jira.hl7.org/browse/FHIR-54537">FHIR-54537</a></li>
      <li>DocumentReference.basedOn points to requests not events - <a href="https://jira.hl7.org/browse/FHIR-54536">FHIR-54536</a></li>
      <li>DocumentReference.related changed to backbone with target and code, relatesTo clarified, with search adjustments - <a href="https://jira.hl7.org/browse/FHIR-53824">FHIR-53824</a>, <a href="https://jira.hl7.org/browse/FHIR-53550">FHIR-53550</a></li>
      <li>DocumentReference.context definition clarified - <a href="https://jira.hl7.org/browse/FHIR-54170">FHIR-54170</a></li>
      <li>DocumentReference.basedOn definition clarified - <a href="https://jira.hl7.org/browse/FHIR-54167">FHIR-54167</a></li>
      <li>DocumentReference.custodian definition clarified - <a href="https://jira.hl7.org/browse/FHIR-54169">FHIR-54169</a></li>
      <li><a href="https://jira.hl7.org/browse/FHIR-54618">FHIR-54618</a></li>
    </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53824](https://jira.hl7.org/browse/FHIR-53824) | Problems with DocumentReference related/relatesTo | [`3800384a0c47`](https://github.com/HL7/fhir/commit/3800384a0c47165145ee8b96d9eb58e1cfd238c4), [`798e52f2ef4b`](https://github.com/HL7/fhir/commit/798e52f2ef4b1dd1f75d79550c4851ae7c5ad30d), [`cca94fde6b3f`](https://github.com/HL7/fhir/commit/cca94fde6b3f56952f3411755b7182f9716d6607), [`092a94f8214c`](https://github.com/HL7/fhir/commit/092a94f8214cab0b0db22d1532d1b88136a75daa), [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2), [`bceb01eb6054`](https://github.com/HL7/fhir/commit/bceb01eb60543d614f1543bf1affae216bed9666), [`54d91d57eaf6`](https://github.com/HL7/fhir/commit/54d91d57eaf68b69ebceea2e2e04f9e1a781972e), [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef) |
| [FHIR-53550](https://jira.hl7.org/browse/FHIR-53550) | DocumentReference.related shouldn't exist | [`3800384a0c47`](https://github.com/HL7/fhir/commit/3800384a0c47165145ee8b96d9eb58e1cfd238c4) (folded into FHIR-53824 work) |
| [FHIR-54536](https://jira.hl7.org/browse/FHIR-54536) | DocumentReference.basedOn points to requests not events | [`34b17c93932e`](https://github.com/HL7/fhir/commit/34b17c93932e3ad1ecac6b6aaf81f1bf6d68cfa4), [`ef3d9470353b`](https://github.com/HL7/fhir/commit/ef3d9470353bcd68b5c9ccce47a4db9b36652855), [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) |
| [FHIR-54537](https://jira.hl7.org/browse/FHIR-54537) | DocumentReference.docStatus -> modifier should be false | [`132ce0038210`](https://github.com/HL7/fhir/commit/132ce0038210768d4fbd45ba401dd94ef70a9c37) |
| [FHIR-54167](https://jira.hl7.org/browse/FHIR-54167) | basedOn Description Mismatch | [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2), [`ef3d9470353b`](https://github.com/HL7/fhir/commit/ef3d9470353bcd68b5c9ccce47a4db9b36652855), [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef) (overlap with FHIR-54536) |
| [FHIR-54169](https://jira.hl7.org/browse/FHIR-54169) | custodian Description vs. Element Definition Mismatch | [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef) |
| [FHIR-54170](https://jira.hl7.org/browse/FHIR-54170) | context Now Allows Appointment - Description needs to be aligned | [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef), [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) |
| [FHIR-54618](https://jira.hl7.org/browse/FHIR-54618) | basedOn Lists DocumentReference Twice | release-notes reference only — see "Notes for Reviewer" |
| (unattributed) | "added headers" — adds the `stu-note` Release Notes block | [`a5af3a9ef639`](https://github.com/HL7/fhir/commit/a5af3a9ef639065214eb0d306d0e9adf27144afc) |

`fhir-augury-cli cross-referenced` returned no hits for any of the 12 commit SHAs, so attribution comes entirely from commit message text plus the new release-notes block added in this window. Only FHIR-53824, FHIR-53550, FHIR-54536, FHIR-54537, and FHIR-56179 are named in commit messages; FHIR-54167 / 54169 / 54170 / 54618 are inferred from the release-notes block plus the matching SD edits. FHIR-56179 is not included above because it concerns `BiologicallyDerivedProduct.collection.sourceOrganization` (no DocumentReference files were touched on its behalf — see "Notes for Reviewer").

## Per-Ticket Detail

### [FHIR-53824](https://jira.hl7.org/browse/FHIR-53824) — Problems with DocumentReference related/relatesTo

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We propose these changes:
  >
  > **relatesTo** — Definition: "Relationships that this document reference has with other document references that already exist." Short Display: "Relationships to other document references and their lifecycle changes". Cardinality 0..*. Summary: true. Comment: "This element is labeled as a modifier because documents that append to other documents are incomplete on their own."
  >
  > Add this text to a bullet after the first bullet in Implementation Notes 10.2.5: "relatesTo is dedicated to document reference lifecycle changes. It is only to be used in covering document reference lifecycle changes such as revisions of a document reference from one to next, a transform of a document reference to another form, amendments attached to a document reference, and signatures of a document reference."
  >
  > **related** — restructured into a backbone with `target 1..1 Reference(Any)` and `code 0..1 CodeableConcept` (example binding to a new `AssociatedReferenceType` value set drawn from `relatedArtifactType` with the codes `documentation`, `justification`, `citation`, `part-of`).
  >
  > Applied-vote follow-up (per [JIRAUSER19407]): "The concepts in the disposition are part of the existing code system that the disposition is asking to be used (relatedArtifactType). The only deviation from the disposition is using the existing valueset pointing at that code system rather than creating a new-net value set." This deviation was subsequently corrected in commit `092a94f8214c` by adding a dedicated value set with only the four requested concepts.

- **Disposition summary:** Split the previously-overlapping `related` and `relatesTo` semantics. `related` becomes a backbone (target + typed code) for non-lifecycle pointers. `relatesTo` is restricted in narrative to document-lifecycle relationships (replace, transform, append, signed). A bound value set restricted to the four lifecycle-relevant codes is added for `related.code`.
- **Commits applying this ticket:**
  - [`3800384a0c47`](https://github.com/HL7/fhir/commit/3800384a0c47165145ee8b96d9eb58e1cfd238c4) — FHIR-53824, FHIR-53550 — DocumentReference.related/relatesTo clarified for purpose of each (2026-03-27)
  - [`798e52f2ef4b`](https://github.com/HL7/fhir/commit/798e52f2ef4b1dd1f75d79550c4851ae7c5ad30d) — fixes (search-param path + event-mapping fixes follow-on, 2026-03-27)
  - [`cca94fde6b3f`](https://github.com/HL7/fhir/commit/cca94fde6b3f56952f3411755b7182f9716d6607) — fixes (2026-03-27)
  - [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef) — Additional docRef changes based on moehrke-docRef-202603 (2026-03-30)
  - [`bceb01eb6054`](https://github.com/HL7/fhir/commit/bceb01eb60543d614f1543bf1affae216bed9666) — Updating intro notes (2026-04-02)
  - [`54d91d57eaf6`](https://github.com/HL7/fhir/commit/54d91d57eaf68b69ebceea2e2e04f9e1a781972e) — clarify change to related and relatesTo (2026-04-01)
  - [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) — Adjustments to FHIR-53824 and FHIR-56179 (2026-04-07)
  - [`092a94f8214c`](https://github.com/HL7/fhir/commit/092a94f8214cab0b0db22d1532d1b88136a75daa) — Adding valueset showing only the concepts requested in the ticket (2026-04-09)
- **Changes applied (per Step 5b, scoped to this artifact):** `DocumentReference.related` is converted from a flat `Reference(Resource)` 0..* into a backbone with two child elements: `target 1..1 Reference(Resource)` (carrying the actual reference) and `code 0..1 CodeableConcept` (example-bound to the new `AssociatedReferenceType` value set). The element's short / definition / comment are rewritten to scope it to "non-lifecycle" relationships and `isSummary` is set to false. `DocumentReference.relatesTo` keeps its existing structure but its short and definition are rewritten ("Relationships to other document references and their lifecycle changes" / "Relationships that this document reference has with other document references that already exist") and the modifier-rationale comment is removed (the comment line `"This element is labeled as a modifier because documents that append to other documents are incomplete on their own"` is dropped). The intro adds a release-notes bullet for this change and `documentreference-notes.xml` gains two implementation-note bullets explaining the `relatesTo` (lifecycle) vs. `related` (non-lifecycle) split. The `related` SearchParameter expression / path is updated from `DocumentReference.related` to `DocumentReference.related.target` to keep it pointing at the reference. A new `valueset-document-related-artifact-type.xml` is added defining `AssociatedReferenceType` as a four-code subset of `http://hl7.org/fhir/related-artifact-type` (`documentation`, `justification`, `citation`, `part-of`).

### [FHIR-54536](https://jira.hl7.org/browse/FHIR-54536) — DocumentReference.basedOn points to requests not events

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will make the following changes to the definitions for basedOn:
  >
  > Definition: "An activity that is fulfilled in whole or in part by the creation of this media."
  > Short Display: "Activity that caused this media to be created"

- **Disposition summary:** Replace the procedure-specific wording on `basedOn` with broader "activity"-based wording so the element correctly admits the request resource targets it already lists.
- **Commits applying this ticket:**
  - [`34b17c93932e`](https://github.com/HL7/fhir/commit/34b17c93932e3ad1ecac6b6aaf81f1bf6d68cfa4) — FHIR-54536 - DocumentReference.basedOn points to requests not events (2026-03-27)
  - [`ef3d9470353b`](https://github.com/HL7/fhir/commit/ef3d9470353bcd68b5c9ccce47a4db9b36652855) — Change media to document (2026-04-02)
  - [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) — Adjustments to FHIR-53824 and FHIR-56179 (2026-04-07)
- **Changes applied (per Step 5b, scoped to this artifact):** `DocumentReference.basedOn` short and definition are rewritten — the after-applied state reads short = "Activity that caused this document to be created" and definition = "An activity that is fulfilled in whole or in part by the creation of this document." The corresponding `documentreference-event-mapping-exceptions.xml` `shortUnmatched` / `definitionUnmatched` reasons for `Event.basedOn` are updated in lockstep so the pattern-divergence record stays consistent with the new wording. (Note: the disposition wording from FMG ended at "this media"; the after-applied state goes one step further to "this document" via FHIR-54167, which is the right roll-up.)

### [FHIR-54167](https://jira.hl7.org/browse/FHIR-54167) — basedOn Description Mismatch

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > We will make the following changes:
  >
  > The description for basedOn should say "A request or response that is fulfilled..." not "A procedure that is fulfilled..."
  >
  > Also, the description mentions "this media" which should be changed to "this document" for consistency.

- **Disposition summary:** Fix two narrative bugs on `basedOn` — the obsolete "procedure" subject and the "this media" carry-over from the Media resource pattern.
- **Commits applying this ticket:**
  - [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) — Adjustments to FHIR-53824 and FHIR-56179 (2026-04-07) — supplies the "Activity / document" wording
  - [`ef3d9470353b`](https://github.com/HL7/fhir/commit/ef3d9470353bcd68b5c9ccce47a4db9b36652855) — Change media to document (2026-04-02)
- **Changes applied (per Step 5b, scoped to this artifact):** Together with FHIR-54536, the `basedOn` short / definition end up as "Activity that caused this document to be created" / "An activity that is fulfilled in whole or in part by the creation of this document." The "media" → "document" sweep also propagates into the event-mapping exception's `shortUnmatched` / `definitionUnmatched` resource-side strings. Note the overlap with FHIR-54536: per the roll-up, only one set of `basedOn` definition/short edits exists in the after-applied state and it satisfies both tickets simultaneously.

### [FHIR-54170](https://jira.hl7.org/browse/FHIR-54170) — context Now Allows Appointment — Description needs to be aligned

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > We will update the description to read "The encounter or other triggering event during which this DocumentReference was created..."

- **Disposition summary:** Bring the `context` definition in line with the now-broadened `Reference(Appointment | Encounter | EpisodeOfCare)` target list.
- **Commits applying this ticket:**
  - [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef) — Additional docRef changes based on moehrke-docRef-202603 (2026-03-30)
  - [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) — Adjustments to FHIR-53824 and FHIR-56179 (2026-04-07)
- **Changes applied (per Step 5b, scoped to this artifact):** `DocumentReference.context` definition is updated to "The encounter or other triggering event during which this DocumentReference was created or to which the creation of this record is tightly associated." A matching `divergentElement` for `Event.encounter` → `DocumentReference.context` is added to `documentreference-event-mapping-exceptions.xml` to record the broader resource-side wording vs. the Event pattern.

### [FHIR-54169](https://jira.hl7.org/browse/FHIR-54169) — custodian Description vs. Element Definition Mismatch

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > We will remove "or group" from the description of custodian.

- **Disposition summary:** Drop the dangling "or group" phrase that no longer matches the `Reference(Organization)`-only target.
- **Commits applying this ticket:**
  - [`2acd897d0cbd`](https://github.com/HL7/fhir/commit/2acd897d0cbd53e6b3c1f60fe14895aa1af630ef) — Additional docRef changes based on moehrke-docRef-202603 (2026-03-30)
- **Changes applied (per Step 5b, scoped to this artifact):** `DocumentReference.custodian` definition becomes "Identifies the organization who is responsible for ongoing maintenance of and access to the document." (the words "or group" are deleted).

### [FHIR-54537](https://jira.hl7.org/browse/FHIR-54537) — DocumentReference.docStatus -> modifier should be false

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > We will change docStatus to not be a modifier and remove the reason to be a modifier.

- **Disposition summary:** Demote `docStatus` from modifier status — `entered-in-error` lives on `status`, not `docStatus`, so flagging the latter as a modifier was misleading.
- **Commits applying this ticket:**
  - [`132ce0038210`](https://github.com/HL7/fhir/commit/132ce0038210768d4fbd45ba401dd94ef70a9c37) — FHIR-54537 - DocumentReference.docStatus -> modifier should be false (2026-03-27)
- **Changes applied (per Step 5b, scoped to this artifact):** `DocumentReference.docStatus` loses its `<isModifier value="true"/>` and `<isModifierReason …/>` lines outright. A matching `divergentElement` is added to `documentreference-fivews-mapping-exceptions.xml` to record that `FiveWs.status` is a modifier in the pattern but `DocumentReference.docStatus` is not (`<modifier _pattern="true" _resource="false" reason="Unknown"/>`). The reason text on the new mapping-exception entry is currently "Unknown" and is worth a follow-up tightening.

### [FHIR-53550](https://jira.hl7.org/browse/FHIR-53550) — DocumentReference.related shouldn't exist

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > The disposition and vote for [FHIR-53824](https://jira.hl7.org/browse/FHIR-53824) fulfill this request by introducing a backbone with a CodeableConcept to describe the target reference.

- **Disposition summary:** Closed by reference to FHIR-53824 — no independent edits.
- **Commits applying this ticket:**
  - [`3800384a0c47`](https://github.com/HL7/fhir/commit/3800384a0c47165145ee8b96d9eb58e1cfd238c4) — co-named on the FHIR-53824 commit (2026-03-27)
- **Changes applied (per Step 5b, scoped to this artifact):** No edits independent of FHIR-53824 — the `related` backbone restructure that landed for FHIR-53824 is what addresses this ticket. See FHIR-53824 above for the authoritative description.

### [FHIR-54618](https://jira.hl7.org/browse/FHIR-54618) — basedOn Lists DocumentReference Twice

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will fix.

- **Disposition summary:** Remove the duplicate `DocumentReference` entry from the `basedOn` `targetProfile` list.
- **Commits applying this ticket:**
  - None in window — only referenced in the new release-notes block added by [`a5af3a9ef639`](https://github.com/HL7/fhir/commit/a5af3a9ef639065214eb0d306d0e9adf27144afc).
- **Changes applied (per Step 5b, scoped to this artifact):** No `targetProfile` change to `DocumentReference.basedOn` is visible in the `since-commit..HEAD` diff. The fix may have landed before `5d67a34a13a5` (the since-commit), or be still pending. See "Notes for Reviewer" — the release-notes block lists this ticket but the after-applied diff does not corroborate it within the window.

### (unattributed) — "added headers"

- **Commits:**
  - [`a5af3a9ef639`](https://github.com/HL7/fhir/commit/a5af3a9ef639065214eb0d306d0e9adf27144afc) — added headers (2026-03-31)
- **Changes applied:** Inserts the `<blockquote class="stu-note" …>Release Notes (pending alternative process review with FMG)…</blockquote>` block into `documentreference-introduction.xml`. The bullets in that block reference FHIR-54537, FHIR-54536, FHIR-53824, FHIR-53550, FHIR-54170, FHIR-54167, FHIR-54169, and FHIR-54618 — the commit itself doesn't apply any SD or terminology change.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a13a5..db79dcdfe196 -- source/documentreference/**`. Seven files changed; 127 insertions, 20 deletions.

- **StructureDefinition (`structuredefinition-DocumentReference.xml`):**
  - `DocumentReference.basedOn` — short / definition rewritten from procedure-specific media wording to "Activity that caused this document to be created" / "An activity that is fulfilled in whole or in part by the creation of this document." (FHIR-54536, FHIR-54167)
  - `DocumentReference.docStatus` — `isModifier` and `isModifierReason` removed; element is no longer a modifier. (FHIR-54537)
  - `DocumentReference.context` — definition expanded to "The encounter or other triggering event during which this DocumentReference was created…" to cover the broader `Reference(Appointment | Encounter | EpisodeOfCare)` target list. (FHIR-54170)
  - `DocumentReference.related` — restructured from a flat `Reference(Resource)` 0..* into a backbone; new children `related.target 1..1 Reference(Resource)` and `related.code 0..1 CodeableConcept` (example-bound to `http://hl7.org/fhir/ValueSet/document-related-artifact-type`); element narrative scoped to non-lifecycle relationships; `isSummary` set to false; a `uml-dir=right` rendering hint added. (FHIR-53824, FHIR-53550)
  - `DocumentReference.custodian` — definition trimmed: "or group" removed. (FHIR-54169)
  - `DocumentReference.relatesTo` — short / definition rewritten ("Relationships to other document references and their lifecycle changes" / "Relationships that this document reference has with other document references that already exist"); the modifier-rationale `<comment>` line is removed (the element retains its existing isModifier setting, however — the only edit is to the comment + short/definition). (FHIR-53824)
  - Snapshot regeneration is required for the resource — `<snapshot>` edits are intentionally not narrated above per the skill's "treat snapshot as derived" rule.
- **Intro / narrative (`documentreference-introduction.xml`, `documentreference-notes.xml`):**
  - A new `stu-note` "Release Notes (pending alternative process review with FMG)" block is added to the intro, listing eight tickets with Jira links. (FHIR-54537, FHIR-54536, FHIR-53824, FHIR-53550, FHIR-54170, FHIR-54167, FHIR-54169, FHIR-54618)
  - Two new implementation-notes bullets are added in `documentreference-notes.xml` distinguishing `relatesTo` (document-lifecycle revisions / transforms / amendments / signatures) from `related` (everything else, but not duplicating `subject`/`context`). (FHIR-53824)
  - The existing `ballot-note` (`bn1`) is **unchanged** in this window.
- **Search parameters (`bundle-DocumentReference-search-params.xml`):**
  - The `related` SearchParameter's `path` and `expression` are updated from `DocumentReference.related` to `DocumentReference.related.target` to track the new backbone. No new or removed search parameters. (FHIR-53824)
- **Operations (`list-DocumentReference-operations.xml`):**
  - No changes; `$docref` and `$generate` OperationDefinition files are untouched.
- **Examples:**
  - No example files changed in window. The new `related.target`/`related.code` shape is therefore *not* yet exercised by an example — worth a follow-up.
- **Mapping exceptions:**
  - `documentreference-event-mapping-exceptions.xml` — `Event.basedOn` `shortUnmatched` / `definitionUnmatched` resource-side strings updated to track the new "activity / this document" wording; a new `definitionUnmatched` for `Event.encounter` → `DocumentReference.context` is added to record the broader resource-side definition.
  - `documentreference-fivews-mapping-exceptions.xml` — new `divergentElement` for `FiveWs.status` → `DocumentReference.docStatus` recording `modifier _pattern="true" _resource="false" reason="Unknown"` (consequence of FHIR-54537).
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - **New file** `valueset-document-related-artifact-type.xml` — `AssociatedReferenceType` value set, version 6.0.0, `experimental=true`, includes four codes from `http://hl7.org/fhir/related-artifact-type`: `documentation`, `justification`, `citation`, `part-of`. WG = `oo`, status = `informative`, FMM 1. Used as the example binding for the new `DocumentReference.related.code`. (FHIR-53824)
  - No other valueset / codesystem changes.
  - The new value set composes against an HL7-published code system (`related-artifact-type`); per the FhirCore briefing's UTG cross-repo gotcha, this value set itself lives in the FHIR core repo and is fine here, but reviewers should confirm the four selected codes are also present upstream in HL7/UTG's `related-artifact-type` (no UTG change required for this ballot).

## Proposed Ballot Note (HTML)

The existing `bn1` is preserved (the R5→R6 elements it calls out are still accurate in the after-applied state) and a new `bn2` is added to summarise the work that landed since `5d67a34a13a5`. The release-notes `stu-note` should be retained for the FMG alternative-process review but the substance of its bullets is now also captured in `bn2` for balloters who will not see the `stu-note` styling.

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
<ul>
    <li>Addition of the following elements:</li>
        <ul>
            <li>DocumentReference.related</li>
        </ul>
    <li>Updates to the following elements:</li>
        <ul>
            <li>DocumentReference.bodySite has been changed to DocumentReference.bodyStructure</li>
        </ul>
</ul>
</blockquote>
<blockquote class="ballot-note" id="bn2">
<p><b>Note to Balloters (changes since the previous ballot):</b> The following substantive changes have been applied to <code>DocumentReference</code> in response to ballot reconciliation. Reviewers should pay particular attention to the restructuring of <code>related</code> and the modifier change on <code>docStatus</code>, both of which have implementation impact.</p>
<ul>
    <li><code>DocumentReference.related</code> has been restructured from a flat <code>Reference(Resource)</code> into a backbone with <code>target&nbsp;1..1&nbsp;Reference(Resource)</code> and <code>code&nbsp;0..1&nbsp;CodeableConcept</code> (example-bound to a new <code>AssociatedReferenceType</code> value set drawn from <code>related-artifact-type</code>: <code>documentation</code>, <code>justification</code>, <code>citation</code>, <code>part-of</code>). The <code>related</code> SearchParameter expression is updated to <code>DocumentReference.related.target</code> accordingly. The narrative now explicitly scopes <code>related</code> to non-lifecycle relationships and reserves <code>relatesTo</code> for document-lifecycle changes (revisions, transforms, amendments, signatures). (<a href="https://jira.hl7.org/browse/FHIR-53824">FHIR-53824</a>, <a href="https://jira.hl7.org/browse/FHIR-53550">FHIR-53550</a>)</li>
    <li><code>DocumentReference.docStatus</code> is no longer a modifier element. The <code>isModifier</code> flag and its rationale have been removed, since <code>entered-in-error</code> handling lives on <code>status</code>. (<a href="https://jira.hl7.org/browse/FHIR-54537">FHIR-54537</a>)</li>
    <li><code>DocumentReference.basedOn</code> definition / short have been rewritten from procedure-specific media wording to "Activity that caused this document to be created" / "An activity that is fulfilled in whole or in part by the creation of this document," matching the fact that <code>basedOn</code> targets request resources rather than events. (<a href="https://jira.hl7.org/browse/FHIR-54536">FHIR-54536</a>, <a href="https://jira.hl7.org/browse/FHIR-54167">FHIR-54167</a>)</li>
    <li><code>DocumentReference.context</code> definition has been broadened to "The encounter or other triggering event during which this DocumentReference was created…" to align with the now-permitted <code>Reference(Appointment | Encounter | EpisodeOfCare)</code> targets. (<a href="https://jira.hl7.org/browse/FHIR-54170">FHIR-54170</a>)</li>
    <li><code>DocumentReference.custodian</code> definition has been corrected — "or group" removed — to match its <code>Reference(Organization)</code> target. (<a href="https://jira.hl7.org/browse/FHIR-54169">FHIR-54169</a>)</li>
    <li><code>DocumentReference.relatesTo</code> short / definition have been rewritten to explicitly call out document-lifecycle relationships, and the modifier-rationale comment has been removed in favour of the narrative split with <code>related</code>. (<a href="https://jira.hl7.org/browse/FHIR-53824">FHIR-53824</a>)</li>
</ul>
<p>Implementation Notes have been extended with two new bullets distinguishing the intended scope of <code>relatesTo</code> versus <code>related</code>; the corresponding pattern-mapping exception files (Event, FiveWs) have been updated to keep mapping divergence records consistent. Snapshot regeneration is required.</p>
</blockquote>
```

## Notes for Reviewer

- **Existing `bn1` retained as-is.** Both bullets in `bn1` (addition of `related`, rename `bodySite`→`bodyStructure`) describe R5→R6 changes that are still true at HEAD; nothing in the window contradicts them, so no edit is needed. The new `related` backbone restructuring is balloter-relevant in its own right and is captured in `bn2`.
- **`stu-note` Release Notes block.** A non-`ballot-note` `stu-note` block was added to the intro in this window (commit [`a5af3a9ef639`](https://github.com/HL7/fhir/commit/a5af3a9ef639065214eb0d306d0e9adf27144afc)) and is marked "pending alternative process review with FMG." The proposed `bn2` above mirrors and supersedes that content for balloter consumption; the WG should decide whether the `stu-note` should remain alongside `bn2` (useful for FMG review) or be removed before publishing the ballot.
- **FHIR-54618 ("basedOn Lists DocumentReference Twice") has no corroborating diff in the window.** It appears in the new release-notes block but the `targetProfile` list on `DocumentReference.basedOn` is unchanged in `since-commit..HEAD`. The fix likely landed prior to `5d67a34a13a5` (so the release-notes mention is retrospective) or is still outstanding. The proposed `bn2` therefore does not list FHIR-54618; reviewers should confirm before signing off.
- **FHIR-56179 is out of scope for DocumentReference.** Commit [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2)'s subject names FHIR-56179, but that ticket is "BDP should support searching by collection.sourceOrganization" (BiologicallyDerivedProduct). The commit's edits to `source/documentreference/**` are all FHIR-53824 / FHIR-54167 follow-ups; the BDP work for FHIR-56179 lives in `source/biologicallyderivedproduct/**` (out of scope for this report).
- **Lower-case `<extraTypes _resource="Reference(Appointment,EpisodeOfCare)" reason="More broad"/>` on the `Event.encounter` mapping divergence is unchanged**, but a sibling `definitionUnmatched` entry was added — flag if the Event-pattern mapping reviewers want both to be revisited together.
- **`<modifier ... reason="Unknown"/>`** on the new FiveWs divergence (FHIR-54537 fall-out) carries a placeholder reason. Recommend filling that in with a one-line justification (e.g., "DocumentReference.docStatus does not invalidate the resource").
- **No example currently exercises `DocumentReference.related.target` / `related.code`.** None of the 28 example files in the folder were updated in this window. Reviewers may want at least one example showing the new shape before publishing, to flush out tooling issues.
- **`fhir-augury-cli cross-referenced` returned zero hits for every commit SHA** in the window. All ticket attribution is therefore from commit-message text and the in-narrative release-notes block; no additional cross-references were available to widen attribution.
- **HEAD (`db79dcdfe196`) is a descendant of since-commit (`5d67a34a13a5`)** — `git merge-base --is-ancestor` returned 0, so the linear `since-commit..HEAD` window is authoritative; no symmetric-difference fallback was needed.
- **Briefing freshness.** The repo-analysis briefing was generated against clone HEAD `1b369ff4e28e`; the current clone HEAD is `db79dcdfe196`. Folder layout for `source/documentreference/` did not change in that delta, so the Artifact Map remains valid for this run, but a refresh would be appropriate before bulk roll-ups.

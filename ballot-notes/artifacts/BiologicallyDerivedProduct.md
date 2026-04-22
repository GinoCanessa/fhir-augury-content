# Artifact Ballot Note Draft: BiologicallyDerivedProduct (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `BiologicallyDerivedProduct` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 3 (BDP-relevant); 1 commit unattributed |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T16:49:07Z |

> **Note on briefing freshness.** The briefing `meta.json` records the briefing was taken at clone HEAD `1b369ff4e28e`, while the cached clone HEAD at run time is `db79dcdfe196`. The artifact-map patterns for FhirCore resources (folder `source/<name>/`) are stable, so this report uses them; no artifact-level layout changes have landed for BDP between the two HEADs.

## Source Files

Files considered part of `BiologicallyDerivedProduct` for this run (per the FhirCore artifact-map patterns under `source/biologicallyderivedproduct/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/biologicallyderivedproduct/structuredefinition-BiologicallyDerivedProduct.xml` | Canonical StructureDefinition | yes |
| `source/biologicallyderivedproduct/biologicallyderivedproduct-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/biologicallyderivedproduct/biologicallyderivedproduct-notes.xml` | Supplementary narrative | no |
| `source/biologicallyderivedproduct/BiologicallyDerivedProduct-release-notes.xml` | Release-notes fragment | no |
| `source/biologicallyderivedproduct/biologicallyderivedproduct-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/biologicallyderivedproduct/bundle-BiologicallyDerivedProduct-search-params.xml` | Search parameters bundle | yes |
| `source/biologicallyderivedproduct/list-BiologicallyDerivedProduct-operations.xml` | Operations list | no |
| `source/biologicallyderivedproduct/list-BiologicallyDerivedProduct-examples.xml` | Examples list | no |
| `source/biologicallyderivedproduct/list-BiologicallyDerivedProduct-packs.xml` | Packs list | no |
| `source/biologicallyderivedproduct/biologicallyderivedproduct-examples-header.xml` | Examples-page header narrative | yes |
| `source/biologicallyderivedproduct/biologicallyderivedproduct-example*.xml` | Example instances (7 files) | no |
| `source/biologicallyderivedproduct/structuredefinition-profile-medicalproductofhumanorigin.xml` | Sibling profile (MPHO) | no |
| `source/biologicallyderivedproduct/profile-mphobiologicallyderivedproduct-introduction.xml` | MPHO profile narrative | no |
| `source/biologicallyderivedproduct/biologicallyderivedproduct-mphobiologicallyderivedproduct-profile-notes.xml` | MPHO profile notes | no |
| `source/biologicallyderivedproduct/implementationguide-BiologicallyDerivedProduct-core.xml` | IG manifest | no |
| `source/biologicallyderivedproduct/valueset-*.xml` | Artifact-scoped ValueSets (4) | no |
| `source/biologicallyderivedproduct/codesystem-*.xml` | Artifact-scoped CodeSystems (4) | no |
| `source/biologicallyderivedproduct/biologicallyderivedproduct.svg` | Class diagram | no |

Patterns from the briefing that produced no match in the clone:

- `source/biologicallyderivedproduct/biologicallyderivedproduct-spreadsheet.xml` — no legacy spreadsheet present (SD is authoritative, consistent with FhirCore briefing guidance).

## Current Ballot Note

Existing `bn1` block from `biologicallyderivedproduct-introduction.xml` at HEAD (`db79dcdfe196`):

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
<ul>
    <li>Change to the .collection backbone with respect to the collection source.  This includes updates to the corresponding search parameters.</li>
    <li>Addition of a Notes section: <a href="biologicallyderivedproduct.html#8.25.5">biologicallyderivedproduct.html#8.25.5</a> to include information on how to handle information about the intended recipient.</li>

    <li>The following artifacts have been moved to the [OO Incubator IG|<a href="https://build.fhir.org/ig/HL7/oo-incubator">https://build.fhir.org/ig/HL7/oo-incubator</a>]</li>
    <ul>
        <li>The Medical Product of Human Origin (MPHO) Profile is still under development.</li>
        <li>The BiologicallyDerivedProductDispense resource.  Additional work needs to be done on dispensing and administering biologically derived products.</li>

    </ul>
</ul>
</blockquote>
```

Additionally, the intro now carries a separate (non-ballot-note) `stu-note` "Release Notes (pending alternative process review with FMG)" block listing FHIR-54999 and FHIR-56179 — added in this window. It is shown for context only; this skill does not modify it.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54999](https://jira.hl7.org/browse/FHIR-54999) | BiologicallyDerivedProduct should have a grouping identifier or equivalent for hierarchical instances | [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) |
| [FHIR-56179](https://jira.hl7.org/browse/FHIR-56179) | BDP should support searching by collection.sourceOrganization | [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) |
| [FHIR-55001](https://jira.hl7.org/browse/FHIR-55001) | Typo on BDP Example page | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| (unattributed) | Whitespace cleanup in SD | [`0320420219 38`](https://github.com/HL7/fhir/commit/03204202193826dd8624758078bd3831bd4d51c3) |

The remaining ticket keys mentioned in the bulk commits (FHIR-53824 in `27bd95`; FHIR-55272, FHIR-55257, FHIR-53677 in `b62975`; FHIR-55444, FHIR-55372, FHIR-55271, FHIR-55270, FHIR-54041, FHIR-54037, FHIR-54034 in `f22405`) target other Orders & Observations resources (DocumentReference, ObservationDefinition, DeviceDefinition, Device, Observation, ServiceRequest) and did not touch any file under `source/biologicallyderivedproduct/`. They are not listed against this artifact.

## Per-Ticket Detail

### [FHIR-54999](https://jira.hl7.org/browse/FHIR-54999) — BiologicallyDerivedProduct should have a grouping identifier or equivalent for hierarchical instances

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The accepted resolution is captured by the ticket description and the linked PR (HL7/fhir#4029): introduce an element on `BiologicallyDerivedProduct` to carry a grouping identifier (e.g., ISBT 128 Chain of Identity) that links multiple BDP instances administered as part of the same therapy, and add a corresponding search parameter.

- **Disposition summary:** The current model only carried a per-instance product identifier and a donation-event identifier (`biologicalSourceEvent`), with no way to express that several distinct BDPs belong to the same patient therapy across multiple collections and manufacturing steps. The ticket asks for a dedicated repeating identifier element to carry such grouping identifiers (e.g., ISBT 128 CoI) and an accompanying search parameter so that all products participating in one therapy can be retrieved together.
- **Commits applying this ticket:**
  - [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) — More OO tickets (2026-03-11)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-BiologicallyDerivedProduct.xml`, a new repeating element `BiologicallyDerivedProduct.therapyIdentifier` (`Identifier`, `0..*`, `isSummary=false`) was added immediately after `biologicalSourceEvent`, with the short "Identifiers common to a given therapy" and an ISBT128Code mapping ("Chain of Identity Identifier. Required for some ISBT 128 labeled products"). In `bundle-BiologicallyDerivedProduct-search-params.xml`, a matching `token` SearchParameter `BiologicallyDerivedProduct-therapy-identifier` (`code=therapy-identifier`, expression `BiologicallyDerivedProduct.therapyIdentifier`, `status=active`, `standards-status=normative`) was inserted. The intro's release-notes block also gained an `FHIR-54999` entry in the same commit. Snapshot regeneration is required to surface the new element in the published SD snapshot.

### [FHIR-56179](https://jira.hl7.org/browse/FHIR-56179) — BDP should support searching by collection.sourceOrganization

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The accepted resolution is captured by the ticket description and the linked PR (HL7/fhir#4046): add a `reference` search parameter targeting `BiologicallyDerivedProduct.collection.sourceOrganization`, named `organization` (kept aligned with the existing `patient` parameter naming for `sourcePatient` rather than the originally proposed `source-organization`).

- **Disposition summary:** Implementers had no way to retrieve products by the organization that facilitated the collection. The ticket adds a reference search parameter exposing `collection.sourceOrganization`. After workgroup discussion captured on the ticket, the parameter was named `organization` (mirroring the existing `patient` parameter for `sourcePatient`) instead of the originally proposed `source-organization`.
- **Commits applying this ticket:**
  - [`27bd95ec53c3`](https://github.com/HL7/fhir/commit/27bd95ec53c3ba23fcbd3acd1ad2b1443b206be2) — Adjustments to FHIR-53824 and FHIR-56179 (2026-04-07)
- **Changes applied (per Step 5b, scoped to this artifact):** In `bundle-BiologicallyDerivedProduct-search-params.xml`, a new `reference` SearchParameter `BiologicallyDerivedProduct-collection-sourceOrganization` (`code=organization`, expression `BiologicallyDerivedProduct.collection.sourceOrganization`, description "The organization that facilitated the collection of the product", `status=active`, `standards-status=normative`) was appended at the end of the bundle. The intro's release-notes block gained a corresponding `FHIR-56179` entry. No StructureDefinition change was needed — `collection.sourceOrganization` already exists on the resource. (FHIR-53824 also appears in this commit's subject; that ticket targets DocumentReference and did not modify any BDP file.)

### [FHIR-55001](https://jira.hl7.org/browse/FHIR-55001) — Typo on BDP Example page

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The accepted resolution is the wording change in the ticket: replace "biologicall-derived" with "biologically-derived" in the BDP Examples narrative (PR HL7/fhir#4006).

- **Disposition summary:** Pure technical correction — restore the missing "y" in "biologically-derived" in the introductory sentence of the BDP examples list.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
- **Changes applied (per Step 5b, scoped to this artifact):** Single-line wording fix in `biologicallyderivedproduct-examples-header.xml`: "The following are examples of biologicall-derived product resource uses" → "biologically-derived". No structural change.

### (unattributed) — Whitespace cleanup

- **Commits:**
  - [`03204202 1938`](https://github.com/HL7/fhir/commit/03204202193826dd8624758078bd3831bd4d51c3) — Remove excess whitespace (2026-03-11)
- **Changes applied (per Step 5b, scoped to this artifact):** A single-character whitespace adjustment in `structuredefinition-BiologicallyDerivedProduct.xml` (1 line modified). No semantic change to elements, types, cardinalities, bindings, mappings, or constraints. Excluded from the proposed ballot note.

## Roll-up Summary (after-applied state)

Authoritative summary derived from `git diff 5d67a34a13a5..db79dcdfe196 -- source/biologicallyderivedproduct/` (4 files, 63 insertions, 1 deletion):

- **StructureDefinition (`structuredefinition-BiologicallyDerivedProduct.xml`):**
  - Added a new repeating element **`BiologicallyDerivedProduct.therapyIdentifier`** (`Identifier`, `0..*`, `isSummary=false`) positioned immediately after `biologicalSourceEvent`, with short "Identifiers common to a given therapy" and an ISBT128Code mapping for the Chain of Identity identifier. ([FHIR-54999](https://jira.hl7.org/browse/FHIR-54999))
  - Trivial whitespace adjustment elsewhere in the differential; no other element-level changes (no cardinality, type, binding, constraint, or invariant edits).
  - **Snapshot regeneration is required** so published renderings expose `therapyIdentifier`.

- **Intro / narrative (`biologicallyderivedproduct-introduction.xml`):**
  - Added a separate `stu-note` "Release Notes (pending alternative process review with FMG)" block listing the two BDP changes in this window (FHIR-54999, FHIR-56179). The existing `bn1` ballot-note block (the "Note to Balloters" framing the change set since R5) and the existing `stu-note` pointer to the module page are unchanged. No other narrative — Scope and Usage, Boundaries and Relationships — was modified.
  - `biologicallyderivedproduct-notes.xml` and `BiologicallyDerivedProduct-release-notes.xml` were not touched.

- **Search parameters (`bundle-BiologicallyDerivedProduct-search-params.xml`):**
  - **Added** `BiologicallyDerivedProduct-therapy-identifier` — `token`, `code=therapy-identifier`, expression `BiologicallyDerivedProduct.therapyIdentifier`, `standards-status=normative`. ([FHIR-54999](https://jira.hl7.org/browse/FHIR-54999))
  - **Added** `BiologicallyDerivedProduct-collection-sourceOrganization` — `reference`, `code=organization`, expression `BiologicallyDerivedProduct.collection.sourceOrganization`, `standards-status=normative`. ([FHIR-56179](https://jira.hl7.org/browse/FHIR-56179))
  - No existing parameters were renamed, retyped, or removed.

- **Operations (`list-BiologicallyDerivedProduct-operations.xml`):** No changes.

- **Examples:** No example instances were added, removed, or updated. The examples-header narrative had a single typo correction ("biologicall-derived" → "biologically-derived") via [FHIR-55001](https://jira.hl7.org/browse/FHIR-55001); not balloter-relevant beyond noting the spelling fix and intentionally omitted from the proposed ballot note.

- **Terminology (sibling `valueset-*` / `codesystem-*`):** None of the four artifact-scoped ValueSets or four CodeSystems (status, product-category, product codes, property-type codes) were modified in this window. No new terminology was introduced; the new search parameters reuse existing typing.

- **Cross-cutting / sibling profile / IG manifest / MPHO profile:** No changes to `structuredefinition-profile-medicalproductofhumanorigin.xml`, the MPHO profile narrative, or `implementationguide-BiologicallyDerivedProduct-core.xml`.

## Proposed Ballot Note (HTML)

Drop-in replacement for the existing `bn1` block in `biologicallyderivedproduct-introduction.xml`. Existing R5→R6 framing bullets are retained verbatim because the underlying changes (collection backbone reshape, Notes section, OO-Incubator artifact moves) are still present in the after-applied state; the new bullets cover what was added in this window.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
  <ul>
    <li>Change to the <code>.collection</code> backbone with respect to the collection source. This includes updates to the corresponding search parameters.</li>
    <li>Addition of a Notes section (<a href="biologicallyderivedproduct.html#8.25.5">biologicallyderivedproduct.html#8.25.5</a>) describing how to handle information about the intended recipient.</li>
    <li>The following artifacts have been moved to the <a href="https://build.fhir.org/ig/HL7/oo-incubator">OO Incubator IG</a>:
      <ul>
        <li>The Medical Product of Human Origin (MPHO) Profile (still under development).</li>
        <li>The <code>BiologicallyDerivedProductDispense</code> resource (additional work is needed on dispensing and administering biologically derived products).</li>
      </ul>
    </li>
    <li>Added a new repeating <code>BiologicallyDerivedProduct.therapyIdentifier</code> element (<code>Identifier 0..*</code>) for grouping identifiers — such as the ISBT 128 Chain of Identity — that tie together multiple BDP instances participating in the same patient therapy across collections and manufacturing steps. A matching <code>therapy-identifier</code> token search parameter is included (<a href="https://jira.hl7.org/browse/FHIR-54999">FHIR-54999</a>).</li>
    <li>Added a new <code>organization</code> reference search parameter on <code>BiologicallyDerivedProduct.collection.sourceOrganization</code>, enabling retrieval of products by the organization that facilitated the collection (<a href="https://jira.hl7.org/browse/FHIR-56179">FHIR-56179</a>).</li>
  </ul>
  <p>Balloters are asked to review whether the new <code>therapyIdentifier</code> element is sufficient to model grouping for cell &amp; gene therapies (vs. the alternative of relaxing the existing <code>identifier</code> definition), and whether the search-parameter naming (<code>therapy-identifier</code>, <code>organization</code>) is appropriate.</p>
</blockquote>
```

## Notes for Reviewer

- The intro file already contains a separate `stu-note` "Release Notes (pending alternative process review with FMG)" block listing FHIR-54999 and FHIR-56179. That block is part of an FMG-led release-note experiment and is **not** the ballot note; it is left untouched. If FMG decides the experimental block is the system of record for per-ticket call-outs, the per-ticket bullets in the proposed ballot note above can be trimmed back to the framing paragraph.
- No bullets were dropped from the existing ballot note — every R5→R6 bullet is still substantively true at HEAD.
- Commit `27bd95ec53c3` mentions FHIR-53824 in its subject, but FHIR-53824 ("Problems with DocumentReference related/relatesTo") affects DocumentReference, not BDP. Its BDP-touching co-changes in that commit are entirely attributable to FHIR-56179.
- Commit `b62975d9ed5b` ("More OO tickets") and `f22405098ca5` ("First pass at some R6 ballot tickets") are bulk OO commits that span many resources. Only the BDP-scoped portions are attributed here; the other ticket keys in those commit bodies pertain to ObservationDefinition, DeviceDefinition, Device, Observation, ServiceRequest, etc.
- Commit `03204202 1938` is a whitespace-only edit in the SD with no semantic effect; it is shown for completeness but excluded from the proposed ballot note.
- The cross-reference index returned no hits for any of the four commit SHAs. Ticket attribution above is based on the explicit `FHIR-XXXXX` keys present in the commit subjects/bodies, intersected with the per-commit file scope.
- HEAD is a fast-forward descendant of the supplied since-commit; no symmetric-difference fallback was needed. `gh` was not invoked — all data came from `fhir-augury-cli` and the cached clone via `git`.

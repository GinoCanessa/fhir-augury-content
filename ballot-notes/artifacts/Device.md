# Artifact Ballot Note Draft: Device (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Device` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 5 (Device-applicable; commits also referenced 13 other keys that touched non-Device files only) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `Device` for this run (folder `source/device/` in the cached clone).

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/device/structuredefinition-Device.xml` | StructureDefinition (canonical) | yes |
| `source/device/device-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/device/device-notes.xml` | Supplementary narrative | yes |
| `source/device/device-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | yes |
| `source/device/device-participant-mapping-exceptions.xml` | Participant mapping exceptions | no |
| `source/device/bundle-Device-search-params.xml` | Search parameters bundle | no |
| `source/device/list-Device-operations.xml` | Operations list | no |
| `source/device/list-Device-examples.xml` | Examples list | no |
| `source/device/list-Device-packs.xml` | Packs list | no |
| `source/device/implementationguide-Device-core.xml` | Device-core IG manifest | no |
| `source/device/codesystem-device-category.xml` | Artifact-scoped CodeSystem | yes |
| `source/device/codesystem-device-*.xml` (10 others) | Artifact-scoped CodeSystems | no |
| `source/device/codesystem-udi-entry-type.xml` | Artifact-scoped CodeSystem | no |
| `source/device/valueset-device-*.xml` (16 files) | Artifact-scoped ValueSets | no |
| `source/device/valueset-udi-entry-type.xml` | Artifact-scoped ValueSet | no |
| `source/device/device-example*.xml` (24 examples) | Examples | no |
| `source/device/device-examples-header.xml` | Examples header | no |
| `source/device/device.svg` | Diagram asset | no |

No `<name>-spreadsheet.xml` is present (Device has fully migrated to SD authoring); no patterns produced unexpected misses.

## Current Ballot Note

The intro file at HEAD contains one `class="ballot-note"` blockquote (`bn1`) plus a sibling, transient "Release Notes" blockquote (styled `background-color: lightblue`) that the work group is using to track tickets pending the FMG alternative-process review. The transient block is **not** a ballot note and should not survive into the ballot package.

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the Device resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<p>For an overview of this resource and others in the Device domain, also see the <a href="device-module.html">Device Module</a> page.</p>
<p>The Device scope and usage has been revised.  A majority of content has been moved DeviceDefinition to describe the types of devices in scope.</p>
<p>The following element was added:</p>
<ul>
<li>Device.additive as a backbone.</li>
</ul>
<p>The following elements have been revised:</p>
<ul>
<li>Updated Device.definition datatype to canonical(DeviceDefinition).</li>
<li>Updated Device.version to Device.deviceVersion.</li>
</ul>
<p>The following elements have been removed from Device:</p>
<ul>
<li>Device.displayName as it was duplicated in Device.name backbone.</li>
<li>Device.owner has been removed and was moved to DeviceAssociation.relationship of the subject. Please comment on the revision if there are issues with removing the identification of individuals in the Device resource.</li>
<li>Device.mode, Device.cycle, Device.duration, Device.gateway, Device.endpoint have been removed and the following extensions were added: device-mode, device-cycle, device-duration, device-gateway, and device-endpoint.</li>
</ul>
<p>The following extensions were added:</p>
<ul>
<li>device-alertDetection to describe the alert detection activation states for the overall device.</li>
<li>device-conformsTo-source – represents the source of the device specification.</li>
</ul>
</blockquote>
```

Sibling (transient) block at HEAD, for reviewer context only:

```html
<blockquote style="background-color: lightblue">
        <p><b>Release Notes (pending alternative process review with FMG):</b></p>
        <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55372">FHIR-55372</a></li>
                <li><a href="https://jira.hl7.org/browse/FHIR-52979">FHIR-52979</a></li>
                <li><a href="https://jira.hl7.org/browse/FHIR-52946">FHIR-52946</a></li>
                <li><a href="https://jira.hl7.org/browse/FHIR-56060">FHIR-56060</a></li>
                <li><a href="https://jira.hl7.org/browse/FHIR-54323">FHIR-54323</a></li>
        </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55372](https://jira.hl7.org/browse/FHIR-55372) | Device.name.display should not be a modifier | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661), [`d68b0d377bc6`](https://github.com/HL7/fhir/commit/d68b0d377bc61943bb98962a0aeb03e7a7cef74b) |
| [FHIR-52979](https://jira.hl7.org/browse/FHIR-52979) | Applying extension to FHIR R4 and earlier versions creates purpose overlap with Device.specialization element | [`f6c9d64997bc`](https://github.com/HL7/fhir/commit/f6c9d64997bc67a7c97a90dbbfe165f10561e64e) |
| [FHIR-56060](https://jira.hl7.org/browse/FHIR-56060) | Minor cleanup to value set display names | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658), [`6c40b35c33c5`](https://github.com/HL7/fhir/commit/6c40b35c33c5fb2bed980f376d6f05dc24a072f9) |
| [FHIR-54323](https://jira.hl7.org/browse/FHIR-54323) | Change definition of `.biologicalSourceEvent` | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) |
| [FHIR-52946](https://jira.hl7.org/browse/FHIR-52946) | Device-conformsTo extension overlaps Device backbone element | [`562bcea91b9f`](https://github.com/HL7/fhir/commit/562bcea91b9fe6d4283cdc173c79abd026b5d6cc) — release-notes listing only; underlying fix lives in `HL7/fhir-extensions` PR #235 |
| (unattributed) | Non-TC cleanup of FiveWs mapping-exception reasons / divergent elements | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658), [`d68b0d377bc6`](https://github.com/HL7/fhir/commit/d68b0d377bc61943bb98962a0aeb03e7a7cef74b) |

The two large multi-resource commits in the window (`f22405098ca5` "First pass at some R6 ballot tickets" and `d2dde0c4a093` "OO tickets first draft") cite a further 13 ticket keys (FHIR-55444, FHIR-55271, FHIR-55270, FHIR-55001, FHIR-54041, FHIR-54037, FHIR-54034, FHIR-55277, FHIR-54961, FHIR-54593, FHIR-54450, FHIR-53457) whose changes did **not** land in any `source/device/**` file in this window. They are listed here for traceability only and are not treated as Device tickets.

## Per-Ticket Detail

### [FHIR-55372](https://jira.hl7.org/browse/FHIR-55372) — Device.name.display should not be a modifier

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied PR is [HL7/fhir#4006](https://github.com/HL7/fhir/pull/4006); the change is described informally as "Ignoring this element doesn't make the interpretation of the instance wrong."

- **Disposition summary:** The work group accepted that `Device.name.display` is a discriminator/preference flag rather than a true modifier — ignoring it does not invalidate or invert the meaning of the Device instance — so the `isModifier` flag is being removed.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
  - [`d68b0d377bc6`](https://github.com/HL7/fhir/commit/d68b0d377bc61943bb98962a0aeb03e7a7cef74b) — Adding placeholder release notes for non-TCs and final cleanup (2026-03-09; release-notes listing only)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-Device.xml`, the `<isModifier value="true"/>` and accompanying `<isModifierReason …>` elements are removed from the `Device.name.display` element definition; `isSummary="true"` is retained. No other element on the SD is touched. The `d68b0d` commit only adds the FHIR-55372 link to the transient Release-Notes blockquote in `device-introduction.xml`. (The `Device.name.display` row added to `device-fivews-mapping-exceptions.xml` in the same `d68b0d` commit is a non-TC FiveWs cleanup — see the unattributed entry below — not the FHIR-55372 fix.)

### [FHIR-52979](https://jira.hl7.org/browse/FHIR-52979) — Applying extension to FHIR R4 and earlier versions creates purpose overlap with Device.specialization element

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied PR is [HL7/fhir#4030](https://github.com/HL7/fhir/pull/4030); a related ticket flagged in comments is FHIR-52946.

- **Disposition summary:** Add narrative guidance to the Device resource explaining how the `device-conformsTo-source` extension relates to `Device.conformsTo` so that R5+ implementers know which mechanism to use for the `.source` sub-element. The matching extension-side resolution (capping the broader `device-conformsTo` extension at R4B) is being handled in FHIR-52946 against `HL7/fhir-extensions`.
- **Commits applying this ticket:**
  - [`f6c9d64997bc`](https://github.com/HL7/fhir/commit/f6c9d64997bc67a7c97a90dbbfe165f10561e64e) — FHIR-52979 (2026-03-13)
- **Changes applied:** Adds a new `Device.ConformsTo Source` section (anchor `conformsTo`) to `device-notes.xml`, stating that "if a need arises for the `.source` subelement, the `Device.conformsTo` element can be used as the element context for the `artifact-relatedArtifact` extension in FHIR R5 and later." Also adds the FHIR-52979 entry to the transient Release-Notes blockquote in `device-introduction.xml`. No SD or terminology files are touched by this ticket.

### [FHIR-56060](https://jira.hl7.org/browse/FHIR-56060) — Minor cleanup to value set display names

- **Work group:** Orders & Observations
- **Resolution:** Persuasive (Technical Correction)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied PR is [HL7/fhir#4037](https://github.com/HL7/fhir/pull/4037); the ticket text directs: "Display Names must be TitleCase: communicating … Change display of 'communicating' to 'Communicating'."

- **Disposition summary:** Correct two display strings in the `device-category` CodeSystem so the IG publisher's TitleCase warning clears: `communicating` → `Communicating` and `In vitro` → `In Vitro`. Definitions and codes are unchanged.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24): fixes `communicating` display.
  - [`6c40b35c33c5`](https://github.com/HL7/fhir/commit/6c40b35c33c5fb2bed980f376d6f05dc24a072f9) — Update codesystem-device-category.xml (2026-03-25): follow-up fix for the `in-vitro` display the first commit missed.
- **Changes applied:** `codesystem-device-category.xml` only — `<concept code="communicating">` display becomes `Communicating`, and `<concept code="in-vitro">` display becomes `In Vitro`. No code, definition, hierarchy, or value-set inclusion changes. Listed in the transient Release-Notes blockquote in `device-introduction.xml`.

### [FHIR-54323](https://jira.hl7.org/browse/FHIR-54323) — Change definition of `.biologicalSourceEvent`

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied PR is [HL7/fhir#4037](https://github.com/HL7/fhir/pull/4037).

- **Disposition summary:** The submitter requested removing the phrase "in this device" from the short and definition because it is confusing. The work group accepted with modification: rather than only deleting the phrase, the language was rewritten to mention the *donor* explicitly and to use the more generic "associated with the biological material incorporated into the device", aligning the wording style with the parallel definitions in `BiologicallyDerivedProduct` and `NutritionProduct`.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24)
- **Changes applied:** `structuredefinition-Device.xml`, the `Device.biologicalSourceEvent` element only — `short` and `definition` change from "A production identifier of the donation, collection, or pooling event from which biological material in this device was derived." to "A production identifier of the donor, donation, or pooling event associated with the biological material incorporated into the device." `comment`, `alias`, cardinality, type and mappings are unchanged. Snapshot regeneration required. Listed in the transient Release-Notes blockquote in `device-introduction.xml`.

### [FHIR-52946](https://jira.hl7.org/browse/FHIR-52946) — Device-conformsTo extension overlaps Device backbone element

- **Work group:** Orders & Observations
- **Resolution:** Not Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied PR for the substantive change is [HL7/fhir-extensions#235](https://github.com/HL7/fhir-extensions/pull/235) (cap the existing `device-conformsTo` extension at R4B); only the cross-link landed in this repo's Device intro.

- **Disposition summary:** Resolve the overlap between the `device-conformsTo` extension and the `Device.conformsTo` backbone element by capping the legacy extension at R4B so that R5/R6 implementers use the resource element (and the new `device-conformsTo-source` extension for the `.source` sub-element only). Companion to FHIR-52979.
- **Commits applying this ticket:**
  - [`562bcea91b9f`](https://github.com/HL7/fhir/commit/562bcea91b9fe6d4283cdc173c79abd026b5d6cc) — Adding an additional ticket for Device release notes (2026-03-16; release-notes listing only)
- **Changes applied:** No `source/device/**` content change beyond adding FHIR-52946 to the transient Release-Notes blockquote in `device-introduction.xml`. The actionable change for this ticket is in `HL7/fhir-extensions` and is out of scope for this artifact's diff.

### (unattributed) — Non-TC FiveWs mapping-exception cleanup

- **Commits applying these changes:**
  - [`d68b0d377bc6`](https://github.com/HL7/fhir/commit/d68b0d377bc61943bb98962a0aeb03e7a7cef74b) — Adding placeholder release notes for non-TCs and final cleanup (2026-03-09)
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24)
- **Changes applied:** In `device-fivews-mapping-exceptions.xml`, a new `divergentElement` row is added for `FiveWs.status` ↔ `Device.name.display` (declaring it modifier in the pattern but not in the resource — consistent with the FHIR-55372 demotion above), and three previously-`Unknown` `unmappedElement` reasons are filled in with explicit text: `FiveWs.author` → "There are no elements that meet the purpose or intent of author"; `FiveWs.actor` → "…of actor"; `FiveWs.source` → "…of source". No other narrative or SD content is affected. These are non-substantive cleanup edits that the work group flagged as non-TC.

## Roll-up Summary (after-applied state)

The window covers six commits and touches five files. Total diff: 26 insertions / 10 deletions. Nothing was added to or removed from search parameters, operations, examples, value sets, or implementation-guide manifests.

- **StructureDefinition (`structuredefinition-Device.xml`):**
  - `Device.biologicalSourceEvent` — `short` and `definition` rewritten to reference the *donor* and to use "associated with the biological material incorporated into the device" instead of "from which biological material in this device was derived" (FHIR-54323). No cardinality / type / binding change.
  - `Device.name.display` — `isModifier` flag and `isModifierReason` removed; element is no longer a modifier (FHIR-55372). Cardinality, type (`boolean`), `condition` (`dev-1`) and `isSummary` are unchanged.
  - Snapshot regeneration required to pick up both differential edits.
- **Intro / narrative (`device-introduction.xml`, `device-notes.xml`):**
  - `device-introduction.xml` — a *transient* "Release Notes (pending alternative process review with FMG)" blockquote was added next to the existing ballot note, listing FHIR-55372, FHIR-52979, FHIR-52946, FHIR-56060, FHIR-54323. The existing `class="ballot-note" id="bn1"` block (R5→R6 normative-readiness summary) was **not** edited in this window. The release-notes block is not styled as a ballot note and the work group has flagged it as awaiting FMG process direction; the proposed ballot note below replaces the listing with a substantive bulleted summary.
  - `device-notes.xml` — new `Device.ConformsTo Source` section (anchor `conformsTo`) telling implementers that, when the `.source` sub-element is needed in R5+, `Device.conformsTo` can be used as the element context for the `artifact-relatedArtifact` extension (FHIR-52979).
- **FiveWs mapping exceptions (`device-fivews-mapping-exceptions.xml`):**
  - New divergent row recording that `FiveWs.status` is modifier in the pattern but not in `Device.name.display` (a downstream consequence of FHIR-55372).
  - Reasons for `FiveWs.author`, `FiveWs.actor`, and `FiveWs.source` changed from `Unknown` to "There are no elements that meet the purpose or intent of …" (non-TC cleanup).
- **Search parameters (`bundle-Device-search-params.xml`):** No changes.
- **Operations (`list-Device-operations.xml`):** No changes.
- **Examples (`list-Device-examples.xml`, `device-example*.xml`):** No additions, removals, or edits. The biologicalSourceEvent text change does not require existing example updates.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - `codesystem-device-category.xml` — TitleCase fix for two display values: `communicating` → `Communicating`, `In vitro` → `In Vitro` (FHIR-56060). Codes, definitions, and value-set membership unchanged.
  - All other `codesystem-*` and `valueset-*` files are unchanged.
  - No content here belongs in UTG (these are Device-domain code systems published by FhirCore per the briefing's cross-repo guidance).

## Proposed Ballot Note (HTML)

The proposal preserves the existing `bn1` block (R5→R6 normative-readiness narrative is still accurate at HEAD) and adds a new `bn2` block summarising the substantive changes that landed since `5d67a34a13a5`. The transient "Release Notes (pending alternative process review with FMG)" blockquote should be replaced by `bn2` once the FMG process question is resolved.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure the Device resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
  <p>For an overview of this resource and others in the Device domain, also see the <a href="device-module.html">Device Module</a> page.</p>
  <p>The Device scope and usage has been revised.  A majority of content has been moved DeviceDefinition to describe the types of devices in scope.</p>
  <p>The following element was added:</p>
  <ul>
    <li>Device.additive as a backbone.</li>
  </ul>
  <p>The following elements have been revised:</p>
  <ul>
    <li>Updated Device.definition datatype to canonical(DeviceDefinition).</li>
    <li>Updated Device.version to Device.deviceVersion.</li>
  </ul>
  <p>The following elements have been removed from Device:</p>
  <ul>
    <li>Device.displayName as it was duplicated in Device.name backbone.</li>
    <li>Device.owner has been removed and was moved to DeviceAssociation.relationship of the subject. Please comment on the revision if there are issues with removing the identification of individuals in the Device resource.</li>
    <li>Device.mode, Device.cycle, Device.duration, Device.gateway, Device.endpoint have been removed and the following extensions were added: device-mode, device-cycle, device-duration, device-gateway, and device-endpoint.</li>
  </ul>
  <p>The following extensions were added:</p>
  <ul>
    <li>device-alertDetection to describe the alert detection activation states for the overall device.</li>
    <li>device-conformsTo-source – represents the source of the device specification.</li>
  </ul>
</blockquote>

<blockquote class="ballot-note" id="bn2">
  <p><b>Note to Balloters:</b> The following substantive changes were applied to Device since the previous ballot snapshot. Reviewers focused on the Normative readiness of Device should pay particular attention to the modifier-flag and biologicalSourceEvent definition changes; the remaining items are clarifications and a technical correction.</p>
  <ul>
    <li><code>Device.name.display</code> is no longer flagged as a modifier element; the <code>isModifier</code> flag and its reason have been removed (the element remains a summary boolean with cardinality 0..1 and the <code>dev-1</code> constraint). A matching FiveWs mapping-exception row has been added to record that the divergence from the FiveWs status pattern is intentional. (<a href="https://jira.hl7.org/browse/FHIR-55372">FHIR-55372</a>)</li>
    <li>The short and definition of <code>Device.biologicalSourceEvent</code> have been rewritten to reference the <em>donor</em> explicitly and to align wording with the parallel elements on <code>BiologicallyDerivedProduct</code> and <code>NutritionProduct</code> ("a production identifier of the donor, donation, or pooling event associated with the biological material incorporated into the device"). No structural change. (<a href="https://jira.hl7.org/browse/FHIR-54323">FHIR-54323</a>)</li>
    <li>Guidance has been added to the Device notes describing how to use <code>Device.conformsTo</code> as the element context for the <code>artifact-relatedArtifact</code> extension when an implementer needs the <code>.source</code> sub-element in FHIR R5 and later. The companion change capping the legacy <code>device-conformsTo</code> extension at R4B is being applied in the FHIR Extensions Pack. (<a href="https://jira.hl7.org/browse/FHIR-52979">FHIR-52979</a>, <a href="https://jira.hl7.org/browse/FHIR-52946">FHIR-52946</a>)</li>
    <li>Display names in the <code>device-category</code> CodeSystem have been corrected to TitleCase (<code>communicating</code> → <code>Communicating</code>, <code>In vitro</code> → <code>In Vitro</code>); codes and definitions are unchanged. (<a href="https://jira.hl7.org/browse/FHIR-56060">FHIR-56060</a>)</li>
  </ul>
  <p>No changes were made to Device search parameters, operations, examples, or other Device-scoped value sets and code systems in this window.</p>
</blockquote>
```

## Notes for Reviewer

- The transient `<blockquote style="background-color: lightblue">` "Release Notes (pending alternative process review with FMG)" block at the top of `device-introduction.xml` is not styled as a ballot note (no `class="ballot-note"`, no `id`). The proposal above replaces its bare ticket list with a substantive `bn2` ballot note; once accepted, the transient block should be deleted from the intro file.
- The existing `bn1` ballot note describes the R5→R6 normative-readiness changes (Device.additive, Device.deviceVersion, Device.displayName/owner/mode/cycle/duration/gateway/endpoint removals, etc.). None of those items have been reverted in this window, so the block is carried forward verbatim.
- The two large multi-resource commits in the window (`f22405098ca5`, `d2dde0c4a093`) cite many tickets in their commit bodies that did not actually touch `source/device/**`. They are listed in the *Tickets Applied in Window* table for traceability but are not surfaced in the proposed ballot note.
- FHIR-52946's substantive change is in `HL7/fhir-extensions` (PR #235); only the cross-link landed in the Device intro. Reviewers chasing the extension cap should look at the extensions-pack ballot note rather than this artifact.
- No applied-vote / disposition comment text was returned by the FhirAugury Jira data for any of the five tickets; the disposition fields above quote the closest available evidence (PR links, ticket-body excerpts) and explicitly note the gap. If verbatim disposition text is needed for the ballot package, it should be pulled from the work group's Confluence minutes or directly from Jira.
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit (`5d67a34a13a5`), so the standard fast-forward `since..HEAD` window was used. Briefing metadata records `clone_head_sha = 1b369ff4e28e`; the live clone has advanced to `db79dcdfe196` since the briefing was taken, but the Artifact Map for `source/device/**` is still accurate.

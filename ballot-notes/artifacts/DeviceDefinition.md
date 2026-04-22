# Artifact Ballot Note Draft: DeviceDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `DeviceDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 5 |
| Tickets attributed | 2 (FHIR-55257, FHIR-54866) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` (briefing analysed at 2026-04-20; clone HEAD has advanced to `db79dcdfe196` since briefing was generated, but the `source/devicedefinition/` Artifact Map remains valid) |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `DeviceDefinition` for this run (resolved against the briefing's FhirCore Artifact Map and the contents of `source/devicedefinition/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/devicedefinition/structuredefinition-DeviceDefinition.xml` | StructureDefinition (canonical SD) | yes |
| `source/devicedefinition/devicedefinition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/devicedefinition/devicedefinition-notes.xml` | Supplementary narrative | no |
| `source/devicedefinition/bundle-DeviceDefinition-search-params.xml` | Search parameters bundle | no |
| `source/devicedefinition/list-DeviceDefinition-operations.xml` | Operations list | no |
| `source/devicedefinition/list-DeviceDefinition-examples.xml` | Examples list | no |
| `source/devicedefinition/list-DeviceDefinition-packs.xml` | Profile/extension pack list (sibling artifact) | no |
| `source/devicedefinition/devicedefinition-example.xml` | Example | no |
| `source/devicedefinition/devicedefinition-example-prodspec.xml` | Example | no |
| `source/devicedefinition/devicedefinition-examples-header.xml` | Examples narrative header | no |
| `source/devicedefinition/devicedefinition-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/devicedefinition/codesystem-devicedefinition-warnings-example.xml` | **New** artifact-scoped CodeSystem | yes (added) |
| `source/devicedefinition/valueset-devicedefinition-warnings-example.xml` | **New** artifact-scoped ValueSet | yes (added) |
| `source/devicedefinition/codesystem-device-correctiveactionscope.xml` | Artifact-scoped CodeSystem | no |
| `source/devicedefinition/codesystem-device-definition-status.xml` | Artifact-scoped CodeSystem | no |
| `source/devicedefinition/codesystem-device-productidentifierinudi.xml` | Artifact-scoped CodeSystem | no |
| `source/devicedefinition/codesystem-devicedefinition-regulatory-identifier-type.xml` | Artifact-scoped CodeSystem (target of FHIR-55257 binding relaxation) | no |
| `source/devicedefinition/codesystem-devicedefinition-relationtype.xml` | Artifact-scoped CodeSystem | no |
| `source/devicedefinition/codesystem-parameter-group.xml` | Artifact-scoped CodeSystem | no |
| `source/devicedefinition/valueset-device-correctiveactionscope.xml` | Artifact-scoped ValueSet | no |
| `source/devicedefinition/valueset-device-definition-status.xml` | Artifact-scoped ValueSet | no |
| `source/devicedefinition/valueset-device-productidentifierinudi.xml` | Artifact-scoped ValueSet | no |
| `source/devicedefinition/valueset-devicedefinition-regulatory-identifier-type.xml` | Artifact-scoped ValueSet (target of FHIR-55257 binding relaxation) | no |
| `source/devicedefinition/valueset-devicedefinition-relationtype.xml` | Artifact-scoped ValueSet | no |
| `source/devicedefinition/valueset-parameter-group.xml` | Artifact-scoped ValueSet | no |

Patterns from the briefing that produced no match in the clone:

- `source/devicedefinition/devicedefinition-spreadsheet.xml` — no file matched (DeviceDefinition does not ship a legacy spreadsheet; SD is authoritative).
- `source/devicedefinition/devicedefinition-example*.xml` extras beyond the two listed above — no additional files matched.
- Sibling `structuredefinition-*.xml` artifacts beyond the canonical SD — none present in this folder.

## Current Ballot Note

A single ballot note exists at HEAD (`bn1`) in `devicedefinition-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the DeviceDefinition resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Updated DeviceDefinition to a CanonicalResource and the necessary element and search parameter changes.</li>
<li>Removed DeviceDefinition.owner.</li>
</ul>
<p>All OO Resources were updated to use the canonical, however other Resources (not owned by the OO Work Group) might not have the canonical reference to DeviceDefinition.</p>
</blockquote>
```

A sibling `<blockquote class="stu-note" …>` "Release Notes (pending alternative process review with FMG)" was **added** in this window (commit [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102)) and lists FHIR-55257 and FHIR-54866. That note is not the canonical ballot note (different `class`); the proposed ballot note below incorporates the same substance more formally and the editor may decide whether to retain the parallel STU release-note block or fold it into `bn1`.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55257](https://jira.hl7.org/browse/FHIR-55257) | DeviceDefinition.regulatoryIdentifier.type has no escape valve | [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) |
| [FHIR-54866](https://jira.hl7.org/browse/FHIR-54866) | Missing value set binding for codeable concept DeviceDefinition.guideline.warning | [`b5d5faeb457e`](https://github.com/HL7/fhir/commit/b5d5faeb457ef2d1915ad1cef73cf047d1d83076), [`0f4a6e1f7714`](https://github.com/HL7/fhir/commit/0f4a6e1f77148c3830e29be22776f1094d9e2503), [`ede19cd9ea69`](https://github.com/HL7/fhir/commit/ede19cd9ea69269aa162ee08fc2253e7015d0894), [`4b59b7f541f4`](https://github.com/HL7/fhir/commit/4b59b7f541f4ec75d73244fbae253beac6f90cda) |

No commits in the window touched DeviceDefinition files without an attributable ticket. (Commit `b62975d9ed5b` also lists FHIR-55272, FHIR-53677, and FHIR-54999 in its body, but those tickets target ObservationDefinition, DeviceAssociation, and BiologicallyDerivedProduct respectively — none of their changes landed in `source/devicedefinition/`. They are noted under "Notes for Reviewer".)

## Per-Ticket Detail

### [FHIR-55257](https://jira.hl7.org/browse/FHIR-55257) — DeviceDefinition.regulatoryIdentifier.type has no escape valve

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Update as follows:
  >
  > | DeviceDefinition.regulatoryIdentifier.type | |
  > | --- | --- |
  > | Element Id | DeviceDefinition.regulatoryIdentifier.type |
  > | Definition | The type of identifier itself. |
  > | Short Display | basic \| master \| license |
  > | Cardinality | 1..1 |
  > | Terminology Binding | Device Definition Regulatory Identifier Type (~~Required~~ Extensible) |
  > | Type | ~~code~~ codeableConcept |
  > | Summary | false |
  >
  > Note that this will allow an "escape" from the options provided.
  >
  > Move to code system to THO in a separate ticket.

- **Disposition summary:** Relax `DeviceDefinition.regulatoryIdentifier.type` so implementers can express jurisdiction-specific or otherwise out-of-list identifier types. The element's data type changes from `code` to `CodeableConcept`, and its binding to the existing `devicedefinition-regulatory-identifier-type` value set is loosened from required to extensible. Cardinality (1..1) is unchanged. The disposition also notes that the underlying code system should later be moved to THO under a separate ticket.
- **Commits applying this ticket:**
  - [`b62975d9ed5b`](https://github.com/HL7/fhir/commit/b62975d9ed5b4cd55c6a598d0cc440395dd8b102) — More OO tickets (2026-03-11)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-DeviceDefinition.xml`, the `DeviceDefinition.regulatoryIdentifier.type` element's `<type>/<code>` is changed from `code` to `CodeableConcept` and its `<binding>/<strength>` is changed from `required` to `extensible`. The bound value set URL (`http://hl7.org/fhir/ValueSet/devicedefinition-regulatory-identifier-type`) and binding name (`DeviceRegulatoryIdentifierType`) are unchanged. The same commit also adds an STU "Release Notes (pending alternative process review with FMG)" `<blockquote>` to `devicedefinition-introduction.xml` listing FHIR-55257 (and FHIR-54866). The underlying code system / value set files are not modified in this window — moving them to THO is deferred per the disposition.

### [FHIR-54866](https://jira.hl7.org/browse/FHIR-54866) — Missing value set binding for codeable concept DeviceDefinition.guideline.warning

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Add an example binding with experimental flag on a new valueset and code system named "device-warnings-example":
  >
  > **Code, Display, Definition**
  >
  > "flammable", Flammable, "Flammable - keep away from heat/open flame"
  > "electrical-shock-risk", Electrical Shock risk, "Risk of electrical shock - follow grounding/earthing instructions"
  > "do-not-submerge", Do Not Submerge, "Do not immerse / keep dry"
  > "temperature-limit", Temperature Limit, "Temperature limits must be observed"
  > "requires-training", Requires Training, "Operator training required"
  > "battery-handling", Battery Handling, "Battery handling / charging instructions"

  HCP 2026-03-16 note (from Jira comments): "the valueset for this binding is example and does not need to be put in THO."

- **Disposition summary:** Provide an example binding for the previously unbound `CodeableConcept` element `DeviceDefinition.guideline.warning`. A new artifact-scoped CodeSystem and ValueSet (`devicedefinition-warnings-example`, marked experimental / informative) are added with six starter concepts covering common device hazards. The binding is `example`, signalling that implementers may freely substitute their own codes; the value set deliberately stays in the `source/devicedefinition/` artifact bundle rather than being promoted to THO.
- **Commits applying this ticket:**
  - [`b5d5faeb457e`](https://github.com/HL7/fhir/commit/b5d5faeb457ef2d1915ad1cef73cf047d1d83076) — Add example valueset for device definition codeable concept (2026-03-16)
  - [`0f4a6e1f7714`](https://github.com/HL7/fhir/commit/0f4a6e1f77148c3830e29be22776f1094d9e2503) — Remove empty identifier tag (2026-03-16)
  - [`ede19cd9ea69`](https://github.com/HL7/fhir/commit/ede19cd9ea69269aa162ee08fc2253e7015d0894) — Adjusting valueset naming (2026-03-17)
  - [`4b59b7f541f4`](https://github.com/HL7/fhir/commit/4b59b7f541f4ec75d73244fbae253beac6f90cda) — Changing valueset and codesystem to informative as they are example only (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** Adds two new files — `codesystem-devicedefinition-warnings-example.xml` (six concepts: `flammable`, `electrical-shock-risk`, `do-not-submerge`, `temperature-limit`, `requires-training`, `battery-handling`) and `valueset-devicedefinition-warnings-example.xml` (composes the new code system). Both carry `structuredefinition-wg = oo`, `experimental = true`, and (after `4b59b7`) `structuredefinition-standards-status = informative`. In `structuredefinition-DeviceDefinition.xml`, the `DeviceDefinition.guideline.warning` element gains a `<binding>` block (binding name `DeviceWarningsExample`, strength `example`, value set `http://hl7.org/fhir/ValueSet/devicedefinition-warnings-example`). Follow-up commits in the same window remove an empty `<identifier/>` tag from the CodeSystem (`0f4a6e`) and align naming/IDs/version of the new artifacts (`ede19c`); these are clean-up of the same change set and have no separate ticket. The four commits should be read together — only the after-applied state is meaningful.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-DeviceDefinition.xml`):**
  - `DeviceDefinition.regulatoryIdentifier.type` — `<type>/<code>` changed from `code` to `CodeableConcept`; `<binding>/<strength>` changed from `required` to `extensible`. Same value set URL (`devicedefinition-regulatory-identifier-type`) and binding name (`DeviceRegulatoryIdentifierType`) are retained. (FHIR-55257)
  - `DeviceDefinition.guideline.warning` — gains a new `<binding>` (binding name `DeviceWarningsExample`, strength `example`, value set `http://hl7.org/fhir/ValueSet/devicedefinition-warnings-example`); previously had no binding. (FHIR-54866)
  - Snapshot regeneration is required (these are differential edits; the repository's snapshot is derived).
- **Intro / narrative (`devicedefinition-introduction.xml`):**
  - A new `<blockquote class="stu-note" …>` "Release Notes (pending alternative process review with FMG)" was added immediately after the existing ballot note `bn1`, citing FHIR-55257 and FHIR-54866.
  - `devicedefinition-notes.xml` is unchanged.
- **Search parameters (`bundle-DeviceDefinition-search-params.xml`):**
  - No changes.
- **Operations (`list-DeviceDefinition-operations.xml`):**
  - No changes.
- **Examples:**
  - No new or removed examples; existing examples were not edited and do not reference either of the changed elements, so no example updates are required to remain valid against the differential.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - **Added** `codesystem-devicedefinition-warnings-example.xml` and `valueset-devicedefinition-warnings-example.xml` (experimental, informative, work-group `oo`, six concepts). (FHIR-54866)
  - The HCP discussion explicitly decided to keep these example artifacts in `source/devicedefinition/` rather than promoting them to UTG, so no UTG cross-repo touch point is introduced.
  - The existing `codesystem-devicedefinition-regulatory-identifier-type.xml` / `valueset-devicedefinition-regulatory-identifier-type.xml` are untouched in this window despite the disposition mentioning a future move to THO under a separate ticket.

## Proposed Ballot Note (HTML)

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure the DeviceDefinition resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Updated DeviceDefinition to a CanonicalResource and the necessary element and search parameter changes.</li>
<li>Removed DeviceDefinition.owner.</li>
</ul>
<p>All OO Resources were updated to use the canonical, however other Resources (not owned by the OO Work Group) might not have the canonical reference to DeviceDefinition.</p>
<p>Substantive changes since the previous ballot:</p>
<ul>
<li><code>DeviceDefinition.regulatoryIdentifier.type</code> has been changed from <code>code</code> to <code>CodeableConcept</code> and its binding to the <code>devicedefinition-regulatory-identifier-type</code> value set has been relaxed from <i>required</i> to <i>extensible</i>, so jurisdictions whose identifier type is not yet enumerated can still populate the element. Cardinality is unchanged (1..1). A follow-up move of the value set to THO is anticipated under a separate ticket. (<a href="https://jira.hl7.org/browse/FHIR-55257">FHIR-55257</a>)</li>
<li><code>DeviceDefinition.guideline.warning</code> now carries an <i>example</i> binding to a new experimental value set <code>devicedefinition-warnings-example</code> (codes: <code>flammable</code>, <code>electrical-shock-risk</code>, <code>do-not-submerge</code>, <code>temperature-limit</code>, <code>requires-training</code>, <code>battery-handling</code>). The binding is intentionally example-strength so implementers may substitute their own warning codes, and the value set is kept artifact-scoped (not promoted to THO) per HCP discussion. (<a href="https://jira.hl7.org/browse/FHIR-54866">FHIR-54866</a>)</li>
</ul>
</blockquote>
```

## Notes for Reviewer

- **Existing `bn1` content carried forward unchanged.** The pre-existing R5 → R6 framing (CanonicalResource conversion, removal of `DeviceDefinition.owner`, OO-resource canonical adoption) is still accurate against HEAD and is preserved verbatim. Only new bullets were appended.
- **Parallel STU release-note block.** Commit `b62975d9ed5b` introduced a `<blockquote class="stu-note" …>` "Release Notes (pending alternative process review with FMG)" block listing FHIR-55257 and FHIR-54866. The proposed ballot note above conveys the same substance more fully; the editor may either delete that STU block when adopting this draft or leave it in place as a tracking artifact pending the FMG process discussion.
- **Tickets mentioned in commit `b62975d9ed5b` that do *not* apply to DeviceDefinition:**
  - [FHIR-55272](https://jira.hl7.org/browse/FHIR-55272) — `ObservationDefinition.identifier should repeat` (changes land in `source/observationdefinition/`).
  - [FHIR-53677](https://jira.hl7.org/browse/FHIR-53677) — `DeviceAssociation.subject` short-description / comment clarification (changes land in `source/deviceassociation/`).
  - [FHIR-54999](https://jira.hl7.org/browse/FHIR-54999) — `BiologicallyDerivedProduct.therapyIdentifier` grouping element (changes land in `source/biologicallyderivedproduct/`).
  These are correctly absent from the proposed ballot note for DeviceDefinition. They will be picked up by their own artifact ballot notes.
- **Code-system → THO follow-up.** The FHIR-55257 disposition explicitly defers moving the `devicedefinition-regulatory-identifier-type` code system to THO. No such follow-up commit is present in the window; the QA comment on the ticket flags that the THO-move ticket may not yet exist. Reviewers may wish to confirm.
- **`fhir-augury-cli cross-referenced` returned no hits** for any of the five commits in this window, so per-ticket attribution was driven by the explicit Jira URLs in commit `b62975d9ed5b`'s body and by content matching for FHIR-54866 (the four warnings-example commits do not cite a ticket directly, but the changes implement FHIR-54866's resolution verbatim and FHIR-54866 is independently listed in the new STU release-notes block).
- **Briefing freshness.** The cached briefing was generated against clone SHA `1b369ff4e28e`; HEAD is now `db79dcdfe196`. The briefing's Artifact Map for DeviceDefinition is unaffected by the intervening commits (none restructure `source/devicedefinition/`), so it was used as-is.

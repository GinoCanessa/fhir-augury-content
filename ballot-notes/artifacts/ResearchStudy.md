# Artifact Ballot Note Draft: ResearchStudy (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `ResearchStudy` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 10 |
| Tickets attributed | 6 (FHIR-53692, FHIR-53693, FHIR-53694, FHIR-53696, FHIR-53697, FHIR-53698) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T17:04:59Z |

## Source Files

Files considered part of `ResearchStudy` for this run (resolved from the
briefing's Artifact Map plus FhirCore folder conventions, against
`source/researchstudy/` in the cache clone). "Touched in window" reflects
the `5d67a34a13a5..db79dcdfe196` diff scoped to the file.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/researchstudy/structuredefinition-ResearchStudy.xml` | Canonical StructureDefinition | yes |
| `source/researchstudy/researchstudy-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/researchstudy/researchstudy-notes.xml` | Supplementary narrative | no |
| `source/researchstudy/bundle-ResearchStudy-search-params.xml` | Search parameters | no |
| `source/researchstudy/list-ResearchStudy-operations.xml` | Operations | no |
| `source/researchstudy/list-ResearchStudy-examples.xml` | Examples list | no |
| `source/researchstudy/list-ResearchStudy-packs.xml` | Packs list | no |
| `source/researchstudy/implementationguide-ResearchStudy-core.xml` | IG companion | no |
| `source/researchstudy/researchstudy-example.xml` | Example | no |
| `source/researchstudy/researchstudy-example-ctgov-study-record.xml` | Example (ClinicalTrials.gov-derived) | yes |
| `source/researchstudy/researchstudy-examples-header.xml` | Examples header narrative | no |
| `source/researchstudy/researchstudy-fivews-mapping-exceptions.xml` | 5Ws mapping notes | no |
| `source/researchstudy/valueset-research-study-arm-type.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-classifiers.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-focus-type.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-objective-type.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-party-organization-type.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-party-role.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-phase.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-prim-purp-type.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-status.xml` | Artifact-scoped ValueSet | no |
| `source/researchstudy/valueset-research-study-trial-phase.xml` | Artifact-scoped ValueSet (deleted) | yes (deleted) |
| `source/researchstudy/codesystem-research-study-arm-type.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-classifiers.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-objective-type.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-party-organization-type.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-party-role.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-phase.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-prim-purp-type.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-status.xml` | Artifact-scoped CodeSystem | no |
| `source/researchstudy/codesystem-research-study-statusDate-activity.xml` | Artifact-scoped CodeSystem | no |

Patterns from the briefing that produced no match in the clone:

- `source/researchstudy/researchstudy-spreadsheet.xml` — no file matched (legacy spreadsheet not present; the StructureDefinition is authoritative for this resource).
- No sibling `structuredefinition-*.xml` other than the canonical SD exists in this folder (no extra profile artifacts ship alongside `ResearchStudy`).

## Current Ballot Note

The ballot note shown below was **added during this window** (commit
[`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064)
by Khalid Shahin on 2026-04-10) and is the state of
`source/researchstudy/researchstudy-introduction.xml` at HEAD
(`db79dcdfe196`). There was no ballot note at the since-commit
(`5d67a34a13a5`).

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> The key changes made since FHIR 6.0.0-ballot4 include:</p>
<p>Changed the ResearchStudy.studyDesign ValueSet binding to be HL7 Terminology.</p>
<p>Changed the ResearchStudy.associatedParty.role ValueSet binding to be HL7 Terminology and &quot;preferred&quot; binding.</p>
<p>Changed the ResearchStudy.progressStatus.state ValueSet binding to be HL7 Terminology and &quot;preferred&quot; binding.</p>
<p>Added DocumentReference as a possible Resource type to ResearchStudy.result.</p>
<p>Added ResearchStudy.comparisonGroup.name string element.</p>
<p>Changed ResearchStudy.primaryPurposeType 0..1 to ResearchStudy.purposeType 0..* and example binding strength..</p>
</blockquote>
```

A second adjacent `<blockquote style="background-color: lightblue">`
"Release Notes" block was added in the same commit and lists Jira links
to FHIR-53692, -53693, -53694, -53696, -53697, -53698. It is included
verbatim below for reference but is not a `class="ballot-note"` element
and is not part of the proposed ballot-note revision:

```html
<blockquote style="background-color: lightblue">
	<p><b>Release Notes:</b></p>
	<ul>
		<li><a href="https://jira.hl7.org/browse/FHIR-53698">FHIR-53698</a></li>
		<li><a href="https://jira.hl7.org/browse/FHIR-53697">FHIR-53697</a></li>
		<li><a href="https://jira.hl7.org/browse/FHIR-53696">FHIR-53696</a></li>
		<li><a href="https://jira.hl7.org/browse/FHIR-53694">FHIR-53694</a></li>
		<li><a href="https://jira.hl7.org/browse/FHIR-53693">FHIR-53693</a></li>
		<li><a href="https://jira.hl7.org/browse/FHIR-53692">FHIR-53692</a></li>
	</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53692](https://jira.hl7.org/browse/FHIR-53692) | change ResearchStudy.primaryPurposeType 0..1 to ResearchStudy.purposeType 0..* | [`29b99a6ac02c`](https://github.com/HL7/fhir/commit/29b99a6ac02cc0bc579b8c911f0cee469d685dce), [`108e9243192e`](https://github.com/HL7/fhir/commit/108e9243192e358b2f733e61a06635775c11e837), [`5a1a9faf4c18`](https://github.com/HL7/fhir/commit/5a1a9faf4c180b23010be1c8519d55c547d6fc22) |
| [FHIR-53693](https://jira.hl7.org/browse/FHIR-53693) | Add ResearchStudy.comparisonGroup.name 0..1 string | [`3c6b5ae436f1`](https://github.com/HL7/fhir/commit/3c6b5ae436f122512c1f6c0101aa5d6a757ec06a) |
| [FHIR-53694](https://jira.hl7.org/browse/FHIR-53694) | Add DocumentReference as a type option for ResearchStudy.result 0..* Reference | [`00ffdb2a4053`](https://github.com/HL7/fhir/commit/00ffdb2a40537951cbe52aa6dcd72fbfb949529c) |
| [FHIR-53696](https://jira.hl7.org/browse/FHIR-53696) | Change binding for ResearchStudy.associatedParty.role | [`138abc2fcfde`](https://github.com/HL7/fhir/commit/138abc2fcfde82ff9ddb74e31c78bfbe4c1ee016) |
| [FHIR-53697](https://jira.hl7.org/browse/FHIR-53697) | Change binding for ResearchStudy.progressStatus.state | [`8ba6eab23c24`](https://github.com/HL7/fhir/commit/8ba6eab23c248e13e6e6214fa9f73eaf2e0e8eca) |
| [FHIR-53698](https://jira.hl7.org/browse/FHIR-53698) | Change binding for ResearchStudy.studyDesign | [`28915130e7d5`](https://github.com/HL7/fhir/commit/28915130e7d5d94fff026bd5e5aa64da6a241480) |
| (unattributed) | n/a | [`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) — "Added a Ballot Note changes to the ResearchStudy introduction"; [`b694f466cf85`](https://github.com/HL7/fhir/commit/b694f466cf85172849240bd786c97936056f9c87) — "updated the example to reflect the changes" |

## Per-Ticket Detail

### [FHIR-53692](https://jira.hl7.org/browse/FHIR-53692) — change ResearchStudy.primaryPurposeType 0..1 to ResearchStudy.purposeType 0..*

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The change request body
  > states: "As discussed in BRR, and resulting from use cases with the
  > Evidence Based Medicine on FHIR Implementation Guide, European
  > Medicines Agency Clinical Trial Information System (EU CTIS), and
  > other projects, the ResearchStudy purpose needs to be a multi-item
  > selection and not specific to a singular primary purpose. Therefore,
  > the ResearchStudy.primaryPurposeType 0..1 CodeableConcept needs to
  > become ResearchStudy.purposeType 0..* CodeableConcept. The binding
  > for this element should be Preferred strength and go to a
  > ResearchStudyPurposeType ValueSet that will be developed by BRR and
  > placed in THO. This was decided by BRR on November 18, 2025."

- **Disposition summary:** Rename `ResearchStudy.primaryPurposeType` to
  `ResearchStudy.purposeType`, widen its cardinality from `0..1` to
  `0..*`, and (per the request) move to a Preferred binding against a
  forthcoming THO ValueSet. The ticket reflects BRR's 2025-11-18
  decision driven by EBM-on-FHIR and EU CTIS use cases that need
  multiple intent codes per study.
- **Commits applying this ticket:**
  - [`29b99a6ac02c`](https://github.com/HL7/fhir/commit/29b99a6ac02cc0bc579b8c911f0cee469d685dce) — J#53692 Changed ResearchStudy.primaryPurposeType 0..1 to ResearchStudy.purposeType 0..* and example binding strength. (2026-04-10)
  - [`108e9243192e`](https://github.com/HL7/fhir/commit/108e9243192e358b2f733e61a06635775c11e837) — Update researchstudy-example-ctgov-study-record.xml (2026-04-10)
  - [`5a1a9faf4c18`](https://github.com/HL7/fhir/commit/5a1a9faf4c180b23010be1c8519d55c547d6fc22) — Update researchstudy-example-ctgov-study-record.xml (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-ResearchStudy.xml`, the element id and path were
  renamed from `ResearchStudy.primaryPurposeType` to
  `ResearchStudy.purposeType`, and `max` was widened from `1` to `*`.
  The binding strength on the same element was changed from `preferred`
  to `example` (note: this contradicts the ticket body, which asked for
  Preferred — see "Notes for Reviewer"). The bindingName
  (`ResearchStudyPrimaryPurposeType`), description ("Codes for the
  main intent of the study."), and ValueSet
  (`http://terminology.hl7.org/ValueSet/research-study-prim-purp-type`)
  were left unchanged. In
  `researchstudy-example-ctgov-study-record.xml`, the
  `<primaryPurposeType>` element was renamed to `<purposeType>` (the
  remaining example-content edits in commits `108e92` and `5a1a9f`
  appear to be tracked-pause re-saves with no semantic delta in the
  after-applied diff).

### [FHIR-53693](https://jira.hl7.org/browse/FHIR-53693) — Add ResearchStudy.comparisonGroup.name 0..1 string

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The change request body
  > states: "Add ResearchStudy.comparisonGroup.name 0..1 string to
  > allow simple labels for comparison groups. This is needed so that
  > implementers do not need to invent and selectively use complex
  > pathways to create labels for comparison groups. Use case
  > established for converting European Union Clinical Trial
  > Information System (EU CTIS) records to FHIR."

- **Disposition summary:** Add an optional plain-string label
  (`name 0..1 string`) to `ResearchStudy.comparisonGroup` so that
  implementers can attach a short human-readable identifier to a
  comparison group without resorting to ad-hoc encodings.
- **Commits applying this ticket:**
  - [`3c6b5ae436f1`](https://github.com/HL7/fhir/commit/3c6b5ae436f122512c1f6c0101aa5d6a757ec06a) — J#53693 Added ResearchStudy.comparisonGroup.name 0..1 string (2026-04-02)
- **Changes applied (per Step 5b, scoped to this artifact):** A new
  `ResearchStudy.comparisonGroup.name` element was inserted into the
  StructureDefinition `<differential>` immediately before
  `ResearchStudy.comparisonGroup.description`, with `min=0`, `max=1`,
  type `string`, and `short` value "A simple label for the comparison
  Group". No examples were updated to demonstrate the new element.

### [FHIR-53694](https://jira.hl7.org/browse/FHIR-53694) — Add DocumentReference as a type option for ResearchStudy.result 0..* Reference

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The change request body
  > states: "Add DocumentReference as a type option for
  > ResearchStudy.result 0..* Reference. This is needed because the
  > prior type option of Citation is no longer available as the
  > Citation Resource became an Additional Resource. The
  > DocumentReference Resource will allow linking externally to a
  > Citation."

- **Disposition summary:** Restore the ability to point at an externally
  hosted citation/document from `ResearchStudy.result` by adding
  `DocumentReference` to the existing `Reference(Composition |
  DiagnosticReport | Evidence)` target list, since `Citation` was
  removed when it moved to Additional Resources.
- **Commits applying this ticket:**
  - [`00ffdb2a4053`](https://github.com/HL7/fhir/commit/00ffdb2a40537951cbe52aa6dcd72fbfb949529c) — J#53694 Add DocumentReference as a type option for ResearchStudy.result 0..* Reference (2026-04-02)
- **Changes applied (per Step 5b, scoped to this artifact):** A new
  `<targetProfile value="http://hl7.org/fhir/StructureDefinition/DocumentReference"/>`
  was added to the `Reference` `type` element on
  `ResearchStudy.result`, between the existing `DiagnosticReport` and
  `Evidence` target profiles. `Composition`, `DiagnosticReport`, and
  `Evidence` remain. Cardinality and other element attributes are
  unchanged.

### [FHIR-53696](https://jira.hl7.org/browse/FHIR-53696) — Change binding for ResearchStudy.associatedParty.role

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The change request body
  > states: "ResearchStudy.associatedParty.role has Example binding to
  > https://hl7.org/fhir/6.0.0-ballot4/valueset-research-study-party-role.html
  > The ValueSet was moved to THO
  > (http://terminology.hl7.org/ValueSet/research-study-party-role) but
  > the binding was not changed in time for the R6 ballot. The binding
  > should be changed and binding strength changed to Preferred."
  >
  > A reviewer comment notes: "when changed, this will complete
  > resolution of FHIR-50461 (Add data-monitoring to
  > ResearchStudyPartyRole CodeSystem)."

- **Disposition summary:** Re-point the `associatedParty.role` binding
  at the THO-hosted `research-study-party-role` ValueSet and tighten
  the strength from Example to Preferred, completing the THO migration
  that was in flight at ballot4. Side effect: this also closes out
  FHIR-50461.
- **Commits applying this ticket:**
  - [`138abc2fcfde`](https://github.com/HL7/fhir/commit/138abc2fcfde82ff9ddb74e31c78bfbe4c1ee016) — J#53696 Changed binding to THO-defined ValueSet with Preferred binding strength. (2026-04-02)
- **Changes applied (per Step 5b, scoped to this artifact):** On
  `ResearchStudy.associatedParty.role` in the SD differential, the
  binding `strength` changed from `example` to `preferred`, the
  `description` changed from the placeholder `"desc."` to `"This is a
  ResearchStudy's party role."`, and the `valueSet` reference changed
  from `http://hl7.org/fhir/ValueSet/research-study-party-role` to
  `http://terminology.hl7.org/ValueSet/research-study-party-role`. The
  ctgov example was correspondingly updated to reference
  `http://terminology.hl7.org/CodeSystem/research-study-party-role`
  (instead of `http://hl7.org/fhir/research-study-party-role`) for its
  three associatedParty `role.coding.system` values.

### [FHIR-53697](https://jira.hl7.org/browse/FHIR-53697) — Change binding for ResearchStudy.progressStatus.state

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The change request body
  > states: "ResearchStudy.progressStatus.state has Example binding to
  > https://hl7.org/fhir/6.0.0-ballot4/valueset-research-study-status.html
  > The ValueSet was moved to THO
  > (http://terminology.hl7.org/ValueSet/research-study-status) but the
  > binding was not changed in time for the R6 ballot. The binding
  > should be changed and binding strength changed to Preferred."

- **Disposition summary:** Re-point `progressStatus.state` at the
  THO-hosted `research-study-status` ValueSet and tighten the strength
  from Example to Preferred, completing the THO migration. Resolution
  is "Persuasive with Modification" — the as-applied change matches the
  body, so the modification is presumed editorial.
- **Commits applying this ticket:**
  - [`8ba6eab23c24`](https://github.com/HL7/fhir/commit/8ba6eab23c248e13e6e6214fa9f73eaf2e0e8eca) — J#53697 Changed ResearchStudy.progressStatus.state binding to THO-defined ValueSet with Preferred binding strength. (2026-04-02)
- **Changes applied (per Step 5b, scoped to this artifact):** On
  `ResearchStudy.progressStatus.state` in the SD differential, the
  binding `strength` changed from `example` to `preferred`, the
  `description` changed from the placeholder `"defn."` to `"Codes that
  convey the current status of the research study."`, and the
  `valueSet` reference changed from
  `http://hl7.org/fhir/ValueSet/research-study-status` to
  `http://terminology.hl7.org/ValueSet/research-study-status`. The
  ctgov example was updated to reference
  `http://terminology.hl7.org/CodeSystem/research-study-status` for its
  two `progressStatus.state.coding.system` values.

### [FHIR-53698](https://jira.hl7.org/browse/FHIR-53698) — Change binding for ResearchStudy.studyDesign

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The change request body
  > states: "ResearchStudy.studyDesign has Preferred binding to
  > https://hl7.org/fhir/6.0.0-ballot4/valueset-study-design.html. The
  > ValueSet was moved to THO
  > (http://terminology.hl7.org/ValueSet/study-design) but the binding
  > was not changed in time for the R6 ballot. The binding should be
  > changed. When done, this will resolve FHIR-39003 and FHIR-39004."

- **Disposition summary:** Re-point `ResearchStudy.studyDesign` at the
  THO-hosted `study-design` ValueSet (strength stays Preferred). Closing
  this also resolves FHIR-39003 and FHIR-39004.
- **Commits applying this ticket:**
  - [`28915130e7d5`](https://github.com/HL7/fhir/commit/28915130e7d5d94fff026bd5e5aa64da6a241480) — J#53698 Changed binding for ResearchStudy.studyDesign (2026-03-20)
- **Changes applied (per Step 5b, scoped to this artifact):** On
  `ResearchStudy.studyDesign` in the SD differential, the
  `valueSet` reference changed from
  `http://hl7.org/fhir/ValueSet/study-design` to
  `http://terminology.hl7.org/ValueSet/study-design`; strength
  (`preferred`) and description are unchanged. The orphaned
  artifact-scoped ValueSet
  `source/researchstudy/valueset-research-study-trial-phase.xml`
  (76 lines) was deleted in the same commit; it was unused after the
  THO re-pointing and is not referenced elsewhere in the resource.

### (unattributed)

- **Commits applying:**
  - [`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) — "Added a Ballot Note changes to the ResearchStudy introduction" (2026-04-10) — adds the existing `<blockquote class="ballot-note" id="bn1">` block (and an adjacent "Release Notes" blockquote) to `researchstudy-introduction.xml`. No Jira key is given in the message and the commit is not returned by `cross-referenced` for any of the six tickets.
  - [`b694f466cf85`](https://github.com/HL7/fhir/commit/b694f466cf85172849240bd786c97936056f9c87) — "updated the example to reflect the changes" (2026-04-10) — example tweak; the after-applied content is rolled into the FHIR-53692 example diff above.

## Roll-up Summary (after-applied state)

The window touched only **four** files; nothing changed under search
parameters, operations, examples list, IG companion, packs list, the
non-ctgov example, the supplementary notes, or any of the surviving
artifact-scoped ValueSets / CodeSystems.

- **StructureDefinition (`structuredefinition-ResearchStudy.xml`):**
  - `ResearchStudy.primaryPurposeType` is renamed to
    `ResearchStudy.purposeType` and widened from `0..1` to `0..*`; its
    binding strength is loosened from `preferred` to `example`
    (bindingName, description, and ValueSet URL unchanged). Snapshot
    regeneration is required.
  - `ResearchStudy.studyDesign` binding `valueSet` is re-pointed from
    `http://hl7.org/fhir/ValueSet/study-design` to
    `http://terminology.hl7.org/ValueSet/study-design`; strength
    (`preferred`) is unchanged.
  - `ResearchStudy.associatedParty.role` binding `valueSet` is
    re-pointed from
    `http://hl7.org/fhir/ValueSet/research-study-party-role` to
    `http://terminology.hl7.org/ValueSet/research-study-party-role`;
    strength tightened from `example` to `preferred`; description
    rewritten from `"desc."` to `"This is a ResearchStudy's party
    role."`.
  - `ResearchStudy.progressStatus.state` binding `valueSet` is
    re-pointed from
    `http://hl7.org/fhir/ValueSet/research-study-status` to
    `http://terminology.hl7.org/ValueSet/research-study-status`;
    strength tightened from `example` to `preferred`; description
    rewritten from `"defn."` to `"Codes that convey the current status
    of the research study."`.
  - New element `ResearchStudy.comparisonGroup.name` (`0..1 string`,
    short "A simple label for the comparison Group") added to the
    differential.
  - `ResearchStudy.result` Reference target list extends to include
    `DocumentReference` (now `Composition | DiagnosticReport |
    DocumentReference | Evidence`).
- **Intro / narrative (`researchstudy-introduction.xml`):**
  - A new `<blockquote class="ballot-note" id="bn1">` and an adjacent
    "Release Notes" blockquote (linking the six tickets above) were
    inserted at the top of the introduction. No other narrative changes.
  - `researchstudy-notes.xml` is unchanged.
- **Search parameters (`bundle-ResearchStudy-search-params.xml`):** No
  changes.
- **Operations (`list-ResearchStudy-operations.xml`):** No changes.
- **Examples:**
  - `researchstudy-example-ctgov-study-record.xml`: renamed
    `<primaryPurposeType>` → `<purposeType>`; `progressStatus.state`
    coding `system`s re-pointed to
    `http://terminology.hl7.org/CodeSystem/research-study-status`;
    `associatedParty.role` coding `system`s re-pointed to
    `http://terminology.hl7.org/CodeSystem/research-study-party-role`.
  - `researchstudy-example.xml` — no changes (note: this example does
    not yet exercise `purposeType`, `comparisonGroup.name`,
    `studyDesign`, or `result` with the new shapes — see "Notes for
    Reviewer").
  - `list-ResearchStudy-examples.xml` — no entries added or removed.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - `valueset-research-study-trial-phase.xml` was deleted as part of
    the studyDesign re-pointing (FHIR-53698). No other artifact-scoped
    ValueSet or CodeSystem was added, removed, or modified in the
    window. The three new THO bindings (`research-study-party-role`,
    `research-study-status`, `study-design`) live in HL7/UTG; they are
    out of this artifact's scope but flagged here as cross-repo touch
    points.

## Proposed Ballot Note (HTML)

The proposed note revises the existing `bn1` block. Compared with the
current text it (a) preserves the `id`, (b) tightens wording to reflect
what actually landed (e.g., `purposeType` strength is **example**, not
Preferred — the `b694f466` example update did not change strength;
`primaryPurposeType` was *renamed* to `purposeType`, not added
alongside; `comparisonGroup.name` is on `comparisonGroup`, not the
top-level resource), (c) uses one bullet per change with inline Jira
links, and (d) removes the duplicated trailing period in the previous
text. The "Release Notes" blockquote that currently sits beside `bn1`
is editorial and may be retained or removed independently of the
ballot-note revision; it is not part of the proposed note.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Since FHIR 6.0.0-ballot4, ResearchStudy
  has had a small set of substantive model changes (driven primarily
  by EBM-on-FHIR and EU CTIS use cases) and a coordinated migration of
  three bindings to HL7 Terminology (THO):</p>
  <ul>
    <li>Renamed <code>ResearchStudy.primaryPurposeType</code> (0..1) to
        <code>ResearchStudy.purposeType</code> (0..*) so a study can
        declare more than one intent; the binding now uses
        <em>example</em> strength against the existing
        <code>research-study-prim-purp-type</code> ValueSet pending
        publication of the BRR-defined THO ValueSet
        (<a href="https://jira.hl7.org/browse/FHIR-53692">FHIR-53692</a>).</li>
    <li>Added <code>ResearchStudy.comparisonGroup.name</code>
        (0..1 string) so implementers can attach a simple label to a
        comparison group without inventing ad-hoc encodings
        (<a href="https://jira.hl7.org/browse/FHIR-53693">FHIR-53693</a>).</li>
    <li>Added <code>DocumentReference</code> to the allowed target
        types of <code>ResearchStudy.result</code>, restoring the
        ability to point at an externally hosted citation/document now
        that <code>Citation</code> has moved to Additional Resources
        (<a href="https://jira.hl7.org/browse/FHIR-53694">FHIR-53694</a>).</li>
    <li>Re-pointed <code>ResearchStudy.studyDesign</code> at the THO
        ValueSet
        <code>http://terminology.hl7.org/ValueSet/study-design</code>
        (strength remains <em>preferred</em>); the orphaned local
        <code>research-study-trial-phase</code> ValueSet has been
        removed
        (<a href="https://jira.hl7.org/browse/FHIR-53698">FHIR-53698</a>).</li>
    <li>Re-pointed <code>ResearchStudy.associatedParty.role</code> at
        the THO ValueSet
        <code>http://terminology.hl7.org/ValueSet/research-study-party-role</code>
        and tightened the binding strength from <em>example</em> to
        <em>preferred</em>
        (<a href="https://jira.hl7.org/browse/FHIR-53696">FHIR-53696</a>).</li>
    <li>Re-pointed <code>ResearchStudy.progressStatus.state</code> at
        the THO ValueSet
        <code>http://terminology.hl7.org/ValueSet/research-study-status</code>
        and tightened the binding strength from <em>example</em> to
        <em>preferred</em>
        (<a href="https://jira.hl7.org/browse/FHIR-53697">FHIR-53697</a>).</li>
  </ul>
  <p>Balloters are asked to confirm the rename of
  <code>primaryPurposeType</code> &rarr; <code>purposeType</code> and
  the widened cardinality, and to flag any implementations affected by
  the three THO binding moves.</p>
</blockquote>
```

## Notes for Reviewer

- **Strength discrepancy on `purposeType` (FHIR-53692).** The Jira
  request asked for a *Preferred* binding to a forthcoming
  THO-hosted `ResearchStudyPurposeType` ValueSet. What landed in the
  SD is `strength=example` against the existing pre-purp-type
  ValueSet. The commit subject explicitly states "and example
  binding strength," so this appears intentional pending creation of
  the THO ValueSet, but the proposed ballot note calls this out so
  balloters can decide whether the as-applied state matches BRR's
  intent.
- **Existing ballot-note bullets reconciled.** All six bullets in the
  current `bn1` block correspond to changes that are still present in
  the after-applied state, so all six were carried forward (with
  wording tightened). No bullets were dropped because of reverts or
  supersession.
- **Adjacent "Release Notes" blockquote.** The
  `<blockquote style="background-color: lightblue">` block listing the
  six FHIR tickets was added in the same commit as `bn1` but is not
  marked `class="ballot-note"`. It is left untouched by the proposed
  revision; the editor can keep or remove it independently.
- **Examples coverage gap.** Only
  `researchstudy-example-ctgov-study-record.xml` was updated to follow
  the new element/CodeSystem shapes. `researchstudy-example.xml` does
  not exercise `comparisonGroup.name`, `result` with a
  `DocumentReference`, or `purposeType` with multiple codings, so the
  new shape is undemonstrated in that example. This is informational —
  not a blocker for the ballot note.
- **Cross-repo touch points (HL7/UTG).** The three new bindings rely on
  ValueSets/CodeSystems hosted under
  `http://terminology.hl7.org/...`. Per the FhirCore briefing's
  cross-repo notes, balloters reviewing terminology should confirm the
  matching THO definitions are available at publication time.
- **Unattributed commits.** Commit `9c7e502982ab` (the in-window add of
  the existing ballot note) and `b694f466cf85` (an example tweak rolled
  into FHIR-53692's after-applied state) carry no `J#` reference and
  are not returned by `cross-referenced`. They are listed under
  "(unattributed)" above and folded into the roll-up.
- **No fallback to `gh` was needed.** The since-commit
  (`5d67a34a13a5`) is reachable from HEAD (`db79dcdfe196`) in the
  cached clone (fast-forward), so all diffs and metadata came from
  `git` against `cache/github/repos/HL7_fhir/clone`.
- **Briefing currency.** `meta.json` records `clone_head_sha =
  1b369ff4e28e` (analyzed 2026-04-20); cache HEAD is `db79dcdfe196`. No
  ResearchStudy files have changed between the briefing's clone HEAD
  and the current HEAD (`git log 1b369ff4e28e..HEAD -- source/researchstudy/`
  is empty), so the briefing's Artifact Map is current for this
  artifact.

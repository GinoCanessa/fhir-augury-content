# Artifact Ballot Note Draft: Evidence (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Evidence` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `Evidence` for this run (resolved against the FhirCore briefing's authoring layout under `source/evidence/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/evidence/structuredefinition-Evidence.xml` | StructureDefinition (canonical) | yes |
| `source/evidence/evidence-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/evidence/evidence-notes.xml` | Supplementary narrative | no |
| `source/evidence/bundle-Evidence-search-params.xml` | Search parameters | no |
| `source/evidence/list-Evidence-operations.xml` | Operations | no |
| `source/evidence/list-Evidence-examples.xml` | Examples list | no |
| `source/evidence/list-Evidence-packs.xml` | Packs list | no |
| `source/evidence/evidence-example.xml` | Example | no |
| `source/evidence/evidence-example-ASTRAL-12-alteplase-mRS3-6.xml` | Example | no |
| `source/evidence/evidence-example-death-or-major-injury-reduce-parachute-vs-empty-backpack.xml` | Example | no |
| `source/evidence/evidence-example-quoted-source.xml` | Example | no |
| `source/evidence/evidence-example-statistic-model-include-if.xml` | Example | no |
| `source/evidence/evidence-example-stroke-0-3-alteplase-vs-no-alteplase-mRS3-6.xml` | Example | no |
| `source/evidence/evidence-example-stroke-3-4half-alteplase-vs-no-alteplase-mRS0-2.xml` | Example | no |
| `source/evidence/evidence-example-stroke-alteplase-fatalICH.xml` | Example | no |
| `source/evidence/evidence-example-stroke-no-alteplase-fatalICH.xml` | Example | no |
| `source/evidence/evidence-examples-header.xml` | Examples header | no |
| `source/evidence/evidence-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/evidence/codesystem-variable-role.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/evidence/valueset-variable-role.xml` | Artifact-scoped ValueSet (1) | no |

Patterns from the briefing that produced no match in the clone:

- `source/evidence/evidence-spreadsheet.xml` — no legacy spreadsheet exists for Evidence; the StructureDefinition is authoritative.
- Sibling `structuredefinition-*.xml` other than the canonical — none ship alongside `Evidence` in this folder.

## Current Ballot Note

Located at HEAD in `source/evidence/evidence-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> The key changes made since FHIR 6.0.0-ballot4 include:</p>
<p>Changed the Evidence.studyDesign ValueSet binding to be HL7 Terminology, and removed the FHIR version of the StudyDesign ValueSet.</p>
</blockquote>
<blockquote style="background-color: lightblue">
<p><b>Release Notes:</b></p>
<ul>
<li><a href="https://jira.hl7.org/browse/FHIR-53699">FHIR-53699</a></li>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53699](https://jira.hl7.org/browse/FHIR-53699) | Change binding for Evidence.studyDesign | [`6031e9a1e8a2`](https://github.com/HL7/fhir/commit/6031e9a1e8a227298aadc16add0c4375abfa5535) |
| (unattributed) | Ballot-note narrative additions for Evidence intro (related to FHIR-53699 but not tagged) | [`cad5560571b3`](https://github.com/HL7/fhir/commit/cad5560571b376162700d37bd100f11e897f5246), [`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) |

## Per-Ticket Detail

### [FHIR-53699](https://jira.hl7.org/browse/FHIR-53699) — Change binding for Evidence.studyDesign

- **Work group:** Clinical Decision Support
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The two recorded comments only reference the implementing pull request ([HL7/fhir#4035](https://github.com/HL7/fhir/pull/4035)); no narrative disposition was captured.

- **Disposition summary:** The ticket reported that the `Evidence.studyDesign` extensible binding still pointed at the FHIR-hosted ValueSet (`http://hl7.org/fhir/ValueSet/study-design`) even though the canonical ValueSet had been moved to HL7 Terminology (THO) at `http://terminology.hl7.org/ValueSet/study-design`. The applied disposition is to repoint the binding at the THO ValueSet so the FHIR core specification consumes the THO copy directly, and to retire the FHIR-resident copy.
- **Commits applying this ticket:**
  - [`6031e9a1e8a2`](https://github.com/HL7/fhir/commit/6031e9a1e8a227298aadc16add0c4375abfa5535) — J#53699 Changed binding for Evidence.studyDesign to THO (2026-03-20)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-Evidence.xml`, the `<binding>` on `Evidence.studyDesign` keeps `strength="extensible"` and the same description, but its `<valueSet>` reference is repointed from `http://hl7.org/fhir/ValueSet/study-design` to `http://terminology.hl7.org/ValueSet/study-design`. No other elements, cardinalities, types, or constraints in the SD differential were touched. The retirement of the FHIR-resident `ValueSet/study-design` is realised outside this artifact's file set (it lived under `source/valuesets/` / cross-repo with UTG); no `valueset-study-design.xml` exists under `source/evidence/`, so this artifact's roll-up only sees the binding URL change. Snapshot regeneration is required to propagate the new ValueSet reference into `<snapshot>`.

### (unattributed) — Ballot-note narrative additions for Evidence intro

- **Commits in window with no ticket key in the message and no `cross-referenced` hits:**
  - [`cad5560571b3`](https://github.com/HL7/fhir/commit/cad5560571b376162700d37bd100f11e897f5246) — Added a Ballot Note changes to the Evidence introduction (2026-04-10)
  - [`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) — Added a Ballot Note changes to the ResearchStudy introduction (2026-04-10) — *commit subject names ResearchStudy but the diff also adjusts one line in `evidence-introduction.xml`; see Notes for Reviewer.*
- **Changes applied (scoped to this artifact):** `cad5560` introduces the `<blockquote class="ballot-note" id="bn1">` block (and the adjacent light-blue Release Notes blockquote that links FHIR-53699) into `evidence-introduction.xml`, immediately above the `<a name="scope"></a>` anchor. `9c7e502` then refines the bullet wording inside that same blockquote, extending the sentence from *"Changed the Evidence.studyDesign ValueSet binding to be HL7 Terminology."* to *"Changed the Evidence.studyDesign ValueSet binding to be HL7 Terminology, and removed the FHIR version of the StudyDesign ValueSet."* These are pure narrative edits documenting the FHIR-53699 change; they do not alter any conformance content. They are listed as unattributed because the commit messages do not carry a `J#…` / `FHIR-…` token and `cross-referenced` returned no hits, but functionally they belong with FHIR-53699.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a13a5..db79dcdf -- <Evidence file set>` (`evidence-introduction.xml` +10/-0; `structuredefinition-Evidence.xml` +1/-1).

- **StructureDefinition (`structuredefinition-Evidence.xml`):**
  - `Evidence.studyDesign` binding: `valueSet` reference changed from `http://hl7.org/fhir/ValueSet/study-design` to `http://terminology.hl7.org/ValueSet/study-design`. Strength remains `extensible`; description (`"This is a set of terms for study design characteristics."`) is unchanged. Snapshot regeneration is required so `<snapshot>` mirrors the new canonical.
  - No other element additions, removals, cardinality, type, profile, or constraint changes in the differential.
- **Intro / narrative (`evidence-introduction.xml`):**
  - A new `<blockquote class="ballot-note" id="bn1">` was added at the top of the intro, calling out the change since FHIR 6.0.0-ballot4 to the `Evidence.studyDesign` binding and the retirement of the FHIR-resident StudyDesign ValueSet.
  - A new `<blockquote style="background-color: lightblue">` Release Notes block was added immediately after, listing FHIR-53699.
  - No changes to the Scope and Usage, Boundaries and Relationships, or other narrative paragraphs.
- **Supplementary narrative (`evidence-notes.xml`):** No changes.
- **Search parameters (`bundle-Evidence-search-params.xml`):** No changes (no entries added, removed, or modified).
- **Operations (`list-Evidence-operations.xml`):** No changes.
- **Examples (`list-Evidence-examples.xml`, `evidence-example*.xml`, `evidence-examples-header.xml`):** No changes; no examples added or removed. Existing examples were not re-rendered for the binding change because the binding URL is metadata only and does not invalidate the example payloads.
- **Terminology (sibling `valueset-variable-role.xml`, `codesystem-variable-role.xml`):** No changes inside this artifact's folder. The retired `ValueSet/study-design` lives outside this artifact's file set (cross-repo touchpoint with UTG / `source/valuesets/`); flag for the FhirCore ↔ UTG reviewer.
- **Other files in the file set (`list-Evidence-packs.xml`, `evidence-fivews-mapping-exceptions.xml`):** No changes.

## Proposed Ballot Note (HTML)

The existing `id="bn1"` is preserved. The existing bullet about the StudyDesign binding move is retained verbatim (it is still accurate in the after-applied state) and is now expressed as a list item with an inline Jira citation, matching the other resources' ballot-note style. The companion light-blue Release Notes blockquote is left in place as a separate block (it is not part of the ballot-note blockquote per repo convention).

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The key changes made to Evidence since FHIR 6.0.0-ballot4 are scoped to terminology alignment; no element-level structural changes were made.</p>
  <ul>
    <li>Repointed the extensible binding on <code>Evidence.studyDesign</code> from the FHIR-resident <code>ValueSet/study-design</code> to the HL7 Terminology copy at <code>http://terminology.hl7.org/ValueSet/study-design</code>, and retired the FHIR version of the StudyDesign ValueSet (<a href="https://jira.hl7.org/browse/FHIR-53699">FHIR-53699</a>).</li>
  </ul>
</blockquote>
<blockquote style="background-color: lightblue">
  <p><b>Release Notes:</b></p>
  <ul>
    <li><a href="https://jira.hl7.org/browse/FHIR-53699">FHIR-53699</a></li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The current ballot note's substance was carried forward unchanged because the change it describes (the studyDesign binding move to THO) is still present in the after-applied diff. The wording was tightened into a bulleted list with an inline Jira citation to match the per-bullet style used by other R6 resources; reviewers who prefer the narrower prose form should keep the original `<p>` rather than the proposed `<ul>`.
- Commit [`9c7e502`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) has the subject *"Added a Ballot Note changes to the ResearchStudy introduction"* but its diff also touches `source/evidence/evidence-introduction.xml`, refining the bullet wording for the studyDesign change. The commit subject appears to misname the artifact; the Evidence-side edit is small and clearly a follow-up to `cad5560`. ResearchStudy reviewers should expect the larger half of that commit (the `+20` lines added to `source/researchstudy/researchstudy-introduction.xml`) on their side.
- Both ballot-note commits (`cad5560`, `9c7e502`) are unattributed: their messages do not carry `J#…` / `FHIR-…` tokens and `fhir-augury-cli cross-referenced` returned zero hits for both SHAs. They are functionally part of the FHIR-53699 disposition (documenting it in the intro narrative) and have been grouped with that ticket in the Roll-up summary and proposed ballot note.
- FHIR-53699's Jira disposition text is not recorded — the only comments are PR links to [HL7/fhir#4035](https://github.com/HL7/fhir/pull/4035). The disposition summary above is reconstructed from the ticket description and the after-applied diff; reviewers may wish to confirm against the work-group minutes.
- The retirement of the FHIR-resident `ValueSet/study-design` is a cross-repo / cross-artifact touchpoint (FHIR core `source/valuesets/` and HL7 UTG). It is mentioned in the ballot note for completeness but is not visible inside the `Evidence` file set itself.
- HEAD (`db79dcdfe196d35bd0e74c58c655a4c1c8f534f7`) is a descendant of the since-commit (`5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd`); no symmetric-difference fallback was needed. No `gh api` calls were required — all commits resolved against the cached clone.

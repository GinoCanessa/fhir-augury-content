# Artifact Ballot Note Draft: Evidence (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Evidence` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `Evidence` for this run (resolved against
`source/evidence/` in the cached clone, per the FhirCore briefing's
Artifact Map convention):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/evidence/structuredefinition-Evidence.xml` | StructureDefinition (canonical) | yes |
| `source/evidence/evidence-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/evidence/evidence-notes.xml` | Supplementary narrative | no |
| `source/evidence/bundle-Evidence-search-params.xml` | Search parameters bundle | no |
| `source/evidence/list-Evidence-operations.xml` | Operations list | no |
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
| `source/evidence/evidence-examples-header.xml` | Examples header narrative | no |
| `source/evidence/evidence-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/evidence/codesystem-variable-role.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/evidence/valueset-variable-role.xml` | Artifact-scoped ValueSet (1) | no |

Patterns from the standard FhirCore artifact pattern set that produced no match in `source/evidence/`:
- `source/evidence/structuredefinition-evidence-spreadsheet.xml` (legacy spreadsheet) — no file matched.
- Sibling `structuredefinition-*.xml` profile artifacts beyond the canonical SD — none present.

## Current Ballot Note

The current intro file at HEAD already carries a ballot note added inside
the window. It is reproduced here verbatim:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> The key changes made since FHIR 6.0.0-ballot4 include:</p>
<p>Changed the Evidence.studyDesign ValueSet binding to be HL7 Terminology, and removed the FHIR version of the StudyDesign ValueSet.</p>
</blockquote>
```

(There is also a sibling `<blockquote style="background-color: lightblue">`
"Release Notes" block listing FHIR-53699 — that is a release-notes
companion, not a ballot note, and is preserved as-is.)

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53699](https://jira.hl7.org/browse/FHIR-53699) | Change binding for Evidence.studyDesign | [`6031e9a1e8a2`](https://github.com/HL7/fhir/commit/6031e9a1e8a227298aadc16add0c4375abfa5535) |
| (unattributed) | — | [`cad5560571b3`](https://github.com/HL7/fhir/commit/cad5560571b376162700d37bd100f11e897f5246), [`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) |

## Per-Ticket Detail

### [FHIR-53699](https://jira.hl7.org/browse/FHIR-53699) — Change binding for Evidence.studyDesign

- **Work group:** Clinical Decision Support
- **Specification:** FHIR Core (FHIR)
- **Resolution:** Persuasive (status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira as a separate applied-vote
  > comment. The two ticket comments simply link the implementing PR
  > (`https://github.com/HL7/fhir/pull/4035`). The ticket description
  > states: "Evidence.studyDesign has Extensible binding to
  > `https://hl7.org/fhir/6.0.0-ballot4/valueset-study-design.html`.
  > The ValueSet was moved to THO
  > (`http://terminology.hl7.org/ValueSet/study-design`) but the
  > binding was not changed in time for the R6 ballot. The binding
  > should be changed."

- **Disposition summary:** The work group accepted the request as
  Persuasive: re-point the extensible binding on
  `Evidence.studyDesign` from the ballot-version FHIR-hosted ValueSet
  to the HL7 Terminology (THO) canonical that now owns the value set,
  and retire the FHIR-side copy of `study-design`.
- **Commits applying this ticket:**
  - [`6031e9a1e8a2`](https://github.com/HL7/fhir/commit/6031e9a1e8a227298aadc16add0c4375abfa5535) — J#53699 Changed binding for Evidence.studyDesign to THO (2026-03-20)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-Evidence.xml`, the binding `valueSet` URL on
  `Evidence.studyDesign` is changed from
  `http://hl7.org/fhir/ValueSet/study-design` to
  `http://terminology.hl7.org/ValueSet/study-design`. Binding strength
  remains `extensible`; description and bound element are unchanged.
  No accompanying change to a sibling `valueset-study-design.xml`
  appears in `source/evidence/` because the FHIR-side copy lived
  outside this artifact's folder; its retirement is recorded in the
  ballot note (see "(unattributed)" below) but the file deletion is
  outside the Evidence artifact's file scope.

### (unattributed) — ballot-note narrative for the studyDesign rebinding

These two commits do not carry a `FHIR-XXXXX` key in the subject/body
and have no FhirAugury cross-reference hits, but their content is a
narrative companion to FHIR-53699 (they author and then refine the
ballot-note paragraph that describes that change).

- **Commits:**
  - [`cad5560571b3`](https://github.com/HL7/fhir/commit/cad5560571b376162700d37bd100f11e897f5246) — Added a Ballot Note changes to the Evidence introduction (2026-04-10)
  - [`9c7e502982ab`](https://github.com/HL7/fhir/commit/9c7e502982ab12c2a0c4d18cbdd1408603f83064) — Added a Ballot Note changes to the ResearchStudy introduction (2026-04-10) — despite the subject, this commit also touches `evidence-introduction.xml`.
- **Changes applied:** `cad5560571b3` inserts a new
  `<blockquote class="ballot-note" id="bn1">` ahead of `<a name="scope">`
  in `evidence-introduction.xml` with the text *"Changed the
  Evidence.studyDesign ValueSet binding to be HL7 Terminology."*, plus
  a sibling lightblue "Release Notes" block linking
  [FHIR-53699](https://jira.hl7.org/browse/FHIR-53699).
  `9c7e502982ab` then revises the single sentence inside that ballot
  note to add *", and removed the FHIR version of the StudyDesign
  ValueSet."* — i.e., it broadens the ballot-note text to also flag
  the retirement of the FHIR-hosted `study-design` ValueSet. No other
  Evidence-scoped files are touched by these commits.

## Roll-up Summary (after-applied state)

The window touches only two files in the Evidence artifact's scope.

- **StructureDefinition (`structuredefinition-Evidence.xml`):** The
  extensible binding on `Evidence.studyDesign` is re-pointed from the
  FHIR-hosted ValueSet
  `http://hl7.org/fhir/ValueSet/study-design` to the HL7
  Terminology canonical
  `http://terminology.hl7.org/ValueSet/study-design`. Binding
  `strength` (`extensible`) and the human-readable `description` are
  unchanged. No element additions, removals, cardinality, type, or
  constraint changes; no other bindings move. Snapshot regeneration
  is required because the binding ValueSet URL is differential.
- **Intro / narrative (`evidence-introduction.xml`):** A new ballot
  note (`<blockquote class="ballot-note" id="bn1">`) is added that
  flags the studyDesign rebinding and the retirement of the FHIR-side
  StudyDesign ValueSet, plus a sibling lightblue "Release Notes"
  block linking FHIR-53699. No other narrative content (Scope,
  Boundaries, etc.) is changed.
- **Notes (`evidence-notes.xml`):** unchanged.
- **Search parameters (`bundle-Evidence-search-params.xml`):** unchanged
  — no entries added, removed, or modified.
- **Operations (`list-Evidence-operations.xml`):** unchanged.
- **Examples (`list-Evidence-examples.xml`, `evidence-example*.xml`):**
  unchanged — no examples added, removed, or updated. The studyDesign
  binding change is non-breaking for the existing examples (no example
  uses a `studyDesign` code that was unique to the FHIR-side copy).
- **Terminology (`codesystem-variable-role.xml`,
  `valueset-variable-role.xml`):** unchanged. The studyDesign
  ValueSet itself is not under `source/evidence/`; its FHIR-side
  retirement (called out in the ballot note) is recorded in another
  area of the spec and is outside this artifact's file scope.

## Proposed Ballot Note (HTML)

The existing single-bullet ballot note is still accurate against the
after-applied state, so the proposed note carries it forward — minor
copy-edits only — and adds an inline Jira citation tying the bullet
to the underlying ticket.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The key changes made since FHIR 6.0.0-ballot4 include:</p>
  <ul>
    <li>The extensible binding on <code>Evidence.studyDesign</code> has been re-pointed from the FHIR-hosted <code>study-design</code> ValueSet to the HL7 Terminology (THO) canonical <code>http://terminology.hl7.org/ValueSet/study-design</code>, and the FHIR-side copy of the StudyDesign ValueSet has been retired (<a href="https://jira.hl7.org/browse/FHIR-53699">FHIR-53699</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The existing `id="bn1"` is preserved.
- The two ballot-note narrative commits (`cad5560571b3`,
  `9c7e502982ab`) do not carry a Jira key in their commit message and
  are not cross-referenced from FhirAugury, so they appear as
  "(unattributed)" in the table above. Their content is, in
  substance, the ballot-note write-up for FHIR-53699; reviewers may
  wish to retro-link them in Jira if precise commit attribution is
  desired.
- The sibling lightblue "Release Notes" block that lists FHIR-53699
  is not part of the ballot note (different `class`), and is left
  intact by the proposed change.
- The retirement of the FHIR-hosted `valueset-study-design` ValueSet
  is mentioned in the ballot note but the file itself is not under
  `source/evidence/`; the deletion lives elsewhere in the spec source
  tree and is therefore not enumerated in the Roll-up Summary above.
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit
  `5d67a34a13a5` ("bump version for publication"), so a fast-forward
  diff was used; no symmetric-difference fallback was needed.
- All FhirAugury, `git`, and ticket calls succeeded; no `gh api`
  fallback was required.

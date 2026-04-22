# Artifact Ballot Note Draft: Ingredient (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Ingredient` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `Ingredient` for this run (FhirCore folder
`source/ingredient/`; the briefing's Artifact Map does not enumerate
per-resource paths so the standard FhirCore patterns from the
`notes-artifact` skill were applied):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/ingredient/structuredefinition-Ingredient.xml` | StructureDefinition (canonical) | yes |
| `source/ingredient/ingredient-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/ingredient/ingredient-notes.xml` | Supplementary narrative | no |
| `source/ingredient/bundle-Ingredient-search-params.xml` | Search parameters bundle | no |
| `source/ingredient/list-Ingredient-operations.xml` | Operations list | no |
| `source/ingredient/list-Ingredient-examples.xml` | Examples list | no |
| `source/ingredient/list-Ingredient-packs.xml` | Profile / pack list | no |
| `source/ingredient/ingredient-example.xml` | Example (canonical) | no |
| `source/ingredient/ingredient-example-strength-repeat.xml` | Example (strength repeat) | no |
| `source/ingredient/ingredient-examples-header.xml` | Examples table header | no |
| `source/ingredient/ingredient-fivews-mapping-exceptions.xml` | Five-Ws mapping exceptions | no |
| `source/ingredient/valueset-ingredient-function.xml` | Artifact-scoped ValueSet | no |
| `source/ingredient/valueset-ingredient-manufacturer-role.xml` | Artifact-scoped ValueSet | no |
| `source/ingredient/valueset-ingredient-role.xml` | Artifact-scoped ValueSet | no |
| `source/ingredient/codesystem-ingredient-function.xml` | Artifact-scoped CodeSystem | no |
| `source/ingredient/codesystem-ingredient-manufacturer-role.xml` | Artifact-scoped CodeSystem | no |
| `source/ingredient/codesystem-ingredient-role.xml` | Artifact-scoped CodeSystem | no |

Patterns from the FhirCore template that produced no match in the clone:

- `source/ingredient/Ingredient-spreadsheet.xml` — no legacy spreadsheet present (SD is authoritative).
- Sibling `structuredefinition-*.xml` for additional profiles — none ship alongside `Ingredient` in this folder.

## Current Ballot Note

A single ballot note exists in `source/ingredient/ingredient-introduction.xml` at HEAD (`db79dcdfe196`):

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since the last R6 ballot are:</p>
<ul>
<li>Updates to the following elements:</li>
<ul>
<li>Ingredient.identifier, which was made 0..* (previously 0..1)</li>
</ul>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55046](https://jira.hl7.org/browse/FHIR-55046) | Ingredient.identifier should repeat | [`284925a8ec84`](https://github.com/HL7/fhir/commit/284925a8ec842d466286856c9031e900e8cfd31c), [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) |

No unattributed commits — both commits in the window reference
`FHIR-55046` (the second commit also bundles introduction-text edits
for sibling resources under `FHIR-55057` / `FHIR-55053`, but those
edits land outside `source/ingredient/` and are therefore out of scope
for this artifact).

## Per-Ticket Detail

### [FHIR-55046](https://jira.hl7.org/browse/FHIR-55046) — Ingredient.identifier should repeat

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive (Resolved - change required)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

  (The ticket has no comments; the only narrative recorded against
  it is the imported reporter description below, attributed to
  Lloyd McKenzie as "Comment 12":
  *"Identifiers can almost always be assigned by multiple entities
  over time, but this element is not marked as repeating."*)

- **Disposition summary:** Reporter argued that, because identifiers
  for an Ingredient may be issued by multiple parties over time
  (manufacturer, regulator, dispenser, etc.), `Ingredient.identifier`
  should permit more than one value. The work group accepted this as
  Persuasive and resolved as "change required", i.e. relax the
  cardinality on `Ingredient.identifier` from `0..1` to `0..*`.
- **Commits applying this ticket:**
  - [`284925a8ec84`](https://github.com/HL7/fhir/commit/284925a8ec842d466286856c9031e900e8cfd31c) — FHIR-55046 Ingredient.identifier made 0..* (from 0..1) (2026-04-16T16:31:25+01:00, riksmithies)
  - [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) — resource introduction updates for FHIR-55057 / FHIR-55053 / FHIR-55046 (2026-04-16T19:28:02+01:00, riksmithies)
- **Changes applied (per Step 5b, scoped to this artifact):** The
  first commit changes `Ingredient.identifier`'s `<max>` from `1` to
  `*` in `structuredefinition-Ingredient.xml` (the differential entry
  for `Ingredient.identifier`). The second commit adds the matching
  ballot-note `<blockquote class="ballot-note" id="bn1">` to
  `ingredient-introduction.xml`, framing the resource as Normative-
  candidate for ballot and listing the `Ingredient.identifier`
  cardinality relaxation as the sole substantive change since the
  last R6 ballot. The `<short>`, `<definition>`, and `<type>` of the
  element are unchanged.

## Roll-up Summary (after-applied state)

Across `5d67a34a13a5..db79dcdfe196`, the after-applied diff for
`source/ingredient/` consists of exactly two file changes
(`+10` / `-1` lines total):

- **StructureDefinition (`structuredefinition-Ingredient.xml`):**
  - `Ingredient.identifier`: cardinality relaxed from `0..1` to
    `0..*` (`<max>` changed from `1` to `*`). The element's `<short>`,
    `<definition>`, type (`Identifier`), and any binding/constraints
    are untouched. No other elements were edited; only the
    `differential` was changed, so snapshot regeneration is required
    before publish.
- **Intro / narrative (`ingredient-introduction.xml`):**
  - A new `<blockquote class="ballot-note" id="bn1">` was added at
    the top of the Scope and Usage section, framing the resource as a
    Normative-status candidate and calling out the
    `Ingredient.identifier` cardinality change as the only
    substantive change since the previous R6 ballot.
- **Supplementary narrative (`ingredient-notes.xml`):** unchanged.
- **Search parameters (`bundle-Ingredient-search-params.xml`):**
  unchanged — no parameters added, removed, or modified.
- **Operations (`list-Ingredient-operations.xml`):** unchanged.
- **Examples (`list-Ingredient-examples.xml`,
  `ingredient-example*.xml`, `ingredient-examples-header.xml`):**
  unchanged — no example needed updating because the change is a
  cardinality relaxation (existing single-identifier examples remain
  valid).
- **Terminology (`valueset-ingredient-*.xml`,
  `codesystem-ingredient-*.xml`):** unchanged.
- **Five-Ws mapping (`ingredient-fivews-mapping-exceptions.xml`):**
  unchanged.

## Proposed Ballot Note (HTML)

The existing ballot note is still accurate against the after-applied
state — `Ingredient.identifier`'s cardinality change is the only
substantive change in the window. The proposal below preserves the
existing `id="bn1"`, retains the Normative-candidate framing, and
adds an inline Jira citation against the bullet so balloters can
trace it back to FHIR-55046. Nested `<ul>` is replaced with a flat
single-bullet list to avoid the existing markup's invalid `<ul>`
inside `<ul>` nesting.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The only substantive change since the last R6 ballot is:</p>
  <ul>
    <li><code>Ingredient.identifier</code> cardinality relaxed from <code>0..1</code> to <code>0..*</code>, allowing an Ingredient to carry identifiers issued by multiple parties (e.g. manufacturer, regulator) over time (<a href="https://jira.hl7.org/browse/FHIR-55046">FHIR-55046</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The existing ballot note's nested `<ul>` ("Updates to the following
  elements:" wrapping a single child `<ul>`) is not valid HTML; the
  proposed revision flattens it into a single `<li>` while preserving
  the same content. Reviewer may prefer to keep the nested style if
  more cardinality / element changes land before publication —
  re-introduce the wrapping bullet at that point.
- Commit `f0c7b541c736` also touches introduction files for
  `SubstanceDefinition` (FHIR-55057) and `RegulatedAuthorization`
  (FHIR-55053), but those edits live in `source/substancedefinition/`
  and `source/regulatedauthorization/` and so do not appear in the
  Ingredient roll-up. Those resources will need their own ballot-note
  refreshes via separate `notes-artifact` runs.
- `cross-referenced` returned no extra ticket links for either commit
  SHA; ticket attribution comes solely from the `FHIR-55046` markers
  in the commit subjects.
- The Jira ticket has no comments, so no verbatim disposition text
  was available; the disposition summary above is reconstructed from
  the imported reporter narrative and the recorded resolution
  (Persuasive — change required).
- Briefing snapshot (`clone_head_sha = 1b369ff4e28e`) is older than
  the current clone HEAD (`db79dcdfe196`); the FhirCore Artifact-Map
  patterns it documents still apply unchanged for `Ingredient`.

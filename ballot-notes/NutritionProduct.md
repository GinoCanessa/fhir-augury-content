# Artifact Ballot Note Draft: NutritionProduct (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `NutritionProduct` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 0 (250 commits in repo window; none touched `source/nutritionproduct/`) |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` (analysis) — current clone HEAD `db79dcdfe196` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `NutritionProduct` for this run (resolved from
the FhirCore convention `source/nutritionproduct/` since the briefing's
Artifact Map does not contain an explicit entry for this artifact):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/nutritionproduct/structuredefinition-NutritionProduct.xml` | StructureDefinition | no |
| `source/nutritionproduct/nutritionproduct-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/nutritionproduct/nutritionproduct-notes.xml` | Supplementary narrative | no |
| `source/nutritionproduct/bundle-NutritionProduct-search-params.xml` | Search parameters | no |
| `source/nutritionproduct/list-NutritionProduct-operations.xml` | Operations | no |
| `source/nutritionproduct/list-NutritionProduct-examples.xml` | Examples list | no |
| `source/nutritionproduct/list-NutritionProduct-packs.xml` | Packs list | no |
| `source/nutritionproduct/nutritionproduct-example.xml` | Example | no |
| `source/nutritionproduct/nutritionproduct-example-adultformula.xml` | Example | no |
| `source/nutritionproduct/nutritionproduct-example-apples.xml` | Example | no |
| `source/nutritionproduct/nutritionproduct-example-highprotein-enteral.xml` | Example | no |
| `source/nutritionproduct/nutritionproduct-example-peanutbutter.xml` | Example | no |
| `source/nutritionproduct/nutritionproduct-example-shake.xml` | Example | no |
| `source/nutritionproduct/nutritionproduct-examples-header.xml` | Examples header | no |
| `source/nutritionproduct/nutritionproduct-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | no |
| `source/nutritionproduct/codesystem-nutritionproduct-status.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/nutritionproduct/valueset-allergen-class.xml` | Artifact-scoped ValueSet | no |
| `source/nutritionproduct/valueset-measurement-property.xml` | Artifact-scoped ValueSet | no |
| `source/nutritionproduct/valueset-nutrient-code.xml` | Artifact-scoped ValueSet | no |
| `source/nutritionproduct/valueset-nutrition-product-category.xml` | Artifact-scoped ValueSet | no |
| `source/nutritionproduct/valueset-nutritionproduct-status.xml` | Artifact-scoped ValueSet | no |

Patterns from the briefing that produced no match in the clone:
- `source/nutritionproduct/structuredefinition-*.xml` (sibling profiles) — only the canonical SD exists; no extra profile artifacts ship alongside this resource.
- `source/nutritionproduct/nutritionproduct-spreadsheet.xml` — legacy spreadsheet not present (SD is authoritative).

## Current Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
  <ul>
    <li>Updated Boundaries and Relationships</li>
    <li>Added NutritionProduct.ingredientSummary</li>
    <li>Updated the NutritionProduct.ingredient backbone</li>
    <li>Update search parameters</li>
  </ul>
</blockquote>
```

## Tickets Applied in Window

No changes to artifact in window. No tickets attributable.

| Ticket | Title | Commits |
|--------|-------|---------|
| _(none)_ | _(no commits in window touched any NutritionProduct source file)_ | — |

## Per-Ticket Detail

No changes to artifact in window — no per-ticket detail to report.

## Roll-up Summary (after-applied state)

**No changes to artifact in window.** `git log 5d67a34a13a5..db79dcdfe196 -- source/nutritionproduct/` returns zero commits across all 21 NutritionProduct source files (StructureDefinition, intro/notes, search params bundle, operations list, examples list, packs list, all examples, the 5Ws mapping-exceptions overlay, and the artifact-scoped CodeSystem and ValueSets). The repo-wide window contains 250 non-merge commits, but none of them touched any path under `source/nutritionproduct/`.

- **StructureDefinition (`structuredefinition-NutritionProduct.xml`):** unchanged.
- **Intro / narrative (`nutritionproduct-introduction.xml`, `nutritionproduct-notes.xml`):** unchanged.
- **Search parameters (`bundle-NutritionProduct-search-params.xml`):** unchanged.
- **Operations (`list-NutritionProduct-operations.xml`):** unchanged.
- **Examples:** unchanged (six example instances and the examples header / packs / examples list files all untouched).
- **Terminology (sibling `valueset-*` / `codesystem-*`):** unchanged. No NutritionProduct-scoped ValueSet or CodeSystem was edited; if any related terminology moved to UTG in this window, it did so without a corresponding edit in the FhirCore source folder.

## Proposed Ballot Note (HTML)

Because nothing changed in the after-applied state, the existing ballot
note remains accurate and is carried forward verbatim (preserving
`id="bn1"`). No revision is proposed.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
  <ul>
    <li>Updated Boundaries and Relationships</li>
    <li>Added NutritionProduct.ingredientSummary</li>
    <li>Updated the NutritionProduct.ingredient backbone</li>
    <li>Update search parameters</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The since-commit `5d67a34a13a5` ("bump version for publication", 2025-12-18) is reachable from cache-clone HEAD `db79dcdfe196`; the window is a clean fast-forward range. 250 non-merge commits landed in that window across the repo, but `git log <since>..HEAD -- source/nutritionproduct/` returns nothing — the resource has not been edited since the publication-bump commit.
- The briefing's Artifact Map does not have an explicit entry for `NutritionProduct`; the file list above was derived from the FhirCore convention (`source/<lower-name>/`) and confirmed against the actual directory listing in the cache clone. All discovered files are reported in the Source Files table.
- No fall-back to `gh api` was required; everything was resolved from the cache clone via `git`.
- Reviewers may still want to verify whether NutritionProduct-relevant terminology has shifted in `HL7/UTG` in the same window; that is out of scope for this artifact-scoped run.

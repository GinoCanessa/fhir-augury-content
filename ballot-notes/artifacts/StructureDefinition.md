# Artifact Ballot Note Draft: StructureDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `StructureDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` (analyzed 2026-04-20) |
| Generated | 2026-04-21T20:00:00Z |

> **Window summary:** A single commit (`a9658ed9`) touched the artifact in this
> window, fixing a one-character typo in the `StructureDefinition.keyword`
> element definition (`nby` → `by`). No Jira ticket is attributable to the
> commit (no `FHIR-####` keys in the commit message and no cross-references
> recorded by FhirAugury). **No ballot-relevant changes have landed for the
> StructureDefinition resource since `5d67a34a13a5`.**

## Source Files

Files considered part of `StructureDefinition` for this run (folder
`source/structuredefinition/`, per the briefing's FhirCore Authoring root and
recommended change recipes):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/structuredefinition/structuredefinition-StructureDefinition.xml` | Canonical StructureDefinition (resource type) | yes |
| `source/structuredefinition/structuredefinition-introduction.xml` | Narrative intro (where ballot notes live) | no |
| `source/structuredefinition/structuredefinition-notes.xml` | Supplementary narrative | no |
| `source/structuredefinition/bundle-StructureDefinition-search-params.xml` | Search parameters bundle | no |
| `source/structuredefinition/list-StructureDefinition-operations.xml` | Operations list | no |
| `source/structuredefinition/list-StructureDefinition-examples.xml` | Examples list | no |
| `source/structuredefinition/list-StructureDefinition-packs.xml` | Profile packs list (resource-specific extra) | no |
| `source/structuredefinition/operationdefinition-StructureDefinition-snapshot.xml` | `$snapshot` OperationDefinition | no |
| `source/structuredefinition/codesystem-extension-context-type.xml` | Artifact-scoped CodeSystem | no |
| `source/structuredefinition/codesystem-structure-definition-kind.xml` | Artifact-scoped CodeSystem | no |
| `source/structuredefinition/codesystem-type-derivation-rule.xml` | Artifact-scoped CodeSystem | no |
| `source/structuredefinition/valueset-definition-use.xml` | Artifact-scoped ValueSet | no |
| `source/structuredefinition/valueset-extension-context-type.xml` | Artifact-scoped ValueSet | no |
| `source/structuredefinition/valueset-structure-definition-kind.xml` | Artifact-scoped ValueSet | no |
| `source/structuredefinition/valueset-type-derivation-rule.xml` | Artifact-scoped ValueSet | no |
| `source/structuredefinition/implementationguide-StructureDefinition-core.xml` | IG packaging for the core StructureDefinition profile pack | no |
| `source/structuredefinition/structuredefinition-example-composition.xml` | Profile example (Composition) | no |
| `source/structuredefinition/structuredefinition-example-section-library.xml` | Profile example (section library) | no |
| `source/structuredefinition/structuredefinition-example.xml` | Profile example (generic) | no |
| `source/structuredefinition/structuredefinition-examples-header.xml` | Examples header profile | no |
| `source/structuredefinition/structuredefinition-fivews-mapping-exceptions.xml` | Five-Ws mapping exceptions profile | no |

Notes on file selection:

- The briefing does not enumerate a per-artifact map for `StructureDefinition`;
  the file list above was derived by listing `source/structuredefinition/` in
  the cache clone and applying the FhirCore recipe patterns from the briefing.
- The folder also contains a vector image (`structuredefinition.svg`) and two
  publisher snapshot fixtures (`$snapshot-request.txt`,
  `$snapshot-response.txt`); these are non-authoring assets and were excluded
  from the diff scope.
- No legacy `structuredefinition-spreadsheet.xml` is present in this folder
  (the canonical SD is the sole source of truth for the resource shape, per
  the briefing's "spreadsheet vs. SD authority" gotcha).

Patterns from the briefing recipes that produced no match in this folder:

- `<resource>-spreadsheet.xml` — no match (no legacy spreadsheet).

## Current Ballot Note

No existing ballot note. `structuredefinition-introduction.xml` and
`structuredefinition-notes.xml` were searched at HEAD (`db79dcdf`) for any
`<blockquote class="ballot-note" …>` block; none were found.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

The single commit in the window has no `FHIR-####` reference in its message
(`typos and bump kindling`), and FhirAugury's `cross-referenced` lookup for
the SHA returned zero hits.

## Per-Ticket Detail

### (unattributed)

- **Commits:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — *typos and bump kindling* (Grahame Grieve, 2026-03-18T13:14:07+11:00)
- **Changes applied (per Step 5b, scoped to this artifact):** Editorial typo
  fix only. In
  `source/structuredefinition/structuredefinition-StructureDefinition.xml`,
  the differential `definition` text for
  `StructureDefinition.keyword` was corrected from
  `"…the use of this structure definition, or the content it describes."`
  with the typo `templates **nby** describing` to `templates **by**
  describing`. Diff stat: 1 file changed, 1 insertion(+), 1 deletion(-).
  The element remains marked `(DEPRECATED)` and the surrounding `<comment>`
  pointing implementers at the
  `http://hl7.org/fhir/StructureDefinition/artifact-topic` extension is
  unchanged. No semantic, cardinality, type, binding, constraint, narrative,
  search-parameter, operation, example, or terminology change was made.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a13a5..db79dcdf -- source/structuredefinition/`
(stat: 1 file, 1 insertion, 1 deletion).

- **StructureDefinition (`structuredefinition-StructureDefinition.xml`):**
  Typo correction in the `<definition>` text of
  `StructureDefinition.keyword` (`nby` → `by`). No element added, removed,
  renamed, retyped, or recardinalised; no binding, constraint, mapping, or
  modifier changes; no normative-status change; no `<differential>`
  structural changes. `<snapshot>` does not need to be regenerated for a
  text-only definition tweak (the publisher will refresh narrative as part
  of normal publication regardless).
- **Intro / narrative (`structuredefinition-introduction.xml`,
  `structuredefinition-notes.xml`):** Unchanged.
- **Search parameters (`bundle-StructureDefinition-search-params.xml`):**
  Unchanged.
- **Operations (`list-StructureDefinition-operations.xml`,
  `operationdefinition-StructureDefinition-snapshot.xml`):** Unchanged.
- **Examples (`list-StructureDefinition-examples.xml`,
  `structuredefinition-example*.xml`,
  `structuredefinition-examples-header.xml`,
  `structuredefinition-fivews-mapping-exceptions.xml`):** Unchanged.
- **Terminology (sibling `valueset-*` / `codesystem-*`,
  `implementationguide-StructureDefinition-core.xml`):** Unchanged. (No
  cross-repo terminology touch points triggered for UTG.)

## Proposed Ballot Note (HTML)

The only change in the window is an editorial typo fix with no Jira
attribution and no balloter-visible impact. Recommendation: **do not add a
new ballot note** to `structuredefinition-introduction.xml` for this window.
For completeness, the minimal placeholder below is provided in case the
publisher / TSC convention requires a "no substantive changes" note for
artifacts that did not change since the previous ballot; otherwise omit
entirely.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes to the
  <code>StructureDefinition</code> resource have been made since the previous
  ballot. The only edit in this window is an editorial typo correction in the
  <code>StructureDefinition.keyword</code> element definition (no semantic
  change). No elements, cardinalities, types, bindings, constraints, search
  parameters, operations, or examples were added, removed, or revised.</p>
</blockquote>
```

## Notes for Reviewer

- **Empty-for-ballot-purposes window.** This run is effectively a "no-op"
  for ballot-note purposes. The single in-window commit is the kind of
  editorial sweep that the publisher / chair would normally not call out
  to balloters. Suggest dropping the proposed note above and leaving
  `structuredefinition-introduction.xml` as-is unless a chair-level
  convention dictates otherwise.
- **No ticket attribution.** `a9658ed9`'s message
  (`typos and bump kindling`) does not reference any `FHIR-####` issue, and
  `fhir-augury-cli cross-referenced --value a9658ed9…` returned zero hits.
  Nothing in Jira to summarise; nothing to cite inline in the proposed note.
- **HEAD vs. since-commit relationship.** Confirmed fast-forward:
  `db79dcdf` is a descendant of `5d67a34a` in the cache clone (`git log
  5d67a34a..HEAD` enumerates commits cleanly without falling back to
  symmetric difference).
- **Briefing currency.** The on-disk briefing was generated against clone
  HEAD `1b369ff4` on 2026-04-20; the actual clone HEAD at run time is
  `db79dcdf` (2026-04-21). The briefing is one day stale relative to the
  clone but the FhirCore Authoring root and recipe guidance are still
  accurate (the staleness affects per-artifact map detail, not the layout
  used here).
- **Out-of-scope siblings.** None of the in-window changes touched files
  outside the artifact's scope, so there is no other artifact / page report
  to redirect to.

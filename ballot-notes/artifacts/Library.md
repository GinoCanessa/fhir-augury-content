# Artifact Ballot Note Draft: Library (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Library` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `Library` for this run (resolved from the briefing's
FhirCore Artifact Map pattern `source/<name>/…`, with `<name> = library`).
Search-parameter, operation, terminology and example patterns are listed
even when they did not change in the window.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/library/structuredefinition-Library.xml` | StructureDefinition (canonical resource SD) | no |
| `source/library/library-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/library/library-notes.xml` | Supplementary narrative | no |
| `source/library/bundle-Library-search-params.xml` | Search parameters bundle | no |
| `source/library/list-Library-operations.xml` | Operations list | no |
| `source/library/list-Library-examples.xml` | Examples list | no |
| `source/library/list-Library-packs.xml` | Packs list | no |
| `source/library/operationdefinition-Library-data-requirements.xml` | `$data-requirements` OperationDefinition (sibling SD) | no |
| `source/library/library-cms146-example.xml` | Example | no |
| `source/library/library-cms146-example-content.cql` | Example CQL content | no |
| `source/library/library-composition-example.xml` | Example | no |
| `source/library/library-example.xml` | Example | no |
| `source/library/library-example-content.cql` | Example CQL content | no |
| `source/library/library-ExampleEventDefinitionLogic.xml` | Example | no |
| `source/library/library-ExampleEventDefinitionLogic-content.cql` | Example CQL content | no |
| `source/library/library-examples-header.xml` | Examples header | no |
| `source/library/library-exclusive-breastfeeding-cds-logic.xml` | Example | no |
| `source/library/library-exclusive-breastfeeding-cds-logic-content.cql` | Example CQL content | no |
| `source/library/library-exclusive-breastfeeding-cqm-logic.xml` | Example | no |
| `source/library/library-exclusive-breastfeeding-cqm-logic-content.cql` | Example CQL content | no |
| `source/library/library-fhir-helpers.xml` | Example | no |
| `source/library/library-fhir-helpers-content.cql` | Example CQL content | no |
| `source/library/library-fhir-model-definition.xml` | Example | no |
| `source/library/library-fhir-model-definition-content.xml` | Example content | no |
| `source/library/library-hiv-indicators.xml` | Example | no |
| `source/library/library-hiv-indicators-content.cql` | Example CQL content | no |
| `source/library/library-mmi-suiciderisk-orderset-logic.xml` | Example | no |
| `source/library/library-mmi-suiciderisk-orderset-logic-content.cql` | Example CQL content | no |
| `source/library/library-omtk-logic.xml` | Example (OMTK opioid logic) | **yes** |
| `source/library/library-omtk-modelinfo.xml` | Example (OMTK model info) | **yes** |
| `source/library/library-opioidcds-common.xml` | Example (OpioidCDS common) | **yes** |
| `source/library/library-opioidcds-recommendation-04.xml` | Example (OpioidCDS rec 04) | **yes** |
| `source/library/library-opioidcds-recommendation-05.xml` | Example (OpioidCDS rec 05) | **yes** |
| `source/library/library-opioidcds-recommendation-07.xml` | Example (OpioidCDS rec 07) | **yes** |
| `source/library/library-opioidcds-recommendation-08.xml` | Example (OpioidCDS rec 08) | **yes** |
| `source/library/library-opioidcds-recommendation-10.xml` | Example (OpioidCDS rec 10) | **yes** |
| `source/library/library-opioidcds-recommendation-11.xml` | Example (OpioidCDS rec 11) | **yes** |
| `source/library/library-predecessor-example.xml` | Example | no |
| `source/library/library-quick-model-definition.xml` | Example | no |
| `source/library/library-quick-model-definition-content.xml` | Example content | no |
| `source/library/library-zika-virus-intervention-logic.xml` | Example | no |
| `source/library/library-zika-virus-intervention-logic-content.cql` | Example CQL content | no |
| `source/library/library-definition-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/library/library-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/library/cms146_data_requirements.json` | Example payload (data-requirements response) | no |
| `source/library/$data-requirements-request.txt` | Example operation request | no |
| `source/library/$data-requirements-response.txt` | Example operation response | no |
| `source/library/invariant-tests/` | Invariant test fixtures | no |

Patterns from the briefing that produced no match in the clone:

- `source/library/valueset-*.xml` — no artifact-scoped ValueSets.
- `source/library/codesystem-*.xml` — no artifact-scoped CodeSystems.
- `source/library/library-spreadsheet.xml` — no legacy spreadsheet (the
  StructureDefinition is authoritative, per the briefing).

## Current Ballot Note

No existing ballot note. `source/library/library-introduction.xml` contains
only the standard "Scope and Usage" / "Boundaries and Relationships"
narrative with no `<blockquote class="ballot-note" …>` block, and
`source/library/library-notes.xml` is empty.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) |

No `FHIR-…` / `UTG-…` ticket key appears in the commit subject or body, and
`fhir-augury-cli cross-referenced` returned zero hits for the commit SHA.

## Per-Ticket Detail

### (unattributed)

- **Commits applying in window:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224)
    — "display names have changed for US and GB" (2026-03-28, JohnMoehrke)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Bulk display-string correction across nine example Library instances. In
  every touched file the ISO-3166 jurisdiction coding for `US`
  (`urn:iso:std:iso:3166` / code `US`) had its `display` value changed from
  `"United States of America (the)"` to `"United States of America"`. The
  change is one line per file, applied identically to
  `library-omtk-logic.xml`, `library-omtk-modelinfo.xml`,
  `library-opioidcds-common.xml`, and
  `library-opioidcds-recommendation-{04,05,07,08,10,11}.xml`. No `GB`
  display occurs in any Library file (the commit's "GB" half landed in
  examples for other resources — see Notes for reviewer). Nothing else in
  the Library scope (StructureDefinition, intro/notes, search parameters,
  operations, examples list, packs, data-requirements OperationDefinition)
  was touched.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-Library.xml`):** unchanged.
  No element added/removed, no cardinality / type / binding / constraint
  edits. No snapshot regeneration required.
- **Intro / narrative (`library-introduction.xml`, `library-notes.xml`):**
  unchanged. Scope, boundaries, and the `asset-collection` /
  artifact-manifest discussion are all as they were at `5d67a34a13a5`.
- **Search parameters (`bundle-Library-search-params.xml`):** unchanged.
  No SearchParameter added, removed, or modified.
- **Operations (`list-Library-operations.xml`,
  `operationdefinition-Library-data-requirements.xml`):** unchanged. The
  `$data-requirements` operation definition is unchanged.
- **Examples:** nine example Library instances had a single
  jurisdiction-display string corrected (ISO-3166 `US`:
  `"United States of America (the)"` → `"United States of America"`).
  No example was added or removed; `list-Library-examples.xml` and
  `library-examples-header.xml` are unchanged. The change is purely
  cosmetic in the example payload — it does not alter the conformance
  requirements, the bound terminology, or the canonical URL of any
  example.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** none in the
  Library folder; nothing changed. The display value comes from the
  ISO-3166 vocabulary referenced by URN; the underlying code system is
  not maintained in this repo.

## Proposed Ballot Note (HTML)

The window contains no balloter-relevant change to the `Library`
resource. Nothing was changed in the StructureDefinition, narrative,
search parameters, operations, or constraints; only an ISO-3166 country
display string was corrected in nine example payloads. **Recommendation:
do not add a ballot note for `Library` in this cycle.** If a placeholder
note is desired so reviewers can see at a glance that nothing of substance
moved, the following minimal block can be dropped into
`source/library/library-introduction.xml` immediately above the existing
`<a name="bnc"></a>` anchor:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to
  the Library resource in this ballot cycle. The StructureDefinition,
  narrative, search parameters, operations, and constraints are
  unchanged from the previous ballot. The only edits in this window were
  a cosmetic correction of the ISO&nbsp;3166 <code>US</code> jurisdiction
  display string (<i>"United States of America (the)"</i> &rarr;
  <i>"United States of America"</i>) across nine example Library
  instances; no Jira ticket was associated with the change.</p>
</blockquote>
```

No Jira ticket links are cited because no `FHIR-…` key was attributable
to the commit (see Notes for reviewer).

## Notes for Reviewer

- The commit `a287d6eb0592` ("display names have changed for US and GB")
  is a sweep across many resource example folders. The "GB" half does not
  land in `source/library/`; the only Library files touched contain `US`
  jurisdictions. The cross-resource character of the commit (also touches
  `capabilitystatement/`, `medicationstatement/`, `messagedefinition/`,
  `operationdefinition/`, `plandefinition/`, `searchparameter/`) suggests
  it is bulk maintenance rather than a Library-specific disposition.
- `fhir-augury-cli cross-referenced` returned zero hits for the commit
  SHA, and no `FHIR-…` / `UTG-…` key appears in the subject or body. If a
  Jira ticket exists for this jurisdiction-display sweep it is not
  discoverable from the commit metadata or from FhirAugury cross-refs;
  the reviewer may wish to confirm with the committer
  (`JohnMoehrke@gmail.com`) before final ballot publication.
- The cache clone HEAD (`db79dcdfe196`) is ahead of the briefing's
  recorded HEAD (`1b369ff4e28e`), but only by commits that did not touch
  `source/library/` — the windowed enumeration above used the live clone
  HEAD as the right-hand bound. No deviation in the workflow was
  required (`5d67a34a13a5` is an ancestor of `db79dcdfe196`, so the
  symmetric-difference fallback was not needed).
- `source/library/library-notes.xml` exists but is empty
  (placeholder-only); no narrative was lost or moved in the window.

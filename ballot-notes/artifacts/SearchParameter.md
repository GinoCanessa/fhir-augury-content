# Artifact Ballot Note Draft: SearchParameter (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `SearchParameter` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `SearchParameter` for this run (resolved from the
briefing's per-resource layout for `source/<name>/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/searchparameter/structuredefinition-SearchParameter.xml` | StructureDefinition (canonical) | no |
| `source/searchparameter/searchparameter-introduction.xml` | Narrative intro | no |
| `source/searchparameter/searchparameter-notes.xml` | Supplementary narrative (current ballot note lives here) | no |
| `source/searchparameter/bundle-SearchParameter-search-params.xml` | Search parameters bundle | no |
| `source/searchparameter/list-SearchParameter-operations.xml` | Operations list | no |
| `source/searchparameter/list-SearchParameter-examples.xml` | Examples list | no |
| `source/searchparameter/list-SearchParameter-packs.xml` | Search-parameter packs list | no |
| `source/searchparameter/implementationguide-SearchParameter-core.xml` | Per-resource IG manifest | no |
| `source/searchparameter/common-search-parameters.xml` | Common search parameters definitions | no |
| `source/searchparameter/searchparameter-filter.xml` | Filter SearchParameter (sibling artifact) | no |
| `source/searchparameter/searchparameter-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | no |
| `source/searchparameter/searchparameter-example.xml` | Primary example | **yes** |
| `source/searchparameter/searchparameter-example-constraint.xml` | Example | no |
| `source/searchparameter/searchparameter-example-extension.xml` | Example | no |
| `source/searchparameter/searchparameter-example-reference.xml` | Example | no |
| `source/searchparameter/searchparameter-examples-header.xml` | Examples header narrative | no |
| `source/searchparameter/valueset-search-comparator.xml` | Artifact-scoped ValueSet | no |
| `source/searchparameter/valueset-search-modifier-all-codes.xml` | Artifact-scoped ValueSet | no |
| `source/searchparameter/valueset-search-modifier-code.xml` | Artifact-scoped ValueSet | no |
| `source/searchparameter/valueset-search-processingmode.xml` | Artifact-scoped ValueSet | no |
| `source/searchparameter/codesystem-search-comparator.xml` | Artifact-scoped CodeSystem | no |
| `source/searchparameter/codesystem-search-modifier-code.xml` | Artifact-scoped CodeSystem | no |
| `source/searchparameter/codesystem-search-processingmode.xml` | Artifact-scoped CodeSystem | no |
| `source/searchparameter/invariant-tests/cnl-0.f1.fail.xml` | Invariant test fixture | **yes** |
| `source/searchparameter/invariant-tests/cnl-1.f1.fail.xml` | Invariant test fixture | **yes** |
| `source/searchparameter/invariant-tests/spd-1.f1.fail.xml` | Invariant test fixture | **yes** |

No `source/searchparameter/searchparameter-spreadsheet.xml` exists in this clone
(the StructureDefinition is the sole authoritative source for this resource).

## Current Ballot Note

A single ballot-note block exists at HEAD, in `searchparameter-notes.xml`
(line 149). It is unchanged in the window.

```html
<blockquote class="ballot-note" id="bn">
Request for ballot feedback: We would like the 'SHOULD' assertions above to become 'SHALL' assertions.
We are invoking our usual implementer outreach process to find out whether anyone else objects, but please file tickets for any rules you do not believe can be enforced that way.
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) |

The single in-window commit carries no `(FHIR\|UTG)-\d+` key in its subject or
body, and `fhir-augury-cli cross-referenced` for the SHA returned zero hits.

## Per-Ticket Detail

### (unattributed)

- **Commits applying this change:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) — "display names have changed for US and GB" (2026-03-28, JohnMoehrke)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Updated the `display` value on the `urn:iso:std:iso:3166` `US` jurisdiction
  coding from `"United States of America (the)"` to
  `"United States of America"` in four files:
  `searchparameter-example.xml` and the three invariant test fixtures
  `invariant-tests/cnl-0.f1.fail.xml`, `invariant-tests/cnl-1.f1.fail.xml`,
  and `invariant-tests/spd-1.f1.fail.xml`. The `<system>` and `<code>` values
  were not touched, and no other element on these instances changed. The
  StructureDefinition, intro, notes, search-parameter bundle, operations
  list, packs list, examples list, sibling SearchParameters, and all
  artifact-scoped ValueSets / CodeSystems were untouched.

## Roll-up Summary (after-applied state)

The `5d67a34..HEAD` window contains a single, non-substantive change to the
`SearchParameter` artifact: a jurisdiction display-name refresh to align
with current ISO 3166 / UTG display strings.

- **StructureDefinition (`structuredefinition-SearchParameter.xml`):** No
  changes. No `<differential>` edits, no `<snapshot>` regeneration required
  for this artifact.
- **Intro / narrative (`searchparameter-introduction.xml`,
  `searchparameter-notes.xml`):** No changes. The existing ballot note
  about promoting derived-SearchParameter "SHOULD" assertions to "SHALL"
  remains in place verbatim.
- **Search parameters (`bundle-SearchParameter-search-params.xml`):** No
  changes. No additions, removals, or expression edits.
- **Operations (`list-SearchParameter-operations.xml`):** No changes.
- **Examples:** Only the jurisdiction `display` text was updated in
  `searchparameter-example.xml` (US coding now `"United States of America"`
  rather than `"United States of America (the)"`). The example's content
  payload (search-parameter shape, code, base, expression, etc.) is
  unchanged.
- **Invariant test fixtures (`invariant-tests/*.fail.xml`):** Same display
  refresh as the example; no change to the invariants being exercised
  (`cnl-0`, `cnl-1`, `spd-1`).
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes to
  any of the four ValueSets or three CodeSystems the artifact ships
  (`search-comparator`, `search-modifier-code`, `search-modifier-all-codes`,
  `search-processingmode`).

Net effect: there is no balloter-relevant change to the `SearchParameter`
resource in this window; the only edits are cosmetic display-string
alignment in test/example instances.

## Proposed Ballot Note (HTML)

The existing ballot note is still accurate in the after-applied state and
should be carried forward unchanged. The window introduces no new
balloter-relevant change to surface, so no additional ballot-note block is
proposed for this artifact.

```html
<blockquote class="ballot-note" id="bn">
Request for ballot feedback: We would like the 'SHOULD' assertions above to become 'SHALL' assertions.
We are invoking our usual implementer outreach process to find out whether anyone else objects, but please file tickets for any rules you do not believe can be enforced that way.
</blockquote>
```

## Notes for Reviewer

- The single commit in the window
  ([`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224))
  has no Jira ticket reference in its message and no cross-references in
  FhirAugury. It appears to be part of a repo-wide jurisdiction-display
  refresh ("display names have changed for US and GB"); the same author
  likely touched many other resources' example/test fixtures in the same
  pass. If a tracking ticket exists, it was not surfaced by
  `fhir-augury-cli cross-referenced` for this SHA.
- The commit subject mentions GB as well, but no `GB`-coded jurisdictions
  appear in the SearchParameter source files — the GB portion of the
  refresh did not affect this artifact.
- HEAD is a descendant of the supplied since-commit; the standard
  fast-forward `since-commit..HEAD` range was used (no symmetric-difference
  fallback needed).
- All data was sourced from the cached clone (`git`) and `fhir-augury-cli`;
  `gh api` was not needed.

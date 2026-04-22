# Artifact Ballot Note Draft: OperationDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `OperationDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `OperationDefinition` for this run (resolved from
`source/operationdefinition/` per the FhirCore briefing's authoring layout):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/operationdefinition/structuredefinition-OperationDefinition.xml` | Canonical StructureDefinition | no |
| `source/operationdefinition/operationdefinition-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/operationdefinition/operationdefinition-notes.xml` | Supplementary narrative | no |
| `source/operationdefinition/bundle-OperationDefinition-search-params.xml` | Search parameters bundle | no |
| `source/operationdefinition/list-OperationDefinition-operations.xml` | Operations list | no |
| `source/operationdefinition/list-OperationDefinition-examples.xml` | Examples list | no |
| `source/operationdefinition/list-OperationDefinition-packs.xml` | Packs list | no |
| `source/operationdefinition/operationdefinition-example.xml` | Example (`populate` operation) | yes |
| `source/operationdefinition/operationdefinition-example-query-high-risk.xml` | Example (`high-risk` query) | no |
| `source/operationdefinition/operationdefinition-examples-header.xml` | Examples header narrative | no |
| `source/operationdefinition/operationdefinition-definition-mapping-exceptions.xml` | Mapping exceptions (Definition pattern) | no |
| `source/operationdefinition/operationdefinition-fivews-mapping-exceptions.xml` | Mapping exceptions (5Ws) | no |
| `source/operationdefinition/implementationguide-OperationDefinition-core.xml` | IG resource for the artifact | no |
| `source/operationdefinition/structuredefinition-extension-operationdefinition-allowed-type.xml` | Sibling extension SD (`allowed-type`) | no |
| `source/operationdefinition/codesystem-binding-strength.xml` | Artifact-scoped CodeSystem | no |
| `source/operationdefinition/codesystem-operation-kind.xml` | Artifact-scoped CodeSystem | no |
| `source/operationdefinition/codesystem-operation-parameter-scope.xml` | Artifact-scoped CodeSystem | no |
| `source/operationdefinition/codesystem-operation-parameter-type.xml` | Artifact-scoped CodeSystem | no |
| `source/operationdefinition/codesystem-synchronicity-control.xml` | Artifact-scoped CodeSystem | no |
| `source/operationdefinition/valueset-operation-kind.xml` | Artifact-scoped ValueSet | no |
| `source/operationdefinition/valueset-operation-parameter-scope.xml` | Artifact-scoped ValueSet | no |
| `source/operationdefinition/valueset-operation-parameter-type.xml` | Artifact-scoped ValueSet | no |
| `source/operationdefinition/valueset-synchronicity-control.xml` | Artifact-scoped ValueSet | no |

Patterns from the briefing that produced no match in the clone:
- `source/operationdefinition/<name>-spreadsheet.xml` — no legacy spreadsheet exists; SD is authoritative.

## Current Ballot Note

No existing ballot note. `operationdefinition-introduction.xml` at HEAD
contains no `<blockquote class="ballot-note" …>` block.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) |

No commit in the window references a `FHIR-` or `UTG-` ticket key in its
subject/body, and `fhir-augury-cli cross-referenced` returned no hits for
the commit SHA. The single change is editorial / data-cleanup.

## Per-Ticket Detail

### (unattributed)

- **Commits applying to this artifact:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) — *display names have changed for US and GB* (2026-03-28, JohnMoehrke)
- **Changes applied (scoped to this artifact):**
  In `operationdefinition-example.xml`, the `jurisdiction` coding for
  `urn:iso:std:iso:3166` code `GB` had its `display` text changed from
  "United Kingdom of Great Britain and Northern Ireland (the)" to
  "United Kingdom of Great Britain and Northern Ireland" (drops the
  parenthetical "(the)" suffix). This is an example-only edit; no
  StructureDefinition, narrative, search parameter, operation, or
  terminology files in `source/operationdefinition/` were touched. The
  same commit also updated jurisdiction display values in many other
  resources (CapabilityStatement, Library, MessageDefinition,
  PlanDefinition, SearchParameter examples) — consistent ISO-3166
  display normalisation across the spec.

## Roll-up Summary (after-applied state)

Diff statistics for `5d67a34a13a5..db79dcdfe196` scoped to
`source/operationdefinition/**`: 1 file changed, 1 insertion(+), 1
deletion(-).

- **StructureDefinition (`structuredefinition-OperationDefinition.xml`):**
  No changes. No element additions/removals, cardinality, type, binding,
  or constraint edits. Snapshot regeneration is not required from this
  artifact's own changes.
- **Sibling extension SD
  (`structuredefinition-extension-operationdefinition-allowed-type.xml`):**
  No changes.
- **Intro / narrative (`operationdefinition-introduction.xml`,
  `operationdefinition-notes.xml`,
  `operationdefinition-examples-header.xml`):** No changes. Substantive
  scope, boundary, and normative-status text is unchanged since the
  since-commit.
- **Search parameters
  (`bundle-OperationDefinition-search-params.xml`):** No changes.
- **Operations (`list-OperationDefinition-operations.xml`):** No
  changes.
- **Examples:** Only the `populate` example
  (`operationdefinition-example.xml`) changed. The change is a cosmetic
  ISO-3166 jurisdiction display update for code `GB` (drops the trailing
  "(the)"). The `high-risk-query` example
  (`operationdefinition-example-query-high-risk.xml`) and the examples
  list/header are unchanged. No examples were added or removed.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes
  to `binding-strength`, `operation-kind`, `operation-parameter-scope`,
  `operation-parameter-type`, or `synchronicity-control` in either the
  CodeSystem or ValueSet form.
- **Mapping exceptions / IG resource:** No changes to
  `operationdefinition-definition-mapping-exceptions.xml`,
  `operationdefinition-fivews-mapping-exceptions.xml`, or
  `implementationguide-OperationDefinition-core.xml`.

Net effect: there are no balloter-relevant changes to the
OperationDefinition resource since `5d67a34a13a5`. The only edit in the
window is an example-data display-string normalisation that does not
affect conformance, schema, terminology, search, or operation surface.

## Proposed Ballot Note (HTML)

Because the after-applied state contains no substantive change to the
OperationDefinition resource, no ballot note is warranted for this
window. The example-only ISO-3166 display update is editorial, applies
across many resources, and does not affect the OperationDefinition
ballot reviewer's assessment.

If the work group nonetheless wants to acknowledge the window
explicitly, the following minimal note can be inlined at the top of
`operationdefinition-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to
  the OperationDefinition resource since the previous ballot. The only
  edit in the window is an editorial normalisation of a jurisdiction
  display value in the <code>populate</code> example
  (<code>operationdefinition-example.xml</code>), applied as part of a
  cross-resource ISO 3166 country-name clean-up. The
  StructureDefinition, search parameters, operations, narrative,
  examples list, and artifact-scoped terminology
  (<code>operation-kind</code>, <code>operation-parameter-type</code>,
  <code>operation-parameter-scope</code>,
  <code>synchronicity-control</code>, <code>binding-strength</code>)
  are unchanged.</p>
</blockquote>
```

The note intentionally has no `<ul>` of ticket bullets because no Jira
ticket is attributable to the change.

## Notes for Reviewer

- **No prior ballot note to carry forward.** `operationdefinition-introduction.xml`
  at HEAD does not contain a `<blockquote class="ballot-note" …>` block,
  so there is nothing to retain or supersede.
- **No ticket attribution.** The single in-window commit
  ([`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224))
  has no `FHIR-`/`UTG-` reference in its subject or body, and
  `fhir-augury-cli cross-referenced` returned zero hits for the SHA. The
  commit appears to be a coordinated editorial pass by JohnMoehrke
  updating ISO-3166 country `display` strings in example resources
  across the spec; no Jira ticket is required to interpret it.
- **Cross-artifact touch points.** The same commit also edits
  `source/capabilitystatement/`, `source/library/`,
  `source/messagedefinition/`, `source/plandefinition/`, and
  `source/searchparameter/` examples. Those artifacts may want to
  acknowledge the change in their own ballot windows; nothing in
  `source/operationdefinition/` outside the one example file was
  touched.
- **Window integrity.** HEAD (`db79dcdfe196`) is a descendant of the
  since-commit (`5d67a34a13a5`); the standard `since..HEAD` range was
  used. The cache clone resolved both SHAs; `gh` was not required.

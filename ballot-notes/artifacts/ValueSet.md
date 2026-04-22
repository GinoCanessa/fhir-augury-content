# Artifact Ballot Note Draft: ValueSet (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `ValueSet` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `ValueSet` for this run (from the `source/valueset/` authoring folder per the briefing's "Authoring root(s)" guidance):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/valueset/structuredefinition-ValueSet.xml` | StructureDefinition (canonical) | no |
| `source/valueset/valueset-introduction.xml` | Narrative intro (where the ballot note would live) | no |
| `source/valueset/valueset-notes.xml` | Supplementary narrative | no |
| `source/valueset/bundle-ValueSet-search-params.xml` | Search parameters | no |
| `source/valueset/list-ValueSet-operations.xml` | Operations index | no |
| `source/valueset/list-ValueSet-examples.xml` | Examples list | no |
| `source/valueset/list-ValueSet-packs.xml` | Profile pack list | no |
| `source/valueset/operationdefinition-ValueSet-expand.xml` | `$expand` OperationDefinition | no |
| `source/valueset/operationdefinition-ValueSet-validate-code.xml` | `$validate-code` OperationDefinition | **yes** |
| `source/valueset/profile-computablevalueset-introduction.xml` | Computable ValueSet profile narrative | no |
| `source/valueset/profile-executablevalueset-introduction.xml` | Executable ValueSet profile narrative | no |
| `source/valueset/profile-publishablevalueset-introduction.xml` | Publishable ValueSet profile narrative | no |
| `source/valueset/profile-shareablevalueset-introduction.xml` | Shareable ValueSet profile narrative | no |
| `source/valueset/implementationguide-ValueSet-core.xml` | ValueSet IG bundle | no |
| `source/valueset/codesystem-expansion-processing-rule.xml` | Artifact-scoped CodeSystem | no |
| `source/valueset/codesystem-filter-operator.xml` | Artifact-scoped CodeSystem | no |
| `source/valueset/valueset-designation-use.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-expansion-processing-rule.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-filter-operator.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-fivews-mapping-exceptions.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-nhin-purposeofuse.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-ucum-common.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-zika-affected-areas.xml` | Artifact-scoped ValueSet | no |
| `source/valueset/valueset-example*.xml`, `valueset-examples-header.xml` | Examples (10 files) | no |

Patterns from the briefing that produced no match in the clone:
- `source/valueset/valueset-spreadsheet.xml` — no legacy spreadsheet exists for ValueSet (StructureDefinition is authoritative, per the briefing).

The `source/valueset/` folder also contains build/derived helpers (`mif/`, `invariant-tests/`, captured `$expand`/`$validate-code` request/response transcripts, `valueset.svg`) which are out of scope for ballot-note authoring.

## Current Ballot Note

No existing ballot note. A scan of every `*.xml` file under `source/valueset/` at HEAD found zero `<blockquote class="ballot-note" …>` blocks.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

The single commit in the window has no Jira key in its subject or body, and `fhir-augury-cli cross-referenced` returned zero hits for the SHA.

## Per-Ticket Detail

### (unattributed)

- **Commits applying to this artifact:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — "typos and bump kindling" (Grahame Grieve, 2026-03-18T13:14:07+11:00)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `source/valueset/operationdefinition-ValueSet-validate-code.xml`, removed an extraneous full stop from the `abstract` parameter's `<documentation>` value: `"Note that. 'abstract' is a property…"` → `"Note that 'abstract' is a property…"`. One line changed; no semantic impact on the operation, parameters, signature, examples, search params, or the ValueSet StructureDefinition itself. The same commit also touches files in 7 other folders (CodeSystem, DeviceMetric, DeviceAlert codesystems, MedicationDispense example, StructureDefinition, terminologies bindings, credits, workflow), all out of scope for this artifact.

## Roll-up Summary (after-applied state)

Diff (`git diff 5d67a34a13a5..db79dcdfe196 -- source/valueset/…`) shows a **single one-line edit** confined to one file:

- **StructureDefinition (`structuredefinition-ValueSet.xml`):** No changes. Snapshot regeneration not required for this window.
- **Intro / narrative (`valueset-introduction.xml`, `valueset-notes.xml`, `profile-*-introduction.xml`):** No changes.
- **Search parameters (`bundle-ValueSet-search-params.xml`):** No changes.
- **Operations:**
  - `list-ValueSet-operations.xml` unchanged.
  - `operationdefinition-ValueSet-expand.xml` unchanged.
  - `operationdefinition-ValueSet-validate-code.xml`: typo fix in the `abstract` parameter's `<documentation>` value (extraneous period removed). Operation signature, parameter set, types, cardinalities, and behavioural prose are otherwise unchanged.
- **Examples:** No changes.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes.
- **IG bundle (`implementationguide-ValueSet-core.xml`):** No changes.

In short, the ValueSet artifact has had **no balloter-relevant changes** in the window — only a copy-edit to one parameter description in the `$validate-code` OperationDefinition.

## Proposed Ballot Note (HTML)

**Recommendation: do not add a ballot note for this window.** The only change is a single typo fix with no semantic impact, well below the threshold for a balloter callout, and there is no pre-existing ballot note whose substance must be carried forward.

If, for procedural consistency, a stub note is nevertheless required, the following minimal note can be inserted at the top of `source/valueset/valueset-introduction.xml` (next free id is `bn1`, since no prior notes exist):

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to the
  ValueSet resource since the previous ballot. The only edit in the window
  is a copy-edit (removal of a stray full stop) in the documentation of the
  <code>abstract</code> parameter on the
  <a href="valueset-operation-validate-code.html"><code>$validate-code</code></a>
  operation; the operation signature and behaviour are unchanged.</p>
</blockquote>
```

No Jira tickets are cited because the underlying commit (`a9658ed97c2a`, "typos and bump kindling") was not attributed to a FHIR Jira issue.

## Notes for Reviewer

- **No prior ballot note to carry forward.** A scan of every `*.xml` file under `source/valueset/` at HEAD (`db79dcdfe196`) found zero `<blockquote class="ballot-note" …>` blocks, so no existing bullets needed to be retained, revised, or dropped.
- **Cross-artifact commit.** Commit `a9658ed97c2a` is a multi-folder typo sweep; it also edits files under `source/codesystem/`, `source/devicealert/`, `source/devicemetric/`, `source/medicationdispense/`, `source/structuredefinition/`, `source/terminologies/`, plus the top-level `source/credits.html` and `source/workflow.html`. Those edits will be picked up by the corresponding artifact / page ballot-note runs and do not affect this artifact's roll-up.
- **No Jira attribution available.** The commit message contains no `FHIR-XXXXX` or `UTG-XXXXX` keys, and `fhir-augury-cli --json '{"command":"cross-referenced","value":"a9658ed97c2a382863b51cf1f260c478cfa18f30","limit":50}'` returned `total: 0`. The "Tickets Applied" table therefore lists only the `(unattributed)` row.
- **Briefing freshness.** Briefing was analysed at clone HEAD `1b369ff4e28e` (2026-04-20); the current cached clone HEAD is `db79dcdfe196` — about one day newer, no structural changes to the `source/valueset/` layout. The briefing's Artifact Map / Authoring Roots remain accurate for this run.
- **Window integrity.** `db79dcdfe196` is a descendant of `5d67a34a13a5`; no symmetric-difference fallback was needed. Cache clone resolved both endpoints; `gh` was not invoked.

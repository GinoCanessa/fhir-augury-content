# Artifact Ballot Note Draft: DeviceAlert (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `DeviceAlert` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `DeviceAlert` for this run (resolved by walking
`source/devicealert/` per the briefing's FhirCore patterns; the briefing's
Artifact Map does not enumerate per-resource paths individually):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/devicealert/structuredefinition-DeviceAlert.xml` | StructureDefinition (canonical) | no |
| `source/devicealert/devicealert-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/devicealert/devicealert-notes.xml` | Supplementary narrative | no |
| `source/devicealert/bundle-DeviceAlert-search-params.xml` | Search parameters | no |
| `source/devicealert/list-DeviceAlert-operations.xml` | Operations | no |
| `source/devicealert/list-DeviceAlert-examples.xml` | Examples list | no |
| `source/devicealert/list-DeviceAlert-packs.xml` | Packs list | no |
| `source/devicealert/devicealert-example.xml` | Example instance | no |
| `source/devicealert/devicealert-examples-header.xml` | Examples header | no |
| `source/devicealert/devicealert-event-mapping-exceptions.xml` | Event-mapping exceptions | no |
| `source/devicealert/devicealert-fivews-mapping-exceptions.xml` | Five-Ws mapping exceptions | no |
| `source/devicealert/codesystem-devicealert-activationState.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-annunciation.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-category.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-manifestation.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-presence.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-priority.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-signalType.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-status.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/codesystem-devicealert-type.xml` | Artifact-scoped CodeSystem | yes |
| `source/devicealert/valueset-devicealert-activationState.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-annunciation.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-category.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-condition.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-manifestation.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-presence.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-priority.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-signalType.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-status.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-devicealert-type.xml` | Artifact-scoped ValueSet | no |
| `source/devicealert/valueset-observation-codes.xml` | Artifact-scoped ValueSet | no |

Patterns from the briefing that produced no match in the clone:

- `source/devicealert/devicealert-spreadsheet.xml` — no legacy spreadsheet present (StructureDefinition is authoritative).
- Sibling `structuredefinition-*.xml` files other than the canonical `structuredefinition-DeviceAlert.xml` — none present (no extra profile artifacts ship alongside the resource).

## Current Ballot Note

No existing ballot note. `source/devicealert/devicealert-introduction.xml` at HEAD contains no `<blockquote class="ballot-note" …>` block.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

The single commit in the window carries no Jira ticket key in its subject or body, and `fhir-augury-cli cross-referenced` returned 0 hits for the SHA.

## Per-Ticket Detail

### (unattributed)

- **Commits:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — "typos and bump kindling" (2026-03-18T13:14:07+11:00, Grahame Grieve)
- **Changes applied (per Step 5b, scoped to this artifact):** Editorial-only change. The commit updates the `<publisher>` element from `"HL7 International / Health Care Devices"` to `"HL7 International / Devices"` in nine DeviceAlert-scoped CodeSystem resources: `activationState`, `annunciation`, `category`, `manifestation`, `presence`, `priority`, `signalType`, `status`, and `type`. No code definitions, codes, display strings, hierarchies, or `caseSensitive` / `content` settings are touched. The DeviceAlert StructureDefinition, intro/notes narrative, search-parameter bundle, operations list, examples list, example instances, mapping-exceptions files, and all sibling `valueset-devicealert-*.xml` files are untouched in the window.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-DeviceAlert.xml`):** No changes. No element additions, removals, cardinality / type / binding adjustments, or constraint edits. Snapshot regeneration is not required.
- **Intro / narrative (`devicealert-introduction.xml`, `devicealert-notes.xml`):** No changes. No scope, boundary, deprecation, or normative-status shifts.
- **Search parameters (`bundle-DeviceAlert-search-params.xml`):** No changes.
- **Operations (`list-DeviceAlert-operations.xml`):** No changes.
- **Examples (`list-DeviceAlert-examples.xml`, `devicealert-example.xml`, `devicealert-examples-header.xml`):** No changes.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** Editorial publisher-name update only. The nine `codesystem-devicealert-*.xml` files now declare their publisher as `"HL7 International / Devices"` (was `"HL7 International / Health Care Devices"`). No code definitions or value-set memberships changed; the ten `valueset-devicealert-*.xml` files (and the ancillary `valueset-observation-codes.xml`) are untouched. Per the FhirCore briefing, terminology placement between FhirCore and UTG is a governance call — this rename does not move any of these CodeSystems out of FhirCore.

## Proposed Ballot Note (HTML)

There are no balloter-relevant substantive changes to DeviceAlert in this window. The single commit in scope is an editorial work-group rename ("Health Care Devices" → "Devices") applied to the `<publisher>` metadata of the resource's nine artifact-scoped CodeSystems, with no impact on the resource definition, narrative, search parameters, operations, examples, or code system / value set content.

If the editor still wants a placeholder ballot note for this cycle (e.g., to advertise that DeviceAlert was reviewed but not materially changed), the following stub can be dropped into `source/devicealert/devicealert-introduction.xml`. Otherwise, **no ballot note needs to be added or revised for DeviceAlert at this time.**

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been applied to DeviceAlert since the previous ballot. The only edit in scope is an editorial work-group rename in the artifact-scoped CodeSystem publisher metadata ("HL7 International / Health Care Devices" → "HL7 International / Devices"); the resource definition, narrative, search parameters, operations, examples, and code system / value set content are unchanged.</p>
</blockquote>
```

## Notes for Reviewer

- The single commit in the window has no attributable Jira ticket: the subject ("typos and bump kindling") contains no `(FHIR|UTG)-\d+` key, and `fhir-augury-cli cross-referenced` returned 0 hits for SHA `a9658ed97c2a382863b51cf1f260c478cfa18f30`. The change is therefore listed under "(unattributed)" and the proposed ballot note carries no Jira citation.
- The briefing snapshot (`clone HEAD 1b369ff`, analysed 2026-04-20) is one commit behind the current cache clone HEAD (`db79dcdfe196`, the window endpoint). Path resolution still applies — no DeviceAlert layout change occurred between `1b369ff` and `db79dcdfe196`.
- Because there is no pre-existing ballot note for DeviceAlert, no carry-forward bullets had to be reconciled. The proposed stub is offered only for editorial completeness; the recommendation is to **omit a ballot note** for DeviceAlert this cycle since no balloter-actionable change occurred.
- The publisher-name change technically also lives in any UTG mirror of these CodeSystems if one exists, but per the FhirCore briefing the artifact-scoped CodeSystems under `source/devicealert/` are governed in FhirCore; no UTG action is implied.

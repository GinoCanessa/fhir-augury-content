# Artifact Ballot Note Draft: CapabilityStatement (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `CapabilityStatement` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `CapabilityStatement` for this run (FhirCore folder
`source/capabilitystatement/`; the briefing's Artifact Map does not contain
an explicit per-artifact entry, so the standard FhirCore patterns from the
`notes-artifact` skill were applied against the folder contents):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/capabilitystatement/structuredefinition-CapabilityStatement.xml` | StructureDefinition (canonical) | no |
| `source/capabilitystatement/capabilitystatement-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/capabilitystatement/capabilitystatement-notes.xml` | Supplementary narrative | no |
| `source/capabilitystatement/bundle-CapabilityStatement-search-params.xml` | Search parameters bundle | no |
| `source/capabilitystatement/list-CapabilityStatement-operations.xml` | Operations list | no |
| `source/capabilitystatement/operationdefinition-CapabilityStatement-versions.xml` | `$versions` OperationDefinition | no |
| `source/capabilitystatement/list-CapabilityStatement-examples.xml` | Examples list | no |
| `source/capabilitystatement/list-CapabilityStatement-packs.xml` | Implementation packs list | no |
| `source/capabilitystatement/implementationguide-CapabilityStatement-core.xml` | Core IG descriptor | no |
| `source/capabilitystatement/capabilitystatement-example.xml` | Example (EHR) | **yes** |
| `source/capabilitystatement/capabilitystatement-phr-example.xml` | Example (PHR) | no |
| `source/capabilitystatement/capabilitystatement-knowledge-repository.xml` | Example (knowledge repo) | no |
| `source/capabilitystatement/capabilitystatement-measure-processor.xml` | Example (measure processor) | no |
| `source/capabilitystatement/capabilitystatement-messagedefinition.xml` | Example (messaging) | no |
| `source/capabilitystatement/capabilitystatement-terminology-server.xml` | Example (terminology server) | no |
| `source/capabilitystatement/capabilitystatement-examples-header.xml` | Examples header narrative | no |
| `source/capabilitystatement/capabilitystatement-definition-mapping-exceptions.xml` | Definition mapping exceptions | no |
| `source/capabilitystatement/capabilitystatement-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/capabilitystatement/invariant-tests/cnl-0.f1.fail.xml` | Invariant test fixture (cnl-0) | **yes** |
| `source/capabilitystatement/invariant-tests/cnl-1.f1.fail.xml` | Invariant test fixture (cnl-1) | **yes** |
| `source/capabilitystatement/invariant-tests/*` (other fixtures) | Invariant test fixtures | no |
| `source/capabilitystatement/codesystem-*.xml` | Artifact-scoped CodeSystems (15) | no |
| `source/capabilitystatement/valueset-*.xml` | Artifact-scoped ValueSets (17) | no |
| `source/capabilitystatement/$versions-request*.txt`, `$versions-response*.txt` | `$versions` request/response samples | no |
| `source/capabilitystatement/capabilitystatementNarrative.xslt`, `capabilitystatement.svg` | Rendering assets | no |

Patterns from the briefing's generic FhirCore mapping that produced no match:

- `source/capabilitystatement/capabilitystatement-spreadsheet.xml` — no legacy spreadsheet exists for this resource.

## Current Ballot Note

No existing ballot note. `capabilitystatement-introduction.xml` at HEAD
contains no `<blockquote class="ballot-note" …>` block.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) |

`fhir-augury-cli cross-referenced` returned zero hits for the commit SHA,
the commit subject/body contains no `(FHIR|UTG)-\d+` reference, and the
commit is a cross-cutting display-name fix touching many resources outside
CapabilityStatement (libraries, medicationstatement, messagedefinition, …)
— it is a tooling/data-quality clean-up rather than work tracked against a
specific Jira ticket.

## Per-Ticket Detail

### (unattributed)

- **Commits applying in window:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224)
    — *display names have changed for US and GB* (2026-03-28, JohnMoehrke)
- **Changes applied (scoped to this artifact):** Updates the `<display>`
  text on the ISO 3166 `US` jurisdiction coding from
  `"United States of America (the)"` to `"United States of America"` in
  three example/test fixtures only:
  `capabilitystatement-example.xml`, `invariant-tests/cnl-0.f1.fail.xml`,
  and `invariant-tests/cnl-1.f1.fail.xml`. No code changes; only the
  human-readable display string was shortened to track an upstream change
  in the ISO 3166 display catalogue. The `GB` portion of the commit
  applies to other resources (Library, MedicationStatement,
  MessageDefinition) and does not touch any CapabilityStatement file.

## Roll-up Summary (after-applied state)

- **StructureDefinition (`structuredefinition-CapabilityStatement.xml`):**
  No changes. Snapshot regeneration is **not** required.
- **Intro / narrative (`capabilitystatement-introduction.xml`,
  `capabilitystatement-notes.xml`):** No changes.
- **Search parameters
  (`bundle-CapabilityStatement-search-params.xml`):** No changes — no
  parameters added, removed, or modified.
- **Operations (`list-CapabilityStatement-operations.xml`,
  `operationdefinition-CapabilityStatement-versions.xml`):** No changes.
- **Examples:** Cosmetic display-string update only. The `US`
  jurisdiction `<display>` value was shortened from
  `"United States of America (the)"` to `"United States of America"` in
  `capabilitystatement-example.xml` and the two `cnl-*` invariant test
  fixtures. No examples were added or removed; no element values changed
  beyond that human-readable label.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes.
  Note that several CodeSystems / ValueSets in this folder
  (e.g., `restful-capability-mode`, `capability-statement-kind`,
  `versioning-policy`) are candidates for relocation to UTG per the
  FhirCore briefing's cross-repo touch points, but no such relocation
  occurred in this window.

## Proposed Ballot Note (HTML)

No ballot note is proposed. The only change to the CapabilityStatement
artifact in `5d67a34a13a5..db79dcdfe196` is a cosmetic display-string
update in three example/test fixtures (ISO 3166 `US` display label),
unattached to any Jira ticket. There is no balloter-relevant change to
narrate, and FHIR's convention is to avoid adding ballot notes for
zero-impact edits.

If the publisher tooling nevertheless requires the placeholder, the
following minimal note is offered for inclusion in
`capabilitystatement-introduction.xml`; otherwise leave the file as-is.

```html
<!-- Optional placeholder; not recommended for inclusion. -->
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made
  to the CapabilityStatement resource since the previous ballot. The
  only edits in scope for this cycle are cosmetic updates to example
  fixtures (shortening of an ISO&nbsp;3166 display label).</p>
</blockquote>
```

## Notes for Reviewer

- **No prior ballot note to carry forward.** The intro file does not
  currently contain a `<blockquote class="ballot-note">`, so there are
  no existing bullets to retain or drop.
- **Briefing currency.** `meta.json` records the briefing was generated
  at clone HEAD `1b369ff4e28e` (2026-04-20); the current clone HEAD is
  `db79dcdfe196`. The drift is small (one day, no CapabilityStatement
  touches) and does not affect the artifact-to-files resolution used
  here. No `repo-analysis` refresh was triggered.
- **Cross-cutting commit.** Commit `a287d6eb0592` also modified files
  for Library, MedicationStatement, and MessageDefinition. Those edits
  are out of scope for this artifact report; per-artifact reports for
  those resources will surface them separately.
- **No `gh` fallback used.** All commit metadata was resolved from the
  cached clone via `git`. The since-commit `5d67a34a13a5` is a strict
  ancestor of HEAD (`git merge-base --is-ancestor` exit 0), so no
  symmetric-difference fallback was needed.
- **`fhir-augury-cli services health` is not a recognised action.** The
  documented `services` actions in this build are `status` / `stats`;
  `status` was used as the equivalent health check and reported all
  three services (GitHub, Jira, Zulip) as healthy.

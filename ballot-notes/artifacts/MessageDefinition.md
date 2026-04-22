# Artifact Ballot Note Draft: MessageDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `MessageDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T17:01:27Z |

## Source Files

Files considered part of `MessageDefinition` for this run (resolved
against the `source/messagedefinition/` folder per the FhirCore
briefing's Artifact Map):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/messagedefinition/structuredefinition-MessageDefinition.xml` | StructureDefinition (canonical) | no |
| `source/messagedefinition/messagedefinition-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/messagedefinition/messagedefinition-notes.xml` | Supplementary narrative | no |
| `source/messagedefinition/bundle-MessageDefinition-search-params.xml` | Search parameters | no |
| `source/messagedefinition/list-MessageDefinition-operations.xml` | Operations | no |
| `source/messagedefinition/list-MessageDefinition-examples.xml` | Examples list | no |
| `source/messagedefinition/list-MessageDefinition-packs.xml` | Implementation packs list | no |
| `source/messagedefinition/messagedefinition-example.xml` | Example (canonical) | no |
| `source/messagedefinition/messagedefinition-examples-header.xml` | Examples header | no |
| `source/messagedefinition/messagedefinition-patient-link-notification.xml` | Example MessageDefinition | **yes** |
| `source/messagedefinition/messagedefinition-patient-link-response.xml` | Example MessageDefinition | **yes** |
| `source/messagedefinition/messagedefinition-definition-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/messagedefinition/messagedefinition-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/messagedefinition/valueset-message-significance-category.xml` | Artifact-scoped ValueSet | no |
| `source/messagedefinition/valueset-messageheader-response-request.xml` | Artifact-scoped ValueSet | no |
| `source/messagedefinition/valueset-publication-status.xml` | Artifact-scoped ValueSet | no |
| `source/messagedefinition/codesystem-message-significance-category.xml` | Artifact-scoped CodeSystem | no |
| `source/messagedefinition/codesystem-messageheader-response-request.xml` | Artifact-scoped CodeSystem | no |
| `source/messagedefinition/invariant-tests/` | Invariant tests directory | no |

No briefing-listed pattern produced zero matches in the clone for this
artifact.

## Current Ballot Note

No existing ballot note. (`messagedefinition-introduction.xml` and
`messagedefinition-notes.xml` contain no
`<blockquote class="ballot-note" …>` block at HEAD.)

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) |

The single in-window commit carries no `FHIR-XXXXX` / `UTG-XXXXX`
reference in its subject or body, and `fhir-augury-cli
cross-referenced` returned no hits for the SHA.

## Per-Ticket Detail

### (unattributed)

- **Commits:**
  - [`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224) — "display names have changed for US and GB" (2026-03-28T11:07:18-05:00, JohnMoehrke)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Two example MessageDefinition resources had their
  `jurisdiction.coding.display` updated for the US ISO-3166 entry
  (`urn:iso:std:iso:3166#US`), changing the literal display text from
  `"United States of America (the)"` to `"United States of America"`.
  Affected files:
  - `source/messagedefinition/messagedefinition-patient-link-notification.xml`
    (line 50)
  - `source/messagedefinition/messagedefinition-patient-link-response.xml`
    (line 50)

  No other files in the artifact were touched. Despite the commit
  subject mentioning GB, no GB jurisdiction edits land in any
  MessageDefinition file in this window.

## Roll-up Summary (after-applied state)

Net change from `5d67a34a13a5..db79dcdfe196` scoped to
`source/messagedefinition/`:

```
.../messagedefinition/messagedefinition-patient-link-notification.xml | 2 +-
 source/messagedefinition/messagedefinition-patient-link-response.xml  | 2 +-
 2 files changed, 2 insertions(+), 2 deletions(-)
```

- **StructureDefinition (`structuredefinition-MessageDefinition.xml`):**
  No change. No element additions / removals / cardinality / type /
  binding / constraint changes; snapshot regeneration is not required
  for this artifact in this window.
- **Intro / narrative (`messagedefinition-introduction.xml`,
  `messagedefinition-notes.xml`):** No change.
- **Search parameters (`bundle-MessageDefinition-search-params.xml`):**
  No change.
- **Operations (`list-MessageDefinition-operations.xml`):** No change.
- **Examples:** Two examples (`messagedefinition-patient-link-notification.xml`,
  `messagedefinition-patient-link-response.xml`) had the display text
  on the US jurisdiction code normalized from
  `"United States of America (the)"` to `"United States of America"`.
  Editorial only; the underlying `system`/`code`
  (`urn:iso:std:iso:3166#US`) is unchanged. No examples were added or
  removed.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No change.

## Proposed Ballot Note (HTML)

The only changes to `MessageDefinition` since `5d67a34a13a5` are
display-text edits in two example files (the US ISO-3166 jurisdiction
display was normalized). The StructureDefinition, narrative, search
parameters, operations, and bound terminologies are all unchanged.
This kind of pure example-data tidy-up is not normally something a
balloter is asked to vote on, and there is no existing ballot note on
this artifact to update.

**Recommendation:** do **not** add a ballot note for `MessageDefinition`
in this ballot. If editors nevertheless want a placeholder noting "no
substantive changes", the following minimal block could be inlined at
the top of `source/messagedefinition/messagedefinition-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made
  to <code>MessageDefinition</code> since the previous ballot. The
  only edits in scope are an editorial normalization of the US
  ISO-3166 jurisdiction display text in two example resources
  (<code>messagedefinition-patient-link-notification</code> and
  <code>messagedefinition-patient-link-response</code>); the
  StructureDefinition, narrative, search parameters, operations, and
  bound terminologies are unchanged.</p>
</blockquote>
```

No Jira ticket links are included because the underlying commit
([`a287d6eb0592`](https://github.com/HL7/fhir/commit/a287d6eb0592d7dcddeb3cd66704f35b4fbee224))
is not attributed to a tracker item.

## Notes for Reviewer

- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit
  (`5d67a34a13a5`); no symmetric-difference fallback was needed.
- `fhir-augury-cli services health` is not a valid action against this
  build of the CLI; `services status` was used instead and reported
  all three services (GitHub, Jira, Zulip) healthy.
- The single in-window commit also touched files outside this
  artifact's scope (the commit subject mentions "US and GB" display
  changes, suggesting parallel edits to other example resources
  elsewhere in the spec). Those edits are out of scope for the
  `MessageDefinition` ballot note and should be picked up by the
  notes runs for the other affected artifacts.
- No existing ballot note was dropped or superseded — there was none
  to begin with.

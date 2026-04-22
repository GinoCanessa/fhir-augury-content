# Artifact Ballot Note Draft: Subscription (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Subscription` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 0 (touching artifact files) / 250 (overall in window) |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:25:00Z |

**No changes to artifact in window.** No commits between
`5d67a34a13a5..db79dcdfe196` modified any file under
`source/subscription/`. The 250 commits in the overall window touched
other artifacts only. No proposed ballot-note revision is required for
`Subscription` from this window.

## Source Files

Files considered part of `Subscription` for this run (FhirCore pattern;
the briefing's authoring-root convention is `source/<name>/` with
lowercase folder name). None were touched in the window.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/subscription/structuredefinition-Subscription.xml` | StructureDefinition (canonical) | no |
| `source/subscription/subscription-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/subscription/subscription-notes.xml` | Supplementary narrative | no |
| `source/subscription/bundle-Subscription-search-params.xml` | Search parameters bundle | no |
| `source/subscription/list-Subscription-operations.xml` | Operations bundle | no |
| `source/subscription/list-Subscription-examples.xml` | Examples list | no |
| `source/subscription/list-Subscription-packs.xml` | Resource packs list | no |
| `source/subscription/operationdefinition-Subscription-events.xml` | OperationDefinition `$events` | no |
| `source/subscription/operationdefinition-Subscription-status.xml` | OperationDefinition `$status` | no |
| `source/subscription/subscription-example.xml`, `subscription-admission.{xml,json}`, `subscription-events-response.xml`, `subscription-status-response.xml`, `subscription-examples-header.xml` | Examples | no |
| `source/subscription/valueset-subscription-channel-type.xml` | Artifact-scoped ValueSet | no |
| `source/subscription/valueset-subscription-payload-content.xml` | Artifact-scoped ValueSet | no |
| `source/subscription/valueset-subscription-status.xml` | Artifact-scoped ValueSet | no |
| `source/subscription/valueset-subscription-tag.xml` | Artifact-scoped ValueSet | no |
| `source/subscription/codesystem-subscription-payload-content.xml` | Artifact-scoped CodeSystem | no |
| `source/subscription/codesystem-subscription-status.xml` | Artifact-scoped CodeSystem | no |
| `source/subscription/codesystem-subscription-tag.xml` | Artifact-scoped CodeSystem | no |
| `source/subscription/subscription-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/subscription/invariant-tests/` | Invariant test fixtures | no |

No briefing-pattern produced an unexpected miss; the FhirCore Artifact
Map convention (`source/<name>/…`) resolved cleanly.

## Current Ballot Note

No existing ballot note. `source/subscription/subscription-introduction.xml`
at HEAD (`db79dcdfe196`) contains no `<blockquote class="ballot-note" …>`
block, and `subscription-notes.xml` likewise has none.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| _(none)_ | _No tickets attributable — no commits in window touched `Subscription` source files._ | — |

## Per-Ticket Detail

_None — no commits in the window touched any `Subscription` source file._

## Roll-up Summary (after-applied state)

`git diff 5d67a34a13a5..db79dcdfe196 -- source/subscription/` returns
an empty diff. There are no element-level, narrative, search-parameter,
operation, example, or terminology changes to report for `Subscription`
in this window.

- **StructureDefinition (`structuredefinition-Subscription.xml`):** no changes.
- **Intro / narrative (`subscription-introduction.xml`, `subscription-notes.xml`):** no changes.
- **Search parameters (`bundle-Subscription-search-params.xml`):** no changes.
- **Operations (`list-Subscription-operations.xml`, `operationdefinition-Subscription-events.xml`, `operationdefinition-Subscription-status.xml`):** no changes.
- **Examples:** no changes.
- **Terminology (sibling `valueset-subscription-*.xml` / `codesystem-subscription-*.xml`):** no changes.

## Proposed Ballot Note (HTML)

No ballot note is proposed: nothing in the after-applied state has
changed for `Subscription` since `5d67a34a13a5`. If the ballot package
nevertheless requires a placeholder note for the artifact, the
following minimal block can be inserted in
`source/subscription/subscription-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to
  the Subscription resource since the prior ballot snapshot
  (<code>5d67a34a13a5</code>). Reviewers should focus on previously
  ballotted content; no new differential, search-parameter, operation,
  example, or terminology changes have been applied in this window.</p>
</blockquote>
```

## Notes for Reviewer

- The window `5d67a34a13a5..db79dcdfe196` contains 250 non-merge
  commits overall, none of which touched `source/subscription/`. Recent
  Subscription work in the cache clone (e.g., `0d0a26e141`
  "FHIR-47353 - subscription notification content clarifications",
  `ac3fd3079e` "FHIR-47344 …", `f64b39db58` "FHIR-47340 …",
  `910bea45a1` "FHIR-47337 …") all predates the since-commit and is
  therefore out of scope for this report.
- Cache clone HEAD (`db79dcdfe196`) is a descendant of the
  since-commit (`5d67a34a13a5`); ancestry confirmed via
  `git merge-base --is-ancestor`. No symmetric-difference fallback was
  needed.
- All FhirAugury services reported `healthy` at run time
  (GitHub / Jira / Zulip) via `services` `status` (the documented
  health-check action for this deployment).
- No `gh api` fallback was required; the since-commit was resolvable
  in the cached clone.

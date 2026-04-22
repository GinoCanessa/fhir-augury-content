# Artifact Ballot Note Draft: SubscriptionTopic (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `SubscriptionTopic` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 0 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `db79dcdfe196` |
| Generated | 2026-04-22T13:24:44Z |

## Source Files

Files considered part of `SubscriptionTopic` for this run (resolved
from the FhirCore folder `source/subscriptiontopic/`; the briefing's
Artifact Map does not list a per-resource entry, so the standard
FhirCore patterns were applied):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/subscriptiontopic/structuredefinition-SubscriptionTopic.xml` | StructureDefinition (canonical) | no |
| `source/subscriptiontopic/subscriptiontopic-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/subscriptiontopic/subscriptiontopic-notes.xml` | Supplementary narrative | no |
| `source/subscriptiontopic/bundle-SubscriptionTopic-search-params.xml` | Search parameters bundle | no |
| `source/subscriptiontopic/list-SubscriptionTopic-operations.xml` | Operations list | no |
| `source/subscriptiontopic/list-SubscriptionTopic-examples.xml` | Examples list | no |
| `source/subscriptiontopic/list-SubscriptionTopic-packs.xml` | Packs list | no |
| `source/subscriptiontopic/codesystem-subscriptiontopic-cr-behavior.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/subscriptiontopic/valueset-subscriptiontopic-cr-behavior.xml` | Artifact-scoped ValueSet | no |
| `source/subscriptiontopic/valueset-interaction-trigger.xml` | Artifact-scoped ValueSet | no |
| `source/subscriptiontopic/subscriptiontopic-definition-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/subscriptiontopic/subscriptiontopic-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/subscriptiontopic/subscriptiontopic-example.xml` | Example | no |
| `source/subscriptiontopic/subscriptiontopic-example-admission.xml` | Example | no |
| `source/subscriptiontopic/subscriptiontopic-example-admission-basic.xml` | Example | no |
| `source/subscriptiontopic/subscriptiontopic-example-admission-binary.xml` | Example | no |
| `source/subscriptiontopic/subscriptiontopic-example-admission-lm.xml` | Example | no |
| `source/subscriptiontopic/subscriptiontopic-example-admission-parameters.xml` | Example | no |
| `source/subscriptiontopic/subscriptiontopic-examples-header.xml` | Examples header | no |

Patterns from the standard FhirCore Artifact Map that produced no
match in the clone:

- `source/subscriptiontopic/subscriptiontopic-spreadsheet.xml` — no file (resource is SD-authored, no legacy spreadsheet).
- Sibling `structuredefinition-*.xml` other than the canonical — none present.

## Current Ballot Note

No existing ballot note. The intro file
(`source/subscriptiontopic/subscriptiontopic-introduction.xml`) and
notes file (`subscriptiontopic-notes.xml`) at HEAD
(`db79dcdfe196`) contain no `<blockquote class="ballot-note" …>`
block.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (none) | No tickets attributable — no commits touched the artifact in the window. | — |

`git log --no-merges 5d67a34a13a5..HEAD -- source/subscriptiontopic/`
returned no commits. The broader window contains 250 commits across
the repository, but none of them modified any
`SubscriptionTopic`-scoped file in the resolved file list above.

## Per-Ticket Detail

None — no commits were attributed to this artifact in the window.

## Roll-up Summary (after-applied state)

`git diff 5d67a34a13a5..HEAD -- <SubscriptionTopic file list>` is
empty. There are no changes to summarise:

- **StructureDefinition (`structuredefinition-SubscriptionTopic.xml`):** unchanged.
- **Intro / narrative (`subscriptiontopic-introduction.xml`, `subscriptiontopic-notes.xml`):** unchanged.
- **Search parameters (`bundle-SubscriptionTopic-search-params.xml`):** unchanged.
- **Operations (`list-SubscriptionTopic-operations.xml`):** unchanged.
- **Examples:** unchanged.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** unchanged.

No snapshot regeneration triggered by SubscriptionTopic-scoped changes
in this window.

## Proposed Ballot Note (HTML)

No new ballot note is proposed for this window. The artifact has not
changed since `5d67a34a13a5`, so there is nothing new for balloters
to be informed about, and no existing ballot note to revise.

If a ballot note is nevertheless desired (e.g., to retain a static
"no substantive change since the previous ballot" advisory), the
following minimal block could be inserted near the top of
`source/subscriptiontopic/subscriptiontopic-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been
  applied to <code>SubscriptionTopic</code> (StructureDefinition,
  search parameters, operations, examples, or scoped terminology)
  since the previous ballot snapshot.</p>
</blockquote>
```

This block carries no Jira citations because no tickets applied work
to the artifact in this window.

## Notes for Reviewer

- **Empty window for this artifact.** The since-commit
  (`5d67a34a13a5`) is reachable from HEAD (`db79dcdfe196`) and the
  fast-forward range contains 250 commits in total, but `git log`
  scoped to every file in the SubscriptionTopic file list returned
  zero commits. A second, broader pathspec check (folder + glob
  fallbacks `**/SubscriptionTopic*` and `**/subscriptiontopic*`) also
  returned zero, confirming there is genuinely no activity scoped to
  this artifact in the window.
- **No briefing Artifact Map entry.** The repo briefing did not
  contain an explicit `SubscriptionTopic` row in its Artifact Map, so
  the file list was assembled from the standard FhirCore patterns
  documented by this skill against `source/subscriptiontopic/`. If
  the briefing is later extended with a per-resource entry, re-run
  to confirm no extra files were missed.
- **No existing ballot note to carry forward.** The intro and notes
  files contain no `<blockquote class="ballot-note">` block at HEAD.
- **No `gh api` fallback used.** The cache clone resolved the
  since-commit and HEAD locally.

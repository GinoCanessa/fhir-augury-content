# Artifact Ballot Note Draft: Patient (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Patient` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 0 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:25:00Z |

> **No changes to artifact in window.** The since-commit is reachable
> from HEAD (250 non-merge commits in the range), but none of them
> touched any file in the resolved Patient file set. The current
> ballot note (none present) and the artifact's authored content are
> unchanged across `5d67a34a13a5..db79dcdfe196`.

## Source Files

Files considered part of `Patient` for this run (resolved from the
briefing's FhirCore Authoring root `source/<name>/` pattern; the
briefing has no per-artifact Artifact Map override, so the standard
FhirCore patterns from the skill were applied).

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/patient/structuredefinition-Patient.xml` | StructureDefinition (canonical) | no |
| `source/patient/patient-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/patient/patient-notes.xml` | Supplementary narrative | no |
| `source/patient/bundle-Patient-search-params.xml` | Search parameters | no |
| `source/patient/list-Patient-operations.xml` | Operations list | no |
| `source/patient/list-Patient-examples.xml` | Examples list | no |
| `source/patient/list-Patient-packs.xml` | Packs list | no |
| `source/patient/implementationguide-Patient-core.xml` | IG manifest fragment | no |
| `source/patient/operationdefinition-Patient-match.xml` | OperationDefinition `$match` | no |
| `source/patient/operationdefinition-Patient-purge.xml` | OperationDefinition `$purge` | no |
| `source/patient/operation-Patient-merge-notes.xml` | `$merge` operation notes | no |
| `source/patient/codesystem-administrative-gender.xml` | Artifact-scoped CodeSystem | no |
| `source/patient/codesystem-link-type.xml` | Artifact-scoped CodeSystem | no |
| `source/patient/valueset-link-type.xml` | Artifact-scoped ValueSet | no |
| `source/patient/valueset-patient-contactrelationship.xml` | Artifact-scoped ValueSet | no |
| `source/patient/patient-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/patient/patient-participant-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/patient/patient-participantcontactable-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/patient/patient-participantliving-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/patient/patient-example*.xml`, `patient-examples-*.xml`, `patient-genetics-example*.xml`, `patient-glossy-example*.xml` | Examples (24 files) | no |
| `source/patient/$*-request.txt`, `$*-response.txt`, `$merge-provenance.txt` | Operation request/response examples (9 files) | no |

Patterns from the skill that produced no match in the clone:

- `source/patient/patient-spreadsheet.xml` — no legacy spreadsheet for
  this resource (Patient is SD-authored only; consistent with the
  briefing's gotcha about SD authority).
- Sibling `structuredefinition-*.xml` whose stem differs from the
  folder — none present in `source/patient/`.

## Current Ballot Note

No existing ballot note. `source/patient/patient-introduction.xml` at
HEAD (`db79dcdfe196`) contains no `<blockquote class="ballot-note" …>`
element.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| _(none)_ | No commits in the window touched the Patient artifact's source files. | _(none)_ |

No `cross-referenced` lookup was performed because there were no
in-window commits to attribute.

## Per-Ticket Detail

_None — no tickets attributed._

## Roll-up Summary (after-applied state)

The diff `git diff 5d67a34a13a5..db79dcdfe196 -- <Patient file set>`
returned **no changes**. Specifically:

- **StructureDefinition (`structuredefinition-Patient.xml`):** unchanged.
  No differential element changes; no snapshot regeneration required
  on Patient's own behalf.
- **Intro / narrative (`patient-introduction.xml`, `patient-notes.xml`):**
  unchanged.
- **Search parameters (`bundle-Patient-search-params.xml`):** no
  parameters added, removed, or modified.
- **Operations (`list-Patient-operations.xml`,
  `operationdefinition-Patient-match.xml`,
  `operationdefinition-Patient-purge.xml`,
  `operation-Patient-merge-notes.xml`):** unchanged.
- **Examples:** no examples added, removed, or modified; no
  example refresh required for Patient itself.
- **Terminology (`codesystem-administrative-gender.xml`,
  `codesystem-link-type.xml`, `valueset-link-type.xml`,
  `valueset-patient-contactrelationship.xml`):** unchanged.

## Proposed Ballot Note (HTML)

No proposed ballot note. There are no substantive changes to Patient
since `5d67a34a13a5` to call out to balloters. If a placeholder note
is desired purely to inform balloters that Patient is unchanged
relative to the previous ballot, the following minimal block could be
inserted into `source/patient/patient-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made
  to the Patient resource since the previous ballot. The
  StructureDefinition, search parameters, operations
  (<code>$match</code>, <code>$purge</code>, <code>$merge</code>,
  <code>$everything</code>), examples, and resource-scoped
  terminology are unchanged across this ballot window.</p>
</blockquote>
```

This is offered for completeness only; the recommended action is to
**not** add a ballot note for Patient in this cycle.

## Notes for Reviewer

- The window contains 250 non-merge commits across `HL7/fhir`, but
  none touched any file under `source/patient/`. Two unrelated files
  outside Patient's authoring folder match the substring "patient" in
  the global diff stat
  (`source/messageheader/messagedefinition-patient-link-notification.xml`
  and `messagedefinition-patient-link-response.xml`); these belong to
  `MessageHeader` / messaging and are out of scope for the Patient
  artifact.
- HEAD (`db79dcdfe196`) is a descendant of since-commit
  (`5d67a34a13a5`); the linear `since..HEAD` range was used (no
  symmetric-difference fallback needed).
- The cache clone was authoritative; `gh api` was not required.
- The briefing is dated 2026-04-20 (clone HEAD `1b369ff` at analysis
  time); current clone HEAD is `db79dcdfe196`. The briefing's
  FhirCore Artifact Map / authoring conventions are still applicable
  — `source/patient/` exists and contains the expected file set.
- No existing ballot note was found to carry forward; nothing was
  dropped or superseded.

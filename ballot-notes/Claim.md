# Artifact Ballot Note Draft: Claim (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Claim` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 0 (touching `source/claim/`); 250 in repo overall |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `db79dcdfe196` |
| Generated | 2026-04-21T19:25:00Z |

## Source Files

Files considered part of `Claim` for this run (resolved from the
briefing's FhirCore Artifact Map / `source/claim/` folder convention).
None were modified between the since-commit and HEAD.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/claim/structuredefinition-Claim.xml` | StructureDefinition (canonical) | no |
| `source/claim/claim-introduction.xml` | Narrative intro (ballot note lives here) | no |
| `source/claim/claim-notes.xml` | Supplementary narrative | no |
| `source/claim/bundle-Claim-search-params.xml` | Search parameters bundle | no |
| `source/claim/list-Claim-operations.xml` | Operations list | no |
| `source/claim/list-Claim-examples.xml` | Examples list | no |
| `source/claim/list-Claim-packs.xml` | Packs list | no |
| `source/claim/operationdefinition-Claim-submit.xml` | `$submit` OperationDefinition | no |
| `source/claim/claim-example*.xml` (19 examples) | Examples | no |
| `source/claim/claim-examples-header.xml` | Examples header | no |
| `source/claim/claim-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/claim/claim-request-mapping-exceptions.xml` | Request mapping exceptions | no |
| `source/claim/valueset-*.xml` (artifact-scoped ValueSets, 38) | Terminology | no |
| `source/claim/codesystem-*.xml` (artifact-scoped CodeSystems, 17) | Terminology | no |
| `source/claim/$submit-request.txt`, `$submit-response.txt` | `$submit` examples | no |
| `source/claim/claim.svg` | Diagram | no |
| `source/claim/gg-testing-connectathon-9.xml` | Connectathon test artifact | no |

Patterns from the briefing that produced no match in the clone:
- `source/claim/claim-spreadsheet.xml` — no legacy spreadsheet (Claim
  is SD-authored; SD is authoritative).

## Current Ballot Note

No existing ballot note. The intro file (`source/claim/claim-introduction.xml`)
at HEAD contains only Scope/Usage and Boundaries-and-Relationships
narrative; no `<blockquote class="ballot-note" …>` block is present.

## Tickets Applied in Window

None. No commits in `5d67a34a13a5..db79dcdfe196` touched any file
under `source/claim/`.

## Per-Ticket Detail

None — no tickets attributable to changes in this artifact's files
during the window.

## Roll-up Summary (after-applied state)

**No changes to artifact in window.**

`git diff 5d67a34a13a5..db79dcdfe196 -- source/claim/` returns an
empty diff. The Claim resource's StructureDefinition, narrative,
search parameters, operations, examples, and artifact-scoped
terminology are byte-identical between the since-commit
(`5d67a34a13a5`, "bump version for publication", 2025-12-18) and the
current clone HEAD (`db79dcdfe196`, 2026-04-21). The 250 commits
that landed elsewhere in the repo during this window did not touch
Claim.

## Proposed Ballot Note (HTML)

No ballot note is proposed. The artifact is unchanged in the window,
there was no pre-existing ballot note to revise, and there is no new
material to flag for balloters. If a forward-looking note is desired
to confirm the artifact is being re-balloted as-is, that is an
editorial decision outside the scope of this skill (which only drafts
notes from observed changes).

## Notes for Reviewer

- HEAD is a descendant of the since-commit (`git merge-base
  --is-ancestor` returned 0); the linear range
  `5d67a34a13a5..db79dcdfe196` was used directly — no symmetric-
  difference fallback was needed.
- File enumeration used the `source/claim/` folder convention from
  the FhirCore briefing's Artifact Map; no `gh api` fallbacks were
  required.
- If the orchestrator expected changes here, double-check the
  since-commit — `5d67a34a13a5` is dated 2025-12-18 ("bump version
  for publication"), which may post-date the most recent Claim work
  in this branch.
- No related cross-artifact touch points were identified in the
  window for Claim's siblings (`ClaimResponse`,
  `ExplanationOfBenefit`, `CoverageEligibilityRequest`/`Response`);
  if a wider Financial-Management roll-up is desired, run this skill
  against those artifacts separately.

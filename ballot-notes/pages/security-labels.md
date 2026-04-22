# Page Ballot Note Draft: security-labels (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/security-labels.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (meta @ analyzed_at 2026-04-20, clone HEAD `1b369ff4e28e` at analysis time) |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `security-labels` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/security-labels.html` | Page source (ballot note lives here) | yes |

No `source/security-labels-notes.html` or `source/security-labels-examples.html` siblings exist at HEAD, so only the primary page source is in scope.

## Current Ballot Note

No existing ballot note. If a ballot note is added, the conventional location is at the top of the body of `source/security-labels.html`, immediately after the page title / intro paragraph (before the first `<h2>` section).

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55342](https://jira.hl7.org/browse/FHIR-55342) | Spelling/abbreviation issues on page: security | [`ff14caab3c24`](https://github.com/HL7/fhir/commit/ff14caab3c240e3f4684163140ec568b5c5338a8) |

## Per-Ticket Detail

### [FHIR-55342](https://jira.hl7.org/browse/FHIR-55342) — Spelling/abbreviation issues on page: security

- **Work group:** Security
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied-vote comment on the ticket links only to the implementing pull request: <https://github.com/HL7/fhir/pull/4028>. The original tracker description reads: "The page contains one or more misspelled or abbreviated words. Abbreviations need to be fully spelled out. Specifics: 'doesn't' 'isn't'."

- **Disposition summary:** A technical-correction request to expand contracted English forms (such as `doesn't`, `isn't`) to their fully spelled-out equivalents on the security pages, on grounds that abbreviated/contracted forms should be avoided in normative narrative. Resolution is **Persuasive** with status **Applied**.
- **Commits applying this ticket:**
  - [`ff14caab3c24`](https://github.com/HL7/fhir/commit/ff14caab3c240e3f4684163140ec568b5c5338a8) — FHIR-55342 - Spelling/abbreviation issues on page: security (2026-03-09, John Moehrke)
- **Changes applied (per Step 5b, scoped to this page):** Two contracted forms in narrative prose are expanded:
  - In the security-label property table, the `display` row description changes `doesn't` → `does not`.
  - In the "Break the Glass" section's introductory paragraph, `it's` → `it is`, `doesn't` → `does not`, and `wouldn't` → `would not`.
  No headings, conformance-language, examples, code snippets, diagrams, or cross-page links are touched. The diff is two single-line edits totalling 2 insertions and 2 deletions; the rendered semantics of the page are unchanged.

## Roll-up Summary (after-applied state)

The window contains one commit and the after-applied diff is purely editorial.

- **Section: `<h2>` security label property table (around line 75):** The `display` row's parenthetical changes contraction `doesn't` to `does not`. No semantic change.
- **Section: `<h2>Break the Glass</h2>` (around line 259):** The opening paragraph expands three contractions (`it's` → `it is`, `doesn't` → `does not`, `wouldn't` → `would not`). Wording, examples, and conformance language are otherwise unchanged.
- **Examples / code snippets:** None touched.
- **Diagrams / images:** None touched.
- **Cross-page links:** None touched.
- **Editorial cleanup:** The entire window is editorial — contraction-to-full-word expansion in narrative prose, with no normative or semantic impact.

## Proposed Ballot Note

Because the only change in the window is editorial contraction-expansion (a single Technical Correction with no normative impact), there is no substantive material to call out to balloters for `security-labels.html`. The most defensible options are, in order of preference:

1. **Add no ballot note.** The page has no existing ballot note and the window contains no substantive change. This is the recommended outcome — a ballot note that says only "we expanded `doesn't` to `does not`" adds noise without informing reviewers.
2. **Add a minimal editorial-only note** if the editor prefers to acknowledge the change explicitly. A suggested form, matching the FhirCore HTML convention, is below.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to this page since the previous ballot. Editorial cleanup only: contracted English forms (e.g., <code>doesn't</code>, <code>it's</code>, <code>wouldn't</code>) in the security-label property table and the "Break the Glass" introductory paragraph have been expanded to their fully spelled-out equivalents (<a href="https://jira.hl7.org/browse/FHIR-55342">FHIR-55342</a>).</p>
</blockquote>
```

## Notes for Reviewer

- The single commit in the window (`ff14caab3c24`) is attributed by its commit subject (`FHIR-55342 - …`); `cross-referenced` against the SHA returned no additional ticket associations.
- The applied-vote / disposition comment on FHIR-55342 in Jira contains only a link to PR <https://github.com/HL7/fhir/pull/4028>, with no narrative disposition text. The "Disposition (verbatim)" block above falls back to the tracker description per the skill's guidance.
- The ticket title references "page: security", but the change actually landed in `source/security-labels.html` (a sibling page in the same Security work-group cluster). A companion ticket / commit may have addressed `source/security.html` itself; that change, if any, belongs to a separate `notes-page` run for the `security` page and is out of scope here.
- No companion sibling files (`security-labels-notes.html`, `security-labels-examples.html`) exist at HEAD, so the page's working file list collapses to the single primary source.
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit (`5d67a34a13a5`); no symmetric-difference fallback was needed.
- Briefing `meta.json` records analysis at clone HEAD `1b369ff4e28e` (2026-04-20), which is older than the current clone HEAD (`db79dcdfe196`). The briefing is mildly stale in the sense that its clone snapshot has advanced, but the FhirCore page convention used here (`source/<page>.html`) is unchanged, so resolution is not affected.

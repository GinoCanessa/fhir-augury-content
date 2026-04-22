# Page Ballot Note Draft: credits (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/credits.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:25:00Z |

## Source Files

Files considered part of the `credits` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/credits.html` | Page source (ballot note lives here) | yes |

No `source/credits-notes.html` or `source/credits-examples.html` siblings exist at HEAD.

## Current Ballot Note

No existing ballot note. The credits page contains no `<blockquote class="ballot-note">` block at HEAD. If a ballot note were to be added, the conventional location would be at the top of the page body, immediately after the opening `<h2>Credits</h2>` heading and intro paragraph.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

The single commit in the window has no Jira ticket key in its subject or body and is not linked to any Jira ticket via FhirAugury cross-references (`cross-referenced` returned zero hits for the SHA).

## Per-Ticket Detail

### (unattributed)

- **Commits:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — *typos and bump kindling* (2026-03-18T13:14:07+11:00, Grahame Grieve)
- **Changes applied (per Step 5b, scoped to this page):**
  Single one-character typo correction in the contributor list: the affiliation for Reinhard Egelkraut was changed from "ComuGroup Medical" to "CompuGroup Medical" (line 117). No other lines in `source/credits.html` were touched.

## Roll-up Summary (after-applied state)

The full since-commit → HEAD diff for `source/credits.html` is a single one-line change inside the alphabetised contributor `<ul>`:

- **Section: contributor list (`Of particular note as contributors`):** Corrected the affiliation for Reinhard Egelkraut from "ComuGroup Medical" to "CompuGroup Medical".
- **Headings / structure:** No changes. No headings added, removed, or restructured.
- **Narrative / conformance language:** No changes. No `SHALL` / `SHOULD` / `MAY` deltas, no scope or boundary changes, no normative-status changes.
- **Examples / code snippets:** None present on this page; none added or removed.
- **Diagrams / images:** No changes.
- **Cross-page links:** No changes.
- **Editorial cleanup:** The entire window for this page consists of a single typo fix in one contributor name.

## Proposed Ballot Note

The credits page changes in this window are purely editorial (a one-character typo in a contributor affiliation) and do not warrant a ballot-note bullet. Per the "Editorial churn is not a ballot bullet" rule and the absence of any existing ballot note on this page, **no ballot note is proposed**.

If the editor nonetheless wishes to add a ballot note framing for completeness, the following minimal block would be appropriate; it should be inserted immediately after the opening `<h2>Credits</h2>` and intro paragraph:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to the Credits page since the previous ballot. Editorial cleanup only (a single contributor-affiliation typo correction).</p>
</blockquote>
```

The recommendation, however, is to add nothing.

## Notes for Reviewer

- The single commit in the window (`a9658ed97c2a`, "typos and bump kindling") is a sweep commit whose subject suggests it may have touched many files across the repo as part of a build/kindling bump. Only its `source/credits.html` hunk is in scope for this skill; any other file changes from that commit belong to the relevant `notes-artifact` / `notes-page` / `notes-datatype` runs for those files.
- FhirAugury `cross-referenced` returned zero hits for the commit SHA, and no `FHIR-NNNNN` / `UTG-NNNNN` keys appear in the commit subject or body, so the change is genuinely unattributed.
- HEAD of the cached clone is `db79dcdfe196` (`db79dcdfe196d35bd0e74c58c655a4c1c8f534f7`); the briefing's recorded `clone_head_sha` (`1b369ff4e28e`) is slightly behind but the since-commit is reachable from current HEAD as a fast-forward, so the standard `since-commit..HEAD` window applies. No symmetric-difference fallback was needed.
- No use of `gh api` was required; all commit metadata was resolved against the cached clone.

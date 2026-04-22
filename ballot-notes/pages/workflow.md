# Page Ballot Note Draft: workflow (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/workflow.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `workflow` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/workflow.html` | Page source (ballot note lives here) | yes |
| `source/workflow-examples.html` | Examples appendix | no |

Note: the conventional `source/workflow-notes.html` sibling does not exist
at HEAD. The `workflow-ad-hoc.html`, `workflow-communications.html`,
`workflow-management.html`, and `workflow-module.html` files are
**separate pages** in their own right (each rendered as its own page in the
spec) and are not in scope for this report.

## Current Ballot Note

No existing ballot note. If the editors decide a ballot note is warranted
for this window, the conventional location is at the top of the page body,
immediately after the page title / introductory paragraphs (before the
first `<a name="…">` anchor / `<h3>`).

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

The single commit in the window has no Jira key in its subject or body,
and `fhir-augury-cli cross-referenced` returned no hits for the SHA.

## Per-Ticket Detail

### (unattributed)

- **Commits applying this change:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — `typos and bump kindling` (2026-03-18, Grahame Grieve)
- **Changes applied (per Step 5b, scoped to this page):**
  In the "Workflow Resource Relationships" → workflow-resource list (the
  table that enumerates request / event / definition resources), the
  `‡` footnote superscript was removed from the **Transport** entry in
  the events list. The `‡` footnote (defined in the `listnotes` legend
  table further down the page) flags resources that "take on
  characteristics of both 'requests' and 'events' and thus shares
  characteristics from both patterns" — after this change, only **Task**
  carries that marker; Transport no longer does. The change is one line
  and is a cleanup / consistency fix; no narrative, no normative
  language, and no other markup was modified. (A stray CRLF line ending
  was introduced on the edited line.)

## Roll-up Summary (after-applied state)

- **Section: `<h4>Workflow Resource Relationships</h4>` — events resource list:**
  Removed the `‡` "shares request + event characteristics" footnote
  marker from the **Transport** entry. Task remains the only resource
  flagged with that marker. The `listnotes` legend table itself is
  unchanged.
- **Headings / structure / normative language / examples / diagrams /
  cross-page links:** No changes.
- **Editorial cleanup:** A single-character markup tweak (footnote
  marker removed) and a stray CRLF line ending on the edited line.

## Proposed Ballot Note

The only change in the window is a one-line footnote-marker cleanup with
no associated Jira ticket. This does not rise to the threshold of a
ballot note bullet (per the skill's "Editorial churn is not a ballot
bullet" rule), and there is no existing ballot note on the page to
revise or carry forward.

**Recommendation: do not add a ballot note for this window.** If the
editors nevertheless want a placeholder note acknowledging that the page
was reviewed and is otherwise unchanged since the previous ballot, the
following minimal block could be inserted at the top of the page body:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> No substantive changes have been made to
  this page since the previous ballot. The only edit in this window was
  a minor cleanup of a footnote marker in the workflow-resource list
  (see the <i>Workflow Resource Relationships</i> section). Reviewers
  should focus their attention on the per-resource pages
  (<a href="task.html">Task</a>, <a href="appointment.html">Appointment</a>,
  etc.) and on the sibling workflow pages
  (<a href="workflow-ad-hoc.html">Ad-hoc Workflow</a>,
  <a href="workflow-communications.html">Workflow Communications</a>,
  <a href="workflow-management.html">Workflow Management</a>) for
  ballot-relevant changes.</p>
</blockquote>
```

## Notes for Reviewer

- **No ticket attribution.** The single in-window commit
  (`a9658ed97c2a`) has no `FHIR-` key in its subject/body and no
  cross-references in FhirAugury. The change is editorial in nature
  ("typos and bump kindling"), consistent with that absence.
- **Sibling workflow pages out of scope.** `workflow-ad-hoc.html`,
  `workflow-communications.html`, `workflow-management.html`, and
  `workflow-module.html` are independent pages, not page-fragment
  siblings of `workflow.html`. If ballot notes are needed for any of
  those, run `notes-page` for each one separately.
- **Whitespace nit.** The edited line in the diff has a `^M` (CRLF
  ending) where the surrounding file uses LF. Worth a follow-up
  whitespace-only fix, but not ballot-relevant.
- **Briefing.** Used `cache/github/repos/HL7_fhir/repo-analysis/briefing.md`
  for repo category (FhirCore). Briefing was not consulted for page
  resolution because the FhirCore convention (`source/<page>.html`)
  applied directly.

# Page Ballot Note Draft: diagnostics-module (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/diagnostics-module.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `diagnostics-module` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/diagnostics-module.html` | Page source (ballot note lives here) | yes |

No `diagnostics-module-notes.html` or `diagnostics-module-examples.html` sibling
files exist at HEAD.

## Current Ballot Note

No existing ballot note. The proposed note will be inserted at the top of the
page body, immediately after the opening `<h2>` title block and before the
responsible-owner / standards-status table.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54964](https://jira.hl7.org/browse/FHIR-54964) | Diagnostic Module updates: Co-authors | [`aeb4890122be`](https://github.com/HL7/fhir/commit/aeb4890122becd32899ef50327ad7d91cec27b8d) |

## Per-Ticket Detail

### [FHIR-54964](https://jira.hl7.org/browse/FHIR-54964) — Diagnostic Module updates: Co-authors

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will adjust the responsible workgroup party to include CG and II and
  > include an acknowledgement section at the end similar to the one present
  > for the Clinical Reasoning Module.

- **Disposition summary:** The submitter asked that Clinical Genomics (CG) and
  Imaging Integration (II) be recognised as co-owners of the Diagnostic
  Module alongside Orders & Observations (OO). The work group agreed to add
  CG and II to the responsible-owner row of the module's metadata table and
  to add a closing acknowledgements section modelled on the one already
  present in the Clinical Reasoning Module.
- **Commits applying this ticket:**
  - [`aeb4890122be`](https://github.com/HL7/fhir/commit/aeb4890122becd32899ef50327ad7d91cec27b8d) — FHIR-54964: Add CG and II as co-responsible workgroups, add acknowledgements section (2026-02-28)
- **Changes applied (per Step 5b, scoped to this page):** The single commit
  edits the responsible-owner cell of the module's metadata table at the top
  of `source/diagnostics-module.html`, extending it from a single OO link
  (`[%wgt oo%]`) to a comma-separated list that also includes the CG
  (`[%wgt cg%]`) and II (`[%wgt ii%]`) work-group placeholders, which the
  publisher resolves to the corresponding work-group names and URLs. It also
  appends a new `Acknowledgements` section (`<a name="acknowledgements">`,
  `<h3>Acknowledgements</h3>`, plus a one-sentence paragraph) immediately
  before the `[%file newfooter%]` include, crediting OO, CG, and II for the
  combined work behind the module.

## Roll-up Summary (after-applied state)

The window contains a single, narrowly scoped change touching two locations
in `source/diagnostics-module.html`:

- **Section: module metadata table (top of page):** The "Responsible Owner:
  Work Group" cell now lists three work groups — Orders & Observations,
  Clinical Genomics, and Imaging Integration — instead of Orders &
  Observations alone. The `[%wg cg%] / [%wgt cg%]` and `[%wg ii%] / [%wgt
  ii%]` publisher placeholders are added inline so the rendered links pick
  up the canonical CG and II work-group URLs and titles.
- **Section: new `<h3>Acknowledgements</h3>` (end of page, before footer
  include):** A new anchored section (`<a name="acknowledgements">`) is
  appended at the bottom of the body with a single sentence stating that
  the resources and guidance in the module are the combined work of HL7
  Orders and Observations, Clinical Genomics, and Imaging Integration.
- **Examples / code snippets:** None.
- **Diagrams / images:** None.
- **Cross-page links:** None changed (the new placeholders point at existing
  work-group canonicals rendered by the publisher).
- **Editorial cleanup:** None.

## Proposed Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Since the previous ballot, the Diagnostic
  Module has been updated to recognise its multi-work-group ownership.
  Clinical Genomics and Imaging Integration are now listed alongside Orders
  &amp; Observations as co-responsible work groups for the module, and a
  new <a href="#acknowledgements">Acknowledgements</a> section has been
  added at the end of the page crediting the combined work of the three
  groups.</p>
  <ul>
    <li>Added Clinical Genomics and Imaging Integration to the
    "Responsible Owner: Work Group" row of the module metadata table at
    the top of the page, so the module is now jointly owned by OO, CG,
    and II
    (<a href="https://jira.hl7.org/browse/FHIR-54964">FHIR-54964</a>).</li>
    <li>Added a new <a href="#acknowledgements">Acknowledgements</a>
    section at the end of the module page acknowledging the combined work
    of the HL7 Orders and Observations, Clinical Genomics, and Imaging
    Integration Work Groups, modelled on the equivalent section in the
    Clinical Reasoning Module
    (<a href="https://jira.hl7.org/browse/FHIR-54964">FHIR-54964</a>).</li>
  </ul>
</blockquote>
```

Insert at the top of the page body, immediately after the opening
`<h2>Diagnostics Module</h2>` block and before the metadata table, matching
the placement used by ballot notes on other module pages in `HL7/fhir`.

## Notes for Reviewer

- The single commit in the window (`aeb4890122be`) returned no
  `cross-referenced` hits from `fhir-augury-cli`; ticket attribution was
  therefore taken solely from the `FHIR-54964:` prefix in the commit subject,
  which matches the disposition recorded in Jira (Applied, Persuasive with
  Modification, PR HL7/fhir#4015).
- No prior ballot note existed on this page, so there are no superseded or
  reverted bullets to carry forward or remove.
- No commits in the window touched files outside `source/diagnostics-module.html`,
  so no resource/profile/datatype follow-up to `notes-artifact` or
  `notes-datatype` is needed.
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit
  (`5d67a34a13a5`); a straight `since..HEAD` range was used.

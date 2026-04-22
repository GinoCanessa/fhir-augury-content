# Page Ballot Note Draft: medication-definition-module (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/medication-definition-module.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `medication-definition-module` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/medication-definition-module.html` | Page source (ballot note lives here) | yes |

No `-notes.html` or `-examples.html` siblings exist for this page at HEAD.

## Current Ballot Note

No existing ballot note. The proposed note will be inserted at the top of the
page body, immediately after the opening `<h2>` title (i.e., before the
introductory `<p>` describing what the module covers).

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55041](https://jira.hl7.org/browse/FHIR-55041) | Spelling/abbreviation issues on page: medication-definition-module | [`c57b4e6a7d45`](https://github.com/HL7/fhir/commit/c57b4e6a7d455bc2db2f619f0d6433027badcda5) |
| (unattributed) | — | [`c27b8ff89b8e`](https://github.com/HL7/fhir/commit/c27b8ff89b8e5e49888fd61b7ba8a0698d4561fe) |

## Per-Ticket Detail

### [FHIR-55041](https://jira.hl7.org/browse/FHIR-55041) — Spelling/abbreviation issues on page: medication-definition-module

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Change both instances of doesn't to does not, and change licence to license.

- **Disposition summary:** Reporter flagged that the page contained
  contracted forms ("doesn't") and a non-US spelling ("licence"), and that
  one of the "doesn't" instances rendered with a corrupted character. The
  WG agreed to expand the contractions to "does not" and to change
  "licence" to "license".
- **Commits applying this ticket:**
  - [`c57b4e6a7d45`](https://github.com/HL7/fhir/commit/c57b4e6a7d455bc2db2f619f0d6433027badcda5) — FHIR-55041 changed 2 doesn'ts to does nots (one had a bad character in it) changed licence to license fixed issue where the text that comes after the diagram gets wrapped to the side of the diagram on wide browsers. (2026-04-16)
- **Changes applied (per Step 5b, scoped to this page):**
  In the "Relationship to Prescribing" section, the contracted "doesn∩┐╜t"
  (containing a corrupted byte sequence) and the contracted "doesn't"
  later in the section were both expanded to "does not", and "drug licence
  approval" became "drug license approval". The same commit also restyled
  the inline `<img>` of the relationship diagram to render as a block
  element (`style="display: block"`) and moved it out of the surrounding
  `<p>`, so that the explanatory paragraph following the diagram no
  longer wraps alongside it on wide browsers. The image-wrap fix is a
  layout/editorial improvement and was not called out in the ticket
  disposition.

### (unattributed) — feedback-request paragraph removed

- **Commits applying this change:**
  - [`c27b8ff89b8e`](https://github.com/HL7/fhir/commit/c27b8ff89b8e5e49888fd61b7ba8a0698d4561fe) — removed old message about feedback, not relevant in R6 (2026-04-17)
- **Changes applied:**
  Deleted the closing italicised paragraph at the end of the
  "Boundaries and Relationships" / module-overview narrative that read
  *"BR&R welcomes feedback with evidence to show if these design
  decisions have made a solution that works, and is implementable, for
  users across a range of domains."* The author noted the request is no
  longer relevant in R6.

## Roll-up Summary (after-applied state)

Across the window, the page changed in three small ways; there is no
new normative content and no scope or boundary change.

- **Section: `<h3>Relationship to Prescribing</h3>`:**
  - Replaced "doesn∩┐╜t" and "doesn't" with "does not", and "licence"
    with "license", fixing a corrupted character and aligning with US
    spelling conventions used elsewhere in the spec ([FHIR-55041](https://jira.hl7.org/browse/FHIR-55041)).
  - Restructured the relationship-diagram markup so the `<img>` renders
    as a block element outside the surrounding `<p>`, preventing the
    following explanatory paragraph from wrapping beside the diagram on
    wide browsers (incidental layout fix, applied in the same commit as
    [FHIR-55041](https://jira.hl7.org/browse/FHIR-55041)).
- **End of module overview (post-"Transactional Use" paragraph):**
  - Removed the closing italicised paragraph requesting feedback on the
    design decisions ("*BR&R welcomes feedback with evidence …*"); the
    request is no longer relevant in R6 (unattributed,
    [`c27b8ff89b8e`](https://github.com/HL7/fhir/commit/c27b8ff89b8e5e49888fd61b7ba8a0698d4561fe)).
- **Examples / code snippets:** None added or removed.
- **Diagrams / images:** No image content changed; only the wrapping
  markup around `medication-definition-and-prescribing-resources.png`
  was adjusted (above).
- **Cross-page links:** None changed.
- **Editorial cleanup:** The spelling/contraction fixes and the
  feedback-paragraph removal are themselves editorial in nature and do
  not warrant a substantive ballot bullet beyond a brief note.

## Proposed Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Changes to this page since the previous ballot
  are editorial only. There are no scope, boundary, or normative changes to
  the Medication Definition module narrative in this cycle.</p>
  <ul>
    <li>Expanded contracted forms ("doesn't" → "does not"), corrected a
      corrupted character, and changed "licence" to "license" in the
      <i>Relationship to Prescribing</i> section
      (<a href="https://jira.hl7.org/browse/FHIR-55041">FHIR-55041</a>).</li>
    <li>Fixed a layout issue where text following the
      medication-definition / prescribing relationship diagram wrapped
      alongside the image on wide browsers; the diagram now renders as a
      block element with the explanatory paragraph below it
      (<a href="https://jira.hl7.org/browse/FHIR-55041">FHIR-55041</a>).</li>
    <li>Removed an outdated paragraph soliciting feedback on the module's
      design decisions, which is no longer relevant for R6.</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- No existing ballot note was present on this page, so the proposed note
  is a fresh insertion. Suggested placement: at the top of the page body,
  immediately after the `<h2>` title and before the introductory "This
  module is concerned with…" paragraph. Reviewers may prefer to omit a
  ballot note entirely given how minor the changes are.
- The image-wrap layout fix in commit `c57b4e6a7d45` was bundled with the
  FHIR-55041 spelling fixes but is not described in the ticket
  disposition. It is included in the proposed note for transparency; if
  the WG considers it purely editorial they may drop that bullet.
- Commit `c27b8ff89b8e` (feedback-paragraph removal) carries no Jira key
  in its message and the FhirAugury cross-reference index returned no
  hits for the SHA. It is reported under "(unattributed)" and rolled into
  the closing bullet of the proposed note without a Jira citation.
- No commits in the window touched files outside the page's scope, so
  there is nothing to defer to `notes-artifact` or `notes-datatype`.
- HEAD (`db79dcdfe196`) is a descendant of the since-commit; the
  fast-forward range was used directly.

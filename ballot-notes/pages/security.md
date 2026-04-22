# Page Ballot Note Draft: security (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/security.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 2 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `security` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/security.html` | Page source (ballot note lives here) | yes |

Conventional siblings (`source/security-notes.html`, `source/security-examples.html`) do not exist at HEAD and are not included.

## Current Ballot Note

A ballot note was added inside the window (commit [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a)) and is present at HEAD:

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> To ensure that security page is ready for Normative status, we are seeking ballot comments on the substantive content.</p>
    <ul>
    <li>The key changes made since the January 2026 R6 ballot include:</li>
      <ul>
      <li>Relaxed statement that security labels are often used. - <a href="https://jira.hl7.org/browse/FHIR-53718">FHIR-53718</a></li>
      </ul>
    </ul>
  </blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53718](https://jira.hl7.org/browse/FHIR-53718) | Are security labels often used? | [`8a2f3c289d5f`](https://github.com/HL7/fhir/commit/8a2f3c289d5ff9c0335aec196d339752bfd84c55) |
| [FHIR-55342](https://jira.hl7.org/browse/FHIR-55342) | Spelling/abbreviation issues on page: security | [`ff14caab3c24`](https://github.com/HL7/fhir/commit/ff14caab3c240e3f4684163140ec568b5c5338a8) |
| (unattributed) | Editorial: added ballot-note for changes since Jan ballot | [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a) |

## Per-Ticket Detail

### [FHIR-53718](https://jira.hl7.org/browse/FHIR-53718) — Are security labels often used?

- **Work group:** Security
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only ticket comment is a pointer to the implementing PR: <https://github.com/HL7/fhir/pull/4028>.

- **Disposition summary:** The submitter challenged the original wording that Patient-Sensitive resources "will often use" security labels, arguing this overstates real-world practice. The disposition reframes the statement as a normative recommendation rather than an empirical observation, and broadens the scope from confidentiality to confidentiality *and* sensitivity labels.
- **Commits applying this ticket:**
  - [`8a2f3c289d5f`](https://github.com/HL7/fhir/commit/8a2f3c289d5ff9c0335aec196d339752bfd84c55) — FHIR-53718 - Are security labels often used? (2026-03-09)
- **Changes applied (per Step 5b, scoped to this page):** In the "Patient Sensitive" section of the resource sensitivity classification, the sentence describing security-label usage was rewritten from "These Resources will often use the security labels to differentiate various confidentiality levels within this broad group of Patient Sensitive data." to "These Resources **SHOULD** use the security labels to differentiate various confidentiality **and sensitivity** levels within this broad group of Patient Sensitive data." This converts an empirical claim into a conformance recommendation and expands the dimensions covered by labels.

### [FHIR-55342](https://jira.hl7.org/browse/FHIR-55342) — Spelling/abbreviation issues on page: security

- **Work group:** Security
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only ticket comment is a pointer to the implementing PR: <https://github.com/HL7/fhir/pull/4028>.

- **Disposition summary:** Per Lloyd McKenzie's review (Comment 306), contracted forms on the security page were to be expanded to their full spellings to satisfy the project's prose conventions. The ticket explicitly cited "doesn't" and "isn't" as examples; the implementing commit also expanded other contractions encountered on the page.
- **Commits applying this ticket:**
  - [`ff14caab3c24`](https://github.com/HL7/fhir/commit/ff14caab3c240e3f4684163140ec568b5c5338a8) — FHIR-55342 - Spelling/abbreviation issues on page: security (2026-03-09)
- **Changes applied (per Step 5b, scoped to this page):** Pure editorial: contractions were expanded throughout the page — `doesn't` → `does not` (in the OAuth/RESTful authentication discussion and in the "Return a 404 'Not Found'" access-denied paragraph), `isn't` → `is not` (in the resource-identity prerequisites paragraph), `can't` → `cannot` (in the FHIR-narrative active-content cross-reference to `narrative.html#security`), and `won't` → `will not` (in the narrative-validation bullet). No semantic content changed.

### (unattributed) — added ballot-note for changes since Jan ballot

- **Commits:**
  - [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a) — added ballot-note for changes since Jan ballot (2026-03-10)
- **Changes applied (per Step 5b, scoped to this page):** Authoring/editorial commit (no Jira key in the commit message and no cross-reference in FhirAugury). It inserts a new `<blockquote class="ballot-note" id="bn1">` immediately above the page title, framing the page as Normative-readiness ballot content and listing the FHIR-53718 change as the only substantive bullet. The contraction-expansion work from FHIR-55342 is not represented in the new note.

## Roll-up Summary (after-applied state)

Diff: 1 file changed, 17 insertions(+), 7 deletions(-). All changes are in `source/security.html`; no siblings are touched.

- **Page header (above `<h1>FHIR Security</h1>`):** New `<blockquote class="ballot-note" id="bn1">` ballot-note block introduced. It frames the page as approaching Normative status and seeks ballot comment on substantive content; the only substantive bullet listed is the FHIR-53718 relaxation.
- **Section: "Patient Sensitive" (resource sensitivity classification, near `<h3>` for Patient-Sensitive resources):** The single sentence describing how Patient-Sensitive resources use security labels was rewritten — "will often use … to differentiate various confidentiality levels" became "**SHOULD** use … to differentiate various confidentiality **and sensitivity** levels." This is the only substantive normative-language change in the window (FHIR-53718).
- **Section: "Communication Security / Authentication" (around the OAuth/RESTful HTTP-call discussion, in an HTML comment block):** `doesn't` → `does not` (FHIR-55342, editorial).
- **Section: "Identity Management" (the paragraph on correctly identifying people, devices, locations, organizations):** `isn't` → `is not` (FHIR-55342, editorial).
- **Section: "Access Denied" responses:** `doesn't` → `does not` in the 404 "Not Found" bullet, and `doesn't` → `does not` in the 403 "Forbidden" bullet (FHIR-55342, editorial).
- **Section: "Narrative" (XHTML active-content discussion):** `can't contain active content` → `cannot contain active content` in the prose, and `won't handle it` → `will not handle it` in the narrative-validation list bullet (FHIR-55342, editorial).
- **Examples / code snippets:** None added, removed, or changed.
- **Diagrams / images:** None added, removed, or replaced.
- **Cross-page links:** No targets were redirected or removed; cross-references to `security-labels.html`, `consent.html`, `narrative.html#security`, `versions.html#std-process`, and external resources are unchanged.
- **Editorial cleanup:** Contraction expansions (`doesn't`/`isn't`/`can't`/`won't`) applied at five spots on the page (FHIR-55342). No whitespace/typo churn beyond that.

## Proposed Ballot Note

The existing note (id `bn1`) is retained and revised in place. Its existing FHIR-53718 bullet is preserved and tightened to reflect that the change is normative (SHOULD) and now covers both confidentiality and sensitivity. The FHIR-55342 contraction-expansion work is bundled into a single closing editorial sentence per the skill's editorial-churn rule, rather than added as a separate bullet.

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> To ensure that the security page is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since the January 2026 R6 ballot are:</p>
    <ul>
      <li>For Patient Sensitive resources, the recommendation on security labels was reframed from an empirical observation ("will often use") to a normative recommendation ("<b>SHOULD</b> use") and broadened from confidentiality only to confidentiality <b>and sensitivity</b> labels (<a href="https://jira.hl7.org/browse/FHIR-53718">FHIR-53718</a>).</li>
    </ul>
    <p>Editorial cleanup: contractions ("doesn't", "isn't", "can't", "won't") were expanded throughout the page (<a href="https://jira.hl7.org/browse/FHIR-55342">FHIR-55342</a>); no semantic change.</p>
  </blockquote>
```

## Notes for Reviewer

- The existing `bn1` block (added in [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a)) used a nested `<ul>` directly inside another `<ul>`, which is not valid HTML (a `<ul>` may only contain `<li>` children). The proposed note flattens the structure into a single-level list with the framing sentence in a leading `<p>`. Reviewers may prefer to keep the original nested style if that matches house style for ballot notes elsewhere in the spec.
- The original `bn1` did not mention FHIR-55342 even though that ticket landed in the same window. The proposed note adds it as a single editorial-cleanup sentence per the skill's "editorial churn is not a ballot bullet" rule. If the Security WG prefers to omit purely editorial dispositions from the ballot note, that sentence may be dropped.
- Neither FHIR-53718 nor FHIR-55342 has a recorded `resolution_description` or applied-vote disposition comment in Jira; both ticket comment streams contain only a pointer to PR <https://github.com/HL7/fhir/pull/4028>. The disposition summaries above are reconstructed from the ticket description plus the resolution code.
- The `services` action `health` documented in the skill is not implemented by this build of `fhir-augury-cli` (only `status` and `stats` are accepted); `cross-referenced` and `get` calls succeeded normally.
- No commits in the window touched `structuredefinition-*`, `bundle-*`, `valueset-*`, or `codesystem-*` files, so there is no spillover work for `notes-artifact` or `notes-datatype`.
- HEAD (`db79dcdfe196`) is a descendant of the since-commit (`5d67a34a13a5`); the linear `since..HEAD` window was used without falling back to symmetric difference.

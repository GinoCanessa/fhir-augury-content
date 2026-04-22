# Page Ballot Note Draft: medications-module (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/medications-module.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 1 (inferred from diff content — see Notes for reviewer) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (SHA-1 `28697D008733`; `meta.json` analyzed_at 2026-04-20) |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `medications-module` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/medications-module.html` | Page source (ballot note lives here) | yes |

No `source/medications-module-notes.html` or `source/medications-module-examples.html` sibling files exist at HEAD.

## Current Ballot Note

A ballot note (`id="bn1"`) was added inside the window by commit [`2b1fe4c966ab`](https://github.com/HL7/fhir/commit/2b1fe4c966ab0534ff1397cb94e46f4a70e4c086) and lightly tweaked by [`89dee5631672`](https://github.com/HL7/fhir/commit/89dee5631672c8015817245ebe832c5d11726ad1). It currently reads:

```html
 <blockquote class="ballot-note" id="bn1">
  <ul>
 <li>The key changes made since the January 2026 R6 ballot include:</li>
   <ul>
   <li>Corrections of typographical errors and rearrangement of Common Use Cases to group like use cases. - <a href="https://jira.hl7.org/browse/FHIR-53486">FHIR-53486</a></li>
   <li>Creation of an Additional Resources section with updated resource descriptions. - <a href="https://jira.hl7.org/browse/FHIR-53486">FHIR-53486</a></li>
  </ul>
</ul>
</blockquote>
```

Note: the markup nests a `<ul>` directly inside another `<ul>` (no enclosing `<li>`), which is invalid HTML; the proposed note below corrects this while preserving substance.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53486](https://jira.hl7.org/browse/FHIR-53486) | Updates to the Medications Module page | [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed), [`2b1fe4c966ab`](https://github.com/HL7/fhir/commit/2b1fe4c966ab0534ff1397cb94e46f4a70e4c086), [`89dee5631672`](https://github.com/HL7/fhir/commit/89dee5631672c8015817245ebe832c5d11726ad1) |

All three commits are attributed to **FHIR-53486** by inference: the substantive content commit (`4339778eb3f5`, "R6 ballot comment updates") implements the typo fixes, table restructure, description rewrites, and Common-Use-Case reordering described verbatim in FHIR-53486's resolution; the two follow-on commits (`2b1fe4c966ab`, `89dee5631672`) add and tidy the ballot-note blockquote that explicitly cites FHIR-53486. Neither commit message contains the ticket key, and `cross-referenced` returned no hits for any of the three SHAs — see Notes for reviewer.

## Per-Ticket Detail

### [FHIR-53486](https://jira.hl7.org/browse/FHIR-53486) — Updates to the Medications Module page

- **Work group:** Public Health
- **Resolution:** Persuasive (status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. (No comments returned by `fhir-augury-cli get` for FHIR-53486; the resolution body is captured under "Disposition summary" below from the ticket description.)

- **Disposition summary:** R6 ballot QA cleanup of `medications-module.html`: fix three text typos ("an 'Request'" → "a 'Request'"; "construct a patients" → "construct a patient's"; "stand alone … patients' medication list" → "stand-alone … patient's medication list"), split section 11.0.2 into Normative and Additional-Resources subsections by moving FormularyItem, ImmunizationEvaluation, and ImmunizationRecommendation into a new Additional Resources block, rewrite the ImmunizationRecommendation and ImmunizationEvaluation descriptions in 11.0.2.2 to flag them as Additional Resources, and reorder the Common Use Cases bullets so all medication use cases group together followed by the immunization use cases.
- **Commits applying this ticket:**
  - [`4339778eb3f5`](https://github.com/HL7/fhir/commit/4339778eb3f56eda5d28a552377b5185197b69ed) — R6 ballot comment updates (2026-03-06T14:53:48-06:00)
  - [`2b1fe4c966ab`](https://github.com/HL7/fhir/commit/2b1fe4c966ab0534ff1397cb94e46f4a70e4c086) — Add Note to Balloters for Immunizations and Medications Module (2026-03-09T15:22:49-07:00)
  - [`89dee5631672`](https://github.com/HL7/fhir/commit/89dee5631672c8015817245ebe832c5d11726ad1) — Updates to Notes to Balloters (2026-03-09T15:26:28-07:00)
- **Changes applied (per Step 5b, scoped to this page):**
  Commit `4339778eb3f5` is the substantive change: it fixes the three typos called out in the ticket, closes the existing Immunizations table after the `Immunization` row, and inserts a new `<a name="additional"></a><h4>Additional Resources</h4>` table containing rewritten `ImmunizationRecommendation` and `ImmunizationEvaluation` rows (now described as "Additional Resource designed to represent a patient's personalized point-in-time immunization recommendations…" and "Additional Resource intended to cover communicating the results of an evaluation … against a published schedule"). The same commit reorders the `Common Use Cases` `<ul>` so the dispensing, planned-therapy, and stand-alone medication-retrieval bullets immediately follow the existing medication bullets and precede the immunization bullets. Commit `2b1fe4c966ab` adds the `<blockquote class="ballot-note" id="bn1">` block summarising those changes; commit `89dee5631672` is editorial (removes a stray blank line above the blockquote). All three are coherent and reflected in the after-applied state.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a13a5..db79dcdfe196 -- source/medications-module.html` (1 file, +24/−12).

- **Top-of-page (header / pre-`<h2>Medications Module</h2>`):** New `<blockquote class="ballot-note" id="bn1">` inserted immediately after the Responsible-Owner / Standards-Status table, citing FHIR-53486. No other header changes.
- **Section: `<h4>Medications</h4>` (`#meds`) / `<h4>Immunizations</h4>` (`#imm`):** The single Immunizations table was split: the `Immunizations` table now contains only the `Immunization` row, and the previously co-located `ImmunizationRecommendation` / `ImmunizationEvaluation` rows were moved out (table closed with `</table>` after the `Immunization` row).
- **New section: `<h4>Additional Resources</h4>` (new `#additional` anchor):** Added a new `<table class="bare">` containing `ImmunizationRecommendation` and `ImmunizationEvaluation`. Both descriptions were rewritten to explicitly identify them as "Additional Resource" (incubator-hosted external resources): ImmunizationRecommendation is now described as personalized point-in-time recommendations forecasting eligibility against a published schedule; ImmunizationEvaluation is now described as communicating evaluation results against a published schedule (formerly "set of published recommendations (protocols)").
- **Section: `<h3>Common Use Cases</h3>` (`#uses`):** Bullet order changed. The dispensing-of-MedicationDispense bullet, the planned-medication-therapy / Care Plan bullet, and the stand-alone medication-retrieval bullet are now positioned immediately after the existing medication bullets (Placing a MedicationRequest; Listing current medications) and before the Immunization-related bullets (querying Immunizations; retrieving recommendations). The bullet text is unchanged apart from the `stand-alone` typo fix in the third moved bullet.
- **Editorial cleanup:** Three small text fixes in the prose tables — "an 'Request'" → "a 'Request'" (MedicationRequest description), "construct a patients" → "construct a patient's" (MedicationStatement description), and "stand alone request" → "stand-alone request" (Common Use Cases). One stray blank line removed above the new ballot note.
- **Cross-page links / diagrams / images:** None added, removed, or changed.

## Proposed Ballot Note

The proposed note retains the substance of the existing `bn1`, repairs the invalid `<ul>`-in-`<ul>` markup, adds a one-sentence framing paragraph, and tightens the bullets to name the specific structural change (the new `Additional Resources` section now containing the two incubator-hosted Immunization resources) alongside the use-case grouping and typo fixes.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The Medications Module page has been refreshed since the January 2026 R6 ballot to address Pharmacy / Public Health QA findings on the page itself; no resource-level normative changes are introduced by this page update.</p>
  <ul>
    <li>Restructured the resource index in section 11.0.2 by closing the existing <i>Immunizations</i> table after the <code>Immunization</code> row and adding a new <i>Additional Resources</i> subsection (<code>&lt;h4 id="additional"&gt;</code>) that contains <code>ImmunizationRecommendation</code> and <code>ImmunizationEvaluation</code>, with rewritten descriptions that identify both as Additional Resources hosted in the immunization incubator and update the ImmunizationEvaluation phrasing from "set of published recommendations (protocols)" to "published schedule" (<a href="https://jira.hl7.org/browse/FHIR-53486">FHIR-53486</a>).</li>
    <li>Reordered the <i>Common Use Cases</i> list so that all medication-related use cases (placing a request, listing current medications, dispensing, planned therapy, stand-alone medication retrieval) appear together, followed by the immunization-related use cases (<a href="https://jira.hl7.org/browse/FHIR-53486">FHIR-53486</a>).</li>
    <li>Editorial cleanup throughout the page (typo fixes: "an 'Request'" &rarr; "a 'Request'"; "patients 'Current Medications'" &rarr; "patient's 'Current Medications'"; "stand alone request" &rarr; "stand-alone request") (<a href="https://jira.hl7.org/browse/FHIR-53486">FHIR-53486</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Ticket attribution by inference.** None of the three commits in the window contain a `FHIR-#####` key in their subject or body, and `fhir-augury-cli cross-referenced` returned zero hits for each SHA. Attribution to FHIR-53486 was inferred from (a) the verbatim correspondence between the ticket's resolution description and the content changes in `4339778eb3f5`, and (b) the explicit `FHIR-53486` Jira link in the ballot-note blockquote added by `2b1fe4c966ab`. If ticket attribution must be evidence-only, the three commits should instead be listed as "(unattributed)" with the same roll-up.
- **No disposition comment recorded.** `fhir-augury-cli get` for FHIR-53486 returned `comments: []`, so the disposition summary above is paraphrased from the ticket description rather than quoted from an applied-vote comment.
- **Existing ballot note carried forward.** The current `bn1` was added inside this very window, so there are no prior bullets to drop; the proposed note revises wording for specificity (naming the new `#additional` subsection and the description rewrite) and fixes invalid HTML (`<ul>` directly inside `<ul>`).
- **Out-of-scope work in window:** none. No commits in the window touched `structuredefinition-*`, `bundle-*`, `valueset-*`, `codesystem-*`, `list-*-operations`, or `source/datatypes/**` files in the medications space, so no follow-on work is owed to `notes-artifact` or `notes-datatype` from this window.
- **Briefing freshness.** `cache/github/repos/HL7_fhir/repo-analysis/meta.json` records `analyzed_at: 2026-04-20T18:46:14Z` against `clone_head_sha` `1b369ff4e28e695908ed97d802bbad1e8ff32874`, which differs from the current cache HEAD `db79dcdfe196d35bd0e74c58c655a4c1c8f534f7`. The briefing was used only for category confirmation (FhirCore); the divergence does not affect this report.
- **HEAD reachability.** `5d67a34a13a5` is an ancestor of cache HEAD `db79dcdfe196`; no symmetric-difference fallback was needed. `gh api` was not used.

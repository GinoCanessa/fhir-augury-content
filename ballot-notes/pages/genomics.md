# Page Ballot Note Draft: genomics (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/genomics.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 1 (FHIR-55078); 1 commit unattributed |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (consulted; FhirCore convention applies) |
| Generated | 2026-04-21T20:00:00Z |

## Source Files

Files considered part of the `genomics` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/genomics.html` | Page source (ballot note lives here) | yes |

No conventional sibling files (`source/genomics-notes.html`, `source/genomics-examples.html`) exist at HEAD. The `source/genomicstudy/` directory belongs to the `GenomicStudy` resource artifact (handled by `notes-artifact`) and is intentionally excluded.

## Current Ballot Note

A ballot note was added inside the window (commit `2b25386194839b7dd9bee870c5a736c5c1245aa5`) and is present at HEAD:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this genomics page is ready for Normative status, we are seeking ballot comments on the content.</p>
  <ul>
  <li>The changes made since R5:</li>
    <ul>
    <li>Correct misspellings and spell out abbreviated words: <a href="https://jira.hl7.org/browse/FHIR-55078">FHIR-55078</a></li>
    </ul>
  </ul>
</blockquote>
```

The proposed revision (Step 7) keeps the `id="bn1"` and the existing FHIR-55078 bullet, refines the framing paragraph, and adds bullets for the other material changes that landed in the window.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55078](https://jira.hl7.org/browse/FHIR-55078) | Spelling/abbreviation issues on page: genomics | [`e6eb42ea7994`](https://github.com/HL7/fhir/commit/e6eb42ea7994d933c4bcafba975a84a267d1877b) |
| (unattributed) | — | [`2b2538619483`](https://github.com/HL7/fhir/commit/2b25386194839b7dd9bee870c5a736c5c1245aa5) |

`fhir-augury-cli cross-referenced` returned no hits for either commit SHA. FHIR-55078 was attributed by inspecting the diff and the ballot-note text added by commit `2b2538`, which explicitly cites that ticket as the driver for the spelling/abbreviation cleanup performed in commit `e6eb42`.

## Per-Ticket Detail

### [FHIR-55078](https://jira.hl7.org/browse/FHIR-55078) — Spelling/abbreviation issues on page: genomics

- **Work group:** FHIR Infrastructure
- **Resolution:** Persuasive (Status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The ticket records the original comment ("The page contains one or more misspelled or abbreviated words. Abbreviations need to be fully spelled out. Specifics: 'timeframe.'") and tracking comments noting that suggested text was drafted to "accomplish the spirit of this request" and explicitly identifying the abbreviations to spell out: "CNV, or SNV" and "BAM, CRAM" (Patrick Werner, work-group call).

- **Disposition summary:** Reviewers asked the editors to remove or expand opaque abbreviations on the genomics page. The work-group call accepted the request as Persuasive and scoped the change to the file-format abbreviations in the intro paragraph (BAM, CRAM, VCF) and the variant-class abbreviations in the GenomicStudy bullet (CNV, SNV), rather than rewriting the whole page.
- **Commits applying this ticket:**
  - [`e6eb42ea7994`](https://github.com/HL7/fhir/commit/e6eb42ea7994d933c4bcafba975a84a267d1877b) — Corrections and updates to the genomics guidance page (2026-03-18)
- **Changes applied (per Step 5b, scoped to this page):**
  In the page intro, the sentence describing what bioinformaticists historically worked with was rewritten from "such artifacts as alignment (e.g., BAM, CRAM) and variant calling (e.g., VCF) data files, we are now seeing tremendous interest" to the abbreviation-free "domain-specific data files, we are seeing tremendous interest". In the resource bullet list, the GenomicStudy bullet's example methods were rewritten from "karyotyping, CNV, or SNV detection" to "karyotyping, detection of sequence variants". The same commit also reordered the resource list so the GenomicStudy bullet appears before the Molecular Definition IG paragraph and reflowed the Molecular Definition IG paragraph onto multiple lines (no rendered-content change). The reorder and reflow are not strictly required by FHIR-55078, but they were bundled into the same commit.

### (unattributed)

- **Commits applying without ticket attribution:**
  - [`2b2538619483`](https://github.com/HL7/fhir/commit/2b25386194839b7dd9bee870c5a736c5c1245aa5) — Add ballot note and changes summary in genomics.html (2026-03-19)
- **Changes applied (per Step 5b, scoped to this page):**
  Inserts a new `<blockquote class="ballot-note" id="bn1">` block immediately after the standardisation-status table (before the opening "The era of precision medicine" paragraph). The block tells balloters that the page is being put forward for Normative status and lists "Correct misspellings and spell out abbreviated words" with a link to FHIR-55078. No other narrative content is touched.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a..HEAD -- source/genomics.html` (37 lines changed: +27/-10).

- **Section: standardisation-status table → intro:** A new `<blockquote class="ballot-note" id="bn1">` block was inserted between the standardisation-status table and the opening narrative paragraph. It announces the Normative-readiness intent and points balloters at FHIR-55078.
- **Section: page intro paragraph ("The era of precision medicine…"):** The clause naming specific bioinformatics file formats — "such artifacts as alignment (e.g., BAM, CRAM) and variant calling (e.g., VCF) data files" — was replaced with the abbreviation-free phrase "domain-specific data files". The sentence still establishes the historical bioinformatics-only audience, just without naming file formats. Driven by [FHIR-55078](https://jira.hl7.org/browse/FHIR-55078).
- **Section: "Resources of relevance to genomics" bullet list:** The `GenomicStudy` bullet was moved up so it now appears immediately after the `MolecularDefinition` bullet and before the "Molecular Definition Implementation Guide" bullet (previously it sat at the end of the list). The bullet's example-methods phrase was changed from "karyotyping, CNV, or SNV detection" to "karyotyping, detection of sequence variants" (also FHIR-55078). The `MolecularDefinition` bullet itself is unchanged.
- **Examples / code snippets:** None added or removed.
- **Diagrams / images:** None added or removed.
- **Cross-page links:** No outgoing links were added, removed, or retargeted; existing links to the cg-incubator and molecular-definition-data-types IGs are preserved.
- **Editorial cleanup:** The "Molecular Definition Implementation Guide for Molecular Data Types" paragraph was reflowed from a single long line onto multiple lines so each `<a>` element sits on its own line. The rendered content is identical.

## Proposed Ballot Note

The existing `bn1` block already covers the FHIR-55078 abbreviation cleanup. The revision below preserves that bullet, sharpens the framing paragraph (so reviewers understand which sections changed), adds a bullet for the GenomicStudy bullet reorder + wording tweak that landed in the same commit, and notes the editorial reflow at the end.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The genomics guidance page is being put forward for Normative status. Substantive content is unchanged since R5; this ballot is seeking comments on the framing of the page intro and the catalogue of genomics-related resources and IGs. Changes since R5 are listed below.</p>
  <ul>
    <li>Removed file-format abbreviations from the page intro and from the GenomicStudy resource bullet: the intro no longer names "BAM", "CRAM", or "VCF" data files, and the GenomicStudy bullet's example methods now read "karyotyping, detection of sequence variants" rather than "karyotyping, CNV, or SNV detection" (<a href="https://jira.hl7.org/browse/FHIR-55078">FHIR-55078</a>).</li>
    <li>Reordered the "Resources of relevance to genomics" bullet list so the <a href="https://build.fhir.org/ig/HL7/cg-incubator/StructureDefinition-GenomicStudy.html">GenomicStudy</a> resource is introduced alongside the other resource entries (immediately after MolecularDefinition) rather than after the Molecular Definition Implementation Guide. No content was added or removed; only the presentation order changed.</li>
    <li>Editorial: reflowed the Molecular Definition Implementation Guide paragraph for readability of the source markup. No rendered-content change.</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The existing ballot note (added in commit `2b2538` and present at HEAD) cites only FHIR-55078. The roll-up shows two additional non-editorial changes — the GenomicStudy bullet reorder and the wording change from "CNV, or SNV detection" → "detection of sequence variants" — that were bundled into the same commit (`e6eb42`) under the generic message "Corrections and updates to the genomics guidance page". The wording change is squarely in scope of FHIR-55078; the bullet reorder is not strictly required by that ticket but no separate ticket was found. The proposed revision attributes both items to FHIR-55078 (the wording change explicitly, the reorder implicitly via the same commit). Reviewer should confirm whether a separate ticket covers the reorder or whether FHIR-55078 should be widened.
- `fhir-augury-cli cross-referenced` returned zero hits for both commit SHAs in the window. FHIR-55078 attribution comes entirely from the diff content (the ballot-note bullet added by commit `2b2538` cites it directly) and from FHIR-55078's own comments naming the BAM/CRAM/VCF/CNV/SNV abbreviations as the targets.
- No commits in the window touched files outside `source/genomics.html`, so there is no spillover to flag for `notes-artifact` or `notes-datatype`.
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit (`5d67a34a13a5`); a fast-forward range was used. No symmetric-difference fallback was needed.
- A formal "applied-vote" comment with the disposition text was not recorded on FHIR-55078; the disposition above is reconstructed from the work-group call comments (Patrick Werner / James Jones) on the ticket.
- `fhir-augury-cli services health` is not a valid action in this build (use `services status`); `services status` reports all backends healthy. No `gh api` fallback was needed because both commits are present in the cache clone.

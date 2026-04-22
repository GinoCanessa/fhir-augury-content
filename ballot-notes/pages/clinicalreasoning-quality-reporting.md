# Page Ballot Note Draft: clinicalreasoning-quality-reporting (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/clinicalreasoning-quality-reporting.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `clinicalreasoning-quality-reporting` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/clinicalreasoning-quality-reporting.html` | Page source (ballot note lives here) | yes |

No `-notes.html` or `-examples.html` siblings exist for this page at HEAD.

## Current Ballot Note

A ballot note exists at HEAD (it was added during this window — there was no ballot-note block at the since-commit). Verbatim:

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> Key changes made since FHIR 6.0.0-ballot4:</p>
    <ul>
        <li>Non-compatible Changes
            <ul>
                <li>None</li>
            </ul>
        </li>
        <li>Compatible, Substantive Changes
            <ul>
                <li>None</li>
            </ul>
        </li>
        <li>Non-substantive Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55079">FHIR-55079</a>: Incomplete content indicated on: clinicalreasoning-quality-reporting</li>
            </ul>
        </li>
    </ul>
    <p></p>
</blockquote>
<blockquote style="background-color: lightblue">
    <p><b>All Changes (including Technical Corrections not listed above):</b></p>
    <ul>
        <li>None</li>
    </ul>
</blockquote>
```

The companion light-blue "All Changes" block lists "None"; it should be updated to enumerate FHIR-55079 alongside the ballot note (see "Notes for reviewer").

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55079](https://jira.hl7.org/browse/FHIR-55079) | Incomplete content indicated on: clinicalreasoning-quality-reporting | [`cc4e4ed3495a`](https://github.com/HL7/fhir/commit/cc4e4ed3495ae5c40d4e754ba06bc0df89e61fe7) |

## Per-Ticket Detail

### [FHIR-55079](https://jira.hl7.org/browse/FHIR-55079) — Incomplete content indicated on: clinicalreasoning-quality-reporting

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Even though it was not necessary, we agree to change the language.
  >
  > Remove "To do this using criteria-based stratifiers" and replace with
  >
  > "Doing this using criteria-based stratifiers is not recommended because it"
  >
  > leave the rest of the sentence "would require specifying a stratifier expression for each possible combination of age range group and gender. With even larger stratifications, this is untenable."

- **Disposition summary:** The reporter flagged the phrase "To do" in the page as implying incomplete/missing content. CQI agreed (while noting it was a stylistic rather than semantic problem) to rephrase the offending sentence in the component-stratifiers discussion so the prose no longer reads as a "to do" placeholder.
- **Commits applying this ticket:**
  - [`cc4e4ed3495a`](https://github.com/HL7/fhir/commit/cc4e4ed3495ae5c40d4e754ba06bc0df89e61fe7) — [FHIR-55079](https://jira.hl7.org/browse/FHIR-55079): Incomplete content indicated on: clinicalreasoning-quality-reporting (2026-04-20)
- **Changes applied (per Step 5b, scoped to this page):** In the *Component Stratifiers* subsection (under *Stratifiers*), the sentence introducing the age-range × gender stratification example was rephrased from "To do this using criteria-based stratifiers would require specifying a stratifier expression for each possible combination of age range group and gender. With even larger stratifications, this is untenable." to "Doing this using criteria-based stratifiers is not recommended because it would require specifying a stratifier expression for each possible combination of age range group and gender. With even larger stratifications, this is untenable." The change is purely editorial — semantics are preserved, the recommendation against criteria-based stratifiers for combinatorial cases is now stated explicitly rather than implied. The same commit also inserted the page's ballot-note block (and the companion "All Changes" blockquote) at the top of the page, immediately after the standards-status table, and added a single trailing blank line before `[%file newfooter%]`.

## Roll-up Summary (after-applied state)

The diff between `5d67a34a13a5..db79dcdfe196` for `source/clinicalreasoning-quality-reporting.html` consists of:

- **Top of page (new ballot-note infrastructure):** A `<div>` containing a `<blockquote class="ballot-note" id="bn1">` plus a light-blue "All Changes" companion blockquote was inserted immediately after the responsible-owner / standards-status table. The ballot note advertises FHIR 6.0.0-ballot4 → current as the comparison baseline, lists no non-compatible or compatible substantive changes, and lists FHIR-55079 as the sole non-substantive change. The "All Changes" companion currently lists "None".
- **Section: *Component Stratifiers* (under *Stratifiers*):** One sentence reworded from "To do this using criteria-based stratifiers would require…" to "Doing this using criteria-based stratifiers is not recommended because it would require…" The surrounding prose, code samples, headings, and cross-references are unchanged.
- **Examples / code snippets:** No changes (the surrounding CQL `define "Age Range Stratifier"` / `define "Gender Stratifier"` / `define "Age Range and Gender Stratifier"` blocks are untouched).
- **Diagrams / images:** No changes.
- **Cross-page links:** No changes.
- **Editorial cleanup:** A single trailing blank line was added before `[%file newfooter%]`. No other typographical churn.

## Proposed Ballot Note

The existing ballot note is already accurate for the after-applied state — the only ticket landed in the window is FHIR-55079, and it is a non-substantive wording change. The proposed revision below preserves the existing `id="bn1"`, retains the three-bucket (non-compatible / compatible-substantive / non-substantive) structure already in use on this page, and adds a one-sentence framing paragraph derived from the roll-up summary so reviewers know what to look for.

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> The only normative change to this page since FHIR 6.0.0-ballot4 is an editorial rewording in the <i>Component Stratifiers</i> section to remove "to do" phrasing that read as a placeholder; the underlying guidance is unchanged.</p>
    <p>Key changes made since FHIR 6.0.0-ballot4:</p>
    <ul>
        <li>Non-compatible Changes
            <ul>
                <li>None</li>
            </ul>
        </li>
        <li>Compatible, Substantive Changes
            <ul>
                <li>None</li>
            </ul>
        </li>
        <li>Non-substantive Changes
            <ul>
                <li>Reworded the introductory sentence of the age-range × gender stratification example in <i>Component Stratifiers</i> from "To do this using criteria-based stratifiers would require…" to "Doing this using criteria-based stratifiers is not recommended because it would require…", removing language that read as a "to do" placeholder (<a href="https://jira.hl7.org/browse/FHIR-55079">FHIR-55079</a>)</li>
            </ul>
        </li>
    </ul>
</blockquote>
<blockquote style="background-color: lightblue">
    <p><b>All Changes (including Technical Corrections not listed above):</b></p>
    <ul>
        <li>Editorial rewording in <i>Component Stratifiers</i> (<a href="https://jira.hl7.org/browse/FHIR-55079">FHIR-55079</a>)</li>
    </ul>
</blockquote>
```

## Notes for Reviewer

- The page had no ballot-note block at the since-commit; the block was introduced inside this window by the same commit that applied FHIR-55079. The proposed note above keeps the page's three-bucket structure (matching what the editor seeded) so it remains consistent with whatever batch convention CQI is following.
- The companion light-blue "All Changes" blockquote currently lists "None" at HEAD. That is inconsistent with the ballot-note block immediately above it, which lists FHIR-55079. The proposed revision populates that list with the FHIR-55079 entry; reviewers should confirm this matches the page's intended convention before accepting.
- `fhir-augury-cli cross-referenced` returned zero hits for the commit SHA; ticket attribution comes from the `[FHIR-55079]` token in the commit subject, which matches the disposition text exactly.
- No commits in the window touched files outside this page's scope, so there is nothing to hand off to `notes-artifact` or `notes-datatype`.
- HEAD (`db79dcdfe196`) is a descendant of the since-commit; the standard `since..HEAD` window was used.

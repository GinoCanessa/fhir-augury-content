# Artifact Ballot Note Draft: Group (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Group` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 1 (FHIR-45508) + 2 unattributed commits |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `Group` for this run (from `source/group/` per the FhirCore briefing's Artifact Map):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/group/structuredefinition-Group.xml` | StructureDefinition (canonical) | yes |
| `source/group/group-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/group/group-notes.xml` | Supplementary narrative | yes |
| `source/group/bundle-Group-search-params.xml` | Search parameters | no |
| `source/group/list-Group-operations.xml` | Operations list | no |
| `source/group/list-Group-examples.xml` | Examples list | no |
| `source/group/list-Group-packs.xml` | Implementation packs list | no |
| `source/group/operationdefinition-Group-everything.xml` | $everything operation | no |
| `source/group/operationdefinition-Group-purge.xml` | $purge operation | no |
| `source/group/implementationguide-Group-core.xml` | Core IG entry | no |
| `source/group/group-examples-header.xml` | Examples header narrative | no |
| `source/group/group-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/group/group-participant-mapping-exceptions.xml` | Participant mapping exceptions | no |
| `source/group/group-example*.xml` (12 files) | Examples (3 touched: `conceptualcohortdefinition-cancer-except-subset`, `eligibility-criteria-ada-rec-bariatric`, `outcomedefinition-hba1c-at-12-months`) | partial |
| `source/group/valueset-*.xml` (8 files) | Artifact-scoped ValueSets | no |
| `source/group/codesystem-*.xml` (6 files) | Artifact-scoped CodeSystems | no |

No briefing patterns produced empty matches; the legacy `group-spreadsheet.xml` is absent (resource is SD-authored — expected for current FhirCore conventions).

## Current Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> The key changes made since FHIR 6.0.0-ballot4 include:</p>
<p>Moved the section on the Inclusion and Exclusion Criteria from the Scope and Usage to the Group notes.</p>
<p>The Group.characteristic.timing element is now called Group.characteristic.relativeTime</p>
<ul>
<li>The definition for it has been changed to "The relative time in which the characteristic is determined."</li>
<li>The short description is now "When (with respect to an event)"</li>
<li>Updated the Group examples for this element change.</li>
</ul>
<p>The following elements have their definitions revised:</p>
<ul>
<li>Group.combinationMethod, before: "Used to specify how two or more characteristics are combined." To now: "Used to specify how two or more characteristics are combined.&#xA;&#xA;* 'all-of': Each of the characteristics must be met. This is functionally equivalent to combining all characteristics with an AND operator.&#xA;* 'any-of': At least one of the characteristics must be met. This is functionally equivalent to combining all characteristics with an OR operator.&#xA;* 'at-least': At least n of the characteristics must be met. Use Group.combinationThreshold to specify the value of n.&#xA;* 'at-most': At most n of the characteristics must be met. Use Group.combinationThreshold to specify the value of n.&#xA;*  'except-subset': The characteristics expressed as exclusion criteria are used as exceptions to meeting the characteristics expressed as inclusion criteria."</li>
<li>Group.characteristic.method, before: "Method for how the characteristic value was determined." To now: "The method modifies the Group.characteristic.code and indicates how the value is to be determined."</li>
</ul>
<p>The following elements have their short descriptions revised:</p>
<ul>
<li>Group.characteristic.instances[x]: "Number of occurrences"</li>
<li>Group.characteristic.duration[x]: "How long"</li>
<li>Group.characteristic.period: "When (in calendar time)"</li>
</ul>
<p>Added a comment to the Group.characteristic.offset element: "As an example, to express a characteristic of a calcium level greater than the normal limit or a hemoglobin level less than 1 g/dL below the reference range, the offset concept would represent &quot;normal limit&quot; [upper limit] or &quot;reference range&quot; [lower limit]."</p>
</blockquote>
```

A sibling Release Notes blockquote (`<blockquote style="background-color: lightblue">`) cites `FHIR-45508` and was added in the same commit window.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508) | Duration element should not be a choice type | [`8892f7afb459`](https://github.com/HL7/fhir/commit/8892f7afb459a1e8cb5c13aa6118fd8f05c49c20), [`be5c0d9e5bf5`](https://github.com/HL7/fhir/commit/be5c0d9e5bf5f2d7dc70ef16eb8e1645cc3a4b1b), [`c5d713b7ff5f`](https://github.com/HL7/fhir/commit/c5d713b7ff5f36e601fa6ff25618fb35c0257ff5), [`6d145d350cf2`](https://github.com/HL7/fhir/commit/6d145d350cf2d3e1d241efa0aadd414b0d2c69e7) |
| (unattributed) | Ballot note authoring + formatting | [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8), [`a088d67c58c6`](https://github.com/HL7/fhir/commit/a088d67c58c6d9d0acfc9fdb2ba4777144dfa9e9) |

`fhir-augury-cli cross-referenced` returned zero hits for all six commit SHAs; ticket attribution is therefore based solely on the `J#NNNNN` markers in the commit subjects (regex `(FHIR|UTG)-\d+` plus the `J#` shorthand the FHIR-I editor uses).

## Per-Ticket Detail

### [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508) — Duration element should not be a choice type

- **Work group:** FHIR Infrastructure
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > 1. Rename the timing element to relativeTime to avoid the implication that the element is of type Timing.
  >
  > 2. Add examples and discussion to the Notes section, specifically documenting examples for the need and use of the duration, period, and relativeTime elements, as described in this PR: https://github.com/HL7/fhir/pull/3998/files

- **Disposition summary:** Although the ticket originated as a request to drop `Range` from `Group.characteristic.duration[x]`, the work group concluded that `duration`, `period` and `timing` are independent and all needed, but that `Group.characteristic.timing` was misleadingly named (implementers were assuming the `Timing` datatype). The disposition therefore renames `timing` to `relativeTime` (datatype unchanged: `RelativeTime`) and asks for substantially expanded usage notes covering when each of `duration`, `period`, and `relativeTime` apply.
- **Commits applying this ticket:**
  - [`6d145d350cf2`](https://github.com/HL7/fhir/commit/6d145d350cf2d3e1d241efa0aadd414b0d2c69e7) — J#45508 updated the Group short and descriptions (2025-12-03)
  - [`c5d713b7ff5f`](https://github.com/HL7/fhir/commit/c5d713b7ff5f36e601fa6ff25618fb35c0257ff5) — J#45508 moved "Defining Group Inclusion and Exclusion Criteria" from group-introduction to group-notes (2025-12-03)
  - [`be5c0d9e5bf5`](https://github.com/HL7/fhir/commit/be5c0d9e5bf5f2d7dc70ef16eb8e1645cc3a4b1b) — J#45508 Group notes improvement (2025-12-03)
  - [`8892f7afb459`](https://github.com/HL7/fhir/commit/8892f7afb459a1e8cb5c13aa6118fd8f05c49c20) — J#45508 changed the element name from timing to relativeTime (2025-12-10)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `structuredefinition-Group.xml`: renamed the element `Group.characteristic.timing` → `Group.characteristic.relativeTime` (path, id, short and definition all updated; cardinality and `RelativeTime` type unchanged); revised short labels for `instances[x]` ("Number of occurrences"), `duration[x]` ("How long"), `period` ("When (in calendar time)"), and `relativeTime` ("When (with respect to an event)"); rewrote the definition of `Group.combinationMethod` to enumerate each of the five `all-of`/`any-of`/`at-least`/`at-most`/`except-subset` codes inline; rewrote the definition of `Group.characteristic.method`; added a `<comment>` on `Group.characteristic.offset` with a calcium / haemoglobin worked example. The snapshot will need regeneration.
  - In `group-introduction.xml`: removed the entire "Defining Group Inclusion and Exclusion Criteria" section (membership / combinationMethod / characteristic.code / value / exclude / description / method / formula / determiner / offset / instances / duration / period / timing element guidance) from Scope and Usage.
  - In `group-notes.xml`: re-added that guidance under a new `<a name="inclusion-exclusion-criteria">` section, with the rename `timing` → `relativeTime` propagated through the prose and the JSON examples, the `method`/`formula`/`determiner` write-ups consolidated under a "Describing how the characteristic value is determined" sub-heading, and `period`/`relativeTime` consolidated under "Describing when the characteristic value is present".
  - In the three trial / cohort examples (`group-example-conceptualcohortdefinition-cancer-except-subset.xml`, `group-example-eligibility-criteria-ada-rec-bariatric.xml`, `group-example-outcomedefinition-hba1c-at-12-months.xml`): every `<timing>` wrapper was renamed to `<relativeTime>` (5 instances total). No content inside the wrappers changed.

### (unattributed) — Ballot note authoring + formatting

- **Commits:**
  - [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8) — Added two sections for balloters (2026-03-30, khalid_shahin)
  - [`a088d67c58c6`](https://github.com/HL7/fhir/commit/a088d67c58c6d9d0acfc9fdb2ba4777144dfa9e9) — improved formatting (2026-03-30, khalid_shahin)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `group-introduction.xml`: added the `<blockquote class="ballot-note" id="bn1">…</blockquote>` whose text documents the FHIR-45508 work above, and a sibling Release Notes blockquote linking `FHIR-45508`. Both blocks were inserted at the top of the first `<div>` of the intro file. The follow-up commit tightened whitespace inside the new bullets — no semantic change. These commits document, rather than perform, the FHIR-45508 work.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a..HEAD` over the 6 files actually touched (40 source files in scope, 6 changed; +112 / −93 lines):

- **StructureDefinition (`structuredefinition-Group.xml`):**
  - Element renamed: `Group.characteristic.timing` → `Group.characteristic.relativeTime` (path/id/short/definition updated; type remains `RelativeTime`; cardinality unchanged at `0..*`).
  - Element short labels rewritten for parallelism: `instances[x]` → "Number of occurrences"; `duration[x]` → "How long"; `period` → "When (in calendar time)"; `relativeTime` → "When (with respect to an event)".
  - Element definitions rewritten:
    - `Group.combinationMethod` definition expanded inline to enumerate each of the five concept codes (was a one-line summary).
    - `Group.characteristic.method` re-worded to "The method modifies the Group.characteristic.code and indicates how the value is to be determined."
  - Added `<comment>` on `Group.characteristic.offset` providing a calcium-level / haemoglobin worked example.
  - No cardinality, type, binding, constraint, or `<differential>` element-add/remove changes beyond the rename. Snapshot regeneration required.
- **Intro / narrative (`group-introduction.xml`, `group-notes.xml`):**
  - The "Defining Group Inclusion and Exclusion Criteria" subsection was relocated from the intro's *Scope and Usage* to the *Group notes* page, where it is now anchored as `inclusion-exclusion-criteria`.
  - During the move, prose was reorganised: `method`/`formula`/`determiner` are presented together under a "Describing how the characteristic value is determined" heading, and `period`/`relativeTime` together under "Describing when the characteristic value is present"; `timing` references in the prose and the inline JSON example were updated to `relativeTime`.
  - A `<blockquote class="ballot-note" id="bn1">` summarising these ballot-cycle changes (and a Release Notes blockquote citing FHIR-45508) were inserted at the top of `group-introduction.xml`.
- **Search parameters (`bundle-Group-search-params.xml`):** no changes in window.
- **Operations (`list-Group-operations.xml`, `operationdefinition-Group-everything.xml`, `operationdefinition-Group-purge.xml`):** no changes in window.
- **Examples:** three existing examples updated (`conceptualcohortdefinition-cancer-except-subset`, `eligibility-criteria-ada-rec-bariatric`, `outcomedefinition-hba1c-at-12-months`) — purely the `<timing>`→`<relativeTime>` element rename to track the SD; no example-level content or list (`list-Group-examples.xml`) changes.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** no changes in window. The Group-scoped value sets and code systems (group-type, group-membership-basis, group-characteristic-combination, characteristic-offset, definition-method, etc.) are unchanged.

## Proposed Ballot Note (HTML)

The existing `bn1` already reflects the after-applied state accurately; the proposed note retains the existing `id="bn1"` and the existing structure, with two minor edits: (a) tighten the `combinationMethod` and `method` bullets (the verbatim before/after pasting in the current note is hard to read in a balloter context), and (b) add an explicit Jira citation to each bullet so balloters can trace each item to FHIR-45508.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The key changes to <code>Group</code> since FHIR 6.0.0-ballot4 are concentrated in the <em>characteristic</em> back-bone and its surrounding usage notes; no elements were added or removed and all cardinalities are unchanged.</p>
  <ul>
    <li><b>Element renamed:</b> <code>Group.characteristic.timing</code> is now <code>Group.characteristic.relativeTime</code> (datatype <code>RelativeTime</code> unchanged). The short description is now "When (with respect to an event)" and the definition is "The relative time in which the characteristic is determined." All shipped Group examples have been updated to use the new element name (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li><b>Usage guidance relocated:</b> the "Defining Group Inclusion and Exclusion Criteria" walk-through (covering <code>membership</code>, <code>combinationMethod</code>, and every <code>characteristic.*</code> element) has moved from the Scope and Usage section into the <a href="group-notes.html#inclusion-exclusion-criteria">Group notes</a>, and was reorganised so that <code>method</code>/<code>formula</code>/<code>determiner</code> are described together, and <code>period</code>/<code>relativeTime</code> are described together (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li><b>Definitions clarified:</b> <code>Group.combinationMethod</code>'s definition now enumerates each of the <code>all-of</code> / <code>any-of</code> / <code>at-least</code> / <code>at-most</code> / <code>except-subset</code> codes inline; <code>Group.characteristic.method</code>'s definition was rewritten to "The method modifies the Group.characteristic.code and indicates how the value is to be determined." (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li><b>Short descriptions tightened</b> for parallelism across the time/quantity-style elements: <code>characteristic.instances[x]</code> = "Number of occurrences", <code>characteristic.duration[x]</code> = "How long", <code>characteristic.period</code> = "When (in calendar time)", <code>characteristic.relativeTime</code> = "When (with respect to an event)" (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li><b>New comment on <code>Group.characteristic.offset</code></b> illustrating intended use with a calcium-level / haemoglobin worked example: the offset concept would represent "normal limit" [upper limit] or "reference range" [lower limit] (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Single ticket window.** All material in-scope changes derive from FHIR-45508; the two "unattributed" commits are the act of writing the ballot-note + Release-Notes blockquotes themselves and a one-commit formatting fix. They should be considered part of the FHIR-45508 disposition for ballot purposes, even though their commit messages omit the `J#45508` marker.
- **Disposition divergence from original ask.** The ticket as filed asked to drop `Range` from `Group.characteristic.duration[x]`. The work group declined that and instead renamed `timing` → `relativeTime` and improved usage notes. Balloters following the original Jira description may be surprised; the proposed note above frames the actual landed change rather than the original request.
- **Snapshot is stale in the diff.** The `<snapshot>` was not regenerated in any of these commits; the diff narrated above is from the `<differential>`. A snapshot rebuild is required before publication.
- **No cross-repo touch points.** The changed value set / code system bindings on the renamed element are unchanged, so no UTG companion change is implied. The 5W mapping exception files were not touched (the `Group.characteristic.timing` row in `mappings.xml` may still need a follow-up rename — out of scope for this artifact's source folder, flagged here for the editor).
- **Existing ballot note is accurate.** Every bullet in the existing `bn1` survives in the after-applied state; the proposed revision keeps the same scope and `id`, adds inline Jira citations, and replaces the verbatim before/after definition dumps with a more balloter-readable summary.

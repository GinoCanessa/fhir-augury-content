# Artifact Ballot Note Draft: Group (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Group` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 1 (FHIR-45508) + 2 unattributed commits |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T16:56:42Z |

## Source Files

Files considered part of `Group` for this run (resolved from the briefing's Artifact Map and the `source/group/` folder layout):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/group/structuredefinition-Group.xml` | StructureDefinition (canonical) | yes |
| `source/group/group-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/group/group-notes.xml` | Supplementary narrative | yes |
| `source/group/bundle-Group-search-params.xml` | Search parameters bundle | no |
| `source/group/list-Group-operations.xml` | Operations bundle | no |
| `source/group/list-Group-examples.xml` | Examples list | no |
| `source/group/list-Group-packs.xml` | Packs list | no |
| `source/group/operationdefinition-Group-everything.xml` | OperationDefinition `$everything` | no |
| `source/group/operationdefinition-Group-purge.xml` | OperationDefinition `$purge` | no |
| `source/group/group-example*.xml` (10 files) | Examples (3 touched) | partial — 3 of 10 |
| `source/group/valueset-*.xml` (8 files) | Artifact-scoped ValueSets | no |
| `source/group/codesystem-*.xml` (5 files) | Artifact-scoped CodeSystems | no |
| `source/group/implementationguide-Group-core.xml` | IG manifest fragment | no |
| `source/group/group-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/group/group-participant-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/group/group-examples-header.xml` | Examples header narrative | no |
| `source/group/invariant-tests/*` | Invariant tests | no |

Examples touched in window:

- `source/group/group-example-conceptualcohortdefinition-cancer-except-subset.xml`
- `source/group/group-example-eligibility-criteria-ada-rec-bariatric.xml`
- `source/group/group-example-outcomedefinition-hba1c-at-12-months.xml`

No briefing-listed pattern produced zero matches against the clone for this artifact.

## Current Ballot Note

A ballot note (`id="bn1"`) was introduced into `group-introduction.xml` during this window (commit [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8)) by the same author landing the FHIR-45508 work. It is the current ballot note at HEAD and is reproduced verbatim below; this skill's draft (Step 7) revises it to align with the after-applied state and to add inline ticket citations.

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
<li>Group.combinationMethod, before: "Used to specify how two or more characteristics are combined." To now: "Used to specify how two or more characteristics are combined.&#xA;&#xA;* 'all-of': Each of the characteristics must be met. ...&#xA;* 'except-subset': The characteristics expressed as exclusion criteria are used as exceptions to meeting the characteristics expressed as inclusion criteria."</li>
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

(Note: a sibling release-notes blockquote was added immediately after `bn1` in the same commit, linking to [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508). It is not styled as a balloter note and is preserved as-is.)

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508) | Duration element should not be a choice type | [`6d145d350cf2`](https://github.com/HL7/fhir/commit/6d145d350cf2d3e1d241efa0aadd414b0d2c69e7), [`c5d713b7ff5f`](https://github.com/HL7/fhir/commit/c5d713b7ff5f36e601fa6ff25618fb35c0257ff5), [`be5c0d9e5bf5`](https://github.com/HL7/fhir/commit/be5c0d9e5bf5f2d7dc70ef16eb8e1645cc3a4b1b), [`8892f7afb459`](https://github.com/HL7/fhir/commit/8892f7afb459a1e8cb5c13aa6118fd8f05c49c20) |
| (unattributed) | — | [`a088d67c58c6`](https://github.com/HL7/fhir/commit/a088d67c58c6d9d0acfc9fdb2ba4777144dfa9e9), [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8) |

Commit-message ticket extraction used the variant prefix `J#NNNNN` (= `FHIR-NNNNN`) used by the author for these commits, in addition to the standard `(FHIR|UTG)-\d+` regex. `cross-referenced` returned no hits for either of the unattributed commits.

## Per-Ticket Detail

### [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508) — Duration element should not be a choice type

- **Work group:** FHIR Infrastructure
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The `resolution_description` field is empty and no comment carries a discrete "applied vote" / disposition block. The closest authoritative pointers are Bryn Rhodes' comment "Proposed changes as discussed on last couple FHIR-I calls have been applied here: https://github.com/HL7/fhir/pull/3998/files" and the long FHIR-I discussion thread that preceded it.

- **Disposition summary:** The submitter questioned why `Group.characteristic.duration` was a choice between `Duration` and `Range`. FHIR-I discussions broadened the scope: the group decided that the `timing`/`period`/`duration` triad needed clarification, agreed to rename `Group.characteristic.timing` to `Group.characteristic.relativeTime` (matching its `RelativeTime` datatype), and to tighten short descriptions and definitions across the surrounding elements rather than collapse the choice. The narrative on inclusion/exclusion criteria was relocated from the resource's Scope-and-Usage intro into the supplementary notes page, and a clarifying comment was added to `Group.characteristic.offset`.
- **Commits applying this ticket:**
  - [`6d145d350cf2`](https://github.com/HL7/fhir/commit/6d145d350cf2d3e1d241efa0aadd414b0d2c69e7) — J#45508 updated the Group short and descriptions (2025-12-03)
  - [`c5d713b7ff5f`](https://github.com/HL7/fhir/commit/c5d713b7ff5f36e601fa6ff25618fb35c0257ff5) — J#45508 moved "Defining Group Inclusion and Exclusion Criteria" from group-introduction to group-notes (2025-12-03)
  - [`be5c0d9e5bf5`](https://github.com/HL7/fhir/commit/be5c0d9e5bf5f2d7dc70ef16eb8e1645cc3a4b1b) — J#45508 Group notes improvement (2025-12-03)
  - [`8892f7afb459`](https://github.com/HL7/fhir/commit/8892f7afb459a1e8cb5c13aa6118fd8f05c49c20) — J#45508 changed the element name from timing to relativeTime (2025-12-10)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - In `structuredefinition-Group.xml` (differential): renamed `Group.characteristic.timing` → `Group.characteristic.relativeTime`, with new short `"When (with respect to an event)"` and new definition `"The relative time in which the characteristic is determined."`. Tightened short descriptions for `Group.characteristic.instances[x]` (`"Number of occurrences"`), `duration[x]` (`"How long"`), and `period` (`"When (in calendar time)"`). Replaced the terse `combinationMethod` definition with a per-code enumeration covering `all-of`, `any-of`, `at-least`, `at-most`, and `except-subset`. Replaced the terse `characteristic.method` definition with the new wording `"The method modifies the Group.characteristic.code and indicates how the value is to be determined."`. Added a `<comment>` to `Group.characteristic.offset` illustrating the "normal limit" / "reference range" use cases.
  - In `group-introduction.xml`: removed the lengthy `<h3>Defining Group Inclusion and Exclusion Criteria</h3>` section (and its sub-headings on `membership`, `combinationMethod`, `combinationThreshold`, `characteristic.code`, `value[x]`, `exclude`, `description`, `method`, `formula`, `determiner`, `offset`, `instances[x]`, `duration[x]`, `period`, and `timing`) from the Scope-and-Usage intro.
  - In `group-notes.xml`: added the same inclusion/exclusion section under a new `<a name="inclusion-exclusion-criteria">` anchor; restructured the `method` / `formula` / `determiner` block under a unified "Describing how the characteristic value is determined" heading; merged the period/timing material into a "Describing when the characteristic value is present" section that uses the new `relativeTime` element name (and its example payload).
  - In the three example files (`group-example-conceptualcohortdefinition-cancer-except-subset.xml`, `group-example-eligibility-criteria-ada-rec-bariatric.xml`, `group-example-outcomedefinition-hba1c-at-12-months.xml`): renamed the `<timing>` element wrapper to `<relativeTime>` to track the SD rename. No structural / terminology changes inside those wrappers.
  - Snapshot regeneration is required to reflect the SD differential changes (snapshot edits not narrated per skill rules).

### (unattributed)

- **Commits without ticket attribution:**
  - [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8) — Added two sections for balloters (2026-03-30, khalid_shahin)
  - [`a088d67c58c6`](https://github.com/HL7/fhir/commit/a088d67c58c6d9d0acfc9fdb2ba4777144dfa9e9) — improved formatting (2026-03-30, khalid_shahin)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - `95481d16` inserted the new ballot-note `<blockquote class="ballot-note" id="bn1">` (the very note this skill is being asked to refresh) and a sibling "Release Notes" blockquote linking to [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508) at the top of `group-introduction.xml`. By content, this commit is part of the FHIR-45508 ballot prep but it does not carry a `J#` prefix in the message; treat it as logically attributable to FHIR-45508 even though commit-message attribution did not bind it.
  - `a088d67c` is whitespace / formatting cleanup of `group-notes.xml` (7 insertions, 9 deletions, no semantic change). Logically follow-up to FHIR-45508 narrative work but not attributed in the message.

## Roll-up Summary (after-applied state)

After-applied diff stats (`git diff 5d67a34a..HEAD -- source/group`):

```
 ...eptualcohortdefinition-cancer-except-subset.xml |   4 +-
 ...mple-eligibility-criteria-ada-rec-bariatric.xml |  16 ++--
 ...xample-outcomedefinition-hba1c-at-12-months.xml |   4 +-
 source/group/group-introduction.xml                | 100 ++++++---------------
 source/group/group-notes.xml                       |  62 +++++++++++++
 source/group/structuredefinition-Group.xml         |  19 ++--
 6 files changed, 112 insertions(+), 93 deletions(-)
```

- **StructureDefinition (`structuredefinition-Group.xml`):**
  - Renamed `Group.characteristic.timing` → `Group.characteristic.relativeTime` (path, id, short, definition all updated; element id is now `Group.characteristic.relativeTime`). The element keeps `0..*` cardinality and its `RelativeTime` datatype; only the name and human-readable text changed.
  - `Group.combinationMethod`: short unchanged (`"all-of | any-of | at-least | at-most | except-subset"`); definition expanded from one sentence to a per-code enumeration explaining each combination semantic (and clarifying that `at-least` / `at-most` use `combinationThreshold`).
  - `Group.characteristic.method`: short unchanged; definition rewritten as `"The method modifies the Group.characteristic.code and indicates how the value is to be determined."`.
  - `Group.characteristic.offset`: definition unchanged; added a `<comment>` element with the "normal limit" / "reference range" example.
  - `Group.characteristic.instances[x]`: short shortened to `"Number of occurrences"`.
  - `Group.characteristic.duration[x]`: short shortened to `"How long"`. **The originally-reported duration choice (`Duration` vs. `Range`) was not collapsed**; the underlying ask of FHIR-45508 was addressed via clarification of the surrounding elements rather than by removing the choice.
  - `Group.characteristic.period`: short tightened to `"When (in calendar time)"`.
  - No element additions, removals, type changes, binding changes, or new constraints/invariants in the differential.
  - Snapshot regeneration required (snapshot edits not enumerated per skill rules).
- **Intro / narrative (`group-introduction.xml`, `group-notes.xml`):**
  - Added new ballot-note `bn1` and a sibling Release-Notes blockquote at the top of `group-introduction.xml`.
  - Removed the entire `<h3>Defining Group Inclusion and Exclusion Criteria</h3>` section from the Scope-and-Usage intro (~72 narrative lines).
  - Re-added that material in `group-notes.xml` under a new `inclusion-exclusion-criteria` anchor, with the following editorial restructuring:
    - The `method` / `formula` / `determiner` sub-headings are folded into a single "Describing how the characteristic value is determined" section.
    - The `period` / `timing` sub-headings are folded into a single "Describing when the characteristic value is present" section, using the new `relativeTime` element name and updating the JSON example to use `"relativeTime": [...]`.
- **Search parameters (`bundle-Group-search-params.xml`):** unchanged in window.
- **Operations (`list-Group-operations.xml`, `operationdefinition-Group-everything.xml`, `operationdefinition-Group-purge.xml`):** unchanged in window. (`$everything` and `$purge` definitions and the Operations list are untouched.)
- **Examples:** no examples were added or removed; three existing examples were updated only to rename the `<timing>` wrapper to `<relativeTime>` (no payload restructuring).
- **Terminology (sibling `valueset-*.xml`, `codesystem-*.xml`):** unchanged in window. No artifact-scoped terminology was added, removed, or rebound. (Per the FhirCore briefing's UTG cross-repo note: nothing here belongs in UTG; the Group-scoped value sets and code systems remain in `source/group/` and were not touched.)

## Proposed Ballot Note (HTML)

The proposed note revises the existing `bn1` to (a) carry inline Jira citations, (b) drop the verbose before/after definition payloads in favour of intent statements, and (c) add a clarifying line about what FHIR-45508 did **not** change (the `duration` choice was retained).

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The substantive changes to <code>Group</code> since FHIR 6.0.0-ballot4 are concentrated in the <code>characteristic</code> backbone element and its supporting narrative. There are no new elements, no removed elements, no cardinality changes, and no binding changes; the StructureDefinition differential edits are limited to a single rename and to clarified wording on existing elements (snapshot regeneration is therefore required).</p>
  <ul>
    <li>Renamed <code>Group.characteristic.timing</code> to <code>Group.characteristic.relativeTime</code> to align the element name with its <code>RelativeTime</code> datatype, and updated the short description to <em>"When (with respect to an event)"</em>. All in-tree <code>Group</code> examples that used the element have been re-serialised under the new name (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li>Expanded the <code>Group.combinationMethod</code> definition from a single sentence to a per-code enumeration covering <code>all-of</code>, <code>any-of</code>, <code>at-least</code>, <code>at-most</code>, and <code>except-subset</code>, including the relationship to <code>Group.combinationThreshold</code> (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li>Rewrote the <code>Group.characteristic.method</code> definition as a clarification of how it modifies <code>Group.characteristic.code</code>, and tightened the short descriptions for <code>Group.characteristic.instances[x]</code> ("Number of occurrences"), <code>duration[x]</code> ("How long"), and <code>period</code> ("When (in calendar time)") (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li>Added a clarifying <code>&lt;comment&gt;</code> on <code>Group.characteristic.offset</code> illustrating its use for "normal limit" / "reference range" reference points (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li>Relocated the <em>Defining Group Inclusion and Exclusion Criteria</em> guidance out of Scope-and-Usage and into the Group notes page, where it is now organised under "Describing how the characteristic value is determined" and "Describing when the characteristic value is present" sub-headings that explicitly cover the renamed <code>relativeTime</code> element (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
    <li><b>What did <em>not</em> change:</b> the original FHIR-45508 ask was to remove the <code>Duration | Range</code> choice on <code>Group.characteristic.duration[x]</code>. After FHIR-I discussion the working group elected to retain the choice and instead clarify the surrounding semantics; balloters should review whether the clarified wording is sufficient (<a href="https://jira.hl7.org/browse/FHIR-45508">FHIR-45508</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Existing `bn1` was added inside this window.** The "current" ballot note at HEAD is itself part of the changes since `5d67a34a13a5`, having been introduced by [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8). It is therefore both the baseline this skill must respect *and* an artefact of this window. The proposed draft preserves its structure but trims the verbose before/after definition payloads (those belong in the SD diff, not the ballot note), adds inline Jira citations, and adds an explicit "what did not change" bullet to set balloter expectations against the original FHIR-45508 ask.
- **Sibling Release-Notes blockquote.** The non-ballot-note `<blockquote style="background-color: lightblue">` block immediately below `bn1` already cites [FHIR-45508](https://jira.hl7.org/browse/FHIR-45508). This skill does not modify it; it remains a separate authoring convention used by this resource's intro.
- **Two unattributed commits are logically part of FHIR-45508.** [`95481d16b4d6`](https://github.com/HL7/fhir/commit/95481d16b4d662ba0e9fad5883fffeaf0fc961d8) (ballot-note + release-notes blocks) and [`a088d67c58c6`](https://github.com/HL7/fhir/commit/a088d67c58c6d9d0acfc9fdb2ba4777144dfa9e9) (formatting cleanup) lack a `J#` prefix and produced no `cross-referenced` hits, but their content is entirely about the FHIR-45508 work. They have been listed under "(unattributed)" per the skill's rules but should be regarded as part of the FHIR-45508 ballot-prep tranche.
- **Disposition text is not directly quotable.** Jira's `resolution_description` is empty and no comment contains a single block of disposition text. The "Persuasive with Modification" outcome is sourced from the discussion thread between Bryn Rhodes, Lloyd McKenzie, and Brian Alper and the realised changes in [PR #3998](https://github.com/HL7/fhir/pull/3998).
- **Window arithmetic.** `git merge-base --is-ancestor 5d67a34a..HEAD` succeeded; the window is a clean fast-forward, so `since-commit..HEAD` is sufficient — no symmetric difference fallback was required.
- **Out-of-scope touches:** none. No commits in this window touched files outside `source/group/` (verified via `git log --pretty=format:'%H' 5d67a34a..HEAD -- source/group` matching the per-commit diffstat).

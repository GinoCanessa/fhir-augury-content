# Artifact Ballot Note Draft: CodeSystem (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `CodeSystem` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T16:48:26Z |

## Source Files

Files considered part of `CodeSystem` for this run (resolved per the FhirCore
authoring layout in the briefing — `source/codesystem/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/codesystem/structuredefinition-CodeSystem.xml` | StructureDefinition (canonical) | no |
| `source/codesystem/codesystem-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/codesystem/codesystem-notes.xml` | Supplementary narrative | yes |
| `source/codesystem/bundle-CodeSystem-search-params.xml` | Search parameters | no |
| `source/codesystem/list-CodeSystem-operations.xml` | Operations list | no |
| `source/codesystem/list-CodeSystem-examples.xml` | Examples list | no |
| `source/codesystem/list-CodeSystem-packs.xml` | Packs list | no |
| `source/codesystem/operationdefinition-CodeSystem-lookup.xml` | `$lookup` operation | no |
| `source/codesystem/operationdefinition-CodeSystem-subsumes.xml` | `$subsumes` operation | no |
| `source/codesystem/operationdefinition-CodeSystem-validate-code.xml` | `$validate-code` operation | yes |
| `source/codesystem/implementationguide-CodeSystem-core.xml` | IG packaging for CodeSystem | no |
| `source/codesystem/codesystem-codesystem-content-mode.xml` | Sibling CodeSystem (content-mode) | no |
| `source/codesystem/codesystem-codesystem-hierarchy-meaning.xml` | Sibling CodeSystem (hierarchy-meaning) | no |
| `source/codesystem/codesystem-concept-properties.xml` | Sibling CodeSystem (concept-properties) | yes |
| `source/codesystem/codesystem-concept-property-type.xml` | Sibling CodeSystem (concept-property-type) | no |
| `source/codesystem/codesystem-concept-subsumption-outcome.xml` | Sibling CodeSystem (subsumption-outcome) | no |
| `source/codesystem/codesystem-example*.xml` (7 files) | CodeSystem examples | no |
| `source/codesystem/codesystem-fivews-mapping-exceptions.xml` | Sibling CodeSystem (fivews exceptions) | no |
| `source/codesystem/codesystem-nhin-purposeofuse.xml` | Sibling CodeSystem (NHIN PoU example) | no |
| `source/codesystem/codesystem-request-category.xml` | Sibling CodeSystem (request-category) | no |
| `source/codesystem/codesystem-resource-status.xml` | Sibling CodeSystem (resource-status) | no |
| `source/codesystem/codesystem-restful-interaction.xml` | Sibling CodeSystem (restful-interaction) | no |
| `source/codesystem/codesystem-safety-entries.xml` | Sibling CodeSystem (safety-entries) | no |
| `source/codesystem/loinc.xml` | Static LOINC reference instance | no |
| `source/codesystem/valueset-codesystem-content-mode.xml` | Sibling ValueSet (content-mode) | no |
| `source/codesystem/valueset-codesystem-hierarchy-meaning.xml` | Sibling ValueSet (hierarchy-meaning) | no |
| `source/codesystem/valueset-concept-property-type.xml` | Sibling ValueSet (property-type) | no |
| `source/codesystem/valueset-concept-subsumption-outcome.xml` | Sibling ValueSet (subsumption-outcome) | no |
| `source/codesystem/valueset-publication-status.xml` | Sibling ValueSet (publication-status) | no |

There is no `codesystem-spreadsheet.xml` in the folder; the StructureDefinition
is authoritative for this resource (and was not touched in the window).

## Current Ballot Note

The current intro file at HEAD already carries a ballot note that was added
inside this window (the entire `bn1` block is part of the rollup diff), so the
"current" note shown below is the post-FHIR-56201 state authored by Bryn Rhodes
in commit [`95e797e1e00e`](https://github.com/HL7/fhir/commit/95e797e1e00edd18392cbc82c67b2e1cdc6d9b9d):

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
      <li><a href="https://jira.hl7.org/browse/FHIR-56201">FHIR-56201</a>: Added lastVersionPresent concept property</li>
    </ul>
  </li>
  <li>Non-substantive Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
</ul>
<p></p>
</blockquote>
<blockquote style="background-color: lightblue">
  <p><b>All Changes (including Technical Corrections not listed above):</b></p>
  <ul>
    <li><a href="https://jira.hl7.org/browse/FHIR-56201">FHIR-56201</a>: Added lastVersionPresent concept property</li>
  </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-56201](https://jira.hl7.org/browse/FHIR-56201) | Add an invalidInVersion concept property | [`95e797e1e00e`](https://github.com/HL7/fhir/commit/95e797e1e00edd18392cbc82c67b2e1cdc6d9b9d), [`e46b57c91b9a`](https://github.com/HL7/fhir/commit/e46b57c91b9a1704d47884caf6891933a55b26f8) |
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — "typos and bump kindling" (Grahame Grieve, 2026-03-18) |

## Per-Ticket Detail

### [FHIR-56201](https://jira.hl7.org/browse/FHIR-56201) — Add an invalidInVersion concept property

- **Work group:** Terminology Infrastructure
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Add lastVersionPresent concept to the concept properties code system
  >
  > lastVersionPresent string
  >
  > Description: The value of the property is the version of the code system
  > where the concept was last known to be present. This property is used in
  > value set expansions to indicate concepts that are explicitly referenced
  > in value set definitions but are no longer present in the code system
  > version being used for the expansion. See the includeLastVersionPresent
  > parameter in the Canonical Resource Management Infrastructure
  > specialization of the ValueSet/$expand operation for a description of
  > when this parameter is used.
  >
  > This property will only appear in expansions because it describes
  > concepts that are not in the code system version used in the $expand.
  >
  > Add the new concept to the table on this page:
  > https://build.fhir.org/codesystem-concept-properties.html

- **Disposition summary:** The original request asked for a new
  `invalidInVersion` concept property in the FHIR concept-properties code
  system to flag concepts that are referenced from value sets but are not
  present in the expansion's code system version. With modification, the
  workgroup elected to add the property under the name **`lastVersionPresent`**
  (string) and to align it with the CRMI `includeLastVersionPresent`
  `$expand` parameter. The disposition also requires the
  `codesystem-concept-properties.html` table to be updated.
- **Commits applying this ticket:**
  - [`e46b57c91b9a`](https://github.com/HL7/fhir/commit/e46b57c91b9a1704d47884caf6891933a55b26f8) — "[FHIR-56201](https://jira.hl7.org/browse/FHIR-56201): Added invalidInVersion concept property" (2026-04-03) — pre-applied via PR #4044, using the originally-proposed `invalidInVersion` name.
  - [`95e797e1e00e`](https://github.com/HL7/fhir/commit/95e797e1e00edd18392cbc82c67b2e1cdc6d9b9d) — "[FHIR-56201](https://jira.hl7.org/browse/FHIR-56201): Added lastVersionPresent concept property" (2026-04-06) — updated disposition applied via PR #4045; renames the property to `lastVersionPresent` and re-points the description at `includeLastVersionPresent`.
- **Changes applied (per Step 5b, scoped to this artifact):** The two
  commits together add a single new `<concept>` to
  `codesystem-concept-properties.xml` for code `lastVersionPresent` (display
  `LastVersionPresent`, `dataType` = `string`) with the disposition's
  definition text verbatim, and append the matching row to the concept-property
  reference table in `codesystem-notes.xml` (`http://hl7.org/fhir/concept-properties#lastVersionPresent`).
  They also introduce the `bn1` "Note to Balloters" block plus the
  "All Changes" blockquote in `codesystem-introduction.xml`, both citing
  FHIR-56201. The earlier `invalidInVersion` commit was effectively rewritten
  by the later `lastVersionPresent` commit; only the after-applied
  `lastVersionPresent` form is present at HEAD.

### (unattributed) — typo / housekeeping

- **Commits:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — "typos and bump kindling" (Grahame Grieve, 2026-03-18)
- **Changes applied:** Two narrative typos in
  `operationdefinition-CodeSystem-validate-code.xml` (the `abstract`
  parameter `documentation`): removed a stray period after "Note that"
  (`Note that.` → `Note that`) and corrected the spelling of "asbtract"
  to "abstract" in one of the two occurrences in that paragraph. No
  parameter, type, cardinality or binding change. The cross-reference
  index returned no Jira key for this commit, and the commit message does
  not cite a ticket.

## Roll-up Summary (after-applied state)

Scope is narrow: only four files changed across the entire CodeSystem artifact
in this window, and the substantive change is the addition of one concept
property.

- **StructureDefinition (`structuredefinition-CodeSystem.xml`):** No changes.
  No element-level additions/removals, no cardinality, type, or binding
  changes; snapshot regeneration is **not** required for this artifact.
- **Intro / narrative (`codesystem-introduction.xml`, `codesystem-notes.xml`):**
  - `codesystem-introduction.xml` gains a new `<blockquote class="ballot-note" id="bn1">` block plus a sibling light-blue "All Changes" blockquote, both citing FHIR-56201.
  - `codesystem-notes.xml` gains a new row in the concept-property reference table for `...lastVersionPresent` (string, with the full description and a clipboard-copy widget for `http://hl7.org/fhir/concept-properties#lastVersionPresent`), placed between the existing `lastVersionValid` and `replacedBy[X]` rows.
- **Search parameters (`bundle-CodeSystem-search-params.xml`):** No changes.
- **Operations (`list-CodeSystem-operations.xml` and the three
  `operationdefinition-CodeSystem-*.xml` files):** No structural change.
  `operationdefinition-CodeSystem-validate-code.xml` has narrative-only
  copyedits in the `abstract` input parameter's `documentation` (period
  and spelling fix described above); the parameter itself is unchanged.
- **Examples:** No additions or removals; no example required adjustment
  because no element changed.
- **Terminology (sibling `valueset-*` / `codesystem-*` in this folder):**
  One sibling CodeSystem instance changed —
  `codesystem-concept-properties.xml` (`http://hl7.org/fhir/concept-properties`)
  gains a single new concept `lastVersionPresent` (display
  `LastVersionPresent`, `dataType` = `string`) immediately before the
  existing `replacedByCode` concept. No other sibling CodeSystem or
  ValueSet was touched. Because `concept-properties` is the FHIR-managed
  concept-property registry, the change stays in `HL7/fhir`; no UTG move
  is implied by the briefing's cross-repo touch points.

## Proposed Ballot Note (HTML)

The existing `bn1` block already accurately reflects the after-applied state.
The only refinements proposed below are: (a) restore a narrative framing
sentence so balloters get context before the bullet list, (b) sharpen the
bullet so it names the affected code system (`http://hl7.org/fhir/concept-properties`)
and the linkage to the CRMI `$expand.includeLastVersionPresent` parameter,
which is the consumer of the new property, and (c) keep "Non-compatible" and
"Non-substantive" buckets explicit with `None`. The typo fix in
`operationdefinition-CodeSystem-validate-code.xml` is intentionally **not**
listed as a non-substantive bullet because it has no Jira attribution; it is
covered by the standard "Technical Corrections not listed" sweep in the
companion blue blockquote.

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> Key changes to the <code>CodeSystem</code> resource and its companion concept-properties registry since FHIR 6.0.0-ballot4. The CodeSystem <code>StructureDefinition</code> itself is unchanged in this window; the substantive change is in the FHIR concept-properties code system.</p>
<ul>
  <li>Non-compatible Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li>Compatible, Substantive Changes
    <ul>
      <li>Added a new <code>lastVersionPresent</code> concept (string) to the <a href="codesystem-concept-properties.html"><code>http://hl7.org/fhir/concept-properties</code></a> code system. The property records the code-system version in which a concept was last known to be present, and is intended for use in <code>ValueSet/$expand</code> expansions when consumers opt in to the CRMI <code>includeLastVersionPresent</code> parameter — i.e. it surfaces concepts that a value set explicitly references but that are no longer in the code-system version being expanded (<a href="https://jira.hl7.org/browse/FHIR-56201">FHIR-56201</a>).</li>
    </ul>
  </li>
  <li>Non-substantive Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
</ul>
<p></p>
</blockquote>
<blockquote style="background-color: lightblue">
  <p><b>All Changes (including Technical Corrections not listed above):</b></p>
  <ul>
    <li><a href="https://jira.hl7.org/browse/FHIR-56201">FHIR-56201</a>: Added <code>lastVersionPresent</code> concept property to <code>http://hl7.org/fhir/concept-properties</code></li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Ticket-name vs. applied-name mismatch is expected.** FHIR-56201 is titled
  "Add an invalidInVersion concept property" and the first commit
  ([`e46b57c91b9a`](https://github.com/HL7/fhir/commit/e46b57c91b9a1704d47884caf6891933a55b26f8))
  used that name; the resolution ("Persuasive with Modification") and the
  follow-up commit ([`95e797e1e00e`](https://github.com/HL7/fhir/commit/95e797e1e00edd18392cbc82c67b2e1cdc6d9b9d))
  renamed it to `lastVersionPresent`. Only the latter exists at HEAD; the
  proposed ballot note reflects the after-applied name.
- **The "current ballot note" was authored inside this window.** Before
  `5d67a34a13a5` there was no ballot note in `codesystem-introduction.xml`;
  the entire `bn1` block plus the blue "All Changes" blockquote were added
  by the FHIR-56201 commits. The proposed note therefore largely carries
  forward the bullet that is already there, with sharpened wording.
- **One unattributed commit** ([`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30))
  applies a pure-typo fix to the `$validate-code` operation's `abstract`
  parameter narrative ("Note that." → "Note that"; "asbtract" → "abstract").
  The cross-reference index returns no Jira key for this SHA, so it is not
  listed as a ballot bullet; it is covered by the catch-all "Technical
  Corrections not listed" sweep.
- **No CodeSystem `StructureDefinition` change** — balloters comparing this
  ballot to `ballot4` will see element-level diffs of zero on the resource
  itself; the diff is concentrated in the concept-properties registry that
  ships in the same folder.
- **Cross-repo touch points:** None triggered. `concept-properties` is the
  FHIR-managed registry and remains in `HL7/fhir`; no UTG canonical was
  edited as part of FHIR-56201.

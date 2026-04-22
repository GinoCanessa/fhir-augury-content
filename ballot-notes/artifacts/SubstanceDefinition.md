# Artifact Ballot Note Draft: SubstanceDefinition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `SubstanceDefinition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 4 (2 with substantive changes to this artifact, 2 referenced by a multi-resource intro commit only) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `SubstanceDefinition` for this run (from the briefing's
Artifact Map / FhirCore conventions):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/substancedefinition/structuredefinition-SubstanceDefinition.xml` | Canonical StructureDefinition | yes |
| `source/substancedefinition/substancedefinition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/substancedefinition/substancedefinition-notes.xml` | Supplementary narrative | no |
| `source/substancedefinition/bundle-SubstanceDefinition-search-params.xml` | Search parameters | no |
| `source/substancedefinition/list-SubstanceDefinition-operations.xml` | Operations | no |
| `source/substancedefinition/list-SubstanceDefinition-examples.xml` | Examples list | no |
| `source/substancedefinition/list-SubstanceDefinition-packs.xml` | Packs list | no |
| `source/substancedefinition/substancedefinition-example.xml` | Example instance | no |
| `source/substancedefinition/substancedefinition-examples-header.xml` | Examples header | no |
| `source/substancedefinition/codesystem-substance-name-authority.xml` | Artifact-scoped CodeSystem | yes |
| `source/substancedefinition/codesystem-substance-*.xml` (18 others) | Artifact-scoped CodeSystems | no |
| `source/substancedefinition/valueset-substance-*.xml` (19 files) | Artifact-scoped ValueSets | no |

Patterns from the conventions that produced no match in the clone:

- `source/substancedefinition/substancedefinition-spreadsheet.xml` — no file matched (legacy spreadsheet absent; SD is authoritative).
- Sibling `structuredefinition-*.xml` other than the canonical — no extras present.

## Current Ballot Note

A single ballot note exists at HEAD in `substancedefinition-introduction.xml`:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since the last R6 ballot are:</p>
<ul>
    <li>Updates to the following elements:</li>
        <ul>
            <li>SubstanceDefinition.moiety.identifier, which was made 0..* (previously 0..1)</li>
            <li>SubstanceDefinition.name.official.authority, value set (and code system) substance-name-authority has been extended with code: "UT", UMC Terminologies</li>
        </ul>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55057](https://jira.hl7.org/browse/FHIR-55057) | SubstanceDefinition.moiety.identifier should repeat | [`0bd34d09fb78`](https://github.com/HL7/fhir/commit/0bd34d09fb78b5f58fadcb85ee4746e773068a29), [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) |
| [FHIR-56036](https://jira.hl7.org/browse/FHIR-56036) | Add UMC as a substances naming authority | [`ff1d2e240f82`](https://github.com/HL7/fhir/commit/ff1d2e240f82f7a41003a9a34ca2a61e4bbe6965), [`d5a414dd234a`](https://github.com/HL7/fhir/commit/d5a414dd234a1a02f5c60a92b509a950d852141a) |
| [FHIR-55053](https://jira.hl7.org/browse/FHIR-55053) | RegulatedAuthorization.case.identifier should repeat | [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) (referenced in commit subject only; no SubstanceDefinition file change) |
| [FHIR-55046](https://jira.hl7.org/browse/FHIR-55046) | Ingredient.identifier should repeat | [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) (referenced in commit subject only; no SubstanceDefinition file change) |

No unattributed commits in the window — every commit cites at least one ticket key.

## Per-Ticket Detail

### [FHIR-55057](https://jira.hl7.org/browse/FHIR-55057) — SubstanceDefinition.moiety.identifier should repeat

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive (Resolved - change required)
- **Disposition (verbatim):**

  > Make the identifier element maximal cardinality *

  Disposition text taken from the Jira "Resolution Description" — no separate
  applied-vote comment was recorded on the issue.
- **Disposition summary:** The submitter (Lloyd McKenzie, comment 23) noted
  that identifiers may be assigned by multiple entities over time, but
  `SubstanceDefinition.moiety.identifier` was modeled as 0..1. The work group
  agreed and resolved to raise the upper cardinality to `*`.
- **Commits applying this ticket:**
  - [`0bd34d09fb78`](https://github.com/HL7/fhir/commit/0bd34d09fb78b5f58fadcb85ee4746e773068a29) — `FHIR-55057 SubstanceDefinition.moiety.identifier to 0..* from 0..1` (2026-04-16, Rik Smithies)
  - [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) — `resource introduction updates for FHIR-55057 ... FHIR-55053 ... FHIR-55046` (2026-04-16, Rik Smithies; multi-resource intro update)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-SubstanceDefinition.xml`, the `moiety.identifier`
  element's `<max>` was changed from `1` to `*` in the differential. The
  follow-up intro commit added the corresponding bullet to the ballot note
  in `substancedefinition-introduction.xml`. No other SubstanceDefinition
  elements were touched. `<snapshot>` regeneration is required.

### [FHIR-56036](https://jira.hl7.org/browse/FHIR-56036) — Add UMC as a substances naming authority

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive (Resolved - change required)
- **Disposition (verbatim):**

  > Add code 'UT' and display 'UMC Terminologies' to the CodeSystem.

  Disposition text taken from the Jira "Resolution Description"; no separate
  applied-vote comment was recorded on the issue.
- **Disposition summary:** UMC (Uppsala Monitoring Centre) operate the UMC
  SRS substance-naming system and requested inclusion in the
  `substance-name-authority` CodeSystem so that
  `SubstanceDefinition.name.official.authority` can identify them as the
  source. The work group agreed and resolved to add the new code.
- **Commits applying this ticket:**
  - [`ff1d2e240f82`](https://github.com/HL7/fhir/commit/ff1d2e240f82f7a41003a9a34ca2a61e4bbe6965) — `FHIR-56036 added UT name authority for UMC Terminologies` (2026-04-01, Rik Smithies)
  - [`d5a414dd234a`](https://github.com/HL7/fhir/commit/d5a414dd234a1a02f5c60a92b509a950d852141a) — `FHIR-56036 added UT name authority for UMC Terminologies - added note` (2026-04-03, Rik Smithies)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `codesystem-substance-name-authority.xml`, a new `<concept>` was appended
  with `code="UT"` and `display="UMC Terminologies"`. The corresponding
  bullet calling out the new code was added to the ballot note in
  `substancedefinition-introduction.xml`. The companion ValueSet
  (`valueset-substance-name-authority.xml`) is unchanged and picks up the
  new code automatically because it expands the full CodeSystem.

### [FHIR-55053](https://jira.hl7.org/browse/FHIR-55053) — RegulatedAuthorization.case.identifier should repeat

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive (Resolved - change required)
- **Disposition (verbatim):**

  > change maximal cardinality of identifier to *
- **Disposition summary:** Companion to FHIR-55057/FHIR-55046 — raises
  `RegulatedAuthorization.case.identifier` from 0..1 to 0..*. **Out of scope
  for SubstanceDefinition**: this ticket only appears here because the
  multi-resource intro-update commit `f0c7b541` happened to touch the
  `substancedefinition-introduction.xml` file in the same commit it used to
  update other resources' intros. No SubstanceDefinition element or
  terminology was changed by this ticket; see the `regulatedauthorization`
  artifact for its real impact.
- **Commits applying this ticket:**
  - [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) — multi-resource intro update; the SubstanceDefinition hunk is the FHIR-55057 bullet, not anything for this ticket.
- **Changes applied (per Step 5b, scoped to this artifact):** None. No
  bytes attributable to this ticket changed under `source/substancedefinition/`.

### [FHIR-55046](https://jira.hl7.org/browse/FHIR-55046) — Ingredient.identifier should repeat

- **Work group:** Biomedical Research & Regulation
- **Resolution:** Persuasive (Resolved - change required)
- **Disposition (verbatim):**

  > make the identifier element ..*
- **Disposition summary:** Companion to FHIR-55057/FHIR-55053 — raises
  `Ingredient.identifier` from 0..1 to 0..*. **Out of scope for
  SubstanceDefinition**: same situation as FHIR-55053; the ticket key
  appears in the multi-resource intro-update commit but no
  SubstanceDefinition file change is attributable to it. See the `ingredient`
  artifact for its real impact.
- **Commits applying this ticket:**
  - [`f0c7b541c736`](https://github.com/HL7/fhir/commit/f0c7b541c736196950e89f45753f19dfa7742832) — multi-resource intro update; not attributable to a SubstanceDefinition change.
- **Changes applied (per Step 5b, scoped to this artifact):** None.

## Roll-up Summary (after-applied state)

The window touches three files (15 insertions, 1 deletion across the
artifact). All changes are concentrated in two substantive areas.

- **StructureDefinition (`structuredefinition-SubstanceDefinition.xml`):**
  - `SubstanceDefinition.moiety.identifier` upper cardinality raised from
    `1` to `*` (differential edit at element id
    `SubstanceDefinition.moiety.identifier`). Snapshot regeneration is
    required; no other elements (type, binding, constraints, definitions)
    were touched.
- **Intro / narrative (`substancedefinition-introduction.xml`):**
  - The existing balloter note (`bn1`) was extended with two new bullets
    documenting the moiety.identifier cardinality change and the new
    `UT` authority code. No other narrative was edited; the `Scope and
    Usage` body is unchanged.
- **Search parameters (`bundle-SubstanceDefinition-search-params.xml`):** No changes.
- **Operations (`list-SubstanceDefinition-operations.xml`):** No changes.
- **Examples (`substancedefinition-example.xml`,
  `list-SubstanceDefinition-examples.xml`):** No changes; the cardinality
  relaxation does not invalidate the existing example.
- **Terminology (sibling `valueset-*` / `codesystem-*`):**
  - `codesystem-substance-name-authority.xml`: added concept `UT` /
    "UMC Terminologies" appended at the end of the `<concept>` list.
  - `valueset-substance-name-authority.xml`: no edit needed — it
    expands the full CodeSystem, so the new code surfaces automatically.
  - All other 18 `codesystem-substance-*.xml` and 19
    `valueset-substance-*.xml` files in the artifact folder are unchanged.
  - The `substance-name-authority` CodeSystem lives under
    `source/substancedefinition/`, not in UTG, consistent with the
    artifact-scoped terminology pattern noted in the briefing.

## Proposed Ballot Note (HTML)

The existing `bn1` already enumerates exactly the two substantive changes
in the after-applied state, so the proposed note retains its substance
and structure. The revisions below: (a) add inline Jira citations against
each bullet, (b) flatten the malformed nested `<ul>` (a `<ul>` directly
inside another `<ul>` without an intervening `<li>` is invalid HTML), and
(c) use a single, clearer lead-in sentence.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since the last R6 ballot are:</p>
  <ul>
    <li><code>SubstanceDefinition.moiety.identifier</code> upper cardinality has been changed from <code>0..1</code> to <code>0..*</code>, since identifiers for a moiety substance may be assigned by multiple authorities over time (<a href="https://jira.hl7.org/browse/FHIR-55057">FHIR-55057</a>).</li>
    <li>The <code>substance-name-authority</code> CodeSystem (used by <code>SubstanceDefinition.name.official.authority</code>) has been extended with the new code <code>UT</code> &mdash; "UMC Terminologies", at the request of the Uppsala Monitoring Centre (<a href="https://jira.hl7.org/browse/FHIR-56036">FHIR-56036</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The existing ballot-note bullets are both retained: each one still
  describes a change that is present in the after-applied state. No
  bullets were dropped or carried-over-then-reverted.
- Two of the four tickets attributed in the window (FHIR-55053
  RegulatedAuthorization, FHIR-55046 Ingredient) appear only because
  the multi-resource intro-update commit `f0c7b541` touched the
  SubstanceDefinition intro file as part of the same commit it used to
  update other resources' intros. They are listed for completeness in
  the per-ticket section but contribute zero bytes to the
  SubstanceDefinition diff and are intentionally not cited in the
  proposed ballot note. The sibling `regulatedauthorization` and
  `ingredient` artifact reports should pick those tickets up.
- All four tickets were resolved Persuasive; none of the Jira issues
  has applied-vote comments recorded, so the disposition text quoted in
  the per-ticket section is taken from each ticket's "Resolution
  Description" field (the only authoritative disposition text available
  in Jira for these issues).
- HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit
  (`5d67a34a13a5`); the simple `since..HEAD` window was used (no
  symmetric-difference fallback needed).
- `fhir-augury-cli cross-referenced` returned zero hits for each commit
  SHA in the window; ticket attribution relies entirely on the
  `(FHIR|UTG)-\d+` regex match against commit subject/body, which is
  unambiguous here because every commit subject explicitly cites its
  ticket(s).
- The briefing's HEAD (`1b369ff4e28e`, analyzed 2026-04-20) is one
  commit behind the current clone HEAD (`db79dcdfe196`); the artifact
  layout has not changed in that gap, so the briefing's Artifact Map
  is still authoritative for this report.

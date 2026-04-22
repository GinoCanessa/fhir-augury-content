# Artifact Ballot Note Draft: Composition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Composition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 5 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `Composition` for this run (folder: `source/composition/`, FhirCore Artifact Map conventions):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/composition/structuredefinition-Composition.xml` | Canonical StructureDefinition | yes |
| `source/composition/composition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/composition/composition-notes.xml` | Supplementary narrative | no |
| `source/composition/bundle-Composition-search-params.xml` | Search parameters | no |
| `source/composition/list-Composition-operations.xml` | Operations | no |
| `source/composition/list-Composition-examples.xml` | Examples list | no |
| `source/composition/list-Composition-packs.xml` | Packs list | no |
| `source/composition/operationdefinition-Composition-document.xml` | `$document` operation definition | no |
| `source/composition/composition-example.xml`, `composition-example-mixed.xml`, `document-example-dischargesummary.xml`, `connectathon-example-scenario21.xml` | Examples | no |
| `source/composition/composition-examples-header.xml` | Examples header | no |
| `source/composition/composition-event-mapping-exceptions.xml`, `composition-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/composition/structuredefinition-profile-catalog.xml` | Sibling profile (Catalog) | no |
| `source/composition/composition-catalog-profile-introduction.xml`, `composition-clinicaldocument-introduction.xml`, `composition-measurereport-profile-introduction.xml` | Sibling profile narratives | no |
| `source/composition/implementationguide-Composition-core.xml` | IG container | no |
| `source/composition/codesystem-composition-status.xml`, `codesystem-composition-attestation-mode.xml`, `codesystem-artifact-relationship-type.xml`, `codesystem-catalog-type.xml` | Artifact-scoped CodeSystems (4) | no |
| `source/composition/valueset-composition-status.xml`, `valueset-composition-attestation-mode.xml`, `valueset-artifact-relationship-type.xml`, `valueset-catalog-type.xml`, `valueset-doc-categorycodes.xml`, `valueset-doc-confidentiality.xml`, `valueset-doc-event-code.xml`, `valueset-doc-event-code-rsna.xml`, `valueset-doc-section-codes.xml`, `valueset-doc-typecodes.xml` | Artifact-scoped ValueSets (10) | no |
| `source/composition/conceptmap-cm-composition-status-v3.xml` | ConceptMap | no |
| `source/composition/$document-request.txt`, `$document-response.txt` | $document fixtures | no |
| `source/composition/invariant-tests/` | Invariant test fixtures | no |
| `source/composition/composition.svg` | Diagram asset | no |

No briefing-listed pattern produced an empty match for this artifact.

## Current Ballot Note

A ballot note `bn1` exists at HEAD (it was introduced inside this window — there was no ballot note at the since-commit). Verbatim:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> The key changes made since FHIR 6.0.0-ballot4 include:</p>
<p>Changed the Composition.participant.type short description to &quot;Meaning and purpose of participation, in creation of the clinical document&quot; as a correction.</p>
</blockquote>
```

A sibling release-notes blockquote (not a `ballot-note`) lists the contributing tickets:

```html
<blockquote style="background-color: lightblue">
<p><b>Release Notes:</b></p>
<ul>
<li><a href="https://jira.hl7.org/browse/FHIR-53695">FHIR-53695</a></li>
<li><a href="https://jira.hl7.org/browse/FHIR-54103">FHIR-54103</a></li>
<li><a href="https://jira.hl7.org/browse/FHIR-54182">FHIR-54182</a></li>
<li><a href="https://jira.hl7.org/browse/FHIR-54343">FHIR-54343</a></li>
<li><a href="https://jira.hl7.org/browse/FHIR-54986">FHIR-54986</a></li>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53695](https://jira.hl7.org/browse/FHIR-53695) | Replace short description for Composition.participant.type | [`0665e5c4b4b2`](https://github.com/HL7/fhir/commit/0665e5c4b4b232b56e09fe4240b76d9f7ef9ffca) |
| [FHIR-54103](https://jira.hl7.org/browse/FHIR-54103) | Composition.participant.type short description should be corrected | [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) |
| [FHIR-54182](https://jira.hl7.org/browse/FHIR-54182) | Composition.participant.type 0..* codeableConcept :: value set confusion | [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) |
| [FHIR-54343](https://jira.hl7.org/browse/FHIR-54343) | Composition.participant.type lists codes which are excluded in corresponding value set | [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) |
| [FHIR-54986](https://jira.hl7.org/browse/FHIR-54986) | Composition value type comment | [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) |

No unattributed commits.

## Per-Ticket Detail

All five tickets were collapsed onto a single underlying change. Per Jira coordination comments (e.g., FHIR-54103 → "Coordinate this FHIR-54986, FHIR-54343, FHIR-54182, FHIR-54103, and FHIR-53695 which are all addressing the same issue.") the workgroup treated FHIR-53695 as the change-bearing ticket and the other four as duplicates resolved by the same fix. The per-ticket diffs below therefore overlap heavily; the authoritative summary is in the **Roll-up Summary** section.

### [FHIR-53695](https://jira.hl7.org/browse/FHIR-53695) — Replace short description for Composition.participant.type

- **Work group:** Structured Documents
- **Specification:** FHIR Core (FHIR)
- **Type / Resolution:** Technical Correction / Persuasive (status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (no `resolution_description`; the only related comment is the implementing PR pointer: "Pull request 4049").

- **Disposition summary:** Replace the misleading short description on `Composition.participant.type` (which listed `AUT | AUTHEN | CST | LA | RCT | SBJ` — codes that are explicitly *excluded* from the bound value set) with text that describes the meaning of the element rather than enumerating disallowed codes.
- **Commits applying this ticket:**
  - [`0665e5c4b4b2`](https://github.com/HL7/fhir/commit/0665e5c4b4b232b56e09fe4240b76d9f7ef9ffca) — `J#53695 Updated the short description for Composition.participant.type` (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-Composition.xml`, the `<short>` of element `Composition.participant.type` was changed from `"AUT | AUTHEN | CST | LA | RCT | SBJ"` to `"Meaning and purpose of participation, in creation of the clinical document"`. The element's `<definition>`, cardinality, type, and binding were not changed. The same commit also added the `bn1` ballot note describing this change to `composition-introduction.xml`.

### [FHIR-54103](https://jira.hl7.org/browse/FHIR-54103) — Composition.participant.type short description should be corrected

- **Work group:** Structured Documents
- **Specification:** FHIR Core (FHIR)
- **Type / Resolution:** Technical Correction / Persuasive (status: Resolved - change required)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only substantive comment is the coordination note: *"Coordinate this FHIR-54986, FHIR-54343, FHIR-54182, FHIR-54103, and FHIR-53695 which are all addressing the same issue."*

- **Disposition summary:** Duplicate of FHIR-53695 — the short display for `Composition.participant.type` should not advertise the six v3-ParticipationType codes (AUT, AUTHEN, CST, LA, RCT, SBJ) that the bound value set explicitly excludes.
- **Commits applying this ticket:**
  - [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) — `Added additional trackers that were saying the same thing J#54103 J#54182 J#54343 J#54986` (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** This commit only added the `<li>FHIR-54103</li>` entry to the Release Notes blockquote in `composition-introduction.xml`; it did not touch the StructureDefinition. The substantive correction is delivered by the FHIR-53695 commit; see the roll-up.

### [FHIR-54182](https://jira.hl7.org/browse/FHIR-54182) — Composition.participant.type 0..* codeableConcept :: value set confusion

- **Work group:** Structured Documents
- **Specification:** FHIR Core (FHIR)
- **Type / Resolution:** Technical Correction / Persuasive (status: Resolved - change required)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only substantive comment is the coordination note: *"Coordinate this FHIR-54986, FHIR-54343, FHIR-54182, FHIR-54103, and FHIR-53695 which are all addressing the same issue."*

- **Disposition summary:** Duplicate of FHIR-53695 — flagged the contradiction between the resource page (which listed AUT|AUTHEN|CST|LA|RCT|SBJ) and the bound value set (which excludes those exact codes).
- **Commits applying this ticket:**
  - [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) — `Added additional trackers that were saying the same thing J#54103 J#54182 J#54343 J#54986` (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** Added as a Release Notes link only (one `<li>` entry in `composition-introduction.xml`). Substantive change is via FHIR-53695.

### [FHIR-54343](https://jira.hl7.org/browse/FHIR-54343) — Composition.participant.type lists codes which are excluded in corresponding value set

- **Work group:** Structured Documents
- **Specification:** FHIR Core (FHIR)
- **Type / Resolution:** Change Request / Persuasive with Modification (status: Resolved - change required)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only substantive comment is the coordination note: *"Coordinate this FHIR-54986, FHIR-54343, FHIR-54182, FHIR-54103, and FHIR-53695 which are all addressing the same issue."*

- **Disposition summary:** Same defect as FHIR-53695 / FHIR-54103 / FHIR-54182, raised from a different angle. Resolved "Persuasive with Modification" because the workgroup chose to fix the short display rather than alter the value set, but the on-disk change is identical to FHIR-53695.
- **Commits applying this ticket:**
  - [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) — `Added additional trackers that were saying the same thing J#54103 J#54182 J#54343 J#54986` (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** Added as a Release Notes link only (one `<li>` entry). Substantive change via FHIR-53695.

### [FHIR-54986](https://jira.hl7.org/browse/FHIR-54986) — Composition value type comment

- **Work group:** Structured Documents
- **Specification:** FHIR Core (FHIR)
- **Type / Resolution:** Technical Correction / Persuasive (status: Resolved - change required)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. Comments captured: "This is a technical correction" (gdolin, 2026-04-02) and the coordination note "Coordinate this FHIR-54986 with FHIR-54343, FHIR-54182, FHIR-54103, and FHIR-53695 which are all addressing the same issue."

- **Disposition summary:** Originally argued for either pruning the participant.type value set (to remove codes already represented by sibling elements like `.author`, `.attester`, `.subject`, `.custodian`) or removing the redundant top-level elements. The workgroup declined the structural change and instead absorbed it into the same short-description correction as FHIR-53695.
- **Commits applying this ticket:**
  - [`1081ab4398e5`](https://github.com/HL7/fhir/commit/1081ab4398e5bfc673dd98941f18ff1b53115854) — `Added additional trackers that were saying the same thing J#54103 J#54182 J#54343 J#54986` (2026-04-10)
- **Changes applied (per Step 5b, scoped to this artifact):** Added as a Release Notes link only (one `<li>` entry). The structural changes the ticket originally asked for (pruning the value set or removing duplicate elements) were **not** made; only the short-description correction was applied, via FHIR-53695.

## Roll-up Summary (after-applied state)

The window contains only two on-disk changes for this artifact, both landed on 2026-04-10. Diff stat:

```
 source/composition/composition-introduction.xml        | 14 ++++++++++++++
 source/composition/structuredefinition-Composition.xml |  2 +-
 2 files changed, 15 insertions(+), 1 deletion(-)
```

- **StructureDefinition (`structuredefinition-Composition.xml`):**
  - `Composition.participant.type` `<short>` changed from `"AUT | AUTHEN | CST | LA | RCT | SBJ"` to `"Meaning and purpose of participation, in creation of the clinical document"`. The new short matches the existing `<definition>` and removes the misleading enumeration of codes that the bound `fhir-clinical-doc-participant` value set actually excludes.
  - No other element was modified — cardinality, type (`CodeableConcept`), binding (`preferred` to `fhir-clinical-doc-participant`), and `<definition>` are unchanged.
  - No `<snapshot>` edits in the diff; snapshot regeneration on next publication run will pick up the new short automatically.
- **Intro / narrative (`composition-introduction.xml`):**
  - Added a new `<blockquote class="ballot-note" id="bn1">` describing the `Composition.participant.type` short-description correction (no prior ballot note existed at the since-commit).
  - Added a sibling `<blockquote style="background-color: lightblue">` "Release Notes" listing the five contributing Jira tickets (FHIR-53695, FHIR-54103, FHIR-54182, FHIR-54343, FHIR-54986).
  - No changes to Scope, Background, Boundaries, or any other narrative section.
- **Notes (`composition-notes.xml`):** No changes.
- **Search parameters (`bundle-Composition-search-params.xml`):** No changes.
- **Operations (`list-Composition-operations.xml`, `operationdefinition-Composition-document.xml`):** No changes; `$document` operation untouched.
- **Examples (`list-Composition-examples.xml`, `composition-example*.xml`, `document-example-dischargesummary.xml`, `connectathon-example-scenario21.xml`):** No additions, removals, or updates required by the short-description change.
- **Sibling profiles / IG (`structuredefinition-profile-catalog.xml`, `composition-*-profile-introduction.xml`, `implementationguide-Composition-core.xml`):** No changes.
- **Terminology (`valueset-*`, `codesystem-*`, `conceptmap-*` siblings):** No changes. In particular `fhir-clinical-doc-participant` (which lives in `HL7/UTG`, not in this folder) was *not* edited; the structural request from FHIR-54986 to prune it was declined.

## Proposed Ballot Note (HTML)

The existing `bn1` is accurate but understates the scope of the underlying balloter feedback (four duplicate trackers were collapsed) and does not link the responsible Jira tickets inline. Proposed revision keeps the existing `id`:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The only normative-content change applied to Composition since FHIR 6.0.0-ballot4 is a technical correction to the short display of <code>Composition.participant.type</code>. Multiple ballot comments observed that the previous short display (<code>AUT | AUTHEN | CST | LA | RCT | SBJ</code>) advertised v3-ParticipationType codes that are explicitly <i>excluded</i> from the element's bound value set (<code>fhir-clinical-doc-participant</code>); the codes themselves remain excluded.</p>
  <ul>
    <li>Replaced the <code>Composition.participant.type</code> short display with <i>"Meaning and purpose of participation, in creation of the clinical document"</i>, aligning the short with the existing definition and removing the misleading code enumeration (<a href="https://jira.hl7.org/browse/FHIR-53695">FHIR-53695</a>, <a href="https://jira.hl7.org/browse/FHIR-54103">FHIR-54103</a>, <a href="https://jira.hl7.org/browse/FHIR-54182">FHIR-54182</a>, <a href="https://jira.hl7.org/browse/FHIR-54343">FHIR-54343</a>).</li>
    <li>Did <b>not</b> change the cardinality, type, or binding of <code>Composition.participant.type</code>, and did <b>not</b> prune the bound value set or remove the sibling top-level participant elements (<code>.author</code>, <code>.attester</code>, <code>.subject</code>, <code>.custodian</code>) requested by <a href="https://jira.hl7.org/browse/FHIR-54986">FHIR-54986</a>; that ticket was resolved as a technical correction handled by the same short-display fix.</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Briefing/Artifact Map:** The repo's briefing does not enumerate Composition explicitly; this run used the FhirCore folder convention (`source/composition/`) plus the generic file-name patterns (`structuredefinition-<Name>.xml`, `<name>-introduction.xml`, `bundle-<Name>-search-params.xml`, `list-<Name>-{operations,examples,packs}.xml`, `operationdefinition-<Name>-*.xml`, sibling `valueset-*` / `codesystem-*` / `conceptmap-*`). Every file actually present in the folder is listed in the Source Files table.
- **Cross-ref index returned no commits.** `cross-referenced` for both window commits returned `total: 0`. Ticket attribution was therefore taken entirely from the `J#NNNNN` tokens in the commit subjects, which the repo uses as its canonical commit→ticket marker. This is consistent with the workgroup's coordination comment that the five tickets are duplicates.
- **Disposition text was not recorded in Jira** for any of the five tickets (`resolution_description` is empty on all of them). Where comments contained substantive text, it has been quoted verbatim in the Per-Ticket Detail section; otherwise this is called out explicitly.
- **Original Release Notes blockquote:** A sibling release-notes block was added alongside the ballot note. It is not a `ballot-note` and is left untouched by this proposal — the proposed `bn1` revision references the same tickets inline so the release-notes block remains a redundant but harmless link list.
- **FHIR-54986 scope deviation:** The original tracker asked for either trimming the participant.type value set or removing the sibling top-level participant elements. Neither was done. The proposed ballot note explicitly calls this out so balloters are not surprised.
- **HEAD vs. since-commit:** `git merge-base --is-ancestor` confirmed HEAD (`db79dcdfe196`) is a descendant of the since-commit (`5d67a34a13a5`); a straight `since..HEAD` window was used (no symmetric-difference fallback needed).
- **No `gh` calls were required.** All evidence was sourced from `fhir-augury-cli` (Jira tickets) and the cached clone (`git`).

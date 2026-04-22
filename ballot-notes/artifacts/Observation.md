# Artifact Ballot Note Draft: Observation (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Observation` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 5 |
| Tickets attributed | 8 (of 17 ticket keys cited across the 5 commits — see "Notes for Reviewer") |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T20:10:00Z |

## Source Files

Files considered part of `Observation` for this run (from the FhirCore briefing's authoring-root patterns; the briefing has no explicit Artifact Map row for `Observation`, so the standard FhirCore file patterns were applied against `source/observation/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/observation/structuredefinition-Observation.xml` | StructureDefinition (canonical) | yes |
| `source/observation/observation-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/observation/observation-notes.xml` | Supplementary narrative | yes |
| `source/observation/bundle-Observation-search-params.xml` | Search parameters | no |
| `source/observation/list-Observation-operations.xml` | Operations list | no |
| `source/observation/list-Observation-examples.xml` | Examples list | no |
| `source/observation/list-Observation-packs.xml` | Packs list | no |
| `source/observation/observation-example*.xml` (≈70 files) | Examples | no |
| `source/observation/observation-vitalsigns-profile-introduction.xml` | Vital Signs profile intro | yes |
| `source/observation/observation-vitalsigns-profile-notes.xml` | Vital Signs profile notes | no |
| `source/observation/observation-device-metric-profile-notes.xml` | Device-metric profile notes | no |
| `source/observation/observation-fivews-mapping-exceptions.xml` | 5-Ws mapping exceptions | no |
| `source/observation/observation-event-mapping-exceptions.xml` | Event-mapping exceptions | no |
| `source/observation/structuredefinition-profile-*.xml` (vital-signs profiles, 11 files) | Sibling profile SDs | no |
| `source/observation/implementationguide-Observation-vitalsigns.xml` | Vital Signs IG package | no |
| `source/observation/operationdefinition-Observation-lastn.xml`, `operationdefinition-Observation-stats.xml` | Operation definitions | no |
| `source/observation/valueset-*.xml` (≈30 files) | Artifact-scoped ValueSets | no |
| `source/observation/codesystem-*.xml` (5 files) | Artifact-scoped CodeSystems | no |
| `source/observation/$lastn-*.txt`, `$stats-*.txt` | Operation request/response samples | no |
| `source/observation/krcore-observation-labresult-example-01.xml` | KR Core example | no |

Patterns from the standard FhirCore layout that produced no match:

- `source/observation/observation-spreadsheet.xml` — no legacy spreadsheet for Observation in the clone.

## Current Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure that the Observation resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
<ul>
<li>Multiple updates to the <a href="observation-vitalsigns.html">Vital Signs</a> profiles (including the <a href="vitalsigns.html">Vital Signs Base</a> profile and the set of specific Vital Signs profiles).  The primary changes include:</li>
  <ul>
  <li>Removed references to the LOINC "magic value" code, and instead refer to it as the "interoperability category".</li>
  <li>Created value sets of the specific LOINC codes that should apply for each vital sign profile, and create a 'preferred' binding from Observation.code to the value set for that profile.  </li>
  <li>Renamed the main vital signs page to "Observation Vital Signs Profiles", and adjust other names and text accordingly.</li>
  <li>Renamed the title of the "base" vital signs profile (which the other specific vital sign profiles are based on) to "Vital Signs Base Profile", to help make this clear.</li>
  <li>Move the reference and link to the "Vital Signs Base Profile" to a more prominently visible location on the Observation Vital Signs Profiles page (as the "header" for the requirements list).</li>
  <li>Made additional text changes needed for overall clarity and consistency.</li>
  <li>Updated the vital signs examples where needed to be consistent with the updated profiles.</li>
  </ul>
<li>The Observation.bodySite element has been deprecated, corresponding with the change to make Observation.bodyStructure a CodeableReference.</li>
<li>The 'instantiates[x]' element (with the 'instantiatesCanonical' and 'instantiatesReference' choices) has been removed and is replaced with the workflow instantiation extensions: https://build.fhir.org/workflow-extensions.html.</li>
<li>These elements previously marked as 'Trial Use' (TU) are now Normative candidates:</li>
  <ul>
  <li>Observation.triggeredBy</li>
  <li>Observation.focus</li>
  <li>Observation.bodyStructure</li>
  <li>Observation.referenceRange.normalValue</li>
  <li>Observation.referenceRange.type</li>
  <li>Observation.organizer</li>
    <ul>
    <li>
    The 'organizer' element was newly added to the Observation resource in the previous R6 3rd Draft ballot cycle (2025-04-03), so there has been less time available for it to be reviewed, but it is now also a Normative candidate. The 'organizer' element is intended to help clarify and make explicit when an instance of the Observation resource is used for organizing/grouping sets of sub-observations (e.g., for laboratory panel/battery result reporting).  This capability is particularly applicable for use in laboratory result reporting, but it can also be used as appropriate with other types of observations.
    </li>
    </ul>
  </ul>
</ul>
</blockquote>
```

In addition, two transient `stu-note` working blockquotes ("Release Notes (pending alternative process review with FMG)") have been added by the work group during this window, citing FHIR-53457, FHIR-54518, and FHIR-54036. They are work-group bookkeeping for the alternative-process review and are not part of the balloter-facing note; they are not carried into the proposed ballot note below.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54036](https://jira.hl7.org/browse/FHIR-54036) | Not the best location for the last bullet in Subject of an Observation section | [`ce31169ea948`](https://github.com/HL7/fhir/commit/ce31169ea948aa17ad222e8ba1d1db117a453fc3) |
| [FHIR-53457](https://jira.hl7.org/browse/FHIR-53457) | Remove .bodySite from Terminology Bindings in Observation | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) |
| [FHIR-54518](https://jira.hl7.org/browse/FHIR-54518) | Example description in 10.1.18.3 should be more accurate | [`d920bcd5d72e`](https://github.com/HL7/fhir/commit/d920bcd5d72e8834a7d5e7f00c30b73bfc7b4ca7) |
| [FHIR-54034](https://jira.hl7.org/browse/FHIR-54034) | Fix sentence in Subject of an Observation | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-54037](https://jira.hl7.org/browse/FHIR-54037) | Remove extranoues word from section title "Observation.hasMember of and Observation.derivedFrom" | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-54041](https://jira.hl7.org/browse/FHIR-54041) | Update section heading to correct Observation element for Using codes in Observation | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-55270](https://jira.hl7.org/browse/FHIR-55270) | Spelling/abbreviation issues on page: observation | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-55271](https://jira.hl7.org/browse/FHIR-55271) | Observation.triggeredBy.type has no escape valve | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661), [`793572dc6408`](https://github.com/HL7/fhir/commit/793572dc6408d8387156e724dd02f80a2a46768e) (revert) |

All five window commits are accounted for; no commit is unattributed.

## Per-Ticket Detail

### [FHIR-54036](https://jira.hl7.org/browse/FHIR-54036) — Not the best location for the last bullet in Subject of an Observation section

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > We will make a new section "Performer of an Observation" after "Subject of an Observation":
  >
  > In some cases, the source of the observation is not the entity recording it. This may be, for example, a radiologist-dictated observation entered by a transcriptionist, or a reading off a thermometer entered into the chart by a nurse. If it is important to record that the person or device that made the observation is not the person or device that entered it into the record, then the observation-recording extension may be used.

- **Disposition summary:** The "performer-vs-recorder" bullet was misplaced under *Subject of an Observation*. The disposition is to lift it into a brand-new H3 section, *Performer of an Observation*, sitting between *Subject of an Observation* and *Grouping of Observations*, with the same prose preserved verbatim.
- **Commits applying this ticket:**
  - [`ce31169ea948`](https://github.com/HL7/fhir/commit/ce31169ea948aa17ad222e8ba1d1db117a453fc3) — changes for FHIR-54036 (2026-03-31)
- **Changes applied:** In `observation-notes.xml`, the radiologist/transcriptionist `<li>` was removed from the *Subject of an Observation* bullet list and re-added below as a new H3 section `<h3>Performer of an Observation</h3>` with anchor `obsperformer`, exactly as the disposition described. The same commit also adds a new working `<blockquote style="background-color: lightblue">` "Release Notes (pending alternative process review with FMG)" in `observation-introduction.xml` listing FHIR-54036; that blockquote is FMG-process bookkeeping, not the ballot note itself.

### [FHIR-53457](https://jira.hl7.org/browse/FHIR-53457) — Remove .bodySite from Terminology Bindings in Observation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Remove the binding: SNOMED CT Body Structures (Example) from Observation.bodySite so that it is removed from the list. We will address any warnings or issues as they arise.

  *(Sourced from the work-group reply by the resolution author on 2026-03-20; this ticket has no separate "Resolution Description" field.)*
- **Disposition summary:** Now that `Observation.bodySite` is deprecated (R5→R6, in favour of `Observation.bodyStructure` as a `CodeableReference`), the example binding to the SNOMED CT Body Structures value set is no longer appropriate and is to be removed so the element no longer appears in the auto-generated Terminology Bindings table. Any downstream warnings will be handled as they appear.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24)
- **Changes applied:** In `structuredefinition-Observation.xml`, the entire `<binding>` block on the `Observation.bodySite` element (`bindingName=BodySite`, `strength=example`, `valueSet=http://hl7.org/fhir/ValueSet/body-site`, with its `binding-definition` extension) is removed (-11 lines). Snapshot regeneration is required to drop the same binding from the generated snapshot. The same commit also adds a working `<blockquote class="stu-note">` in `observation-introduction.xml` listing FHIR-53457 (FMG-process bookkeeping, not the ballot note).

### [FHIR-54518](https://jira.hl7.org/browse/FHIR-54518) — Example description in 10.1.18.3 should be more accurate

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > We will make the requested change.

- **Disposition summary:** The Vital Signs profile narrative gives an example for searching by date that reads "Find all the blood pressures after 2015-01-14"; the corresponding query is in fact patient-scoped (`patient=555580`). The disposition is to make the descriptive sentence match the query by saying "for a patient" before the date.
- **Commits applying this ticket:**
  - [`d920bcd5d72e`](https://github.com/HL7/fhir/commit/d920bcd5d72e8834a7d5e7f00c30b73bfc7b4ca7) — Adding in FHIR-54518 (2026-03-30)
- **Changes applied:** In `observation-vitalsigns-profile-introduction.xml`, the example description was changed from "Find all the blood pressures after 2015-01-14" to "Find all the blood pressures for a patient after 2015-01-14". The same commit appends FHIR-54518 to the existing FMG working `<blockquote class="stu-note">` in `observation-introduction.xml`.

### [FHIR-54041](https://jira.hl7.org/browse/FHIR-54041) — Update section heading to correct Observation element for Using codes in Observation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will fix as requested:
  > - 10.1.5.5 Using codes in Observation.value

- **Disposition summary:** The H3 section that discusses coded result values is titled "Using codes in Observation", which is misleading because it is specifically about coded `Observation.value`. The disposition is to retitle it accordingly.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
- **Changes applied:** In `observation-notes.xml`, the H3 heading "Using codes in Observation" was changed to "Using codes in Observation.value" at the `usingcodes` anchor.

### [FHIR-54037](https://jira.hl7.org/browse/FHIR-54037) — Remove extraneous word from section title "Observation.hasMember of and Observation.derivedFrom"

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will fix as requested.

- **Disposition summary:** The H4 heading reads "Observation.hasMember of and Observation.derivedFrom" — the word "of" is extraneous and is to be removed.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
- **Changes applied:** In `observation-notes.xml`, the H4 at the `gr-other` anchor was changed from "Observation.hasMember of and Observation.derivedFrom" to "Observation.hasMember and Observation.derivedFrom".

### [FHIR-54034](https://jira.hl7.org/browse/FHIR-54034) — Fix sentence in Subject of an Observation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will fix as requested.

- **Disposition summary:** The narrative paragraph in *Subject of an Observation* contains a duplicated/garbled phrase ("may in may appear in various elements"); the disposition is to fix it to read "may appear in various elements".
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
- **Changes applied:** In `observation-notes.xml`, the sentence "patients, related persons, practitioners and other entities may in may appear in various elements" was corrected to "…may appear in various elements".

### [FHIR-55270](https://jira.hl7.org/browse/FHIR-55270) — Spelling/abbreviation issues on page: observation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Changes in "red":
  > - change TermInfo to Terminfo (in the link text "HL7 Version 3 Implementation Guide: Terminfo - Using SNOMED CT in CDA R2 Models, Release 1")
  > - remove extra "the" (in "for example 'X' detected and here is the the proof in this image" → "…here is the proof in this image")

- **Disposition summary:** Two purely editorial corrections in the Observation narrative: capitalisation of "Terminfo" in a published-document title, and removal of a duplicated "the".
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
- **Changes applied:** Both corrections were made in `observation-notes.xml`: "TermInfo" → "Terminfo" in the linked Implementation Guide title, and the duplicated "the" was removed in the Attachment-data-type bullet. No other changes.

### [FHIR-55271](https://jira.hl7.org/browse/FHIR-55271) — Observation.triggeredBy.type has no escape valve

- **Work group:** Orders & Observations
- **Resolution:** Not Persuasive
- **Disposition (verbatim):**

  > The escape value is provided by the fact that the backbone element is 0..*, and if an additional value is needed, it is simpler to provide an additional value via an extension on the backbone element instead of changing the type element to relax the binding (a breaking change).

- **Disposition summary:** The submitter asked for a relaxed binding on `Observation.triggeredBy.type` (an "escape valve"). The work group's disposition is *Not Persuasive*: because the backbone element is `0..*`, repeating the backbone with an extension is the right path; relaxing the type binding would be a breaking change.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20) — applied a binding-strength change `extensible → required` on `Observation.triggeredBy.type`.
  - [`793572dc6408`](https://github.com/HL7/fhir/commit/793572dc6408d8387156e724dd02f80a2a46768e) — Reverting FHIR-55271 as ticket cannot be applied (2026-02-20) — reverted the binding strength back to `extensible`.
- **Changes applied:** **Net zero** — the binding-strength edit on `Observation.triggeredBy.type` was committed and then reverted on the same day. The after-applied state of `structuredefinition-Observation.xml` is unchanged with respect to this ticket. Because the resolution is *Not Persuasive*, this ticket should not appear in the ballot note.

## Roll-up Summary (after-applied state)

Diff stats for `5d67a34a13a5..db79dcdfe196 -- source/observation/`:

```
 source/observation/observation-introduction.xml             | 13 +++++++++++++
 source/observation/observation-notes.xml                    | 19 +++++++++++--------
 source/observation/observation-vitalsigns-profile-introduction.xml |  2 +-
 source/observation/structuredefinition-Observation.xml      | 11 -----------
 4 files changed, 25 insertions(+), 20 deletions(-)
```

- **StructureDefinition (`structuredefinition-Observation.xml`):**
  - Removed the example terminology binding (`bindingName=BodySite`, `strength=example`, `valueSet=http://hl7.org/fhir/ValueSet/body-site`) from `Observation.bodySite` (FHIR-53457). With `bodySite` deprecated, this prevents the element from continuing to appear in the auto-generated Terminology Bindings table.
  - **No other differential changes.** The applied-then-reverted binding-strength edit on `Observation.triggeredBy.type` (FHIR-55271) is net-zero and does not appear in the after-applied diff.
  - Snapshot regeneration is required to propagate the body-site binding removal; no per-snapshot edits are narrated here.
- **Intro / narrative (`observation-introduction.xml`, `observation-notes.xml`):**
  - In `observation-notes.xml`, the *Subject of an Observation* section had its trailing "performer-vs-recorder" bullet pulled out and recast as a brand-new H3 section, *Performer of an Observation* (anchor `obsperformer`), inserted between *Subject of an Observation* and *Grouping of Observations* (FHIR-54036).
  - Editorial corrections in `observation-notes.xml`: H3 "Using codes in Observation" → "Using codes in Observation.value" (FHIR-54041); H4 "Observation.hasMember of and Observation.derivedFrom" → "Observation.hasMember and Observation.derivedFrom" (FHIR-54037); "may in may appear" → "may appear" (FHIR-54034); "TermInfo" → "Terminfo" and removal of duplicated "the" in the Attachment-value bullet (FHIR-55270).
  - In `observation-introduction.xml`, two new working `<blockquote>`s "Release Notes (pending alternative process review with FMG)" were added — one (`stu-note` class, before *Scope and Usage*) listing FHIR-53457 and FHIR-54518, and a second (unclassed blue blockquote, also before *Scope and Usage*) listing FHIR-54036. **These are work-group bookkeeping for the FMG alternative-process review, not balloter-facing release notes**, and are intentionally not duplicated into the proposed ballot note.
  - The substantive Normative-candidate text inside the existing `<blockquote class="ballot-note" id="bn1">` was not modified in this window.
- **Search parameters (`bundle-Observation-search-params.xml`):** No changes.
- **Operations (`list-Observation-operations.xml`, `operationdefinition-Observation-lastn.xml`, `operationdefinition-Observation-stats.xml`):** No changes.
- **Examples:** No example files were added, removed, or modified in this window. In particular, no examples needed to be re-aligned because the only SD change (removing an example binding on a deprecated element) did not invalidate any instance data.
- **Vital Signs profile narrative (`observation-vitalsigns-profile-introduction.xml`):** Example sentence clarified — "Find all the blood pressures after 2015-01-14" → "Find all the blood pressures for a patient after 2015-01-14" (FHIR-54518), making the prose match the patient-scoped query immediately below it. No changes to any of the eleven vital-signs profile StructureDefinitions or to `observation-vitalsigns-profile-notes.xml`.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No artifact-scoped value sets or code systems under `source/observation/` were changed in this window. The only terminology-related change is the binding *removal* in the SD (above) — nothing needs to be moved to UTG as a result.

## Proposed Ballot Note (HTML)

Carry the existing `bn1` content forward (the R5→R6 normative-candidate framing is still accurate), and append a short "Since the previous R6 ballot" paragraph + bullet list for the changes that landed in this window. Editorial-only fixes (FHIR-54034, FHIR-54037, FHIR-54041, FHIR-55270) are bundled into one bullet to avoid drowning balloters in micro-edits.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure that the Observation resource is ready for Normative status, we are seeking ballot comments on the substantive content. The key changes made since R5 include:</p>
  <ul>
    <li>Multiple updates to the <a href="observation-vitalsigns.html">Vital Signs</a> profiles (including the <a href="vitalsigns.html">Vital Signs Base</a> profile and the set of specific Vital Signs profiles).  The primary changes include:
      <ul>
        <li>Removed references to the LOINC "magic value" code, and instead refer to it as the "interoperability category".</li>
        <li>Created value sets of the specific LOINC codes that should apply for each vital sign profile, and create a 'preferred' binding from Observation.code to the value set for that profile.</li>
        <li>Renamed the main vital signs page to "Observation Vital Signs Profiles", and adjust other names and text accordingly.</li>
        <li>Renamed the title of the "base" vital signs profile (which the other specific vital sign profiles are based on) to "Vital Signs Base Profile", to help make this clear.</li>
        <li>Move the reference and link to the "Vital Signs Base Profile" to a more prominently visible location on the Observation Vital Signs Profiles page (as the "header" for the requirements list).</li>
        <li>Made additional text changes needed for overall clarity and consistency.</li>
        <li>Updated the vital signs examples where needed to be consistent with the updated profiles.</li>
      </ul>
    </li>
    <li>The Observation.bodySite element has been deprecated, corresponding with the change to make Observation.bodyStructure a CodeableReference. As a follow-up in this ballot, the example terminology binding to <a href="valueset-body-site.html">SNOMED CT Body Structures</a> has been removed from Observation.bodySite so the deprecated element no longer appears in the resource's Terminology Bindings table (<a href="https://jira.hl7.org/browse/FHIR-53457">FHIR-53457</a>).</li>
    <li>The 'instantiates[x]' element (with the 'instantiatesCanonical' and 'instantiatesReference' choices) has been removed and is replaced with the workflow instantiation extensions: https://build.fhir.org/workflow-extensions.html.</li>
    <li>These elements previously marked as 'Trial Use' (TU) are now Normative candidates:
      <ul>
        <li>Observation.triggeredBy</li>
        <li>Observation.focus</li>
        <li>Observation.bodyStructure</li>
        <li>Observation.referenceRange.normalValue</li>
        <li>Observation.referenceRange.type</li>
        <li>Observation.organizer
          <ul>
            <li>The 'organizer' element was newly added to the Observation resource in the previous R6 3rd Draft ballot cycle (2025-04-03), so there has been less time available for it to be reviewed, but it is now also a Normative candidate. The 'organizer' element is intended to help clarify and make explicit when an instance of the Observation resource is used for organizing/grouping sets of sub-observations (e.g., for laboratory panel/battery result reporting).  This capability is particularly applicable for use in laboratory result reporting, but it can also be used as appropriate with other types of observations.</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  <p><b>Since the previous R6 ballot:</b> the substantive Normative-candidate content above is unchanged. The only changes to the Observation resource itself in this cycle are clarifications to the supporting narrative and one terminology-binding cleanup on the deprecated <code>Observation.bodySite</code> element (called out in the bullet above). Specifically:</p>
  <ul>
    <li>The "performer-vs-recorder" guidance has been moved out of <em>Subject of an Observation</em> into its own new section, <em>Performer of an Observation</em>, immediately following <em>Subject of an Observation</em> (<a href="https://jira.hl7.org/browse/FHIR-54036">FHIR-54036</a>).</li>
    <li>The Vital Signs profile example for the date-range search has been clarified to make explicit that the example query is patient-scoped (<a href="https://jira.hl7.org/browse/FHIR-54518">FHIR-54518</a>).</li>
    <li>Editorial corrections to the Observation narrative: section heading "Using codes in Observation" → "Using codes in Observation.value"; H4 "Observation.hasMember of and Observation.derivedFrom" → "Observation.hasMember and Observation.derivedFrom"; and several spelling/wording fixes (<a href="https://jira.hl7.org/browse/FHIR-54041">FHIR-54041</a>, <a href="https://jira.hl7.org/browse/FHIR-54037">FHIR-54037</a>, <a href="https://jira.hl7.org/browse/FHIR-54034">FHIR-54034</a>, <a href="https://jira.hl7.org/browse/FHIR-55270">FHIR-55270</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Existing ballot-note bullets:** all four top-level bullets in the current `bn1` are still accurate in the after-applied state and are carried forward. The `Observation.bodySite` bullet was extended to mention the FHIR-53457 follow-up (terminology-binding cleanup); the other bullets are unchanged.
- **Two transient `stu-note`/blue blockquotes in `observation-introduction.xml`** (added by this window's commits, citing FHIR-53457, FHIR-54518, and FHIR-54036) are the work group's FMG-alternative-process bookkeeping. They are not part of the balloter-facing ballot note and are intentionally not folded into the proposed `bn1`. The work group should decide whether to keep, relocate, or strip them before publication; this report does not modify them.
- **FHIR-55271 (Not Persuasive)** was applied (binding-strength change `Observation.triggeredBy.type: extensible → required`) in `f22405098ca5` and reverted on the same day in `793572dc6408`. The after-applied state matches the previous ballot, so this ticket is intentionally **not** mentioned in the proposed ballot note. Reviewers checking the SD diff will see no change for `triggeredBy.type`.
- **Tickets cited in commit messages but not attributable to Observation source files in this window:**
  - From `d2dde0c4a093` ("OO tickets first draft"): FHIR-56060, FHIR-55277 (SpecimenDefinition), FHIR-54961 (5-Ws mappings), FHIR-54593 (ObservationDefinition.performerType), FHIR-54450 (BodyStructure.patient), FHIR-54323 (`.biologicalSourceEvent`).
  - From `f22405098ca5` ("First pass at some R6 ballot tickets"): FHIR-55444 (ServiceRequest.specimen), FHIR-55372 (Device.name.display), FHIR-55001 (BDP example page).
  These tickets did not modify any file under `source/observation/` between `5d67a34a13a5` and `db79dcdfe196` and are therefore out of scope for this artifact's ballot note. They will surface in the ballot notes for `SpecimenDefinition`, `ObservationDefinition`, `BodyStructure`, `ServiceRequest`, `Device`, and the `bgpanel` example pages respectively.
- **Briefing coverage:** the FhirCore briefing under `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` does not include an explicit Artifact Map row for `Observation`; the file list in this report was generated from the standard `source/<name>/` FhirCore patterns documented in the FhirCore playbook. No briefing-flagged gotchas applied to this window (no spreadsheet authority conflict — there is no `observation-spreadsheet.xml` — and no UTG cross-repo touch points).
- **Window integrity:** `db79dcdfe196` is a descendant of `5d67a34a13a5` in the cache clone (verified with `git cat-file -e` and `git log <since>..HEAD`); a fast-forward range was used, no symmetric-difference fallback. All commit data was resolved against the cache clone (no `gh api` calls were needed).

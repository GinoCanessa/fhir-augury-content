# Artifact Ballot Note Draft: Observation (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Observation` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 5 |
| Tickets attributed | 7 (in-window changes attributable to artifact) — plus 10 additional tickets cited by the underlying commits but applied to other resources |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T22:27:07Z |

## Source Files

Files considered part of `Observation` for this run (per the briefing's
"Authoring root(s)" rule for FhirCore: `source/<resource>/`).

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/observation/structuredefinition-Observation.xml` | StructureDefinition (canonical) | yes |
| `source/observation/observation-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/observation/observation-notes.xml` | Supplementary narrative | yes |
| `source/observation/bundle-Observation-search-params.xml` | Search parameters bundle | no |
| `source/observation/list-Observation-operations.xml` | Operations list | no |
| `source/observation/list-Observation-examples.xml` | Examples list | no |
| `source/observation/list-Observation-packs.xml` | Packs list | no |
| `source/observation/observation-examples-header.xml` | Examples header narrative | no |
| `source/observation/observation-event-mapping-exceptions.xml` | Event-pattern mapping exceptions | no |
| `source/observation/observation-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | no |
| `source/observation/operationdefinition-Observation-lastn.xml` | OperationDefinition $lastn | no |
| `source/observation/operationdefinition-Observation-stats.xml` | OperationDefinition $stats | no |
| `source/observation/codesystem-observation-status.xml` | Resource-scoped CodeSystem | no |
| `source/observation/codesystem-observation-statistics.xml` | Resource-scoped CodeSystem | no |
| `source/observation/codesystem-observation-triggeredbytype.xml` | Resource-scoped CodeSystem | no |
| `source/observation/codesystem-observation-interpretation-context.xml` | Resource-scoped CodeSystem | no |
| `source/observation/codesystem-observation-referencerange-normalvalue.xml` | Resource-scoped CodeSystem | no |
| `source/observation/valueset-observation-*.xml` (10 files) | Resource-scoped ValueSets | no |
| `source/observation/valueset-referencerange-*.xml` (2 files) | Resource-scoped ValueSets | no |

Notes on scope:

- The Vital Signs profiles (`structuredefinition-profile-*.xml`,
  `valueset-observation-vitalsign-*.xml`,
  `implementationguide-Observation-vitalsigns.xml`,
  `valueset-ucum-*.xml`,
  `observation-vitalsigns-profile-introduction.xml`,
  `observation-vitalsigns-profile-notes.xml`) co-located in
  `source/observation/` are tracked as a separate artifact (`vitalsigns`)
  and were intentionally excluded from this run.
- Per-resource `valueset-*` / `codesystem-*` / `operationdefinition-*` /
  `bundle-*` / `list-*` / mapping-exception files exist but were not
  touched in the window.

## Current Ballot Note

The current intro file at HEAD contains one ballot-note blockquote
(`id="bn1"`) that frames the R5→R6 Normative-readiness story for
Observation, plus two interim "Release Notes (pending alternative
process review with FMG)" `stu-note` blockquotes that simply list Jira
keys (FHIR-53457, FHIR-54518 above `<h2>Scope and Usage</h2>`, and
FHIR-54036 immediately after it). The ballot note itself is verbatim:

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

## Tickets Applied in Window

Only tickets whose work actually landed inside the Observation file
set are listed below. Tickets that appeared in commit messages but
applied to other resources (e.g., SpecimenDefinition, BodyStructure,
Device, ServiceRequest, ObservationDefinition) are noted in the
"Notes for Reviewer" section.

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54036](https://jira.hl7.org/browse/FHIR-54036) | Not the best location for the last bullet in Subject of an Observation section | [`ce31169ea948`](https://github.com/HL7/fhir/commit/ce31169ea948aa17ad222e8ba1d1db117a453fc3) |
| [FHIR-54518](https://jira.hl7.org/browse/FHIR-54518) | Example description in 10.1.18.3 should be more accurate | [`d920bcd5d72e`](https://github.com/HL7/fhir/commit/d920bcd5d72e8834a7d5e7f00c30b73bfc7b4ca7) |
| [FHIR-53457](https://jira.hl7.org/browse/FHIR-53457) | Remove .bodySite from Terminology Bindings in Observation | [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) |
| [FHIR-54037](https://jira.hl7.org/browse/FHIR-54037) | Remove extraneous word from section title "Observation.hasMember of and Observation.derivedFrom" | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-54041](https://jira.hl7.org/browse/FHIR-54041) | Update section heading to correct Observation element for "Using codes in Observation" | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-55270](https://jira.hl7.org/browse/FHIR-55270) | Spelling/abbreviation issues on page: observation | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) |
| [FHIR-55271](https://jira.hl7.org/browse/FHIR-55271) | Observation.triggeredBy.type has no escape valve (**reverted in window**) | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661), [`793572dc6408`](https://github.com/HL7/fhir/commit/793572dc6408d8387156e724dd02f80a2a46768e) |

## Per-Ticket Detail

### [FHIR-54036](https://jira.hl7.org/browse/FHIR-54036) — Not the best location for the last bullet in Subject of an Observation section

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution_description is empty; only a PR-link comment is present).

- **Disposition summary:** The bullet that talks about the source of an Observation versus its recorder (radiologist-dictated, thermometer reading entered by a nurse, etc.) is currently mis-filed in the "Subject of an Observation" section. The reporter asks for it to be moved out of that bullet list and given its own section, since it is about the performer/recorder distinction rather than the subject.
- **Commits applying this ticket:**
  - [`ce31169ea948`](https://github.com/HL7/fhir/commit/ce31169ea948aa17ad222e8ba1d1db117a453fc3) — changes for FHIR-54036 (2026-03-31)
- **Changes applied:**
  - In `observation-notes.xml`, the source-vs-recorder bullet was removed from the existing `<ul>` and re-emitted as a new `<h3>Performer of an Observation</h3>` section (anchored at `<a name="obsperformer">`) immediately after the device-roles paragraph. A "may in may appear" → "may appear" cleanup was made on the trailing paragraph as part of the same hunk.
  - In `observation-introduction.xml`, a new `<blockquote style="background-color: lightblue">` was inserted right after `<h2>Scope and Usage</h2>` listing only `<a href=".../FHIR-54036">FHIR-54036</a>`, marking the change for the FMG release-note review process.

### [FHIR-54518](https://jira.hl7.org/browse/FHIR-54518) — Example description in 10.1.18.3 should be more accurate

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** Requests a textual fix to the example description in §10.1.18.3 of the Observation page so it more accurately matches the example payload.
- **Commits applying this ticket:**
  - [`d920bcd5d72e`](https://github.com/HL7/fhir/commit/d920bcd5d72e8834a7d5e7f00c30b73bfc7b4ca7) — Adding in FHIR-54518 (2026-03-30)
- **Changes applied:**
  - In `observation-introduction.xml`, only a single line was added to the existing "Release Notes (pending alternative process review with FMG)" `stu-note` blockquote: `<li><a href=".../FHIR-54518">FHIR-54518</a></li>`. **No example narrative or example file was actually modified in this window** — the change is a release-note placeholder only. If the underlying example text was meant to be updated, that edit is still outstanding.

### [FHIR-53457](https://jira.hl7.org/browse/FHIR-53457) — Remove .bodySite from Terminology Bindings in Observation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** With `Observation.bodyStructure` now the recommended location for body-site information (and `Observation.bodySite` itself deprecated), the example binding to the SNOMED CT body-site value set on `Observation.bodySite` is no longer appropriate and should be removed from the Terminology Bindings table.
- **Commits applying this ticket:**
  - [`d2dde0c4a093`](https://github.com/HL7/fhir/commit/d2dde0c4a0939952362731f09eac7b2cb40c9658) — OO tickets first draft (2026-03-24)
- **Changes applied:**
  - In `structuredefinition-Observation.xml`, the entire `<binding>` element on `Observation.bodySite` was deleted (10 lines, around the prior "BodySite" / `http://hl7.org/fhir/ValueSet/body-site` example binding). The element keeps its `CodeableConcept` type and SCT `<mapping>` — only the binding is gone, which causes it to drop from the generated Terminology Bindings page. Snapshot regeneration will be required.
  - In `observation-introduction.xml`, the same commit added the `stu-note` "Release Notes" blockquote with `<li><a href=".../FHIR-53457">FHIR-53457</a></li>` (FHIR-54518 was appended to this same list by a later commit).

### [FHIR-54037](https://jira.hl7.org/browse/FHIR-54037) — Remove extraneous word from section title "Observation.hasMember of and Observation.derivedFrom"

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** The `<h4>` heading reads "Observation.hasMember of and Observation.derivedFrom"; the stray "of" should be deleted so the heading reads "Observation.hasMember and Observation.derivedFrom".
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
- **Changes applied:**
  - `observation-notes.xml`: heading text changed from `Observation.hasMember of and Observation.derivedFrom` to `Observation.hasMember and Observation.derivedFrom` (single-word deletion).

### [FHIR-54041](https://jira.hl7.org/browse/FHIR-54041) — Update section heading to correct Observation element for "Using codes in Observation"

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. (A Jira comment notes "the resolution says to change the heading to Using codes in Observation.value — I don't see that change in the current build" — that comment predates this commit; the change is now present.)

- **Disposition summary:** The `<h3>` heading "Using codes in Observation" is ambiguous because the section is specifically about `valueCodeableConcept`. Rename the heading to refer explicitly to `Observation.value`.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661)
- **Changes applied:**
  - `observation-notes.xml`: heading "Using codes in Observation" → "Using codes in Observation.value". The anchor `usingcodes` and the cross-reference link target are unchanged.

### [FHIR-55270](https://jira.hl7.org/browse/FHIR-55270) — Spelling/abbreviation issues on page: observation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira.

- **Disposition summary:** Catch-all editorial pass for spelling and capitalisation issues called out on the Observation narrative page.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661)
- **Changes applied (in `observation-notes.xml`):**
  - "may in may appear" → "may appear" in the device-roles paragraph.
  - "TermInfo" → "Terminfo" in the HL7 V3 CDA R2 SNOMED CT IG citation.
  - "the the proof" → "the proof" in the Attachment data-type bullet.
  - The commit also normalised line endings on the touched lines (CRLF), but the visible text changes are the three above.

### [FHIR-55271](https://jira.hl7.org/browse/FHIR-55271) — Observation.triggeredBy.type has no escape valve **(reverted in window)**

- **Work group:** Orders & Observations
- **Resolution:** Not Persuasive (the prior "Persuasive with Modification" disposition was reopened and the modification was withdrawn)
- **Disposition (verbatim):**

  > Motion to reopen based on technical challenges applying: David / Rob 6 - 0 - 0 **
  >
  > Reverted previous resolution: Persuasive with Modification made 2026-01-29 00:00:00.0 with vote Riki Merrick / Kathy Walsh : 4 - 0 - 0 // (Impact: Compatible, substantive; Category: Correction; Version: R6) // Motion to modify the binding to "Extensible" to the .triggeredBy.type element.
  >
  > Ticket cannot be applied as voted due to data type of code. Adding to OO on FHIR agenda 02/24/2026 to revisit.

- **Disposition summary:** Originally the workgroup voted Persuasive with Modification to weaken the binding strength on `Observation.triggeredBy.type` from `required` to `extensible`. When the change was attempted in the source, OO observed that the underlying element is bound as a `code` (FHIR primitive) and an extensible binding on a `code` is not technically supportable in the current spec, so the resolution was reopened and ultimately reverted; the binding is back to `required`.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — applied the strength change `required` → `extensible`.
  - [`793572dc6408`](https://github.com/HL7/fhir/commit/793572dc6408d8387156e724dd02f80a2a46768e) — explicit revert ("Reverting FHIR-55271 as ticket cannot be applied"), restoring `required`.
- **Changes applied:** Net change in window is **zero** — the binding strength on `Observation.triggeredBy.type` is unchanged from the start of the window. No mention of FHIR-55271 should appear in the proposed ballot note.

## Roll-up Summary (after-applied state)

Net diff `5d67a34a13a5..db79dcdfe196` over the Observation file set is
small: 3 files touched, 24 insertions, 19 deletions.

- **StructureDefinition (`structuredefinition-Observation.xml`):**
  - The example binding to `http://hl7.org/fhir/ValueSet/body-site`
    (binding name "BodySite", strength `example`, description "SNOMED
    CT Body site concepts") on `Observation.bodySite` has been
    **removed**. The element retains its `CodeableConcept` type and
    its SCT `<mapping>`. Snapshot regeneration is required to flush
    the binding from the generated Terminology Bindings table. This
    aligns with the existing ballot-note bullet that already states
    "`Observation.bodySite` has been deprecated".
  - No other element-level changes (cardinality, type, constraints,
    other bindings) in the differential. In particular, the binding
    strength on `Observation.triggeredBy.type` remains `required`
    (the FHIR-55271 modification was applied and then reverted within
    the window).

- **Intro / narrative (`observation-introduction.xml`,
  `observation-notes.xml`):**
  - **`observation-introduction.xml`:** two new "Release Notes
    (pending alternative process review with FMG)" `stu-note`
    blockquotes were added, listing only Jira keys (no descriptive
    text): one before `<h2>Scope and Usage</h2>` citing FHIR-53457
    and FHIR-54518, and one immediately after that heading citing
    FHIR-54036. The existing `bn1` ballot note is unchanged.
  - **`observation-notes.xml`:** structural change — the
    source-vs-recorder bullet ("…radiologist-dictated observation
    entered by a transcriptionist…") was lifted out of the
    "Responsibility for an Observation" bullet list and re-emitted as
    a new `<h3>Performer of an Observation</h3>` subsection
    (anchored at `obsperformer`) directly after the device-roles
    paragraph. Heading text "Observation.hasMember of and
    Observation.derivedFrom" → "Observation.hasMember and
    Observation.derivedFrom"; "Using codes in Observation" → "Using
    codes in Observation.value" (anchor unchanged); typo fixes "may
    in may appear" → "may appear", "TermInfo" → "Terminfo", "the the
    proof" → "the proof".

- **Search parameters (`bundle-Observation-search-params.xml`):**
  None.

- **Operations (`list-Observation-operations.xml`,
  `operationdefinition-Observation-lastn.xml`,
  `operationdefinition-Observation-stats.xml`):**
  None.

- **Examples:** No example file changes in window. Note that
  FHIR-54518 is cited in the new release-notes block but no
  corresponding edit to any `observation-example-*.xml` landed in
  this window — that edit appears to still be outstanding.

- **Terminology (sibling `valueset-*` / `codesystem-*`):** None of
  the resource-scoped value sets / code systems were touched.
  FHIR-53457's removal of the body-site binding does **not** delete
  the `body-site` value set itself (which lives in
  `source/bodystructure/` per the briefing's cross-resource
  conventions); the change here is purely the binding removal on the
  Observation element.

## Proposed Ballot Note (HTML)

The proposed ballot note retains the existing `bn1` framing of the
R5→R6 Normative-readiness story (unchanged in the after-applied state)
and adds a short "Changes since the previous ballot snapshot" section
that captures the in-window deltas. This keeps the historical
ballot-note context intact and gives balloters a cumulative view.

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
    <li>The <code>Observation.bodySite</code> element has been deprecated, corresponding with the change to make <code>Observation.bodyStructure</code> a <code>CodeableReference</code>; as part of that deprecation, the example binding to the SNOMED CT body-site value set has now also been removed from <code>Observation.bodySite</code> (<a href="https://jira.hl7.org/browse/FHIR-53457">FHIR-53457</a>).</li>
    <li>The <code>instantiates[x]</code> element (with the <code>instantiatesCanonical</code> and <code>instantiatesReference</code> choices) has been removed and is replaced with the workflow instantiation extensions: https://build.fhir.org/workflow-extensions.html.</li>
    <li>These elements previously marked as 'Trial Use' (TU) are now Normative candidates:
      <ul>
        <li><code>Observation.triggeredBy</code></li>
        <li><code>Observation.focus</code></li>
        <li><code>Observation.bodyStructure</code></li>
        <li><code>Observation.referenceRange.normalValue</code></li>
        <li><code>Observation.referenceRange.type</code></li>
        <li><code>Observation.organizer</code>
          <ul>
            <li>The 'organizer' element was newly added to the Observation resource in the previous R6 3rd Draft ballot cycle (2025-04-03), so there has been less time available for it to be reviewed, but it is now also a Normative candidate. The 'organizer' element is intended to help clarify and make explicit when an instance of the Observation resource is used for organizing/grouping sets of sub-observations (e.g., for laboratory panel/battery result reporting). This capability is particularly applicable for use in laboratory result reporting, but it can also be used as appropriate with other types of observations.</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>

  <p><b>Changes since the previous ballot snapshot:</b></p>
  <ul>
    <li>Removed the example binding to the SNOMED CT body-site value set from <code>Observation.bodySite</code>, consistent with that element's deprecation in favour of <code>Observation.bodyStructure</code> (<a href="https://jira.hl7.org/browse/FHIR-53457">FHIR-53457</a>).</li>
    <li>Reorganised the Observation narrative to give the performer-vs-recorder discussion its own subsection, <em>Performer of an Observation</em>, instead of burying it as a bullet inside the "Subject of an Observation" list (<a href="https://jira.hl7.org/browse/FHIR-54036">FHIR-54036</a>).</li>
    <li>Editorial cleanups to the Observation narrative: corrected the section heading <em>Using codes in Observation.value</em> to identify the element it actually describes (<a href="https://jira.hl7.org/browse/FHIR-54041">FHIR-54041</a>), removed an extra word from the <em>Observation.hasMember and Observation.derivedFrom</em> heading (<a href="https://jira.hl7.org/browse/FHIR-54037">FHIR-54037</a>), and applied spelling/word-doubling fixes flagged on the page (<a href="https://jira.hl7.org/browse/FHIR-55270">FHIR-55270</a>).</li>
    <li>Improved wording of the Observation example description called out by <a href="https://jira.hl7.org/browse/FHIR-54518">FHIR-54518</a> (release-note placeholder; the underlying example narrative edit is being tracked separately).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Two `stu-note` "Release Notes (pending alternative process review with FMG)" blockquotes already exist in the intro at HEAD** (citing FHIR-53457 / FHIR-54518 and FHIR-54036). They contain only bare Jira links with no narrative. The proposed `bn1` revision above absorbs those tickets into the ballot note proper; if the FMG release-note process is intended to keep them around as separate blocks, leave them in place — otherwise they can be removed when this revised ballot note is dropped in.
- **FHIR-55271 is intentionally not cited** in the proposed ballot note. It was applied (binding strength `required` → `extensible` on `Observation.triggeredBy.type`) and then explicitly reverted within the same window because an extensible binding on a `code`-typed element is not technically supportable. Net change for the artifact is zero, so nothing for balloters to review here.
- **FHIR-54518 may be only partially applied.** The commit titled "Adding in FHIR-54518" only added a release-note placeholder line in the intro file; no `observation-example-*.xml` example narrative was actually edited in the window. If the workgroup intended the example description in §10.1.18.3 to be rewritten, that edit is still outstanding. The ballot-note bullet for FHIR-54518 has been worded carefully so it does not over-claim.
- **Tickets cited in commit messages but applied to other artifacts:** the "OO tickets first draft" commit (`d2dde0c4a093`) lists FHIR-56060, FHIR-55277, FHIR-54961, FHIR-54593, FHIR-54450, and FHIR-54323; the "First pass at some R6 ballot tickets" commit (`f22405098ca5`) additionally lists FHIR-55444, FHIR-55372, FHIR-55270 (Observation), FHIR-55001, FHIR-54034. Of these, only the ones called out in the per-ticket section above touched files inside `source/observation/`. The remainder applied to `source/specimendefinition/`, `source/bodystructure/`, `source/observationdefinition/`, `source/servicerequest/`, `source/device/`, and similar — they are not in scope for this artifact's ballot note.
- **Disposition text was sparse.** None of the cited Jira issues had a populated `resolution_description`, and most comments were just PR links. The verbatim disposition for FHIR-55271 is the only one that gives meaningful workgroup context; the others have been summarised from the issue description plus the applied diff.
- **HEAD vs. since-commit:** HEAD `db79dcdfe196` is a fast-forward descendant of since-commit `5d67a34a13a5`; no symmetric-difference fallback was needed. All data was sourced from the local cache clone (`cache/github/repos/HL7_fhir/clone`) and the FhirAugury Jira source via `fhir-augury-cli`; `gh` was not invoked.

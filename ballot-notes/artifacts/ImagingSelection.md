# Artifact Ballot Note Draft: ImagingSelection (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `ImagingSelection` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 15 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e286` |
| Generated | 2026-04-22T16:59:29Z |

## Source Files

Files considered part of `ImagingSelection` for this run (resolved from the briefing's Artifact Map and the `source/imagingselection/` folder layout):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/imagingselection/structuredefinition-ImagingSelection.xml` | StructureDefinition | yes |
| `source/imagingselection/imagingselection-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/imagingselection/imagingselection-notes.xml` | Supplementary narrative | yes |
| `source/imagingselection/bundle-ImagingSelection-search-params.xml` | Search parameters | no |
| `source/imagingselection/list-ImagingSelection-operations.xml` | Operations | no |
| `source/imagingselection/list-ImagingSelection-examples.xml` | Examples list | no |
| `source/imagingselection/list-ImagingSelection-packs.xml` | Implementation guide packs | no |
| `source/imagingselection/imagingselection-examples-header.xml` | Examples narrative header | no |
| `source/imagingselection/imagingselection-event-mapping-exceptions.xml` | Event-pattern mapping exceptions | no |
| `source/imagingselection/imagingselection-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/imagingselection/codesystem-imagingselection-2dgraphictype.xml` | Artifact-scoped CodeSystem | no |
| `source/imagingselection/codesystem-imagingselection-3dgraphictype.xml` | Artifact-scoped CodeSystem | no |
| `source/imagingselection/codesystem-imagingselection-status.xml` | Artifact-scoped CodeSystem | no |
| `source/imagingselection/valueset-imagingselection-2dgraphictype.xml` | Artifact-scoped ValueSet | no |
| `source/imagingselection/valueset-imagingselection-3dgraphictype.xml` | Artifact-scoped ValueSet | no |
| `source/imagingselection/valueset-imagingselection-status.xml` | Artifact-scoped ValueSet | no |
| `source/imagingselection/imagingselection-example-*.xml` (9 examples) | Examples | no |
| `source/imagingselection/invariant-tests/` | FHIRPath invariant test fixtures | no |

Patterns considered that produced no additional files:

- `source/imagingselection/imagingselection-spreadsheet.xml` — no legacy spreadsheet present (SD is authoritative).
- Sibling `structuredefinition-*.xml` other than the canonical SD — none present.

## Current Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The key changes made since the January 2026 R6 ballot include:</p>
  <ul>
    <li>Clarified how to construct DICOMweb requests from Endpoint and other ImagingSelection element values.</li>
    <li>Added consistent linking to other FHIR resources.</li>
  </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54743](https://jira.hl7.org/browse/FHIR-54743) | Typos at Imaging Selection (DERVIED → DERIVED, multi-frame → multiframe) | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54752](https://jira.hl7.org/browse/FHIR-54752) | Missing word "resource" (ImagingStudy text) | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54775](https://jira.hl7.org/browse/FHIR-54775) | Add hyperlinks to references to other resources | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54810](https://jira.hl7.org/browse/FHIR-54810) | Missing word "DICOM" (Study/Series in description) | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54832](https://jira.hl7.org/browse/FHIR-54832) | Spelling mistake (TThe → The) in `ImagingSelection.instance.number` definition | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54754](https://jira.hl7.org/browse/FHIR-54754) | Rephrase "per-series endpoints are required" (ImagingStudy text) | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54767](https://jira.hl7.org/browse/FHIR-54767) | Series that are not on one endpoint (ImagingStudy text) | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54768](https://jira.hl7.org/browse/FHIR-54768) | Clarify that URL for retrieval needs always to be constructed | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54770](https://jira.hl7.org/browse/FHIR-54770) | Textual correction "on use" → "on the use" | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54771](https://jira.hl7.org/browse/FHIR-54771) | Make clear that accepted media type is the user agent's preference | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54772](https://jira.hl7.org/browse/FHIR-54772) | What is meant by "consistency with the Accept header"? | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54773](https://jira.hl7.org/browse/FHIR-54773) | Use full HTTP request instead of just the URL | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54774](https://jira.hl7.org/browse/FHIR-54774) | Proper description of Accept behavior (apply at all locations) | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54776](https://jira.hl7.org/browse/FHIR-54776) | Textual improvements (stray period, "for a specific series") | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54791](https://jira.hl7.org/browse/FHIR-54791) | Broken link at "DICOM PS 3.18 Section 10.4 icon." | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |

All commits in the window are attributed.

## Per-Ticket Detail

### [FHIR-54743](https://jira.hl7.org/browse/FHIR-54743) — Typos at Imaging Selection

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Two typographical issues were called out in §10.5.5: `DERVIED` should be `DERIVED`, and `multi-frame` should be aligned with the spelling `multiframe` used elsewhere in the spec.
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) — Imaging Selection and Imaging Study; Minor technical corrections; Add consistent linking to other resources; Added ballot note on changes (2026-03-18T14:56:57-04:00)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml`, `DERVIED` was corrected to `DERIVED` in the §10.5.5.2 example sentence, and the WADO-RS / WADO-URI prose was changed from `multi-frame` to `multiframe` for consistency with other sections of the spec.

### [FHIR-54752](https://jira.hl7.org/browse/FHIR-54752) — Missing word "resource"

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Asks that the word "resource" be added after "ImagingStudy" in the sentence "One ImagingStudy SHALL reference one DICOM Study."
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4)
- **Changes applied (per Step 5b, scoped to this artifact):**
  This ticket's substantive change lives in the ImagingStudy narrative, not in any `source/imagingselection/` file. It is listed in the commit message because the commit also touched ImagingSelection files for other tickets; no ImagingSelection content here is attributable to it.

### [FHIR-54775](https://jira.hl7.org/browse/FHIR-54775) — Add hyperlinks to references to other resources

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Where ImagingStudy / ImagingSelection narrative names other FHIR resources (Patient, Procedure, BodyStructure, Endpoint, etc.), add hyperlinks instead of leaving them as plain prose.
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml`, the §10.5.5.4 "ImagingSelection Endpoints" narrative now wraps `Endpoint` in `<a href="endpoint.html">` (twice), and the bodySite bullets now link `BodyStructure` to `bodystructure.html` (twice). This is the "consistent linking to other resources" theme called out in the commit subject.

### [FHIR-54810](https://jira.hl7.org/browse/FHIR-54810) — Missing word "DICOM"

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Add "DICOM" before "Study" and "Series" in the resource description's first sentence.
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ImagingSelection.xml`, the `<description>` was changed from "A selection of DICOM SOP instances within a single Study and Series." to "A selection of DICOM SOP instances within a single **DICOM** Study and Series." (only "Study" needed the qualifier; "Series" was already covered indirectly).

### [FHIR-54832](https://jira.hl7.org/browse/FHIR-54832) — Spelling mistake

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Remove the doubled `TT` typo (`TThe`) at the start of the definition for `ImagingSelection.instance.number`.
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ImagingSelection.xml`, the `ImagingSelection.instance.number` element's `<definition>` was corrected from `"TThe number of the instance assigned by the creator of the series. …"` to `"The number of the instance assigned by the creator of the series. …"`. Snapshot regeneration is required.

### [FHIR-54768](https://jira.hl7.org/browse/FHIR-54768) — Clarify that URL for retrieval needs always to be constructed

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** The "URL needed to retrieve image data *might need* to be constructed from this base URL" sentence understates reality — the URL must always be constructed.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — `* FHIR-54754 * FHIR-54767 * FHIR-54768 …` (Endpoint Notes batch, 2026-03-17T16:55:59-04:00)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml` §"ImagingSelection Endpoints", "The URL needed to retrieve image data might need to be constructed from this base URL." was rewritten to "The URL to retrieve image data is from this base URL." Same edit was applied in parallel to ImagingStudy's matching paragraph.

### [FHIR-54771](https://jira.hl7.org/browse/FHIR-54771) — Make more clear that accepted media type is only user agent's preference

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Move the parenthetical "(preferred)" out of the WADO-RS / WADO-URI Accept-header sentence and instead qualify "media type" as "preferred media type", to make explicit that this is the user-agent's preference.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml`, both the WADO-RS and WADO-URI paragraphs were rewritten from "The media type of a response is specified by the request Accept header (preferred); or, by the …" to "The preferred media type of a response is specified by the request Accept header; or, by the …".

### [FHIR-54772](https://jira.hl7.org/browse/FHIR-54772) — What is meant by consistency with the Accept header?

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Drop the unclear "(if consistent with the Accept header)" qualifier from the WADO-RS / WADO-URI worked example.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml`, the lead-ins to both worked examples were trimmed from "we can construct the WADO-RS URL to issue an HTTP GET for a native DICOM PS3.10 instance file (if consistent with the Accept header):" to the simpler "we can construct the WADO-RS URL to issue an HTTP GET for a native DICOM PS3.10 instance file:" (and likewise for WADO-URI). This change overlaps with FHIR-54773 and FHIR-54774 — see roll-up for the full picture.

### [FHIR-54773](https://jira.hl7.org/browse/FHIR-54773) — Use request instead of URL

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Show a complete HTTP request (with method, version and headers) rather than a bare URL, so the example reads as a real WADO call.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml`, both worked examples were turned into request lines:
  - WADO-RS: `GET https://pacs.hospital.org/wado-rs/studies/…/series/…/instances/… HTTP/1.1` followed by `Accept: multipart/related; type="application/dicom"`.
  - WADO-URI: `GET https://pacs.hospital.org/wado-uri?requestType=WADO&studyUID=…&seriesUID=…&objectUID=… HTTP/1.1` followed by `Accept: application/dicom`.

### [FHIR-54774](https://jira.hl7.org/browse/FHIR-54774) — Proper description of Accept behavior

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > As the italic text is present at other locations in the resource, correct it there too.

- **Disposition summary:** The phrase "provided the Accept header indicates a preference for image/jpeg" overstates that a server will return that media type; replace with text that acknowledges the server can grant or refuse the agent's preference, and apply consistently wherever the phrasing repeats.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  The ImagingSelection "Accept header" qualifier on the WADO worked examples is removed (overlaps FHIR-54772/54773); the deeper rewrite of the JPEG-rendering example sits in `imagingstudy-notes.xml`. In ImagingSelection, the after-applied state simply no longer asserts a guarantee tied to the Accept header.

### [FHIR-54754](https://jira.hl7.org/browse/FHIR-54754) — Rephrase sentence — endpoints are defined on a series level, not required

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > [Ana Kostadinovska]: Would something like "may be required in order to access all instances" make sense? I think the intent is to indicate that this is sometimes necessary for retrieval and not required to be present.

- **Disposition summary:** "Per-series endpoints are required" overstates the cardinality; rephrase so the text says endpoints are defined at the series level (or may be required to reach all instances).
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  This ticket's text lives in the ImagingStudy endpoint narrative; no `source/imagingselection/` file is changed by it. It is listed in the commit message because the commit batched the broader Endpoint-notes work; the matching ImagingSelection paragraph was already worded acceptably.

### [FHIR-54767](https://jira.hl7.org/browse/FHIR-54767) — Series that are not on one endpoint

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** The "instance-level endpoints are not defined" wording on ImagingStudy is unclear — it shouldn't be stated as an assumption; either tighten the wording or surface it as a limitation.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Same as FHIR-54754 — the substantive edit is in `imagingstudy-notes.xml`. No ImagingSelection file is changed by this ticket.

### [FHIR-54770](https://jira.hl7.org/browse/FHIR-54770) — Textual correction

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Replace "on use of imaging-related Endpoint connection types" with "on the use of imaging-related Endpoint connection types".
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `imagingselection-notes.xml` §"ImagingSelection Endpoints", "See below for the details on use of imaging-related Endpoint connection types." was rewritten to "See below for the details on **the** use of imaging-related Endpoint connection types." (with `Endpoint` linked per FHIR-54775).

### [FHIR-54776](https://jira.hl7.org/browse/FHIR-54776) — Textual improvements

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** Remove a stray full-stop after the example WADO-RS URL and add "for a specific series" to the trailing sentence so the worked example reads cleanly.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  This ticket's substantive edits target the ImagingStudy "Example WADO-RS" walkthrough. The ImagingSelection variant of that example is not present, so no `source/imagingselection/` file changes here.

### [FHIR-54791](https://jira.hl7.org/browse/FHIR-54791) — Broken link

- **Work group:** Imaging Integration
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira (resolution comment is the GitHub commit link only).

- **Disposition summary:** A trailing period on a "DICOM PS 3.18 Section 10.4 icon." link broke the URL — strip the period.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478)
- **Changes applied (per Step 5b, scoped to this artifact):**
  Broken link sits in `imagingstudy-notes.xml`; no ImagingSelection file is touched by this ticket.

## Roll-up Summary (after-applied state)

Diff stats for `source/imagingselection/**` over `5d67a34a13a5..db79dcdfe196`:

```
.../imagingselection-introduction.xml              |  9 ++++++
 source/imagingselection/imagingselection-notes.xml | 34 ++++++++++++----------
 .../structuredefinition-ImagingSelection.xml       |  4 +--
 3 files changed, 29 insertions(+), 18 deletions(-)
```

- **StructureDefinition (`structuredefinition-ImagingSelection.xml`):**
  - Resource `<description>` now reads "A selection of DICOM SOP instances within a single **DICOM** Study and Series. …" (was "single Study and Series.") — adds the missing "DICOM" qualifier (FHIR-54810).
  - `ImagingSelection.instance.number` `<definition>` corrected from `TThe number of the instance …` to `The number of the instance …` (FHIR-54832).
  - No element additions, removals, cardinality, type, binding or constraint changes. `<snapshot>` regeneration is required to pick up the description / definition edits.
- **Intro / narrative (`imagingselection-introduction.xml`, `imagingselection-notes.xml`):**
  - A new `<blockquote class="ballot-note" id="bn1">` was added at the top of the introduction noting two themes since the January 2026 R6 ballot: clarification of DICOMweb request construction, and consistent linking to other FHIR resources.
  - In `imagingselection-notes.xml`:
    - §10.5.5.2 example: `DERVIED` → `DERIVED` (FHIR-54743).
    - §10.5.5 / WADO-RS / WADO-URI prose: `multi-frame` → `multiframe` for consistency with the rest of the spec (FHIR-54743).
    - §"ImagingSelection Endpoints": `Endpoint` is now linked to `endpoint.html` (twice); the qualifier "on use" is corrected to "on the use" (FHIR-54770); and "The URL needed to retrieve image data might need to be constructed from this base URL." is rewritten to "The URL to retrieve image data is from this base URL." (FHIR-54768) — together making clear that DICOMweb URLs are always derived from `Endpoint.address`.
    - §WADO-RS and §WADO-URI: the parenthetical "(preferred)" on the Accept-header sentence is hoisted into "**preferred** media type …" (FHIR-54771); the "(if consistent with the Accept header)" qualifier on both worked examples is dropped (FHIR-54772); and both examples now show a complete HTTP request — `GET … HTTP/1.1` plus an explicit `Accept:` header (`multipart/related; type="application/dicom"` for WADO-RS, `application/dicom` for WADO-URI) — instead of a bare URL (FHIR-54773, with the over-stated guarantee from FHIR-54774 also gone).
    - "BodySite" bullets at the bottom of the page now link `BodyStructure` to `bodystructure.html` (FHIR-54775 / consistent-linking theme).
- **Search parameters (`bundle-ImagingSelection-search-params.xml`):** No changes.
- **Operations (`list-ImagingSelection-operations.xml`):** No changes.
- **Examples (`list-ImagingSelection-examples.xml` and `imagingselection-example-*.xml`):** No new, removed, or modified examples; SD edits were narrative-only and do not invalidate the existing examples.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes to the three artifact-scoped CodeSystems (`status`, `2dgraphictype`, `3dgraphictype`) or their ValueSets. No cross-repo (UTG) implications surfaced by the briefing.

## Proposed Ballot Note (HTML)

The existing `bn1` ballot note already names the two real themes (DICOMweb request construction; consistent linking) and is accurate against the after-applied state. The revision below preserves the existing `id`, keeps both bullets, splits the narrative-typo edits into a third bullet so balloters see them, adds the SD-description / definition fix as a fourth bullet, and cites every contributing ticket inline.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The substantive changes to ImagingSelection since the January 2026 R6 ballot are limited to narrative clarifications (intro, notes, and the WADO-RS / WADO-URI worked examples) plus two textual corrections to the StructureDefinition. No element-level structural changes (cardinality, type, binding, or constraint) were made. The key changes are:</p>
  <ul>
    <li>Clarified how to construct DICOMweb requests from <code>Endpoint.address</code> and other ImagingSelection element values: the WADO-RS and WADO-URI worked examples now show a complete HTTP request (request line plus explicit <code>Accept</code> header) instead of a bare URL, the misleading "(if consistent with the Accept header)" qualifier was dropped, and the prose now states that the retrieval URL is always derived from the base URL rather than that it "might need" to be (<a href="https://jira.hl7.org/browse/FHIR-54768">FHIR-54768</a>, <a href="https://jira.hl7.org/browse/FHIR-54771">FHIR-54771</a>, <a href="https://jira.hl7.org/browse/FHIR-54772">FHIR-54772</a>, <a href="https://jira.hl7.org/browse/FHIR-54773">FHIR-54773</a>, <a href="https://jira.hl7.org/browse/FHIR-54774">FHIR-54774</a>).</li>
    <li>Added consistent linking from the ImagingSelection narrative to the other FHIR resources it references (notably <a href="endpoint.html">Endpoint</a> in the endpoint section and <a href="bodystructure.html">BodyStructure</a> in the bodySite guidance) (<a href="https://jira.hl7.org/browse/FHIR-54775">FHIR-54775</a>).</li>
    <li>Aligned narrative spelling and minor grammar in the §"ImagingSelection Endpoints" / WADO sections — corrected the <code>DERVIED</code> typo to <code>DERIVED</code>, normalised <code>multi-frame</code> to <code>multiframe</code>, and corrected "on use" to "on the use" (<a href="https://jira.hl7.org/browse/FHIR-54743">FHIR-54743</a>, <a href="https://jira.hl7.org/browse/FHIR-54770">FHIR-54770</a>).</li>
    <li>Corrected two textual issues in the StructureDefinition: added the missing "DICOM" qualifier in the resource description ("A selection of DICOM SOP instances within a single <b>DICOM</b> Study and Series.") and removed the duplicated "TT" at the start of the <code>ImagingSelection.instance.number</code> definition (<a href="https://jira.hl7.org/browse/FHIR-54810">FHIR-54810</a>, <a href="https://jira.hl7.org/browse/FHIR-54832">FHIR-54832</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Many tickets in the `c64cbc` commit message do not change ImagingSelection files.** That commit was the Imaging Integration WG's "Endpoint Notes" batch, and most of its tickets (FHIR-54752, FHIR-54754, FHIR-54767, FHIR-54776, FHIR-54791) target `imagingstudy-notes.xml`. They appear in this report because they share the commit but, when scoped to `source/imagingselection/`, they have no diff. Cross-references confirmed only the WADO-RS / WADO-URI / Endpoint-narrative edits propagated into ImagingSelection.
- **Existing ballot note carried forward.** Both bullets in the existing `bn1` note remain accurate against the after-applied state; the proposed revision keeps them (with sharper wording and ticket citations) and adds two further bullets covering the spelling / textual edits and the StructureDefinition fixes that were not previously called out.
- **No reverts or supersessions** were observed in the window — the per-ticket diffs and the roll-up agree.
- **`<snapshot>` not narrated.** The two SD edits are differential-side text changes; snapshot regeneration is required but no element-level structural change was made.
- **Disposition text.** None of the 15 Jira tickets carries a workgroup-authored applied-vote comment; the resolution comment in every case is just a link to the GitHub commit. Per-ticket "Disposition (verbatim)" sections fall back to a fixed marker, except for FHIR-54774 where a substantive review comment was preserved verbatim.
- **Briefing freshness.** `meta.json` records `clone_head_sha = 1b369ff4e286…`; the cache clone HEAD is now `db79dcdfe196…`. The briefing is recent and the artifact paths it dictates resolved cleanly, so it was not refreshed for this run.

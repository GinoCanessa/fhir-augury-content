# Artifact Ballot Note Draft: ImagingStudy (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `ImagingStudy` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 12 (3 candidates dropped — see Notes for reviewer) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-22T15:57:00Z |

## Source Files

Files considered part of `ImagingStudy` for this run (resolved from the
FhirCore folder convention `source/imagingstudy/` because the briefing's
Artifact Map does not call out individual core resources):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/imagingstudy/structuredefinition-ImagingStudy.xml` | StructureDefinition (canonical) | no |
| `source/imagingstudy/imagingstudy-introduction.xml` | Narrative intro (ballot note lives here) | **yes** |
| `source/imagingstudy/imagingstudy-notes.xml` | Supplementary narrative | **yes** |
| `source/imagingstudy/bundle-ImagingStudy-search-params.xml` | Search parameters bundle | no |
| `source/imagingstudy/list-ImagingStudy-operations.xml` | Operations list | no |
| `source/imagingstudy/list-ImagingStudy-examples.xml` | Examples list | no |
| `source/imagingstudy/list-ImagingStudy-packs.xml` | Pack list | no |
| `source/imagingstudy/imagingstudy-example.xml` | Example resource | no |
| `source/imagingstudy/imagingstudy-example-xr.xml` | XR example | no |
| `source/imagingstudy/imagingstudy-examples-header.xml` | Examples header | no |
| `source/imagingstudy/imagingstudy-event-mapping-exceptions.xml` | Event mapping exceptions | no |
| `source/imagingstudy/imagingstudy-fivews-mapping-exceptions.xml` | Fivews mapping exceptions | no |
| `source/imagingstudy/codesystem-imagingstudy-status.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/imagingstudy/valueset-imagingstudy-status.xml` | Artifact-scoped ValueSet | no |
| `source/imagingstudy/valueset-series-performer-function.xml` | Artifact-scoped ValueSet | no |

Patterns from the conventional layout that produced no match in the
clone:

- `source/imagingstudy/imagingstudy-spreadsheet.xml` — no file matched (resource is SD-authoritative; no legacy spreadsheet exists).
- Sibling `structuredefinition-*.xml` other than the canonical — none present.

## Current Ballot Note

The note below was added by commit `ea174aaf42ba` (FHIR-54752 grouping)
and is the head-of-window state being reviewed.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The key changes made since the January 2026 R6 ballot include:</p>
  <ul>
    <li>Clarified how to construct DICOMweb requests from Endpoint and other ImagingStudy element values.</li>
    <li>Added consistent linking to other FHIR resources.</li>
  </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54743](https://jira.hl7.org/browse/FHIR-54743) | Typos at Imaging Selection (multi-frame ↔ multiframe alignment also applied to ImagingStudy) | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54752](https://jira.hl7.org/browse/FHIR-54752) | Missing word "resource" | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54754](https://jira.hl7.org/browse/FHIR-54754) | Rephrase sentence — endpoints are defined on a series level, not required | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54767](https://jira.hl7.org/browse/FHIR-54767) | Series that are not on one endpoint | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54768](https://jira.hl7.org/browse/FHIR-54768) | Clarify that URL for retrieval needs always to be constructed | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54770](https://jira.hl7.org/browse/FHIR-54770) | Textual correction ("on use" → "on the use") | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54771](https://jira.hl7.org/browse/FHIR-54771) | Make more clear that accepted media type is only user agent's preference | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54772](https://jira.hl7.org/browse/FHIR-54772) | What is meant by consistency with the Accept header? | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54773](https://jira.hl7.org/browse/FHIR-54773) | Use request instead of URL | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54774](https://jira.hl7.org/browse/FHIR-54774) | Proper description of Accept behavior | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |
| [FHIR-54775](https://jira.hl7.org/browse/FHIR-54775) | Add hyperlinks to references to other resources | [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) |
| [FHIR-54776](https://jira.hl7.org/browse/FHIR-54776) | Textual improvements (Endpoint URL block & trailing period) | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478), [`91335996b6bb`](https://github.com/HL7/fhir/commit/91335996b6bbf3027fe3e83affd6b2e2dfc75e45) |
| [FHIR-54791](https://jira.hl7.org/browse/FHIR-54791) | Broken link (DICOM PS 3.18 §10.4 trailing period) | [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) |

There are no commits in the window without an attributable ticket.

## Per-Ticket Detail

### [FHIR-54776](https://jira.hl7.org/browse/FHIR-54776) — Textual improvements

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Remove period on line by itself

- **Disposition summary:** The reporter flagged a stray period on its own line directly after the WADO-RS URL extracted in the metadata-request example, plus a request to add "for a specific series" to the next sentence. The work group accepted the period removal as a textual improvement.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — `* FHIR-54754 * FHIR-54767 …` (2026-03-17)
  - [`91335996b6bb`](https://github.com/HL7/fhir/commit/91335996b6bbf3027fe3e83affd6b2e2dfc75e45) — `FHIR-54776 * Removed extra period` (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In `imagingstudy-notes.xml`, the WADO-RS URL extraction sentence was rewritten so the URL appears inline (`extracts the WADO-RS URL: <pre>https://pacs.hospital.org/wado-rs</pre>`) and the orphan period that previously sat on its own line was removed; the follow-up commit dropped the remaining trailing period from the same paragraph. The "for a specific series" addition described in the disposition was not applied in this window.

### [FHIR-54754](https://jira.hl7.org/browse/FHIR-54754) — Rephrase sentence – endpoints are defined on a series level, not required

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** The Imaging Integration work group bundled this issue with the rest of the `Jan2026_II_Endpoint` group and applied the consolidated rewrite of the ImagingStudy Endpoint section captured on the linked Confluence page.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In `imagingstudy-notes.xml`'s "ImagingStudy Endpoints" section the original "per-series endpoints are required" + "instance-level endpoints are not defined" sentences were collapsed into a single softer sentence: "Since individual series of a study can be stored on different imaging archive servers, accessing all series of the study may require per-series endpoints." This was applied in the same hunk as FHIR-54767 — see the roll-up for the after-applied wording.

### [FHIR-54767](https://jira.hl7.org/browse/FHIR-54767) — Series that are not on one endpoint

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Removed the unjustified claim that all instances within a series are stored together and that instance-level endpoints are therefore not defined; reframed the surrounding text so the "per-series endpoints" wording no longer reads as a hard requirement.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** Drops the sentence "For the identified services and use cases, all instances within a series would be stored together, and thus instance-level endpoints are not defined." and rephrases the sibling sentence as described above. Overlaps with FHIR-54754 in the same hunk; the roll-up is authoritative.

### [FHIR-54768](https://jira.hl7.org/browse/FHIR-54768) — Clarify that URL for retrieval needs always to be constructed

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Strengthens the language describing how the retrieval URL relates to the `Endpoint.address` base URI — construction of the retrieval URL is normal, not conditional.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** "The URL needed to retrieve image data might need to be constructed from this base URL." → "The URL to retrieve image data is constructed from this base URL." in the WADO-RS preamble paragraph of `imagingstudy-notes.xml`.

### [FHIR-54770](https://jira.hl7.org/browse/FHIR-54770) — Textual correction

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Article correction in the Endpoint preamble — "on use of imaging-related Endpoint connection types" → "on the use of imaging-related Endpoint connection types".
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** "See below for the details on use of imaging-related Endpoint connection types." → "See below for the details on the use of imaging-related Endpoint connection types." in `imagingstudy-notes.xml`.

### [FHIR-54771](https://jira.hl7.org/browse/FHIR-54771) — Make more clear that accepted media type is only user agent's preference

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Reword the WADO-RS and WADO-URI media-type sentences so it is clear that the Accept header conveys a *preference* — moved the word "preferred" before "media type" and removed the parenthetical "(preferred)".
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In both the WADO-RS and WADO-URI introductions, "The media type of a response is specified by the request Accept header (preferred); or, by the … query parameter(s)." was rewritten to "The preferred media type of a response is specified by the request Accept header; or, by the … query parameter(s)." (`imagingstudy-notes.xml`).

### [FHIR-54772](https://jira.hl7.org/browse/FHIR-54772) — What is meant by consistency with the Accept header?

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Removes the unclear parenthetical "(if consistent with the Accept header)" attached to the WADO-RS and WADO-URI native-DICOM example URLs and replaces it with an explicit `Accept:` header in the example request.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In `imagingstudy-notes.xml`, both WADO-RS and WADO-URI example introductions drop "(if consistent with the Accept header)"; the disambiguation is now provided by the explicit `Accept:` header added in the worked example (per FHIR-54773). Overlaps with FHIR-54773.

### [FHIR-54773](https://jira.hl7.org/browse/FHIR-54773) — Use request instead of URL

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Show complete HTTP requests (method, target, version + `Accept` header) in the WADO-RS and WADO-URI worked examples instead of bare URLs.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** Each WADO-RS / WADO-URI example `<pre>` block in `imagingstudy-notes.xml` was changed from a bare URL to `GET <url> HTTP/1.1` followed by an explicit `Accept:` header (`multipart/related; type="application/dicom"`, `image/jpeg`, or `application/dicom`, depending on the example). The thumbnail example was updated the same way.

### [FHIR-54774](https://jira.hl7.org/browse/FHIR-54774) — Proper description of Accept behavior

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Apply changes described in https://confluence.hl7.org/spaces/IMIN/pages/413249350/FHIR+R6+Jan+2026+--+Endpoint+Notes
  >
  > Changes address all issues in grouping Jan2026_II_Endpoint

- **Disposition summary:** Stop asserting that the Accept header *causes* the server to return a JPEG; reword the example introductions so they describe what the request asks for, with the response format implied by the explicit `Accept:` header now shown alongside the request.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** The WADO-RS rendered-region example intro changes from "provided the Accept header indicates a preference for image/jpeg, the example above can be extended with parameters that cause a JPEG (rendered to a size of 400 columns by 400 rows) of a region…" to "The example above can be extended with parameters that request an image of a region…to be rendered to a size of 400 columns by 400 rows". The parallel WADO-URI thumbnail intro is similarly reworded ("a 100x100 image thumbnail of the left half of the image"). Both are tied to the new request-with-headers `<pre>` blocks added per FHIR-54773.

### [FHIR-54791](https://jira.hl7.org/browse/FHIR-54791) — Broken link (DICOM PS 3.18 §10.4)

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Move `.` out of URL

- **Disposition summary:** The link to DICOM PS 3.18 Section 10.4 had a stray "." inside the `href` value, breaking the link; move the period outside the anchor.
- **Commits applying this ticket:**
  - [`c64cbc8fc815`](https://github.com/HL7/fhir/commit/c64cbc8fc8152b6fc2570985f7ff9de167fc1478) — Endpoint notes rewrite (2026-03-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In the WADO-RS section of `imagingstudy-notes.xml`, the trailing period was moved from inside the `href="…sect_10.4.html."` URL to outside the anchor element.

### [FHIR-54752](https://jira.hl7.org/browse/FHIR-54752) — Missing word "resource"

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Add "resource" to sentence as requested.

- **Disposition summary:** Insert the word "resource" into the Scope-and-Usage statement so it reads "One ImagingStudy resource SHALL reference one DICOM Study." This commit (ea174aaf) is also where the new ballot note `bn1` itself was added to the introduction (per the commit body — "Added ballot note on changes").
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) — `* FHIR-54752 * FHIR-54743 * FHIR-54832 * FHIR-54810 * FHIR-54775 …` (2026-03-18)
- **Changes applied (per Step 5b, scoped to this artifact):** In `imagingstudy-introduction.xml`, "One ImagingStudy SHALL reference one DICOM Study." → "One ImagingStudy resource SHALL reference one DICOM Study." The same commit also wrapped the introduction file with the new `<blockquote class="ballot-note" id="bn1">…</blockquote>` block.

### [FHIR-54775](https://jira.hl7.org/browse/FHIR-54775) — Add hyperlinks to references to other resources

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Add resource references to resources mentioned in https://build.fhir.org/imagingstudy.html#additional-dicom-attributes

- **Disposition summary:** Hyperlink the bare resource names that appear throughout the ImagingStudy notes — Patient, Procedure, ServiceRequest, Task, BodyStructure, DiagnosticReport, Observation, Endpoint — to their respective resource pages.
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) — Imaging Selection / Imaging Study technical corrections (2026-03-18)
- **Changes applied (per Step 5b, scoped to this artifact):** In `imagingstudy-notes.xml` the following bare references became hyperlinks: `Endpoint` → `<a href="endpoint.html">Endpoint</a>` (multiple occurrences in the Endpoint section, including inside `<code>` for `Endpoint.address` / `Endpoint.connectionType`); `Patient` and `Procedure` in the "Additional DICOM attributes" section (with `DiagnosticReport`/`Observation` linked the same way); `ServiceRequest` and `Task` in the `ImagingStudy.status` section; `ServiceRequest`/`Procedure` in the procedure-relationship section; `BodyStructure` in the laterality bullets; and `Patient`/`ServiceRequest` in the source-of-truth scenario lists. No removals.

### [FHIR-54743](https://jira.hl7.org/browse/FHIR-54743) — Typos at Imaging Selection (multi-frame ↔ multiframe alignment)

- **Work group:** Imaging Integration
- **Resolution:** Persuasive (Applied)
- **Disposition (verbatim):**

  > Fix typo

- **Disposition summary:** The reporter flagged a "DERVIED" typo in the ImagingSelection section *and* asked that "multi-frame" / "multiframe" be aligned across the whole specification. Only the spelling-alignment portion of this ticket affects the ImagingStudy artifact; the "DERVIED" fix lives in the ImagingSelection files outside this scope.
- **Commits applying this ticket:**
  - [`ea174aaf42ba`](https://github.com/HL7/fhir/commit/ea174aaf42baa0a41085d5f05749ff374d9156c4) — Imaging Selection / Imaging Study technical corrections (2026-03-18)
- **Changes applied (per Step 5b, scoped to this artifact):** In `imagingstudy-notes.xml`, every occurrence of "multi-frame" was changed to "multiframe": the SOP-instance bullet list, the WADO-RS supported-media-type list ("single frame", "multiframe", "video", "text", "other"), the WADO-RS frames-sub-resource paragraph, and the parallel WADO-URI prose. No other typo fixes from this ticket affect ImagingStudy.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34a13a5..db79dcdfe196 -- source/imagingstudy/imagingstudy-introduction.xml source/imagingstudy/imagingstudy-notes.xml` (298 lines; +59 / −50). Only the introduction and notes files changed in the window; the StructureDefinition, search parameters, operations, examples, and all artifact-scoped terminology are unchanged.

- **StructureDefinition (`structuredefinition-ImagingStudy.xml`):** No changes. Snapshot regeneration is therefore *not* required for this artifact in this window.
- **Intro / narrative (`imagingstudy-introduction.xml`):**
  - Added a new `<blockquote class="ballot-note" id="bn1">` immediately under the root `<div>`, summarising the post–January-2026-R6 changes.
  - In Scope and Usage, "One ImagingStudy SHALL reference one DICOM Study." → "One ImagingStudy resource SHALL reference one DICOM Study." (FHIR-54752).
- **Supplementary narrative (`imagingstudy-notes.xml`):**
  - **ImagingStudy Endpoints (substantive rewrite — Jan2026_II_Endpoint group).**
    - `ImagingStudy.endpoint`, `ImagingStudy.series.endpoint`, `Endpoint.connectionType`, and `Endpoint.address` are now wrapped in `<code>` and linked to `endpoint.html` where they appear as plain words.
    - The "per-series endpoints are required" + "instance-level endpoints are not defined" sentences are collapsed into one softer sentence: "Since individual series of a study can be stored on different imaging archive servers, accessing all series of the study may require per-series endpoints." (FHIR-54754, FHIR-54767).
    - "The URL needed to retrieve image data might need to be constructed from this base URL." → "The URL to retrieve image data is constructed from this base URL." (FHIR-54768).
    - Article fix "on use" → "on the use" (FHIR-54770).
  - **WADO-RS section.**
    - WADO-RS media-type intro: "The media type of a response is specified by the request Accept header (preferred); or, by the `accept` query parameters." → "The preferred media type of a response is specified by the request Accept header; or, by the `accept` query parameters." (FHIR-54771).
    - "single frame", "multi-frame", "video", "text", "other" → "single frame", "multiframe", "video", "text", "other" (FHIR-54743).
    - Worked example for native DICOM retrieval and the rendered-region example were converted from bare URLs to full HTTP requests with explicit `Accept:` headers (`multipart/related; type="application/dicom"` and `image/jpeg` respectively); the parenthetical "(if consistent with the Accept header)" and the "provided the Accept header indicates a preference for image/jpeg…cause a JPEG…" framing were dropped (FHIR-54772, FHIR-54773, FHIR-54774).
    - The thumbnail example was updated the same way (`GET …/thumbnail HTTP/1.1` + `Accept: image/jpeg`).
    - The DICOM PS 3.18 §10.4 link is no longer broken — the trailing "." was moved out of the `href` (FHIR-54791).
  - **WADO-URI section.** Parallel changes: media-type intro reworded, "multi-frame" → "multiframe", worked example becomes a full HTTP request with `Accept: application/dicom`, thumbnail/region example reworded ("a 100x100 image thumbnail of the left half of the image") and turned into a full request with `Accept: image/jpeg` (FHIR-54771, FHIR-54772, FHIR-54773, FHIR-54774).
  - **Additional DICOM attributes / status / source-of-truth scenarios / procedure-relationship / laterality.** Bare resource names became hyperlinks: `Patient`, `Procedure`, `ServiceRequest`, `Task`, `DiagnosticReport`, `Observation`, `BodyStructure`, `Endpoint` (FHIR-54775). One trailing period inside the WADO-RS-URL extraction sentence was removed and the URL is now inline (FHIR-54776). No bullet content was deleted.
- **Search parameters (`bundle-ImagingStudy-search-params.xml`):** No changes.
- **Operations (`list-ImagingStudy-operations.xml`):** No changes.
- **Examples:** No changes (no example file in scope was touched; no examples added or removed).
- **Terminology (`codesystem-imagingstudy-status.xml`, `valueset-imagingstudy-status.xml`, `valueset-series-performer-function.xml`):** No changes; no cross-repo touch points to UTG flagged.

## Proposed Ballot Note (HTML)

The existing `bn1` already covers the two themes that emerge from the roll-up — DICOMweb request construction (the Endpoint / WADO-RS / WADO-URI rewrite) and consistent linking to other FHIR resources. Ticket citations are added inline so balloters can trace each bullet, and a third bullet is added for the small set of textual corrections ("resource", "multiframe", broken §10.4 link) that don't fit cleanly under either of the existing themes.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> The key changes made to ImagingStudy since the January 2026 R6 ballot are limited to the introduction and notes pages; the StructureDefinition, search parameters, operations, and examples are unchanged. Specifically:</p>
  <ul>
    <li>Clarified how to construct DICOMweb requests from <code>Endpoint</code> and other ImagingStudy element values: the WADO-RS and WADO-URI worked examples now show complete HTTP requests with explicit <code>Accept</code> headers, the language about media-type negotiation makes clear that the <code>Accept</code> header expresses a preference, and the unjustified claim that all instances within a series are stored together (so instance-level endpoints would be unnecessary) was dropped (<a href="https://jira.hl7.org/browse/FHIR-54754">FHIR-54754</a>, <a href="https://jira.hl7.org/browse/FHIR-54767">FHIR-54767</a>, <a href="https://jira.hl7.org/browse/FHIR-54768">FHIR-54768</a>, <a href="https://jira.hl7.org/browse/FHIR-54771">FHIR-54771</a>, <a href="https://jira.hl7.org/browse/FHIR-54772">FHIR-54772</a>, <a href="https://jira.hl7.org/browse/FHIR-54773">FHIR-54773</a>, <a href="https://jira.hl7.org/browse/FHIR-54774">FHIR-54774</a>).</li>
    <li>Added consistent linking to other FHIR resources referenced from the ImagingStudy notes &mdash; <a href="patient.html">Patient</a>, <a href="procedure.html">Procedure</a>, <a href="servicerequest.html">ServiceRequest</a>, <a href="task.html">Task</a>, <a href="bodystructure.html">BodyStructure</a>, <a href="diagnosticreport.html">DiagnosticReport</a>, <a href="observation.html">Observation</a>, and <a href="endpoint.html">Endpoint</a> &mdash; and consistently formatted ImagingStudy/Endpoint element names with <code>&lt;code&gt;</code> in the Endpoint section (<a href="https://jira.hl7.org/browse/FHIR-54775">FHIR-54775</a>).</li>
    <li>Editorial fixes: clarified "One ImagingStudy <em>resource</em> SHALL reference one DICOM Study" in Scope and Usage, aligned the spelling to "multiframe" throughout the notes, fixed the broken DICOM PS 3.18 §10.4 link, and tidied stray punctuation in the WADO-RS metadata-request example (<a href="https://jira.hl7.org/browse/FHIR-54752">FHIR-54752</a>, <a href="https://jira.hl7.org/browse/FHIR-54743">FHIR-54743</a>, <a href="https://jira.hl7.org/browse/FHIR-54770">FHIR-54770</a>, <a href="https://jira.hl7.org/browse/FHIR-54791">FHIR-54791</a>, <a href="https://jira.hl7.org/browse/FHIR-54776">FHIR-54776</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Three candidate tickets dropped from attribution.** Commit `ea174aaf42ba` lists FHIR-54832 ("Spelling mistake — Definition of `ImagingSelection.instance.number`") and FHIR-54810 ("Missing word DICOM" — first sentence of the ImagingSelection section) in its body, but the scoped diff against `source/imagingstudy/**` shows no corresponding hunk; both were applied to the ImagingSelection artifact. They should appear in the ImagingSelection ballot-note draft, not here. The "DERVIED" portion of FHIR-54743 is in the same situation — only the multi-frame ↔ multiframe alignment portion of that ticket reaches ImagingStudy. No commits in the window were unattributed.
- **FHIR-54776 disposition partially applied.** The reporter also asked that "for a specific series" be appended to "construct a WADO-RS metadata request" — that portion of the disposition is *not* in the after-applied state (commits c64cbc8f / 91335996 only addressed the orphan period). Worth flagging during ballot review if the work group still wants the addition.
- **No changes to the StructureDefinition.** Snapshot regeneration is not required for this artifact in this window. All changes are narrative.
- **Existing ballot-note bullets retained.** Both pre-existing bullets in `bn1` are still accurate against the after-applied state, so they were carried forward (with citations and minor wording reinforcement). No bullets were dropped because of revert/supersede.
- **Service health.** `fhir-augury-cli services status` reports GitHub, Jira, and Zulip all healthy at run time; the cache clone HEAD (`db79dcdfe196`) is a descendant of the supplied since-commit (`5d67a34a13a5`), so the simple fast-forward window was used. `gh api` was not needed.

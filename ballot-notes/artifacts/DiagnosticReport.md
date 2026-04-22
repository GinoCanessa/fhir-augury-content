# Artifact Ballot Note Draft: DiagnosticReport (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `DiagnosticReport` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 3 (FHIR-54554, FHIR-55448, FHIR-54163) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (clone HEAD `db79dcdfe196`, briefing analyzed_at 2026-04-20) |
| Generated | 2026-04-22T16:56:42Z |

## Source Files

Files considered part of `DiagnosticReport` for this run, derived from
the FhirCore authoring convention (`source/diagnosticreport/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/diagnosticreport/structuredefinition-DiagnosticReport.xml` | StructureDefinition (canonical) | yes |
| `source/diagnosticreport/diagnosticreport-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/diagnosticreport/diagnosticreport-notes.xml` | Supplementary narrative | no |
| `source/diagnosticreport/diagnosticreport.svg` | UML class diagram | yes |
| `source/diagnosticreport/bundle-DiagnosticReport-search-params.xml` | Search parameters | no |
| `source/diagnosticreport/list-DiagnosticReport-operations.xml` | Operations list | no |
| `source/diagnosticreport/list-DiagnosticReport-examples.xml` | Examples list | no |
| `source/diagnosticreport/list-DiagnosticReport-packs.xml` | Packs list | no |
| `source/diagnosticreport/codesystem-diagnostic-report-status.xml` | Artifact-scoped CodeSystem | no |
| `source/diagnosticreport/codesystem-diagnosticreport-relevant-information-types.xml` | Artifact-scoped CodeSystem | no |
| `source/diagnosticreport/codesystem-diagnosticreport-supportinginfo-type.xml` | Artifact-scoped CodeSystem | no |
| `source/diagnosticreport/valueset-clinical-findings.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/valueset-diagnostic-based-on-snomed.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/valueset-diagnostic-report-status.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/valueset-diagnostic-service-sections.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/valueset-diagnosticreport-relevant-information-types.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/valueset-lipid-ldl-codes.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/valueset-report-codes.xml` | Artifact-scoped ValueSet | no |
| `source/diagnosticreport/diagnosticreport-event-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/diagnosticreport/diagnosticreport-fivews-mapping-exceptions.xml` | Mapping exceptions | no |
| `source/diagnosticreport/diagnosticreport-example*.xml`, `bundle-lipids.xml`, `bundle-lri-example.xml`, `diagnosticreport-micro1.xml`, `diagnosticreport-examples-*.xml` | Examples (~17 files) | no |

Patterns from the FhirCore conventions that produced no match in the
clone:

- `source/diagnosticreport/diagnosticreport-spreadsheet.xml` — no file
  matched (no legacy spreadsheet ships for this resource; the
  StructureDefinition is authoritative).
- Sibling `structuredefinition-*.xml` other than the canonical SD —
  none present.

## Current Ballot Note

The intro file at HEAD contains one `class="ballot-note"` blockquote
plus an unstyled "Release Notes" blockquote that was added inside the
window (see roll-up). Verbatim:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
<p>Addition of the following elements:</p>
<ul>
 <li>DiagnosticReport.relatesTo</li>
 <li>DiagnosticReport.procedure</li>
 <li>DiagnosticReport.recommendation</li>
 <li>DiagnosticReport.communication</li>
 <li>DiagnosticReport.comparison</li>
</ul>
<p>Changes to the following elements:</p>
<ul>
 <li>DiagnosticReport.conclusionCode datatype</li>
</ul>
</blockquote>
<blockquote style="background-color: lightblue">
    <p><b>Release Notes (pending alternative process review with FMG):</b></p>
    <ul>
        <li><a href="https://jira.hl7.org/browse/FHIR-54554">FHIR-54554</a></li>
        <li><a href="https://jira.hl7.org/browse/FHIR-55448">FHIR-55448</a></li>
        <li><a href="https://jira.hl7.org/browse/FHIR-54163">FHIR-54163</a></li>
    </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54163](https://jira.hl7.org/browse/FHIR-54163) | Spelling Error in Element Name: recomendation | [`cac10c581352`](https://github.com/HL7/fhir/commit/cac10c5813521648aeb7f7efad8e3addd591302f), [`f3844943fd7b`](https://github.com/HL7/fhir/commit/f3844943fd7b26db29af72c5a78ea19011fe8d19) |
| [FHIR-54554](https://jira.hl7.org/browse/FHIR-54554) | DiagnosticReport.conclusionCode should be in summary | [`e7e8dd13fb38`](https://github.com/HL7/fhir/commit/e7e8dd13fb38ccdbc51eb604799765795b3fc944), [`49e24e9db46d`](https://github.com/HL7/fhir/commit/49e24e9db46d9ae086f9b554b8f06ee297f50e8e) |
| [FHIR-55448](https://jira.hl7.org/browse/FHIR-55448) | Review need for .media and not .results in the summary | [`c5fca0d6248d`](https://github.com/HL7/fhir/commit/c5fca0d6248df1140e1518106caa1d96335dcf99), [`ea8587ad2535`](https://github.com/HL7/fhir/commit/ea8587ad2535cd4997b0f591184b15ad2394edfd), [`49e24e9db46d`](https://github.com/HL7/fhir/commit/49e24e9db46d9ae086f9b554b8f06ee297f50e8e) |

The three "updated header" commits (`ea8587ad2535`, `f3844943fd7b`,
`49e24e9db46d`) carry no Jira key in their commit message and are not
linked via FhirAugury cross-referenced. They are attributed above by
inspecting their diff content: each one introduces a "Release Notes"
blockquote into the intro that links to exactly one of the three
tickets in the window, and `49e24e9db46d` additionally re-applies the
`isSummary` flag on `DiagnosticReport.conclusion` that FHIR-55448
called for. They are listed alongside the per-ticket commits rather
than as a separate "(unattributed)" group.

## Per-Ticket Detail

### [FHIR-55448](https://jira.hl7.org/browse/FHIR-55448) — Review need for .media and not .results in the summary

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will remove .media from the summary and add .conclusion and .conclusionCode to the summary.

- **Disposition summary:** The work group agreed that `media` does not
  belong in the resource summary view while the report's clinical
  bottom line — `conclusion` (narrative) and `conclusionCode` (coded
  result) — does. The fix is to flip `isSummary` off on the `media`
  backbone and on, on `conclusion` and `conclusionCode`.
- **Commits applying this ticket:**
  - [`c5fca0d6248d`](https://github.com/HL7/fhir/commit/c5fca0d6248df1140e1518106caa1d96335dcf99) — FHIR-55448: Remove .media from summary, add .conclusion and .conclusionCode to summary (2026-02-28)
  - [`ea8587ad2535`](https://github.com/HL7/fhir/commit/ea8587ad2535cd4997b0f591184b15ad2394edfd) — updated header (2026-03-29) — adds the FHIR-55448 line to the intro Release-Notes blockquote
  - [`49e24e9db46d`](https://github.com/HL7/fhir/commit/49e24e9db46d9ae086f9b554b8f06ee297f50e8e) — updated header and summary (2026-03-31) — re-asserts `isSummary` on `DiagnosticReport.conclusion`
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-DiagnosticReport.xml`, `<isSummary value="true"/>`
  is removed from `DiagnosticReport.media` (BackboneElement) and from
  `DiagnosticReport.media.link`, and added to `DiagnosticReport.conclusion`
  (markdown) and to `DiagnosticReport.conclusionCode` (CodeableReference,
  inserted after the `<type>` block, before `<binding>`). Note that the
  `.conclusion` `isSummary` flag was lost between `c5fca0d6248d` and the
  Mar-29/Mar-31 housekeeping commits — `49e24e9db46d` re-applies it, and
  the after-applied state contains it. See "Notes for Reviewer" for an
  unintended duplicate-`isSummary` artifact on `.conclusionCode` that
  results from the overlap with FHIR-54554.

### [FHIR-54554](https://jira.hl7.org/browse/FHIR-54554) — DiagnosticReport.conclusionCode should be in summary

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > We will add both conclusion and conclusionCode as summary elements.

- **Disposition summary:** The originally-requested change was to flag
  only `conclusionCode` as a summary element; the work group expanded
  the scope to also include `conclusion` so the textual and coded
  conclusions travel together in summary projections.
- **Commits applying this ticket:**
  - [`e7e8dd13fb38`](https://github.com/HL7/fhir/commit/e7e8dd13fb38ccdbc51eb604799765795b3fc944) — FHIR-54554: Add isSummary to DiagnosticReport.conclusionCode (2026-03-08)
  - [`49e24e9db46d`](https://github.com/HL7/fhir/commit/49e24e9db46d9ae086f9b554b8f06ee297f50e8e) — updated header and summary (2026-03-31) — adds the FHIR-54554 link to the intro Release-Notes blockquote
- **Changes applied (per Step 5b, scoped to this artifact):**
  `e7e8dd13fb38` adds a single `<isSummary value="true"/>` to
  `DiagnosticReport.conclusionCode`, inserted between the element's
  `<type>` block and its `<binding>`. The companion change of also
  marking `DiagnosticReport.conclusion` as `isSummary` is supplied by
  FHIR-55448's commits (this ticket's resolution explicitly delegates
  the `.conclusion` half to that work). Because FHIR-55448 also adds an
  `isSummary` to `.conclusionCode` (after the `<binding>` block), the
  two tickets together leave a duplicate flag on the same element —
  see the roll-up and Reviewer Notes.

### [FHIR-54163](https://jira.hl7.org/browse/FHIR-54163) — Spelling Error in Element Name: recomendation

- **Work group:** Orders & Observations
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Will fix

- **Disposition summary:** Correct the spelling of the new R6 element
  `DiagnosticReport.recomendation` to `DiagnosticReport.recommendation`
  (and propagate the fix to the rendered class diagram).
- **Commits applying this ticket:**
  - [`cac10c581352`](https://github.com/HL7/fhir/commit/cac10c5813521648aeb7f7efad8e3addd591302f) — FHIR-54163: Fix spelling recomendation → recommendation (2026-03-08)
  - [`f3844943fd7b`](https://github.com/HL7/fhir/commit/f3844943fd7b26db29af72c5a78ea19011fe8d19) — updated header (2026-03-31) — adds the FHIR-54163 link to the intro Release-Notes blockquote
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-DiagnosticReport.xml`, the element id and
  path are renamed from `DiagnosticReport.recomendation` to
  `DiagnosticReport.recommendation` (the element retains its
  `0..* CodeableReference` cardinality and target profile list —
  ServiceRequest, CommunicationRequest, NutritionOrder, CarePlan).
  In `diagnosticreport.svg`, the matching class-diagram label and the
  in-page anchor (`xlink:href` to
  `diagnosticreport-definitions.html#DiagnosticReport.recommendation`)
  are updated to the corrected spelling.

## Roll-up Summary (after-applied state)

Diff base `5d67a34a13a5..db79dcdfe196` over `source/diagnosticreport/`
(15 +, 6 −, 3 files): `diagnosticreport-introduction.xml` (+8),
`diagnosticreport.svg` (±2 label edits),
`structuredefinition-DiagnosticReport.xml` (+5, −4).

- **StructureDefinition (`structuredefinition-DiagnosticReport.xml`):**
  - `DiagnosticReport.recomendation` → `DiagnosticReport.recommendation`
    (element id, path, and SVG anchor renamed; cardinality and
    target-profile list unchanged) — FHIR-54163.
  - `DiagnosticReport.media` (BackboneElement) and
    `DiagnosticReport.media.link` (Reference(DocumentReference)): the
    `<isSummary value="true"/>` flag is removed — FHIR-55448.
  - `DiagnosticReport.conclusion` (markdown) is now `isSummary` —
    FHIR-55448 (with the second commit `49e24e9db46d` reinstating the
    flag after the Mar housekeeping cycle).
  - `DiagnosticReport.conclusionCode` (CodeableReference to
    Observation/Condition, bound to the SNOMED `clinical-findings`
    value set) is now `isSummary` — jointly FHIR-54554 and FHIR-55448.
  - **Snapshot will need to be regenerated** to reflect the renamed
    element and the four `isSummary` flips before publication.
- **Intro / narrative (`diagnosticreport-introduction.xml`):** A new
  unstyled `<blockquote style="background-color: lightblue">` titled
  *Release Notes (pending alternative process review with FMG)* was
  added immediately after the existing `bn1` ballot-note blockquote.
  It lists the three tickets above as bullets pointing at jira.hl7.org.
  No edits were made to the existing `bn1` ballot-note content, the
  Scope-and-Usage prose, or `diagnosticreport-notes.xml`.
- **SVG (`diagnosticreport.svg`):** Class-diagram label and anchor for
  the renamed element updated to `recommendation` — FHIR-54163.
- **Search parameters (`bundle-DiagnosticReport-search-params.xml`):**
  No changes in window.
- **Operations (`list-DiagnosticReport-operations.xml`):** No changes
  in window.
- **Examples:** No example files added, removed, or modified in window;
  no example currently exercises the renamed `.recommendation` element
  or asserts `.media` summary projection, so no example refresh is
  forced by the changes.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes
  in window. The SNOMED `clinical-findings` value set referenced from
  `.conclusionCode` is unchanged.

## Proposed Ballot Note (HTML)

The proposed update keeps the existing `bn1` Normative-readiness
framing intact (those R5→R6 element-set bullets are still accurate at
HEAD) and adds a second ballot note `bn2` covering the changes that
have landed since the previous ballot. The unstyled blue "Release
Notes (pending alternative process review with FMG)" blockquote is
left in place separately; it documents an in-flight process and is
not the ballot-note surface.

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure this resource is ready for Normative status, we are seeking ballot comment on the substantive content. The key changes made since R5 include:</p>
<p>Addition of the following elements:</p>
<ul>
 <li>DiagnosticReport.relatesTo</li>
 <li>DiagnosticReport.procedure</li>
 <li>DiagnosticReport.recommendation</li>
 <li>DiagnosticReport.communication</li>
 <li>DiagnosticReport.comparison</li>
</ul>
<p>Changes to the following elements:</p>
<ul>
 <li>DiagnosticReport.conclusionCode datatype</li>
</ul>
</blockquote>
<blockquote class="ballot-note" id="bn2">
  <p><b>Note to Balloters:</b> Since the previous ballot, the
  StructureDefinition has been adjusted to better reflect the clinical
  intent of the resource summary view and to correct one element name.
  Reviewers are asked to confirm the revised summary projection and
  the renamed element.</p>
  <ul>
    <li>The element previously spelled <code>DiagnosticReport.recomendation</code> has been renamed to <code>DiagnosticReport.recommendation</code>; cardinality (<code>0..*</code>) and the <code>CodeableReference</code> target list (<code>ServiceRequest</code>, <code>CommunicationRequest</code>, <code>NutritionOrder</code>, <code>CarePlan</code>) are unchanged (<a href="https://jira.hl7.org/browse/FHIR-54163">FHIR-54163</a>).</li>
    <li><code>DiagnosticReport.conclusion</code> (markdown) and <code>DiagnosticReport.conclusionCode</code> (<code>CodeableReference</code> bound to the SNOMED <em>clinical-findings</em> value set) are now flagged as summary elements, so the report's clinical bottom line is carried in summary projections (<a href="https://jira.hl7.org/browse/FHIR-54554">FHIR-54554</a>, <a href="https://jira.hl7.org/browse/FHIR-55448">FHIR-55448</a>).</li>
    <li><code>DiagnosticReport.media</code> (and its <code>media.link</code> child) is no longer a summary element; key images and attachments are no longer pulled into summary projections of the report (<a href="https://jira.hl7.org/browse/FHIR-55448">FHIR-55448</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Duplicate `<isSummary value="true"/>` on `DiagnosticReport.conclusionCode`.**
  In the after-applied SD, `.conclusionCode` carries the `isSummary`
  flag twice — once after `<type>`/before `<binding>` (added by
  FHIR-54554, commit `e7e8dd13fb38`) and once after `<binding>` (added
  by FHIR-55448, commit `c5fca0d6248d`). XML parsers will accept this
  but it is almost certainly an unintended artifact of the two tickets
  landing independently. Recommend removing one occurrence before the
  next publication build.
- **`isSummary` on `.conclusion` was lost and re-added.** The original
  FHIR-55448 commit (`c5fca0d6248d`) flipped `isSummary` on for
  `.conclusion`, but the flag is absent from the file at the head of
  the Mar housekeeping cycle and is re-added by `49e24e9db46d`
  ("updated header and summary"). The after-applied state has it on,
  matching the ticket's resolution; no action required, but reviewers
  tracing the per-commit diffs may notice the regression.
- **Existing `bn1` ballot-note content carried forward unchanged.**
  Every R5→R6 bullet currently in `bn1` (added elements `relatesTo`,
  `procedure`, `recommendation`, `communication`, `comparison`; datatype
  change to `conclusionCode`) is still true in the after-applied state,
  so nothing is dropped from `bn1`. The recent rename ensures the
  `recommendation` bullet now reads correctly.
- **The blue "Release Notes (pending alternative process review with FMG)"
  blockquote is a process placeholder, not a ballot note.** It is added
  by the three "updated header" commits and lists the three tickets as
  bare links. It is intentionally left in place by this draft; the
  proposed `bn2` is the substantive balloter-facing summary.
- **Snapshot regeneration required** before publication to reflect
  the renamed `.recommendation` element and the four `isSummary`
  flips in the differential. No snapshot edits were narrated here per
  the skill's "snapshot is derived" rule.
- **Out-of-scope touch points.** No commits in the window touched
  search parameters, operations, examples, or sibling
  ValueSet/CodeSystem files; no cross-repo (UTG, extensions pack) work
  was implied by the diffs.
- **Window integrity.** HEAD (`db79dcdfe196`) is a descendant of the
  since-commit (`5d67a34a13a5`); `git merge-base --is-ancestor`
  succeeded against the cached clone, so the window is a
  fast-forward range and no symmetric-difference fallback was needed.
  All data was sourced from the cached clone via `git` and from
  FhirAugury via `fhir-augury-cli`; `gh` was not required.

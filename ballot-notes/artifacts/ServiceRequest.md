# Artifact Ballot Note Draft: ServiceRequest (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `ServiceRequest` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 2 (FHIR-54618, FHIR-55444) — plus 7 unrelated ticket keys mentioned in one bulk commit but applied to other artifacts |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

Files considered part of `ServiceRequest` for this run (folder
`source/servicerequest/`; folder name lower-case per FhirCore
convention, file stems use the canonical `ServiceRequest` casing):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/servicerequest/structuredefinition-ServiceRequest.xml` | StructureDefinition | yes |
| `source/servicerequest/servicerequest-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/servicerequest/servicerequest-notes.xml` | Supplementary narrative | no |
| `source/servicerequest/bundle-ServiceRequest-search-params.xml` | Search parameters | no |
| `source/servicerequest/list-ServiceRequest-operations.xml` | Operations | no |
| `source/servicerequest/list-ServiceRequest-examples.xml` | Examples list | no |
| `source/servicerequest/list-ServiceRequest-packs.xml` | Packs list | no |
| `source/servicerequest/implementationguide-ServiceRequest-core.xml` | IG manifest | no |
| `source/servicerequest/codesystem-request-orderdetail-parameter-code.xml` | Artifact-scoped CodeSystem | no |
| `source/servicerequest/codesystem-servicerequest-status-reason.xml` | Artifact-scoped CodeSystem | no |
| `source/servicerequest/valueset-request-orderdetail-parameter-code.xml` | Artifact-scoped ValueSet | no |
| `source/servicerequest/valueset-servicerequest-category.xml` | Artifact-scoped ValueSet | no |
| `source/servicerequest/valueset-servicerequest-orderdetail.xml` | Artifact-scoped ValueSet | no |
| `source/servicerequest/valueset-servicerequest-status-reason.xml` | Artifact-scoped ValueSet | no |
| `source/servicerequest/servicerequest-fivews-mapping-exceptions.xml` | FiveWs pattern mapping exceptions | no |
| `source/servicerequest/servicerequest-request-mapping-exceptions.xml` | Request pattern mapping exceptions | yes |
| `source/servicerequest/servicerequest-example-lipid.xml` | Example | yes |
| `source/servicerequest/servicerequest-example*.xml` (24 other examples) | Examples | no |

No briefing-derived file pattern produced a zero-match result for this
artifact.

## Current Ballot Note

No existing `<blockquote class="ballot-note">` was found in
`servicerequest-introduction.xml` at HEAD. The intro currently carries
two non–ballot-note blockquotes that are present for context only:

```html
<blockquote class="stu-note">
  <p><b>Note to Balloters:</b>The new 'servicerequest-specimenSuggestion' extension is expected to be available soon in an upcoming release of the Extensions Pack.</p>
</blockquote>
<blockquote style="background-color: lightblue">
  <p><b>Release Notes (pending alternative process review with FMG):</b></p>
  <ul>
    <li><a href="https://jira.hl7.org/browse/FHIR-55444">FHIR-55444</a></li>
  </ul>
</blockquote>
```

The first is an STU note (announcement of the replacement extension)
and the second is a placeholder release-notes block that the
committers added during this window pending alternative-process review
with FMG. Neither is structured as a `ballot-note`.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-55444](https://jira.hl7.org/browse/FHIR-55444) | Remove deprecated ServiceRequest.specimen | [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661), [`d68b0d377bc6`](https://github.com/HL7/fhir/commit/d68b0d377bc61943bb98962a0aeb03e7a7cef74b), [`11ca31879b4d`](https://github.com/HL7/fhir/commit/11ca31879b4dd7bde60246ecfa8cf901c06535a4), [`5df069a01cb9`](https://github.com/HL7/fhir/commit/5df069a01cb90a0114e462314f1d8c36c13c25e9) |
| [FHIR-54618](https://jira.hl7.org/browse/FHIR-54618) | basedOn Lists DocumentReference Twice | [`4e50e199a609`](https://github.com/HL7/fhir/commit/4e50e199a6097bb3ceb081223c58c1483ea6f890), [`092a94f8214c`](https://github.com/HL7/fhir/commit/092a94f8214cab0b0db22d1532d1b88136a75daa) |

Both window commits without an explicit Jira key (`092a94f8214c`,
`d68b0d377bc6`, `11ca31879b4d`, `5df069a01cb9`) have been attributed
above by inspecting their diffs and the QA/Committer notes on
FHIR-55444 / the duplicate-`DocumentReference` clean-up — none of them
remain unattributed for this artifact. `cross-referenced` returned no
hits for any of those four SHAs, so the attribution rests on diff
content + commit subject + ticket commenter notes.

## Per-Ticket Detail

### [FHIR-55444](https://jira.hl7.org/browse/FHIR-55444) — Remove deprecated ServiceRequest.specimen

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only recorded comments
  > on the ticket are committer notes:
  >
  > > PR: <https://github.com/HL7/fhir/pull/4006> — QA note: see
  > > comment regarding impact this change has to
  > > `servicerequest/servicerequest-example-lipid`.
  > >
  > > Committer note: `servicerequest/servicerequest-example-lipid.xml`
  > > has a contained specimen that is no longer referenced in the
  > > example, which fails the build. This specimen is being removed
  > > as a part of this change but may warrant inclusion elsewhere
  > > through different resources.

- **Disposition summary:** This is a child of FHIR-53722 covering the
  R6 sweep of long-deprecated elements. The applied change removes
  `ServiceRequest.specimen` outright (it has carried `deprecated`
  status across multiple releases and its replacement, the
  `servicerequest-specimenSuggestion` extension on the Extensions
  Pack, is already announced in the STU note). The resolution was
  accepted with modification to also clean up the lipid example and
  publish a release-note placeholder.
- **Commits applying this ticket:**
  - [`f22405098ca5`](https://github.com/HL7/fhir/commit/f22405098ca56696b5de3ef2359acb6e4333a661) — First pass at some R6 ballot tickets (2026-02-20)
  - [`5df069a01cb9`](https://github.com/HL7/fhir/commit/5df069a01cb90a0114e462314f1d8c36c13c25e9) — Update servicerequest-example-lipid.xml (2026-03-06)
  - [`11ca31879b4d`](https://github.com/HL7/fhir/commit/11ca31879b4dd7bde60246ecfa8cf901c06535a4) — Removing specimen from service request example (2026-03-06)
  - [`d68b0d377bc6`](https://github.com/HL7/fhir/commit/d68b0d377bc61943bb98962a0aeb03e7a7cef74b) — Adding placeholder release notes for non-TCs and final cleanup (2026-03-09)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ServiceRequest.xml`, the entire
  `ServiceRequest.specimen` element definition (id, path, short,
  definition, comment, cardinality `0..*`, type
  `Reference(Specimen)`, `isSummary=true`, v2/RIM mappings, and the
  prior `deprecated` standards-status / committee-notes extensions)
  was removed from the differential — 27 deleted lines, no surviving
  bytes. In `servicerequest-example-lipid.xml`, the contained
  `Specimen` resource (`#serum`) and the top-level `<specimen>`
  reference back to it were both removed across the three example
  edits, plus an unrelated whitespace re-flow. In
  `servicerequest-introduction.xml`, a placeholder light-blue
  "Release Notes (pending alternative process review with FMG)"
  blockquote was inserted referencing FHIR-55444. The pre-existing
  `stu-note` pointing implementers at the
  `servicerequest-specimenSuggestion` extension was left untouched and
  remains the recommended replacement.

### [FHIR-54618](https://jira.hl7.org/browse/FHIR-54618) — basedOn Lists DocumentReference Twice

- **Work group:** Orders & Observations
- **Resolution:** Persuasive (Technical Correction)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The only recorded comment
  > is the committer note:
  >
  > > PR: <https://github.com/HL7/fhir/pull/4018>

  The ticket description itself records the agreed action verbatim:
  *"basedOn Lists DocumentReference twice. Remove the duplicate
  DocumentReference entry."*
- **Disposition summary:** Pure technical correction. The
  `ServiceRequest.basedOn` target-profile list contained
  `DocumentReference` twice; the second occurrence is to be removed.
  No semantic change.
- **Commits applying this ticket:**
  - [`4e50e199a609`](https://github.com/HL7/fhir/commit/4e50e199a6097bb3ceb081223c58c1483ea6f890) — FHIR-54618: Remove duplicate DocumentReference from ServiceRequest.basedOn (2026-02-28)
  - [`092a94f8214c`](https://github.com/HL7/fhir/commit/092a94f8214cab0b0db22d1532d1b88136a75daa) — Adding valueset showing only the concepts requested in the ticket (2026-04-09; bulk commit whose only ServiceRequest-scoped hunk synchronizes the request-pattern mapping exceptions file with the new SD)
- **Changes applied (per Step 5b, scoped to this artifact):**
  In `structuredefinition-ServiceRequest.xml`, the duplicate
  `<targetProfile value=".../DocumentReference"/>` entry on
  `ServiceRequest.basedOn` was removed (one line; the surviving
  `DocumentReference` target profile, plus `CarePlan`, `ServiceRequest`,
  `MedicationRequest`, `RequestOrchestration` and `NutritionOrder`
  remain intact). In `servicerequest-request-mapping-exceptions.xml`,
  the mirror entry under `divergentElement
  patternPath="Request.basedOn"` was updated so the
  `extraTypes _resource` Reference list no longer carries the trailing
  duplicate `,DocumentReference` token.

## Roll-up Summary (after-applied state)

Authoritative summary derived from the
`5d67a34a13a5..db79dcdfe196` diff (4 files changed, 7 insertions,
55 deletions).

- **StructureDefinition (`structuredefinition-ServiceRequest.xml`):**
  - `ServiceRequest.basedOn` — removed the duplicate
    `DocumentReference` entry from the `<targetProfile>` list. The
    remaining target profiles (`CarePlan`, `DocumentReference`,
    `ServiceRequest`, `MedicationRequest`, `RequestOrchestration`,
    `NutritionOrder`) are unchanged. `isSummary=true` retained.
    (FHIR-54618).
  - `ServiceRequest.specimen` — element removed entirely from the
    differential. The previous definition was `0..*
    Reference(Specimen)`, summary, with a `standards-status =
    deprecated` extension and committee-notes extension. Implementers
    are directed to the `servicerequest-specimenSuggestion` extension
    on the Extensions Pack (already called out in the existing
    `stu-note`). (FHIR-55444).
  - **Snapshot regeneration is required**; snapshot edits are not
    enumerated here per skill rules.
- **Intro / narrative (`servicerequest-introduction.xml`):**
  - A new light-blue "Release Notes (pending alternative process
    review with FMG)" blockquote was inserted, currently containing
    only a link to FHIR-55444. This is a placeholder block intended
    for FMG review and is not styled as a ballot-note.
  - `servicerequest-notes.xml` is unchanged in window.
- **Search parameters (`bundle-ServiceRequest-search-params.xml`):**
  No changes. (Note: removal of `ServiceRequest.specimen` makes the
  `specimen` search parameter — if any was defined in the
  predecessor — a candidate for review; verify out-of-window or in
  the next pass.)
- **Operations (`list-ServiceRequest-operations.xml`):** No changes.
- **Examples:**
  - `servicerequest-example-lipid.xml` — removed the contained
    `Specimen` (`#serum`) and the top-level `<specimen>` back-reference
    (28 lines net). Required to keep the build green after
    `ServiceRequest.specimen` was removed; the committer note flagged
    that the contained Specimen "may warrant inclusion elsewhere
    through different resources". No other examples were touched.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes
  to ServiceRequest-scoped value sets or code systems. None of the
  in-window ServiceRequest changes appear to belong in UTG (the
  removed element carried no UTG-managed binding).

## Proposed Ballot Note (HTML)

No prior `ballot-note` exists, so this is a fresh `bn1`. The existing
STU note pointing at the replacement `servicerequest-specimenSuggestion`
extension and the placeholder release-notes blockquote should be left
in place as-is; this new ballot-note sits alongside them and frames
the breaking change for balloters.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Two changes have been applied to ServiceRequest since the previous ballot. The substantive change is the removal of the long-deprecated <code>ServiceRequest.specimen</code> element; the second is a technical correction to <code>ServiceRequest.basedOn</code>. Reviewers familiar with R5 should pay particular attention to the <code>specimen</code> removal and to the migration path described below.</p>
  <ul>
    <li>Removed the deprecated <code>ServiceRequest.specimen</code> element (<code>0..* Reference(Specimen)</code>, summary). Implementers that previously populated this element should migrate to the <code>servicerequest-specimenSuggestion</code> extension being published in the Extensions Pack (see the STU note above). The lipid example was updated to drop its contained <code>Specimen</code> and the corresponding back-reference (<a href="https://jira.hl7.org/browse/FHIR-55444">FHIR-55444</a>).</li>
    <li>Technical correction to <code>ServiceRequest.basedOn</code>: removed the duplicate <code>DocumentReference</code> entry from the list of allowed target profiles. The remaining target profiles (<code>CarePlan</code>, <code>DocumentReference</code>, <code>ServiceRequest</code>, <code>MedicationRequest</code>, <code>RequestOrchestration</code>, <code>NutritionOrder</code>) are unchanged, and the request-pattern mapping-exceptions file was synchronized with the new list (<a href="https://jira.hl7.org/browse/FHIR-54618">FHIR-54618</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **No prior ballot-note carry-forward.** The intro file did not
  contain a `ballot-note` blockquote at the since-commit, so no
  bullets were dropped or revised — the proposed note is brand new.
  The pre-existing `stu-note` (replacement-extension announcement) is
  topically related to the `specimen` removal and should remain in
  place; the proposed `ballot-note` complements rather than duplicates
  it.
- **Bulk commit `f22405098ca5` lists eight Jira keys but only one
  affects this artifact.** Only FHIR-55444 produced a hunk inside
  `source/servicerequest/`. The other seven keys mentioned in the
  commit body (FHIR-55372 — Device; FHIR-55271, FHIR-55270, FHIR-55001,
  FHIR-54041, FHIR-54037, FHIR-54034 — Observation/BDP narrative
  fixes) were applied to other artifacts and have been deliberately
  excluded from this report's per-ticket section. They will surface in
  the corresponding `Observation` / `Device` / BDP ballot-note runs.
- **Bulk commit `092a94f8214c` ("Adding valueset…") is a multi-ticket
  commit too;** its only ServiceRequest-scoped hunk synchronises the
  `servicerequest-request-mapping-exceptions.xml` file with the FHIR-54618
  basedOn change. The commit's own subject refers to a value-set
  edit elsewhere in the repo.
- **Snapshot regeneration is required** for
  `structuredefinition-ServiceRequest.xml`; the snapshot is treated as
  derived per skill rules and was not narrated.
- **Release-notes placeholder.** A light-blue "Release Notes (pending
  alternative process review with FMG)" blockquote was added to the
  intro by commit `d68b0d377bc6`. This is a non-ballot-note placeholder
  pending FMG sign-off and was preserved in place; it should not be
  conflated with the proposed ballot-note above.
- **No `gh api` fallback was needed.** All commits and ticket data
  were resolved against the cached clone and the local FhirAugury
  services.
- **HEAD is a descendant of the since-commit** (`git merge-base
  --is-ancestor` returned true), so the simple `since..HEAD` window
  was used; no symmetric-difference fallback applied.

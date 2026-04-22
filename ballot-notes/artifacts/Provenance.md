# Artifact Ballot Note Draft: Provenance (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Provenance` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 2 (FHIR-53917, FHIR-53783) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff` |
| Generated | 2026-04-22T12:05:00Z |

## Source Files

Files considered part of `Provenance` for this run (resolved from the briefing's authoring conventions for FhirCore — `source/<name>/` folder, lowercase `provenance/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/provenance/structuredefinition-Provenance.xml` | StructureDefinition (canonical resource) | no |
| `source/provenance/structuredefinition-profile-provenance-relevant-history.xml` | Sibling profile (relevant history) | no |
| `source/provenance/provenance-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/provenance/provenance-notes.xml` | Supplementary narrative | yes |
| `source/provenance/notes.txt` | Authoring notes | no |
| `source/provenance/profile-provenance-relevant-history-introduction.xml` | Relevant-history profile intro | no |
| `source/provenance/profile-provenance-relevant-history-notes.xml` | Relevant-history profile notes | no |
| `source/provenance/provenance-relevant-history-introduction.xml` | Relevant-history intro (alt) | no |
| `source/provenance/provenance-relevant-history-notes.xml` | Relevant-history notes (alt) | no |
| `source/provenance/bundle-Provenance-search-params.xml` | Search parameters | no |
| `source/provenance/list-Provenance-operations.xml` | Operations | no |
| `source/provenance/list-Provenance-examples.xml` | Examples list | yes |
| `source/provenance/list-Provenance-packs.xml` | Packs list | no |
| `source/provenance/implementationguide-Provenance-core.xml` | IG manifest fragment | no |
| `source/provenance/provenance-event-mapping-exceptions.xml` | Event mapping exceptions | no |
| `source/provenance/provenance-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | yes (net no-op: added then reverted) |
| `source/provenance/provenance-consent-signature.xml` | Consent-signature artifact | no |
| `source/provenance/provenance-examples-header.xml` | Examples header | no |
| `source/provenance/provenance-example-correction-replacement.xml` | Example (correction with replacement) | yes (added) |
| `source/provenance/provenance-example-delete.xml` | Example (delete) | yes |
| `source/provenance/provenance-example.xml`, `provenance-example1..6.xml`, `provenance-example-advanced.xml`, `-anon0.xml`, `-bundle-allergyintolerance.xml`, `-create-consent.xml`, `-diagnosticreport-sig.xml`, `-import.xml`, `-sig.xml` | Examples | no |
| `source/provenance/valueset-provenance-entity-role.xml`, `valueset-provenance-history-agent-type.xml`, `valueset-provenance-history-record-activity.xml` | Artifact-scoped ValueSets (3) | no |
| `source/provenance/codesystem-provenance-entity-role.xml`, `codesystem-w3c-provenance-activity-type.xml` | Artifact-scoped CodeSystems (2) | no |
| `source/provenance/invariant-tests/provenance-example-replace.xml` | Invariant-test example (added) | yes (added) |

No briefing patterns produced empty matches; the legacy `<resource>-spreadsheet.xml` is absent for Provenance (consistent with the briefing's note that the SD is authoritative).

## Current Ballot Note

The current `provenance-introduction.xml` at HEAD already carries a ballot note — it was added during this window by commit `406d76cb` ("added ballot-note for changes since Jan ballot"):

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> To ensure that the Provenance resource is ready for Normative status, we are seeking ballot comments on the substantive content.</p>
<ul>
<li>The key changes made since the January 2026 R6 ballot include:</li>
  <ul>
  <li>More clear how to do Provenance of Replace and Removal. - <a href="https://jira.hl7.org/browse/FHIR-53917">FHIR-53917</a></li>
  <li>Added and example of Provenance of correction (replace) - <a href="https://jira.hl7.org/browse/FHIR-53783">FHIR-53783</a></li>
  </ul>
</ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53917](https://jira.hl7.org/browse/FHIR-53917) | Provenance of removal | [`bb74e6feffed`](https://github.com/HL7/fhir/commit/bb74e6feffedb048c2a7339e6203b7d2201b10fa) |
| [FHIR-53783](https://jira.hl7.org/browse/FHIR-53783) | Need example of Provenance of a correction | [`bb74e6feffed`](https://github.com/HL7/fhir/commit/bb74e6feffedb048c2a7339e6203b7d2201b10fa) |
| (unattributed) | Build hygiene / ballot-note authoring | [`304cab599273`](https://github.com/HL7/fhir/commit/304cab5992734827f2bb23df3b1ee2e4fbbb9368), [`fdd471f0778c`](https://github.com/HL7/fhir/commit/fdd471f0778cc78a73515151fb1bc1ffcc27c116), [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a) |

`fhir-augury-cli cross-referenced` returned zero hits for every commit in the window. Attribution above is derived from commit subjects/bodies and the existing ballot note's own ticket citations: `bb74e6f` names FHIR-53917 in its subject, and the same commit also delivers the correction-with-replacement example called for by FHIR-53783 (the two tickets share PR #4028 and were resolved together by the Security WG on 2026-01-29).

## Per-Ticket Detail

### [FHIR-53917](https://jira.hl7.org/browse/FHIR-53917) — Provenance of removal

- **Work group:** Security
- **Resolution:** Not Persuasive with Modification
- **Disposition (verbatim):**

  > Update header to "Provenance of Removal and Replace"
  >
  > Will update the removal section to indicate that always when a resource is removed it will be indicated on both .target and .entity.what; and add an invariant to assure this is the case (When an .entity.role is removal, the .entity.what is on .target) (point at the invariant)
  >
  > Add new first sentence
  >
  > Provenance.target needs to be inclusive of all create, update, and removal; therefore a replace of a resource needs special handling to indicate the removal state transition.
  >
  > Add the following new paragraph to this section:
  >
  > When replacing a Resource, and it is important to track which Resource replaces the removed Resource, then one Provenance SHOULD be used to indicate this. Where multiple relationships need to be tracked, multiple Provenance SHOULD be used.
  >
  > Update the definition of .target to indicate remove too
  >
  > The Reference(s) that were generated, updated, or removed by the activity described in this resource. A provenance can point to more than one target if multiple resources were created/updated/removed by the same activity.
  >
  > Add two examples: A delete without replace, and a Replace. Point to those examples from this text.

- **Disposition summary:** The Security WG agreed that the existing `removal` guidance was misleading because it left replace‑style removals indistinguishable from plain deletes. Rather than relaxing `Provenance.target` to `0..*`, they kept its cardinality and chose to clarify that a removed resource is always carried on **both** `.target` and `.entity.what` (with `entity.role = removal`), to retitle the section to *Provenance of Removal and Replace*, to add a paragraph describing the single‑Provenance pattern for a replace, and to add an invariant plus two examples (a plain delete and a replace).
- **Commits applying this ticket:**
  - [`bb74e6feffed`](https://github.com/HL7/fhir/commit/bb74e6feffedb048c2a7339e6203b7d2201b10fa) — FHIR-53917 - Provenance of removal (2026-03-09)
- **Changes applied (per Step 5b, scoped to this artifact):**
  - `provenance-notes.xml`: the section heading became *Provenance of Removal and Replace*; the previous single paragraph was rewritten into three paragraphs covering (a) removal recorded with `Provenance.target` referencing the removed resource and `Provenance.entity` indicating the removed resource (linking to `provenance-example-delete.html`), (b) replace recorded as a single Provenance whose `target` points at both the removed and the new resource and whose `entity` indicates the removed resource (linking to `provenance-example-correction-replacement.html`), and (c) a SHOULD that multiple removal/replace actions be split across multiple Provenance resources.
  - `provenance-example-delete.xml`: the existing delete example's `entity.role` was changed from `source` to `removal`, aligning the example with the new guidance.
  - `invariant-tests/provenance-example-replace.xml`: a new invariant‑test example was added that exercises the replace pattern (target referencing both old and new, entity with `role=removal`).
  - **Not applied:** the disposition's "add an invariant" item is **not visible** in `structuredefinition-Provenance.xml` — that file is unchanged in the window. Only the invariant‑test example was added; if the corresponding `<constraint>` on `Provenance.entity` (or `Provenance.target`) is intended to ship with R6 it still needs to be authored on the SD differential. Likewise the `Provenance.target` definition text the disposition asked to extend to "generated, updated, or removed" is **not** present in the SD diff (the SD was not touched) and should be reconciled before publication.

### [FHIR-53783](https://jira.hl7.org/browse/FHIR-53783) — Need example of Provenance of a correction

- **Work group:** Security
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Yes, add an example.

- **Disposition summary:** The Security WG accepted the request to add a worked example showing how a correction (record replacement) should be expressed with Provenance, so that downstream consumers can see that prior data had errors and follow the chain to the corrected resource.
- **Commits applying this ticket:**
  - [`bb74e6feffed`](https://github.com/HL7/fhir/commit/bb74e6feffedb048c2a7339e6203b7d2201b10fa) — FHIR-53917 - Provenance of removal (2026-03-09) — single combined commit; FHIR-53783's deliverable (the correction example) ships in the same change.
  - [`304cab599273`](https://github.com/HL7/fhir/commit/304cab5992734827f2bb23df3b1ee2e4fbbb9368) — clean build (2026-03-09) — registers the new example in `list-Provenance-examples.xml`.
- **Changes applied (per Step 5b, scoped to this artifact):**
  - New file `provenance-example-correction-replacement.xml`: a Provenance instance whose `target` is `Immunization/example`, whose `activity` is `FIXDATA` (v3‑ActReason) with authorization `PATSFTY`, and whose `entity` carries `role=removal` referencing a historical immunization (with an OID identifier and a "Historic Immunization Record with Errors" display). The narrative `why` records the corrective intent.
  - `list-Provenance-examples.xml`: a new entry was appended that titles the example *Provenance for a correction replacement*, with description "Example of using Provenance for a correction replace." Two pre‑existing entries also had the misspellings "De-Identifiation" / "Re-Identificaiton" corrected to "De-Identification" / "Re-Identification".
  - The example is referenced from the new "Replace" paragraph in `provenance-notes.xml` added under FHIR-53917.

### (unattributed) — build hygiene and ballot-note authoring

- **Commits:**
  - [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a) — added ballot-note for changes since Jan ballot (2026-03-10)
  - [`fdd471f0778c`](https://github.com/HL7/fhir/commit/fdd471f0778cc78a73515151fb1bc1ffcc27c116) — updates for build (2026-03-09)
  - [`304cab599273`](https://github.com/HL7/fhir/commit/304cab5992734827f2bb23df3b1ee2e4fbbb9368) — clean build (2026-03-09)
- **Changes applied:**
  - `406d76cb` inserts the current `<blockquote class="ballot-note" id="bn1">…</blockquote>` block at the top of `provenance-introduction.xml`, citing FHIR-53917 and FHIR-53783.
  - `fdd471f0` adds five lines to `provenance-fivews-mapping-exceptions.xml` and tweaks one line of `provenance-notes.xml`; `304cab59` removes the same five lines from `provenance-fivews-mapping-exceptions.xml` (net no-op for that file in the rollup) and registers the new correction-replacement example in `list-Provenance-examples.xml` plus the spelling fixes noted above.

## Roll-up Summary (after-applied state)

Derived from `git diff 5d67a34..HEAD -- source/provenance/`:

- **StructureDefinition (`structuredefinition-Provenance.xml`):** *No changes in the window.* Snapshot regeneration is therefore not required for this artifact. Note that the FHIR-53917 disposition asked for an `entity.role = removal ⇒ entity.what is in .target` invariant on the SD and for an updated definition on `Provenance.target`; neither is visible here yet.
- **Intro / narrative (`provenance-introduction.xml`, `provenance-notes.xml`):**
  - Added a ballot note at the top of the intro pointing reviewers at the post-January-2026 changes (ids: FHIR-53917, FHIR-53783).
  - Renamed the *Provenance of Removal* section to *Provenance of Removal and Replace*.
  - Replaced the prior single paragraph with three: removal is now described as recorded on both `Provenance.target` (the removed resource) and `Provenance.entity` (with `entity.role = removal`); replace is described as a single Provenance whose `target` references both the removed and the new resource; and multiple removal/replace actions SHOULD be split across multiple Provenance resources. Both descriptions link to worked examples.
- **Search parameters (`bundle-Provenance-search-params.xml`):** No changes.
- **Operations (`list-Provenance-operations.xml`):** No changes.
- **Examples:**
  - **Added** `provenance-example-correction-replacement.xml` (registered in `list-Provenance-examples.xml`) — the worked example FHIR-53783 asked for, also serving as the *replace* example FHIR-53917 asked for.
  - **Updated** `provenance-example-delete.xml`: `entity.role` changed from `source` → `removal`, aligning the canonical delete example with the new guidance.
  - **Spelling fixes** in `list-Provenance-examples.xml` for the *De-Identification / Re-Identification* anonymisation example (description and display).
  - **Added invariant test** `invariant-tests/provenance-example-replace.xml` exercising the replace pattern.
- **Mapping exceptions (`provenance-fivews-mapping-exceptions.xml`):** Net no-op in the rollup (5 lines added in `fdd471f0`, removed in `304cab59`).
- **Terminology (sibling `valueset-*` / `codesystem-*`):** No changes. No new terminology was introduced; the `entity.role = removal` code already exists in the existing `valueset-provenance-entity-role.xml` / `codesystem-provenance-entity-role.xml`. No cross-repo (UTG) impact arising from this window.

## Proposed Ballot Note (HTML)

The existing `bn1` block already covers both attributed tickets. The revision below preserves the existing `id`, keeps both bullets, but tightens the wording so balloters can see at a glance what the after-applied state actually changed (the rewritten *Removal and Replace* narrative and the new worked example), and adds a one-line caveat noting that the SD-level invariant the disposition called for has not yet landed — reviewers should comment if they expect to see it on the SD before normative ballot close.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Provenance is being put forward for Normative status.
  We are seeking ballot comments on the substantive changes made since the
  January 2026 R6 ballot, which clarify how Provenance is used to record
  removal and replace.</p>
  <ul>
    <li>The "Provenance of Removal" section has been retitled
    <i>Provenance of Removal and Replace</i> and rewritten to require that a
    removed resource is carried on both <code>Provenance.target</code> and
    <code>Provenance.entity</code> (with <code>entity.role = removal</code>),
    and to describe replace as a single Provenance whose <code>target</code>
    references both the removed and the replacement resource
    (<a href="https://jira.hl7.org/browse/FHIR-53917">FHIR-53917</a>).</li>
    <li>The canonical delete example (<a href="provenance-example-delete.html">provenance-example-delete</a>)
    has been aligned with this guidance — its <code>entity.role</code> is now
    <code>removal</code>
    (<a href="https://jira.hl7.org/browse/FHIR-53917">FHIR-53917</a>).</li>
    <li>A new worked example,
    <a href="provenance-example-correction-replacement.html">provenance-example-correction-replacement</a>,
    has been added showing how a correction that replaces a historic
    Immunization is expressed
    (<a href="https://jira.hl7.org/browse/FHIR-53783">FHIR-53783</a>,
    <a href="https://jira.hl7.org/browse/FHIR-53917">FHIR-53917</a>).</li>
    <li>The StructureDefinition itself has not changed in this cycle. The
    FHIR-53917 disposition called for an invariant ensuring that when
    <code>entity.role = removal</code> the <code>entity.what</code> reference
    also appears in <code>target</code>, and for an extension of the
    <code>Provenance.target</code> definition to mention "removed". Reviewers
    should comment if they expect either change to land on the
    StructureDefinition before this ballot closes
    (<a href="https://jira.hl7.org/browse/FHIR-53917">FHIR-53917</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **CLI cross-references returned no hits** for any of the four commits (`fhir-augury-cli cross-referenced` reported `total: 0` for each). Ticket attribution was therefore reconstructed from the commit subject (`bb74e6f` names FHIR-53917) and from the in-tree ballot note added by `406d76cb`, which itself cites both FHIR-53917 and FHIR-53783. Both tickets share PR #4028 (per the Jira comments) and were resolved together by the Security WG on 2026-01-29, which is consistent with the single combined implementation commit observed here.
- **Disposition vs. after-applied gap on FHIR-53917.** The disposition explicitly asks for (a) a new invariant on the SD ensuring `entity.role = removal ⇒ entity.what ∈ target`, and (b) a rewording of the `Provenance.target` definition to mention "removed". `structuredefinition-Provenance.xml` is **untouched** in this window, so neither has been applied to the SD itself; only an invariant‑test example was added. The proposed ballot note flags this as a balloter‑visible gap rather than silently asserting that the work is complete.
- **`provenance-fivews-mapping-exceptions.xml`** appears in commits `fdd471f0` and `304cab59` but the rollup diff is empty (added then removed). It is listed in the source-files table for completeness but does not appear in the roll-up summary.
- The window is a clean ancestor range: HEAD (`db79dcdfe196`) is a descendant of `5d67a34a13a5`. No `gh api` fallback was needed — all data came from the cached clone and from `fhir-augury-cli`.

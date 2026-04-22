# Artifact Ballot Note Draft: MeasureReport (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `MeasureReport` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 6 |
| Tickets attributed | 4 (FHIR-51028, FHIR-55082, FHIR-55083, FHIR-55366) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T20:00:00Z |

## Source Files

Files considered part of `MeasureReport` for this run (folder `source/measurereport/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/measurereport/structuredefinition-MeasureReport.xml` | StructureDefinition (canonical) | yes |
| `source/measurereport/measurereport-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/measurereport/measurereport-notes.xml` | Supplementary narrative | no |
| `source/measurereport/bundle-MeasureReport-search-params.xml` | Search parameters | no |
| `source/measurereport/list-MeasureReport-operations.xml` | Operations | no |
| `source/measurereport/list-MeasureReport-examples.xml` | Examples list | no |
| `source/measurereport/list-MeasureReport-packs.xml` | Packs | no |
| `source/measurereport/measurereport-example.xml`, `measurereport-cms146-cat{1,2,3}-example.xml`, `measurereport-788ca455-e11b1a59.xml`, `measurereport-general-example.xml`, `measurereport-hiv-indicators.xml`, `measurereport-examples-header.xml` | Examples | no |
| `source/measurereport/measurereport-fivews-mapping-exceptions.xml` | FiveWs mapping exceptions | no |
| `source/measurereport/valueset-measure-report-status.xml` | Artifact-scoped ValueSet | no |
| `source/measurereport/valueset-measure-report-type.xml` | Artifact-scoped ValueSet | no |
| `source/measurereport/valueset-measurereport-stratifier-value-example.xml` | Artifact-scoped ValueSet | no |
| `source/measurereport/valueset-submit-data-update-type.xml` | Artifact-scoped ValueSet | no |
| `source/measurereport/codesystem-measure-report-status.xml` | Artifact-scoped CodeSystem | no |
| `source/measurereport/codesystem-measure-report-type.xml` | Artifact-scoped CodeSystem | yes |
| `source/measurereport/codesystem-measurereport-stratifier-value-example.xml` | Artifact-scoped CodeSystem | no |
| `source/measurereport/codesystem-submit-data-update-type.xml` | Artifact-scoped CodeSystem | no |
| `source/measurereport/measurereport.svg` | Generated UML diagram (derived) | yes |
| `source/measurereport/invariant-tests/` | Invariant tests | no |

No legacy `measurereport-spreadsheet.xml` exists; the StructureDefinition is authoritative.
No sibling `structuredefinition-*.xml` profiles ship alongside MeasureReport.

## Current Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> Key changes made since FHIR 6.0.0-ballot4:</p>
    <ul>
        <li>Non-compatible Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-51028">FHIR-51028</a>: Clarified examples are experimental content</li>
            </ul>
        </li>
        <li>Compatible, Substantive Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55083">FHIR-55083</a>: Relaxed .type to 0..1 and added 'other' to .type allowable concepts.</li>
            </ul>
        </li>
        <li>Non-substantive Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55081">FHIR-55081</a>: Potentially re-useable THO-candidate value sets in resource MeasureReport</li>
            </ul>
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55082">FHIR-55082</a>: MeasureReport.status has no escape valve</li>
            </ul>
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55366">FHIR-55366</a>: Removed isModifier from .scoring, .dataUpdateType, and .improvementNotation</li>
            </ul>
        </li>
    </ul>
    <p></p>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-51028](https://jira.hl7.org/browse/FHIR-51028) | Change measure-stratifier code system and value set to a non-example | [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) |
| [FHIR-55083](https://jira.hl7.org/browse/FHIR-55083) | MeasureReport.type has no escape valve | [`2d1475b12988`](https://github.com/HL7/fhir/commit/2d1475b1298876cb2263a07d5e207dae3b2edfd1) |
| [FHIR-55082](https://jira.hl7.org/browse/FHIR-55082) | MeasureReport.status has no escape valve | [`93a23bcac743`](https://github.com/HL7/fhir/commit/93a23bcac743eee6cede1a4ffabc60c8594d791e) |
| [FHIR-55366](https://jira.hl7.org/browse/FHIR-55366) | Why is scoring a modifier | [`ddb69d6546fc`](https://github.com/HL7/fhir/commit/ddb69d6546fc083ea053d6483c86ac8a6b0d4643) |
| (unattributed) | Ballot-note narrative scaffolding (PR cleanup) | [`f43fbf565a77`](https://github.com/HL7/fhir/commit/f43fbf565a77bf872216d73bce2ef961e739462c), [`c83599e70004`](https://github.com/HL7/fhir/commit/c83599e70004bfd658b51ef62426524eb948df6c) |

## Per-Ticket Detail

### [FHIR-51028](https://jira.hl7.org/browse/FHIR-51028) — Change measure-stratifier code system and value set to a non-example

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The applied-vote comment was not present; the closest comment is a reviewer note ("11/19 Matthew Tiller to review proposed disposition"). Per the discussion comments, the WG concluded that the example stratifier code system / value set in core would be renamed to align with the Quality Measures IG `measure-stratifier-type` example (the canonical content lives in QM IG / UV-CQM and is targeted for THO once mature; until then the core copy is renamed to make its alignment explicit while keeping it labelled `example`).

- **Disposition summary:** TSMG (2025-06-02) restricted use of `example` code systems in core / THO. For MeasureReport's stratifier value, the WG could not move the canonical to THO yet (it lives in UV/CQM), so the core artifact was renamed from `MeasureStratifierExample` to `MeasureStratifierTypeExample` and the example binding was repointed to `http://hl7.org/fhir/ValueSet/measure-stratifier-type-example` to match the QM-IG naming.
- **Commits applying this ticket:**
  - [`18df653fdc32`](https://github.com/HL7/fhir/commit/18df653fdc321d3e20a95d14638e59a6d41168d7) — `[FHIR-51028]: Change measure-stratifier code system and value set to a non-example.` (2026-04-15)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-MeasureReport.xml`, the example binding on `MeasureReport.group.stratifier.code` and `MeasureReport.group.stratifier.stratum.component.code` was renamed: `bindingName` `MeasureStratifierExample` → `MeasureStratifierTypeExample` and `valueSet` `…/measure-stratifier-example` → `…/measure-stratifier-type-example`. The same rename is reflected in the regenerated `measurereport.svg`. Note that the existing ballot-note bullet ("Clarified examples are experimental content") is a thematic summary of the TSMG-driven cleanup; the concrete change in this artifact is the binding URL/name rename, not a textual experimental-content notice.

### [FHIR-55083](https://jira.hl7.org/browse/FHIR-55083) — MeasureReport.type has no escape valve

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. From the discussion: "Having 'other' + extension is a possible solution. … The base question is there any possibility of legacy or new instances that need to be exposed where a system might not know …". The applied resolution was to relax cardinality and add an `other` code with extension guidance.

- **Disposition summary:** A generic QA review flagged that `MeasureReport.type` had no escape value. The WG agreed to add an `other` code (with guidance to use an extension to qualify the actual type) and, in the same ticket, relaxed the cardinality of `.type` from `1..1` to `0..1`.
- **Commits applying this ticket:**
  - [`2d1475b12988`](https://github.com/HL7/fhir/commit/2d1475b1298876cb2263a07d5e207dae3b2edfd1) — `[FHIR-55083]: MeasureReport.type has no escape valve. Added 'other' to MeasureReport Type CodeSystem` (2026-04-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In `codesystem-measure-report-type.xml`, a new `other` concept was appended (display "Other"; definition explains it is for known-but-not-enumerated types). In `structuredefinition-MeasureReport.xml`, `MeasureReport.type.short` gained `| other`, the `definition` was extended to describe when (and when not) to use `other` and to require an accompanying extension, and `min` changed from `1` to `0`. Snapshot regeneration is required.

### [FHIR-55082](https://jira.hl7.org/browse/FHIR-55082) — MeasureReport.status has no escape valve

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. From the discussion: "If the work group believes that proper solution is to treat 'don't know' as 'not done', that's fair. A reasonable resolution would be to add that guidance to the spec." The applied resolution adds the suggested guidance rather than introducing a new status code.

- **Disposition summary:** The WG concluded that no new status code (e.g., `unknown` / `other`) was needed; instead the `status` definition was clarified to direct systems that do not know the status to use `error` with an explanatory message, and to clarify what `pending` implies.
- **Commits applying this ticket:**
  - [`93a23bcac743`](https://github.com/HL7/fhir/commit/93a23bcac743eee6cede1a4ffabc60c8594d791e) — `[FHIR-55082]: MeasureReport.status has no escape valve` (2026-04-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-MeasureReport.xml`, `MeasureReport.status.definition` was extended with two clarifying sentences: that `pending` means in-progress and is expected to resolve to either complete or error, and that systems that do not know the status should use `status = "error"` with an explanatory message. No code was added to `valueset-measure-report-status.xml` / `codesystem-measure-report-status.xml`. The existing ballot-note bullet ("MeasureReport.status has no escape valve") restates the ticket title rather than the applied resolution; consider rewording (see proposed note below).

### [FHIR-55366](https://jira.hl7.org/browse/FHIR-55366) — Why is scoring a modifier

- **Work group:** Clinical Quality Information
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The latest tracked comment ("2/25/26 subgroup call – Bryn has confirmed with submitter that proposed resolution is acceptable.") confirms acceptance. Per discussion: `scoring`, `improvementNotation` and `dataUpdateType` were re-evaluated against the `isModifier` test and found not to qualify ("ignoring this does not cause an incorrect interpretation of the instance"); they were flipped to `isModifier=false` while keeping the existing `isModifierReason` text.

- **Disposition summary:** Confirm that `scoring`, `improvementNotation`, and `dataUpdateType` do not meet the `isModifier` definition (ignoring them does not cause incorrect interpretation of the instance) and remove the modifier flag from all three.
- **Commits applying this ticket:**
  - [`ddb69d6546fc`](https://github.com/HL7/fhir/commit/ddb69d6546fc083ea053d6483c86ac8a6b0d4643) — `[FHIR-55366]: Removed isModifier flags on 3 elements as described` (2026-04-17)
- **Changes applied (per Step 5b, scoped to this artifact):** In `structuredefinition-MeasureReport.xml`, `<isModifier>` flipped from `true` to `false` on `MeasureReport.dataUpdateType`, `MeasureReport.scoring`, and `MeasureReport.improvementNotation`. The existing `<isModifierReason>` strings were retained (now stale relative to `isModifier=false`); reviewers may wish to remove or revise them as a follow-up. Snapshot regeneration is required.

### (unattributed) — Ballot-note narrative scaffolding

- **Commits:**
  - [`f43fbf565a77`](https://github.com/HL7/fhir/commit/f43fbf565a77bf872216d73bce2ef961e739462c) — `Adding update note to Measure and MeasureReport per PR request` (2026-04-16)
  - [`c83599e70004`](https://github.com/HL7/fhir/commit/c83599e70004bfd658b51ef62426524eb948df6c) — `Updating Measure and MeasureReport introduction notes` (2026-04-17)
- **Changes applied:** `f43fbf56` introduced the `<blockquote class="ballot-note" id="bn1">…</blockquote>` scaffold in `measurereport-introduction.xml` (with `FHIR-51028` already populated as the only listed change and "None" placeholders in the other categories). `c83599e7` filled in the remaining bullets for FHIR-55083 (Compatible, Substantive) and FHIR-55081, FHIR-55082, FHIR-55366 (Non-substantive); it also tweaked the `MeasureReport.type` `short` text in the SD to add `| other` (consistent with the FHIR-55083 commit landed earlier the same day; this is editorial/duplicate alignment). No `cross-referenced` results were returned for either commit; both are treated as PR-cleanup commits associated primarily with FHIR-51028 (whose PR was [#4050](https://github.com/HL7/fhir/pull/4050) per the FHIR-51028 Jira comments). Note that **FHIR-55081** is referenced in the existing ballot note but no commit in this window mentions it and no source file under `source/measurereport/` was touched on its behalf — see "Notes for Reviewer".

## Roll-up Summary (after-applied state)

Net change across `5d67a34a13a5..db79dcdfe196`, scoped to `source/measurereport/`:

- **StructureDefinition (`structuredefinition-MeasureReport.xml`):**
  - `MeasureReport.status.definition` extended with clarifying guidance: `pending` is in-progress and expected to resolve to complete/error; systems that do not know the status SHOULD use `status = "error"` with an explanatory message (FHIR-55082).
  - `MeasureReport.type.short` adds `| other`; `definition` extended to describe `other` semantics ("known but not one of the enumerated report types") and to require an accompanying extension when `other` is used; `min` cardinality relaxed `1` → `0` (FHIR-55083).
  - `MeasureReport.dataUpdateType.isModifier` flipped `true` → `false` (FHIR-55366). Existing `isModifierReason` text retained.
  - `MeasureReport.scoring.isModifier` flipped `true` → `false` (FHIR-55366). Existing `isModifierReason` text retained.
  - `MeasureReport.improvementNotation.isModifier` flipped `true` → `false` (FHIR-55366). Existing `isModifierReason` text retained.
  - `MeasureReport.group.stratifier.code` and `MeasureReport.group.stratifier.stratum.component.code` example bindings renamed: `bindingName` `MeasureStratifierExample` → `MeasureStratifierTypeExample`; `valueSet` `http://hl7.org/fhir/ValueSet/measure-stratifier-example` → `http://hl7.org/fhir/ValueSet/measure-stratifier-type-example` (FHIR-51028).
  - Snapshot regeneration required (no narrative `<snapshot>` edits enumerated here per skill rules).

- **Intro / narrative (`measurereport-introduction.xml`):**
  - New `<blockquote class="ballot-note" id="bn1">` block introduced inside a wrapping `<div>` summarising changes since FHIR 6.0.0-ballot4. Bullets: FHIR-51028 (Non-compatible), FHIR-55083 (Compatible, Substantive), and FHIR-55081 / FHIR-55082 / FHIR-55366 (Non-substantive). A second `<blockquote style="background-color: lightblue">` "All Changes" placeholder block lists "None".

- **Search parameters (`bundle-MeasureReport-search-params.xml`):** No changes.

- **Operations (`list-MeasureReport-operations.xml`):** No changes.

- **Examples:** No example files added or removed; no example payloads updated. The renamed stratifier example value set URL is not referenced from any of the bundled `measurereport-*-example.xml` files in the window.

- **Terminology (sibling artifacts):**
  - `codesystem-measure-report-type.xml` — added `other` concept (display "Other"; definition allows for known-but-not-enumerated report types) (FHIR-55083).
  - `valueset-measure-report-type.xml` — unchanged content; the new `other` code is included via the value set's CodeSystem reference and will appear after expansion regeneration.
  - `valueset-measurereport-stratifier-value-example.xml` / `codesystem-measurereport-stratifier-value-example.xml` — unchanged in this window; the rename in FHIR-51028 was applied at the SD's binding URL level (the renamed canonical `measure-stratifier-type-example` itself is expected to be re-homed under `source/codesystems/` or similar — confirm at next briefing refresh; at HEAD here it does not yet exist as a file in `source/measurereport/`).
  - No new value sets or code systems were added in this folder; FHIR-55081 (referenced in the existing ballot note as "Potentially re-useable THO-candidate value sets") did not produce any file change in `source/measurereport/` within this window — its work, if applied, is in another folder (likely UTG / `source/codesystems/`).
  - `measurereport.svg` regenerated to reflect the FHIR-51028 binding rename (derived artifact; no narrative impact).

## Proposed Ballot Note (HTML)

```html
<blockquote class="ballot-note" id="bn1">
    <p><b>Note to Balloters:</b> Key changes made to MeasureReport since FHIR 6.0.0-ballot4:</p>
    <ul>
        <li>Non-compatible Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-51028">FHIR-51028</a>: Renamed the example stratifier binding to align with the Quality Measures IG &mdash; <code>MeasureReport.group.stratifier.code</code> and <code>.stratum.component.code</code> now bind (example) to <code>http://hl7.org/fhir/ValueSet/measure-stratifier-type-example</code> (was <code>measure-stratifier-example</code>). Implementations that referenced the prior URL must update.</li>
            </ul>
        </li>
        <li>Compatible, Substantive Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55083">FHIR-55083</a>: Relaxed <code>MeasureReport.type</code> cardinality from <code>1..1</code> to <code>0..1</code> and added an <code>other</code> concept to the MeasureReportType code system (with guidance that an extension SHOULD accompany <code>other</code> to convey the actual type).</li>
                <li><a href="https://jira.hl7.org/browse/FHIR-55366">FHIR-55366</a>: Removed the <code>isModifier</code> flag from <code>MeasureReport.scoring</code>, <code>MeasureReport.dataUpdateType</code>, and <code>MeasureReport.improvementNotation</code>. These elements remain summary-level but ignoring them does not cause an incorrect interpretation of the instance.</li>
            </ul>
        </li>
        <li>Non-substantive Changes
            <ul>
                <li><a href="https://jira.hl7.org/browse/FHIR-55082">FHIR-55082</a>: Clarified the definition of <code>MeasureReport.status</code> &mdash; <code>pending</code> means the report is in progress (expected to resolve to <code>complete</code> or <code>error</code>); systems that do not know the report status SHOULD use <code>status = "error"</code> with an explanatory message rather than guess.</li>
                <li><a href="https://jira.hl7.org/browse/FHIR-55081">FHIR-55081</a>: Identified MeasureReport-scoped value sets as candidates for promotion to THO (no in-resource changes within this window).</li>
            </ul>
        </li>
    </ul>
</blockquote>
```

## Notes for Reviewer

- **FHIR-55081 has no commits in this window touching `source/measurereport/`.** It is listed in the existing ballot note (under "Non-substantive Changes") and has been retained in the proposed note, but reviewers should verify that the THO-candidate work has been (or will be) tracked in another folder (likely UTG / `source/codesystems/`) before final ballot publication. If the work has been deferred or applied entirely outside MeasureReport's source folder, consider whether it still belongs in this artifact's ballot note.
- **FHIR-51028 ballot bullet rewording.** The existing bullet ("Clarified examples are experimental content") describes the cross-cutting TSMG initiative behind the change; the actual change applied to MeasureReport is a binding URL/name rename. The proposed note rewords this to spell out the rename so balloters can audit downstream impact. This is reflected as a Non-compatible change because the example value set canonical URL changed.
- **FHIR-55082 ballot bullet rewording.** The existing bullet restated the ticket title ("MeasureReport.status has no escape valve"), which is misleading because no escape code was added. The proposed note describes the clarifying definition guidance that was actually applied.
- **`isModifierReason` text was retained on the three elements flipped to `isModifier=false` (FHIR-55366).** This is now stale — the reasons describe why the elements *were* modifiers. A small editorial follow-up to remove or rephrase those `isModifierReason` strings may be appropriate before publication; flagged for the work group rather than auto-applied here.
- **Briefing currency.** The cached briefing's `clone_head_sha` is `1b369ff4e28e` while the clone's actual HEAD at run time is `db79dcdfe196`. The briefing is slightly behind HEAD but the artifact-map / authoring layout for `source/measurereport/` is unaffected by intervening commits, so the file resolution above is sound. Refresh `repo-analysis` if a strictly current briefing is required.
- **Cross-reference index returned no Jira hits for the two "ballot-note scaffolding" commits** (`f43fbf56`, `c83599e7`). They are treated as PR-cleanup work for FHIR-51028's PR (#4050, per FHIR-51028 Jira comments) and are noted under "(unattributed)".
- **`measurereport.svg` was regenerated** by the FHIR-51028 commit. It is a derived artifact; no narrative content depends on it directly in the intro file.

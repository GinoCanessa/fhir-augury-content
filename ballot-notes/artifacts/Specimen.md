# Artifact Ballot Note Draft: Specimen (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Specimen` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 3 |
| Tickets attributed | 1 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

> **Briefing note:** The cached briefing was generated against clone HEAD `1b369ff4e28e`; the current clone HEAD is `db79dcdfe196`. The Specimen artifact layout has not changed between those revisions, so the briefing's Artifact Map remains applicable for this run.

## Source Files

Files considered part of `Specimen` for this run (resolved against the briefing's Artifact Map and the conventional FhirCore patterns under `source/specimen/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/specimen/structuredefinition-Specimen.xml` | StructureDefinition (canonical) | yes |
| `source/specimen/specimen-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/specimen/specimen-notes.xml` | Supplementary narrative | no |
| `source/specimen/bundle-Specimen-search-params.xml` | Search parameters bundle | yes (added & reverted in window) |
| `source/specimen/list-Specimen-operations.xml` | Operations list | no |
| `source/specimen/list-Specimen-examples.xml` | Examples list | no |
| `source/specimen/list-Specimen-packs.xml` | Resource pack list | no |
| `source/specimen/specimen-examples-header.xml` | Examples header | no |
| `source/specimen/specimen-example.xml` | Example | no |
| `source/specimen/specimen-example-isolate.xml` | Example | no |
| `source/specimen/specimen-example-liver-biopsy.xml` | Example | no |
| `source/specimen/specimen-example-pooled-serum.xml` | Example | no |
| `source/specimen/specimen-example-serum-control.xml` | Example | no |
| `source/specimen/specimen-example-serum.xml` | Example | no |
| `source/specimen/specimen-example-urine.xml` | Example | no |
| `source/specimen/specimen-extensions-spreadsheet.xml` | Legacy spreadsheet (SD is authoritative) | no |
| `source/specimen/specimen-fivews-mapping-exceptions.xml` | 5Ws mapping exceptions | no |
| `source/specimen/implementationguide-Specimen-core.xml` | IG manifest | no |
| `source/specimen/codesystem-specimen-combined.xml` | Artifact-scoped CodeSystem | no |
| `source/specimen/codesystem-specimen-role.xml` | Artifact-scoped CodeSystem | no |
| `source/specimen/codesystem-specimen-status.xml` | Artifact-scoped CodeSystem | no |
| `source/specimen/valueset-containerdevice-code.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-hierarchical-relationship-type.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-processingdevice-code.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-collection-method.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-combined.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-container-type.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-processing-method.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-role.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-status.xml` | Artifact-scoped ValueSet | no |
| `source/specimen/valueset-specimen-type.xml` | Artifact-scoped ValueSet | no |

## Current Ballot Note

No existing `<blockquote class="ballot-note">` is present at HEAD. The intro file does carry an interim release-notes blockquote (using `style="background-color: lightblue"` rather than `class="ballot-note"`) added by commit [`810b9abd0f2c`](https://github.com/HL7/fhir/commit/810b9abd0f2c67f3d498cbe2f538cb61479688a2):

```html
<blockquote style="background-color: lightblue">
    <p><b>Release Notes (pending alternative process review with FMG):</b></p>
    <ul>
        <li><a href="https://jira.hl7.org/browse/FHIR-53384">FHIR-53384</a></li>
    </ul>
</blockquote>
```

This is a stub (a bare ticket link, no narrative). The proposed ballot note below is intended to replace it (or sit alongside it inside a properly classed `<blockquote class="ballot-note" id="bn1">` wrapper), so balloters get a substantive description rather than just a Jira link.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-53384](https://jira.hl7.org/browse/FHIR-53384) | Add Specimen.focus (CodeableReference) to represent the entity that is the focus of testing | [`7b25639a0330`](https://github.com/HL7/fhir/commit/7b25639a03303a2b75b2c7117d2fc9f24be94335), [`1764e013bfe9`](https://github.com/HL7/fhir/commit/1764e013bfe972d03cbc1aac2bbdf5d43e4d6a92), [`810b9abd0f2c`](https://github.com/HL7/fhir/commit/810b9abd0f2c67f3d498cbe2f538cb61479688a2) |

All three commits in the window are attributable to FHIR-53384: the first commit implements the originally-proposed `Specimen.focus` element, the second commit ("updated references") rolls the implementation back to the workgroup's actual disposition (RelatedPerson on `Specimen.subject` plus a new `comment`), and the third commit registers the ticket in the interim release-notes blockquote on the intro page. None of the commits matched any cross-references via `fhir-augury-cli cross-referenced`; ticket attribution is from the `FHIR-53384` token in the `7b25639a` commit message, with the other two commits attributed by content (they touch the same lines and the commit window contains no other ticket work).

## Per-Ticket Detail

### [FHIR-53384](https://jira.hl7.org/browse/FHIR-53384) — Add Specimen.focus (CodeableReference) to represent the entity that is the focus of testing

- **Work group:** Orders & Observations
- **Resolution:** Persuasive with Modification (status: Applied; resolved 2026-02-02)
- **Disposition (verbatim):**

  > **Motion to** allow referencing RelatedPerson from Specimen.subject  - Riki Merrick, Rik Smithies, no further discussion, 5-1-1
  >
  > recorded this one below, but we also had additonal motion:
  >
  > **Motion to** add the this text: "When the specimen is not from the record subject, the RelatedPerson can be used for specimens from other entities, either from humans or animals."
  >
  > as the Comments text on Specimen.subject.  Rik Smithies, Ralf Herzog, no further discussion, 4-0-0

- **Disposition summary:** O&O voted *not* to introduce a new `Specimen.focus` element as originally proposed. Instead, two narrowly-scoped modifications were approved: (1) add `RelatedPerson` to the list of permitted target profiles on the existing `Specimen.subject` reference, and (2) add a comment on `Specimen.subject` explaining that `RelatedPerson` is the mechanism for representing specimens taken from an entity other than the record subject (including humans or animals). A separate concern raised by Lloyd — that patient-specific resources should always carry a direct reference to `Patient` — was deferred to follow-up ticket [FHIR-56301](https://jira.hl7.org/browse/FHIR-56301).
- **Commits applying this ticket:**
  - [`7b25639a0330`](https://github.com/HL7/fhir/commit/7b25639a03303a2b75b2c7117d2fc9f24be94335) — FHIR-53384: Add Specimen.focus CodeableReference element (2026-03-08)
  - [`1764e013bfe9`](https://github.com/HL7/fhir/commit/1764e013bfe972d03cbc1aac2bbdf5d43e4d6a92) — updated references (2026-03-31)
  - [`810b9abd0f2c`](https://github.com/HL7/fhir/commit/810b9abd0f2c67f3d498cbe2f538cb61479688a2) — update release notes (2026-03-27)
- **Changes applied (per Step 5b, scoped to this artifact):** Commit `7b25639a` initially implemented the *original* proposal: it added a new `Specimen.focus` element (`0..* CodeableReference` targeting Group / Device / Substance / Location / RelatedPerson / BiologicallyDerivedProduct) to `structuredefinition-Specimen.xml` (+22 lines) and corresponding `focus` and `focus-code` search parameters to `bundle-Specimen-search-params.xml` (+40 lines). Commit `1764e013` ("updated references") then **reverted** both of those additions to bring the artifact in line with the actual workgroup disposition: it removed `Specimen.focus` from the StructureDefinition and removed both new search parameters from the bundle (-40 lines from the search-param bundle, -22 lines net from the SD), and in the same commit added a single `<targetProfile>` for `http://hl7.org/fhir/StructureDefinition/RelatedPerson` to `Specimen.subject` along with a new `<comment>` element on `Specimen.subject` ("When the specimen is not from the record subject, the RelatedPerson can be used for specimens from other entities, either from humans or animals."). Commit `810b9abd` is editorial: it added an `FHIR-53384` link to the interim release-notes blockquote in `specimen-introduction.xml`. The per-ticket diff is therefore misleading on its own (it adds and then removes a brand-new element); the after-applied state — i.e., RelatedPerson added to `Specimen.subject` and a new comment on `Specimen.subject` — is captured in the roll-up below.

## Roll-up Summary (after-applied state)

The window's net effect on Specimen, scoped to the files above and derived from `git diff 5d67a34a..HEAD`:

- **StructureDefinition (`structuredefinition-Specimen.xml`):** Two surgical additions on `Specimen.subject`:
  - A new `<comment>` element with text *"When the specimen is not from the record subject, the RelatedPerson can be used for specimens from other entities, either from humans or animals."*
  - A new `<targetProfile value="http://hl7.org/fhir/StructureDefinition/RelatedPerson"/>` appended after `NutritionProduct` in the existing `Reference` type on `Specimen.subject`. The cardinality of `Specimen.subject` is unchanged (`0..1`, `isSummary=true`). No other elements were added, removed, retyped, or rebound. **No new `Specimen.focus` element was introduced** despite the ticket title — the original proposal was superseded by the workgroup motion. Snapshot regeneration is required for the new `targetProfile` and `comment`.
- **Intro / narrative (`specimen-introduction.xml`):** A 6-line `<blockquote style="background-color: lightblue">` was added at the top of the Scope and Usage section as an interim release-notes marker, listing only `FHIR-53384` as a Jira link. No substantive narrative description of the change was added; the proposed ballot note below is intended to replace this stub. `specimen-notes.xml` is unchanged.
- **Search parameters (`bundle-Specimen-search-params.xml`):** Net-zero. The `focus` and `focus-code` search parameters added by `7b25639a` were removed by `1764e013`, leaving the search-parameter bundle identical to its state at the since-commit.
- **Operations (`list-Specimen-operations.xml`):** Unchanged.
- **Examples:** No examples added, removed, or modified — the existing `Specimen.subject` examples remain valid because `RelatedPerson` is purely additive to its target list.
- **Terminology (sibling `valueset-*` / `codesystem-*`):** Unchanged. No artifact-scoped ValueSet or CodeSystem under `source/specimen/` was touched in the window.

## Proposed Ballot Note (HTML)

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Since the previous ballot, a single change has been
  applied to Specimen by Orders &amp; Observations to broaden how specimens collected
  from someone other than the record subject are represented. The change is narrowly
  scoped to <code>Specimen.subject</code>; no new elements have been introduced and no
  existing cardinalities, types, search parameters, or operations have changed.</p>
  <ul>
    <li><code>Specimen.subject</code> may now reference <code>RelatedPerson</code> in
    addition to its existing target types (Patient, Group, Device, Substance, Location,
    NutritionProduct), and a comment has been added on <code>Specimen.subject</code>
    clarifying that <code>RelatedPerson</code> is the mechanism for representing a
    specimen drawn from an entity (human or animal) that is not the record subject —
    for example, veterinary zoonotic testing where a human is the clinical subject but
    the specimen originates from an animal, or genomic trio testing where parent
    specimens are reported in the proband's record
    (<a href="https://jira.hl7.org/browse/FHIR-53384">FHIR-53384</a>).</li>
    <li>The originally-proposed <code>Specimen.focus</code> CodeableReference element
    and its associated <code>focus</code>/<code>focus-code</code> search parameters
    were <em>not</em> adopted; the workgroup chose the lighter modification above
    instead. A follow-up concern about always retaining a direct
    <code>Patient</code> reference on patient-specific resources is being tracked
    separately under
    <a href="https://jira.hl7.org/browse/FHIR-56301">FHIR-56301</a> and is not part
    of this ballot
    (<a href="https://jira.hl7.org/browse/FHIR-53384">FHIR-53384</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **Existing stub release-notes blockquote.** The interim `<blockquote style="background-color: lightblue">…</blockquote>` added by commit [`810b9abd0f2c`](https://github.com/HL7/fhir/commit/810b9abd0f2c67f3d498cbe2f538cb61479688a2) at the top of `specimen-introduction.xml` only carries the bare `FHIR-53384` Jira link with no description. Recommend replacing it with the proposed `<blockquote class="ballot-note" id="bn1">` above (the in-progress message text — *"Release Notes (pending alternative process review with FMG)"* — suggests the editor was waiting for the proper ballot-note structure).
- **Ticket title vs. applied change.** The ticket title still reads *"Add Specimen.focus (CodeableReference)…"* but the applied change is the much smaller RelatedPerson modification on `Specimen.subject`. The proposed ballot note explicitly calls this out so balloters comparing the title to the spec are not surprised.
- **Search-parameter neutrality.** Although `bundle-Specimen-search-params.xml` shows up as "touched in window" in the per-commit table, the after-applied diff is empty (`focus`/`focus-code` were added then removed). No reviewer action on search parameters is required.
- **Cross-references.** `fhir-augury-cli cross-referenced` returned zero hits for all three commit SHAs in the window; ticket attribution for the two non-`FHIR-…`-tagged commits (`1764e013`, `810b9abd`) is by content (they touch the same `Specimen.subject` differential / the FHIR-53384 release-notes link). No `gh api` fallback was needed; all three commits were resolvable from the cached clone.
- **Follow-up ticket.** [FHIR-56301](https://jira.hl7.org/browse/FHIR-56301) is referenced from FHIR-53384's Jira comments as the home for Lloyd's "must keep a direct Patient reference" concern; that ticket is not in the current window and is mentioned in the proposed note only to scope balloter expectations.

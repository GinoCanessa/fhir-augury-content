# Artifact Ballot Note Draft: Condition (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `Condition` |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 2 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of `Condition` for this run (resolved against the
briefing's authoring layout for `source/<resource>/`):

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/condition/structuredefinition-Condition.xml` | StructureDefinition (canonical) | yes |
| `source/condition/condition-introduction.xml` | Narrative intro (ballot note lives here) | yes |
| `source/condition/condition-notes.xml` | Supplementary narrative | no |
| `source/condition/bundle-Condition-search-params.xml` | Search parameters | no |
| `source/condition/list-Condition-operations.xml` | Operations | no |
| `source/condition/list-Condition-examples.xml` | Examples list | no |
| `source/condition/list-Condition-packs.xml` | Implementation packs list | no |
| `source/condition/condition-examples-header.xml` | Examples narrative header | no |
| `source/condition/condition-fivews-mapping-exceptions.xml` | 5W mapping exceptions | no |
| `source/condition/implementationguide-Condition-core.xml` | Sibling IG artifact | no |
| `source/condition/codesystem-condition-state.xml` | Artifact-scoped CodeSystem (1) | no |
| `source/condition/valueset-condition-*.xml` | Artifact-scoped ValueSets (12) | no |
| `source/condition/condition-example*.xml` | Examples (14 files) | no |

Patterns that produced no match in the clone:

- `source/condition/condition-spreadsheet.xml` — no legacy spreadsheet present (SD is authoritative, per the briefing's gotchas).

## Current Ballot Note

The intro file at HEAD already carries one `ballot-note` blockquote
plus a sibling "All Changes" blockquote that lists the same tickets:

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> Key changes made since FHIR 6.0.0-ballot4:</p>
<ul>
  <li>Non-Compatible Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li>Compatible, Substantive Changes
    <ul>
	  <li>None</li>
    </ul>
  </li>
  <li>Non-Substantive Changes
    <ul>
      <li><a href="https://jira.hl7.org/browse/FHIR-54914">FHIR-54914</a>: Clarified Condition.verificationStatus comment</li>
	  <li><a href="https://jira.hl7.org/browse/FHIR-54454">FHIR-54454</a>: Clarified Condition.category short display</li>
    </ul>
  </li>
</ul>
<p></p>
</blockquote>
<blockquote style="background-color: lightblue">
  <p><b>All Changes (including Technical Corrections not listed above):</b></p>
  <ul>
    <li><a href="https://jira.hl7.org/browse/FHIR-54914">FHIR-54914</a>: Clarified Condition.verificationStatus comment</li>
	<li><a href="https://jira.hl7.org/browse/FHIR-54454">FHIR-54454</a>: Clarified Condition.category short display</li>
  </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-54914](https://jira.hl7.org/browse/FHIR-54914) | Clarify Condition.verificationStatus comments | [`921fc1585a20`](https://github.com/HL7/fhir/commit/921fc1585a203f472f9650a5896e155734300777) |
| [FHIR-54454](https://jira.hl7.org/browse/FHIR-54454) | Show diagnostic-report-impression in Condition.category description | [`921fc1585a20`](https://github.com/HL7/fhir/commit/921fc1585a203f472f9650a5896e155734300777) |

Both tickets were applied by the same single commit; ticket attribution
was derived from the `J#54914` / `J#54454` markers in the commit
subject. The `cross-referenced` lookup against the commit SHA returned
no additional hits.

## Per-Ticket Detail

### [FHIR-54914](https://jira.hl7.org/browse/FHIR-54914) — Clarify Condition.verificationStatus comments

- **Work group:** Patient Care
- **Resolution:** Persuasive with Modification
- **Disposition (verbatim):**

  > 2/12/26:
  >
  > text: Although the Terminology Binding is Required, the data type
  > is CodeableConcept which allows multiple codings. If populated,
  > one code from the binding must be present, but additional codes
  > with greater specificity, ~~perhaps~~ drawn from other
  > terminologies ~~SNOMED~~, may also be present if needed.
  >
  > explanation:
  >
  > search:
  >
  > (Vote recorded earlier: Rob Hausam / Emma Jones: 0-0-4.)

- **Disposition summary:** Patient Care agreed to replace the existing
  `Condition.verificationStatus` comment with a tighter statement that
  reconciles the Required binding with the CodeableConcept data type:
  the binding code must be present when populated, and additional
  codings drawn from other terminologies may be added for greater
  specificity. The reporter's secondary point about removing the
  abdominal-pain-in-the-ED example was accepted by dropping that
  paragraph; the suggestion to mirror the change on
  `Condition.clinicalStatus` was not adopted in this commit.
- **Commits applying this ticket:**
  - [`921fc1585a20`](https://github.com/HL7/fhir/commit/921fc1585a203f472f9650a5896e155734300777) — J#54914 Clarified Condition.verificationStatus comment;  J#54454 Clarified Condition.category short display (2026-04-21)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-Condition.xml`, the `<comment>` on element
  `Condition.verificationStatus` was rewritten from the prior
  two-paragraph text (which led with "verificationStatus is not
  required" and used the ED abdominal-pain example) to the new
  single-paragraph text aligned with the disposition: "Although the
  terminology binding is required, the data type is CodeableConcept
  which allows multiple codings. If populated, one code from the
  binding must be present, but additional codes with greater
  specificity, drawn from other terminologies, may also be present if
  needed." The committee-notes extension on the same element was
  updated from `GF#11281, GF#16193, J#28458.` to
  `GF#11281, GF#16193, J#28458, J#54914`. No changes to cardinality,
  type, or binding. The matching ballot-note bullet was added to
  `condition-introduction.xml`.

### [FHIR-54454](https://jira.hl7.org/browse/FHIR-54454) — Show diagnostic-report-impression in Condition.category description

- **Work group:** Patient Care
- **Resolution:** Not Persuasive with Modification
- **Disposition (verbatim):**

  > 2/12 PC
  >
  > Motion: This is an example binding; listing the values in 'short'
  > is useful for required bindings but may be confusing in this
  > case. We will replace this list with sufficiently vague text
  > describing the broad category: "Classification of type of
  > condition"
  >
  > (Follow-up note from michelle.m.miller: "This is not a technical
  > correction. It is a non-substantive change request.")

- **Disposition summary:** Rather than enumerating individual
  category codes (including the newly added
  `diagnostic-report-impression`) in the element's `short` display,
  Patient Care voted to replace the value enumeration with a generic
  descriptor, on the rationale that `Condition.category` carries an
  example binding for which a code list in `short` is misleading.
- **Commits applying this ticket:**
  - [`921fc1585a20`](https://github.com/HL7/fhir/commit/921fc1585a203f472f9650a5896e155734300777) — J#54914 Clarified Condition.verificationStatus comment;  J#54454 Clarified Condition.category short display (2026-04-21)
- **Changes applied (per Step 5b, scoped to this artifact):** In
  `structuredefinition-Condition.xml`, the `<short>` value on
  `Condition.category` changed from
  `problem-list-item | encounter-diagnosis` to
  `Classification of type of condition`. The committee-notes
  extension on the same element was updated from `J#48358` to
  `J#48358, J#54454`. The element's `<definition>`, `<comment>`,
  cardinality, type, and binding were not modified, and no value-set
  files were touched in this window (the `diagnostic-report-impression`
  code that originally prompted the ticket lives in the bound
  ValueSet, which was not changed here). The matching ballot-note
  bullet was added to `condition-introduction.xml`.

## Roll-up Summary (after-applied state)

Diff window: `5d67a34a13a5..db79dcdfe196`, scoped to `source/condition/`.
Two files changed (`condition-introduction.xml` +32 / -0;
`structuredefinition-Condition.xml` +4 / -4).

- **StructureDefinition (`structuredefinition-Condition.xml`):**
  - `Condition.verificationStatus.comment` rewritten to a single
    paragraph reconciling the Required binding with the CodeableConcept
    data type and dropping the abdominal-pain-in-the-ED example; the
    differential text now reads "Although the terminology binding is
    required, the data type is CodeableConcept which allows multiple
    codings. If populated, one code from the binding must be present,
    but additional codes with greater specificity, drawn from other
    terminologies, may also be present if needed."
  - `Condition.category.short` changed from
    `problem-list-item | encounter-diagnosis` to
    `Classification of type of condition`.
  - Committee-notes extensions updated on both elements to record the
    applying tickets (`J#54914`, `J#54454`).
  - No changes to cardinality, type, binding, constraints, or any
    other element. `<snapshot>` regeneration is required so that the
    revised `verificationStatus` comment and `category` short flow
    into the published view; treat snapshot as derived.
- **Intro / narrative (`condition-introduction.xml`,
  `condition-notes.xml`):** A new `ballot-note` blockquote (`id="bn1"`)
  plus a companion "All Changes" blockquote were added at the top of
  the intro, listing both tickets under "Non-Substantive Changes".
  `condition-notes.xml` was not touched.
- **Search parameters (`bundle-Condition-search-params.xml`):** No
  changes.
- **Operations (`list-Condition-operations.xml`):** No changes.
- **Examples:** No changes — none of the
  `condition-example*.xml` files were touched and the existing
  examples remain valid against the unchanged element shapes.
- **Terminology (sibling `valueset-condition-*.xml`,
  `codesystem-condition-state.xml`):** No changes. In particular, the
  `diagnostic-report-impression` code referenced by FHIR-54454 was
  resolved at the narrative level only; the bound ValueSets were not
  modified.

## Proposed Ballot Note (HTML)

The intro file already carries a ballot note that correctly classifies
both changes as Non-Substantive and links each ticket. The proposed
revision keeps that classification, preserves the existing `id="bn1"`,
and tightens the bullet wording so it reflects the actual after-applied
edits (rewritten comment / replaced short display) rather than a
generic "Clarified …" gloss.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> Changes since FHIR 6.0.0-ballot4 are
  limited to two element-level narrative clarifications on the
  <code>Condition</code> StructureDefinition; cardinality, types,
  bindings, search parameters, operations, and examples are unchanged.</p>
  <ul>
    <li>Non-Compatible Changes
      <ul>
        <li>None</li>
      </ul>
    </li>
    <li>Compatible, Substantive Changes
      <ul>
        <li>None</li>
      </ul>
    </li>
    <li>Non-Substantive Changes
      <ul>
        <li>Rewrote the <code>Condition.verificationStatus</code>
        comment to reconcile the required binding with the
        <code>CodeableConcept</code> data type: when populated, one
        code from the binding must be present, and additional codings
        from other terminologies may be added for greater specificity.
        The earlier abdominal-pain-in-the-ED example was removed
        (<a href="https://jira.hl7.org/browse/FHIR-54914">FHIR-54914</a>).</li>
        <li>Replaced the <code>Condition.category</code>
        <code>short</code> display, which previously enumerated two
        example codes (<code>problem-list-item | encounter-diagnosis</code>),
        with the generic descriptor &quot;Classification of type of
        condition&quot;, on the rationale that an example binding is
        not well served by a code list in <code>short</code>
        (<a href="https://jira.hl7.org/browse/FHIR-54454">FHIR-54454</a>).</li>
      </ul>
    </li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- The companion light-blue "All Changes (including Technical
  Corrections not listed above)" blockquote that already sits below
  `bn1` should be retained as-is; it lists the same two tickets and is
  the spec's standard pattern for the artifact-level change log.
- FHIR-54914's reporter also suggested mirroring the comment
  clarification onto `Condition.clinicalStatus`. The applied commit
  did **not** touch `clinicalStatus`; if the work group still wants
  that mirror, it will need a follow-up ticket / commit and is out of
  scope for this ballot window.
- FHIR-54454's resolution is recorded as "Not Persuasive with
  Modification" — the reporter's request to add
  `diagnostic-report-impression` to the `short` display was rejected
  in favour of removing the enumeration entirely. The bound
  ValueSet was not edited in this window, so reviewers checking
  whether `diagnostic-report-impression` is in scope should look at
  the value set rather than the element narrative.
- The cached clone fully resolved the since-commit
  (`5d67a34a13a5`) and HEAD (`db79dcdfe196`); HEAD is a descendant of
  the since-commit, so the standard `since..HEAD` window was used and
  no `gh api` fallback was needed.
- `cross-referenced` returned no additional hits for the commit SHA;
  ticket attribution comes solely from the `J#…` markers in the
  commit subject, which match the two tickets exactly.

# Artifact Ballot Note Draft: terminologies (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Artifact | `terminologies` (support directory `source/terminologies/`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 1 |
| Tickets attributed | 0 |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` @ clone `1b369ff4e28e` |
| Generated | 2026-04-21T19:30:00Z |

## Source Files

`source/terminologies/` is a FhirCore *support directory* — a flat
collection of cross-resource value sets, code systems, and the
authoring spreadsheet that drives terminology binding generation. It
is not an artifact folder in the conventional `source/<name>/` sense
(no `structuredefinition-terminologies.xml`, no
`terminologies-introduction.xml`, no search-params / operations
bundle). The customary FhirCore artifact-file patterns are therefore
not applicable here; the file table below lists what the directory
actually holds and which files were touched in the window.

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/terminologies/bindings.xml` | Master bindings spreadsheet (XML SpreadsheetML); drives `terminologies.html` row generation | yes |
| `source/terminologies/quantity-exceptions.csv` | Bindings support table | no |
| `source/terminologies/boolean-yes-no.csv` | Bindings support table | no |
| `source/terminologies/template-code-list.csv` | Bindings support table | no |
| `source/terminologies/codesystem-*.xml` (16 files) | Cross-resource CodeSystems housed in this directory | no |
| `source/terminologies/valueset-*.xml` (57 files) | Cross-resource ValueSets housed in this directory | no |

Patterns from the briefing's standard Artifact Map that produced no match (expected — `terminologies` is a support directory, not a resource):

- `source/terminologies/structuredefinition-terminologies.xml` — no file (not an SD-backed artifact).
- `source/terminologies/terminologies-introduction.xml` — no file (the narrative lives in `source/terminologies.html`, which is a *page* and is handled by `notes-page`).
- `source/terminologies/terminologies-notes.xml` — no file.
- `source/terminologies/bundle-terminologies-search-params.xml` — no file.
- `source/terminologies/list-terminologies-operations.xml` — no file.
- `source/terminologies/list-terminologies-examples.xml` — no file.
- `source/terminologies/terminologies-spreadsheet.xml` — no file (the spreadsheet *is* `bindings.xml`, not a per-resource one).

## Current Ballot Note

`source/terminologies/` has no intro file, so there is no
artifact-scoped ballot-note location. (Ballot notes for the rendered
`terminologies.html` page belong to the page-level note flow handled
by `notes-page`, not to this artifact-style report.)

No existing ballot note.

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| (unattributed) | — | [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) |

The single commit in the window has no `FHIR-####` / `UTG-####` key
in its subject or body, and `cross-referenced` returned no hits for
the SHA.

## Per-Ticket Detail

### (unattributed)

- **Commits:**
  - [`a9658ed97c2a`](https://github.com/HL7/fhir/commit/a9658ed97c2a382863b51cf1f260c478cfa18f30) — *typos and bump kindling* (2026-03-18, Grahame Grieve)
- **Changes applied (scoped to this artifact):** A one-character typo
  fix in `source/terminologies/bindings.xml` at the row for binding
  number 58 (`Identifier.type`-style row): the literal value
  `6.0.0-ballo1` was corrected to `6.0.0-ballot1` in the source-version
  cell. The companion (target / final) cell on the same row already
  read `6.0.0-ballot1`, so this is purely a transcription correction
  with no semantic effect on which value set, strength, or version is
  bound — once `bindings.xml` is re-rendered the affected row in
  `terminologies.html` will display `6.0.0-ballot1` consistently
  across both columns. The remainder of the commit ("bump kindling")
  refers to a build-tool version bump in files outside
  `source/terminologies/` and is out of scope for this artifact.

## Roll-up Summary (after-applied state)

- **Master bindings spreadsheet (`bindings.xml`):** One row's
  source-version cell corrected from `6.0.0-ballo1` to `6.0.0-ballot1`.
  No row added, removed, reordered, or rebound; no value-set, code,
  strength, or context column changed; no schema change to the
  spreadsheet itself.
- **Support tables (`*.csv`):** Unchanged.
- **CodeSystems (`codesystem-*.xml`):** Unchanged.
- **ValueSets (`valueset-*.xml`):** Unchanged.

Net effect on the published spec: the affected row in
`terminologies.html` will show the correct ballot-version label
(`6.0.0-ballot1`) in both the source and target columns. There is
no normative or semantic change to any binding.

## Proposed Ballot Note (HTML)

This artifact (the `source/terminologies/` support directory) does
not host a ballot-note location of its own — there is no intro file
to embed a `<blockquote class="ballot-note">` into. The single change
in the window is a non-semantic typo fix and does **not** warrant a
balloter-visible note.

**Recommendation: no ballot note required for this artifact in this
window.**

If the typo correction needs to be acknowledged anywhere, the
appropriate location is the page-level note for `terminologies.html`
(handled by `notes-page`), not an artifact-level note here. The
verbiage below is provided only as a copy-paste fragment in case the
page-level draft wishes to mention the fix; it is **not** intended to
be inserted into `source/terminologies/` directly.

```html
<!-- Optional fragment for the page-level note on terminologies.html;
     do NOT insert into source/terminologies/ — there is no intro file
     here. -->
<li>Bindings table (row 58): corrected source-version label from
  <code>6.0.0-ballo1</code> to <code>6.0.0-ballot1</code> for
  consistency with the target-version cell. Non-semantic.</li>
```

## Notes for Reviewer

- **Artifact scope.** `source/terminologies/` is a FhirCore support
  directory, not a resource/datatype artifact. The standard FhirCore
  artifact patterns (`structuredefinition-*`, `<name>-introduction.xml`,
  search-params / operations bundles, examples lists, spreadsheet)
  do not apply. The "Source Files" table is enumerated directly from
  the directory contents rather than from the briefing's Artifact Map.
- **Ballot-note location.** Because there is no intro file under
  `source/terminologies/`, there is no place to attach an
  artifact-scoped ballot note. The user-facing narrative for this
  area lives in `source/terminologies.html` and is in scope for
  `notes-page` (page name `terminologies`).
- **Tickets.** No Jira keys appear in the only commit's message, and
  `fhir-augury-cli cross-referenced` returned 0 hits for the SHA. No
  tickets are attributable to the change.
- **Out-of-scope content in the same commit.** Commit
  `a9658ed97c2a` also touches files outside `source/terminologies/`
  ("bump kindling" — a build dependency / version bump). Those
  changes are intentionally not narrated here.
- **Briefing freshness.** `meta.json` records the briefing was
  generated against clone HEAD `1b369ff4e28e` (2026-04-20), while the
  cache clone is now at `db79dcdfe196`. The Artifact Map sections
  used here (general FhirCore patterns and the support-directory
  treatment of `source/terminologies/`) are stable across that small
  delta; this drift did not affect any conclusion.

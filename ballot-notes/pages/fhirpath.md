# Page Ballot Note Draft: fhirpath (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/fhirpath.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 2 |
| Tickets attributed | 1 (plus 1 cited in the existing note) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (analyzed against clone HEAD `1b369ff4e28e`; current clone HEAD is `db79dcdfe196` — briefing is slightly behind but category is unchanged) |
| Generated | 2026-04-21T00:00:00Z |

## Source Files

Files considered part of the `fhirpath` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/fhirpath.html` | Page source (ballot note lives here) | yes |
| `source/fhirpath-notes.html` | Supplementary narrative (FhirCore convention) | not present at HEAD |
| `source/fhirpath-examples.html` | Examples appendix (FhirCore convention) | not present at HEAD |

Note: a `source/fhirpath.md` file also exists at HEAD, but it is an
unmaintained legacy draft (no `[%settitle%]` / IG-publisher template
markers, plain-text formatting) that is not touched in this window
and is not the rendered page source. It is excluded from this report.

## Current Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> Key changes made since FHIR 6.0.0-ballot4:</p>
<ul>
  <li>Non-compatible Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li>Compatible, Substantive Changes
    <ul>
      <li><a href="https://jira.hl7.org/browse/FHIR-56303">FHIR-56303</a>: Allow htmlChecks() to be invoked on strings in addition to xhtml</li>
    </ul>
  </li>
  <li>Non-substantive Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
</ul>
<p></p>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-56312](https://jira.hl7.org/browse/FHIR-56312) | Extend htmlChecks() to apply to strings too | [`149475cc2c7b`](https://github.com/HL7/fhir/commit/149475cc2c7b0d24c349091284db13429b0c47d8) |
| (unattributed) | — | [`8d42f18e070c`](https://github.com/HL7/fhir/commit/8d42f18e070cf224ff528f180a2c6969c3326c5f) ("Added change description") |

The existing ballot note text cites [FHIR-56303](https://jira.hl7.org/browse/FHIR-56303) ("Enforce that this is safe XHTML"),
but FHIR-56303 is the *dependent* extension-pack ticket that consumes the
new behaviour — it does not itself change `fhirpath.html`. The actual
normative change to the page in this window comes from FHIR-56312. See
"Notes for reviewer" below.

## Per-Ticket Detail

### [FHIR-56312](https://jira.hl7.org/browse/FHIR-56312) — Extend htmlChecks() to apply to strings too

- **Work group:** FHIR Infrastructure
- **Resolution:** Persuasive
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. (The only Jira comment on
  > this ticket is an author note: "NOTE: There are existing servers
  > that return 'false' instead of 'empty' when invoking htmlChecks
  > on strings right now. This means that when this is rolled out,
  > some old servers will report an error when they encounter it.
  > (This might be a good thing from a safety perspective, but may be
  > frustrating from a compatibility perspective.)")

- **Disposition summary:** Extend `htmlChecks()` so it can be invoked
  on `string`-typed elements in addition to `xhtml` elements. When
  applied to a string, the string content is parsed as the body of a
  `<div>` and the same XHTML safety rules are evaluated. The function
  returns `false` (rather than empty) when the string is not valid
  HTML or fails the rules; it remains empty when invoked on an
  unsupported element type or on a collection.
- **Commits applying this ticket:**
  - [`149475cc2c7b`](https://github.com/HL7/fhir/commit/149475cc2c7b0d24c349091284db13429b0c47d8) — `https://jira.hl7.org/browse/FHIR-56312 - Extend htmlChecks to support the 'string' type too.` (2026-04-19)
- **Changes applied (per Step 5b, scoped to this page):**
  Rewrites the body of the `htmlChecks : Boolean` definition (anchor
  `fn-htmlChecks`, in the §6.5.2 "Additional functions" section). The
  prior text described `htmlChecks()` only for a single `xhtml`
  element. The revised text adds a second sentence stating that when
  invoked on items of type `string`, the contents are parsed as the
  content of a `<div>` and the function returns `false` if the string
  does not parse as valid HTML or fails the XHTML rules. The
  empty-return clause is also tightened: it now applies to any other
  kind of element *or* when invoked on a collection of elements
  (previously the wording read "or a collection of xhtml elements").

### (unattributed) — `8d42f18e070c` "Added change description"

- **Commit:** [`8d42f18e070c`](https://github.com/HL7/fhir/commit/8d42f18e070cf224ff528f180a2c6969c3326c5f) by Lloyd McKenzie (2026-04-19)
- **Changes applied:** Inserts the `<blockquote class="ballot-note"
  id="bn1">…</blockquote>` block at the top of `source/fhirpath.html`,
  immediately after `[%file newnavbar%]`. The block lists "Allow
  htmlChecks() to be invoked on strings in addition to xhtml" under
  "Compatible, Substantive Changes" and cites FHIR-56303. No other
  page content was modified by this commit. (The ticket reference is
  almost certainly the wrong key for the actual page change — see
  "Notes for reviewer".)

## Roll-up Summary (after-applied state)

- **Page header (above `<h2>FHIRPath</h2>`):** A new
  `<blockquote class="ballot-note" id="bn1">` was inserted with the
  "Note to Balloters" structure (Non-compatible / Compatible
  Substantive / Non-substantive). The single substantive bullet calls
  out "Allow htmlChecks() to be invoked on strings in addition to
  xhtml" and cites FHIR-56303.
- **Section: §6.5.2 "Additional functions" → `htmlChecks : Boolean`
  (anchor `fn-htmlChecks`):** The function definition is rewritten to
  cover string inputs in addition to `xhtml` elements. New text says
  that when invoked on a `string`, the content is parsed as the body
  of a `<div>` and `htmlChecks()` returns `false` if the string is
  not valid HTML or fails the XHTML safety rules. The empty-return
  clause is broadened to "any other kind of element or … a collection
  of elements" (previously phrased as "a collection of xhtml
  elements"). No change to the function signature or its Boolean
  return type for the xhtml case.
- **Examples / code snippets:** None added, removed, or changed.
- **Diagrams / images:** None.
- **Cross-page links:** Existing links to `narrative.html#xhtml` and
  `narrative.html#rules` are preserved verbatim; no new cross-page
  links.
- **Editorial cleanup:** Negligible — minor wording tightening
  ("returns true" → "the function returns true"; double space before
  the new sentence) folded into the htmlChecks() rewrite.

## Proposed Ballot Note

```html
<blockquote class="ballot-note" id="bn1">
<p><b>Note to Balloters:</b> Key changes made since FHIR 6.0.0-ballot4:</p>
<ul>
  <li>Non-compatible Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
  <li>Compatible, Substantive Changes
    <ul>
      <li>Extended <code>htmlChecks()</code> so it may be invoked on items of type <code>string</code> in addition to <code>xhtml</code> elements: the string is parsed as the body of a <code>&lt;div&gt;</code> and the same XHTML safety rules are applied, returning <code>false</code> when the string is not valid HTML or fails the rules. The empty-return clause was also clarified to cover any other element type or a collection of elements (<a href="https://jira.hl7.org/browse/FHIR-56312">FHIR-56312</a>).</li>
    </ul>
  </li>
  <li>Non-substantive Changes
    <ul>
      <li>None</li>
    </ul>
  </li>
</ul>
<p></p>
</blockquote>
```

## Notes for Reviewer

- **Mis-cited ticket in the existing ballot note.** The current
  `bn1` block cites [FHIR-56303](https://jira.hl7.org/browse/FHIR-56303)
  ("Enforce that this is safe XHTML") for the htmlChecks-on-string
  change. FHIR-56303 is a dependent FHIR Extensions Pack ticket — its
  own Jira comment says it can only be applied "if FHIR-56312 is
  approved" — and it does not itself touch `source/fhirpath.html` in
  this window. The actual page change was applied by commit
  [`149475cc2c7b`](https://github.com/HL7/fhir/commit/149475cc2c7b0d24c349091284db13429b0c47d8),
  whose subject explicitly references
  [FHIR-56312](https://jira.hl7.org/browse/FHIR-56312). The proposed
  note above re-cites FHIR-56312. Reviewer should confirm and decide
  whether to retain a secondary FHIR-56303 reference (e.g., as a
  "see also" pointer to the extension-pack consumer).
- **Behaviour-compatibility caveat (from FHIR-56312 author comment).**
  Some existing servers currently return `false` (rather than empty)
  when `htmlChecks()` is invoked on a string. The new specification
  text now defines that case to return `false` only when the string
  fails the rules, and to return empty when the input type is
  unsupported. Implementers may want to flag this in implementation
  notes; not adding it as a ballot bullet because it is not a
  separate spec change.
- **Unattributed commit `8d42f18e070c`.** This commit only inserts
  the ballot-note block (no narrative changes). It carries no Jira
  key in its message and `cross-referenced` returned no hits, so it
  is reported as unattributed; functionally it is part of the
  FHIR-56312 work.
- **Cross-reference lookups.** `fhir-augury-cli cross-referenced`
  returned zero hits for both commit SHAs in the window. Ticket
  attribution was therefore based solely on the regex match
  (`FHIR-\d+`) in commit subjects/bodies.
- **Out-of-scope file in window:** None. Both commits in the window
  touch only `source/fhirpath.html`.
- **Briefing freshness.** The briefing was generated against clone
  HEAD `1b369ff4e28e`; the current clone HEAD is `db79dcdfe196`. The
  category (`FhirCore`) is unchanged, so page resolution is
  unaffected.
- **Services health-check.** `fhir-augury-cli services health` is not
  a supported action in the deployed CLI version
  (`2026.0421.1709+f1c9f5b…`); valid actions are `status` and
  `stats`. The substantive ticket-fetch and cross-reference calls
  succeeded, so this did not block the run.

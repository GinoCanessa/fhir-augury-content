# Page Ballot Note Draft: signatures (HL7/fhir)

| | |
|-|-|
| Repository | [HL7/fhir](https://github.com/HL7/fhir) (FhirCore) |
| Page | `source/signatures.html` |
| Resolution rule | FhirCore convention (`source/<page>.html`) |
| Window | [`5d67a34a13a5`](https://github.com/HL7/fhir/commit/5d67a34a13a58961296ccac9dd9d63e1fe4fdbdd)..[`db79dcdfe196`](https://github.com/HL7/fhir/commit/db79dcdfe196d35bd0e74c58c655a4c1c8f534f7) |
| Commits in window | 4 |
| Tickets attributed | 4 (3 from commit subjects; 1 (FHIR-52810) inferred from the after-applied diff and the existing ballot note) |
| Briefing | `cache/github/repos/HL7_fhir/repo-analysis/briefing.md` (per `meta.json`, analyzed 2026-04-20 against clone HEAD `1b369ff4e28e`) |
| Generated | 2026-04-22T17:13:18Z |

## Source Files

Files considered part of the `signatures` page for this run:

| Path | Role | Touched in window |
|------|------|-------------------|
| `source/signatures.html` | Page source (ballot note lives here) | yes |

No `signatures-notes.html` / `signatures-examples.html` siblings exist at HEAD.

## Current Ballot Note

The page at HEAD contains a single ballot note, added in commit
[`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a)
(“added ballot-note for changes since Jan ballot”), inserted between
the `[%file newnavbar%]` directive and the `<h1>Digital Signatures</h1>`
heading:

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To ensure that signature is ready for Normative status, we are seeking ballot comments on the substantive content.</p>
  <ul>
  <li>The key changes made since the January 2026 R6 ballot include:</li>
    <ul>
    <li>Added notes that XAdES has other signature profiles. - <a href="https://jira.hl7.org/browse/FHIR-52819">FHIR-52819</a></li>
    <li>Added notes that JAdES has other signature profiles. - <a href="https://jira.hl7.org/browse/FHIR-52818">FHIR-52818</a></li>
    <li>Clarified Bundle signature should not use id, use fragment identifier. - <a href="https://jira.hl7.org/browse/FHIR-52810">FHIR-52810</a></li>
    <li>Clarified counter signing. - <a href="https://jira.hl7.org/browse/FHIR-52813">FHIR-52813</a></li>
    </ul>
  </ul>
</blockquote>
```

## Tickets Applied in Window

| Ticket | Title | Commits |
|--------|-------|---------|
| [FHIR-52819](https://jira.hl7.org/browse/FHIR-52819) | recommending XAdES-T for non-repudiation | [`138153a94544`](https://github.com/HL7/fhir/commit/138153a94544af48e501fc7213f8c3287b2e1088) |
| [FHIR-52818](https://jira.hl7.org/browse/FHIR-52818) | Recommend JAdES-B-T for non-repudiation | [`44795cdd7120`](https://github.com/HL7/fhir/commit/44795cdd712065b658a8df2538a5a095bdd5b4d9) |
| [FHIR-52813](https://jira.hl7.org/browse/FHIR-52813) | Countersigning not completely clear | [`9f8597f0a551`](https://github.com/HL7/fhir/commit/9f8597f0a551bb5fcf4b3db6cd8071f8845de9d8) |
| [FHIR-52810](https://jira.hl7.org/browse/FHIR-52810) | Signature on Bundle should not use id | (no commit subject cites this key in window — see Notes for reviewer; the after-applied Bundle/`#/` change rides along inside [`9f8597f0a551`](https://github.com/HL7/fhir/commit/9f8597f0a551bb5fcf4b3db6cd8071f8845de9d8)) |
| (unattributed) | added ballot-note for changes since Jan ballot | [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a) |

The single unattributed commit is the editorial commit that inserted
the ballot-note `<blockquote>` itself; it carries no ticket key and
no other narrative changes.

## Per-Ticket Detail

### [FHIR-52819](https://jira.hl7.org/browse/FHIR-52819) — recommending XAdES-T for non-repudiation

- **Work group:** Security
- **Resolution:** Persuasive with Modification (Status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. The submitter (CarlGe / JIRAUSER26199) argued that XAdES (ETSI EN 319 132‑1) extends XMLDSIG to meet eIDAS AdES requirements and proposed differentiating XMLDSIG (integrity) from XAdES (non‑repudiation). John Moehrke’s applied‑vote comment on 2026‑03‑09 records: “I have updated the specification as much as I can. There is no way to reference XAdES‑B‑T nor XAdES‑B‑LTA. From Wikipedia reference it is clear these profiles existed before but do not exist now. So I have left in place the XAdES‑T that does exist.”

- **Disposition summary:** Acknowledge that XAdES defines additional signature profiles beyond what FHIR currently names, and steer implementers needing more than integrity protection to consult those profiles, while keeping the existing `XAdES-T` reference (the only profile name still resolvable via current ETSI/W3C URLs).
- **Commits applying this ticket:**
  - [`138153a94544`](https://github.com/HL7/fhir/commit/138153a94544af48e501fc7213f8c3287b2e1088) — FHIR-52819 - recommending XAdES-T for non-repudiation (2026-03-09T13:17:15-05:00)
- **Changes applied (per Step 5b, scoped to this page):**
  In the “XML Digital Signature” rules list, the `MAY conform to
  XAdES-T` bullet is extended with a trailing sentence: *“If more
  than integrity is required, the XAdES specification provides a set
  of profiles, and implementers should consider the rules found in
  those profiles carefully.”* No URL or normative keyword changes;
  the bullet remains a `MAY`.

### [FHIR-52818](https://jira.hl7.org/browse/FHIR-52818) — Recommend JAdES-B-T for non-repudiation

- **Work group:** Security
- **Resolution:** Persuasive with Modification (Status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. Submitter (CarlGe / JIRAUSER26199) proposed allowing both JWS and JAdES, recommending JWS for integrity and JAdES for non‑repudiation per eIDAS, and argued the specific `-B-T` / `-LT` levels should be left to implementer choice. Resolver (John Moehrke) responded that FHIR should “rather indicate that JAdES has recommendations worth following” because pinning specific JAdES levels would drift as JAdES evolves.

- **Disposition summary:** Soften the JAdES guidance by pointing implementers at the JAdES profile family rather than mandating a specific level, and upgrade the long-term-signature recommendation from `JAdES-B-LT` to `JAdES-B-LTA` (with a working ETSI URL).
- **Commits applying this ticket:**
  - [`44795cdd7120`](https://github.com/HL7/fhir/commit/44795cdd712065b658a8df2538a5a095bdd5b4d9) — FHIR-52818 - Recommend JAdES-B-T for non-repudiation (2026-03-09T13:20:19-05:00)
- **Changes applied (per Step 5b, scoped to this page):**
  In the “JWS Digital Signature” rules list, the `MAY conform to
  JAdES-B-T` bullet gains the same trailing sentence as the XAdES
  bullet (“If more than integrity is required, the JAdES specification
  provides a set of profiles, and implementers should consider the
  rules found in those profiles carefully.”). The adjacent `SHOULD
  conform to JAdES-B-LT` bullet is changed to `SHOULD conform to
  JAdES-B-LTA`, the link target is updated to the same ETSI TS
  119 182‑1 PDF, and the “…adds the timestamp of the signing,
  inclusion of the signing certificate, and statement of revocation”
  rationale is preserved (now describing `JAdES-B-LTA`).

### [FHIR-52813](https://jira.hl7.org/browse/FHIR-52813) — Countersigning not completely clear

- **Work group:** Security
- **Resolution:** Persuasive (Status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. Only post-resolution comment is the GitHub PR pointer (HL7/fhir#4028).

- **Disposition summary:** Rewrite the Bundle-signing rule that explains *which* embedded provenance entries are excluded from the to-be-signed Bundle, so that counter-signing is unambiguously covered: the trigger is now any embedded `Provenance` whose `Provenance.target` includes the bundle’s own fragment identifier `#/`, with an explicit note that counter-signing provenances may carry additional targets.
- **Commits applying this ticket:**
  - [`9f8597f0a551`](https://github.com/HL7/fhir/commit/9f8597f0a551bb5fcf4b3db6cd8071f8845de9d8) — FHIR-52813 - Countersigning not completely clear (2026-03-09T13:25:12-05:00)
- **Changes applied (per Step 5b, scoped to this page):**
  In the “Signature on Bundle” rules, the bullet describing the
  `Provenance.signature` content is rewritten. The previous text
  selected entries by *“all entries that have a resource where the
  Provenance.targets includes a reference to `Bundle/{id}`”*; the new
  text selects entries by *“all entries that have a resource which is
  a Provenance, where the Provenance.target elements includes a
  reference to `#/`. Note that counter-signing signatures will
  include additional targets, but one of the targets is always
  `#/`.”* This single edit is also the vehicle for FHIR-52810’s
  Bundle/id-vs-fragment-identifier change (see Notes for reviewer).

### [FHIR-52810](https://jira.hl7.org/browse/FHIR-52810) — Signature on Bundle should not use id

- **Work group:** Security
- **Resolution:** Persuasive with Modification (Status: Applied)
- **Disposition (verbatim):**

  > Disposition text not recorded in Jira. Submitter (CarlGe / JIRAUSER26199) argued that, for non‑repudiation, a Bundle signature should survive a `Bundle.id` change so that an importing server need not force the original signer to re‑sign; integrity‑only signatures (server‑applied) can tolerate re‑signing. Resolver (John Moehrke) initially countered that a `Bundle.id` change is itself a change requiring a fresh signature/Provenance, but agreed an alternative addressing scheme “like alternative canonicalization” could be useful.

- **Disposition summary:** Stop using `Bundle/{id}` as the in-bundle target reference for signature/countersigning provenance, and use the bundle’s self fragment identifier (`#/`) instead, so signatures remain valid under a `Bundle.id` change.
- **Commits applying this ticket:**
  - (none with this ticket key in the commit subject; the
    `Bundle/{id}` → `#/` change is carried by
    [`9f8597f0a551`](https://github.com/HL7/fhir/commit/9f8597f0a551bb5fcf4b3db6cd8071f8845de9d8)
    above.)
- **Changes applied (per Step 5b, scoped to this page):**
  Same single bullet rewrite as FHIR-52813 — the `Provenance.target`
  reference moves from `Bundle/{id}` to the fragment identifier `#/`.
  This is unavoidable overlap; the after-applied roll-up below is the
  authoritative description.

### (unattributed) — ballot-note insertion

- **Commits:**
  - [`406d76cb22d5`](https://github.com/HL7/fhir/commit/406d76cb22d5b3f53d68e77f716f2cba4488295a) — added ballot-note for changes since Jan ballot (2026-03-10T09:13:36-05:00)
- **Changes applied:** Inserts a new `<blockquote class="ballot-note" id="bn1">` immediately above the `<h1>Digital Signatures</h1>` heading. No narrative content outside the blockquote is touched.

## Roll-up Summary (after-applied state)

Authoritative summary of what changed across `source/signatures.html`
between `5d67a34a13a5` and `db79dcdfe196` (4 commits, +17 / −5 lines,
all in this file):

- **New ballot-note block (top of page, before `<h1>Digital
  Signatures</h1>`):** A `<blockquote class="ballot-note" id="bn1">`
  was added that frames the page as candidate Normative content for
  R6 and lists four bullets of substantive change (XAdES profiles,
  JAdES profiles, Bundle-signature fragment identifier, counter
  signing).
- **Section: `<h2>JWS Digital Signature</h2>` (rules list around
  line 369):**
  - `MAY conform to JAdES-B-T` bullet now ends with “If more than
    integrity is required, the JAdES specification provides a set of
    profiles, and implementers should consider the rules found in
    those profiles carefully.” (FHIR-52818)
  - `SHOULD conform to JAdES-B-LT` is upgraded to `SHOULD conform
    to JAdES-B-LTA`, with a working ETSI TS 119 182‑1 link; the
    rationale (timestamp, certificate, revocation statement) is
    preserved (FHIR-52818). No `SHOULD` → other normative keyword
    change.
- **Section: `<h2>XML Digital Signature</h2>` (rules list around
  line 396):** `MAY conform to XAdES-T` bullet is extended with the
  same “If more than integrity is required, the XAdES specification
  provides a set of profiles, and implementers should consider the
  rules found in those profiles carefully” sentence (FHIR-52819). No
  conformance-keyword change.
- **Section: “Signature on Bundle” rules (around line 436):** The
  `Provenance.signature` exclusion bullet is rewritten end‑to‑end.
  The set of entries removed from the to‑be‑signed Bundle is now
  qualified to *Provenance* resources whose `Provenance.target`
  includes the bundle self‑reference `#/` (instead of `Bundle/{id}`),
  with an explicit clarifying note that counter‑signing provenances
  may carry additional targets but always include `#/` (FHIR-52813
  and FHIR-52810). This change implicitly retires the
  `Bundle/{id}` self-reference style for embedded signature
  provenances.
- **Examples / code snippets:** None added or removed in the window.
- **Diagrams / images:** None added, removed, or replaced.
- **Cross-page links:** None added or removed; one ETSI URL is
  introduced inline against the `JAdES-B-LTA` upgrade.
- **Editorial cleanup:** No typo, whitespace, or link-normalization
  churn worth calling out (the diff introduces some CRLF endings on
  the affected lines but no separate editorial pass).

## Proposed Ballot Note

The existing `bn1` block is accurate against the after-applied state
and already cites the right four tickets. The proposed revision keeps
the existing `id="bn1"`, preserves all four bullets, lifts the inner
list out of the malformed nested `<ul>` (the current note has a `<ul>`
opened directly inside another `<ul>` with no surrounding `<li>`,
which renders inconsistently), and tightens each bullet to match the
specific narrative change in the after-applied diff.

```html
<blockquote class="ballot-note" id="bn1">
  <p><b>Note to Balloters:</b> To progress this page toward Normative status for R6, we are seeking ballot comments on the substantive content. Key changes since the January 2026 R6 ballot:</p>
  <ul>
    <li>In the XML Digital Signature rules, the <code>XAdES-T</code> bullet now points implementers at the broader XAdES profile family when more than integrity protection is required (<a href="https://jira.hl7.org/browse/FHIR-52819">FHIR-52819</a>).</li>
    <li>In the JWS Digital Signature rules, the <code>JAdES-B-T</code> bullet is similarly broadened to point at the JAdES profile family, and the long‑term‑signature recommendation is upgraded from <code>JAdES-B-LT</code> to <code>JAdES-B-LTA</code> with a working ETSI TS 119 182‑1 reference (<a href="https://jira.hl7.org/browse/FHIR-52818">FHIR-52818</a>).</li>
    <li>For Bundle signatures, the embedded‑signing‑provenance exclusion now keys off the bundle self‑reference <code>#/</code> instead of <code>Bundle/{id}</code>, so a signature survives a <code>Bundle.id</code> change (<a href="https://jira.hl7.org/browse/FHIR-52810">FHIR-52810</a>).</li>
    <li>The same Bundle‑signing rule is reworded to make counter‑signing unambiguous: a counter‑signing Provenance may carry additional targets, but one of its targets is always <code>#/</code> (<a href="https://jira.hl7.org/browse/FHIR-52813">FHIR-52813</a>).</li>
  </ul>
</blockquote>
```

## Notes for Reviewer

- **FHIR-52810 has no commit of its own in the window.** Its
  after‑applied change (Bundle/`{id}` → fragment identifier `#/`)
  is delivered by commit
  [`9f8597f0a551`](https://github.com/HL7/fhir/commit/9f8597f0a551bb5fcf4b3db6cd8071f8845de9d8),
  which is labelled FHIR-52813. Both tickets are marked “Applied”
  in Jira and both reference PR
  [HL7/fhir#4028](https://github.com/HL7/fhir/pull/4028) in their
  applied-vote comments, so this is co-resolution rather than a
  missed ticket. The proposed ballot note keeps both citations.
- **Existing ballot-note markup has a structural quirk.** The current
  `bn1` opens a `<ul>` directly inside another `<ul>` (with the
  intermediate `<li>The key changes…</li>` sitting alongside, not
  wrapping, the inner list). The proposed revision flattens this to
  a single `<ul>`. If the editorial preference is to keep the
  current nested structure verbatim, only the bullet wording from
  the proposed note needs to be substituted in.
- **`fhir-augury-cli services/health` is not a supported action** in
  the running orchestrator (returns `INVALID_ARGUMENT`; valid actions
  are `status` and `stats`). The skill instructions still call for
  `health`. Treated as non‑blocking; the `get` and `cross-referenced`
  commands used elsewhere in the workflow returned successfully.
- **`cross-referenced` for the four window commits returned zero hits
  in each case**, so ticket attribution relied on the `(FHIR|UTG)-\d+`
  regex against commit subjects/bodies plus the after-applied diff.
- **Briefing freshness:** `meta.json` records analysis on
  2026‑04‑20 against clone HEAD `1b369ff4e28e`; current clone HEAD
  is `db79dcdfe196`. The category (`FhirCore`) is unchanged and the
  page resolution is the standard `source/<page>.html` rule, so the
  staleness does not affect this report.
- **No commits in the window touched files outside
  `source/signatures.html`** (within the resolved page-source set),
  so no hand‑off to `notes-artifact` or `notes-datatype` is
  required.
- HEAD is a strict descendant of the since-commit; no symmetric‑
  difference fallback was needed.

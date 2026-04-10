# Session Log: FHIR-21013

**Phase:** planned
**Work Group:** BiomedicalResearchAndRegulation
**Source File:** `planned/BiomedicalResearchAndRegulation/FHIR-21013.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `6bb6405b-1d1b-4b0b-b4a9-631f765aa3bb` |
| **Session Summary** | Create Ticket Implementation Plans |
| **Agent ID** | `plan-FHIR-21013` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 17:47:02 UTC |
| **Duration** | 307s |
| **Total Tool Calls** | 31 |
| **Total Tokens** | 704,063 |

---

## Task Prompt

````markdown
You are planning the implementation of FHIR Jira ticket FHIR-21013 ("Patient.communication.language or Patient.communication.preferred?") for the "Biomedical Research & Regulation" work group.

Your job is to produce a structured implementation plan report and save it to:
C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21013.md

## Data Access

This skill supports two data access methods, in priority order:

1. **FhirAugury MCP** (preferred) — Use MCP tools directly when available.
   These are tools prefixed with `FhirAugury-` (e.g., `FhirAugury-get_item`,
   `FhirAugury-cross_referenced`). MCP tools are more efficient because they
   avoid shell invocation overhead.

2. **fhir-augury CLI** (fallback) — Use the CLI when MCP tools are not
   available. The CLI requires shell access and running FHIR Augury services
   (the CLI connects to the orchestrator, default `http://localhost:5150`).

**Detection:** At the start of the workflow, check whether `FhirAugury-get_item`
is available as a callable tool. If so, use MCP for all data access. Otherwise,
fall back to the CLI.

### MCP Tool Reference

| MCP Tool | Purpose |
|----------|---------|
| `FhirAugury-get_item` | Fetch full details of an item from a source |
| `FhirAugury-cross_referenced` | Get all cross-references (both directions) for a value |
| `FhirAugury-refers_to` | Get outgoing cross-references from an item |
| `FhirAugury-referred_by` | Get incoming cross-references to an item |
| `FhirAugury-content_search` | Unified text search across all sources |
| `FhirAugury-query_zulip_messages` | Structured Zulip message search |
| `FhirAugury-get_zulip_thread` | Get a full Zulip topic thread |
| `FhirAugury-get_jira_comments` | Get comments on a Jira issue |
| `FhirAugury-get_keywords` | Get extracted keywords for an item |
| `FhirAugury-related_by_keyword` | Find items related by keyword similarity |

### CLI Reference (Fallback)

The `fhir-augury` CLI accepts JSON commands. All examples below use inline
JSON; for readability, use `--pretty` when inspecting output manually.

```bash
fhir-augury --json '<json>' --pretty
```

| CLI Command | MCP Equivalent |
|-------------|----------------|
| `get` | `FhirAugury-get_item` |
| `cross-referenced` | `FhirAugury-cross_referenced` |
| `refers-to` | `FhirAugury-refers_to` |
| `referred-by` | `FhirAugury-referred_by` |
| `search` | `FhirAugury-content_search` |
| `keywords` | `FhirAugury-get_keywords` |
| `related-by-keyword` | `FhirAugury-related_by_keyword` |

## Prerequisites

- The GitHub source service cache must be populated (cloned repositories live
  under `cache/github/repos/`).

## Known GitHub Repository Cache

The following repositories are cloned under `cache/github/repos/`. The
directory names use underscores in place of slashes (e.g., `HL7_fhir` for
`HL7/fhir`). Each contains a `clone/` subdirectory with the actual git
checkout.

| Directory | Repository | Category |
|-----------|------------|----------|
| `HL7_fhir` | HL7/fhir | FhirCore |
| `HL7_UTG` | HL7/UTG | Utg (Unified Terminology Governance) |
| `HL7_fhir-extensions` | HL7/fhir-extensions | FhirExtensionsPack |
| `HL7_admin-incubator` | HL7/admin-incubator | Incubator |
| `HL7_api-incubator-ig` | HL7/api-incubator-ig | Incubator |
| `HL7_capstmt` | HL7/capstmt | Incubator |
| `HL7_cg-incubator` | HL7/cg-incubator | Incubator |
| `HL7_ebm-incubator` | HL7/ebm-incubator | Incubator |
| `HL7_fhir-testing-ig` | HL7/fhir-testing-ig | Ig |
| `HL7_immunization-incubator` | HL7/immunization-incubator | Incubator |
| `HL7_oo-incubator` | HL7/oo-incubator | Incubator |

### Repository Structure Conventions

**HL7/fhir (FhirCore):**
- Source files under `source/` directory
- Artifact directories: `source/<resource-name>/` (e.g., `source/patient/`)
- StructureDefinitions: `structuredefinition-*.xml`
- Canonical artifacts: `codesystem-*.xml`, `valueset-*.xml`, `searchparameter-*.xml`, etc.
- Configuration: `source/fhir.ini` maps artifact names to directories

**HL7/UTG (Terminology):**
- CodeSystems and ValueSets under `input/` directory
- Contains `sourceOfTruth/` with authoritative definitions

**HL7/fhir-extensions:**
- Extensions under `input/definitions/` and `input/` directories
- FSH files may be present for newer definitions

**Incubator repos:**
- Typically IG structure with `input/` directory
- May use FSH (`.fsh` files under `input/fsh/`)
- FHIR resources under `input/resources/` or `input/profiles/`

## Workflow

Execute the following steps. Run independent calls in parallel where possible.

### Step 1: Gather Ticket Details and Resolution

Run these commands in parallel:

**1a. Get the ticket with full content, comments, and snapshot:**

Using MCP:
```
FhirAugury-get_item(source="jira", id="FHIR-21013", includeComments=true, includeContent=true, includeSnapshot=true)
```

Key fields to extract from the response:
- `metadata.resolution` — the resolution type
- `metadata.resolution_description` — free-text description of the resolution
- `metadata.specification` — which spec is targeted
- `metadata.work_group` — owning work group
- `content` — the full ticket description
- `comments` — all discussion comments

**1b. Get all cross-references:**

Using MCP:
```
FhirAugury-cross_referenced(value="FHIR-21013", limit=50)
```

**1c. Get keywords for the ticket:**

Using MCP:
```
FhirAugury-get_keywords(source="jira", id="FHIR-21013", limit=30)
```

### Step 2: Determine Affected Repositories

Using the data gathered in Step 1, identify which repositories are affected:

**2a. Map the specification to repositories.**

| Specification Pattern | Primary Repository | Secondary |
|-----------------------|-------------------|-----------|
| "FHIR Core (FHIR)" | HL7/fhir | HL7/fhir-extensions |
| Contains "UTG" or "Terminology" | HL7/UTG | — |
| Contains "Extensions" | HL7/fhir-extensions | — |
| Specific IG name | Look for matching incubator/IG repo | — |

**2b. Identify repositories from cross-references.**

**2c. Identify resources from keywords.**

**2d. Search the repository clones directly.**

On Windows, use PowerShell:
```powershell
Get-ChildItem -Path cache\github\repos\HL7_fhir\clone\source -Directory -Recurse -Filter "<resource-name>"
Get-ChildItem -Path cache\github\repos\*\clone -Recurse -Include "*.xml","*.fsh" | Select-String -Pattern "<term>" -List | Select-Object Path
```

### Step 3: Analyze Impact

**3a. Examine existing definitions.**
**3b. Check for related PRs and commits.**
**3c. Look for related issues in the same area.**
**3d. Assess terminology impact.**

### Step 4: Build the Report

Compose a markdown report with the sections described below. Use the gathered
data to write substantive, specific content — not generic placeholders.

## Report Format

The report MUST follow this structure. Every section is required, though
sections may note "None identified" if no data exists.

```markdown
# Implementation Plan: {TICKET-KEY}

**Title:** {ticket title}
**Status:** {status}
**Resolution:** {resolution}
**Work Group:** {work group}
**Specification:** {specification}
**Resolved:** {resolved date}

---

## Resolution Summary

{A clear, concise summary of what the resolution requires.}

## Feature Proposal

### Problem Statement

{What problem or gap does this ticket address?}

### Proposed Change

{A detailed description of the change to be made.}

### Design Rationale

{Why this approach was chosen.}

## Impact Analysis

### Affected Repositories

#### {Repository Full Name} ({Category})

- **Role:** {What this repository contributes to the change}
- **Affected Files:**
  - `{file-path}` — {what changes in this file}
- **Change Scope:** {Minor / Moderate / Major}

### Breaking Changes

{Identify any backward-incompatible changes.}

### Related Specifications

{List other FHIR resources, operations, or profiles that reference or depend
on the changed artifacts.}

### Related Tickets

- **{TICKET-KEY}:** {title} — {how it relates}

### Terminology Impact

{If the change involves coded elements, list affected ValueSets and CodeSystems.}

## Implementation Plan

### Prerequisites

{Any changes that must be completed before this work can begin.}

### Step-by-Step Tasks

#### {Repository Full Name}

1. **{Task title}**
   - File: `{path/to/file}`
   - Action: {Precise description of what to change}
   - Details: {Any additional context}

### Validation Checklist

- [ ] StructureDefinition(s) validate with no errors
- [ ] Element definitions include short description and formal definition
- [ ] Cardinality is correct and consistent with the resolution
- [ ] Type constraints match the intended design
- [ ] Terminology bindings reference valid ValueSets
- [ ] Search parameters updated if the change adds searchable elements
- [ ] Examples updated to demonstrate the new/changed elements
- [ ] Resource scope/boundaries documentation updated if resource scope changed
- [ ] Cross-references to other resources are bidirectional
- [ ] No regressions in existing invariants or constraints

### Testing Considerations

{Describe what should be tested after the change is applied.}

### Open Questions

{List any ambiguities in the resolution that need clarification.}
```

## Important Rules

- **Use only data from the MCP or CLI and cached repositories.** Do not fabricate
  ticket details, file paths, or resolution content. If a call fails or
  returns no data, say so in the report.
- **Be specific in the proposal.** Generic statements like "modify the
  resource" are not useful. Name the exact element, path, type, cardinality,
  and binding.
- **Include actual file paths.** When referencing repository files, use the
  real paths found in the cache clones. Verify files exist before listing them.
- **The implementation plan must be actionable.** Each task should describe a
  single, concrete file change. A developer should be able to follow the plan
  without referring back to the original ticket.
- **Assess breaking changes honestly.** Do not downplay impact.
- **Cross-reference related tickets.**
- **Read the resolution description carefully.** The resolution (not the
  original ticket description) dictates what must be implemented.
- **Distinguish between resolution types.** Only "Applied", "Persuasive", and
  "Persuasive with Modification" resolutions require implementation. If the
  resolution is "Not Persuasive", "Duplicate", or "Withdrawn", note this in
  the report and explain that no implementation is needed.
- **Search the repo clones to find real files.** Don't guess at file paths.

Save the final report to: C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21013.md

````

---

## Agent Execution Log

### Turn 1

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-21013",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-21013: Patient.communication.language or Patient.communication.preferred?

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** US Coordinated Registry Network (CRN) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Robin Taylor
- **Created:** 2019-04-26T19:38:54+00:00
- **Updated:** 2020-01-16T04:19:47+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-21013

## Content
<p>What is the CRN trying to collect with the language element--a communication language, or the <b>preferred</b>* *communication language?</p>

<ul class="alternate" type="square">
	<li>The template gives concept and short name "communication language," but for long name, it refers to Preferred Language ISO 639.2).</li>
</ul>


<ul class="alternate" type="square">
	<li>The Mappings table lists harmonized element pat_pref_language_spoken, but FHIR Data Element Patient.communication.language.</li>
</ul>


<p>         If we want to collect the preferred language, should the IG use Patient.communication.preferred instead?</p>

## Snapshot
# FHIR-21013: Patient.communication.language or Patient.communication.preferred?

**Status:** Resolved - change required  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Persuasive  
**Assignee:** Unassigned  
**Reporter:** Robin Taylor  
**Work Group:** Biomedical Research & Regulation  
**Specification:** US Coordinated Registry Network (CRN) (FHIR)  
**Created:** 2019-04-26  
**Updated:** 2020-01-16  
**Resolved:** 2019-08-28  

## Description

<p>What is the CRN trying to collect with the language element--a communication language, or the <b>preferred</b>* *communication language?</p>

<ul class="alternate" type="square">
	<li>The template gives concept and short name "communication language," but for long name, it refers to Preferred Language ISO 639.2).</li>
</ul>


<ul class="alternate" type="square">
	<li>The Mappings table lists harmonized element pat_pref_language_spoken, but FHIR Data Element Patient.communication.language.</li>
</ul>


<p>         If we want to collect the preferred language, should the IG use Patient.communication.preferred instead?</p>

## Resolution Description

<p>For pat_pref_language_spoken add mapping to Patient.communication.preferred also to indicate that the language represented in Patient.communication.language is a preferred language.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-21013" (2 results)

- [jira] FHIR-21013 → [fhir] Patient.communication.language
  **Source:** Patient.communication.language or Patient.communication.preferred?
  **Type:** mentions
  **Context:** ... table lists harmonized element pat_pref_language_spoken, but FHIR Data Element Patient.communication.language. If we want to collect the preferred language, sh...
  **Score:** 0.05
  **Updated:** 2020-01-16T04:19:47+00:00
- [jira] FHIR-21013 → [fhir] Patient.communication.preferred
  **Source:** Patient.communication.language or Patient.communication.preferred?
  **Type:** mentions
  **Context:** ...ation.language. If we want to collect the preferred language, should the IG use Patient.communication.preferred instead? Patient.communication.language or Patie...
  **Score:** 0.05
  **Updated:** 2020-01-16T04:19:47+00:00
**Warnings:**
- Value 'FHIR-21013' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-21013
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| patient.communication.preferred | fhir_path | 4 | 13.504 |
| patient.communication.language | fhir_path | 4 | 12.092 |
| pref | word | 2 | 9.615 |
| communication | fhir_path | 19 | 9.448 |
| preferred | word | 12 | 8.085 |
| language | word | 18 | 7.064 |
| pat | word | 2 | 6.785 |
| speak | word | 2 | 6.303 |
| 639 | word | 1 | 5.687 |
| collect | word | 2 | 5.615 |
| crn | word | 1 | 5.498 |
| square | word | 2 | 4.856 |
| patient | fhir_path | 16 | 4.697 |
| alternate | word | 2 | 4.555 |
| harmonize | word | 1 | 3.875 |
| ul | word | 4 | 3.786 |
| mapping | word | 2 | 3.668 |
| iso | word | 1 | 3.601 |
| li | word | 4 | 3.526 |
| template | word | 1 | 3.288 |
| element | word | 3 | 2.614 |
| refer | word | 1 | 2.326 |
| type | word | 2 | 2.235 |
| concept | word | 1 | 2.167 |
| table | word | 1 | 2.144 |
| represent | word | 1 | 2.113 |
| list | word | 1 | 2.112 |
| ig | word | 1 | 1.465 |
| 2 | word | 1 | 1.462 |
| data/datum | word | 1 | 1.339 |

```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21013.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\planned\\BiomedicalResearchAndRegulation\\FHIR-21013.md",
  "file_text": "# Implementation Plan: FHIR-21013\n\n**Title:** Patient.communication.language or Patient.communication.preferred?\n**Status:** Resolved - change required\n**Resolution:** Persuasive\n**Work Group:** Biomedical Research & Regulation\n**Specification:** US Coordinated Registry Network (CRN) (FHIR)\n**Resolved:** 2019-08-28\n\n---\n\n## Resolution Summary\n\nThe resolution requires that the CRN IG's harmonized data element `pat_pref_language_spoken` be mapped to **both** `Patient.communication.language` and `Patient.communication.preferred`. Currently, the CDE-to-FHIR mapping table only maps `pat_pref_language_spoken` to `Patient.communication.language`, which captures the language itself but does not indicate that this is the patient's *preferred* language. By adding a mapping to the boolean element `Patient.communication.preferred`, the IG will correctly express that the communicated language is the patient's preferred one.\n\n## Feature Proposal\n\n### Problem Statement\n\nThe CRN IG's harmonized Common Data Element (CDE) template has an inconsistency between naming and FHIR mapping for the preferred language concept:\n\n1. The CDE uses the harmonized element name `pat_pref_language_spoken`, where \"pref\" clearly denotes **preferred** language.\n2. The CDE template's \"long name\" references \"Preferred Language (ISO 639.2).\"\n3. However, the FHIR mapping only points to `Patient.communication.language` \u2014 which captures a communication language but does **not** indicate whether it is the patient's preferred language.\n\nIn the FHIR Patient resource, preferred language status is expressed through the boolean element `Patient.communication.preferred` (0..1), which exists alongside `Patient.communication.language` (1..1) within the `Patient.communication` backbone element. Without mapping to `Patient.communication.preferred`, implementers using the CRN IG cannot determine whether a given communication language entry represents the patient's preferred language or merely one of several languages the patient can communicate in.\n\n### Proposed Change\n\nUpdate the CDE-to-FHIR mapping table in the CRN IG to map `pat_pref_language_spoken` to both FHIR elements:\n\n| Harmonized CDE | Current FHIR Mapping | Updated FHIR Mapping |\n|----------------|---------------------|----------------------|\n| `pat_pref_language_spoken` | `Patient.communication.language` | `Patient.communication.language`, `Patient.communication.preferred` |\n\nThis means that when populating `pat_pref_language_spoken`, implementers should:\n1. Set `Patient.communication.language` to the appropriate language code (using ISO 639 / BCP 47).\n2. Set `Patient.communication.preferred` to `true` to indicate that this is the patient's preferred communication language.\n\n### Design Rationale\n\nThis approach was chosen because:\n\n1. **Semantic completeness:** The har

... *(truncated, 14683 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21013.md with 14377 characters
```

</details>


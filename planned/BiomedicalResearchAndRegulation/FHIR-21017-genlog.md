# Session Log: FHIR-21017

**Phase:** planned
**Work Group:** BiomedicalResearchAndRegulation
**Source File:** `planned/BiomedicalResearchAndRegulation/FHIR-21017.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `6bb6405b-1d1b-4b0b-b4a9-631f765aa3bb` |
| **Session Summary** | Create Ticket Implementation Plans |
| **Agent ID** | `plan-FHIR-21017` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 17:56:50 UTC |
| **Duration** | 249s |
| **Total Tool Calls** | 39 |
| **Total Tokens** | 1,034,295 |

---

## Task Prompt

````markdown
You are planning the implementation of FHIR Jira ticket FHIR-21017 ("use procedure.location instead of location.identifier?") for the "Biomedical Research & Regulation" work group.

Your job is to produce a structured implementation plan report and save it to:
C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21017.md

## Data Access

Use MCP tools directly (prefixed with `FhirAugury-`). These are available as callable tools.

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

## Known GitHub Repository Cache

Repositories cloned under `cache/github/repos/` (directory names use underscores, each has `clone/` subdirectory):

| Directory | Repository | Category |
|-----------|------------|----------|
| `HL7_fhir` | HL7/fhir | FhirCore |
| `HL7_UTG` | HL7/UTG | Utg |
| `HL7_fhir-extensions` | HL7/fhir-extensions | FhirExtensionsPack |
| `HL7_admin-incubator` | HL7/admin-incubator | Incubator |
| `HL7_api-incubator-ig` | HL7/api-incubator-ig | Incubator |
| `HL7_capstmt` | HL7/capstmt | Incubator |
| `HL7_cg-incubator` | HL7/cg-incubator | Incubator |
| `HL7_ebm-incubator` | HL7/ebm-incubator | Incubator |
| `HL7_fhir-testing-ig` | HL7/fhir-testing-ig | Ig |
| `HL7_immunization-incubator` | HL7/immunization-incubator | Incubator |
| `HL7_oo-incubator` | HL7/oo-incubator | Incubator |

## Workflow

### Step 1: Gather Ticket Details (run in parallel)
1a. `FhirAugury-get_item(source="jira", id="FHIR-21017", includeComments=true, includeContent=true, includeSnapshot=true)`
1b. `FhirAugury-cross_referenced(value="FHIR-21017", limit=50)`
1c. `FhirAugury-get_keywords(source="jira", id="FHIR-21017", limit=30)`

### Step 2: Determine Affected Repositories
Map specification to repos. Search repo clones for actual files.

### Step 3: Analyze Impact
Examine existing definitions, check related PRs, look for related issues, assess terminology impact.

### Step 4: Build the Report

## Report Format

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
## Feature Proposal
### Problem Statement
### Proposed Change
### Design Rationale
## Impact Analysis
### Affected Repositories
#### {Repository Full Name} ({Category})
- **Role:** ...
- **Affected Files:** ...
- **Change Scope:** Minor / Moderate / Major
### Breaking Changes
### Related Specifications
### Related Tickets
### Terminology Impact
## Implementation Plan
### Prerequisites
### Step-by-Step Tasks
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
### Open Questions
```

## Important Rules
- Use only data from MCP and cached repositories. Do not fabricate.
- Be specific — name exact elements, paths, types, cardinalities.
- Include actual file paths verified to exist.
- Make the plan actionable.
- Assess breaking changes honestly.
- Read the resolution description carefully — it dictates what to implement.
- Only "Applied", "Persuasive", "Persuasive with Modification" require implementation.
- Search repo clones for real files — don't guess.

Save the final report to: C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21017.md

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
  "id": "FHIR-21017",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-21017: use procedure.location instead of location.identifier?

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** US Coordinated Registry Network (CRN) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Robin Taylor
- **Created:** 2019-04-26T20:09:56+00:00
- **Updated:** 2020-01-16T04:18:13+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-21017

## Content
<p>Since the CRN is trying to collect the ID of "The facility where the procedure was performed," should Procedure.location be used instead of Location.identifier?</p>

## Snapshot
# FHIR-21017: use procedure.location instead of location.identifier?

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

<p>Since the CRN is trying to collect the ID of "The facility where the procedure was performed," should Procedure.location be used instead of Location.identifier?</p>

## Resolution Description

<p>Modify Mapping of FacilityID to be Procedure.location.identifier instead of just "location.identifier". Change the profile to be procedure-crn. Implementers can use the us-core-location profile to represent the location resource within the bundle referenced by the procedure. Update the procedure-crn profile to reference us-core-location profile for the location data element.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-21017" (3 results)

- [jira] FHIR-21017 → [fhir] Procedure.location
  **Source:** use procedure.location instead of location.identifier?
  **Type:** mentions
  **Context:** ...g to collect the ID of "The facility where the procedure was performed," should Procedure.location be used instead of Location.identifier? use procedure.locatio...
  **Score:** 0.05
  **Updated:** 2020-01-16T04:18:13+00:00
- [jira] FHIR-21017 → [fhir] Location.identifier
  **Source:** use procedure.location instead of location.identifier?
  **Type:** mentions
  **Context:** ...here the procedure was performed," should Procedure.location be used instead of Location.identifier? use procedure.location instead of location.identifier? Modi...
  **Score:** 0.05
  **Updated:** 2020-01-16T04:18:13+00:00
- [jira] FHIR-21017 → [fhir] Procedure.location.identifier
  **Source:** use procedure.location instead of location.identifier?
  **Type:** mentions
  **Context:** ...ure.location instead of location.identifier? Modify Mapping of FacilityID to be Procedure.location.identifier instead of just "location.identifier". Change the ...
  **Score:** 0.05
  **Updated:** 2020-01-16T04:18:13+00:00
**Warnings:**
- Value 'FHIR-21017' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-21017
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| crn | word | 3 | 12.948 |
| procedure.location.identifier | fhir_path | 1 | 10.245 |
| facilityid | word | 1 | 10.245 |
| procedure.location | fhir_path | 1 | 9.058 |
| location.identifier | fhir_path | 1 | 8.559 |
| location | fhir_path | 15 | 8.290 |
| procedure | fhir_path | 10 | 7.759 |
| identifier | word | 7 | 6.432 |
| collect | word | 1 | 5.201 |
| facility | word | 1 | 5.012 |
| modify | word | 1 | 4.245 |
| perform | word | 1 | 3.896 |
| bundle | fhir_path | 1 | 3.576 |
| profile | word | 4 | 3.488 |
| mapping | word | 1 | 3.398 |
| implementer | word | 1 | 3.229 |
| core | word | 2 | 3.151 |
| represent | word | 1 | 3.036 |
| reference | word | 2 | 2.894 |
| update | word | 1 | 1.996 |
| element | word | 1 | 1.976 |
| data/datum | word | 1 | 1.924 |
| change | word | 1 | 1.857 |
| resource | word | 1 | 1.779 |

```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21017.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\planned\\BiomedicalResearchAndRegulation\\FHIR-21017.md",
  "file_text": "# Implementation Plan: FHIR-21017\n\n**Title:** use procedure.location instead of location.identifier?\n**Status:** Resolved - change required\n**Resolution:** Persuasive\n**Work Group:** Biomedical Research & Regulation\n**Specification:** US Coordinated Registry Network (CRN) (FHIR)\n**Resolved:** 2019-08-28\n\n---\n\n## Resolution Summary\n\nThe resolution directs implementers to modify the CDE (Common Data Element) mapping for \"Facility ID\" from `Location.identifier` to `Procedure.location.identifier`, making the data path explicit through the Procedure resource. The profile associated with this CDE should change from `us-core-location` to `procedure-crn`. The `procedure-crn` profile must be updated to constrain `Procedure.location` to reference the US Core Location profile (`us-core-location`), ensuring the facility identifier is discoverable through the procedure's location reference chain.\n\n## Feature Proposal\n\n### Problem Statement\n\nThe CRN IG's CDE-to-FHIR mapping table currently maps the \"Facility ID\" data element directly to `Location.identifier` using the `us-core-location` profile. This is semantically ambiguous because:\n\n1. It does not specify _which_ Location resource is relevant \u2014 the mapping implies a standalone Location resource rather than one connected to the procedure context.\n2. The CRN's purpose is to collect the identifier of \"the facility where the procedure was performed.\" The relationship between the procedure and the facility is only implicit.\n3. The FHIR Procedure resource already has a `Procedure.location` element (0..1, Reference(Location)) that explicitly captures \"the location where the procedure actually happened.\"\n\nBy not using `Procedure.location`, the mapping misses the semantic link between the procedure and the facility, making it harder for implementers to understand how to populate a conformant CRN bundle.\n\n### Proposed Change\n\nPer the resolution:\n\n1. **Update CDE mapping:** Change the \"Facility ID\" CDE mapping from `Location.identifier` (profile: `us-core-location`) to `Procedure.location.identifier` (profile: `procedure-crn`).\n2. **Update procedure-crn profile:** Add a type constraint on `Procedure.location` that requires it to reference a resource conforming to the US Core Location profile (`http://hl7.org/fhir/us/core/StructureDefinition/us-core-location`).\n3. **Maintain us-core-location reuse:** Implementers continue to use the `us-core-location` profile for the actual Location resource instance within the bundle; the change only affects how that resource is _reached_ (via `Procedure.location`).\n\n### Design Rationale\n\n- **Explicit data path:** `Procedure.location.identifier` provides a clear, unambiguous traversal path from the procedure to the facility ID, aligning with the CRN's intent to collect facility information in the context of a speci

... *(truncated, 15079 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-21017.md with 14774 characters
```

</details>


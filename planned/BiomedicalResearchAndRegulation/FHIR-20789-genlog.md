# Session Log: FHIR-20789

**Phase:** planned
**Work Group:** BiomedicalResearchAndRegulation
**Source File:** `planned/BiomedicalResearchAndRegulation/FHIR-20789.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `31796050-70c3-4658-b5f9-324e4fc40e4c` |
| **Session Summary** | Orchestrate WG Ticket Planning |
| **Agent ID** | `plan-FHIR-20789` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 17:03:07 UTC |
| **Duration** | 373s |
| **Total Tool Calls** | 32 |
| **Total Tokens** | 620,085 |

---

## Task Prompt

````markdown
You are planning the implementation of FHIR Jira ticket FHIR-20789 ("Use of AdverseEvent for tracking adverse events in WHT CRN") for the "Biomedical Research & Regulation" work group.

Your job is to produce a structured implementation plan report and save it to:
C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-20789.md

## Workflow

### Step 1: Gather Ticket Details and Resolution

Run these 3 CLI commands IN PARALLEL:

1a. Get the ticket with full content, comments, and snapshot:
```
fhir-augury --json "{\"command\":\"get\",\"source\":\"jira\",\"id\":\"FHIR-20789\",\"includeComments\":true,\"includeContent\":true,\"includeSnapshot\":true}"
```

1b. Get all cross-references:
```
fhir-augury --json "{\"command\":\"cross-referenced\",\"value\":\"FHIR-20789\",\"limit\":50}"
```

1c. Get keywords for the ticket:
```
fhir-augury --json "{\"command\":\"keywords\",\"source\":\"jira\",\"id\":\"FHIR-20789\",\"limit\":30}"
```

### Step 2: Determine Affected Repositories

Using the data gathered in Step 1:
- Map the specification to repositories using these rules:
  - "FHIR Core (FHIR)" → HL7/fhir + HL7/fhir-extensions
  - Contains "UTG" or "Terminology" → HL7/UTG
  - Contains "Extensions" → HL7/fhir-extensions
  - Specific IG name → Look for matching incubator/IG repo
- Extract repository names from GitHub cross-references (format owner/repo#N)
- Use keywords to identify FHIR resources and find their source files
- Search the repository clones under cache\github\repos\ to find actual files:

Known repos in cache:
| Directory | Repository | Category |
|-----------|------------|----------|
| HL7_fhir | HL7/fhir | FhirCore |
| HL7_UTG | HL7/UTG | Utg |
| HL7_fhir-extensions | HL7/fhir-extensions | FhirExtensionsPack |
| HL7_admin-incubator | HL7/admin-incubator | Incubator |
| HL7_api-incubator-ig | HL7/api-incubator-ig | Incubator |
| HL7_capstmt | HL7/capstmt | Incubator |
| HL7_cg-incubator | HL7/cg-incubator | Incubator |
| HL7_ebm-incubator | HL7/ebm-incubator | Incubator |
| HL7_fhir-testing-ig | HL7/fhir-testing-ig | Ig |
| HL7_immunization-incubator | HL7/immunization-incubator | Incubator |
| HL7_oo-incubator | HL7/oo-incubator | Incubator |

Use PowerShell to search the clones:
```powershell
Get-ChildItem -Path cache\github\repos\HL7_fhir\clone\source -Directory -Recurse -Filter "<resource-name>"
Get-ChildItem -Path cache\github\repos\*\clone -Recurse -Include "*.xml","*.fsh" | Select-String -Pattern "<term>" -List | Select-Object Path
```

### Step 3: Analyze Impact
- Examine existing definitions by reading current source files
- Check for related PRs and commits from cross-references
- Search for related tickets affecting the same resources
- Assess terminology impact if coded elements are involved

### Step 4: Build the Report

Compose the report using this EXACT structure:

```markdown
# Implementation Plan: FHIR-20789

**Title:** {ticket title}
**Status:** {status}
**Resolution:** {resolution}
**Work Group:** {work group}
**Specification:** {specification}
**Resolved:** {resolved date}

---

## Resolution Summary
{Clear summary of what the resolution requires, using exact wording where available}

## Feature Proposal

### Problem Statement
{What problem does this ticket address?}

### Proposed Change
{Detailed, concrete description of the change}

### Design Rationale
{Why this approach was chosen}

## Impact Analysis

### Affected Repositories
#### {Repository Full Name} ({Category})
- **Role:** {What this repository contributes}
- **Affected Files:**
  - `{file-path}` — {what changes}
- **Change Scope:** {Minor / Moderate / Major}

### Breaking Changes
{Identify backward-incompatible changes, or "No breaking changes identified."}

### Related Specifications
{Other FHIR resources/operations/profiles that reference changed artifacts}

### Related Tickets
{Other Jira tickets affecting same resources}

### Terminology Impact
{ValueSet/CodeSystem changes needed, or "No terminology impact."}

## Implementation Plan

### Prerequisites
{Changes needed before this work can begin}

### Step-by-Step Tasks
#### {Repository Full Name}
1. **{Task title}**
   - File: `{path}`
   - Action: {Precise description}
   - Details: {Additional context}

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
{What should be tested after the change}

### Open Questions
{Ambiguities needing clarification, or "No open questions."}
```

## Important Rules
- Use ONLY data from the CLI and cached repositories. Do not fabricate ticket details, file paths, or resolution content.
- Be specific — name exact elements, paths, types, cardinality, and bindings.
- Include actual file paths verified from the cache clones.
- Only "Applied", "Persuasive", and "Persuasive with Modification" resolutions require implementation. Other resolutions should note no implementation needed.
- Search the repo clones to find real files. Don't guess at file paths.

Save the final report to: C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-20789.md

````

---

## Agent Execution Log

### Turn 1

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-20789.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\planned\\BiomedicalResearchAndRegulation\\FHIR-20789.md",
  "file_text": "# Implementation Plan: FHIR-20789\n\n**Title:** Use of AdverseEvent for tracking adverse events in WHT CRN\n**Status:** Resolved - change required\n**Resolution:** Persuasive\n**Work Group:** Biomedical Research & Regulation\n**Specification:** US Coordinated Registry Network (CRN) (FHIR)\n**Resolved:** 2019-10-23\n\n---\n\n## Resolution Summary\n\nThe resolution accepts the commenter's concern that the CRN IG's CDE mapping table may be incorrectly mapping adverse events and post-operative complications to the AdverseEvent resource. The AdverseEvent resource is primarily intended for causality determination and risk management, not simply recording clinical events that occurred.\n\nThe resolution requires this ticket to be addressed alongside FHIR-21016 (\"Remove AdverseEvent?\"). The approach is to:\n\n1. Determine whether each specific data element in the CDE mapping table is for **risk management** (causality assessment) or for **identification of \"what occurred\"** (clinical observation).\n2. Map data elements accordingly \u2014 risk management elements remain with AdverseEvent; clinical observation elements should use Condition or Observation instead.\n3. Contact the FDA POP Clinical Working Group to clarify data requirements and whether AdverseEvent must be retained, and if so, which data elements.\n4. Examine the FDA MDR adverse event codes (<https://www.fda.gov/medical-devices/mdr-adverse-event-codes/coding-resources>) to determine coding requirements.\n\nPer the FHIR-21016 resolution update (2019-08-16), the FDA clinical WG plans to collect complications or adverse events that occur during surgery, in the short term (0\u201330 days), from 30\u201390 days, and longer-term (>90 days) after surgery. A list of specific complications was developed during a Delphi process with the work group.\n\n## Feature Proposal\n\n### Problem Statement\n\nThe CRN IG's CDE (Common Data Element) mapping table maps adverse events and post-operative complications directly to the FHIR AdverseEvent resource. However, the AdverseEvent resource is designed for causality determination and risk management \u2014 not for simple tracking of clinical complications or conditions. The resource's scope includes cause-and-effect analysis, suspect entities, causality assessment methods, and entity relatedness evaluations. If the CRN's intent is simply to record \"what occurred\" (e.g., a surgical complication happened), then Condition or Observation may be more appropriate resources. Using the wrong resource leads to semantic inaccuracy and interoperability issues with other systems that correctly interpret AdverseEvent as a causality-assessment artifact.\n\n### Proposed Change\n\nReview and revise the CRN IG's CDE mapping table to correctly categorize adverse event data elements:\n\n1. **Retain AdverseEvent** for data elements that genuinely involve cau

... *(truncated, 16753 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\planned\BiomedicalResearchAndRegulation\FHIR-20789.md with 16499 characters
```

</details>


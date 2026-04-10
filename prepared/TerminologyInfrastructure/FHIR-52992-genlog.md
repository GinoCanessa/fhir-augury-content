# Session Log: FHIR-52992

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-52992.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-52992` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:36:44 UTC |
| **Duration** | 90s |
| **Total Tool Calls** | 12 |
| **Total Tokens** | 217,812 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-52992
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52992.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-52992", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-52992", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-52992", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52992.md
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
  "id": "FHIR-52992",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-52992: Document that in the absence of a concept property, the standards-status extension provides a property value

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Grahame Grieve
- **labels:** TEXTONLY
- **Created:** 2025-09-27T01:26:01+00:00
- **Updated:** 2026-01-20T04:55:18+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-52992

## Content
<p>In practice, we (HL7, in both core FHIR spec and THO) deprecate or retire concepts using the standards-status extension, but we do not document that it provides a status value in the absence of an explicit status. </p>

<p>We should do that. </p>

<p>Or explicitly document that it's an error to have a standards status of deprecated etc without an explicit status, and fix up any existing examples.</p>

## Comments (2)

### grahamegrieve — 2025-12-15T16:03:13+00:00
<p>Yes I intended that to apply to our code systems. but it should apply anywhere that extension is used - the kind of code system publishers that would use it should be bound to that rule </p>

<p> </p>

<p> </p>

### carmela_couderc — 2025-12-08T22:28:25+00:00
<p>Discussed on the 2025-12-08 TI Tracker call. </p>

<p>Does this apply to code systems owned by HL7 International? If not, HL7 shouldn't be setting the rules for how status is defined. HL7 doesn't have control over how code system publishers/owners define the status of the concepts. </p>

<p>SNOMED CT provides a model to follow. </p>

<p>What are the implications if the values of status and the extension are in conflict? </p>

<p>An option is to add a caution to the spec that its possible to create an inconsistent state. </p>

<p> </p>


## Snapshot
# FHIR-52992: Document that in the absence of a concept property, the standards-status extension provides a property value

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Grahame Grieve  
**Work Group:** Terminology Infrastructure  
**Specification:** FHIR Core (FHIR)  
**Labels:** TEXTONLY  
**Created:** 2025-09-27  
**Updated:** 2026-01-20  

## Description

<p>In practice, we (HL7, in both core FHIR spec and THO) deprecate or retire concepts using the standards-status extension, but we do not document that it provides a status value in the absence of an explicit status. </p>

<p>We should do that. </p>

<p>Or explicitly document that it's an error to have a standards status of deprecated etc without an explicit status, and fix up any existing examples.</p>

## Comments

### grahamegrieve (2025-12-15)

<p>Yes I intended that to apply to our code systems. but it should apply anywhere that extension is used - the kind of code system publishers that would use it should be bound to that rule </p>

<p> </p>

<p> </p>

### carmela_couderc (2025-12-08)

<p>Discussed on the 2025-12-08 TI Tracker call. </p>

<p>Does this apply to code systems owned by HL7 International? If not, HL7 shouldn't be setting the rules for how status is defined. HL7 doesn't have control over how code system publishers/owners define the status of the concepts. </p>

<p>SNOMED CT provides a model to follow. </p>

<p>What are the implications if the values of status and the extension are in conflict? </p>

<p>An option is to add a caution to the spec that its possible to create an inconsistent state. </p>

<p> </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-52992" (1 results)

- [zulip] 541764648 → [jira] FHIR-52992
  **Source:** [Terminology Service Test Cases] structuredefinition-standards-status
  **Type:** mentions
  **Context:** FHIR-52992 <p><a href="http://jira.hl7.org/browse/FHIR-52992">FHIR-52992</a></p>
  **Score:** 0.64
  **Updated:** 2025-09-27T01:26:09+00:00
**Warnings:**
- Value 'FHIR-52992' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 541764648 — [Terminology Service Test Cases] structuredefinition-standards-status
- **Score:** 0.64
- **Updated:** 2025-09-27T01:26:09+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Terminology%20Service%20Test%20Cases/topic/structuredefinition-standards-status/near/541764648
- **Snippet:** <b>FHIR-52992</b>


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52992.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-52992.md",
  "file_text": "# FHIR-52992: Document that in the absence of a concept property, the standards-status extension provides a property value\n\n## Summary\n\n| Field          | Value                                  |\n|----------------|----------------------------------------|\n| **Ticket**     | [FHIR-52992](https://jira.hl7.org/browse/FHIR-52992) |\n| **Type**       | Change Request                         |\n| **Priority**   | Medium                                 |\n| **Status**     | Triaged                                |\n| **Resolution** | Unresolved                             |\n| **Work Group** | Terminology Infrastructure             |\n| **Specification** | FHIR Core (FHIR)                   |\n| **Reporter**   | Grahame Grieve                         |\n| **Assignee**   | Unassigned                             |\n| **Labels**     | TEXTONLY                               |\n| **Created**    | 2025-09-27                             |\n| **Updated**    | 2026-01-20                             |\n\n## Description\n\nIn practice, HL7 (in both the core FHIR spec and THO) deprecates or retires concepts using the `structuredefinition-standards-status` extension, but there is no documentation stating that this extension provides a concept status value in the absence of an explicit `status` concept property.\n\nThe submitter proposes either:\n1. Documenting that the `standards-status` extension provides a status value when no explicit `status` concept property is present, **or**\n2. Explicitly documenting that it is an error to have a standards-status of \"deprecated\" etc. without an explicit `status` property, and fixing up existing examples that violate this rule.\n\n## Keywords\n\n`standards-status`, `concept property`, `status`, `deprecated`, `retired`, `CodeSystem`, `extension`, `structuredefinition-standards-status`, `concept status`, `THO`\n\n## Related Discussions\n\n### Zulip Conversations\n\n1. **[Terminology Service Test Cases > structuredefinition-standards-status](https://chat.fhir.org/#narrow/stream/Terminology%20Service%20Test%20Cases/topic/structuredefinition-standards-status)** (2025-09-27)\n   - **Origin of this ticket.** Michael Lawley asked whether it is documented that the `structuredefinition-standards-status` extension should set (or override) the value of a concept's status property. Grahame Grieve confirmed it is not documented but should be, and clarified it should **not** override an explicitly stated status property. Grahame then filed FHIR-52992.\n\n2. **[terminology > Deprecating Selected Codes in a Value Set](https://chat.fhir.org/#narrow/stream/terminology/topic/Deprecating%20Selected%20Codes%20in%20a%20Value%20Set)** (2023-08-03 to 2023-09-01)\n   - Extensive discussion about how to deprecate codes in code systems and value sets. Grahame indicated the `structuredefinition-standards-status` extension is the int

... *(truncated, 10648 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52992.md with 10442 characters
```

</details>


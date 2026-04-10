# Session Log: FHIR-46515

**Phase:** prepared
**Work Group:** Hl7AustraliaFhir
**Source File:** `prepared/Hl7AustraliaFhir/FHIR-46515.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-46515` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:58:32 UTC |
| **Duration** | 85s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 254,358 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-46515
## Work Group: HL7 Australia FHIR
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-46515.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-46515", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-46515", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-46515", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-46515.md
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
  "id": "FHIR-46515",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-46515: disable doNotPerform

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Australia FHIR
- **specification:** AU eRequesting (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Andy Bond
- **Created:** 2024-08-01T04:07:50+00:00
- **Updated:** 2024-08-15T03:23:32+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-46515

## Content
<p>doNotPerform is not relevant to our eRequesting use cases</p>

## Snapshot
# FHIR-46515: disable doNotPerform

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Andy Bond  
**Work Group:** HL7 Australia FHIR  
**Specification:** AU eRequesting (FHIR)  
**Created:** 2024-08-01  
**Updated:** 2024-08-15  

## Description

<p>doNotPerform is not relevant to our eRequesting use cases</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-46515".
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-46515.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7AustraliaFhir\\FHIR-46515.md",
  "file_text": "# FHIR-46515: disable doNotPerform\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-46515](https://jira.hl7.org/browse/FHIR-46515) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | AU eRequesting (FHIR) |\n| **Work Group** | HL7 Australia FHIR |\n| **Reporter** | Andy Bond |\n| **Assignee** | Unassigned |\n| **Created** | 2024-08-01 |\n| **Updated** | 2024-08-15 |\n\n## Description\n\nThe submitter requests that the `doNotPerform` element be disabled (constrained out) from the AU eRequesting ServiceRequest profiles. The rationale is that `doNotPerform` is not relevant to AU eRequesting use cases.\n\n`ServiceRequest.doNotPerform` is a boolean modifier element in the base FHIR ServiceRequest resource that, when set to `true`, indicates that the service/procedure should **not** be performed. The submitter's position is that this concept does not apply within the Australian eRequesting context, where service requests represent positive orders for diagnostic services.\n\n## Keywords\n\n`doNotPerform`, `ServiceRequest`, `AU eRequesting`, `modifier element`, `profile constraint`, `disable element`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-52405](https://jira.hl7.org/browse/FHIR-52405) | semantics of donotperform when false | Applied | Persuasive with Modification | Directly related \u2014 also by Andy Bond, addresses the unclear semantics of `doNotPerform` when set to `false` in AU eRequesting. This was resolved in block vote 2 with modification, suggesting the WG has already engaged with the semantics of this element. |\n| [FHIR-51764](https://jira.hl7.org/browse/FHIR-51764) | Correct the use of element shorts in eRequesting profiles | Resolved - No Change | Not Persuasive | Tangentially related \u2014 mentions `CommunicationRequest.doNotPerform` short descriptions in eRequesting profiles, indicating `doNotPerform` is present across multiple eRequesting profile types. |\n| [FHIR-46842](https://jira.hl7.org/browse/FHIR-46842) | eRequesting ServiceRequest or eRequesting Diagnostic ServiceRequest | Applied | Persuasive with Modification | Context \u2014 addresses the naming/scope of the eRequesting ServiceRequest profile that this ticket would modify. |\n\n## Related Zulip Discussions\n\nNo Zulip discussions were found that directly reference FHIR-46515.\n\nA broader search for `doNotPerform` surfaced a relevant Zulip thread in the **workflow** stream:\n\n- **[workflow > Task.doNotPerform FHIR-47394](https://chat.fhir.org/#narrow/stream/workflow/topic/Task.doNotPerform%20FHIR-47394)** (Oct 2025, 10 messages) \u2014 Discussion between Ralf Herzog, Bryn Rhodes, and Lloyd McKenzie about when `doNotPerform` is appropriate. Key takeaway

... *(truncated, 8046 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-46515.md with 7889 characters
```

</details>


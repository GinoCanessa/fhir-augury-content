# Session Log: FHIR-47939

**Phase:** prepared
**Work Group:** Hl7AustraliaFhir
**Source File:** `prepared/Hl7AustraliaFhir/FHIR-47939.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-47939` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:15:38 UTC |
| **Duration** | 93s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 223,055 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-47939
## Work Group: HL7 Australia FHIR
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-47939.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-47939", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-47939", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-47939", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-47939.md
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
  "id": "FHIR-47939",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-47939: Remove referencePolicy from AU Requester and AU Responder Capability Statements

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Australia FHIR
- **specification:** AU Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Heath Frankel
- **Created:** 2024-09-16T10:49:08+00:00
- **Updated:** 2024-11-19T23:18:48+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-47939

## Content
<p>There has been some confusion about the intent of the Reference Policy of Resolves in the AU Core Responder and AU Core Requester CapabilityStatement resources.</p>

<p>Through investigation <a href="https://www.hl7.org/fhir/references.html#logical" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/references.html#logical</a>, suggest that this is related to the capability of the server to support the Reference.identifier element and hence only relevant to the AU Core Responder CapabilityStatement. </p>

<p>Having tested this with Smile CDR (HAPI JPA Server) and significant investigation looking for configuration or usage documentation, it appears that it does not support the resolving of the Reference.identifier.</p>

<p>From documentation, it also appears that Google Cloud FHIR Server doesn't support it either.</p>

<p>Therefore, given that this is not supported by at least one of the most significant reference implementations I would suggest that resolves is to strong expectation even though it is only a SHOULD. I don't think this is something AU Core needs to specify at this time.</p>

<p>Recommendation</p>
<ol>
	<li>remove referencePolicy from each resource in AU Core Requester CapabilityStatement.</li>
	<li>remove referencePolicy from each resource in AU Core Responder CapabilityStatement, otherwise change value to 'logical'</li>
</ol>


## Comments (2)

### JIRAUSER22800 — 2024-10-28T10:30:47+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=GrahameGrieve" class="user-hover" rel="GrahameGrieve">Grahame Grieve</a> any chance you can provide some guidance on this item?</p>

<p>I have attempt to get input from Zulip a couple of times on this with no response, <a href="https://chat.fhir.org/#narrow/channel/179177-conformance/topic/CapabilityStatement.20referencePolicy" class="external-link" target="_blank" rel="nofollow noopener">https://chat.fhir.org/#narrow/channel/179177-conformance/topic/CapabilityStatement.20referencePolicy</a> and  <a href="https://chat.fhir.org/#narrow/channel/179177-conformance/topic/Meaning.20and.20use.20of.20referencePolicy.20in.20core.20IG.20CapabilityStat" class="external-link" target="_blank" rel="nofollow noopener">https://chat.fhir.org/#narrow/channel/179177-conformance/topic/Meaning.20and.20use.20of.20referencePolicy.20in.20core.20IG.20CapabilityStat</a>. </p>

<p>I have a sense that there is some limited understanding on this conformance element, At least If I can get some understanding on how it should be use then I can help articulate this to others rather than just following what the US are doing.</p>

### JIRAUSER25123 — 2024-09-20T03:00:27+00:00
<p>NOTE: Reference policy of 'resolves' required in US Core and IPA. IPS does not define a reference policy.</p>


## Snapshot
# FHIR-47939: Remove referencePolicy from AU Requester and AU Responder Capability Statements

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Heath Frankel  
**Work Group:** HL7 Australia FHIR  
**Specification:** AU Core (FHIR)  
**Created:** 2024-09-16  
**Updated:** 2024-11-19  

## Description

<p>There has been some confusion about the intent of the Reference Policy of Resolves in the AU Core Responder and AU Core Requester CapabilityStatement resources.</p>

<p>Through investigation <a href="https://www.hl7.org/fhir/references.html#logical" class="externa

... *(truncated, 6521 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-47939" (2 results)

- [jira] FHIR-47939 → [zulip] 179177:CapabilityStatement.20referencePolicy
  **Source:** Remove referencePolicy from AU Requester and AU Responder Capability Statements
  **Type:** mentions
  **Context:** ...ave attempt to get input from Zulip a couple of times on this with no response, https://chat.fhir.org/#narrow/channel/179177-conformance/topic/CapabilityStateme...
  **Score:** 0.51
  **Updated:** 2024-11-19T23:18:48+00:00
- [jira] FHIR-47939 → [zulip] 179177:Meaning.20and.20use.20of.20referencePolicy.20in.20core.20IG.20CapabilityStat
  **Source:** Remove referencePolicy from AU Requester and AU Responder Capability Statements
  **Type:** mentions
  **Context:** ...rrow/channel/179177-conformance/topic/CapabilityStatement.20referencePolicy and https://chat.fhir.org/#narrow/channel/179177-conformance/topic/Meaning.20and.20u...
  **Score:** 0.51
  **Updated:** 2024-11-19T23:18:48+00:00
**Warnings:**
- Value 'FHIR-47939' is not a valid Zulip message ID

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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-47939.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7AustraliaFhir\\FHIR-47939.md",
  "file_text": "# FHIR-47939: Remove referencePolicy from AU Requester and AU Responder Capability Statements\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-47939](https://jira.hl7.org/browse/FHIR-47939) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | AU Core (FHIR) |\n| **Work Group** | HL7 Australia FHIR |\n| **Reporter** | Heath Frankel |\n| **Assignee** | Unassigned |\n| **Created** | 2024-09-16 |\n| **Updated** | 2024-11-19 |\n\n## Description Summary\n\nThe reporter identifies confusion around the `referencePolicy` element (value `resolves`) in both the AU Core Responder and AU Core Requester CapabilityStatement resources. Key points:\n\n1. **Applicability concern:** The FHIR specification defines `referencePolicy` values in server-centric terms (\"The server will attempt to...\"), suggesting it is only meaningful for the AU Core Responder (server), not the AU Core Requester (client).\n2. **Implementation gap:** Testing with Smile CDR (HAPI JPA Server) revealed it does not support resolving `Reference.identifier` to `Reference.reference`. Google Cloud FHIR Server also appears to lack this capability.\n3. **Expectation too strong:** Even though conformance is only SHOULD, the reporter argues that `resolves` sets an overly ambitious expectation given major reference implementations do not support it.\n\n**Recommendation from reporter:**\n1. Remove `referencePolicy` from each resource in AU Core Requester CapabilityStatement.\n2. Remove `referencePolicy` from each resource in AU Core Responder CapabilityStatement, or alternatively change the value to `logical`.\n\n## Comments Summary\n\n- **JIRAUSER22800 (2024-10-28):** Requested guidance from Grahame Grieve. Noted two Zulip posts on the conformance stream received no responses. Expressed concern about limited community understanding of this conformance element and a desire to understand proper usage rather than simply following US Core's approach.\n- **JIRAUSER25123 (2024-09-20):** Noted that `resolves` referencePolicy is required in US Core and IPA, while IPS does not define a reference policy.\n\n## Keywords\n\n`referencePolicy`, `resolves`, `CapabilityStatement`, `AU Core`, `Reference.identifier`, `Reference.reference`, `logical`, `conformance`, `Responder`, `Requester`\n\n## Related Discussions\n\n### Zulip Threads\n\n1. **[conformance > CapabilityStatement referencePolicy](https://chat.fhir.org/#narrow/stream/conformance/topic/CapabilityStatement%20referencePolicy)** (2024-09-02)\n   - Heath Frankel asked about the expectations `referencePolicy` places on clients vs. servers. Questioned what to test for a server's read/search interactions and what to test for a client's interactions when `resolves` is specified. **No responses received.**\n\n2. **[conformance > Meaning and 

... *(truncated, 9060 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-47939.md with 8908 characters
```

</details>


# Session Log: FHIR-23061

**Phase:** prepared
**Work Group:** PatientCare
**Source File:** `prepared/PatientCare/FHIR-23061.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-23061` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:01:06 UTC |
| **Duration** | 98s |
| **Total Tool Calls** | 11 |
| **Total Tokens** | 242,896 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-23061
## Work Group: Patient Care
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-23061.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-23061", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-23061", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-23061", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-23061.md
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
  "id": "FHIR-23061",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-23061: Communication needs to explain the boundary between it and messaging

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Lloyd McKenzie
- **Created:** 2019-08-05T22:10:20+00:00
- **Updated:** 2024-08-13T22:34:32+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-23061

## Content
<p>Projects are starting to use Communication as equivalent to MessageHeader - which is a problem.  We need to clarify the scope of Communication and MessageHeader so that everyone knows when each should be used.</p>

<p>         As examples: Da Vinci PDex is using CommunicationRequest to ask for documentation to be shared and then Communication to document that the information was shared (and doing the sharing as part of that).  I think this is ok because it's happening at the provider level (providers asking for the data, providers prepping and providing the data.)</p>

<p>         Da Vinci Alerts, on the other hand, is using Communication within a Bundle to essentially do the equivalent of v2 ADT messages sending notifications that patient has been admitted, patient has been discharged, lab result has been received, prescription has been cancelled, etc.  That seems to be stepping squarely into the space expected to be covered by messaging.</p>

<p>         However, there is no guidance in MessageHeader, Communication or messaging section that explains what the boundaries are.  We desparately need to provide such language - and get consensus on what the boundaries should be.</p>

## Comments (5)

### michelle.m.miller — 2023-08-24T22:25:26+00:00
<p>Review current updates in spec</p>
<ul>
	<li><a href="http://build.fhir.org/communication.html#wrapping" class="external-link" target="_blank" rel="nofollow noopener">Communication - FHIR v6.0.0-cibuild</a></li>
	<li>Resolved JIRAs pending commits: <a href="https://jira.hl7.org/browse/FHIR-28235" class="external-link" rel="nofollow">https://jira.hl7.org/browse/FHIR-28235</a> </li>
</ul>


<p>Propose/draft additional boundaries between Communication and MessageHeader, if needed.</p>

### mckenzie — 2020-02-24T03:55:15+00:00
<p>This has been done - see <a href="https://docs.google.com/document/d/1OHfFcJ-OZvC81OFOOFudmcG3Lg5Wrrwo4n0dA09z40o/edit" class="external-link" target="_blank" rel="nofollow noopener">https://docs.google.com/document/d/1OHfFcJ-OZvC81OFOOFudmcG3Lg5Wrrwo4n0dA09z40o/edit</a></p>

### michelle.m.miller — 2019-10-03T14:03:13+00:00
<p>Related to <a href="https://gforge.hl7.org/gf/project/fhir/tracker/?action=TrackerItemEdit&amp;tracker_item_id=13389" class="external-link" target="_blank" rel="nofollow noopener">GF#13389</a> Clarify Communication Scope and Usage</p>

### michelle.m.miller — 2019-09-17T19:01:53+00:00
<p>+               <b>Patient Care WGM Tues Q3 (Sept 17, 2019) discussion</b>            +         </p>

<p>         Messaging is a framework that allows communicating a bunch of resources at once when query is not supported or has limitations (e.g. need to send all data that user might need at once), and event-driven or async responses (days or weeks later) - may not know the final endpoint.</p>

<p>         Communication is independent of paradigm (e.g. REST vs messaging).  Expose in clinical record that certain data has been communicated.  Can identify the specific data or describe the data in coded terms (e.g. smoking cessassion).  Because Communication can convey specific payload, it can also be used for transport in addition to record.  For example, existing implementations of Communication/CommunicationRequest used for secure email over FHIR.  Using Communication as a means for transport is useful, but no specific boundaries exist yet.</p>

<p>         However, Communication boundaries currently say "This resource is a record of a communication that has occurred. It 

... *(truncated, 18324 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-23061" (2 results)

- [jira] FHIR-23061 → [zulip] 179166:Messaging.20vs.2E.20Communication
  **Source:** Communication needs to explain the boundary between it and messaging
  **Type:** mentions
  **Context:** Discussion on https://chat.fhir.org/#narrow/stream/179166-implementers/topic/Messaging.20vs.2E...
  **Score:** 0.42
  **Updated:** 2024-08-13T22:34:32+00:00
- [zulip] 172543286 → [jira] FHIR-23061
  **Source:** [implementers] Messaging vs. Communication
  **Type:** mentions
  **Context:** I've just submitted a new tracker item ( GF#23061 ) seeking some clarification around the boundaries of using Messaging v...
  **Score:** 0.01
  **Updated:** 2019-08-05T22:17:17+00:00
**Warnings:**
- Value 'FHIR-23061' is not a valid Zulip message ID

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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-23061.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientCare\\FHIR-23061.md",
  "file_text": "# FHIR-23061: Communication needs to explain the boundary between it and messaging\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-23061](https://jira.hl7.org/browse/FHIR-23061) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | Patient Care |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter** | Lloyd McKenzie |\n| **Assignee** | Unassigned |\n| **Created** | 2019-08-05 |\n| **Updated** | 2024-08-13 |\n\n## Description\n\nProjects are starting to use the Communication resource as a functional equivalent to MessageHeader, which creates confusion about the intended scope of each resource. The ticket requests that the FHIR specification provide clear guidance on the boundaries between Communication and MessageHeader (messaging), so implementers know when to use each.\n\n**Examples cited:**\n- **Da Vinci PDex** uses CommunicationRequest to ask for documentation to be shared, then Communication to record that the information was shared. Lloyd considers this acceptable because it operates at the provider level.\n- **Da Vinci Alerts** uses Communication within a Bundle to send event-driven notifications (admission, discharge, lab results, prescription cancellation) \u2014 essentially replicating v2 ADT messages. This appears to overlap directly with the messaging paradigm.\n\nThe ticket observes that no guidance currently exists in MessageHeader, Communication, or the messaging section of the spec to differentiate these use cases.\n\n## Keywords\n\nCommunication, MessageHeader, messaging, CommunicationRequest, boundary, scope, Da Vinci, PDex, Alerts, ADT, notification, v2, Bundle, workflow, transport, record\n\n## Cross-References\n\n### Related Jira Tickets\n\n| Ticket | Title | Status | Relationship |\n|--------|-------|--------|-------------|\n| [FHIR-13389](https://jira.hl7.org/browse/FHIR-13389) | Clarify Communication Scope and Usage | Published (Persuasive with Modification) | Directly related \u2014 earlier ticket on the same scope-clarification topic. Referenced in FHIR-23061 comments. |\n| [FHIR-28235](https://jira.hl7.org/browse/FHIR-28235) | Consider rephrasing the text and explanation | Applied (Persuasive with Modification) | Addresses Communication intro text rephrasing. Referenced in FHIR-23061 comments as a resolved JIRA pending commits. |\n| [FHIR-40214](https://jira.hl7.org/browse/FHIR-40214) | Recommend change of wording: Communication should support sending correspondence co-occurring with the interaction | Applied (Persuasive with Modification) | Changed Communication intro to acknowledge it can represent actual flow of communication in some use cases (e.g., secure messaging). Referenced from FHIR-28235. |\n| [FHIR-26132](https://jira.hl7.org/browse/FHIR-26132) | Unsolicited notifications should be limited to d

... *(truncated, 10846 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-23061.md with 10654 characters
```

</details>


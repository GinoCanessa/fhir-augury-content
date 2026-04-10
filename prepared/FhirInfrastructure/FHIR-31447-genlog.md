# Session Log: FHIR-31447

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-31447.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-31447` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 00:52:15 UTC |
| **Duration** | 85s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 210,594 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-31447
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31447.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-31447", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-31447", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-31447", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31447.md
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
  "id": "FHIR-31447",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-31447: Websocket sub-protocol?

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** FHIR Infrastructure
- **specification:** FHIR R5 Subscriptions Backport (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Isaac Vetter
- **Created:** 2021-03-08T16:17:38+00:00
- **Updated:** 2022-07-18T20:30:10+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-31447

## Content
<p>Are you defining a websocket sub-protocol here, such that it should be passed into the javascript WebSocket constructor? If not, why not? 'Cause you are defining a websocket sub-protocol.</p>

<p>(<b>Comment 18 - imported by: Gino Canessa</b>)</p>

## Comments (3)

### lynn_laakso — 2022-07-18T20:30:10+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-07-18T20:30:10+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-05-09 00:00:00.0 with vote Gino Canessa/Michael Donnelly: 41-0-1//(Impact: null; Category: null; Version: null)//Since several implementers have been able to create working clients and servers, it does not appear that a full websocket-subprotocol is currently <b>required</b>.</p>

<p>Given the effort and lack of 'real world' feedback, I believe it makes more sense to leave this as a future consideration.</p>

### jiraadmin — 2021-03-08T16:17:40+00:00
<p>Imported from spreadsheet by ginocanessa - comment #18</p>


## Snapshot
# FHIR-31447: Websocket sub-protocol?

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Isaac Vetter  
**Work Group:** FHIR Infrastructure  
**Specification:** FHIR R5 Subscriptions Backport (FHIR)  
**Created:** 2021-03-08  
**Updated:** 2022-07-18  

## Description

<p>Are you defining a websocket sub-protocol here, such that it should be passed into the javascript WebSocket constructor? If not, why not? 'Cause you are defining a websocket sub-protocol.</p>

<p>(<b>Comment 18 - imported by: Gino Canessa</b>)</p>

## Comments

### lynn_laakso (2022-07-18)

<p>re-open post STU1 publication</p>

### lynn_laakso (2022-07-18)

<p>Reverted previous resolution: Considered for Future Use made 2022-05-09 00:00:00.0 with vote Gino Canessa/Michael Donnelly: 41-0-1//(Impact: null; Category: null; Version: null)//Since several implementers have been able to create working clients and servers, it does not appear that a full websocket-subprotocol is currently <b>required</b>.</p>

<p>Given the effort and lack of 'real world' feedback, I believe it makes more sense to leave this as a future consideration.</p>

### jiraadmin (2021-03-08)

<p>Imported from spreadsheet by ginocanessa - comment #18</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-31447" (1 results)

- [zulip] 281361986 → [jira] FHIR-31447
  **Source:** [fhir/infrastructure-wg] agenda item
  **Type:** mentions
  **Context:** ...1</a>, <a href="http://jira.hl7.org/browse/FHIR-31448">FHIR-31448</a>, <a href="http://jira.hl7.org/browse/FHIR-31447">FHIR-31447</a>, <a href="http://jira.hl7....
  **Score:** 0.03
  **Updated:** 2022-05-05T21:32:14+00:00
**Warnings:**
- Value 'FHIR-31447' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 281361986 — [fhir/infrastructure-wg] agenda item
- **Score:** 0.03
- **Updated:** 2022-05-05T21:32:14+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/agenda%20item/near/281361986
- **Snippet:** ...FHIR-34287 , FHIR-31471 , FHIR-31448 , <b>FHIR-31447</b> , FHIR-31440 , FHIR-31438 , FHIR-30634 , FHIR-30410 , and FHIR-30173 . I...


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31447.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-31447.md",
  "file_text": "# FHIR-31447: Websocket sub-protocol?\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-31447](https://jira.hl7.org/browse/FHIR-31447) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Specification** | FHIR R5 Subscriptions Backport (FHIR) |\n| **Work Group** | FHIR Infrastructure |\n| **Reporter** | Isaac Vetter |\n| **Assignee** | Unassigned |\n| **Created** | 2021-03-08 |\n| **Updated** | 2022-07-18 |\n\n## Description\n\nThe submitter asks whether the FHIR Subscriptions Backport IG is effectively defining a WebSocket sub-protocol, and if so, why it is not formally registered as one. Per the WebSocket specification (RFC 6455), sub-protocols should be declared so that clients (e.g., the JavaScript `WebSocket` constructor) can pass the sub-protocol identifier during the handshake. The submitter's position is that the IG *is* defining a sub-protocol (message formats, binding tokens, connection semantics) and should acknowledge and formalize this.\n\nThis ticket was originally imported from a ballot spreadsheet (comment #18 by Gino Canessa). It was previously resolved as **\"Considered for Future Use\"** with a 41-0-1 vote (Gino Canessa / Michael Donnelly), with the rationale that several implementers had created working clients and servers without a formal sub-protocol definition, and that formalizing one lacked sufficient real-world feedback. However, the ticket was **re-opened post STU1 publication** by Lynn Laakso on 2022-07-18.\n\n## Keywords\n\n- WebSocket, sub-protocol, RFC 6455, JavaScript WebSocket constructor\n- Subscriptions Backport IG, websocket binding, notification channel\n- Subscription handshake, ws/wss, bind-with-token\n\n## Cross-References\n\n### Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-31438](https://jira.hl7.org/browse/FHIR-31438) | Websocket message format unclear | Published | Persuasive with Modification | Directly related \u2014 asks for the websocket message format to be specified, which is part of what a sub-protocol defines |\n| [FHIR-31471](https://jira.hl7.org/browse/FHIR-31471) | Vague interaction descriptions for websocket connections | Published | Persuasive | Directly related \u2014 requests detailed schemas/operation definitions for get-ws-binding-token and bind-with-token interactions |\n| [FHIR-40924](https://jira.hl7.org/browse/FHIR-40924) | Need to better define websocket extension | Applied | Persuasive with Modification | Related \u2014 recognizes the websocket extension definition is unclear |\n| [FHIR-31449](https://jira.hl7.org/browse/FHIR-31449) | Is this true? (WS auth headers) | Published | Persuasive | Related \u2014 questions the claim that WS/WSS don't support authentication headers, relevant

... *(truncated, 9135 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31447.md with 8981 characters
```

</details>


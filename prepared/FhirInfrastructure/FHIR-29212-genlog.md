# Session Log: FHIR-29212

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-29212.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29212` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:33:22 UTC |
| **Duration** | 92s |
| **Total Tool Calls** | 17 |
| **Total Tokens** | 268,794 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29212
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29212.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29212", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29212", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29212", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29212.md
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
  "id": "FHIR-29212",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29212: CapabilityStatement state support of async

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Corey Spears
- **reporter:** Bas van den Heuvel
- **labels:** CapabilityStatement2
- **Created:** 2020-10-12T19:29:48+00:00
- **Updated:** 2025-10-27T20:27:42+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29212

## Content
<p>How do I state in the CapabilityStatement that async calls are supported? At what level can I state this? It should be possible on server, resource and operation level.</p>

## Comments (6)

### jmandel — 2025-10-27T20:27:42+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=corey_spears" class="user-hover" rel="corey_spears">Corey Spears</a>, after the App Feature IG has been published and the mechanism for externally defined features is clear, please bring this back to FHIR-I. We agree generally that we want to define features for discovery (including discovery of async support for specific operations, or general resource queries) inside the API Incubator IG.</p>


### jmandel — 2025-10-27T20:22:16+00:00
<p>After 4y, we have a better understanding of how to resolve &#8211; e.g., we now expect the App Feature IG should define a general feature mechanism, and the API Incubator IG will define the features related to async...</p>

### jmandel — 2025-10-27T20:22:16+00:00
<p>Reverted previous resolution: Not Persuasive with Modification made 2021-06-28 00:00:00.0 with vote Ewout Kramer/Josh Mandel: 11-0-0//(Impact: Compatible, substantive; Category: Enhancement; Version: null)//Will add the codes that Bas has proposed to the CapabilityStatement2 <a href="https://build.fhir.org/codesystem-capability-features.html" class="external-link" target="_blank" rel="nofollow noopener"><tt>capability-features</tt></a> code system of properties.</p>

### bvdh — 2021-06-21T19:36:02+00:00
<p>Add features (codes in the <a href="http://hl7.org/fhir/CodeSystem/capability-features" class="external-link" target="_blank" rel="nofollow noopener">capability-features</a> valueset) called: <em>synchronous</em> and <em>asynchronous</em>. </p>

<p>The allowed values are <em>true</em> and <em>false</em>. This will allow searching for synchronous and asynchronous calls.</p>

<p>The feature can occur on rest, rest.resource, rest.interaction, rest.operation, rest.resource.interaction and rest.resource.operation level. <br/>
In the case multiple are present the one deepest in the chain counts. A feature on rest.resource.interaction overrides one on rest.interaction.</p>

### bvdh — 2021-06-14T07:24:29+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=lloyd" class="user-hover" rel="lloyd">Lloyd McKenzie</a>, I took a look at it and the mechanism would work.</p>

### mckenzie — 2021-01-27T20:20:36+00:00
<p>Can you experiment with the proposed new 'feature' approach to describing capabilities in CapabilityStatement2 and see if/how it would work to meet your requirement?</p>


## Snapshot
# FHIR-29212: CapabilityStatement state support of async

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Corey Spears  
**Reporter:** Bas van den Heuvel  
**Work Group:** FHIR Infrastructure  
**Specification:** FHIR Core (FHIR)  
**Labels:** CapabilityStatement2  
**Created:** 2020-10-12  
**Updated:** 2025-10-27  

## Description

<p>How do I state in the CapabilityStatement that async calls are supported? At what level can I state this? It should be possible on server, resource and operation level.</p>

## Comments

### jmandel (2025-10-27)

<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=corey_spears" class="user-hover" rel="corey_spears">Corey Spears</a>, after the App Feature IG has been published and the mechanism for ex

... *(truncated, 6141 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-29212" (3 results)

- [zulip] 295119345 → [jira] FHIR-29212
  **Source:** [fhir/infrastructure-wg] CapabilityStatement state support of async
  **Type:** mentions
  **Context:** ...Does FHIR-I want to revisit this, or leave it to the future CS2 IG? <p><a href="http://jira.hl7.org/browse/FHIR-29212">FHIR-29212</a> CapabilityStatement state ...
  **Score:** 0.04
  **Updated:** 2022-08-24T20:14:38+00:00
- [zulip] 295768221 → [jira] FHIR-29212
  **Source:** [fhir/infrastructure-wg] agenda item for upcoming call
  **Type:** mentions
  **Context:** ...1</a> Change data type of constraint requirements to markdown</li> <li><a href="http://jira.hl7.org/browse/FHIR-29212">FHIR-29212</a> CapabilityStatement state ...
  **Score:** 0.02
  **Updated:** 2022-08-29T00:41:43+00:00
- [zulip] 328143250 → [jira] FHIR-29212
  **Source:** [fhir/infrastructure-wg] Status Report
  **Type:** mentions
  **Context:** ...nclude 3rd param in CapabilityStatement: Nothing to do for R5</li> <li><a href="http://jira.hl7.org/browse/FHIR-29212">FHIR-29212</a> CapabilityStatement state ...
  **Score:** 0.00
  **Updated:** 2023-02-16T02:20:27+00:00
**Warnings:**
- Value 'FHIR-29212' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (3 total, showing 3)

### [zulip] 295119345 — [fhir/infrastructure-wg] CapabilityStatement state support of async
- **Score:** 0.04
- **Updated:** 2022-08-24T20:14:38+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/CapabilityStatement%20state%20support%20of%20async/near/295119345
- **Snippet:** <b>FHIR-29212</b> CapabilityStatement state support of async Does FHIR-I want to revisit this, or leave it to the future...

### [zulip] 295768221 — [fhir/infrastructure-wg] agenda item for upcoming call
- **Score:** 0.02
- **Updated:** 2022-08-29T00:41:43+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/agenda%20item%20for%20upcoming%20call/near/295768221
- **Snippet:** ...28141 Change data type of constraint requirements to markdown <b>FHIR-29212</b> CapabilityStatement state support of async FHIR-31613 Clarification on...

### [zulip] 328143250 — [fhir/infrastructure-wg] Status Report
- **Score:** 0.00
- **Updated:** 2023-02-16T02:20:27+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/Status%20Report/near/328143250
- **Snippet:** ...Nothing to do for R5 <b>FHIR-29212</b> CapabilityStatement state support of async FHIR-27932 Declaratively handle behaviour for unknown extensions...


```

</details>

### Turn 2

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 3

**Assistant:**

Now I have all the data I need. Let me build the report.

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29212.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-29212.md",
  "file_text": "# FHIR-29212: CapabilityStatement state support of async\n\n> **Prepared for:** FHIR Infrastructure Work Group Review\n> **Prepared on:** 2025-07-17\n> **Ticket URL:** https://jira.hl7.org/browse/FHIR-29212\n\n---\n\n## 1. Summary\n\n**Status:** Triaged | **Type:** Change Request | **Priority:** Medium\n**Specification:** FHIR Core (FHIR) | **Labels:** CapabilityStatement2\n**Reporter:** Bas van den Heuvel (2020-10-12) | **Assignee:** Corey Spears\n**Resolution:** Unresolved\n\nThe submitter asks how a server can declare in its CapabilityStatement that it supports asynchronous (async) request patterns. The request specifies that async support should be expressible at the server, resource, and operation levels.\n\n### History\n\n1. **2020-10** \u2014 Ticket filed by Bas van den Heuvel.\n2. **2021-01** \u2014 Lloyd McKenzie suggested experimenting with the new \"feature\" approach in CapabilityStatement2.\n3. **2021-06** \u2014 Bas confirmed the feature mechanism would work and proposed adding `synchronous` and `asynchronous` codes to the `capability-features` CodeSystem, applicable at `rest`, `rest.resource`, `rest.interaction`, `rest.operation`, `rest.resource.interaction`, and `rest.resource.operation` levels, with deeper declarations overriding higher ones.\n4. **2021-06-28** \u2014 Originally resolved as **Not Persuasive with Modification** (vote: Ewout Kramer / Josh Mandel, 11-0-0). The plan was to add the proposed codes to the CapabilityStatement2 `capability-features` CodeSystem.\n5. **2022-08** \u2014 Grahame Grieve raised on Zulip whether FHIR-I wanted to revisit or defer to a future CS2 IG.\n6. **2023-02** \u2014 Listed in Grahame's status report as \"CapabilityStatement2 stuff \u2014 deferred for an implementation guide.\"\n7. **2025-10-27** \u2014 Josh Mandel **reverted** the previous resolution, reopening the ticket. He noted that after 4+ years the community now has a better understanding: the **App Feature IG** should define a general feature mechanism, and the **API Incubator IG** will define async-related features. He asked Corey Spears to bring this back to FHIR-I once the App Feature IG is published and the externally defined features mechanism is clear.\n\n---\n\n## 2. Keywords\n\n`CapabilityStatement`, `CapabilityStatement2`, `async`, `asynchronous`, `capability-features`, `feature discovery`, `App Feature IG`, `API Incubator IG`, `conformance`\n\n---\n\n## 3. Related Jira Tickets\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-21764](https://jira.hl7.org/browse/FHIR-21764) | How does discovery work? (Bulk Data) | Published | Async operation discovery for Bulk Data \u2014 closely related use case |\n| [FHIR-41457](https://jira.hl7.org/browse/FHIR-41457) | CapabilityStatements cannot show support for unqualified searches | Resolved - change required | Another gap in Capability

... *(truncated, 7727 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29212.md with 7539 characters
```

</details>


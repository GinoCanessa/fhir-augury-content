# Session Log: FHIR-31052

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-31052.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-31052` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 00:35:20 UTC |
| **Duration** | 105s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 299,170 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-31052
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31052.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-31052", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-31052", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-31052", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31052.md
````

---

## Agent Execution Log

### Turn 1

**Assistant:**

Let me fetch details on the most closely related tickets.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-31052: Remove scratchpad from spec, consolidate message groups

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** SMART Web Messaging (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Varghese Mathew
- **Created:** 2021-02-10T21:44:45+00:00
- **Updated:** 2021-03-05T17:31:07+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-31052

## Content
<p>The SMART Web Messaging spec introduces three or four types of message groups</p>
<ul>
	<li>scratchpad.*</li>
	<li>ui.*</li>
	<li>fhir.*</li>
	<li>status.* (??)</li>
</ul>


<p>These message groups are arbitrary, and I am struggling to see a useful purpose that they serve. In fact, I am worried they complicate rather than simplify the spec?</p>
<h1><a name="Scratchpad"></a>Scratchpad</h1>

<p>First off, the “scratchpad” group assumes an EHR “scratchpad”</p>
<ul>
	<li>This issue <a href="https://jira.hl7.org/browse/FHIR-29349" class="external-link" rel="nofollow">https://jira.hl7.org/browse/FHIR-29349</a> points out that it is unclear what is meant by a scratchpad.</li>
	<li>In this issue <a href="https://jira.hl7.org/browse/FHIR-29368" class="external-link" rel="nofollow">https://jira.hl7.org/browse/FHIR-29368</a> I have raised the concern that it doesn’t matter to the SMART App whether there is a scratchpad or not – that is an implementation detail that should not be baked into the specification.</li>
</ul>


<p>SMART Web Messaging spec started its journey from the PAMA use-case in CDS Hooks where a SMART on FHIR App that the CDS Hooks response launches may need to place or remove or update orders with UI integration. Remember that it is already possible to place or remove or update orders using the FHIR Create and Delete APIs on the FHIR Server. However, the missing piece was UI integration:</p>
<ul>
	<li>If a SMART App placed an order on the FHIR server, there is no UI indication that an order was placed. Whereas, the physician needs to be able to see it and be prompted to sign it.</li>
	<li>Likewise, if the App removed an order through the FHIR server, then there should be some indication to the physician that the order was removed.</li>
	<li>So also for updates for CDSM values etc.</li>
</ul>


<p>Broadening this from the PAMA use-case case, when actions like adding a problem, recording an allergy, recording vitals etc are done by a SMART App, it would again be desirable to have that UI integration for the EHR UI to indicate that something has happened.</p>

<p>This is the crucial advantage of SMART Web Messaging over the SMART App directly talking to the FHIR server.</p>

<p>So the messages should really be ui.create, ui.delete, ui.update.</p>

<p>Whether a scratchpad / shopping cart needs to be used is an implementation detail of the UI, and MUST NOT be part of the specification.</p>

<p>Some EHRs may have a scratchpad, some may not. Some EHRs may have scratchpads for certain resources (say orders) whereas no scratchpad for certain others (say Condition). Whether there is a scratchpad or not is really not relevant to the use-case and so to the spec.</p>

<p> </p>
<h1><a name="Status"></a>Status</h1>

<p>In the status group, there is currently only one message. It is really a status handshake with the EHR. So this message is more appropriately a ui.handshake (<em>or host.handshake, since what we really mean by UI is the EHR host</em>).</p>

<p>The question was raised what if there is a use-case for a handshake in the other direction. This is <b>semantically different</b> – the purpose of such a handshake or status check is very different from the current handshake (<em>which examines if the EHR host is capable of SMART Web Messaging and constitutes a registration for subsequent future interactions using SMART Web Messaging</em>). So such a status check from the host to the app should have a different message – perhaps guest.status or app.status

... *(truncated, 5629 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29356: Catelog mandatory?

- **status:** Published
- **type:** Change Request
- **priority:** Highest
- **work_group:** FHIR Infrastructure
- **specification:** SMART Web Messaging (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **Created:** 2020-10-21T19:01:27+00:00
- **Updated:** 2022-05-06T18:24:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29356

## Content
<p>Are only events from the Catelog allowed. Do clients have to implement them?</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The activityType property conveys an activity type drawn from the SMART Web Messaging Activity Catalog</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-28473: Ballot Feedback: "Discovery of Server Capabilities"

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** SMART Web Messaging (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Jenni Syed
- **Created:** 2020-09-10T17:41:31+00:00
- **Updated:** 2022-05-06T18:24:15+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-28473

## Content
<p><a href="http://hl7.org/fhir/uv/smart-web-messaging/2020Sep/index.html#discovery-of-server-capabilities" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/smart-web-messaging/2020Sep/index.html#discovery-of-server-capabilities</a></p>

<p>.well-known/smart-configuration is an appropriate location for advertising a level of protocol support (supported message types, activity types, and activityParameters), but at the point of publication we're not sure there are apps trying to flex capabilities by EHR.</p>

```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-31052",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-31052: Remove scratchpad from spec, consolidate message groups

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** SMART Web Messaging (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Varghese Mathew
- **Created:** 2021-02-10T21:44:45+00:00
- **Updated:** 2021-03-05T17:31:07+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-31052

## Content
<p>The SMART Web Messaging spec introduces three or four types of message groups</p>
<ul>
	<li>scratchpad.*</li>
	<li>ui.*</li>
	<li>fhir.*</li>
	<li>status.* (??)</li>
</ul>


<p>These message groups are arbitrary, and I am struggling to see a useful purpose that they serve. In fact, I am worried they complicate rather than simplify the spec?</p>
<h1><a name="Scratchpad"></a>Scratchpad</h1>

<p>First off, the “scratchpad” group assumes an EHR “scratchpad”</p>
<ul>
	<li>This issue <a href="https://jira.hl7.org/browse/FHIR-29349" class="external-link" rel="nofollow">https://jira.hl7.org/browse/FHIR-29349</a> points out that it is unclear what is meant by a scratchpad.</li>
	<li>In this issue <a href="https://jira.hl7.org/browse/FHIR-29368" class="external-link" rel="nofollow">https://jira.hl7.org/browse/FHIR-29368</a> I have raised the concern that it doesn’t matter to the SMART App whether there is a scratchpad or not – that is an implementation detail that should not be baked into the specification.</li>
</ul>


<p>SMART Web Messaging spec started its journey from the PAMA use-case in CDS Hooks where a SMART on FHIR App that the CDS Hooks response launches may need to place or remove or update orders with UI integration. Remember that it is already possible to place or remove or update orders using the FHIR Create and Delete APIs on the FHIR Server. However, the missing piece was UI integration:</p>
<ul>
	<li>If a SMART App placed an order on the FHIR server, there is no UI indication that an order was placed. Whereas, the physician needs to be able to see it and be prompted to sign it.</li>
	<li>Likewise, if the App removed an order through the FHIR server, then there should be some indication to the physician that the order was removed.</li>
	<li>So also for updates for CDSM values etc.</li>
</ul>


<p>Broadening this from the PAMA use-case case, when actions like adding a problem, recording an allergy, recording vitals etc are done by a SMART App, it would again be desirable to have that UI integration for the EHR UI to indicate that something has happened.</p>

<p>This is the crucial advantage of SMART Web Messaging over the SMART App directly talking to the FHIR server.</p>

<p>So the messages should really be ui.create, ui.delete, ui.update.</p>

<p>Whether a scratchpad / shopping cart needs to be used is an implementation detail of the UI, and MUST NOT be part of the specification.</p>

<p>Some EHRs may have a scratchpad, some may not. Some EHRs may have scratchpads for certain resources (say orders) whereas no scratchpad for certain others (say Condition). Whether there is a scratchpad or not is really not relevant to the use-case and so to the spec.</p>

<p> </p>
<h1><a name="Status"></a>Status</h1>

<p>In the status group, there is currently only one message. It is really a status handshake with the EHR. So this message is more appropriately a ui.handshake (<em>or host.handshake, since what we really mean by UI is the EHR host</em>).</p>

<p>The question was raised what if there is a use-case for a handshake in the other direction. This is <b>semantically different</b> – the purpose of such a handshake or status check is very different from the current handshake (<em>which examines if the EHR host is capable of SMART Web Messaging and constitutes a registration for subsequent future interactions using SMART Web Messaging</em>). So such a status check from the host to the app should have a different message – perhaps guest.status or app.status

... *(truncated, 11758 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-31052" (3 results)

- [jira] FHIR-31052 → [github] HL7/smart-web-messaging#41
  **Source:** Remove scratchpad from spec, consolidate message groups
  **Type:** mentions
  **Context:** I have created PR https://github.com/HL7/smart-web-messaging/pull/41 for this change.
  **Score:** 0.07
  **Updated:** 2021-03-05T17:31:07+00:00
- [zulip] 226672219 → [jira] FHIR-31052
  **Source:** [smart] Web messaging, scratchpad
  **Type:** mentions
  **Context:** Well, my issue already documents this - https://jira.hl7.org/browse/FHIR-31052 <p>Well, my issue already documents this ...
  **Score:** 0.02
  **Updated:** 2021-02-17T15:25:22+00:00
- [zulip] 226204305 → [jira] FHIR-31052
  **Source:** [implementers] FHIR, Scratchpad, SMART Web Messaging, and unfinalized in...
  **Type:** mentions
  **Context:** For reference, the original JIRA issue I wrote up: https://jira.hl7.org/browse/FHIR-31052 <p>For reference, the original JIRA issue...
  **Score:** 0.00
  **Updated:** 2021-02-12T22:22:11+00:00
**Warnings:**
- Value 'FHIR-31052' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (2 total, showing 2)

### [zulip] 226672219 — [smart] Web messaging, scratchpad
- **Score:** 0.02
- **Updated:** 2021-02-17T15:25:22+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/smart/topic/Web%20messaging%2C%20scratchpad/near/226672219
- **Snippet:** Well, my issue already documents this - https://jira.hl7.org/browse/<b>FHIR-31052</b>

### [zulip] 226204305 — [implementers] FHIR, Scratchpad, SMART Web Messaging, and unfinalized in...
- **Score:** 0.00
- **Updated:** 2021-02-12T22:22:11+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/FHIR%2C%20Scratchpad%2C%20SMART%20Web%20Messaging%2C%20and%20unfinalized%20in.../near/226204305
- **Snippet:** For reference, the original JIRA issue I wrote up: https://jira.hl7.org/browse/<b>FHIR-31052</b>


```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31052.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-31052.md",
  "file_text": "# FHIR-31052: Remove scratchpad from spec, consolidate message groups\n\n## Ticket Summary\n\n| Field | Value |\n|---|---|\n| **Key** | [FHIR-31052](https://jira.hl7.org/browse/FHIR-31052) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | FHIR Infrastructure |\n| **Specification** | SMART Web Messaging (FHIR) |\n| **Reporter** | Varghese Mathew |\n| **Assignee** | Unassigned |\n| **Created** | 2021-02-10 |\n| **Updated** | 2021-03-05 |\n\n## Description Summary\n\nThe reporter proposes two major changes to the SMART Web Messaging specification:\n\n1. **Remove the \"scratchpad\" concept entirely** \u2014 The scratchpad assumes an EHR-specific implementation detail (an in-memory holding area for draft resources). Whether an EHR uses a scratchpad, shopping cart, or persists draft resources directly to a FHIR server should not be dictated by the specification. The reporter argues the specification should remain silent on this, much as the base FHIR spec does.\n\n2. **Consolidate message groups into three roles** \u2014 The current spec defines multiple message groups (`scratchpad.*`, `ui.*`, `fhir.*`, `status.*`) that the reporter sees as arbitrary and unnecessarily complex. The proposed replacement is:\n   - **`ui.*` (or `host.*`)** \u2014 Messages from the App invoking the EHR host (e.g., `ui.create`, `ui.delete`, `ui.update`, `ui.handshake`)\n   - **`app.*` (or `guest.*`)** \u2014 Messages from the EHR host invoking the App\n   - **`fhir.*`** \u2014 Special case where the EHR host acts as a FHIR proxy on behalf of the App\n\nThe reporter acknowledges this is a significant breaking change and suggests it may not be part of an immediate ballot.\n\n## Keywords\n\n`SMART Web Messaging`, `scratchpad`, `message groups`, `EHR`, `CDS Hooks`, `postMessage`, `ui integration`, `FHIR proxy`, `draft orders`, `PAMA`\n\n## Related Jira Tickets\n\n### FHIR-29349 \u2014 Scratchpad undefined\n- **Status:** Published | **Resolution:** Persuasive with Modification | **Priority:** Highest\n- **Reporter:** Bas van den Heuvel\n- **Relevance:** Directly referenced in FHIR-31052. Requests a definition of \"scratchpad\" \u2014 what data is present and when. The current ticket argues that removing the scratchpad concept entirely would make this issue moot.\n\n### FHIR-29368 \u2014 I'm struggling with the notion of scratchpad\n- **Status:** Resolved - No Change | **Resolution:** Not Persuasive | **Priority:** Highest\n- **Reporter:** Varghese Mathew (same reporter as FHIR-31052)\n- **Relevance:** Also directly referenced. An earlier expression of the same concern \u2014 that from the SMART App's perspective the scratchpad is an EHR implementation detail, and messages should just be `fhir.*`. This ticket was resolved as Not Persuasive, meaning the work group previously decided agai

... *(truncated, 10660 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-31052.md with 10446 characters
```

</details>


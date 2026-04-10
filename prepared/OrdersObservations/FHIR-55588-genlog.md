# Session Log: FHIR-55588

**Phase:** prepared
**Work Group:** OrdersObservations
**Source File:** `prepared/OrdersObservations/FHIR-55588.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `52256f69-5fb6-416b-be46-75c24182f098` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-55588` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 14:09:41 UTC |
| **Duration** | 75s |
| **Total Tool Calls** | 8 |
| **Total Tokens** | 207,857 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-55588
## Work Group: Orders & Observations
## Output File: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-55588.md

## Data Access
Use FhirAugury MCP tools (preferred) or CLI fallback at: C:\ai\git\fhir-augury\src\FhirAugury.Cli\bin\Release\net10.0\FhirAugury.Cli.exe

## Steps
1. Gather in parallel: FhirAugury-get_item(source="jira", id="FHIR-55588", includeComments=true, includeContent=true, includeSnapshot=true) AND FhirAugury-cross_referenced(value="FHIR-55588", limit=50)
2. Fetch Related Jira Tickets for each Jira cross-reference.
3. Fetch Zulip threads for each Zulip cross-reference + FhirAugury-content_search(values="FHIR-55588", sources="zulip", limit=10)
4. Note GitHub Items
5. Build Report with standard template and three dispositions.

## Rules: Use ONLY data from MCP/CLI. Be specific. Recommendation must pick one.
## Save to the output file path above.
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
  "id": "FHIR-55588",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-55588: How can we handle a “Fulfiller-proposed alternative/continuation/addition”?

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** Clinical Order Workflow (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Jose Costa-Teixeira
- **labels:** COW
- **Created:** 2026-02-03T20:20:53+00:00
- **Updated:** 2026-02-27T18:24:39+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-55588

## Content
<p>At fulfillment, we can have some requests to do additional procedures (or alternatives, or continuation)<br/>
What are the elements, resources and references between those? <br/>
.basedOn the original request? Do we fill Task.output?<br/>
Scenarios</p>
<ul>
	<li>Nurse can just authorize an order</li>
	<li>Nurse does something from protocol, which implies a (implicitly approved) order</li>
	<li>Nurse needs an order to be authorized</li>
</ul>


## Comments (1)

### costateixeira — 2026-02-16T17:36:58+00:00
<p>Clarify the linkage between orders - considering triggeredBy / .reason (explaining why / why not).<br/>
Check for upstream or downstream impact from/on other patterns<br/>
Add an example. Something like<br/>
Nurse was requested to do wound care. While doing that, they realize the patient has an acute infection and requests analgesics.</p>


## Snapshot
# FHIR-55588: How can we handle a “Fulfiller-proposed alternative/continuation/addition”?

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Jose Costa-Teixeira  
**Work Group:** Orders & Observations  
**Specification:** Clinical Order Workflow (FHIR)  
**Labels:** COW  
**Created:** 2026-02-03  
**Updated:** 2026-02-27  

## Description

<p>At fulfillment, we can have some requests to do additional procedures (or alternatives, or continuation)<br/>
What are the elements, resources and references between those? <br/>
.basedOn the original request? Do we fill Task.output?<br/>
Scenarios</p>
<ul>
	<li>Nurse can just authorize an order</li>
	<li>Nurse does something from protocol, which implies a (implicitly approved) order</li>
	<li>Nurse needs an order to be authorized</li>
</ul>


## Comments

### costateixeira (2026-02-16)

<p>Clarify the linkage between orders - considering triggeredBy / .reason (explaining why / why not).<br/>
Check for upstream or downstream impact from/on other patterns<br/>
Add an example. Something like<br/>
Nurse was requested to do wound care. While doing that, they realize the patient has an acute infection and requests analgesics.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-55588" (2 results)

- [jira] FHIR-55588 → [fhir] Task.output
  **Source:** How can we handle a “Fulfiller-proposed alternative/continuation/addition”?
  **Type:** mentions
  **Context:** ...sources and references between those? .basedOn the original request? Do we fill Task.output? Scenarios Nurse can just authorize an order Nurse does something fr...
  **Score:** 0.99
  **Updated:** 2026-02-27T18:24:39+00:00
- [zulip] 578941201 → [jira] FHIR-55588
  **Source:** [workflow] Intent-driven interaction
  **Type:** mentions
  **Context:** ...t the backend handle the logic.</p> <ol> <li> <p>We have that in scope <a href="https://jira.hl7.org/browse/FHIR-55588">FHIR-55588</a>- I would guess we're look...
  **Score:** 0.99
  **Updated:** 2026-03-12T14:39:08+00:00
**Warnings:**
- Value 'FHIR-55588' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 578941201 — [workflow] Intent-driven interaction
- **Score:** 0.99
- **Updated:** 2026-03-12T14:39:08+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/workflow/topic/Intent-driven%20interaction/near/578941201
- **Snippet:** ...We have that in scope <b>FHIR-55588</b> - I would guess we're looking at an order with intent proposal - we...


```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# workflow > Intent-driven interaction

**Messages:** 5
**First message:** 2026-03-12 08:10:00+00:00
**Last message:** 2026-03-12 20:28:47+00:00
**Participants:** Lionel Cremer, Jose Costa Teixeira, Lloyd McKenzie

## Messages

### Lionel Cremer — 2026-03-12 08:10:00+00:00
Hi, We are designing a FHIR-based API where client applications express user intentions rather than directly manipulating resources. An intention represents a user action (e.g. approve, reject, complete) that may result in updates to one or several FHIR resources. Architecture Our architecture separates the FHIR interface from the backend domain logic: a FHIR Gateway exposing the FHIR API FHIR-agnostic backend services implementing the business logic The backend persists domain resources (e.g. Prescription (ServiceRequest), Professional Assignment (Task), etc.), but user intentions themselves are not stored as resources and therefore do not have a lifecycle. Objectives In practice, a single user intention may result in: updating the status of one or several resources updating resource content creating new resources completing workflow items Example use cases 1. Proposal review Nurse creates a care proposal Physician reviews the proposal Physician approves or rejects the proposal (a note may be added by the physician) This may result in: creating a new prescription + a new assignment (nurse who initiated the proposal is assigned to the prescription) adding a note to the proposal completing workflow tasks around the proposal 2. Completion of treatment A caregiver completes his part of a treatment (multiple caregivers can be assigned on the same prescription). The caregiver can also explicitly indicate that all the treatment is done and the prescription should be marked as completed. This results in: completing a Task (the one from the caregiver) optionally, if explicitly requested, completing the associated prescription 3. Radiology prescription evaluation A radiologist evaluates a prescription and may: approve the requested exam substitute the exam by another reject the request, resulting to the revocation of the prescription Question What FHIR workflow pattern would be most appropriate to represent these kinds of intent-driven interactions where a user action may trigger coordinated updates across several resources? Especially when the user action itself is not persisted as a resource.

### Jose Costa Teixeira — 2026-03-12 14:39:08+00:00
If backend services are fhir-agnostic, you can express them as "normal" FHIR content, and then let the backend handle the logic. We have that in scope FHIR-55588 - I would guess we're looking at an order with intent proposal - we had some discussion, possibly a Task to "please create"? We can confirm and get back to you This seems a request to mark something as completed, right? the caregiver doesn't automatically change the authorization, they signal to the placer that they intend this is marked as completed. FHIR-56051 the radiologist may reject their fulfillment AND request the revocation of the authorization. We have that as an explicit use case for COW - https://build.fhir.org/ig/HL7/fhir-cow-ig/en/StructureDefinition-cancellation-request-task.html . This is what gets exchanged - which seems compatible with your statement that the backend services and logic are FHIR-agnostic

### Lloyd McKenzie — 2026-03-12 15:17:13+00:00
I'm not completely clear what's meant by "user intentions are not stored". You don't retain a record of the fact that someone proposed a therapy, proposed changing the status of a resource, etc.? In any case, I agree with Jose that the processes you've described can be handled via standard RESTful interfaces with the combination of different Request 'intents' and the appropriate use of Task. And you'll get better interoperability that way than by inventing custom operations, messages, etc.

### Lionel Cremer — 2026-03-12 18:54:28+00:00
Thanks @Lloyd McKenzie , let me clarify what I m

... *(truncated, 7305 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-55588
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| continuation | word | 3 | 12.875 |
| nurse | word | 3 | 10.294 |
| fulfiller | word | 2 | 9.847 |
| task.output | fhir_path | 1 | 7.924 |
| alternative | word | 3 | 7.478 |
| output | word | 2 | 7.011 |
| authorize | word | 2 | 6.981 |
| cow | word | 1 | 6.767 |
| implicitly | word | 1 | 6.509 |
| fulfillment | word | 1 | 5.992 |
| handle | word | 2 | 5.569 |
| task | fhir_path | 2 | 5.564 |
| basedon | word | 1 | 5.454 |
| fill | word | 1 | 5.400 |
| order | word | 3 | 5.321 |
| addition | word | 2 | 5.258 |
| protocol | word | 1 | 4.978 |
| li | word | 6 | 4.672 |
| original | word | 1 | 4.341 |
| imply | word | 1 | 4.339 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-55588.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\OrdersObservations\\FHIR-55588.md",
  "file_text": "# FHIR-55588: How can we handle a \"Fulfiller-proposed alternative/continuation/addition\"?\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-55588](https://jira.hl7.org/browse/FHIR-55588) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | Clinical Order Workflow (FHIR) |\n| **Work Group** | Orders & Observations |\n| **Reporter** | Jose Costa-Teixeira |\n| **Assignee** | Unassigned |\n| **Labels** | COW |\n| **Created** | 2026-02-03 |\n| **Updated** | 2026-02-27 |\n\n## Description\n\nThis ticket asks how to model the situation where, during fulfillment of an order, the fulfiller identifies the need for **additional, alternative, or continuation procedures**. The ticket raises the following questions:\n\n- What FHIR elements, resources, and references should link the new request to the original order?\n- Should `ServiceRequest.basedOn` reference the original request?\n- Should `Task.output` be used to capture the fulfiller's proposal?\n\nThree scenarios are presented:\n1. A nurse can directly authorize an order.\n2. A nurse acts from protocol, implying an (implicitly approved) order.\n3. A nurse identifies a need but requires an order to be authorized by a physician.\n\n## Reporter's Comment (2026-02-16)\n\nJose Costa-Teixeira added guidance for resolution:\n- Clarify the **linkage between orders**, particularly using `triggeredBy` and `.reason` to explain why the new order was created.\n- Check for upstream or downstream impact on other COW patterns.\n- Add an **example scenario**: e.g., a nurse performing wound care realizes the patient has an acute infection and requests analgesics.\n\n## Keywords\n\n`continuation`, `fulfiller`, `alternative`, `Task.output`, `authorize`, `basedOn`, `order`, `protocol`, `fulfillment`, `COW`\n\n## Cross-References\n\n### FHIR Elements\n- **Task.output** \u2014 mentioned in the ticket description as a potential carrier for the fulfiller's proposed action.\n\n### Related Jira Tickets\n- **[FHIR-56051](https://jira.hl7.org/browse/FHIR-56051)** \u2014 *Clarify the use of Task to request order status changes* (Applied, Persuasive with Modification). This closely related ticket adds a generic mechanism for using Task to request status changes on orders (e.g., cancellation, completion). It proposes adding a Task profile and an example for \"please mark this as complete\" workflows. Both tickets address how Task mediates communication between fulfiller and placer.\n\n### Zulip Discussions\n- **[workflow > Intent-driven interaction](https://chat.fhir.org/#narrow/stream/workflow/topic/Intent-driven%20interaction)** (2026-03-12, 5 messages, participants: Lionel Cremer, Jose Costa Teixeira, Lloyd McKenzie). A community member asked about modeling intent-driven interactions where a single user action t

... *(truncated, 7670 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-55588.md with 7508 characters
```

</details>


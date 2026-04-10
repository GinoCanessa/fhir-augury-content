# Session Log: FHIR-48395

**Phase:** prepared
**Work Group:** OrdersObservations
**Source File:** `prepared/OrdersObservations/FHIR-48395.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-48395` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 01:36:48 UTC |
| **Duration** | 115s |
| **Total Tool Calls** | 17 |
| **Total Tokens** | 307,250 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-48395
## Work Group: Orders & Observations
## Output File: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-48395.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-48395", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-48395", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-48395", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-48395.md
````

---

## Agent Execution Log

### Turn 1

**Assistant:**

Let me fetch the most relevant related tickets and the Zulip thread.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-48395: Mechanism to request device settings changes

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** OO Incubator (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Joint-OO-PC, OO, Ready-to-Discuss, WGM-September-2025
- **Created:** 2024-09-25T12:57:30+00:00
- **Updated:** 2026-02-02T20:59:49+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48395

## Content
<p>A request was recieved from <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=chuscmi" class="user-hover" rel="chuscmi">Stephen Chu</a> to be able to request device settings changes.</p>

<p>Currently you can define a task or service request to get a person to change the settings on a device, but there isn't a defined mechanism to request those changes of the device itself.</p>

<p>We need a way to represent requested settings in a structured representation; a way to convey the request to the device (perhaps profiling or modifying Task, and/or defining an operation on Device). We will also need to be able to track requested settings, pending settings, as-applied settings, etc.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-39688: Device resource needs semantically accurate structure for setting device function parameters

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Stephen Chu
- **labels:** DeviceSettings, HCP, Joint-OO-PC, Ready-to-Discuss, WGM-January2026
- **Created:** 2022-12-23T03:25:48+00:00
- **Updated:** 2026-02-02T20:44:45+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-39688

## Content
<p>Devices (external | implantable), such as insulin infusion pump, implantable cardioverter-defibrillator, need to be programmed to operate correctly based on patient's clinical status. For example:<br/>
Insulin infusion pump dosage - basal and bolus dosage<br/>
Implantable cardioverter-defibrillator (ICD) - pacing mode<br/>
These device function parameters may also need to be adjusted from time to time, based on changing patient clinical status<br/>
The initial setting and subsequent parameters adjustments need to be captured for reasons including: decision traceability, evaluation of parameter setting clinical effectiveness, to inform future device function parameter setting, etc</p>

<p>A detail analysis of the FHIR Device (and Device related) resources lead to the assessment that these requirements are not supported by the current Device resource structure.<br/>
This change request is to suggest a detail review of the requirements and to determine the optimal change decision(s).<br/>
An analysis document is uploaded to provide more detail use cases analysis and contextual information to support this change request.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-38917: Add example of and/or guidance on how to associate device settings with clinical observations

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Device-module, HCP, OO, Pending-SME-Input
- **Created:** 2022-10-12T04:21:08+00:00
- **Updated:** 2026-02-02T20:25:16+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-38917

## Content
<p>There seems to be a range of opinions on how to associate clinical observations generated by devices with the settings in effect on the device at the time the clinical observation was made. Associating the device settings and clinical observations is important to provide context for the clinical observations, and to provide historical evidence. </p>

<p>Some have suggested that the clinical observation should use hasMember relationships to the settings observations (either directly or indirectly through a "settings set" observation). This has the advantage of unambiguously tying the clinical observation to the settings in effect.</p>

<p>Others have suggested simply recording the settings observations either when they change, or at defined times (daily at noon, at the start of a procedure, etc.) and recording the clinical observations without regard for the settings; the settings in effect for any clinical observation can be determined by finding the most recent setting observations (for each of the device metrics) prior to the clinical observation. This approach doesn't laden the clinical observations with concern over the settings observations; but makes it more difficult to detect a missing/deleted setting.</p>

<p>There is also some confusion about the difference between device settings (recorded as Observations linked to DeviceMetrics linked to Devices) and device properties, and in general how to record device settings.</p>

<p>An example or guidance that ties these all together, perhaps starting with a clinical Observation linking to settings Observations, would help provide a common approach to these challenges. </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-46963: Misguidance on how to represent device settings

- **status:** Applied
- **type:** Change Request
- **priority:** Highest
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Javier Espina
- **labels:** R6-Text
- **Created:** 2024-09-04T09:26:00+00:00
- **Updated:** 2025-03-12T17:52:11+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-46963

## Content
<p>It is my understanding that device settings (that are not essentially static) should be represented with Observation, where both .subject and .device refer to the device to which the settings apply. This is not reflected by the text "To track changes in settings, Observation resource can be used, where Observation has the subject <b>(e.g., patient)</b>, device, and time window that enable to relate to the proper DeviceAssociation or vice-versa".</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-39322: Device.property definition overlaps with DeviceMetric and Observation

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Marti Velezis
- **reporter:** Elliot Silver
- **labels:** OO, Pending-SME-Input
- **Created:** 2022-10-24T18:15:15+00:00
- **Updated:** 2025-07-14T22:13:37+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-39322

## Content
<p>The current definition of Device.property is:</p>
<blockquote><p>Characteristics or features of the device that are otherwise not captured in available attributes, e.g., actual configuration settings, time or timing attributes, resolution, accuracy, and physical attributes. The focus is on properties of the device actually in use while DeviceDefinition focuses on properties that are available to be used.</p></blockquote>
<p>The R4 definition is simply the first sentence.</p>

<p>Previously I understood that property was intended to capture "fixed" properties (this is a "large" blood pressure cuff, this bed can support up to 900 lbs, the resolution of this MRI is up to <span class="error">&#91;some number&#93;</span>). However, inclusion of "actual configuration settings" and "properties of the device actually in use" leads me to think that the intent is to record the value of dynamic settings in effect at any time. If that is the case, there is overlap and confusion about the role of DeviceMetric (does device metric define a property?), and of "settings" Observations, which refer to those metrics. In my mind, DeviceMetric records the existence of a setting (there is a knob to adjust the volume) and a "setting" Observation captures the value of that setting at a point in time (our volume is 11). However, property seems to be described as supporting the "settings" Observation behavior. If that is the case, clarify how to record a device setting at a point in time, and track changes to that setting over time.</p>

<p>The boundaries and use of these resources, and elements needs to be cleared up.</p>

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
No messages found in stream 'implementers', topic 'History of device settings/properties'.
```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-48395",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-48395: Mechanism to request device settings changes

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** OO Incubator (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Joint-OO-PC, OO, Ready-to-Discuss, WGM-September-2025
- **Created:** 2024-09-25T12:57:30+00:00
- **Updated:** 2026-02-02T20:59:49+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48395

## Content
<p>A request was recieved from <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=chuscmi" class="user-hover" rel="chuscmi">Stephen Chu</a> to be able to request device settings changes.</p>

<p>Currently you can define a task or service request to get a person to change the settings on a device, but there isn't a defined mechanism to request those changes of the device itself.</p>

<p>We need a way to represent requested settings in a structured representation; a way to convey the request to the device (perhaps profiling or modifying Task, and/or defining an operation on Device). We will also need to be able to track requested settings, pending settings, as-applied settings, etc.</p>

## Comments (2)

### marti_velezis — 2026-02-02T20:30:23+00:00
<p>David Barwin / Riki Merrick : against: 0, abstain: 1, in favor: 11</p>

### marti_velezis — 2026-02-02T20:30:23+00:00
<p>Reverted previous resolution: Considered for Future Use made 2025-10-27 00:00:00.0 with vote David Barwin / Elliot Silver: 5-0-0//(Impact: null; Category: null; Version: null)//Motion to consider for future use, which means they will be inserted as ballot feedback in the first R6 round to pick as part of ballot reconciliation. </p>


## Snapshot
# FHIR-48395: Mechanism to request device settings changes

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Elliot Silver  
**Work Group:** Orders & Observations  
**Specification:** OO Incubator (FHIR)  
**Labels:** Joint-OO-PC, OO, Ready-to-Discuss, WGM-September-2025  
**Created:** 2024-09-25  
**Updated:** 2026-02-02  

## Description

<p>A request was recieved from <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=chuscmi" class="user-hover" rel="chuscmi">Stephen Chu</a> to be able to request device settings changes.</p>

<p>Currently you can define a task or service request to get a person to change the settings on a device, but there isn't a defined mechanism to request those changes of the device itself.</p>

<p>We need a way to represent requested settings in a structured representation; a way to convey the request to the device (perhaps profiling or modifying Task, and/or defining an operation on Device). We will also need to be able to track requested settings, pending settings, as-applied settings, etc.</p>

## Comments

### marti_velezis (2026-02-02)

<p>David Barwin / Riki Merrick : against: 0, abstain: 1, in favor: 11</p>

### marti_velezis (2026-02-02)

<p>Reverted previous resolution: Considered for Future Use made 2025-10-27 00:00:00.0 with vote David Barwin / Elliot Silver: 5-0-0//(Impact: null; Category: null; Version: null)//Motion to consider for future use, which means they will be inserted as ballot feedback in the first R6 round to pick as part of ballot reconciliation. </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-48395".
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

Let me search for additional Zulip discussions and check for any GitHub references.

<details>
<summary>`FhirAugury-query_zulip_messages` — device settings request change</summary>

**Result:**
```
## Zulip Query Results

- **implementers > Modelling device settings** [Elliot Silver]
  Hi @Simone Fricke , you're headed in the correct direction, and have picked up on the challenges. As I describe it, DeviceMetric documents the existence of a reading or setting for a device. "This dev
  2024-08-08 15:24:47+00:00

```

</details>

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

### Turn 4

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-48395.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\OrdersObservations\\FHIR-48395.md",
  "file_text": "# FHIR-48395: Mechanism to request device settings changes\n\n## Summary\n\n| Field         | Value                                  |\n|---------------|----------------------------------------|\n| **Ticket**    | [FHIR-48395](https://jira.hl7.org/browse/FHIR-48395) |\n| **Type**      | Change Request                         |\n| **Priority**  | Medium                                 |\n| **Status**    | Triaged                                |\n| **Resolution**| Unresolved                             |\n| **Work Group**| Orders & Observations                  |\n| **Specification** | OO Incubator (FHIR)               |\n| **Reporter**  | Elliot Silver                          |\n| **Assignee**  | Unassigned                             |\n| **Labels**    | Joint-OO-PC, OO, Ready-to-Discuss, WGM-September-2025 |\n| **Created**   | 2024-09-25                             |\n| **Updated**   | 2026-02-02                             |\n\n## Description\n\nStephen Chu requested the ability to request device settings changes directly of a device. Currently, FHIR supports defining a Task or ServiceRequest to ask a **person** to change settings on a device, but there is no defined mechanism to request those changes **of the device itself**.\n\nThe ticket identifies three needs:\n\n1. **Structured representation of requested settings** \u2014 a way to express which settings should be changed and to what values.\n2. **Conveyance mechanism** \u2014 a way to send the request to the device, possibly by profiling or modifying Task, and/or defining a new operation on Device.\n3. **Settings lifecycle tracking** \u2014 the ability to track requested settings, pending settings, and as-applied settings through their various states.\n\n## Voting History\n\n- **2025-10-27:** Motion to resolve as \"Considered for Future Use\" \u2014 vote: David Barwin / Elliot Silver 5-0-0. Intent was to insert as ballot feedback in the first R6 round for ballot reconciliation.\n- **2026-02-02:** Previous resolution **reverted**. New vote: David Barwin / Riki Merrick \u2014 0 against, 1 abstain, 11 in favor. Ticket returned to Triaged status.\n\n## Keywords\n\n`device`, `settings`, `DeviceMetric`, `Task`, `ServiceRequest`, `operation`, `configuration`, `Device`, `OO Incubator`, `request`, `pending settings`, `as-applied settings`\n\n## Related Jira Tickets\n\n### FHIR-48394 \u2014 Mechanism needed to prompt for device settings \u2b50 Companion Ticket\n- **Status:** Triaged | **Resolution:** Unresolved\n- **Reporter:** Elliot Silver | **Work Group:** Orders & Observations\n- **Labels:** Joint-OO-PC, OO, Ready-to-Discuss, WGM-September-2025\n- **Relevance:** Direct companion ticket filed at the same time by the same reporter, also originating from Stephen Chu. FHIR-48394 addresses the **read** side (requesting a device to report its current settings on demand), while FHIR-48395 add

... *(truncated, 9691 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-48395.md with 9459 characters
```

</details>


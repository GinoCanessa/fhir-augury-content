# Session Log: FHIR-29472

**Phase:** prepared
**Work Group:** Pharmacy
**Source File:** `prepared/Pharmacy/FHIR-29472.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29472` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:49:27 UTC |
| **Duration** | 102s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 296,895 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29472
## Work Group: Pharmacy
## Output File: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29472.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29472", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29472", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29472", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29472.md
````

---

## Agent Execution Log

### Turn 1

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29472: <FillStatus> does not represent whether a dispense was a partial fill.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:55:09+00:00
- **Updated:** 2024-03-19T21:31:10+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29472

## Content
<p>&lt;FillStatus&gt; does not represent whether a dispense was a partial fill.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element for Partial Fill Indicator</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29473: More granular guidance should be provided for mapping from those individual NCPDP SCRIPT fields to FHIR.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:55:11+00:00
- **Updated:** 2024-03-19T21:31:23+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29473

## Content
<p>The &lt;Quantity&gt; field within MedicationDispensed of NCPDP SCRIPT (2017071 and 10.6) have multiple subfields that are all required.  More granular guidance should be provided for mapping from those individual NCPDP SCRIPT fields to FHIR.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element for Quantity</p>

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# implementers > Medication Refills

**Messages:** 14
**First message:** 2025-02-14 07:17:43+00:00
**Last message:** 2025-02-16 17:35:38+00:00
**Participants:** niraj631, Pedro Cubero, Lloyd McKenzie, John Moehrke, Peter Jordan, Forest

## Messages

### niraj631 — 2025-02-14 07:17:43+00:00
Hi All, Can somebody share light on how Medication Refills are handled in FHIR? Specific questions Which FHIR Resource is used to create a refill order? I assume Medication Request In that case, What differentiates a refill order from an original order? How is the maxNumberOfRepeatsAllowed field handled. Does the number change with each dispense

### Pedro Cubero — 2025-02-14 12:36:43+00:00
I have more questions about this resource, where can I profile the number of containers related with the prescription, in the MedicationRequest resource?

### Lloyd McKenzie — 2025-02-14 16:19:33+00:00
Do you mean "refill" or "renewal"? A 'refill' is a dispense already authorized under an existing prescription, while a renewal is a new prescription that replaces another. Soliciting a new dispense under an existing prescription would be handled by Task - specifically one with a focus of the original order and with a code saying 'fulfills'. You would also typically specify a Task.restriction to indicate the number of repetitions or period for which fulfillment is sought. The resulting MedicationDispense(s) can indicate that they are refills using MedicationDispense.type. There generally isn't a new MedicationRequest for a refill because the original MedicationRequest authorizes all refills. Seeking a renewal can also be done with Task, typically by proposing a new prescription. The fact an order is a renewal is represented by specifying MedicationRequest.priorPrescription. The MedicationRequest.dispense.numberOfRepeatsAllowed does not change. In fact, the MedicationRequest as a whole doesn't generally change (other than possibly addition of new notes) until such time as the prescriber chooses to mark it as 'complete'. Typically the system simply tracks the dispenses that have been recorded against the MedicationRequest. Due to partial fills, trial fills, etc., the notion of "refills remaining" can also be complex to evaluate. Some systems might choose to have an extension on the MedicationRequest that indicates number of fills remaining or quantity remaining, though there can be challenges with a MedicationRequest being updated by anyone other than the author.

### niraj631 — 2025-02-14 17:46:06+00:00
Thanks @Lloyd McKenzie , I mean “refills” not renewals. In a medication request resource , the prescriber will mention how many refills are authorised . my question is when a patient calls into the call center for a refill, what is the workflow with fhir .

### niraj631 — 2025-02-14 17:50:09+00:00
So this is what I understand based on your explanation. The call center app would send a Task resource to an EMR with reference to the medication request order . The numberofrepeatsallowed element never gets decremented after each dispense ?

### Lloyd McKenzie — 2025-02-14 18:14:03+00:00
Generally the EMR isn't involved in refills at all. The patient would be contacting the pharmacy directly. If the request to the pharmacy were happening electronically, it would be represented as a Task seeking fulfillment. And yes, the numberofrepeatsallowed would not be changed.

### niraj631 — 2025-02-14 18:27:30+00:00
Got it . Isn’t it the case that EMRs work as an intermediary in this case between a portal app/contact center and the various pharmacies that are connected to the EMR ?

### John Moehrke — 2025-02-14 18:27:55+00:00
@Jose Costa Teixeira is this the workflow that IHE-MEOW is working on?

### niraj631 — 2025-02-14 18:30:11+00:00
In addition , based on your experience, is there a referencable implementation in the real world based on this ? Also, do we have pharmacy apps supporting the fhir task resource

### Lloyd McKenzie — 2025-02

... *(truncated, 5640 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29454: The  PDMP IG should be focused on communicting dispenses, not prescriptions.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:35+00:00
- **Updated:** 2024-03-19T23:56:34+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29454

## Content
<p>Wording can be more clear. The PDMP IG should be focused on communicting dispenses, not prescriptions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The above API will fetch all MedicationDispense resources for Patient with a given name of “sherlock” and family name of “holmes” with a birthdate of “1954-01-06” with a prescription from January 6, 1954 to December 01, 2019</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>The above API will fetch all MedicationDispense resources for Patient with a given name of “sherlock” and family name of “holmes” with a birthdate of “1954-01-06” for medications dispensed from January 6, 1954 to December 01, 2019</p>

```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-29472",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29472: <FillStatus> does not represent whether a dispense was a partial fill.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:55:09+00:00
- **Updated:** 2024-03-19T21:31:10+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29472

## Content
<p>&lt;FillStatus&gt; does not represent whether a dispense was a partial fill.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element for Partial Fill Indicator</p>

## Comments (3)

### smrobertson — 2023-11-28T19:25:47+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:25:47+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:55:10+00:00
<p>Imported from spreadsheet by jduteau - comment #22</p>


## Snapshot
# FHIR-29472: <FillStatus> does not represent whether a dispense was a partial fill.

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Daniel Zhang  
**Work Group:** Pharmacy  
**Specification:** US Medication FHIR Implementation Guide (FHIR)  
**Labels:** PDMP-old-issues  
**Created:** 2020-10-26  
**Updated:** 2024-03-19  

## Description

<p>&lt;FillStatus&gt; does not represent whether a dispense was a partial fill.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element for Partial Fill Indicator</p>

## Comments

### smrobertson (2023-11-28)

<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson (2023-11-28)

<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin (2020-10-26)

<p>Imported from spreadsheet by jduteau - comment #22</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29472".
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

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# implementers > NCPDP 2017 to FHIR 4.0

**Messages:** 16
**First message:** 2019-06-13 17:34:52+00:00
**Last message:** 2021-11-22 18:59:23+00:00
**Participants:** Aron Dalentor, Lloyd McKenzie, Scott Robertson, Brendan Keeler, Vassil Peytchev

## Messages

### Aron Dalentor — 2019-06-13 17:34:52+00:00
Hello, does anyone know how to map part of NCPDP related to signature within FHIR? When we search for available examples ( https://www.hl7.org/fhir/medication-mappings.html#script10.6 https://www.hl7.org/fhir/medicationrequest-mappings.html#script10.6 ), much of the data is not mapped and the signature is absent at all.

### Lloyd McKenzie — 2019-06-13 17:41:23+00:00
@Melva Peters @Scott Robertson

### Scott Robertson — 2019-06-13 18:23:17+00:00
Yes, the mapping is incomplete. While SCRIPT 10.6 is in use today, as of 1/1/2020 SCRIPT 2017071 will be the version in use. The current effort is to get a comprehensive SCRIPT 2017071 to FHIR r4 mapping done. This will likely include a set of extensions for the SCRIPT content that does not map or is not added to the resources. I assume your request is in terms of EPCS, the requirement for a digital signature or an indicator that of identity verification (a "Signed Prescription" per DEA regulation). SCRIPT 10.6 does not support digital signatures (although, you should look at FHIR Digital Signatures ( https://www.hl7.org/fhir/signatures.html#6.1.2 ) if that is your intent. SCRIPT 10.6 uses <DrugCoverageStatusCode>="SI" to meet DEA requirements, and that could be sent as a local FHIR extension. I'm interested in your business case. Do you have a system receiving eRx using FHIR?

### Aron Dalentor — 2019-06-14 10:06:04+00:00
We've partnered with company that developed eRx system. They use NCPDP 2017071 and they didn't implement FHIR, but we do and want to integrate their system into ours. They will send to us messages in NCPDP and we want to convert it into FHIR R4 and retranslate to other systems as FHIR messages. We are especially concerned about sig because in NCPDP sig is presented very well compared to dosageInstruction in MedicationRequest resource in FHIR. We are not interested in controlled substances, our focus is oncology and chemotherapy medications. @Scott Robertson @Melva Peters

### Brendan Keeler — 2021-08-18 17:00:05+00:00
This is an interesting thread. Has anyone done significant work on the NCPDP to FHIR mapping?

### Lloyd McKenzie — 2021-08-18 21:36:07+00:00
@Scott Robertson would know if anyone has...

### Scott Robertson — 2021-08-19 05:33:21+00:00
There are individuals interested in mapping between SCRIPT 2017071 and FHIR r4, but no coordinated effort that I am aware of. It will need a business/use case driver since non-inpatient eRx in the US is exclusively SCRIPT 2017071 - CMS names SCRIPT in the Part D regulations, and that drives the overall market.

### Brendan Keeler — 2021-08-19 06:02:55+00:00
FHIR increasingly used in a storage capacity. A FHIR enabled pharmacy receives a NEWRX and wants to store it. A prescriber retrieves medication history and wants to store to the FHIR server

### Brendan Keeler — 2021-08-20 19:20:57+00:00
I imagine RXHISTORYRESPONSE would be MedicationStatement, but RXHISTORYREQUEST seems to map to two distinct FHIR calls (Patient search with demographics, MedicationStatement search with patient ID). Do people agree? Is there a way around that?

### Brendan Keeler — 2021-11-19 15:07:51+00:00
Circling back on this - seems like it was done here: http://hl7.org/fhir/us/meds/2020Sep/pdmp.html#ncpdp-mappings-for-pdmp-request I'm curious about the choice of MedicationDispense vs MedicationStatement

### Lloyd McKenzie — 2021-11-19 18:40:32+00:00
NCPDP lives in the world of dispenses and prescriptions. Why would they use statement, which is more about summarization and tracking compliance?

### Brendan Keeler — 2021-11-19 20:13:41+00:00
The med history response is a summary across all pharmacies and Ph

... *(truncated, 5346 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-29472
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| fillstatus | word | 3 | 18.238 |
| partial | word | 4 | 10.578 |
| fill | word | 4 | 10.270 |
| dispense | word | 3 | 9.868 |
| ncpdp | word | 1 | 7.728 |
| indicator | word | 1 | 7.074 |
| pdmp | word | 1 | 6.923 |
| represent | word | 3 | 5.664 |
| h3 | word | 2 | 5.607 |
| lt | word | 1 | 5.215 |
| existingwording | word | 1 | 4.524 |
| 3a | word | 1 | 4.396 |
| gt | word | 1 | 4.285 |
| word | word | 1 | 3.168 |
| existing | word | 1 | 3.163 |
| issue | word | 1 | 2.695 |
| element | word | 1 | 2.541 |
| data/datum | word | 1 | 2.475 |

```

</details>

### Turn 4

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29472.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Pharmacy\\FHIR-29472.md",
  "file_text": "# FHIR-29472: \\<FillStatus\\> does not represent whether a dispense was a partial fill\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-29472](https://jira.hl7.org/browse/FHIR-29472) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Work Group** | Pharmacy |\n| **Specification** | US Medication FHIR Implementation Guide (FHIR) |\n| **Reporter** | Daniel Zhang |\n| **Assignee** | Unassigned |\n| **Labels** | PDMP-old-issues |\n| **Created** | 2020-10-26 |\n| **Updated** | 2024-03-19 |\n\n## Description\n\nThe ticket reports that the NCPDP `<FillStatus>` element does not represent whether a dispense was a partial fill. The existing wording references \"NCPDP Data Element for Partial Fill Indicator,\" indicating the IG's mapping table uses `<FillStatus>` for the partial fill concept, but `<FillStatus>` is actually a numeric field representing which fill in a sequence of fills a dispense is (i.e., the fill number), not whether the fill was partial or complete.\n\nThis is a companion issue to [FHIR-29471](https://jira.hl7.org/browse/FHIR-29471), which addresses the same `<FillStatus>` element but from the refill number perspective. Together, these tickets highlight that `<FillStatus>` was incorrectly mapped to two different concepts (refill number and partial fill indicator) in the PDMP NCPDP mapping table, when it only represents one (the fill sequence number).\n\n## Keywords\n\n`FillStatus`, `partial fill`, `dispense`, `NCPDP`, `PDMP`, `Partial Fill Indicator`, `MedicationDispense`\n\n## Ticket History\n\n- **2020-10-26**: Imported from ballot comment spreadsheet by jduteau (comment #22). Reporter: Daniel Zhang.\n- **2023-01-18**: Resolved as \"Considered for Future Use\" with vote John Hatem / Tim McNeil: 4-0-0, because the IG had been withdrawn; issues deferred until the IG is taken up again.\n- **2023-11-28**: Reopened by Scott Robertson as part of [PSS-2225 PDMP on FHIR](https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide). Previous resolution reverted.\n- **2024-03-19**: Last updated (status remains Triaged).\n\n## Related Jira Tickets\n\n| Ticket | Title | Relationship |\n|--------|-------|-------------|\n| [FHIR-29471](https://jira.hl7.org/browse/FHIR-29471) | MedicationDispensed.type does not contain a refill number and is not an appropriate mapping to \\<FillStatus\\> | **Companion issue** \u2014 Same `<FillStatus>` element; FHIR-29471 addresses refill number mapping, FHIR-29472 addresses partial fill indicator mapping. Both highlight incorrect use of `<FillStatus>`. |\n| [FHIR-29473](https://jira.hl7.org/browse/FHIR-29473) | More granular guidance should be provided for mapping from those individual NCPDP SCRIPT fields to FHIR | **Related** \u2014 Requests finer-grained NCPDP SCRIPT-to-FHIR mapping guidance fo

... *(truncated, 8687 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29472.md with 8494 characters
```

</details>


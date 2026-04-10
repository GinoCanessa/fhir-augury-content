# Session Log: FHIR-29458

**Phase:** prepared
**Work Group:** Pharmacy
**Source File:** `prepared/Pharmacy/FHIR-29458.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29458` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:04:17 UTC |
| **Duration** | 88s |
| **Total Tool Calls** | 12 |
| **Total Tokens** | 216,554 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29458
## Work Group: Pharmacy
## Output File: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29458.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29458", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29458", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29458", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29458.md
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
  "id": "FHIR-29458",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29458: Capitalization error  “SCRIPT” and correction regarding latest version in use.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:43+00:00
- **Updated:** 2024-03-19T21:56:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29458

## Content
<p>SCRIPT should be all capitalized, and version 2017071 is also the latest in use.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Most of the existing EHR implementations use NCPDP script 10.6 or ASAP web services…</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Most of the existing EHR implementations use NCPDP SCRIPT 2017071, NCPDP SCRIPT 10.6, or ASAP web services…</p>

## Comments (3)

### smrobertson — 2023-11-28T19:26:12+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:26:12+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:54:44+00:00
<p>Imported from spreadsheet by jduteau - comment #8</p>


## Snapshot
# FHIR-29458: Capitalization error  “SCRIPT” and correction regarding latest version in use.

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Not Persuasive with Modification  
**Assignee:** Unassigned  
**Reporter:** Daniel Zhang  
**Work Group:** Pharmacy  
**Specification:** US Medication FHIR Implementation Guide (FHIR)  
**Labels:** PDMP-old-issues  
**Created:** 2020-10-26  
**Updated:** 2024-03-19  
**Resolved:** 2023-11-29  

## Description

<p>SCRIPT should be all capitalized, and version 2017071 is also the latest in use.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Most of the existing EHR implementations use NCPDP script 10.6 or ASAP web services…</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Most of the existing EHR implementations use NCPDP SCRIPT 2017071, NCPDP SCRIPT 10.6, or ASAP web services…</p>

## Resolution Description

<p>specific reference to MedicationRequest mapping to SCRIPT 10.6 NewRx will be removed.  MedicationRequest is not directly related to the PDMP content (minimally used for prescription number, original fills authorized, etc.)</p>

<p>Related tables will be updated to SCRIPT 2017071 RxHistoryRequest and RxHistoryResponse</p>

## Comments

### smrobertson (2023-11-28)

<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson (2023-11-28)

<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin (2020-10-26)

<p>Imported from spreadsheet by jduteau - comment #8</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29458".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29458.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Pharmacy\\FHIR-29458.md",
  "file_text": "# FHIR-29458: Capitalization error \"SCRIPT\" and correction regarding latest version in use\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-29458](https://jira.hl7.org/browse/FHIR-29458) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Work Group** | Pharmacy |\n| **Specification** | US Medication FHIR Implementation Guide (FHIR) |\n| **Resolution** | Not Persuasive with Modification |\n| **Reporter** | Daniel Zhang |\n| **Assignee** | Unassigned |\n| **Labels** | PDMP-old-issues |\n| **Created** | 2020-10-26 |\n| **Updated** | 2024-03-19 |\n\n## Description\n\nThe submitter identifies two issues in the US Medication FHIR IG (PDMP section):\n\n1. **Capitalization error:** \"script\" should be \"SCRIPT\" (the official product name is \"NCPDP SCRIPT\" in all caps).\n2. **Version update:** NCPDP SCRIPT 2017071 should be referenced as the current named version alongside SCRIPT 10.6.\n\n**Existing Wording:**\n> Most of the existing EHR implementations use NCPDP script 10.6 or ASAP web services\u2026\n\n**Proposed Wording:**\n> Most of the existing EHR implementations use NCPDP SCRIPT 2017071, NCPDP SCRIPT 10.6, or ASAP web services\u2026\n\n## Resolution Description\n\nThe resolution (Not Persuasive with Modification) states:\n\n> Specific reference to MedicationRequest mapping to SCRIPT 10.6 NewRx will be removed. MedicationRequest is not directly related to the PDMP content (minimally used for prescription number, original fills authorized, etc.).\n>\n> Related tables will be updated to SCRIPT 2017071 RxHistoryRequest and RxHistoryResponse.\n\nThis goes beyond the submitter's request by also cleaning up mapping table references to align with SCRIPT 2017071 RxHistory messages rather than the older SCRIPT 10.6 NewRx mappings.\n\n## Comment History\n\n| Date | Author | Summary |\n|------|--------|---------|\n| 2020-10-26 | jiraadmin | Imported from spreadsheet by jduteau (comment #8) |\n| 2023-11-28 | smrobertson | Reverted previous resolution of \"Considered for Future Use\" (vote: John Hatem / Tim McNeil, 4-0-0). Original deferral was because the IG had been withdrawn. |\n| 2023-11-28 | smrobertson | Reopened by [PSS-2225 PDMP on FHIR](https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide) |\n\n## Keywords\n\nNCPDP, SCRIPT, 2017071, 10.6, PDMP, capitalization, version, RxHistoryRequest, RxHistoryResponse, MedicationRequest, mapping\n\n## Related Jira Tickets\n\n| Key | Title | Status | Resolution | Relevance |\n|-----|-------|--------|------------|-----------|\n| [FHIR-29460](https://jira.hl7.org/browse/FHIR-29460) | We should just use NCPDP SCRIPT 2017071 since that is the current named version | Triaged | Unresolved | Same submitter, same request to update mapping tables to SCRIPT 2017071 RxHistoryRequest |\n| [FHI

... *(truncated, 8982 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29458.md with 8818 characters
```

</details>

### Turn 3

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29458: Capitalization error  “SCRIPT” and correction regarding latest version in use.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:43+00:00
- **Updated:** 2024-03-19T21:56:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29458

## Content
<p>SCRIPT should be all capitalized, and version 2017071 is also the latest in use.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Most of the existing EHR implementations use NCPDP script 10.6 or ASAP web services…</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Most of the existing EHR implementations use NCPDP SCRIPT 2017071, NCPDP SCRIPT 10.6, or ASAP web services…</p>

## Comments (3)

### smrobertson — 2023-11-28T19:26:12+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:26:12+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:54:44+00:00
<p>Imported from spreadsheet by jduteau - comment #8</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29528: Correct SCRIPT version

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Scott M. Robertson
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:57:05+00:00
- **Updated:** 2024-03-19T21:58:49+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29528

## Content
<p>regulation now requires all eRx transactions to employ SCRIPT 2017071</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP SCRIPT 10.6</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>NCPDP SCRIPT 2017071</p>

## Comments (3)

### smrobertson — 2023-11-28T19:25:54+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:25:54+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:57:07+00:00
<p>Imported from spreadsheet by jduteau - comment #77</p>


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

## Comments (3)

### smrobertson — 2023-11-28T19:25:51+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:25:51+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:55:12+00:00
<p>Imported from spreadsheet by jduteau - comment #23</p>


```

</details>

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
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# Medication > Community question

**Messages:** 4
**First message:** 2022-01-25 17:33:57+00:00
**Last message:** 2022-02-16 19:52:32+00:00
**Participants:** Lloyd McKenzie, Hans Michel, Olivier Boux

## Messages

### Lloyd McKenzie — 2022-01-25 17:33:57+00:00
Can someone respond to this question on dosage? http://community.fhir.org/t/fhir-dosage-timings/3428

### Hans Michel — 2022-01-27 17:01:55+00:00
Lloyd McKenzie said : Can someone respond to this question on dosage? http://community.fhir.org/t/fhir-dosage-timings/3428 Made an attempt.

### Olivier Boux — 2022-02-16 16:19:49+00:00
This is an elegant way to resolve the assertion of an XOR between two dosageInstruction . I would have preferred an actual ability of the Timing data type to support this exclusive schedule alternative. This solution, expressing XOR of two dosageInstruction elements by a third one having .method.coding.code=420561004 in the same .sequence is not obvious. Is it validated by the Pharmacy WG (@Jean Duteau) ?

### Hans Michel — 2022-02-16 19:52:32+00:00
@Olivier Boux I don't know if the suggestion, presented as a possible solution for question 2 in the above community fhir link, is valid according to or has been validated by the Pharmacy WG. My suggestion came out of much ongoing work in trying to get NCPDP Script 2017071 to fhir v 4 (4.6). And inklings of possibilities from NHS https://developer.nhs.uk/apis/dose-syntax-implementation/dosage-sequence.html . I am struggling with this stuff as well, mostly trying to avoid the escape hatch of extensions.

---
*URL: https://chat.fhir.org/#narrow/stream/Medication/topic/Community%20question*

```

</details>


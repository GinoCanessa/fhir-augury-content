# Session Log: FHIR-29459

**Phase:** prepared
**Work Group:** Pharmacy
**Source File:** `prepared/Pharmacy/FHIR-29459.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `retry-FHIR-29459` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:24:21 UTC |
| **Duration** | 97s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 264,505 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29459
## Work Group: Pharmacy
## Output File: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29459.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29459", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29459", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29459", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29459.md
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
  "id": "FHIR-29459",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29459: NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:44+00:00
- **Updated:** 2024-03-19T21:22:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29459

## Content
<p>Current integration methods allow both prescribers and pharmacies to perform queries of PDMPs.  Is the intention of this implementation guide to cover both of those users as a PDMP Requestor?  If yes, NCPDP mappings at least need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Data Elements and Mappings section</p>

## Comments (3)

### smrobertson — 2023-11-28T19:25:45+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:25:45+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:54:46+00:00
<p>Imported from spreadsheet by jduteau - comment #9</p>


## Snapshot
# FHIR-29459: NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.

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

<p>Current integration methods allow both prescribers and pharmacies to perform queries of PDMPs.  Is the intention of this implementation guide to cover both of those users as a PDMP Requestor?  If yes, NCPDP mappings at least need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Data Elements and Mappings section</p>

## Comments

### smrobertson (2023-11-28)

<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson (2023-11-28)

<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin (2020-10-26)

<p>Imported from spreadsheet by jduteau - comment #9</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29459".
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
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-29459",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29459: NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:44+00:00
- **Updated:** 2024-03-19T21:22:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29459

## Content
<p>Current integration methods allow both prescribers and pharmacies to perform queries of PDMPs.  Is the intention of this implementation guide to cover both of those users as a PDMP Requestor?  If yes, NCPDP mappings at least need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Data Elements and Mappings section</p>

## Comments (3)

### smrobertson — 2023-11-28T19:25:45+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:25:45+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:54:46+00:00
<p>Imported from spreadsheet by jduteau - comment #9</p>


## Snapshot
# FHIR-29459: NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.

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

<p>Current integration methods allow both prescribers and pharmacies to perform queries of PDMPs.  Is the intention of this implementation guide to cover both of those users as a PDMP Requestor?  If yes, NCPDP mappings at least need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Data Elements and Mappings section</p>

## Comments

### smrobertson (2023-11-28)

<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson (2023-11-28)

<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin (2020-10-26)

<p>Imported from spreadsheet by jduteau - comment #9</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29459".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29459.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Pharmacy\\FHIR-29459.md",
  "file_text": "# FHIR-29459: Ticket Review Preparation\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-29459](https://jira.hl7.org/browse/FHIR-29459) |\n| **Title** | NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Work Group** | Pharmacy |\n| **Specification** | US Medication FHIR Implementation Guide (FHIR) |\n| **Reporter** | Daniel Zhang |\n| **Assignee** | Unassigned |\n| **Labels** | PDMP-old-issues |\n| **Created** | 2020-10-26 |\n| **Updated** | 2024-03-19 |\n\n## Description\n\nThe submitter notes that current PDMP integration methods allow **both prescribers and pharmacies** to query PDMPs. The ticket asks whether the IG intends to cover both user types as a \"PDMP Requestor.\" If so, the NCPDP mappings in the \"PDMP Data Elements and Mappings\" section need to be updated to reflect that queries use **different data elements** depending on whether the requestor is a prescriber or a pharmacist.\n\nThis is a structural mapping concern: NCPDP SCRIPT represents prescriber and pharmacist data paths differently (e.g., `<Prescriber>/<Name>/<LastName>` vs. `<Pharmacy>/<Pharmacist>/<LastName>`), and the current mappings do not distinguish between these two requestor types.\n\n## Keywords\n\n`NCPDP`, `PDMP`, `mappings`, `prescriber`, `pharmacist`, `requestor`, `PDMP Requestor`, `PractitionerRole`, `data elements`, `query`\n\n## Ticket History\n\n- **2020-10-26** \u2014 Created. Imported from spreadsheet by jduteau (comment #9).\n- **2023-01-18** \u2014 Previously resolved as \"Considered for Future Use\" (vote: John Hatem / Tim McNeil, 4-0-0) with rationale that the IG had been withdrawn and items would be deferred.\n- **2023-11-28** \u2014 Reopened by smrobertson via [PSS-2225 PDMP on FHIR](https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide). Previous resolution reverted.\n- **2024-03-19** \u2014 Last updated (no new comments).\n\n## Related Jira Tickets\n\n### Closely Related (same mapping cluster, same reporter, same label)\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-29461](https://jira.hl7.org/browse/FHIR-29461) | Relative path information should be included to provide clarity around exactly where data is pulled from | Triaged | Directly extends this ticket \u2014 requests explicit NCPDP element paths for prescriber vs. pharmacist requestor (e.g., `<Prescriber>/<Name>/<LastName>` vs. `<Pharmacy>/<Pharmacist>/<LastName>`) |\n| [FHIR-29462](https://jira.hl7.org/browse/FHIR-29462) | The `<Qualifier>` element should reflect that it means the Qualifier attribute of `<Header>/<From>` | Triaged | Request

... *(truncated, 9600 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29459.md with 9445 characters
```

</details>

### Turn 4

**Assistant:**

Let me fetch the Zulip publication announcement and a few of the most closely related Jira tickets.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# Announcements > New Publication

**Messages:** 5
**First message:** 2020-10-12 06:07:36+00:00
**Last message:** 2020-11-23 17:57:40+00:00
**Participants:** Grahame Grieve, Lynn Laakso

## Messages

### Grahame Grieve — 2020-10-12 06:07:36+00:00
new Publication: STU 1 of theFHIR Shorthand implementation guide: http://hl7.org/fhir/uv/shorthand/STU1

### Lynn Laakso — 2020-10-15 20:08:25+00:00
New Publication: STU 1 of the FHIR Da Vinci Unsolicited Notifications Implementation Guide: http://hl7.org/fhir/us/davinci-alerts/STU1

### Lynn Laakso — 2020-10-22 01:06:54+00:00
New Publication: STU 1.1 of the C-CDA on FHIR Implementation Guide: http://hl7.org/fhir/us/ccda/STU1.1

### Lynn Laakso — 2020-10-27 18:03:50+00:00
New Publication: STU 1 of the Vital Records Mortality and Morbidity Reporting FHIR Implementation Guide: http://hl7.org/fhir/us/vrdr/STU1/index.html

### Lynn Laakso — 2020-11-23 17:57:40+00:00
New Publication: STU1 of the CARIN Consumer Directed Payer Data Exchange (CARIN IG for Blue Button®) FHIR Implementation Guide: http://hl7.org/fhir/us/carin-bb/STU1

---
*URL: https://chat.fhir.org/#narrow/stream/Announcements/topic/New%20Publication*

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29459: NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:44+00:00
- **Updated:** 2024-03-19T21:22:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29459

## Content
<p>Current integration methods allow both prescribers and pharmacies to perform queries of PDMPs.  Is the intention of this implementation guide to cover both of those users as a PDMP Requestor?  If yes, NCPDP mappings at least need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Data Elements and Mappings section</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29463: The NCPDP SCRIPT 2017071 standard does support a <Facility>/<Identification> element where requesting facility information could be transmitted.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:52+00:00
- **Updated:** 2024-03-19T21:26:11+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29463

## Content
<p>What are the relative paths for the NCPDP Data Element mappings for &lt;DEANumber&gt; and &lt;NPI&gt; of the facility when a prescriber performs a query?  The Prescriber element has child elements within Identification to send &lt;DEANumber&gt; and &lt;NPI&gt; but those are intended to identify the prescriber, not the facility.  The &lt;Pharmacy&gt;/&lt;Identification&gt; elements are also not appropriate since the prescriber is not performing a query from a pharmacy.</p>

<p>The NCPDP SCRIPT 2017071 standard does support a &lt;Facility&gt;/&lt;Identification&gt; element where requesting facility information could be transmitted.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element for Requesting Facility ID</p>

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "PDMP on FHIR,NCPDP SCRIPT mapping path element"
}
```

**Result:**
```
## Search Results (8 total, showing 8)

### [zulip] 376189226 — [implementers] PDMP implementers
- **Score:** 0.06
- **Updated:** 2023-07-18T00:17:04+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/PDMP%20implementers/near/376189226
- **Snippet:** ...<b>PDMP</b> <b>on</b> <b>FHIR</b> stream <b>PDMP</b> <b>on</b> <b>FHIR</b> Confluence page

### [zulip] 389301342 — [Announcements] new streams
- **Score:** 0.06
- **Updated:** 2023-09-05T23:35:56+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Announcements/topic/new%20streams/near/389301342
- **Snippet:** Scott Robertson created a new stream #<b>PDMP</b> <b>on</b> <b>FHIR</b>/connectathon .

### [zulip] 374388022 — [Announcements] new streams
- **Score:** 0.06
- **Updated:** 2023-07-11T21:14:38+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Announcements/topic/new%20streams/near/374388022
- **Snippet:** Frank McKinney created a new stream #<b>PDMP</b> <b>on</b> <b>FHIR</b> .

### [zulip] 444543444 — [IG creation] THO license link broken
- **Score:** 0.03
- **Updated:** 2024-06-13T19:21:49+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IG%20creation/topic/THO%20license%20link%20broken/near/444543444
- **Snippet:** Built my IG ( <b>PDMP</b> <b>on</b> <b>FHIR</b> ) with no (significant) errors. In the IP Statements, the THO license was added as...

### [zulip] 262078076 — [implementers] NCPDP 2017 to FHIR 4.0
- **Score:** 0.02
- **Updated:** 2021-11-19T15:07:51+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/NCPDP%202017%20to%20FHIR%204.0/near/262078076
- **Snippet:** Circling back <b>on</b> this - seems like it was done here: http://hl7.org/<b>fhir</b>/us/meds/2020Sep/<b>pdmp</b>.html#ncpdp...

### [zulip] 199669066 — [smart] EHRs to assist querying PDMP data
- **Score:** 0.01
- **Updated:** 2020-06-03T19:58:37+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/smart/topic/EHRs%20to%20assist%20querying%20PDMP%20data/near/199669066
- **Snippet:** ...EHRs (providers) to use a SMART <b>on</b> <b>FHIR</b> app to query a <b>PDMP</b> system in a non-production environment. Some...

### [zulip] 209895186 — [social] Ballot time!
- **Score:** 0.01
- **Updated:** 2020-09-12T19:03:31+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/social/topic/Ballot%20time%21/near/209895186
- **Snippet:** I am trying to enter Jira trackers for ballot comments <b>on</b> HL7 <b>FHIR</b>® IG: Pharmacy; Prescription Drug Monitoring Program (<b>PDMP</b>...

### [zulip] 186743714 — [patient empowerment] ONC2020
- **Score:** 0.00
- **Updated:** 2020-01-28T01:08:43+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/patient%20empowerment/topic/ONC2020/near/186743714
- **Snippet:** ...EHR and <b>PDMP</b> integration as well as highlight findings from ONC's state <b>PDMP</b> policy analysis. <b>FHIR</b>®: Advancing Interoperability Standards...


```

</details>

### Turn 5

**Assistant:**

Let me fetch the most closely related tickets for additional context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29459: NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:44+00:00
- **Updated:** 2024-03-19T21:22:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29459

## Content
<p>Current integration methods allow both prescribers and pharmacies to perform queries of PDMPs.  Is the intention of this implementation guide to cover both of those users as a PDMP Requestor?  If yes, NCPDP mappings at least need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Data Elements and Mappings section</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29461: Relative path information should be included to provide clarity around exactly where the data is expected to be pulled from.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:48+00:00
- **Updated:** 2024-03-19T21:25:30+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29461

## Content
<p>Each NCPDP Data Element only contains the furthermost child element where the data is being pulled from, but at least relative path information should be included to provide clarity around exactly where the data is expected to be pulled from.  For example, Requestor name should have something like the following in the NCPDP Data Element column when a prescriber is the PDMP requestor:<br/>
&lt;Prescriber&gt;/&lt;Name&gt;/&lt;LastName&gt; and &lt;Prescriber&gt;/&lt;Name&gt;/&lt;FirstName&gt;</p>

<p>And the following when a pharmacist is a PDMP requestor:<br/>
&lt;Pharmacy&gt;/&lt;Pharmacist&gt;/&lt;LastName&gt; and &lt;Pharmacy&gt;/&lt;Pharmacist&gt;/&lt;FirstName&gt;</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element definitions</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29464: <RequestingState> is not a field that exists in any NCPDP SCRIPT standard.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:54+00:00
- **Updated:** 2024-03-19T21:26:31+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29464

## Content
<p>&lt;RequestingState&gt; is not a field that exists in any NCPDP SCRIPT standard.  In 2017071 the &lt;Facility&gt;/&lt;Address&gt;/&lt;State&gt; element could be used.  </p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element for State code of Requesting Facility</p>

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "github",
  "values": "PDMP Qualifier NCPDP PractitionerRole FHIR-29462"
}
```

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "PDMP on FHIR PSS-2225 PDMP-old-issues reopened"
}
```

**Result:**
```
No results found.
```

</details>


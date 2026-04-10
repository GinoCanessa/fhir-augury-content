# Session Log: FHIR-29461

**Phase:** prepared
**Work Group:** Pharmacy
**Source File:** `prepared/Pharmacy/FHIR-29461.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29461` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:57:05 UTC |
| **Duration** | 127s |
| **Total Tool Calls** | 20 |
| **Total Tokens** | 359,419 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29461
## Work Group: Pharmacy
## Output File: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29461.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29461", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29461", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29461", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29461.md
````

---

## Agent Execution Log

### Turn 1

**Assistant:**

Now let me fetch details on the most closely related tickets and the key Zulip threads.

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
# [jira] FHIR-43140: Mappings

- **status:** Triaged
- **type:** Question
- **priority:** Medium
- **work_group:** Pharmacy
- **specification:** US Prescription Drug Monitoring Program (PDMP) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Scott M. Robertson
- **Created:** 2023-11-20T20:15:55+00:00
- **Updated:** 2023-11-20T20:18:45+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-43140

## Content
<p><b>Section 7 Mappings</b></p>

<p>While this section spells out existing data field mapping situations (at minimum values), it does not outline what FHIR is proposing for required data or mapping.</p>

<p><b><em><span class="error">&#91;SMR-_* _the mappings are not normative content.  Mappings show how the proposed FHIR resource elements correspond to data elements in the other standards.  This provides insight into the nature of the data (as in your comment on state license number for pharmacists) and traceability for troubleshooting.{*}&#93;</span></b></em></p>

<p>Considerations that should be made from existing NCPDP, PMIX, etc., mappings:</p>
<ul>
	<li>Requester identifier needs to accommodate a state license number for pharmacists without NPIs and the VA health system, which allows nurses to access PDMPs through the VA EMR. All requester identifiers must be unique, so pharmacy NPIs or other placeholders cannot be used in place of individual identifiers.</li>
</ul>


<p><b><em><span class="error">&#91;SMR-_* _FHIR can accommodate any number of different identifiers, including multiple types of identifiers from one organization (an employee number and a practitioner ID from an organization) and the same kind of identifier from different organizations (e.g., state licenses from different states).  Regarding the query request, the requestor does need to be uniquely identified (authentication) and verified as an allowed user (authorization) – which are part of Security (which references US Core) and likely needs additional text to explicitly address your concern{*}&#93;</span></b></em></p>
<ul>
	<li>Requester role must be included in the request elements. Authorization for access to the PDMP is granted by each state after careful consideration of each registrant. The requester role needs to be captured to ensure provider authorization requirements are being met for access to data by appropriate role types.</li>
</ul>


<p><b><em>[SMR-</em></b> <em>Authentication can include Role.  It’s not apparent in the IG as the Security discussion refers to US Core.  Generally, FHIR IG don’t repeat “established and reused” content to minimize the need to update multiple IGs when an underlying capability is updated.  However, points of concern, such as this, can and should be included in our IG, while still referring to US Core for the technical details.</em></p>

<p> __ </p>

<p><em>Related: US Core for Authentication and Authorization focus on OAuth 2 and SMART.  The group needs to discuss if this is viable, or another Authentication scheme is needed.<b>]</b></em></p>
<ul>
	<li>Response type needs to be included in the response elements. We need to know whether the request was successful, had an error, found data, etc. This helps us identify if there are issues within the integration producing a high number of errors and helps us with compliance and investigative work to be able to access our audit trail to identify whether a search was successful and/or produced data.</li>
</ul>


<p><b><em><span class="error">&#91;SMR-_* _The FHIR query response model includes the query in the reported response along with either errors or the found data.  I think this points to the need for examples, and some additional narrative.{*}&#93;</span></b></em></p>

<p><b>Gayle Donaldson</b></p>

<p>Assistant Director</p>

<p>Kansas Board of Pharmacy</p>

<p>800 SW Jackson, Suite 1414</p>

<p>Topeka, KS 66612</p>

<p>(785) 608-1023</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-45480: Further work needed on NCPDP mapping

- **status:** Published
- **type:** Technical Correction
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Prescription Drug Monitoring Program (PDMP) (FHIR)
- **resolution:** Persuasive
- **assignee:** Scott M. Robertson
- **reporter:** Scott M. Robertson
- **Created:** 2024-05-05T16:16:50+00:00
- **Updated:** 2024-10-15T18:58:51+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-45480

## Content
<p>Further updates and cleanup (and some formatting) needed for the NCPDP mapping tables.</p>

<p>Also, mappings need to be completed on, or added to, the PDMP-specific resources.</p>

<p>Work is in progress in PDMP GitHub branch <a href="https://github.com/HL7/fhir-pdmp/commit/a660c7287baa90142c6da559de0d3ec9efc5d8a3" class="external-link" target="_blank" rel="nofollow noopener">a660c72</a> pending approval of this technical correction</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29523: Pharmacies also access PDMPs

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Scott M. Robertson
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:56:56+00:00
- **Updated:** 2024-03-19T21:58:17+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29523

## Content
<p>Figure 1 Interaction 2 should include arrows in both directions.  Pharmacies in many states are required to access PDMPs to assess the Rx utilization of the patient.  This could bring interaction 2 in scope for the IG.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29524: Pharmacies also access PDMPs - again

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Scott M. Robertson
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:56:58+00:00
- **Updated:** 2024-03-19T21:58:34+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29524

## Content
<p>in the text and in Figure 2, pharmacies can also be PDMP requesters.  See my comment on Figure 1</p>

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
# implementers > PDMP implementers

**Messages:** 1
**First message:** 2023-07-18 00:17:04+00:00
**Last message:** 2023-07-18 00:17:04+00:00
**Participants:** Scott Robertson

## Messages

### Scott Robertson — 2023-07-18 00:17:04+00:00
Looking for interested implementers: The US Prescription Drug Monitoring Program (PDMP) FHIR IG project is ramping up. We are looking for implementers wanting (or that already have) a FHIR solution for PDMP query/response. We are having 2 overview webinars: July 20 at 1pm ET and July 24th at 2pm ET , please join either or both. For more and ongoing information, check out: PDMP on FHIR stream PDMP on FHIR Confluence page

---
*URL: https://chat.fhir.org/#narrow/stream/implementers/topic/PDMP%20implementers*

```

</details>

### Turn 2

**Assistant:**

Let me get details on the most closely related tickets.

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
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-43140: Mappings

- **status:** Triaged
- **type:** Question
- **priority:** Medium
- **work_group:** Pharmacy
- **specification:** US Prescription Drug Monitoring Program (PDMP) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Scott M. Robertson
- **Created:** 2023-11-20T20:15:55+00:00
- **Updated:** 2023-11-20T20:18:45+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-43140

## Content
<p><b>Section 7 Mappings</b></p>

<p>While this section spells out existing data field mapping situations (at minimum values), it does not outline what FHIR is proposing for required data or mapping.</p>

<p><b><em><span class="error">&#91;SMR-_* _the mappings are not normative content.  Mappings show how the proposed FHIR resource elements correspond to data elements in the other standards.  This provides insight into the nature of the data (as in your comment on state license number for pharmacists) and traceability for troubleshooting.{*}&#93;</span></b></em></p>

<p>Considerations that should be made from existing NCPDP, PMIX, etc., mappings:</p>
<ul>
	<li>Requester identifier needs to accommodate a state license number for pharmacists without NPIs and the VA health system, which allows nurses to access PDMPs through the VA EMR. All requester identifiers must be unique, so pharmacy NPIs or other placeholders cannot be used in place of individual identifiers.</li>
</ul>


<p><b><em><span class="error">&#91;SMR-_* _FHIR can accommodate any number of different identifiers, including multiple types of identifiers from one organization (an employee number and a practitioner ID from an organization) and the same kind of identifier from different organizations (e.g., state licenses from different states).  Regarding the query request, the requestor does need to be uniquely identified (authentication) and verified as an allowed user (authorization) – which are part of Security (which references US Core) and likely needs additional text to explicitly address your concern{*}&#93;</span></b></em></p>
<ul>
	<li>Requester role must be included in the request elements. Authorization for access to the PDMP is granted by each state after careful consideration of each registrant. The requester role needs to be captured to ensure provider authorization requirements are being met for access to data by appropriate role types.</li>
</ul>


<p><b><em>[SMR-</em></b> <em>Authentication can include Role.  It’s not apparent in the IG as the Security discussion refers to US Core.  Generally, FHIR IG don’t repeat “established and reused” content to minimize the need to update multiple IGs when an underlying capability is updated.  However, points of concern, such as this, can and should be included in our IG, while still referring to US Core for the technical details.</em></p>

<p> __ </p>

<p><em>Related: US Core for Authentication and Authorization focus on OAuth 2 and SMART.  The group needs to discuss if this is viable, or another Authentication scheme is needed.<b>]</b></em></p>
<ul>
	<li>Response type needs to be included in the response elements. We need to know whether the request was successful, had an error, found data, etc. This helps us identify if there are issues within the integration producing a high number of errors and helps us with compliance and investigative work to be able to access our audit trail to identify whether a search was successful and/or produced data.</li>
</ul>


<p><b><em><span class="error">&#91;SMR-_* _The FHIR query response model includes the query in the reported response along with either errors or the found data.  I think this points to the need for examples, and some additional narrative.{*}&#93;</span></b></em></p>

<p><b>Gayle Donaldson</b></p>

<p>Assistant Director</p>

<p>Kansas Board of Pharmacy</p>

<p>800 SW Jackson, Suite 1414</p>

<p>Topeka, KS 66612</p>

<p>(785) 608-1023</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29462: The <Qualifier> element specified means the Qualifier attribute of the <Header>/<From> element, and should be updated to reflect that.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Pharmacy
- **specification:** US Medication FHIR Implementation Guide (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Zhang
- **labels:** PDMP-old-issues
- **Created:** 2020-10-26T16:54:50+00:00
- **Updated:** 2024-03-19T21:25:52+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29462

## Content
<p>We believe the &lt;Qualifier&gt; element specified means the Qualifier attribute of the &lt;Header&gt;/&lt;From&gt; element, and should be updated to reflect that.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>PDMP Request Data Element mapping of Requestor Role from the NCPDP &lt;Qualifier&gt; element to PractitionerRole.code</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-46046: Clarify adoption plan given current US ecosystem for PDMP integration

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Pharmacy
- **specification:** US Prescription Drug Monitoring Program (PDMP) (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Scott M. Robertson
- **reporter:** Cooper Thompson
- **labels:** PDMP-ballot-wip
- **Created:** 2024-05-29T13:26:00+00:00
- **Updated:** 2024-10-15T18:58:50+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-46046

## Content
<p>This IG should describe how it intends to fit into the current PDMP ecosystem in the US.</p>

<p>PDMP integration feels like a solved problem in the US, with the primary limitations being state policy.  There are two PDMP integration patterns that are very widely deployed:</p>
<ul>
	<li>NCPDP integration exists and is widely deployed for states that allow PDMP data to flow between systems.</li>
	<li>SMART on FHIR or other web portal launch into the PDMP is also widely deployed in states that do not allow PDMP data to electronically move between  systems.  </li>
</ul>


<p> </p>

<p>It is unclear to those familiar with the PDMP ecosystem within the US why the investment in this FHIR IG is necessary.  It would be helpful to have the rationale for this investment written down, ideally in the IG itself, or at least in the PSS or the disposition of this Jira.</p>

```

</details>

### Turn 3

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-29461",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

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

## Comments (3)

### smrobertson — 2023-11-28T19:26:00+00:00
<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson — 2023-11-28T19:26:00+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be deferred until the IG is taken up again by the project sponsor and/or the workgroup.</p>

### jiraadmin — 2020-10-26T16:54:49+00:00
<p>Imported from spreadsheet by jduteau - comment #11</p>


## Snapshot
# FHIR-29461: Relative path information should be included to provide clarity around exactly where the data is expected to be pulled from.

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

<p>Each NCPDP Data Element only contains the furthermost child element where the data is being pulled from, but at least relative path information should be included to provide clarity around exactly where the data is expected to be pulled from.  For example, Requestor name should have something like the following in the NCPDP Data Element column when a prescriber is the PDMP requestor:<br/>
&lt;Prescriber&gt;/&lt;Name&gt;/&lt;LastName&gt; and &lt;Prescriber&gt;/&lt;Name&gt;/&lt;FirstName&gt;</p>

<p>And the following when a pharmacist is a PDMP requestor:<br/>
&lt;Pharmacy&gt;/&lt;Pharmacist&gt;/&lt;LastName&gt; and &lt;Pharmacy&gt;/&lt;Pharmacist&gt;/&lt;FirstName&gt;</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>NCPDP Data Element definitions</p>

## Comments

### smrobertson (2023-11-28)

<p>reopened by <a href="https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide" class="external-link" target="_blank" rel="nofollow noopener">PSS-2225 PDMP on FHIR</a> </p>

### smrobertson (2023-11-28)

<p>Reverted previous resolution: Considered for Future Use made 2023-01-18 00:00:00.0 with vote John Hatem / Tim McNeil : 4-0-0//(Impact: null; Category: null; Version: null)//This IG has been withdrawn so these items will be defer

... *(truncated, 4180 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29461".
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

**Assistant:**

Now I have all the data needed. Let me create the output directory and write the report.

<details>
<summary>`powershell` — Ensure output directory exists</summary>

**Arguments:**
```json
{
  "command": "New-Item -ItemType Directory -Path \"C:\\ai\\git\\fhir-augury-content\\prepared\\Pharmacy\" -Force | Out-Null; Write-Output \"Directory ready\"",
  "description": "Ensure output directory exists",
  "initial_wait": 10
}
```

**Result:**
```
Directory ready
<exited with exit code 0>
```

</details>

### Turn 5

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29461.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Pharmacy\\FHIR-29461.md",
  "file_text": "# FHIR-29461: Relative path information should be included to provide clarity around exactly where the data is expected to be pulled from\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-29461](https://jira.hl7.org/browse/FHIR-29461) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Work Group** | Pharmacy |\n| **Specification** | US Medication FHIR Implementation Guide (FHIR) |\n| **Resolution** | Unresolved |\n| **Reporter** | Daniel Zhang |\n| **Assignee** | Unassigned |\n| **Labels** | PDMP-old-issues |\n| **Created** | 2020-10-26 |\n| **Updated** | 2024-03-19 |\n\n## Description\n\nThe submitter reports that each NCPDP Data Element mapping in the PDMP IG only shows the leaf (child) element name without the parent path context. This makes it unclear exactly which XML element is intended, especially when the same element name exists under multiple parents.\n\nThe request is to include relative path information in the NCPDP Data Element column. For example:\n\n- When a **prescriber** is the PDMP requestor, \"Requestor Name\" should show:\n  `<Prescriber>/<Name>/<LastName>` and `<Prescriber>/<Name>/<FirstName>`\n\n- When a **pharmacist** is the PDMP requestor, it should show:\n  `<Pharmacy>/<Pharmacist>/<LastName>` and `<Pharmacy>/<Pharmacist>/<FirstName>`\n\n### Existing Wording\nNCPDP Data Element definitions (leaf element names only, without parent path context).\n\n## Keywords\nNCPDP, PDMP, relative path, data element, mapping, prescriber, pharmacist, requestor, XML path, SCRIPT 2017071\n\n## Comment History\n\n| Date | Author | Summary |\n|------|--------|---------|\n| 2020-10-26 | jiraadmin | Imported from spreadsheet by jduteau (comment #11). |\n| 2023-11-28 | smrobertson | Reverted previous resolution: \"Considered for Future Use\" (voted 2023-01-18, John Hatem / Tim McNeil, 4-0-0). Original deferral reason: the IG had been withdrawn; items deferred until IG taken up again. |\n| 2023-11-28 | smrobertson | Reopened by [PSS-2225 PDMP on FHIR](https://confluence.hl7.org/display/PHAR/US+Prescription+Drug+Monitoring+Program+%28PDMP%29+FHIR+Implementation+Guide) project. |\n\n## Related Jira Tickets\n\n| Key | Title | Relationship |\n|-----|-------|-------------|\n| [FHIR-29459](https://jira.hl7.org/browse/FHIR-29459) | NCPDP mappings need to be updated to reflect how queries use different data elements depending on whether the requestor is a prescriber or pharmacist. | Same concern \u2014 ambiguity in mappings when requestor type varies. Triaged, Highest. |\n| [FHIR-29462](https://jira.hl7.org/browse/FHIR-29462) | The `<Qualifier>` element specified means the Qualifier attribute of the `<Header>/<From>` element, and should be updated to reflect that. | Related \u2014 missing parent path context for `<Qualifier>`. Triaged, Highest. |\n| [FHIR-29463](https://jira.hl7.org/brow

... *(truncated, 8580 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Pharmacy\FHIR-29461.md with 8422 characters
```

</details>


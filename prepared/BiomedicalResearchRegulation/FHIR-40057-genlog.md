# Session Log: FHIR-40057

**Phase:** prepared
**Work Group:** BiomedicalResearchRegulation
**Source File:** `prepared/BiomedicalResearchRegulation/FHIR-40057.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-40057` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:26:40 UTC |
| **Duration** | 96s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 254,457 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-40057
## Work Group: Biomedical Research & Regulation
## Output File: C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-40057.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-40057", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-40057", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-40057", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-40057.md
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
  "id": "FHIR-40057",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-40057: Clarifications and additional details for FHIR-36310, FHIR-36311 and FHIR-36312

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2023-01-10T14:48:08+00:00
- **Updated:** 2023-01-10T21:55:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-40057

## Content
<p>Clarifications and additional details for <a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>, <a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a> and <a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a></p>


<p><a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>	Addition of Populate Functionality to the sIRB Questionnaires<br/>
<a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a>	Utilization of attachments data type as intended when the sIRB questionnaires were created.<br/>
<a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a>	Quality control/corrections/bug fixes/typos</p>

## Snapshot
# FHIR-40057: Clarifications and additional details for FHIR-36310, FHIR-36311 and FHIR-36312

**Status:** Triaged  
**Type:** Technical Correction  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Diane Rodden  
**Work Group:** Biomedical Research & Regulation  
**Specification:** Single Institutional Review Board (sIRB) (FHIR)  
**Created:** 2023-01-10  
**Updated:** 2023-01-10  

## Description

<p>Clarifications and additional details for <a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>, <a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a> and <a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a></p>


<p><a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>	Addition of Populate Functionality to the sIRB Questionnaires<br/>
<a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a>	Utilization of attachments data type as intended when the sIRB questionnaires were created.<br/>
<a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a>	Quality control/corrections/bug fixes/typos</p>

... *(truncated, 4005 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-40057".
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

**Assistant:**

Let me search for more related items and check for any Zulip discussions about sIRB.

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-40057 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 101.044 | jira | FHIR-36310 | Addition of Populate Functionality to the sIRB Questionnaires | sirb, questionnaire, functionality, attachment, adverse, populate, addition, issue, recruitment, medical, letter, event, determination, initiate, material, protocol, continue, study, consent, form, support, review |
| 92.788 | jira | FHIR-36312 | Bug fixes to support overall quality of the sIRB Questionnaires | sirb, questionnaire, bug, adverse, quality, issue, recruitment, intended, medical, fix, letter, event, determination, material, typos, protocol, continue, control, study, consent, form, correction, support, review |
| 87.922 | jira | FHIR-36311 | Utilization of attachments data type as intended when the sIRB questionnaires were created. | sirb, questionnaire, utilization, attachment, adverse, recruitment, intended, medical, data/datum, letter, event, determination, create, material, protocol, continue, type, consent, form, support, review |
| 76.077 | jira | FHIR-36309 | Fixes of the IG narrative pages and better examples of QRs | sirb, questionnaire, functionality, adverse, populate, recruitment, medical, fix, data/datum, letter, event, determination, initiate, material, protocol, continue, study, type, form, review |
| 65.519 | jira | FHIR-40058 | Changes related to hidden fields for external data and additional technical corrections | adverse, recruitment, medical, data/datum, letter, additional, event, determination, initiate, material, protocol, continue, study, consent, form, correction, review |
| 57.991 | jira | FHIR-36310:33765 | FHIR-36310:33765 | 36310, 36311, 36312, title, detail, fhir, href, class |
| 56.424 | jira | FHIR-33623 | AE Valuesets | sirb, del, adverse, key, title, issue, medical, data/datum, fhir, additional, event, link, href, class, review |
| 54.791 | jira | FHIR-33621 | FDA AE Reporting Requirement | sirb, del, adverse, key, title, issue, medical, data/datum, fhir, event, support, link, href, class, review |
| 52.891 | jira | FHIR-40059 | Aligning example QRs to questionnaire changes and bringing IG up to current standards for publishing | adverse, recruitment, medical, letter, event, determination, initiate, material, protocol, continue, study, consent, form, review |
| 44.620 | jira | FHIR-49686 | Add MedicationRequest example for .doNotPerform use case | del, key, title, clarification, addition, issue, data/datum, fhir, additional, create, support, br, link, href, class |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "sIRB single institutional review board questionnaire"
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
  "sources": "github",
  "values": "FHIR-40057,FHIR-36310,FHIR-36311,FHIR-36312,sIRB"
}
```

**Result:**
```
No results found.
```

</details>

### Turn 3

**Assistant:**

Now I have all the data needed. Let me create the report.

<details>
<summary>`powershell` — Ensure output directory exists</summary>

**Arguments:**
```json
{
  "command": "if (-not (Test-Path \"C:\\ai\\git\\fhir-augury-content\\prepared\\BiomedicalResearchRegulation\")) { New-Item -ItemType Directory -Path \"C:\\ai\\git\\fhir-augury-content\\prepared\\BiomedicalResearchRegulation\" -Force }",
  "description": "Ensure output directory exists"
}
```

**Result:**
```

<exited with exit code 0>
```

</details>

### Turn 4

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-40057.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\BiomedicalResearchRegulation\\FHIR-40057.md",
  "file_text": "# FHIR-40057: Clarifications and additional details for FHIR-36310, FHIR-36311 and FHIR-36312\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-40057](https://jira.hl7.org/browse/FHIR-40057) |\n| **Status** | Triaged |\n| **Type** | Technical Correction |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | Biomedical Research & Regulation |\n| **Specification** | Single Institutional Review Board (sIRB) (FHIR) |\n| **Reporter** | Diane Rodden |\n| **Assignee** | Unassigned |\n| **Created** | 2023-01-10 |\n| **Updated** | 2023-01-10 |\n\n## Description\n\nThis ticket requests clarifications and additional details for three previously resolved sIRB Questionnaire tickets:\n\n- **[FHIR-36310](https://jira.hl7.org/browse/FHIR-36310)** \u2014 Addition of Populate Functionality to the sIRB Questionnaires\n- **[FHIR-36311](https://jira.hl7.org/browse/FHIR-36311)** \u2014 Utilization of attachments data type as intended when the sIRB questionnaires were created\n- **[FHIR-36312](https://jira.hl7.org/browse/FHIR-36312)** \u2014 Bug fixes to support overall quality of the sIRB Questionnaires\n\nThe ticket appears to be a follow-up to provide supplementary clarifications or documentation for changes that were already accepted and published under those three tickets. No specific change details are described in the ticket body itself beyond listing the referenced tickets.\n\n## Keywords\n\nsIRB, questionnaire, populate, attachment, technical correction, bug fix, quality, data type, consent form, adverse event, recruitment, protocol\n\n## Referenced Tickets\n\n### FHIR-36310 \u2014 Addition of Populate Functionality to the sIRB Questionnaires\n- **Status:** Published | **Resolution:** Persuasive | **Type:** Technical Correction\n- **Description:** Changes to support populate functionality that was a deliverable mentioned in the IG but not ready in time for balloting.\n- **Comments:** A spreadsheet detailing precise changes for all three tickets (FHIR-36310, FHIR-36311, FHIR-36312) was attached. Reviewed on a BRR conf call on 2022-03-15 with no objections.\n\n### FHIR-36311 \u2014 Utilization of attachments data type as intended when the sIRB questionnaires were created\n- **Status:** Published | **Resolution:** Persuasive | **Type:** Technical Correction\n- **Description:** Incorporated ability to attach documents or specify URLs for large files; changed datatype to attachment for placeholder questions; added support for attachment metadata, repeating attachments, grouping/headers/help text, and consent form upload support.\n\n### FHIR-36312 \u2014 Bug fixes to support overall quality of the sIRB Questionnaires\n- **Status:** Published | **Resolution:** Persuasive | **Type:** Technical Correction\n- **Description:** Quality control/corrections including: fixing random caps text in headin

... *(truncated, 8943 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-40057.md with 8761 characters
```

</details>

### Turn 5

**Assistant:**

Let me get the closely related companion tickets and the Zulip thread for more context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-40057: Clarifications and additional details for FHIR-36310, FHIR-36311 and FHIR-36312

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2023-01-10T14:48:08+00:00
- **Updated:** 2023-01-10T21:55:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-40057

## Content
<p>Clarifications and additional details for <a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>, <a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a> and <a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a></p>


<p><a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>	Addition of Populate Functionality to the sIRB Questionnaires<br/>
<a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a>	Utilization of attachments data type as intended when the sIRB questionnaires were created.<br/>
<a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a>	Quality control/corrections/bug fixes/typos</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-40059: Aligning example QRs to questionnaire changes and bringing IG up to current standards for publishing

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2023-01-10T14:52:06+00:00
- **Updated:** 2023-01-10T21:56:15+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-40059

## Content
<p>Aligning example QRs to questionnaire changes and bringing IG up to current standards for publishing</p>

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# Announcements > New Publication

**Messages:** 10
**First message:** 2020-10-12 06:07:36+00:00
**Last message:** 2020-12-23 14:04:05+00:00
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

### Lynn Laakso — 2020-12-20 06:38:13+00:00
New Publication: STU1 of the HL7 Payer Data Exchange (PDex) Payer Network, Release 1 - US Realm Implementation Guide: hl7.org/fhir/us/davinci-pdex-plan-net/STU1

### Lynn Laakso — 2020-12-20 19:40:08+00:00
New Publication: STU1 of the HL7 Prior-Authorization Support (PAS), Release 1- US Realm FHIR® Implementation Guide: http://hl7.org/fhir/us/davinci-pas/STU1

### Lynn Laakso — 2020-12-22 15:08:27+00:00
New Publication: STU1 of the HL7 Payer Data Exchange (PDex), Release 1 - US Realm FHIR® Implementation Guide: http://hl7.org/fhir/us/davinci-pdex/STU1

### Lynn Laakso — 2020-12-22 17:33:08+00:00
New Publication: STU1 of the HL7 Da Vinci - Coverage Requirements Discovery (CRD), Release 1- US Realm FHIR® Implementation Guide: http://hl7.org/fhir/us/davinci-crd/STU1

### Lynn Laakso — 2020-12-23 14:04:05+00:00
New Publication: STU1 of the HL7 FHIR® Implementation Guide: Payer Coverage Decision Exchange, R1 - US Realm: http://hl7.org/fhir/us/davinci-pcde/STU1

---
*URL: https://chat.fhir.org/#narrow/stream/Announcements/topic/New%20Publication*

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-36310: Addition of Populate Functionality to the sIRB Questionnaires

- **status:** Published
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2022-03-15T18:56:04+00:00
- **Updated:** 2023-04-20T14:00:07+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-36310

## Content
<p>Changes to support populate functionality that was a deliverable mentioned in the IG but not ready in time for balloting</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-36312: Bug fixes to support overall quality of the sIRB Questionnaires

- **status:** Published
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2022-03-15T19:15:01+00:00
- **Updated:** 2023-04-20T14:00:06+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-36312

## Content
<p>Spreadsheet to be attached. </p>

<p>Some examples are:</p>

<ul>
	<li>Correction of random text in all caps in group headings or question text</li>
	<li>Correction of typos and extraneous characters in question text, display items, linkIds and help text.</li>
	<li>Fixed issue where questions with 2 and only 2 accepable answer choices  errroneously had the wrong datatype (open-choice) which was allowing an "Other" selection</li>
	<li>Fixed issue where Study Endpoints question was greyed out/not enabled</li>
	<li>Removed drop down item control extension erroneneously placed on some questions that were not drop downs</li>
	<li>Corrected bug where questions had conditional enablement where it was not intended</li>
</ul>


```

</details>

### Turn 6

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-40057: Clarifications and additional details for FHIR-36310, FHIR-36311 and FHIR-36312

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2023-01-10T14:48:08+00:00
- **Updated:** 2023-01-10T21:55:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-40057

## Content
<p>Clarifications and additional details for <a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>, <a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a> and <a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a></p>


<p><a href="https://jira.hl7.org/browse/FHIR-36310" title="Addition of Populate Functionality to the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36310"><del>FHIR-36310</del></a>	Addition of Populate Functionality to the sIRB Questionnaires<br/>
<a href="https://jira.hl7.org/browse/FHIR-36311" title="Utilization of attachments data type as intended when the sIRB questionnaires were created. " class="issue-link" data-issue-key="FHIR-36311"><del>FHIR-36311</del></a>	Utilization of attachments data type as intended when the sIRB questionnaires were created.<br/>
<a href="https://jira.hl7.org/browse/FHIR-36312" title="Bug fixes to support overall quality of the sIRB Questionnaires" class="issue-link" data-issue-key="FHIR-36312"><del>FHIR-36312</del></a>	Quality control/corrections/bug fixes/typos</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-40059: Aligning example QRs to questionnaire changes and bringing IG up to current standards for publishing

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** Single Institutional Review Board (sIRB) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Diane Rodden
- **Created:** 2023-01-10T14:52:06+00:00
- **Updated:** 2023-01-10T21:56:15+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-40059

## Content
<p>Aligning example QRs to questionnaire changes and bringing IG up to current standards for publishing</p>

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


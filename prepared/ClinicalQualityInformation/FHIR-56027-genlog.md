# Session Log: FHIR-56027

**Phase:** prepared
**Work Group:** ClinicalQualityInformation
**Source File:** `prepared/ClinicalQualityInformation/FHIR-56027.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-56027` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:23:19 UTC |
| **Duration** | 104s |
| **Total Tool Calls** | 18 |
| **Total Tokens** | 305,209 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-56027
## Work Group: Clinical Quality Information
## Output File: C:\ai\git\fhir-augury-content\prepared\ClinicalQualityInformation\FHIR-56027.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-56027", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-56027", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-56027", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Title, metadata, Summary, Details, Keywords, Related Zulip, Related GitHub, three Proposed Dispositions (A: Accept, B: Alternative, C: Decline), and Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\ClinicalQualityInformation\FHIR-56027.md
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
  "id": "FHIR-56027",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-56027: Discrepancies in Encounter Dx Lists:  between EHR vs. Claims data

- **status:** Triaged
- **type:** Question
- **priority:** Medium
- **work_group:** Clinical Quality Information
- **specification:** US QI Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Yanyan Hu
- **Created:** 2026-03-06T18:53:47+00:00
- **Updated:** 2026-03-10T18:52:47+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-56027

## Content
<p>As we agree that the Claims data is an appropriate source for retrieving the POA indicator information.  Since Claims data only captures billing codes, EHRs may contain more Diagnosis codes related to the encounter. How to solve the  discrepancies for data submissions?  Should only billing codes are submitted or submitted all EncDx available in EHR and assigning missing POA with W or other value when EncDx is missing from the billing codes? An appropriate guidance would be helpful.</p>

## Snapshot
# FHIR-56027: Discrepancies in Encounter Dx Lists:  between EHR vs. Claims data

**Status:** Triaged  
**Type:** Question  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Yanyan Hu  
**Work Group:** Clinical Quality Information  
**Specification:** US QI Core (FHIR)  
**Created:** 2026-03-06  
**Updated:** 2026-03-10  

## Description

<p>As we agree that the Claims data is an appropriate source for retrieving the POA indicator information.  Since Claims data only captures billing codes, EHRs may contain more Diagnosis codes related to the encounter. How to solve the  discrepancies for data submissions?  Should only billing codes are submitted or submitted all EncDx available in EHR and assigning missing POA with W or other value when EncDx is missing from the billing codes? An appropriate guidance would be helpful.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-56027".
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

Now let me get keywords and write the report.

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-56027
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| encdx | word | 2 | 15.046 |
| poa | word | 2 | 11.537 |
| dx | word | 2 | 11.004 |
| discrepancy | word | 3 | 10.442 |
| bill | word | 3 | 8.421 |
| claim | word | 5 | 7.681 |
| ehr | word | 3 | 6.702 |
| encounter | fhir_path | 3 | 6.181 |
| solve | word | 1 | 5.831 |
| indicator | word | 1 | 5.813 |
| submit | word | 2 | 5.362 |
| ehrs | word | 1 | 5.306 |
| submission | word | 1 | 5.125 |
| qicore | word | 1 | 4.961 |
| missing | word | 2 | 4.931 |
| diagnosis | word | 1 | 4.791 |
| retrieve | word | 1 | 4.683 |
| helpful | word | 1 | 4.553 |
| list | word | 2 | 4.458 |
| assign | word | 1 | 4.390 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\ClinicalQualityInformation\FHIR-56027.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\ClinicalQualityInformation\\FHIR-56027.md",
  "file_text": "# FHIR-56027: Discrepancies in Encounter Dx Lists: between EHR vs. Claims data\n\n## Metadata\n\n| Field          | Value |\n|----------------|-------|\n| **Ticket**     | [FHIR-56027](https://jira.hl7.org/browse/FHIR-56027) |\n| **Status**     | Triaged |\n| **Type**       | Question |\n| **Priority**   | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | Clinical Quality Information |\n| **Specification** | US QI Core (FHIR) |\n| **Reporter**   | Yanyan Hu |\n| **Assignee**   | Unassigned |\n| **Created**    | 2026-03-06 |\n| **Updated**    | 2026-03-10 |\n\n## Summary\n\nThe submitter asks for guidance on how to handle discrepancies between Encounter diagnosis lists sourced from EHR data versus Claims/billing data when submitting data for quality measures. Specifically:\n\n- Claims data captures only billing codes and is the agreed-upon source for the Present on Admission (POA) indicator.\n- EHRs may contain additional diagnosis codes associated with the encounter that are not present in the billing claim.\n- The question is whether submitters should: (a) submit only billing-sourced diagnosis codes, or (b) submit all EHR encounter diagnoses and assign a missing/unknown POA value (e.g., \"W\") for diagnoses not found in the claim data.\n\nThis is a data-submission guidance question relevant to implementers of QI-Core measures that use Encounter diagnoses and POA indicators.\n\n## Details\n\n### Background\n\nQI-Core STU7 shifted the modeling for principal diagnosis, principal procedure, and present on admission (POA) from `Encounter.diagnosis` to the `Claim` profile. This decision\u2014documented in the QI-Core IG and discussed in companion ticket [FHIR-56026](https://jira.hl7.org/browse/FHIR-56026)\u2014was based on implementer feedback that these concepts are more accurately captured via billing/claim data where medical record coders make final determinations.\n\nHowever, this creates a practical problem: EHR systems may record more encounter diagnoses than what appears on the claim. When quality measures require both the full encounter diagnosis list and POA status, implementers need clear guidance on how to reconcile the two sources.\n\n### Related Prior Work\n\nThe QI-Core community has addressed related POA modeling issues several times:\n\n- **[FHIR-23790](https://jira.hl7.org/browse/FHIR-23790)** (Published, Persuasive) \u2014 Added the `presentOnAdmissionIndicator` extension to QI-Core Encounter.diagnosis, originating from QDM 5.5 requirements.\n- **[FHIR-38181](https://jira.hl7.org/browse/FHIR-38181)** (Published, Persuasive) \u2014 Addressed how to capture POA for claim data following UB-04 guidelines, specifically the exempt-from-POA code \"1\" not included in the original value set.\n- **[FHIR-42054](https://jira.hl7.org/browse/FHIR-42054)** (Published, Persuasive) \u2014 Updated the `onAdmission` required

... *(truncated, 10578 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\ClinicalQualityInformation\FHIR-56027.md with 10378 characters
```

</details>


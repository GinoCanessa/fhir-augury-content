# Session Log: FHIR-37158

**Phase:** prepared
**Work Group:** PatientEmpowerment
**Source File:** `prepared/PatientEmpowerment/FHIR-37158.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-37158` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:22:34 UTC |
| **Duration** | 108s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 270,952 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-37158
## Work Group: Patient Empowerment
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientEmpowerment\FHIR-37158.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-37158", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-37158", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-37158", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules
- Use ONLY data from MCP/CLI. Do not fabricate.
- Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientEmpowerment\FHIR-37158.md
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
  "id": "FHIR-37158",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

## Comments (3)

### lynn_laakso — 2025-07-10T16:13:54+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2025-07-10T16:13:54+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-10-17 00:00:00.0 with vote Jason Vogt / Rachel Richesson : 7-0-0//(Impact: null; Category: null; Version: null)//Will consider for future implementation once further code changes are no longer considered</p>

### vlorenzi — 2022-07-11T20:36:16+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=rrichesson" class="user-hover" rel="rrichesson">Rachel Richesson</a> can you help with this issue?</p>


## Snapshot
# FHIR-37158: Defining URL should be anchored in THO. 1.

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Joan Harper  
**Work Group:** Patient Empowerment  
**Specification:** Patient Corrections (FHIR)  
**Labels:** Vocabulary  
**Created:** 2022-05-02  
**Updated:** 2025-07-10  

## Description

<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeS

... *(truncated, 4852 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-37158" (1 results)

- [jira] FHIR-37158 → [confluence] 81034628
  **Source:** Defining URL should be anchored in THO. 1.
  **Type:** mentions
  **Context:** ...to register the Code System in THO. See the following links for best practices: https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Intern...
  **Score:** 0.78
  **Updated:** 2025-07-10T16:13:54+00:00
**Warnings:**
- Value 'FHIR-37158' is not a valid Zulip message ID

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
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "PatientCorrectionBusinessStatus, patient corrections code system THO",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-37158 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 147.950 | jira | FHIR-37159 | Defining URL should be anchored in THO. 2. | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, h3, vocabulary, register, contact, hl7, utg, ron, parker, canonical, correction, r5, existingwording, 3a, define, system, question, terminology, represent, ticket, specification, import, code, create, word, existing, noopener, blank, patient, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 147.950 | jira | FHIR-37160 | Defining URL should be anchored in THO.  3 | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, h3, vocabulary, register, contact, hl7, utg, ron, parker, canonical, correction, r5, existingwording, 3a, define, system, question, terminology, represent, ticket, specification, import, code, create, word, existing, noopener, blank, patient, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 147.950 | jira | FHIR-37161 | Defining URL should be anchored in THO.  4 | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, h3, vocabulary, register, contact, hl7, utg, ron, parker, canonical, correction, r5, existingwording, 3a, define, system, question, terminology, represent, ticket, specification, import, code, create, word, existing, noopener, blank, patient, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 141.876 | jira | FHIR-37192 | Defining URL should be anchored in THO. 1. | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, h3, register, contact, hl7, utg, ron, parker, canonical, r5, existingwording, 3a, define, system, question, terminology, 1, represent, ticket, specification, import, code, create, word, existing, noopener, blank, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 139.711 | jira | FHIR-37149 | Defining URL should be anchored in THO. 1. | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, h3, register, contact, hl7, utg, ron, parker, canonical, r5, existingwording, 3a, define, system, question, terminology, 1, represent, ticket, specification, import, code, create, word, existing, noopener, blank, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 138.910 | jira | FHIR-37150 | Defining URL should be anchored in THO. 2. | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, h3, register, contact, hl7, utg, ron, parker, canonical, r5, existingwording, 3a, define, system, question, terminology, represent, ticket, specification, import, status, code, create, word, existing, noopener, blank, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 133.184 | jira | FHIR-38533 | Defining URL should be anchored in THO. 1. | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, register, contact, hl7, utg, ron, parker, canonical, r5, define, system, question, terminology, 1, represent, ticket, specification, import, code, create, noopener, blank, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 132.233 | jira | FHIR-38431 | Defining URL should be anchored in THO. 1. | codesystemidentifiertaskforce.pptx, codesystemidentifiertaskforce, pptx, anchor, practice, url, org, tsmg, register, contact, hl7, utg, ron, parker, canonical, r5, define, system, question, terminology, 1, represent, ticket, specification, import, code, create, noopener, blank, target, nofollow, external, br, link, rel, comment, href, fhir, class |
| 132.128 | jira | FHIR-38447 | Defining URL should be anch

... *(truncated, 7172 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-37158
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| codesystemidentifiertaskforce.pptx | word | 2 | 8.514 |
| codesystemidentifiertaskforce | word | 2 | 8.514 |
| pptx | word | 2 | 8.165 |
| anchor | word | 3 | 6.541 |
| practice | word | 2 | 5.047 |
| url | word | 3 | 4.711 |
| org | word | 2 | 4.645 |
| tsmg | word | 1 | 4.339 |
| h3 | word | 2 | 4.182 |
| vocabulary | word | 1 | 4.093 |
| register | word | 1 | 3.978 |
| contact | word | 1 | 3.784 |
| hl7 | word | 2 | 3.725 |
| business | word | 1 | 3.669 |
| utg | word | 1 | 3.639 |
| ron | word | 1 | 3.303 |
| parker | word | 1 | 3.303 |
| canonical | word | 1 | 3.299 |
| correction | word | 1 | 3.246 |
| r5 | word | 1 | 3.009 |
| existingwording | word | 1 | 2.971 |
| 3a | word | 1 | 2.887 |
| define | word | 2 | 2.868 |
| system | word | 2 | 2.788 |
| question | word | 1 | 2.745 |
| terminology | word | 1 | 2.705 |
| 1 | word | 3 | 2.566 |
| represent | word | 1 | 2.564 |
| ticket | word | 1 | 2.562 |
| specification | word | 1 | 2.455 |
| import | word | 1 | 2.422 |
| status | word | 1 | 2.411 |
| code | word | 2 | 2.376 |
| create | word | 1 | 2.170 |
| word | word | 1 | 2.080 |
| existing | word | 1 | 2.077 |
| noopener | word | 3 | 1.926 |
| blank | word | 3 | 1.919 |
| patient | fhir_path | 1 | 1.901 |
| target | word | 3 | 1.876 |
| nofollow | word | 3 | 1.829 |
| external | word | 3 | 1.812 |
| br | word | 1 | 1.763 |
| link | word | 4 | 1.746 |
| rel | word | 3 | 1.651 |
| comment | word | 1 | 1.562 |
| href | word | 3 | 1.537 |
| fhir | word | 1 | 1.361 |
| class | word | 3 | 1.360 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientEmpowerment\FHIR-37158.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientEmpowerment\\FHIR-37158.md",
  "file_text": "# FHIR-37158: Defining URL should be anchored in THO. 1.\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-37158](https://jira.hl7.org/browse/FHIR-37158) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Work Group** | Patient Empowerment |\n| **Specification** | Patient Corrections (FHIR) |\n| **Reporter** | Joan Harper |\n| **Assignee** | Unassigned |\n| **Labels** | Vocabulary |\n| **Created** | 2022-05-02 |\n| **Updated** | 2025-07-10 |\n\n---\n\n## Summary\n\nThis ticket requests that the `PatientCorrectionBusinessStatus` CodeSystem canonical URL be migrated from `hl7.org/fhir` to `terminology.hl7.org` (THO \u2014 the HL7 Terminology server). Per HL7 best practices established by the TSMG Code System Identifier Task Force, code system canonical URLs should be anchored in THO rather than in the FHIR IG namespace. A corresponding UTG ticket must be created to register the code system in THO.\n\nThe current (incorrect) canonical URL is:\n`http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus`\n\nThis ticket was originally resolved as \"Considered for Future Use\" in October 2022 (voted 7-0-0, Jason Vogt / Rachel Richesson) with the rationale that it would be considered once further code changes were no longer pending. It was re-opened on 2025-07-10 by Lynn Laakso following STU1 publication.\n\n---\n\n## Details\n\n### Existing Wording\n\nThe current CodeSystem canonical URL:  \n`http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus`\n\n### Requested Change\n\nMigrate the canonical URL to be rooted in THO (e.g., `http://terminology.hl7.org/CodeSystem/PatientCorrectionBusinessStatus` or as determined by UTG registration). A UTG ticket must be created to register the code system.\n\n### References Cited\n\n- [TSMG Code System Identifier Task Force (Jan 2022)](https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&modificationDate=1644006505101&api=v2)\n- [R5 Terminologies Best Practice](http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system)\n\n### Comment History\n\n| Date | Author | Comment |\n|------|--------|---------|\n| 2025-07-10 | lynn_laakso | Re-open post STU1 publication |\n| 2025-07-10 | lynn_laakso | Reverted previous resolution: \"Considered for Future Use\" (2022-10-17, vote 7-0-0, Jason Vogt / Rachel Richesson). Original rationale: will consider once further code changes are no longer pending. |\n| 2022-07-11 | vlorenzi | Asked Rachel Richesson for help with this issue |\n\n---\n\n## Keywords\n\n`CodeSystem`, `canonical URL`, `THO`, `terminology.hl7.org`, `UTG`, `PatientCorrectionBusinessStatus`, `TSMG`, `vocabulary`, `Patient Corrections`\n\n---\n\n## Related Jira Tickets\n\nThese are sibling tick

... *(truncated, 7859 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientEmpowerment\FHIR-37158.md with 7696 characters
```

</details>

### Turn 4

**Assistant:**

Let me get details on the sibling tickets that are part of the same THO anchoring effort for Patient Corrections.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37160: Defining URL should be anchored in THO.  3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:19+00:00
- **Updated:** 2025-07-10T16:13:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37160

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes</a></p>

<p>(<b>Comment 3 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37161: Defining URL should be anchored in THO.  4

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:21+00:00
- **Updated:** 2025-07-10T16:13:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37161

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionTaskTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionTaskTypes</a></p>

<p>(<b>Comment 4 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "patient corrections terminology THO code system canonical URL"
}
```

**Result:**
```
No results found.
```

</details>

### Turn 5

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37159: Defining URL should be anchored in THO. 2.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:16+00:00
- **Updated:** 2025-07-10T16:13:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37159

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionCommunicationTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionCommunicationTypes</a></p>

<p>(<b>Comment 2 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37161: Defining URL should be anchored in THO.  4

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:21+00:00
- **Updated:** 2025-07-10T16:13:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37161

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionTaskTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionTaskTypes</a></p>

<p>(<b>Comment 4 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "github",
  "values": "PatientCorrectionOutputTypes, patient-corrections CodeSystem THO"
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
  "values": "patient corrections terminology, patient-corrections code system url"
}
```

**Result:**
```
## Search Results (6 total, showing 6)

### [zulip] 555496991 — [analytics on FHIR] 11/11 Meeting Recording & Notes
- **Score:** 0.69
- **Updated:** 2025-11-14T03:03:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/analytics%20on%20FHIR/topic/11%2F11%20Meeting%20Recording%20%26%20Notes/near/555496991
- **Snippet:** ...when using multiple <b>patient</b> views from different contexts (e.g., FHIR <b>patient</b>, OMOP <b>patient</b>, IPS <b>patient</b>) Nikolai noted that in...

### [zulip] 572035975 — [argonaut] US Core V9 Ballot Reconciliation
- **Score:** 0.66
- **Updated:** 2026-02-05T00:15:52+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/argonaut/topic/US%20Core%20V9%20Ballot%20Reconciliation/near/572035975
- **Snippet:** ...Device.<b>patient</b> (RikiM) Persuasive Change Impact: Non-substantive (Clarification ) FHIR-54226 : Relationship With Other IGs (3.7 technical <b>corrections</b>) (jen...

### [zulip] 541046991 — [argonaut] Writing Clinical Notes
- **Score:** 0.29
- **Updated:** 2025-09-23T15:40:10+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/argonaut/topic/Writing%20Clinical%20Notes/near/541046991
- **Snippet:** ...These changes make <b>corrections</b> easier, clarify discovery, and keep things simple without over-specifying server policies. Full revised spec: here...

### [zulip] 298702162 — [IPS] IPS Publication Updates (Sept 2022)
- **Score:** 0.04
- **Updated:** 2022-09-14T04:49:03+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IPS/topic/IPS%20Publication%20Updates%20%28Sept%202022%29/near/298702162
- **Snippet:** ...Finally, many changes have happened in SNOMED <b>terminology</b> and FHIR usage patterns that affect IPS implementations. In late 2021 during...

### [zulip] 276614534 — [IG creation] NPE with Publishing Content Failed: null
- **Score:** 0.03
- **Updated:** 2022-03-25T12:59:19+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IG%20creation/topic/NPE%20with%20Publishing%20Content%20Failed%3A%20null/near/276614534
- **Snippet:** I have started getting a NullPointerException in my local build for the <b>Patient</b> Request for <b>Corrections</b> IG. Not certain whether...

### [zulip] 282417915 — [IG creation] "Dependency analysis" downloading lots of packages
- **Score:** 0.00
- **Updated:** 2022-05-15T16:57:44+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IG%20creation/topic/%22Dependency%20analysis%22%20downloading%20lots%20of%20packages/near/282417915
- **Snippet:** ...1.0-ballot hl7.fhir.uv.<b>patient</b>-<b>corrections</b>#current hl7.fhir.uv.<b>patient</b>-<b>corrections</b>#1.0.0-ballot hl7.fhir...


```

</details>

### Turn 6

**Assistant:**

Let me fetch the sibling tickets to understand the full scope and check for any Patient Corrections IG-specific context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37159: Defining URL should be anchored in THO. 2.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:16+00:00
- **Updated:** 2025-07-10T16:13:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37159

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionCommunicationTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionCommunicationTypes</a></p>

<p>(<b>Comment 2 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37160: Defining URL should be anchored in THO.  3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:19+00:00
- **Updated:** 2025-07-10T16:13:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37160

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes</a></p>

<p>(<b>Comment 3 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-query_jira_issues`</summary>

**Arguments:**
```json
{
  "specifications": "Patient Corrections (FHIR)",
  "limit": 20,
  "sortBy": "updated_at",
  "sortOrder": "desc"
}
```

**Result:**
```
## Jira Query Results
(20 results)

- **FHIR-53782** [Triaged] The corrected data needs Provenance  WG: Security  Spec: Patient Corrections (FHIR)  Updated: 2026-03-24T08:26:21-05:00
- **FHIR-37160** [Triaged] Defining URL should be anchored in THO.  3  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:57-05:00
- **FHIR-36876** [Triaged] Can a disagreement be persuasive?  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:57-05:00
- **FHIR-37162** [Triaged] Defining URL should be anchored in THO.  5  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:56-05:00
- **FHIR-37159** [Triaged] Defining URL should be anchored in THO. 2.  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:56-05:00
- **FHIR-37161** [Triaged] Defining URL should be anchored in THO.  4  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:56-05:00
- **FHIR-37163** [Triaged] Defining URL should be anchored in THO.  6  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:55-05:00
- **FHIR-37165** [Triaged] Defining URL should be anchored in THO.  8  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:55-05:00
- **FHIR-37158** [Triaged] Defining URL should be anchored in THO. 1.  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:54-05:00
- **FHIR-37164** [Triaged] Defining URL should be anchored in THO.  7  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:54-05:00
- **FHIR-37398** [Published] The simplest use case (probably not following a HIPAA Request for Amendment workflow)  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:03-05:00
- **FHIR-37048** [Published] EHR's record of a prior patient visit is at odds with the patient's recollection.  Again, how would this be adjudicated?  Human-to-human interaction?  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:03-05:00
- **FHIR-37394** [Published] Add 'request correction received' (from RequestFulfiller to CorrectionRequester)  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:03-05:00
- **FHIR-36938** [Published] 404 error on Downloads webpage  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:03-05:00
- **FHIR-37051** [Published] See typo in the second sentence.  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:02-05:00
- **FHIR-37052** [Published] See the typo in the third sentence.  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:02-05:00
- **FHIR-37386** [Published] The only example available lists a DocumentReference which has unclear resolving rules  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:02-05:00
- **FHIR-37043** [Published] Meaning and proper use of concept medRecCxDenialDisagree is confusing  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:02-05:00
- **FHIR-37390** [Published] The minimum scenario for sending a  corrections request. Adding a scenario in which the patient will be notified of the receivement of the request.  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:02-05:00
- **FHIR-37045** [Published] Not sure how further exchange of data using FHIR in 1.2.4 will resolve this impasse.  WG: Patient Empowerment  Spec: Patient Corrections (FHIR)  Updated: 2025-07-10T11:13:02-05:00

```

</details>

### Turn 7

**Assistant:**

Good — there's a family of related THO anchor tickets. Let me get details on the siblings and the Zulip thread.

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37158",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37159",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37159: Defining URL should be anchored in THO. 2.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:16+00:00
- **Updated:** 2025-07-10T16:13:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37159

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionCommunicationTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionCommunicationTypes</a></p>

<p>(<b>Comment 2 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37160",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37160: Defining URL should be anchored in THO.  3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:19+00:00
- **Updated:** 2025-07-10T16:13:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37160

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes</a></p>

<p>(<b>Comment 3 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37161",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37161: Defining URL should be anchored in THO.  4

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:21+00:00
- **Updated:** 2025-07-10T16:13:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37161

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionTaskTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionTaskTypes</a></p>

<p>(<b>Comment 4 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37163",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37163: Defining URL should be anchored in THO.  6

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:23+00:00
- **Updated:** 2025-07-10T16:13:55+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37163

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/2022MAY/ValueSet-PatientCorrectionCommunicationTypesVS.html" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/2022MAY/ValueSet-PatientCorrectionCommunicationTypesVS.html</a></p>

<p>(<b>Comment 6 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37164",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37164: Defining URL should be anchored in THO.  7

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:24+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37164

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>Only those with required binding to a 'code' data type should be anchored in hl7.org/FHIR</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/ValueSet/PatientCorrectionOutputTypesVS" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/ValueSet/PatientCorrectionOutputTypesVS</a></p>

<p>(<b>Comment 7 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-37165",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-37165: Defining URL should be anchored in THO.  8

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:25+00:00
- **Updated:** 2025-07-10T16:13:55+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37165

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>Only those with required binding to a 'code' data type should be anchored in hl7.org/FHIR</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/ValueSet/PatientCorrectionTaskTypesVS" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/ValueSet/PatientCorrectionTaskTypesVS</a></p>

<p>(<b>Comment 8 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# patient empowerment > project - patient corrections

**Messages:** 30
**First message:** 2020-09-18 22:30:03+00:00
**Last message:** 2020-09-25 15:16:10+00:00
**Participants:** Virginia Lorenzi, Lloyd McKenzie, Michele Mottini, John Moehrke, Vassil Peytchev, Abbie Watson, Dave deBronkart

## Messages

### Virginia Lorenzi — 2020-09-18 22:30:03+00:00
Hey FHIR architects - what is a good way to represent that data has been amended using FHIR?

### Lloyd McKenzie — 2020-09-18 22:30:48+00:00
Provenance?

### Virginia Lorenzi — 2020-09-18 22:55:19+00:00
Like this. My understanding is - A patient requests that their smoking status is corrected - I DON"T SMOKE! The clinician is not able to update the smoking status directly but instead amends the field with a corrected note.

### Lloyd McKenzie — 2020-09-18 23:05:34+00:00
Have you ever seen a system that had the ability to capture correction notes on a per-field basis? (Or even a per record basis?)

### Virginia Lorenzi — 2020-09-18 23:14:46+00:00
Perhaps - I am trying to figure that out.

### Michele Mottini — 2020-09-19 01:02:56+00:00
(deleted)

### John Moehrke — 2020-09-19 15:22:13+00:00
Provenance is the right solution. Given that the old and new version of the target resource exist (provided versioning FHIR), one can always see the DIFF. Thus the Provenance covers the DIFF made between old and new. The Provenance would point at the old, and new as normal; but would also have an .entity that points at the patient request to change. Thus it is clear WHY. I might argue that it is even appropriate to record a Provenance for a requested change that resulted in no change.

### Virginia Lorenzi — 2020-09-20 00:00:52+00:00
Thanks guys for advice on provenance.

### Lloyd McKenzie — 2020-09-20 03:02:24+00:00
The requested change would be a Task. If there was a Provenance it would be on the status change of the Task.

### Virginia Lorenzi — 2020-09-23 07:03:04+00:00
@Lloyd McKenzie I have checked with medical records departments of two hospitals and I know certain data fields do not have the same formal process for correction. For example - demographics changes do not require the same formal process. I checked my patient portal to see what it would allow me to update (and then it auto-flows back to EHR) - I could update all demographics, emergency contact information, and insurance. I have a feeling I might be able to update my own med list as well but lets ignore that for now. Clinical correction requests fall into the formal process.

### Virginia Lorenzi — 2020-09-23 07:34:30+00:00
Another question. There is a formal paper process in which a patient requests a change to a clinical part of their record. The provider sends correspondence saying request received and status. Clearly the response to the request will not be synchronous. And the actual change is not the indicator the change happened - a formal communication saying the change occurred. Lets say I use Task. Do I do an API PUT Task to the EHR?

### Lloyd McKenzie — 2020-09-23 13:00:58+00:00
First step would be a POST of the Task to the EHR (to create it). Then the patient app would either poll the Task (query on a semi-regular basis) to see if it had changed or subscribe to the Task to receive a notification of when it had changed. (Because patient apps wouldn't likely have reliability availability or location, polling would presumably be most common.) The EHR would update the Task to change status & business status.

### Vassil Peytchev — 2020-09-23 15:10:30+00:00
@Virginia Lorenzi if you want to see a visual representation of how to handle exchanges using Task between initiator and recipient, you can look at this part of a current ballot

### Abbie Watson — 2020-09-23 17:09:50+00:00
And those formal processes differ by state. Not drastically, but to some degree.

### Virginia Lorenzi — 2020-09-23 17:29:24+00:00
Abigail - yes I stumbled across NY state's ones and they are d

... *(truncated, 7125 chars total)*
```

</details>

### Turn 8

**Assistant:**

Let me fetch details on the sibling tickets in this series and search for Zulip discussions.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37160: Defining URL should be anchored in THO.  3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:19+00:00
- **Updated:** 2025-07-10T16:13:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37160

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes</a></p>

<p>(<b>Comment 3 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37164: Defining URL should be anchored in THO.  7

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:24+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37164

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>Only those with required binding to a 'code' data type should be anchored in hl7.org/FHIR</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/ValueSet/PatientCorrectionOutputTypesVS" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/ValueSet/PatientCorrectionOutputTypesVS</a></p>

<p>(<b>Comment 7 - imported by: Ron G. Parker</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "patient corrections THO ValueSet canonical URL terminology"
}
```

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

### Turn 9

**Assistant:**

Let me fetch details on the sibling THO tickets to understand the broader context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37158: Defining URL should be anchored in THO. 1.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:14+00:00
- **Updated:** 2025-07-10T16:13:54+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37158

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionBusinessStatus</a></p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

## Comments (3)

### lynn_laakso — 2025-07-10T16:13:54+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2025-07-10T16:13:54+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-10-17 00:00:00.0 with vote Jason Vogt / Rachel Richesson : 7-0-0//(Impact: null; Category: null; Version: null)//Will consider for future implementation once further code changes are no longer considered</p>

### vlorenzi — 2022-07-11T20:36:16+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=rrichesson" class="user-hover" rel="rrichesson">Rachel Richesson</a> can you help with this issue?</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-37160: Defining URL should be anchored in THO.  3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Empowerment
- **specification:** Patient Corrections (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Vocabulary
- **Created:** 2022-05-02T17:14:19+00:00
- **Updated:** 2025-07-10T16:13:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37160

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>See the following links for best practices:<br/>
<a href="https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/download/attachments/81034628/January2022_TSMG_Internal_CodeSystemIdentifierTaskForce.pptx?version=1&amp;modificationDate=1644006505101&amp;api=v2</a><br/>
<a href="http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/5.0.0-snapshot1/terminologies.html#system</a> (this is in the R5 specification and represents best practice)</p>

<p>Contact TSMG if you have further questions.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p><a href="http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/uv/patient-corrections/CodeSystem/PatientCorrectionOutputTypes</a></p>

<p>(<b>Comment 3 - imported by: Ron G. Parker</b>)</p>

## Comments (3)

### lynn_laakso — 2025-07-10T16:13:57+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2025-07-10T16:13:57+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-10-17 00:00:00.0 with vote Jason Vogt / Rachel Richesson : 7-0-0//(Impact: null; Category: null; Version: null)//Will consider for future implementation once further code changes are no longer considered</p>

### vlorenzi — 2022-10-02T07:52:13+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=rrichesson" class="user-hover" rel="rrichesson">Rachel Richesson</a> to follow up</p>


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


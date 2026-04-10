# Session Log: FHIR-10635

**Phase:** prepared
**Work Group:** PatientCare
**Source File:** `prepared/PatientCare/FHIR-10635.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-10635` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:20:04 UTC |
| **Duration** | 106s |
| **Total Tool Calls** | 18 |
| **Total Tokens** | 265,931 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-10635
## Work Group: Patient Care
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10635.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-10635", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-10635", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-10635", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules
- Use ONLY data from MCP/CLI. Do not fabricate.
- Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10635.md
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
  "id": "FHIR-10635",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-10635: QA 5a: Resource references exist in both directions for Condition and ClinicalImpression

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Michelle Miller
- **Created:** 2016-09-09T21:54:07+00:00
- **Updated:** 2019-12-12T23:31:16+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10635

## Content
<p>Resource references exist in both directions for Condition and ClinicalImpression as follows: </p>

<p>         Condition.stage.assessment (to ClinicalImpression)</p>

<p>         ClinicalImpression.problem &amp; ClinicalImpression.finding.item<span class="error">&#91;x&#93;</span> (to Condition)</p>

<p>         Per QA 5a:</p>

<p>         Elements with a type of Resource Reference should be reviewed such that a given relationship shall only be represented in one resource, not both (and should generally be present on the resource that is normally created second - e.g. Procedure is usually created after Encounter, so reference would live on Procedure)</p>

<p>                     <a href="http://wiki.hl7.org/index.php?title=DSTU_QA_Guidelines" class="external-link" target="_blank" rel="nofollow noopener">http://wiki.hl7.org/index.php?title=DSTU_QA_Guidelines</a></p>

## Comments (5)

### melva peters — 2019-01-08T17:38:55+00:00
<p>July 5, 2018: George / Emma:  8-0-0 - Not Persuasive</p>

### michelle.m.miller — 2018-07-05T21:23:09+00:00
<p>+               <b>Past Vote</b>            +:  Deferred on Jan 31 2017 - Rob/Elaine:  7-0-1</p>

<p>         July 5, 2018 - discussion about whether to defer due to lack of ClinicalImpression maturity.</p>

### michelle.m.miller — 2017-02-01T03:34:03+00:00
<p>The note has been applied, but leaving tracker in Deferred status to address the circular reference after STU3.</p>

### michelle.m.miller — 2017-01-26T22:59:10+00:00
<p>ClinicalImpression is not mature enough to resolve this issue.  Ask MnM for an exemption on the QA checklist (re: Condition having a circular reference with ClinicalImpression)</p>

### mckenzie — 2016-09-12T17:21:22+00:00
<p>This one's a little tricky.  In practice, it's the Condition.stage that's pointing to ClinicalImpression, not Condition as a whole.  However, the reality is that ClinicalImpression.problem or ClinicalImpression.finding.item<span class="error">&#91;x&#93;</span> could easily mean both the Condition and the stage were created as part of the ClinicalImpression.  So we certainly need some guidance.  Not sure what it should be though <img class="emoticon" src="https://jira.hl7.org/images/icons/emoticons/sad.png" height="16" width="16" align="absmiddle" alt="" border="0"/></p>


## Snapshot
# FHIR-10635: QA 5a: Resource references exist in both directions for Condition and ClinicalImpression

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Michelle Miller  
**Work Group:** Patient Care  
**Specification:** FHIR Core (FHIR)  
**Created:** 2016-09-09  
**Updated:** 2019-12-12  

## Description

<p>Resource references exist in both directions for Condition and ClinicalImpression as follows: </p>

<p>         Condition.stage.assessment (to ClinicalImpression)</p>

<p>         ClinicalImpression.problem &amp; ClinicalImpression.finding.item<span class="error">&#91;x&#93;</span> (to Condition)</p>

<p>         Per QA 5a:</p>

<p>         Elements with a type of Resource Reference should be reviewed such that a given relationship shall only be represented in one resource, not both (and should generally be present on the resource that is normally created second - e.g. Procedure is usually created after Encounter, so reference would live on Procedure)</p>

<p>                     <a href="http://wiki.hl7.org/index.php?title=DSTU_QA_Guidelines

... *(truncated, 6108 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-10635" (6 results)

- [jira] FHIR-10635 → [fhir] Condition.stage.assessment
  **Source:** QA 5a: Resource references exist in both directions for Condition and ClinicalImpression
  **Type:** mentions
  **Context:** ...ences exist in both directions for Condition and ClinicalImpression as follows: Condition.stage.assessment (to ClinicalImpression) ClinicalImpression.problem & ...
  **Score:** 0.05
  **Updated:** 2019-12-12T23:31:16+00:00
- [jira] FHIR-10635 → [fhir] ClinicalImpression.problem
  **Source:** QA 5a: Resource references exist in both directions for Condition and ClinicalImpression
  **Type:** mentions
  **Context:** ...inicalImpression as follows: Condition.stage.assessment (to ClinicalImpression) ClinicalImpression.problem & ClinicalImpression.finding.item [x] (to Condition) ...
  **Score:** 0.05
  **Updated:** 2019-12-12T23:31:16+00:00
- [jira] FHIR-10635 → [fhir] ClinicalImpression.finding.item
  **Source:** QA 5a: Resource references exist in both directions for Condition and ClinicalImpression
  **Type:** mentions
  **Context:** ...Condition.stage.assessment (to ClinicalImpression) ClinicalImpression.problem & ClinicalImpression.finding.item [x] (to Condition) Per QA 5a: Elements with a ty...
  **Score:** 0.05
  **Updated:** 2019-12-12T23:31:16+00:00
- [jira] FHIR-10635 → [fhir] Condition.stage
  **Source:** QA 5a: Resource references exist in both directions for Condition and ClinicalImpression
  **Type:** mentions
  **Context:** This one's a little tricky. In practice, it's the Condition.stage that's pointing to ClinicalImpression, not Condition as a whole....
  **Score:** 0.05
  **Updated:** 2019-12-12T23:31:16+00:00
- [zulip] 153875629 → [jira] FHIR-10635
  **Source:** [implementers] Using ClinicalImpression for a cancer therapy decisions
  **Type:** mentions
  **Context:** ...t-STU3 around circular references between Condition and ClinicalImpression (per GF#10635 ). As such, let me take the question back to Patient Care to discuss to...
  **Score:** 0.01
  **Updated:** 2017-03-08T22:52:04+00:00
- [zulip] 153846911 → [jira] FHIR-10635
  **Source:** [committers] tracker-item
  **Type:** mentions
  **Context:** GF#10635 : QA 5a: Resource references exist in both directions for Condition and...
  **Score:** 0.01
  **Updated:** 2016-09-09T21:48:27+00:00
**Warnings:**
- Value 'FHIR-10635' is not a valid Zulip message ID

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

Now let me fetch the related Zulip threads and search for related Jira tickets.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "stream": "implementers",
  "topic": "Using ClinicalImpression for a cancer therapy decisions",
  "limit": 30
}
```

**Result:**
```
# implementers > Using ClinicalImpression for a cancer therapy decisions

**Messages:** 9
**First message:** 2017-03-08 09:00:48+00:00
**Last message:** 2017-03-15 18:47:52+00:00
**Participants:** Marten Smits, Michelle (Moseman) Miller, Lloyd McKenzie, Sadiq Saleh

## Messages

### Marten Smits — 2017-03-08 09:00:48+00:00
We are planning on using ClinicalImpression to bundle conditions and observations as input for a CDS tool. In our case: A specific type of cancer including its stage (Condition) and the presence of some types of genes (Observations). Is ClinicalImpression supposed to be used for this? @Michelle (Moseman) Miller

### Michelle (Moseman) Miller — 2017-03-08 22:52:04+00:00
ClinicalImpression is still in draft (FMM=0) as the scope continues to be discussed and refined. Furthermore, we identified some QA issues that we need to address post-STU3 around circular references between Condition and ClinicalImpression (per GF#10635 ). As such, let me take the question back to Patient Care to discuss tomorrow (Thurs, March 9) and get back to you.

### Marten Smits — 2017-03-09 08:40:44+00:00
Great, thank you!

### Michelle (Moseman) Miller — 2017-03-09 23:31:18+00:00
In general, the Patient Care WG discussion included: ClinicalImpression is not intended to bundle Conditions and Observations -- why not use the Bundle resource? ClinicalImpression is intended to represent the clinical assessment ("A" in SOAP notes)

### Lloyd McKenzie — 2017-03-10 01:39:16+00:00
The Bundle resource is a transport resource, not a semantic resource.

### Marten Smits — 2017-03-15 10:49:45+00:00
@Michelle (Moseman) Miller How do you assess (A in SOAP), without linking to Conditions and Observations? Bundle is a no-go as @Lloyd McKenzie just said, since it's for infrastructural purposes only.

### Michelle (Moseman) Miller — 2017-03-15 14:54:07+00:00
My comments above were terse since I was typing while simultaneously chairing the conference call -- sorry about that. To elaborate, I don't think Patient Care had enough context to answer your question definitively. We couldn't tell if you were just needing a transport (e.g. a way to "bundle" input for CDS purposes) or a true semantic linking. If your use case is representing an actual clinical assessment (i.e. clinical summation of information and/or an opinion formed, which is the outcome of the clinical assessment process), then you can use ClinicalImpression (with caution since it is only FMM=0), which includes references for the problem, investigation, and findings. In your use case, is the condition stage the finding or outcome of the assessment?

### Marten Smits — 2017-03-15 16:25:52+00:00
In our use case these are findings: The condition and observations are all input for a CDS tool to decide the best therapy for the patient. A patient has a specific kind of cancer, which includes it's stage etc. (Conditions) The observations are, for example, the presence of a certain gene in the patient. These observations have to be linked somehow to the conditions (as they are related to only certain types of cancer) for the CDS tools and we were thinking of using ClinicalImpression for that.

### Sadiq Saleh — 2017-03-15 18:47:52+00:00
We had a similar use case ( https://chat.fhir.org/#narrow/near/64679/stream/implementers/topic/event-reasonReference.20extension ). In short we are using the reasonReference extension to link back from an observation to the tumor it resulted from.

---
*URL: https://chat.fhir.org/#narrow/stream/implementers/topic/Using%20ClinicalImpression%20for%20a%20cancer%20therapy%20decisions*

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# committers > tracker-item

**Messages:** 10
**First message:** 2016-05-03 21:02:34+00:00
**Last message:** 2016-05-07 14:44:03+00:00
**Participants:** FHIR Bot, James Agnew, Josh Mandel

## Messages

### FHIR Bot — 2016-05-03 21:02:34+00:00
Tracker Issue 5304 : Test issue posted by josh_mandel

### FHIR Bot — 2016-05-03 21:03:10+00:00
#5304 : Test issue posted by josh_mandel

### James Agnew — 2016-05-03 21:03:44+00:00
Nice work, Casino Bot. Always telling us about the issues...

### FHIR Bot — 2016-05-03 21:31:13+00:00
#9952 : fake tracker item to delete posted by josh_mandel

### FHIR Bot — 2016-05-04 09:05:14+00:00
#9953 : Change binding strength from preferred to extensible for daf .substance posted by emhaas

### FHIR Bot — 2016-05-04 11:58:57+00:00
#9954 : Not Authorized status code is incorrect - should be 401 posted by brian_pos

### FHIR Bot — 2016-05-04 19:57:52+00:00
#9955 : Add test case for round-tripping QuestionnaireResponses posted by lloyd_mckenzie

### FHIR Bot — 2016-05-06 17:50:42+00:00
#9959 : Sample CarePlan contains its subject but keeps referencing Patient/example posted by pascal

### Josh Mandel — 2016-05-06 18:00:40+00:00
Marked as resolved -- thanks for the follow-up @Pascal Pfiffner

### FHIR Bot — 2016-05-07 14:44:03+00:00
#9960 : DAF Shall Declare DAF profile posted by jwalonoski

---
*URL: https://chat.fhir.org/#narrow/stream/committers/topic/tracker-item*

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "Condition ClinicalImpression circular reference, QA 5a bidirectional reference",
  "sources": "jira",
  "limit": 10
}
```

**Result:**
```
## Search Results (1 total, showing 1)

### [jira] FHIR-10635 — QA 5a: Resource references exist in both directions for Condition and ClinicalImpression
- **Score:** 0.05
- **Updated:** 2019-12-12T17:31:16-06:00
- **URL:** https://jira.hl7.org/browse/FHIR-10635
- **Snippet:** ...<b>ClinicalImpression</b>) <b>ClinicalImpression</b>.problem & <b>ClinicalImpression</b>.finding.item [x] (to <b>Condition</b>) Per QA 5a: Elements with a type of Resource <b>Reference</b> should...


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "Condition ClinicalImpression circular reference",
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
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-10635
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| clinicalimpression | fhir_path | 14 | 12.610 |
| 5a | word | 3 | 11.624 |
| circular | word | 2 | 7.145 |
| direction | word | 3 | 6.906 |
| condition | fhir_path | 9 | 6.731 |
| condition.stage.assessment | fhir_path | 1 | 6.297 |
| clinicalimpression.finding.item | fhir_path | 1 | 6.297 |
| qa | word | 4 | 6.239 |
| clinicalimpression.problem | fhir_path | 1 | 5.831 |
| stage | word | 2 | 5.634 |
| exist | word | 4 | 5.112 |
| finding | word | 2 | 4.909 |
| assessment | word | 2 | 4.784 |
| substantially | word | 1 | 4.639 |
| exemption | word | 1 | 4.327 |
| checklist | word | 1 | 4.260 |
| problem | word | 2 | 4.070 |
| mature | word | 1 | 4.067 |
| procedure | fhir_path | 2 | 3.905 |
| live | word | 1 | 3.748 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10635.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientCare\\FHIR-10635.md",
  "file_text": "# FHIR-10635: QA 5a: Resource references exist in both directions for Condition and ClinicalImpression\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-10635](https://jira.hl7.org/browse/FHIR-10635) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | Patient Care |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter** | Michelle Miller |\n| **Created** | 2016-09-09 |\n| **Updated** | 2019-12-12 |\n\n---\n\n## Summary\n\nThis ticket flags a QA 5a violation: bidirectional resource references exist between the **Condition** and **ClinicalImpression** resources. Specifically:\n\n- **Condition.stage.assessment** \u2192 references ClinicalImpression\n- **ClinicalImpression.problem** \u2192 references Condition\n- **ClinicalImpression.finding.item[x]** \u2192 references Condition\n\nPer the DSTU QA Guidelines (rule 5a), a given relationship should only be represented in one resource, not both, and should generally live on the resource that is created second. The ticket asks Patient Care to resolve which direction the reference should go and remove the other.\n\nThe ticket was originally filed in September 2016. It was **deferred** in January 2017 (vote: 7-0-1) because ClinicalImpression was not mature enough (FMM=0) to make a definitive decision. A note was added to the spec acknowledging the known circular reference issue. In July 2018, the workgroup voted **Not Persuasive** (8-0-0), but the ticket was never formally resolved and remains in **Triaged** status.\n\nLloyd McKenzie noted in comments that the situation is nuanced \u2014 it is `Condition.stage` (not Condition as a whole) that points to ClinicalImpression, and both the Condition and its stage could plausibly be created as part of a ClinicalImpression workflow.\n\n---\n\n## Details\n\n### The QA 5a Rule\n\nThe DSTU QA Guidelines state: *\"Elements with a type of Resource Reference should be reviewed such that a given relationship shall only be represented in one resource, not both (and should generally be present on the resource that is normally created second).\"*\n\n### Affected Elements\n\n| Element | Target | Direction |\n|---------|--------|-----------|\n| `Condition.stage.assessment` | ClinicalImpression | Condition \u2192 ClinicalImpression |\n| `ClinicalImpression.problem` | Condition | ClinicalImpression \u2192 Condition |\n| `ClinicalImpression.finding.item[x]` | Condition | ClinicalImpression \u2192 Condition |\n\n### Vote History\n\n- **2017-01-31** \u2014 Deferred (Rob/Elaine: 7-0-1). ClinicalImpression not mature enough; requested MnM exemption on QA checklist.\n- **2017-02-01** \u2014 Note applied to spec acknowledging circular reference and low maturity of ClinicalImpression.\n- **2018-07-05** \u2014 Voted Not Persuasive (George/Emma: 8-0-0). Discussion about whether to defer

... *(truncated, 9788 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10635.md with 9601 characters
```

</details>


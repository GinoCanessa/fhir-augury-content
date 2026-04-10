# Session Log: FHIR-10028

**Phase:** prepared
**Work Group:** PatientCare
**Source File:** `prepared/PatientCare/FHIR-10028.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-10028` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 17:59:49 UTC |
| **Duration** | 152s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 421,340 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-10028
## Work Group: Patient Care
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10028.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-10028", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-10028", limit=50)

## Step 2: Fetch Related Jira Tickets
For each Jira ticket in cross-references, fetch details via FhirAugury-get_item.

## Step 3: Fetch Zulip Conversations
For each Zulip cross-reference, get the thread. Also: FhirAugury-content_search(values="FHIR-10028", sources="zulip", limit=10)

## Step 4: Note GitHub Items

## Step 5: Build the Report using this structure:

```markdown
# Ticket Review: FHIR-10028

**Title:** {ticket title}
**Status:** {status} **Priority:** {priority} **Type:** {type}
**Work Group:** {work group} **Specification:** {specification}
**Reporter:** {reporter} **Assignee:** {assignee}
**Created:** {date} **Updated:** {date} **Labels:** {labels}

---

## Summary
{Clear, concise summary in third person.}

## Details
**Description:** {Full description}
**Comments:** {Each comment with author/date}

## Keywords
{Comma-separated keywords}

## Related Zulip Discussions
{Thread summaries or "No related Zulip discussions were found."}

## Related GitHub Items
{Bullet list or "No related GitHub items were found."}

## Proposed Dispositions

### Disposition A: Accept As Requested
#### Proposal
#### Justification

---

### Disposition B: Alternative Approach
#### Proposal
#### Justification

---

### Disposition C: Decline
#### Proposal
#### Justification

---

### Recommendation
**Recommended disposition:** {A, B, or C}
{Paragraph explaining why}
```

## Rules
- Use ONLY data from MCP/CLI. Do not fabricate.
- Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10028.md
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
  "id": "FHIR-10028",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
Output too large to read at once (23.4 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\1775757595161-copilot-tool-output-u36glv.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
# [jira] FHIR-10028: Careplan: Provide ability to specify patient and/or provider preferences

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Emma Jones
- **Created:** 2016-05-13T17:04:56+00:00
- **Updated:** 2025-07-17T21:12:12+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10028

## Content
<p>Clinician on fhir M
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-10028" (4 results)

- [jira] FHIR-10028 → [fhir] NutritionOrder.excludeFoodModifier
  **Source:** Careplan: Provide ability to specify patient and/or provider preferences
  **Type:** mentions
  **Context:** + Patient Care WGM Tues Q3 + FYI - NutritionOrder.excludeFoodModifier can be used for food/substance related prefer...
  **Score:** 0.79
  **Updated:** 2025-07-17T21:12:12+00:00
- [jira] FHIR-10028 → [fhir] Observation.code
  **Source:** Careplan: Provide ability to specify patient and/or provider preferences
  **Type:** mentions
  **Context:** ...ensions with codeable data types – can capture expressor, recorder and outcome. Observation.code would indicate the type of preference (nutrition, medication, c...
  **Score:** 0.79
  **Updated:** 2025-07-17T21:12:12+00:00
- [zulip] 153874450 → [jira] FHIR-10028
  **Source:** [implementers] Patient preference
  **Type:** mentions
  **Context:** Patient Care has a deferred GF#10028 about patient preferences, which originated from a Clinicians On FHIR d...
  **Score:** 0.01
  **Updated:** 2017-03-02T16:18:29+00:00
- [zulip] 153858681 → [jira] FHIR-10028
  **Source:** [committers] Progress Check
  **Type:** mentions
  **Context:** ...Resources: GF#8931 - new condition extension (should get applied prior to STU3) GF#10028 - may need to update gForge status to deferred (resolution said "This p...
  **Score:** 0.01
  **Updated:** 2016-11-28T14:31:17+00:00
**Warnings:**
- Value 'FHIR-10028' is not a valid Zulip message ID

```

</details>

### Turn 2

**Assistant:**

Now let me fetch the Zulip threads and do a content search in parallel.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# implementers > Patient preference

**Messages:** 5
**First message:** 2017-03-02 15:05:52+00:00
**Last message:** 2017-03-02 18:03:05+00:00
**Participants:** Sadiq Saleh, Lloyd McKenzie, Michelle (Moseman) Miller

## Messages

### Sadiq Saleh — 2017-03-02 15:05:52+00:00
I am not clear how a patient preference for a procedurerequest or medicationrequest is captured. Should it be appended to the request as supporting information in the form of a referred observation?

### Lloyd McKenzie — 2017-03-02 16:04:48+00:00
That's what we've talked about doing, but we haven't had a lot of feedback in this area

### Sadiq Saleh — 2017-03-02 16:10:56+00:00
I thought I had seen a discussion about it at some point but could not find it using the search. I assume it was on zulip and not on the gforge page?

### Michelle (Moseman) Miller — 2017-03-02 16:18:29+00:00
Patient Care has a deferred GF#10028 about patient preferences, which originated from a Clinicians On FHIR discussion. Meet need with a profile for preference on the observation resource. Requirements are a preference category (nutrition, medication, care), the preference priority (high/medium/delayed from C-CDA) and with elements of expressor and recorder.This profile would not be developed for this release cycle

### Sadiq Saleh — 2017-03-02 18:03:05+00:00
Thank you @Michelle (Moseman) Miller I will take a look at the tracker

---
*URL: https://chat.fhir.org/#narrow/stream/implementers/topic/Patient%20preference*

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# committers > Progress Check

**Messages:** 10
**First message:** 2016-11-27 19:44:41+00:00
**Last message:** 2016-11-28 22:07:44+00:00
**Participants:** Grahame Grieve, Melva Peters, Michelle (Moseman) Miller, Eric Haas, Brian Postlethwaite

## Messages

### Grahame Grieve — 2016-11-27 19:44:41+00:00
The following resources have substantive change due dates today: AllergyIntolerance, CarePlan, CareTeam, Composition, Condition, Device, DiagnosticReport, Goal, GuidanceResponse, Immunization, Location, Medication, MedicationAdministration, MedicationDispense, MedicationOrder, MedicationStatement, Observation, Organization, Patient, Practitioner, Procedure, ServiceDefinition @Eric Haas @Brian Postlethwaite @Michelle (Moseman) Miller @Melva Peters - can you comment please?

### Grahame Grieve — 2016-11-27 19:45:24+00:00
I have applied all substantiative changes to FHIR-I resources that are approved and that are going to happen for the December milestone

### Melva Peters — 2016-11-27 23:43:00+00:00
Hi @Grahame Grieve We have 1 change remaining for the workflow harmonization for medicationrequest and are just starting on harmonization of event resources. The 2 approved changes that are waiting to be applied are non-substantive. Can you confirm which tracker items you believe are due today?

### Grahame Grieve — 2016-11-27 23:43:57+00:00
I didn't look at tracker items, and don't have any particular ones listed.

### Michelle (Moseman) Miller — 2016-11-28 14:31:17+00:00
The short answer is that I've applied everything that I could prior to the Dec freeze. Here is the list of remaining Patient Care WG "Resolved-Change Required" issues that are substantive changes, but not yet applied: High Priority Resources: GF#8931 - new condition extension (should get applied prior to STU3) GF#10028 - may need to update gForge status to deferred (resolution said "This profile would not be developed for this release cycle") GF#10293 - apply workflow patterns - need to review again with PCWG given changes to workflow patterns GF#11020 - intentionally waiting to apply until larger AllergyIntolerance.reaction discussions land GF#11023 - intentionally waiting to apply until larger AllergyIntolerance.reaction discussions land GF#11354 - intentionally waiting to apply until AllergyIntolerance discussions land (controversial resolution being revisited) Lower Priority Resources: GF#10468 - @Lloyd McKenzie agreed to apply this Questionnaire change after he returns from his vacation GF#12173 - new Questionnaire extension (should get applied prior to STU3)

### Eric Haas — 2016-11-28 21:44:06+00:00
No on Observation or DiagnosticReport

### Grahame Grieve — 2016-11-28 21:47:32+00:00
@Eric Haas "no" - no there are no changes , or no, I still have change?

### Eric Haas — 2016-11-28 22:05:52+00:00
no I still have not made the substantive changes and no we have not voted on many of the substantive comments. Observation: 10117 add Sequence as a target for Observation.related (Bob Milius) Persuasive 10275 add valueBoolean to Observation (Andrew Ross) Persuasive 11115 Do not unbound referenceRange.meaning - use two elements instead. - 2016-09 core #269 (Danielle Friend) Persuasive 10344 Alignment of DiagnosticReport.status and Observation.status ValueSets (Alexander Henket) Persuasive with Mod 10299 Ensure event resource data elements align with event resource template (Eric Haas) Persuasive 10300 align event resource statuses to event resource template (Eric Haas) Persuasive

### Grahame Grieve — 2016-11-28 22:06:17+00:00
not going to make the milestone then

### Brian Postlethwaite — 2016-11-28 22:07:44+00:00
I'm working on the 20 aproved PA changes to get through today.

---
*URL: https://chat.fhir.org/#narrow/stream/committers/topic/Progress%20Check*

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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10028.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientCare\\FHIR-10028.md",
  "file_text": "# Ticket Review: FHIR-10028\n\n**Title:** Careplan: Provide ability to specify patient and/or provider preferences\n**Status:** Triaged **Priority:** Medium **Type:** Change Request\n**Work Group:** Patient Care **Specification:** FHIR Core (FHIR)\n**Reporter:** Emma Jones **Assignee:** Unassigned\n**Created:** 2016-05-13 **Updated:** 2025-07-17 **Labels:** None\n\n---\n\n## Summary\n\nThis long-standing change request, originating from Clinicians on FHIR at Montreal 2016, asks for a standardized mechanism to capture patient and/or provider preferences within FHIR, initially scoped to CarePlan but recognized as cross-resource in nature. Over nine years of discussion, the work group has considered multiple approaches: profiling Observation, creating a new resource, using extensions on CarePlan and Request resources, or leveraging existing resources such as NutritionOrder. The most recent activity (June\u2013July 2025) indicates a logical model for preferences has been drafted and largely agreed upon, with the group now exploring an extension-based approach on CarePlan and all Request resources. Cross-work-group coordination with Orders & Observations, Patient Empowerment, IPS, and PACIO/MCC is planned.\n\n## Details\n\n**Description:**\n\nClinician on FHIR Montreal 2016. Careplan: Provide ability to specify patient and/or provider preferences. Per Lloyd McKenzie, three options were identified: use Observation, Alerts, or a new resource. Examples of preferences include: patient does not like peas, patient prefers apple juice instead of milk, and patient prefers sitting rather than walking.\n\n**Comments:**\n\n**michelle.m.miller \u2014 2025-07-17:**\nPatient Care FHIR Conference Call on July 17, 2025. A logical model has been drafted and is largely agreed upon. Not ready to discuss how it manifests in CarePlan \u2014 needs more discussion within the CarePlan call. CC: Emma Jones, Jay Lyle, Stephen Chu.\n\n**michelle.m.miller \u2014 2025-06-12:**\nPatient Care FHIR Conference Call on June 12, 2025. Three options considered: no change needed, transfer to OO, or ask PACIO/ADI. Emma's use case is in the context of care coordination (caring for the patient), distinct from ADI advanced directives. Rob does not think patient preference to never get mRNA vaccinations would be Observation. Discussion noted that some resources persist indefinitely (e.g., AllergyIntolerance, Condition) while Observation is more point-in-time. An alternative to use an extension was raised. Emma prefers exploring an extension on CarePlan and all Request resources. Next steps: draft extension in PC-only CarePlan call, request a room for joint meeting with OO, PE, IPS, PACIO/MCC (Wed Q4), and socialize with those groups before Sept WGM.\n\n**michelle.m.miller \u2014 2025-06-05:**\nPatient Care FHIR Conference Call on June 5, 2025. Observation is often used for preferences. Questi

... *(truncated, 12452 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-10028.md with 12233 characters
```

</details>

### Turn 4

**Assistant:**

Now let me fetch the related Jira ticket and the Zulip thread in parallel.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-10028: Careplan: Provide ability to specify patient and/or provider preferences

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Emma Jones
- **Created:** 2016-05-13T17:04:56+00:00
- **Updated:** 2025-07-17T21:12:12+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10028

## Content
<p>Clinician on fhir Montreal 2016</p>

<p>         Careplan: Provide ability to specify patient and/or provider preferences</p>

<p>         Per Lloyd - we have 3 options - use Observation, Alerts or New resource</p>



<p>         Example of preference: patient does not like peas. Pateint prefers apple juice instead of milk. Prefers sitting rather than walking.</p>

## Comments (13)

### michelle.m.miller — 2025-07-17T21:12:12+00:00
<p><ins><b>Patient Care FHIR Conference Call on July 17, 2025</b></ins></p>

<p>Logical model has been drafted – largely agreed upon.</p>

<p>Not ready to discuss how it manifests in CarePlan - needs more discussion within CarePlan call.</p>

<p>CC:  <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=emmanurse" class="user-hover" rel="emmanurse">Emma Jones</a> <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=jlyle" class="user-hover" rel="jlyle">Jay Lyle</a> <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=chuscmi" class="user-hover" rel="chuscmi">Stephen Chu</a> </p>

<p> </p>

### michelle.m.miller — 2025-06-12T22:04:36+00:00
<p><ins><b>Patient Care FHIR Conference Call on June 12, 2025</b></ins></p>
<ul>
	<li>No change needed</li>
	<li>Transfer to OO</li>
	<li>Ask PACIO / ADI</li>
</ul>


<p>Emma's use case was in context of care coordination (caring for the patient). </p>

<p>ADI for PACIO is different use case (advanced directives).</p>

<p>Rob doesn't think the patient preference to never get mRNA vaccinations would be Observation.</p>

<p>Some resources represent things that persist indefinitely (e.g. AllergyIntolerance, Condition) whereas other resources (e.g. Observation) are more point in time / snapshot.  Observation is a point of time observation about a characteristic that exists.</p>

<p>Alternative to use extension </p>

<p>Emma prefers exploring an extension on CarePlan and all Request resources.</p>

<p>Next Steps</p>
<ul>
	<li>Could be a topic for CarePlan call - draft extension (PC only)</li>
	<li>Request a room for joint meeting with OO, PE, IPS, PACIO/MCC (Wed Q4)</li>
	<li>Once mature, socialize with OO, PE, PACIO, IPS, MCC (conference call, if needed, before Sept WGM)</li>
</ul>


<p> </p>

### michelle.m.miller — 2025-06-05T21:59:12+00:00
<p><ins><b>Patient Care FHIR Conference Call on June 5, 2025</b></ins></p>

<p>Observation is often used for preferences.</p>

<p>Should OO own this ticket and add preferences to the Observation scope and usage bulleted list?</p>

<p>Wait for Emma before we move forward</p>

### michelle.m.miller — 2024-10-01T18:05:14+00:00
<p>Sept 2024 WGM email.</p>
<blockquote><p><em>All the co-chairs from Patient Care, Orders &amp; Observations, and Community Based Care &amp; Privacy have been copied I believe, plus the core ADI team, but please let me know if I missed someone.</em></p>

<p>Hi all, thank you for your time and involvement in the ADI Report-Out last week in Atlanta.  To ensure we memorialize the consensus we achieved, I thought it important to recap the below.</p>

<p>One of the critical decisions that I believe we achieved consensus on during this report-out, which has long been a topic of discussion on this IG, was the agreement to the below:</p>
<ol>
	<li><b><ins>Person-Authored advance healthcare directive</ins></b> concepts will use the Observation Resource to express:</li>
	<li>Care Experience preferences</li>
	<li>Upon Death preferences</li>
	<li>Additional Documentation</li>
	<li>Witness &amp; Notary</li>
	<li>Administ

... *(truncated, 12056 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "stream": "implementers",
  "topic": "TreatmentDirective: which resource is for this purpose?",
  "limit": 50
}
```

**Result:**
```
# implementers > TreatmentDirective: which resource is for this purpose?

**Messages:** 7
**First message:** 2025-04-24 16:40:43+00:00
**Last message:** 2025-05-15 07:55:51+00:00
**Participants:** Eduard de Rijcke 🇳🇱 🇪🇺, Lloyd McKenzie

## Messages

### Eduard de Rijcke 🇳🇱 🇪🇺 — 2025-04-24 16:40:43+00:00
Hi all, Currently, we are researching how to implement TreatmentDirective (which contains a joint decision between a health professional and a patient or his representative(s) about the desirability of performing a certain treatment) in the Netherlands. For example, some topics that a Patient/representative could agree and register with the health professional: Admission to the intensive care unit Cardiopulmonary resuscitation Artificial respiration With the options: Execute Do not execute Other (Example: do not execute artificial respiration in a hospital) Now we are considering which HL7 FHIR R4 resource is compatible with this kind of information. First, we thought the Consent resource, but now we are doubting whether to use ServiceRequest resource like PACIO ( example stu2 ). Both resources have their pros and cons. Consent describes more of an agreement between both parties, and ServiceRequest is more used for planned/requested actions. So, does PACIO choose the right resource for this TreatmentDirective purpose? The only main issue both resources have only two options (ProvisionType: Deny/Permit or doNotPerform: boolean). So now we're thinking of using an extension to support this other (condition) option. I hope my question is clear and the answer is simple. If not, I could maybe start a Jira ticket for PatientCare and ask this during the WGM International in Madrid.

### Lloyd McKenzie — 2025-04-24 17:20:35+00:00
Be aware that there's a "directive" intent that can be used in most Request resources. It was intended for use in situations like this.

### Eduard de Rijcke 🇳🇱 🇪🇺 — 2025-04-29 09:16:14+00:00
Thank you for your quick answer, Lloyd. We still have questions about whether this information is compatible with ServiceRequest. Also, we have AdvanceDirective , which is a part of TreatmentDirective, that is difficult to match to a FHIR resource. My colleagues and I will address those topics during the Patient Care WGM in Madrid.

### Lloyd McKenzie — 2025-04-29 14:15:19+00:00
@Lisa Nelson has done some work in this space and may have some thoughts

### Eduard de Rijcke 🇳🇱 🇪🇺 — 2025-05-07 08:22:11+00:00
Thanks, Lloyd. I will contact her about her experience using TreatmentDirective in FHIR. I’ll also ask PatientCare if this topic could be added to the agenda for the WGM in Madrid. We could use some advice on which core resource is most compatible for this purpose. We (including HL7 NL) aren’t fully convinced that ServiceRequest is the right choice.

### Eduard de Rijcke 🇳🇱 🇪🇺 — 2025-05-13 09:36:18+00:00
For those interested, I'll present this question today (Tuesday, May 13th) at the HL7 WGM in Madrid at the PatientCare workgroup Q4 .

### Eduard de Rijcke 🇳🇱 🇪🇺 — 2025-05-15 07:55:51+00:00
I've created a Jira ticket because there are more options to discuss and need to be harmonized: https://jira.hl7.org/browse/FHIR-50903

---
*URL: https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F*

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "TreatmentDirective, advance directive Consent ServiceRequest",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 515076027 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.33
- **Updated:** 2025-04-29T14:15:19+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/515076027
- **Snippet:** @Lisa Nelson has done some work in this space and may have some thoughts

### [zulip] 515004929 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.30
- **Updated:** 2025-04-29T09:16:14+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/515004929
- **Snippet:** ...Also, we have AdvanceDirective , which is a part of <b>TreatmentDirective</b>, that is difficult to match to a FHIR resource. My...

### [zulip] 516608980 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.23
- **Updated:** 2025-05-07T08:22:11+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/516608980
- **Snippet:** ...I will contact her about her experience using <b>TreatmentDirective</b> in FHIR. I’ll also ask PatientCare if this topic could...

### [zulip] 517781676 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.16
- **Updated:** 2025-05-13T09:36:18+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/517781676
- **Snippet:** For those interested, I'll present this question today (Tuesday, May 13th) at the HL7 WGM in Madrid at the...

### [zulip] 518231067 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.13
- **Updated:** 2025-05-15T07:55:51+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/518231067
- **Snippet:** I've created a Jira ticket because there are more options to discuss and need to be harmonized: https://jira...

### [zulip] 514181955 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.12
- **Updated:** 2025-04-24T17:20:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/514181955
- **Snippet:** Be aware that there's a "directive" intent that can be used in most Request resources. It was intended for...

### [zulip] 194290157 — [netherlands] consent.except.type in HCIM TreatmentDirective
- **Score:** 0.01
- **Updated:** 2020-04-16T11:37:36+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/netherlands/topic/consent.except.type%20in%20HCIM%20TreatmentDirective/near/194290157
- **Snippet:** Ah yes, once I read the documentation for Consent.Except, that is clear. Thanks Alexander!

### [zulip] 164626540 — [implementers] Cardinality of 'source[x]' in Consent
- **Score:** 0.01
- **Updated:** 2019-05-01T14:19:07+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Cardinality%20of%20%27source%5Bx%5D%27%20in%20Consent/near/164626540
- **Snippet:** We have a Dutch Functional model of <b>TreatmentDirective</b> (based on Consent, see here: https://simplifier.net/NictizSTU3-Zib2017/ZIB-<b>TreatmentDirective</b>...

### [zulip] 194288258 — [netherlands] consent.except.type in HCIM TreatmentDirective
- **Score:** 0.00
- **Updated:** 2020-04-16T11:17:29+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/netherlands/topic/consent.except.type%20in%20HCIM%20TreatmentDirective/near/194288258
- **Snippet:** ...If a Consent.except is used in accordance with the HCIM <b>TreatmentDirective</b>, then the only time an except is in...

### [zulip] 575805374 — [IG 

... *(truncated, 4416 chars total)*
```

</details>


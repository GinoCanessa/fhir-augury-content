# Session Log: FHIR-11173

**Phase:** prepared
**Work Group:** PatientCare
**Source File:** `prepared/PatientCare/FHIR-11173.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-11173` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:40:27 UTC |
| **Duration** | 106s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 288,834 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-11173
## Work Group: Patient Care
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-11173.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-11173", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-11173", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-11173", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-11173.md
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
  "id": "FHIR-11173",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-11173: CarePlan needs support for reviews - 2016-09 core #327

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Stephen Chu
- **Created:** 2016-09-17T23:48:59+00:00
- **Updated:** 2025-07-17T21:09:35+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-11173

## Content
<p>Comment:</p>

<p>         CarePlan - missig support for expressing reviews</p>

<p>         Care plan reviews are important activities/requirements. Reviews can be at components level, e.g. concern, goals, actiities, or at whole-of-plan level</p>

<p>         A minimum requirement will be to support whole-of-plan level review with a "next review date" element</p>

<p>         Summary:</p>

<p>         CarePlan needs support for reviews</p>

## Comments (12)

### michelle.m.miller — 2025-07-17T21:09:35+00:00
<p><ins><b>Patient Care FHIR Conference Call on July 17, 2025</b></ins></p>

<p>Has not been discussed at CarePlan call yet.</p>

<p>Needs more discussion on CarePlan call before we can vote on it.</p>

<p>CC:  <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=emmanurse" class="user-hover" rel="emmanurse">Emma Jones</a> <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=chuscmi" class="user-hover" rel="chuscmi">Stephen Chu</a> </p>

### michelle.m.miller — 2023-09-14T20:22:26+00:00
<p><ins><b>WGM Sept 2023 Thurs Lunch</b></ins></p>

<p>Options</p>
<ul>
	<li>lastUpdated and notes</li>
	<li>Observation</li>
	<li>Provenance</li>
</ul>


### michelle.m.miller — 2019-05-08T16:03:09+00:00
<p>+               <b>PA/PC Wed Q2 Discussion</b>            +         </p>

<p>                     *Provenance *-- where did it come from (chain of possession)</p>

<p>                     *VerificationResult *-- authentication (confirm authenticity) &#8211; Brian questions whether the concept of review fits in here, but Cooper suggested scope could be increased.  If we added a review notes element, does that suffice or is more needed?</p>

<p>                     *Task *-- allocation / assignment to do review, but results of review aren't there</p>

<p>         PA just learned about *MedicinalProductAuthorization *            <a href="http://build.fhir.org/medicinalproductauthorization.html" class="external-link" target="_blank" rel="nofollow noopener">http://build.fhir.org/medicinalproductauthorization.html</a> (might be renamed, though).  May need to talk to Pharmacy about their plans for this resource, but it probably won't work (sip test is this is for FDA approval of new drugs) </p>

<p>         Next step:  Patient Care still needs to document requirements, such as what was reviewed, why it was reviewed, who reviewed it, when it was reviewed, when does it need to be reviewed next?</p>

<p>         Dave suggested expanding the review concept from one practitioner reviewing one care plan to a broader care manager reviewing care plans across an assigned population of patients.  Reviews are broader than just care plan.  Shift changes.  Medication reconciliation review</p>

### michelle.m.miller — 2019-05-08T16:03:09+00:00
<p>+               <b>PA/PC Wed Q2 Discussion</b>            +         </p>

<p>                     *Provenance *-- where did it come from (chain of possession)</p>

<p>                     *VerificationResult *-- authentication (confirm authenticity) &#8211; Brian questions whether the concept of review fits in here, but Cooper suggested scope could be increased.  If we added a review notes element, does that suffice or is more needed?</p>

<p>                     *Task *-- allocation / assignment to do review, but results of review aren't there</p>

<p>         PA just learned about *MedicinalProductAuthorization *            <a href="http://build.fhir.org/medicinalproductauthorization.html" class="external-link" target="_blank" rel="n

... *(truncated, 18291 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-11173" (2 results)

- [jira] FHIR-11173 → [zulip] 40:Reviews
  **Source:** CarePlan needs support for reviews - 2016-09 core #327
  **Type:** mentions
  **Context:** Regarding the second action item noted above, discussion started: https://chat.fhir.org/#narrow/stream/40-workflow/topic/Reviews + FHIR Conference...
  **Score:** 0.79
  **Updated:** 2025-07-17T21:09:35+00:00
- [zulip] 153973936 → [jira] FHIR-11173
  **Source:** [workflow] Reviews
  **Type:** mentions
  **Context:** ...Haas , @Brian Postlethwaite , @Lloyd McKenzie Patient Care has a ballot comment GF#11173 asking for support of CarePlan reviews. We've deferred it a couple time...
  **Score:** 0.01
  **Updated:** 2018-07-05T22:42:42+00:00
**Warnings:**
- Value 'FHIR-11173' is not a valid Zulip message ID

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

Now let me fetch the related Zulip thread and search for additional related content.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# workflow > Reviews

**Messages:** 4
**First message:** 2018-07-05 22:42:42+00:00
**Last message:** 2018-07-06 06:32:18+00:00
**Participants:** Michelle (Moseman) Miller, Lloyd McKenzie, Grahame Grieve, Eric Haas

## Messages

### Michelle (Moseman) Miller — 2018-07-05 22:42:42+00:00
@Eric Haas , @Brian Postlethwaite , @Lloyd McKenzie Patient Care has a ballot comment GF#11173 asking for support of CarePlan reviews. We've deferred it a couple times, but wanted to better understand if there is any coordinated effort going on more broadly across all resources. For example: I think Lloyd once suggested this is something probably best handled by "Task" (owned by OO) but will require a fair bit of analysis and discussion with other work groups to agree on approach VerificationResult (owned by PA) seems to related to review of health care directory information In sum, trying to understand which work group is taking the lead on a coordinated effort around handling reviews, so PC can get plugged into those efforts.... CC: @Stephen Chu , @Rob Hausam , @John Moehrke

### Lloyd McKenzie — 2018-07-05 22:53:38+00:00
VerificationResult is narrowly constrained right now, but the FMG has asked PA to explore broadening it to support all types of reviews. Would certainly like to know if PC thinks the resource is adaptable to meet their needs. Task would allow you to request a review and note that it was done, but wouldn't necessarily capture details about the results - not sure if that's needed or not.

### Grahame Grieve — 2018-07-05 23:57:21+00:00
I'd love to see good write up of distributed care plan reviews. I'm going to work on this once the ballot is out

### Eric Haas — 2018-07-06 06:32:18+00:00
I am not aware of any work by OO on this

---
*URL: https://chat.fhir.org/#narrow/stream/workflow/topic/Reviews*

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "CarePlan review, care plan reviews next review date",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 533520578 — [argonaut] US Core V9 Design
- **Score:** 0.12
- **Updated:** 2025-08-08T20:11:06+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/argonaut/topic/US%20Core%20V9%20Design/near/533520578
- **Snippet:** ...We will <b>review</b> and complete our US Core <b>CarePlan</b>'s proposals and decisions. Discuss USCDI V6 Family History's strawman...

### [zulip] 267378372 — [Care Plan/Care Coordination] post discharge care plan
- **Score:** 0.01
- **Updated:** 2022-01-09T21:20:45+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Care%20Plan%2FCare%20Coordination/topic/post%20discharge%20care%20plan/near/267378372
- **Snippet:** Great, thank you Lloyd! After creating a few drafts of the <b>CarePlan</b>, I will <b>review</b> the post discharge form again...

### [zulip] 164277803 — [implementers] Medication Review
- **Score:** 0.01
- **Updated:** 2019-04-26T16:47:44+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Medication%20Review/near/164277803
- **Snippet:** You'd be looking at ServiceRequest, CommunicationRequest and/or <b>CarePlan</b>

### [zulip] 153940401 — [committers] tracker-item
- **Score:** 0.01
- **Updated:** 2018-02-25T14:16:25+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/tracker-item/near/153940401
- **Snippet:** GF#15644 : <b>review</b> <b>Careplan</b> "completed" status posted by costateixeira

### [zulip] 153922679 — [implementers] Review Instructions
- **Score:** 0.00
- **Updated:** 2017-12-02T17:17:14+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Review%20Instructions/near/153922679
- **Snippet:** sound like part of the P in SOAP so I would say <b>CarePlan</b>. (or a clinical note that is referenced...

### [zulip] 218621313 — [workflow] serviceRequest
- **Score:** 0.00
- **Updated:** 2020-12-02T21:20:13+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/workflow/topic/serviceRequest/near/218621313
- **Snippet:** ...Only, it looks like basedOn for <b>carePlan</b> requires another <b>carePlan</b>... Any ideas? Thank you!!

### [zulip] 175078308 — [implementers] CarePlan vs. ProcedureRequest to capture diary entries?
- **Score:** 0.00
- **Updated:** 2019-09-06T16:02:04+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/CarePlan%20vs.%20ProcedureRequest%20to%20capture%20diary%20entries%3F/near/175078308
- **Snippet:** Hi, I not sure whether the <b>CarePlan</b> or ProcedureRequest resource would be better to capture "diary entry" information? Our requirements...

### [zulip] 164282437 — [implementers] Medication Review
- **Score:** 0.00
- **Updated:** 2019-04-26T17:46:14+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Medication%20Review/near/164282437
- **Snippet:** ...The <b>CarePlan</b> would be the parent resource consolidating all the different recommendations

### [zulip] 164269638 — [implementers] Medication Review
- **Score:** 0.00
- **Updated:** 2019-04-26T15:02:12+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Medication%20Review/near/164269638
- **Snippet:** ...Alternatively, you could create a <b>CarePlan</b> that indicates the recommendation. @Jose Costa Teixeira - I believe the IHE has an IG...

### [zulip] 153949081 — [committers] QA
- **Score:** 0.00
- **Updated:** 2018-03-29T17:33:08+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/QA/near/153949081
- **Snippet:** @David Hay PC has 5 resources that are marked as <b>review</b> completed in the spreadsheet, but I don't see...


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [github] HL7/fhir:source/careplan/careplan-notes.xml — source/careplan/careplan-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/careplan/careplan-notes.xml
- **Snippet:** Notes The Provenance resource can be used for detailed <b>review</b> information, such as when the care plan was last reviewed...

### [github] HL7/fhir:source/careplan/careplan-notes.xml — source/careplan/careplan-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/careplan/careplan-notes.xml
- **Snippet:** Notes The Provenance resource can be used for detailed <b>review</b> information, such as when the care plan was last reviewed...

### [github] HL7/fhir:source/careplan/careplan-notes.xml — source/careplan/careplan-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/careplan/careplan-notes.xml
- **Snippet:** Notes The Provenance resource can be used for detailed <b>review</b> information, such as when the care plan was last reviewed...

### [github] HL7/fhir:source/careplan/careplan-notes.xml — source/careplan/careplan-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/careplan/careplan-notes.xml
- **Snippet:** Notes The Provenance resource can be used for detailed <b>review</b> information, such as when the care plan was last reviewed...

### [github] HL7/fhir-extensions:input/definitions/multiple/StructureDefinition-artifact-reviewer.xml — input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Score:** 0.66
- **URL:** https://github.com/HL7/fhir-extensions/blob/main/input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Snippet:** ArtifactReviewer Artifact Reviewer An individual or organization primarily responsible for <b>review</b> of some aspect of the artifact. This extension is...

### [github] HL7/fhir-extensions:input/definitions/multiple/StructureDefinition-artifact-reviewer.xml — input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Score:** 0.66
- **URL:** https://github.com/HL7/fhir-extensions/blob/main/input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Snippet:** ArtifactReviewer Artifact Reviewer An individual or organization primarily responsible for <b>review</b> of some aspect of the artifact. This extension is...

### [github] HL7/fhir-extensions:input/definitions/multiple/StructureDefinition-artifact-reviewer.xml — input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Score:** 0.66
- **URL:** https://github.com/HL7/fhir-extensions/blob/main/input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Snippet:** ArtifactReviewer Artifact Reviewer An individual or organization primarily responsible for <b>review</b> of some aspect of the artifact. This extension is...

### [github] HL7/fhir-extensions:input/definitions/multiple/StructureDefinition-artifact-reviewer.xml — input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Score:** 0.66
- **URL:** https://github.com/HL7/fhir-extensions/blob/main/input/definitions/multiple/StructureDefinition-artifact-reviewer.xml
- **Snippet:** ArtifactReviewer Artifact Reviewer An individual or organization primarily responsible for <b>review</b> of some aspect of the artifact. This extension is...

### [github] HL7/fhir:source/episodeofcare/episodeofcare-notes.xml — source/episodeofcare/episodeofcare-notes.xml
- **Score:** 0.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/episodeofcare/episodeofcare-notes.xml
- **Snippet:** ...EpisodeOfCare Outcomes <b>Review</b> An Organization may perform analytics on their EpisodeOfCare resources to have an understanding of how their business...

### [github] HL7/fhir:source/episodeofcare/episodeofcare-notes.xml — source/episodeofcare/episodeofcare-notes.xml
- **Score:** 0.00
- **URL:** https://github.com/

... *(truncated, 4244 chars total)*
```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-11173.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientCare\\FHIR-11173.md",
  "file_text": "# FHIR-11173: CarePlan needs support for reviews\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-11173](https://jira.hl7.org/browse/FHIR-11173) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | Patient Care |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter** | Stephen Chu |\n| **Assignee** | Unassigned |\n| **Created** | 2016-09-17 |\n| **Updated** | 2025-07-17 |\n\n## Summary\n\nThis ticket requests that the CarePlan resource support expressing reviews \u2014 both at the component level (concerns, goals, activities) and at the whole-of-plan level. The minimum requirement proposed is a \"next review date\" element on CarePlan.\n\nThe ticket has an extensive history dating back to 2016. It was originally deferred (Nov 2016, vote 5-0-1) with the rationale that review tracking applies broadly across many resources (protocols, standing orders, long-term care admissions, etc.) and would best be handled via the Task resource with cross-work-group coordination. It was voted \"Not Persuasive\" (8-0-0) in July 2018, then reopened for further analysis with PA and OO work groups. As of the most recent comment (July 2025), it still has not been discussed on the CarePlan call and needs more discussion before voting.\n\n## Details\n\n### Original Request\nCarePlan is missing support for expressing reviews. Care plan reviews are important activities/requirements that can occur at the component level (concerns, goals, activities) or at the whole-of-plan level. The submitter proposes at minimum a \"next review date\" element.\n\n### Resolution Description (from prior deferral)\nTracking of reviews and plans for reviews applies to many resources, not just CarePlan. This was considered something best handled by Task, requiring analysis and discussion with other work groups. Deferred to R4.\n\n### Discussion History\n- **Nov 2016:** Deferred (Stephen/Elaine, 5-0-1)\n- **Jul 2018:** Voted Not Persuasive (George/Emma, 8-0-0). Stephen agreed review is not unique to CarePlan. Action items: (1) defer until broader Task pattern analysis, (2) coordinate with OO (Task), PA (VerificationResult), and PC (CarePlan).\n- **Aug 2018:** Zulip discussion started in workflow > Reviews. Care Plan DAM 1.0 requirements cited. Laura volunteered to draft a CarePlan track use case for Clinicians on FHIR.\n- **May 2019 (PA/PC Q2):** Multiple approaches evaluated \u2014 Provenance, VerificationResult, Task \u2014 none fully fit. Requirements still needed: what/why/who/when reviewed, when next review. Dave suggested broadening the review concept beyond single practitioner/single care plan.\n- **Sep 2023 (WGM):** Options discussed: lastUpdated + notes, Observation, Provenance.\n- **Jul 2025:** Has not been discussed at CarePlan call yet. Needs more discussion before voting. CC'd Emma

... *(truncated, 10288 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-11173.md with 10105 characters
```

</details>


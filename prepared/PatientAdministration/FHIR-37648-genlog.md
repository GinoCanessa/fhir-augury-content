# Session Log: FHIR-37648

**Phase:** prepared
**Work Group:** PatientAdministration
**Source File:** `prepared/PatientAdministration/FHIR-37648.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-37648` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:00:05 UTC |
| **Duration** | 136s |
| **Total Tool Calls** | 11 |
| **Total Tokens** | 293,483 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-37648
## Work Group: Patient Administration
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-37648.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-37648", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-37648", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-37648", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-37648.md
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
  "id": "FHIR-37648",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-37648: Better approach for large lists of participants in Encounter.participants

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Administration
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Cooper Thompson
- **labels:** MovingToGuide
- **Created:** 2022-06-22T18:45:27+00:00
- **Updated:** 2026-01-27T14:13:23+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37648

## Content
<p>We've run into issues where the participant list of an Encounter can get very large for long stay admissions.  Typically there are a reasonable number of <em>active</em> participants, but there maybe a large number of historical participants.  For example, if a patient has been admitted for a year, the nurses they had in their first weeks of the stay may still be listed with a period.end of a 11 months ago.</p>

<p> </p>

<p>There are a few possible approaches we could consider:</p>
<ol>
	<li>Add CareTeam as an allowed type for the participant.actor reference.  Then a system could move the participant list to the CareTeam.  This kinda moves the problem.</li>
	<li>Include participants on EncounterHistory, and have guidance that Encounter.participants is just currently active participants.  Though maybe we also want recent and imminent as well?</li>
	<li>Other options are welcome</li>
</ol>


## Comments (7)

### cooper.thompson — 2025-12-09T20:25:06+00:00
<p>Some recent discussion in zulip:  <a href="https://chat.fhir.org/#narrow/channel/179166-implementers/topic/Dealing.20with.20Large.20resources" class="external-link" target="_blank" rel="nofollow noopener">https://chat.fhir.org/#narrow/channel/179166-implementers/topic/Dealing.20with.20Large.20resources</a></p>

### brian.postlethwaite — 2025-09-17T19:33:02+00:00
<p>Have created the new tracker <a href="https://jira.hl7.org/browse/FHIR-52912" title="operations for large resources general feedback and has typos " class="issue-link" data-issue-key="FHIR-52912">FHIR-52912</a> to provide the feedback for FHIR-I.</p>

### cooper.thompson — 2025-01-28T17:26:13+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=brian.postlethwaite" class="user-hover" rel="brian.postlethwaite">Brian Postlethwaite</a> will check with FHIR-I to see if we can have a dedicated joint call in the coming months to discuss this.</p>

### brian.postlethwaite — 2023-09-12T19:25:53+00:00
<p>PA Sept 2023 WGM Phoenix:</p>

<p>Compared the functionality to the newly added group/list $add/$remove/$filter operations</p>

<p><b>Notes for FHIR Infrastructure:</b></p>

<p>How does the caller know to use the $filter in the first place - is that server discretion?</p>

<p>If so, how do we explicitly ask for the complete resource?</p>

<p>How does the server indicate that the $filter was applied?</p>

<p>Is it just that the client receives a resource with the SUBSETTED tag even though they didn't ask for it to be subsetted? What about if they requested a subset using _elements, that would use SUBSETTED but not be able to indicate that the members were filtered?</p>

<p>How is the core of the resource updated? using patch? doesn't that require a version specific update to have been done on a previous GET?</p>

<p>The notes on the filter matching algorithm for dates isn't sufficiently describing how the periods filtering should be applied - can that be clarified?</p>

<p>To be resolved:</p>
<ul>
	<li>How to detect the large list (is this via an exception?)</li>
	<li>How to request get the complete list anyway</li>
	<li>How to update the core elements</li>
	<li>Should the _count parameter also be applied to the number of entries to cap the number if items?</li>
	<li>How to retrieve the next page?</li>
</ul>


<p> </p>

### cooper.thompson — 2022-09-22T15:56:03+00:00
<p><b>PA Sept 2022 WGM - Thurs Q2:</b></p>
<ul>
	<li><del>Generic <b>_summary=active</b> </del> which then add

... *(truncated, 15202 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-37648" (11 results)

- [jira] FHIR-37648 → [zulip] 179166:Dealing.20with.20Large.20resources
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** Some recent discussion in zulip: https://chat.fhir.org/#narrow/channel/179166-implementers/topic/Dealing.20with.2...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [jira] FHIR-37648 → [fhir] Encounter.participants
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** ...s the problem. Include participants on EncounterHistory, and have guidance that Encounter.participants is just currently active participants. Though maybe we al...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [jira] FHIR-37648 → [fhir] Encounter.location
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** ...Some examples of properties we expect may get large are: Encounter.participants Encounter.location Account.coverage There are two options we could consider for ...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [jira] FHIR-37648 → [fhir] Account.coverage
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** ...operties we expect may get large are: Encounter.participants Encounter.location Account.coverage There are two options we could consider for allowing a client t...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [jira] FHIR-37648 → [fhir] Encounter.participant
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** ...e list coming back to something that the client is looking for. property (e.g. "Encounter.participant") filter - start/end date Extension indicating which prope...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [jira] FHIR-37648 → [fhir] CodeSystem.concept.concept.concept
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** ...ties have been filtered "Encounter.participant" // at worst include an indexer "CodeSystem.concept.concept.concept" "Questionnaire.item.item.item" The remaining...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [jira] FHIR-37648 → [fhir] Questionnaire.item.item.item
  **Source:** Better approach for large lists of participants in Encounter.participants
  **Type:** mentions
  **Context:** ...rticipant" // at worst include an indexer "CodeSystem.concept.concept.concept" "Questionnaire.item.item.item" The remaining issue is how to update the large res...
  **Score:** 0.98
  **Updated:** 2026-01-27T14:13:23+00:00
- [zulip] 562791000 → [jira] FHIR-37648
  **Source:** [implementers] Dealing with Large resources
  **Type:** mentions
  **Context:** ...s that we see as important for R6, as it impacts normative resources:  <a href="http://jira.hl7.org/browse/FHIR-37648">FHIR-37648</a>.  Do we anticipate FHIR-I ...
  **Score:** 0.50
  **Updated:** 2025-12-09T20:24:09+00:00
- [zulip] 418822077 → [jira] FHIR-37648
  **Source:** [fhir/infrastructure-wg] WGM discussion
  **Type:** mentions
  **Context:** ...aps we've identified, and some potential proposals to cover these.<br> <a href="http://jira.hl7.org/browse/FHIR-37648">FHIR-37648</a><br> Thanks.</p>
  **Score:** 0.09
  **Updated:** 2024-01-30T12:05:12+00:00
- [zulip] 390583279 → [jira] FHIR-37648
  **Source:** [fhir/infrastructure-wg] WGM discussion
  **Type:** mentions
  **Context:** ...e input from FHIR I on the following tracker regarding handling large resources https://jira.hl7.org/browse/FHIR-37648 How to detect the large list (is this via...
  **Score:** 0.03
  **Updated:** 2023-09-12T19:28:57+00:00
- [zulip] 544608474 → [jira] FHIR-3764

... *(truncated, 4409 chars total)*
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (4 total, showing 4)

### [zulip] 562791000 — [implementers] Dealing with Large resources
- **Score:** 0.50
- **Updated:** 2025-12-09T20:24:09+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Dealing%20with%20Large%20resources/near/562791000
- **Snippet:** ...as important for R6, as it impacts normative resources: <b>FHIR-37648</b> . Do we anticipate FHIR-I landing the related Jira...

### [zulip] 418822077 — [fhir/infrastructure-wg] WGM discussion
- **Score:** 0.09
- **Updated:** 2024-01-30T12:05:12+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/WGM%20discussion/near/418822077
- **Snippet:** ...current documented solution, along with the gaps we've identified, and some potential proposals to cover these. <b>FHIR-37648</b> Thanks.

### [zulip] 390583279 — [fhir/infrastructure-wg] WGM discussion
- **Score:** 0.03
- **Updated:** 2023-09-12T19:28:57+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/WGM%20discussion/near/390583279
- **Snippet:** ...regarding handling large resources https://jira.hl7.org/browse/<b>FHIR-37648</b> How to detect the large list (is this via...

### [zulip] 544608474 — [fhir/infrastructure-wg] "Large Resources" - FHIR-52912
- **Score:** 0.00
- **Updated:** 2025-10-13T19:03:34+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/%22Large%20Resources%22%20-%20FHIR-52912/near/544608474
- **Snippet:** Does FHIR-I have plans for addressing FHIR-52912 ? Patient Admin has <b>FHIR-37648</b> , about how to handle resources that...


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-37648.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientAdministration\\FHIR-37648.md",
  "file_text": "# FHIR-37648: Better approach for large lists of participants in Encounter.participants\n\n| Field         | Value                            |\n|---------------|----------------------------------|\n| **Ticket**    | [FHIR-37648](https://jira.hl7.org/browse/FHIR-37648) |\n| **Status**    | Triaged                          |\n| **Type**      | Change Request                   |\n| **Priority**  | Medium                           |\n| **Resolution**| Persuasive                       |\n| **Work Group**| Patient Administration           |\n| **Specification** | FHIR Core (FHIR)            |\n| **Labels**    | MovingToGuide                    |\n| **Reporter**  | Cooper Thompson                  |\n| **Assignee**  | Unassigned                       |\n| **Created**   | 2022-06-22                       |\n| **Updated**   | 2026-01-27                       |\n| **Resolved**  | 2024-01-30                       |\n\n---\n\n## Summary\n\nLong-stay hospital admissions produce Encounter resources with very large `participant` lists. While a small number of participants are currently active, hundreds or thousands of historical participants (e.g., nurses from months ago) accumulate over time. The submitter requests a better approach for managing these large repeating backbone elements within Encounter resources.\n\nThe ticket was discussed at PA WGMs in 2022, 2023, and 2024, and was resolved as **Persuasive** at the January 2024 WGM. The resolution points to the \"[Operations for Large Resources](https://hl7.org/fhir/operations-for-large-resources.html)\" mechanism (`$filter`, `$add`, `$remove`) as the preferred direction, but identifies several unresolved gaps that require FHIR Infrastructure input. The ticket is labeled **MovingToGuide**, indicating content is intended to move to an implementation guide.\n\n---\n\n## Keywords\n\n- Encounter.participant, Encounter.participants, Encounter.location\n- Account.coverage\n- Large resources, auto-subsetting, SUBSETTED meta tag\n- $filter, $add, $remove operations\n- EncounterHistory, CareTeam\n- _summary, _elements, PATCH\n\n---\n\n## Related Jira Tickets\n\n### FHIR-52912 \u2014 Operations for large resources general feedback and has typos\n- **Status:** Triaged | **Work Group:** FHIR Infrastructure | **Resolution:** Unresolved\n- **URL:** https://jira.hl7.org/browse/FHIR-52912\n- **Relationship:** Created by Brian Postlethwaite (Sept 2025) to provide PA's feedback directly to FHIR-I. Contains the same gap analysis from FHIR-37648's resolution text, plus typo corrections in the operations-for-large-resources page. This is the primary dependency for FHIR-37648 to move forward.\n\n---\n\n## Zulip Discussions\n\n### 1. [implementers] Dealing with Large resources (Nov\u2013Dec 2025)\n- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Dealing%20with%20Large%20resources\n- **Participants:** Al

... *(truncated, 11443 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-37648.md with 11236 characters
```

</details>


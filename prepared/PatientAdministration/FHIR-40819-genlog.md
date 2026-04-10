# Session Log: FHIR-40819

**Phase:** prepared
**Work Group:** PatientAdministration
**Source File:** `prepared/PatientAdministration/FHIR-40819.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-40819` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:38:40 UTC |
| **Duration** | 110s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 297,855 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-40819
## Work Group: Patient Administration
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-40819.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-40819", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-40819", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-40819", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-40819.md
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
  "id": "FHIR-40819",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-40819: FHIR Identity Matching Guide recommendations are not as effective as they can be because they don't include previous names/aliases

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Administration
- **specification:** Interoperable Digital Identity and Patient Matching (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Matthew Visker
- **labels:** STU2, block-vote-6
- **Created:** 2023-04-17T12:46:52+00:00
- **Updated:** 2025-12-10T17:22:53+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-40819

## Content
<p>The identity matching refers to only the first and last name, which implies that patient's current name.  By not including previous names (which also includes variations of the names) in the guide, you might be limiting the number of good matches that the specs will support.  Patient names change and can be stored in different ways in different systems. It is common for one patient record to have a more updated version of the name - particularly when comparing data between systems.  While both systems might think they have the most up-to-date version of the name, that is not usually the case. For example, if a patient was recently married and changed their last name, when the patient is next seen, their name will be updated to their current name. However, another health system across town will still know the patient by their previous name. Using the framework described in this document, those two records would not be found as matches.  If the current health system also sends along a previous name, then they could establish a match.</p>

## Comments (3)

### lynn_laakso — 2025-12-10T17:22:53+00:00
<p>re-open post STU2 publication</p>

### lynn_laakso — 2025-12-10T17:22:53+00:00
<p>Reverted previous resolution: Considered for Future Use made 2025-07-15 00:00:00.0 with vote Humberto Lee / Reuben Daniels : 2 - 0 - 0//(Impact: null; Category: null; Version: null)//Recognizing that previous name has particular value to specific individuals, including those marrying and changing names, we are stopping short of assigning a weight to previous name at this time while we find an appropriate way to introduce a value while protecting patient privacy.</p>

### juliemaas — 2025-04-15T05:06:08+00:00
<p>Current guidance includes discussion of how to store previous names and these should be carried into the Patient resources used in match requests. This seems sufficient for now but the workgroup can discuss whether to provide more specific guidance in its version 3.</p>


## Snapshot
# FHIR-40819: FHIR Identity Matching Guide recommendations are not as effective as they can be because they don't include previous names/aliases

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Matthew Visker  
**Work Group:** Patient Administration  
**Specification:** Interoperable Digital Identity and Patient Matching (FHIR)  
**Labels:** STU2, block-vote-6  
**Created:** 2023-04-17  
**Updated:** 2025-12-10  

## Description

<p>The identity matching refers to only the first and last name, which implies that patient's current name.  By not including previous names (which also includes variations of the names) in the guide, you might be limiting the number of good matches that the specs will support.  Patient names change and can be stored in different ways in different systems. It is common for one patient record to have a more updated version of the name - particularly when comparing data between systems.  While both systems might think they have the most up-to-date version of the name, that is not usually the case. For example, if a patient was recently married and changed their last name, when the patient is next seen, their name will be updated to their current name. However, another health system across town will sti

... *(truncated, 5152 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-40819".
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
  "limit": 10,
  "sources": "zulip",
  "values": "previous name matching, patient name change matching weight"
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 528492015 — [implementers] Discussion on Representation of Middle Name and Maiden Name
- **Score:** 0.48
- **Updated:** 2025-07-13T00:21:44+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Discussion%20on%20Representation%20of%20Middle%20Name%20and%20Maiden%20Name/near/528492015
- **Snippet:** ...on identity <b>matching</b>. And it isn’t about the patient’s <b>previous</b> <b>name</b> (aka maiden <b>name</b>, birth <b>name</b>, or née).

### [zulip] 528439856 — [implementers] Discussion on Representation of Middle Name and Maiden Name
- **Score:** 0.26
- **Updated:** 2025-07-12T07:38:53+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Discussion%20on%20Representation%20of%20Middle%20Name%20and%20Maiden%20Name/near/528439856
- **Snippet:** ...HumanName.suffix Maiden <b>Name</b> <b>Previous</b> surname (for women) HumanName (use: "maiden") While scoping with GPT4.1 and search tool I...

### [zulip] 442584871 — [implementers] FHIR broker
- **Score:** 0.07
- **Updated:** 2024-06-04T17:28:34+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/FHIR%20broker/near/442584871
- **Snippet:** ...<b>previous</b> step -- [baseUrl]/Patient/$match FHIR IQB receives match scores and determines if match score meets IQB defined <b>matching</b> criteria...

### [zulip] 360391314 — [analytics on FHIR] SQL on FHIR WG
- **Score:** 0.03
- **Updated:** 2023-05-22T23:00:51+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/analytics%20on%20FHIR/topic/SQL%20on%20FHIR%20WG/near/360391314
- **Snippet:** ...on <b>name</b> <b>matching</b>. Is that correct? It seems like it could still be incorrectly used similar to our <b>previous</b> example...

### [zulip] 250383616 — [FHIR at Scale Taskforce (FAST): Identity] Patient safety issues related to identity and matching
- **Score:** 0.02
- **Updated:** 2021-08-23T17:25:56+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/FHIR%20at%20Scale%20Taskforce%20%28FAST%29%3A%20Identity/topic/Patient%20safety%20issues%20related%20to%20identity%20and%20matching/near/250383616
- **Snippet:** ...It would be helpful to have additional information such as <b>previous</b> <b>name</b> or former <b>name</b> (married, divorce), Preferred <b>name</b> (Jack...

### [zulip] 172199508 — [nordics] Middle Name
- **Score:** 0.01
- **Updated:** 2019-08-01T07:51:41+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/nordics/topic/Middle%20Name/near/172199508
- **Snippet:** ...Svensson), giving *one *family <b>name</b> consisting of two names (family <b>name</b>=Andersson Svensson) or 2) replace the <b>previous</b> family <b>name</b>...

### [zulip] 250394035 — [FHIR at Scale Taskforce (FAST): Identity] Patient safety issues related to identity and matching
- **Score:** 0.00
- **Updated:** 2021-08-23T18:43:48+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/FHIR%20at%20Scale%20Taskforce%20%28FAST%29%3A%20Identity/topic/Patient%20safety%20issues%20related%20to%20identity%20and%20matching/near/250394035
- **Snippet:** ...Two patients with the same fist <b>name</b> were scheduled for cataract surgery. The wrong patient was brought into the operating...

### [zulip] 231103890 — [fhircast-github] fhircast-docs / PR #356 Bump jinja2 from 2.10.1 to 2.11.3
- **Score:** 0.00
- **Updated:** 2021-03-19T23:29:33+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhircast-github/topic/fhircast-docs%20%2F%20PR%20%23356%20Bump%20jinja2%20from%202.10.1%20to%202.11.3/near/231103890
- **Snippet:** ...badges.githubapp.com/badges/compatibility_score?dependency-<b>name</b>=jinja2&package-manager=pip&<b>previous</b>-version=2.10.1&new-version=2...

### [zulip] 261937370 — [fhircast-github] fhircast-docs / PR #356 Bump jinja2 from 2.10.1 to 2.11.3
- **Score:** 0.00
- **Updated:** 2021-11-18T14:53:39+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhircast-github/topi

... *(truncated, 4760 chars total)*
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-40819.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientAdministration\\FHIR-40819.md",
  "file_text": "# FHIR-40819: Ticket Prep for Workgroup Review\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-40819](https://jira.hl7.org/browse/FHIR-40819) |\n| **Title** | FHIR Identity Matching Guide recommendations are not as effective as they can be because they don't include previous names/aliases |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved (re-opened post STU2 publication) |\n| **Specification** | Interoperable Digital Identity and Patient Matching (FHIR) |\n| **Work Group** | Patient Administration |\n| **Reporter** | Matthew Visker |\n| **Assignee** | Unassigned |\n| **Labels** | STU2, block-vote-6 |\n| **Created** | 2023-04-17 |\n| **Updated** | 2025-12-10 |\n\n## Description\n\nThe submitter argues that the Identity Matching Guide refers only to first and last name, implying the patient's current name. By not including previous names (including variations and aliases), the guide limits the number of good matches. Patient names change frequently (e.g., marriage) and can be stored differently across systems. If a patient recently changed their last name and one system has the new name while another has the old, the current matching framework would fail to find a match. Including previous names in match requests would help establish matches across systems with stale data.\n\n## Ticket History\n\n1. **2023-04-17** \u2014 Ticket created by Matthew Visker.\n2. **2025-04-15** \u2014 Julie Maas commented that current guidance already discusses how to store previous names and that these should be carried into Patient resources used in match requests; suggested deferring more specific guidance to version 3.\n3. **2025-07-15** \u2014 Resolved as **Considered for Future Use** with vote Humberto Lee / Reuben Daniels: 2-0-0. The WG noted that \"previous name has particular value to specific individuals, including those marrying and changing names,\" but chose to stop short of assigning a weight to previous name while finding \"an appropriate way to introduce a value while protecting patient privacy.\"\n4. **2025-12-10** \u2014 Lynn Laakso **re-opened** the ticket post STU2 publication, reverting the previous resolution.\n\n## Keywords\n\n`patient matching`, `previous names`, `aliases`, `identity matching`, `name change`, `HumanName`, `maiden name`, `match weight`, `patient privacy`, `$match`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-36802](https://jira.hl7.org/browse/FHIR-36802) | FHIR Identity Matching Guide should give guidance for matching on previous names or addresses | Published | Not Persuasive with Modification | **Highly related / predecessor** \u2014 Filed by the same reporter (Matthew Visker) in 2022, requesting the same thing: guidance on us

... *(truncated, 9499 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientAdministration\FHIR-40819.md with 9316 characters
```

</details>


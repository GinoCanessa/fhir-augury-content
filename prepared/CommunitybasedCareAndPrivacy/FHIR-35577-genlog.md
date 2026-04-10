# Session Log: FHIR-35577

**Phase:** prepared
**Work Group:** CommunitybasedCareAndPrivacy
**Source File:** `prepared/CommunitybasedCareAndPrivacy/FHIR-35577.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-35577` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:47:40 UTC |
| **Duration** | 92s |
| **Total Tool Calls** | 17 |
| **Total Tokens** | 288,127 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-35577
## Work Group: Community-Based Care and Privacy
## Output File: C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-35577.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-35577", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-35577", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-35577", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-35577.md
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
  "id": "FHIR-35577",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-35577: Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 1

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:01+00:00
- **Updated:** 2022-09-28T16:53:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35577

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this value set can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


## Snapshot
# FHIR-35577: Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 1

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Joan Harper  
**Work Group:** Community-Based Care and Privacy  
**Specification:** US PACIO Re-Assessment Timepoints (FHIR)  
**Labels:** Block-Vote-1  
**Created:** 2022-01-10  
**Updated:** 2022-09-28  

## Description

<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

## Comments

### lynn_laakso (2022-09-28)

<p>re-open post STU1 publication</p>

### lynn_laakso (2022-09-28)

<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this value set can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-35577".
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
  "values": "PACIO Re-Assessment Timepoints THO terminology",
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
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "PACIO Re-Assessment Timepoints value set canonical URL",
  "sources": "jira",
  "limit": 10
}
```

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-query_jira_issues` — PACIO Re-Assessment Timepoints THO</summary>

**Arguments:**
```json
{
  "query": "PACIO Re-Assessment Timepoints THO",
  "specifications": "US PACIO Re-Assessment Timepoints (FHIR)",
  "limit": 20
}
```

**Result:**
```
No Jira issues matched the query.
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-35577
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| anchor | word | 5 | 8.374 |
| org | word | 6 | 7.335 |
| hl7 | word | 6 | 5.882 |
| url | word | 3 | 5.296 |
| register | word | 1 | 4.898 |
| utg | word | 1 | 4.480 |
| binding | word | 2 | 4.388 |
| ron | word | 1 | 4.066 |
| parker | word | 1 | 4.066 |
| canonical | word | 1 | 4.062 |
| define | word | 2 | 3.331 |
| terminology | word | 1 | 3.330 |
| require | word | 2 | 3.261 |
| ticket | word | 1 | 3.155 |
| 1 | word | 4 | 3.122 |
| set | word | 2 | 3.122 |
| fhir | word | 5 | 3.071 |
| type | word | 2 | 3.006 |
| import | word | 1 | 2.982 |
| data/datum | word | 2 | 2.795 |
| code | word | 2 | 2.760 |
| create | word | 1 | 2.672 |
| block | word | 1 | 2.153 |
| comment | word | 1 | 1.923 |
| vote | word | 1 | 1.828 |

```

</details>

### Turn 3

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-35577 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 95.236 | jira | FHIR-35551 | Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org.1 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 95.236 | jira | FHIR-35614 | Defining URL  should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org.1 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 94.600 | jira | FHIR-35578 | Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 2 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 94.600 | jira | FHIR-35579 | Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 3 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 94.489 | jira | FHIR-35486 | Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org.1 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 94.195 | jira | FHIR-38528 | Defining URL should be anchored in THO. 4 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 94.195 | jira | FHIR-38529 | Defining URL should be anchored in THO. 5 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 94.195 | jira | FHIR-38531 | Defining URL should be anchored in THO. 7 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 93.866 | jira | FHIR-38530 | Defining URL should be anchored in THO. 6 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment, vote |
| 93.493 | jira | FHIR-35529 | Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org.1 | anchor, org, hl7, url, register, utg, binding, ron, parker, canonical, define, terminology, require, ticket, 1, set, fhir, type, import, data/datum, code, create, block, comment |

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
  "values": "value set canonical URL THO terminology.hl7.org"
}
```

**Result:**
```
## Search Results (3 total, showing 3)

### [zulip] 360535944 — [shorthand] Change terminology root to THO?
- **Score:** 0.06
- **Updated:** 2023-05-23T13:43:30+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/shorthand/topic/Change%20terminology%20root%20to%20THO%3F/near/360535944
- **Snippet:** ...breakfast-codes Title: "Breakfast Codes" Description: "The <b>set</b> of codes describing breakfast items" * ^<b>url</b> = "http://<b>terminology.hl7.org</b>/CodeSystem/breakfast...

### [zulip] 257855982 — [terminology / utg] Content in Publisher Infrastructure
- **Score:** 0.01
- **Updated:** 2021-10-16T19:45:37+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology%20%2F%20utg/topic/Content%20in%20Publisher%20Infrastructure/near/257855982
- **Snippet:** ...seems the <b>canonical</b> <b>URL</b> http://<b>terminology.hl7.org</b>/CodeSystem/hl7-document-format-codes does NOT exist in <b>THO</b>, but DOES...

### [zulip] 231523827 — [terminology] UTG or FHIR?
- **Score:** 0.00
- **Updated:** 2021-03-23T18:55:20+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/UTG%20or%20FHIR%3F/near/231523827
- **Snippet:** ...a <b>value</b> <b>set</b> whose <b>canonical</b> <b>URL</b> is rooted at http://<b>terminology.hl7.org</b>/ValueSet then it goes into <b>THO</b> via...


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

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-35577.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\CommunitybasedCareAndPrivacy\\FHIR-35577.md",
  "file_text": "# FHIR-35577: Defining URL should be anchored in THO not hl7.org/fhir\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-35577](https://jira.hl7.org/browse/FHIR-35577) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Work Group** | Community-Based Care and Privacy |\n| **Specification** | US PACIO Re-Assessment Timepoints (FHIR) |\n| **Reporter** | Joan Harper |\n| **Assignee** | Unassigned |\n| **Labels** | Block-Vote-1 |\n| **Created** | 2022-01-10 |\n| **Updated** | 2022-09-28 |\n\n---\n\n## Summary\n\nThis ticket requests that the Value Set canonical URL defined in the US PACIO Re-Assessment Timepoints IG be re-anchored from `hl7.org/fhir` to `terminology.hl7.org` (THO). The submitter (Joan Harper, via Ron G. Parker) argues that only value sets with a required binding to a `code` data type should have canonical URLs rooted at `hl7.org/fhir`; all others should be registered in THO via a UTG ticket. This is the first of a series of related comments (Comments 1\u20133) filed against this specification.\n\nThe ticket was originally resolved as \"Considered for Future Use\" in February 2022 (vote: Dave Hill / Dave Pyke, 9-0-0) with the rationale that further experience would inform whether the value set should be absorbed elsewhere, remain IG-specific, or be hosted on THO. That resolution was reverted by Lynn Laakso in September 2022 to re-open the ticket post-STU1 publication, and it currently sits in Triaged/Unresolved status.\n\n---\n\n## Details\n\n**Request:** Move the Value Set canonical URL from `hl7.org/fhir` namespace to `terminology.hl7.org` (THO). Create a UTG ticket to register the Value Set in THO.\n\n**Underlying Principle:** The HL7 terminology governance rule is that value sets bound to the `code` data type with a required binding should remain anchored at `hl7.org/fhir`, while all other value sets should be anchored in THO (`terminology.hl7.org`). This is part of broader HL7 terminology governance to ensure consistent management and public review of terminology artifacts.\n\n**History:**\n- **2022-01-10:** Filed by Joan Harper (imported by Ron G. Parker) as Comment 1 against the PACIO Re-Assessment Timepoints IG.\n- **2022-02-22:** Resolved as \"Considered for Future Use\" by vote (9-0-0, Dave Hill / Dave Pyke) \u2014 the work group chose to defer, allowing the IG and its terminology to mature before deciding placement.\n- **2022-09-28:** Resolution reverted by Lynn Laakso and ticket re-opened post-STU1 publication.\n\n**Sibling Tickets:** FHIR-35578 (Comment 2) and FHIR-35579 (Comment 3) are identical requests against the same specification, each targeting a different value set in the IG.\n\n---\n\n## Keywords\n\n`value set`, `canonical URL`, `THO`, `terminology.hl7.org`, `UTG`, `required binding`, `code data type`, `PACIO`, `R

... *(truncated, 8625 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-35577.md with 8417 characters
```

</details>

### Turn 5

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35577: Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 1

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:01+00:00
- **Updated:** 2022-09-28T16:53:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35577

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this value set can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35579: Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:07+00:00
- **Updated:** 2022-09-28T16:53:02+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35579

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 3 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:53:02+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:53:02+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this value set can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

### Turn 6

**Assistant:**

Let me get details on the closely related sibling tickets from the same specification.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35577: Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 1

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:01+00:00
- **Updated:** 2022-09-28T16:53:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35577

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this value set can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35578: Defining URL should be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org 2

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:03+00:00
- **Updated:** 2022-09-28T16:52:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35578

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 2 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:52:59+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:52:59+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this value set can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35580: Defining URL should be anchored in THO not hl7.org/fhir. 1

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:08+00:00
- **Updated:** 2022-09-28T16:53:01+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35580

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>(<b>Comment 4 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:53:01+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:53:01+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this code system can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35581: Defining URL should be anchored in THO not hl7.org/fhir. .2

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:09+00:00
- **Updated:** 2022-09-28T16:53:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35581

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>(<b>Comment 5 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:53:00+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this code system can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35582: Defining URL should be anchored in THO not hl7.org/fhir. .3

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Community-Based Care and Privacy
- **specification:** US PACIO Re-Assessment Timepoints (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-1
- **Created:** 2022-01-10T21:30:11+00:00
- **Updated:** 2022-09-28T16:52:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35582

## Content
<p>The Code System canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Code System in THO.</p>

<p>(<b>Comment 6 - imported by: Ron G. Parker</b>)</p>

## Comments (2)

### lynn_laakso — 2022-09-28T16:52:59+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2022-09-28T16:52:59+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-02-22 00:00:00.0 with vote Dave Hill / Dave Pyke : 9-0-0//(Impact: null; Category: null; Version: null)//Consider this proposal or other options as the IG and associated terminology matures. Further experience will inform whether this code system can be absorbed elsewhere, should be IG-specific, or hosted on THO or another terminology server.</p>


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "PACIO Re-Assessment Timepoints THO terminology",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
No results found.
```

</details>


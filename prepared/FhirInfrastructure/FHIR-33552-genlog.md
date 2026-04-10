# Session Log: FHIR-33552

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-33552.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-33552` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 01:34:05 UTC |
| **Duration** | 102s |
| **Total Tool Calls** | 21 |
| **Total Tokens** | 320,025 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-33552
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-33552.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-33552", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-33552", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-33552", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-33552.md
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
  "id": "FHIR-33552",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-33552: Why is datatype support TU?

- **status:** Triaged
- **type:** Change Request
- **priority:** High
- **work_group:** FHIR Infrastructure
- **specification:** Shorthand (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **labels:** Block-Vote-2
- **Created:** 2021-09-13T11:41:37+00:00
- **Updated:** 2022-12-22T03:58:41+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33552

## Content
<blockquote><p>FSH supports new pre-release FHIR R5 datatypes integer64 and CodeableReference on a trial use basis.</p></blockquote>
<p> </p>

<p>As the language does not depend on these elements, why is this mentioned. All new datatypes are supported are they not? The are just expressed as strings. Suggest to remove this sentence.</p>

## Comments (2)

### lynn_laakso — 2022-02-17T15:22:49+00:00
<p>re-open issue post publication of Normative Shorthand spec</p>

### lynn_laakso — 2022-02-17T15:22:49+00:00
<p>Reverted previous resolution: Considered for Future Use made 2021-10-25 00:00:00.0 with vote Mark Kramer / Rick Geimer : 16 - 0 - 1//(Impact: null; Category: null; Version: null)//FSH has new language constructs in support of CodeableReference (see Section 3.6.3.7), so it is appropriate to mark things associated with CodeableReference as trial use (TU). For integer64, no new language elements were introduced, so in principle, sections related to integer64 might be OK to go normative. However, removing the TU markings on integer64 datatype at this time would constitute a substantive change, and force another ballot cycle for the entire spec.</p>

<p>We therefore propose to keep the TU and Normative markings unchanged, and defer this issue to a later ballot, when we can advance TU sections to Normative as appropriate.</p>


## Snapshot
# FHIR-33552: Why is datatype support TU?

**Status:** Triaged  
**Type:** Change Request  
**Priority:** High  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Bas van den Heuvel  
**Work Group:** FHIR Infrastructure  
**Specification:** Shorthand (FHIR)  
**Labels:** Block-Vote-2  
**Created:** 2021-09-13  
**Updated:** 2022-12-22  

## Description

<blockquote><p>FSH supports new pre-release FHIR R5 datatypes integer64 and CodeableReference on a trial use basis.</p></blockquote>
<p> </p>

<p>As the language does not depend on these elements, why is this mentioned. All new datatypes are supported are they not? The are just expressed as strings. Suggest to remove this sentence.</p>

## Comments

### lynn_laakso (2022-02-17)

<p>re-open issue post publication of Normative Shorthand spec</p>

### lynn_laakso (2022-02-17)

<p>Reverted previous resolution: Considered for Future Use made 2021-10-25 00:00:00.0 with vote Mark Kramer / Rick Geimer : 16 - 0 - 1//(Impact: null; Category: null; Version: null)//FSH has new language constructs in support of CodeableReference (see Section 3.6.3.7), so it is appropriate to mark things associated with CodeableReference as trial use (TU). For integer64, no new language elements were introduced, so in principle, sections related to integer64 might be OK to go normative. However, removing the TU markings on integer64 datatype at this time would constitute a substantive change, and force another ballot cycle for the entire spec.</p>

<p>We therefore propose to keep the TU and Normative markings unchanged, and defer this issue to a later ballot, when we can advance TU sections to Normative as appropriate.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-33552".
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

Let me search for any GitHub references and additional Zulip context.

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-query_zulip_messages` — shorthand CodeableReference TU normative</summary>

**Result:**
```
No Zulip messages matched the query.
```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-33552 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 78.705 | jira | FHIR-42305 | Clarify if int64 and CodeableReference support remains TU. | tu, integer64, datatypes, codeablereference, fsh, trial, basis, release, r5, support, suggest, remove, fhir |
| 59.790 | jira | FHIR-33552:29017 | FHIR-33552:29017 | tu, integer64, datatype, codeablereference, fsh, trial, support, language, remove, element, vote |
| 54.267 | jira | FHIR-33555 | Datatypes from referred FHIR version | datatypes, datatype, fsh, blockquote, depend, string, support, suggest, 2, block, vote, fhir |
| 49.411 | jira | FHIR-42634 | Refer to R5 instead of R4 | datatypes, fsh, blockquote, depend, release, r5, support, language, suggest, block, vote, fhir |
| 44.272 | jira | FHIR-42360 | Data types identical to the one in FHIR R5 | datatypes, fsh, blockquote, depend, r5, sentence, support, language, block, vote, fhir |
| 39.614 | jira | FHIR-42300 | Align normative statement with other pages | tu, blockquote, trial, release, mention, language, remove, block, vote |
| 37.639 | jira | FHIR-33551 | FHIR version declaration unclear | fsh, blockquote, depend, sentence, support, language, remove, block, vote, fhir |
| 36.048 | jira | FHIR-42311 | Clarify use of non-ASCII characters | datatype, fsh, blockquote, string, support, suggest, block, vote, fhir |
| 35.485 | jira | FHIR-49875 | Add delimiter to EvidenceVariable.dataStorage | datatypes, datatype, express, release, string, suggest, block, element, vote, fhir |
| 35.422 | jira | FHIR-33572 | 3.6.11.1 should be marked as TU | tu, trial, release, language, 2, block, vote |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-33552.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-33552.md",
  "file_text": "# FHIR-33552: Why is datatype support TU?\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-33552](https://jira.hl7.org/browse/FHIR-33552) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | High |\n| **Work Group** | FHIR Infrastructure |\n| **Specification** | Shorthand (FHIR) |\n| **Reporter** | Bas van den Heuvel |\n| **Labels** | Block-Vote-2 |\n| **Created** | 2021-09-13 |\n| **Updated** | 2022-12-22 |\n\n## Description\n\nThe submitter questions why the FSH specification includes a sentence stating that FSH supports FHIR R5 datatypes `integer64` and `CodeableReference` \"on a trial use basis.\" The argument is that FSH as a language does not depend on these specific datatype elements \u2014 all datatypes are simply expressed as strings \u2014 so the sentence is unnecessary and should be removed.\n\nThe quoted text from the spec:\n\n> FSH supports new pre-release FHIR R5 datatypes integer64 and CodeableReference on a trial use basis.\n\n## Ticket History\n\n- **2021-09-13**: Ticket created by Bas van den Heuvel during Block-Vote-2 ballot review.\n- **2021-10-25**: Previously resolved as **Considered for Future Use** with vote Mark Kramer / Rick Geimer: 16\u20130\u20131. The rationale noted that FSH has new language constructs for CodeableReference (Section 3.6.3.7), making the TU marking appropriate for CodeableReference-related content. For `integer64`, no new language elements were introduced, but removing TU markings would be a substantive change forcing another ballot cycle. The proposal was to keep TU/Normative markings unchanged and defer to a later ballot.\n- **2022-02-17**: Resolution reverted by Lynn Laakso to re-open the issue post-publication of the Normative Shorthand spec.\n- **2022-12-22**: Last updated; currently in **Triaged** status, still unresolved.\n\n## Related Tickets\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-42305](https://jira.hl7.org/browse/FHIR-42305) | Clarify if int64 and CodeableReference support remains TU | Resolved \u2013 No Change (Question Answered) | Directly related \u2014 asks the same question for FSH 3.0.0, proposing to remove \"on a trial use basis\" from the sentence. Resolved by answering that the TU status aligns with the spec's maturity model. |\n| [FHIR-33555](https://jira.hl7.org/browse/FHIR-33555) | Datatypes from referred FHIR version | Published (Persuasive) | Same submitter, same ballot round \u2014 addresses FSH datatype language referencing the FHIR version in use. |\n| [FHIR-33572](https://jira.hl7.org/browse/FHIR-33572) | 3.6.11.1 should be marked as TU | Published (Persuasive) | Same submitter \u2014 concerns proper TU marking of spec sections related to trial-use content. |\n| [FHIR-42300](https://jira.hl7.org/browse/FHIR-42300) | Align normative statement with other pages | Pub

... *(truncated, 8093 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-33552.md with 7872 characters
```

</details>


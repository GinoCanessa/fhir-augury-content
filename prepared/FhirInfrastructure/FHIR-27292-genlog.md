# Session Log: FHIR-27292

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-27292.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-27292` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:10:47 UTC |
| **Duration** | 76s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 243,481 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-27292
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-27292.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-27292", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-27292", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-27292", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-27292.md
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
  "id": "FHIR-27292",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-27292: Doc should be more pedagogical

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** Shorthand (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Keith W. Boone
- **labels:** Block-Vote-3
- **Created:** 2020-05-19T21:34:25+00:00
- **Updated:** 2020-10-12T23:45:06+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-27292

## Content
<p>The reference is good enough for a specification, but not good enough to teach people how to use it.  The example is very limited.  There should be a little bit more of an introductory approach to how to use SUSHI for practical work in this guide.  Think about the first half of the K&amp;R which introduced The C Programming Language </p>

## Comments (3)

### lynn_laakso — 2020-10-12T23:45:06+00:00
<p>Re-opening after publication of STU1</p>

### lynn_laakso — 2020-10-12T23:45:06+00:00
<p>Reverted previous resolution: Considered for Future Use made 2020-07-06 00:00:00.0 with vote Moesel/Rhodes 11-0-1//(Impact: null; Category: null; Version: null)//Improving the documentation is an ongoing process. We recently introduced the Overview to try and address the "what is it all about" type of question. It could always be better, but together with the tutorials (available here: <a href="https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track)</a> there is quite a bit of documentation. We propose to defer re-writing the documentation to get a release of a reasonably good version in a timely way.</p>

### mark_kramer — 2020-05-21T18:29:06+00:00
<p>We recently introduced the Overview to try and fill this gap. The tutorials should also be considered part of the package (available here: <a href="https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track)</a></p>


## Snapshot
# FHIR-27292: Doc should be more pedagogical

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Keith W. Boone  
**Work Group:** FHIR Infrastructure  
**Specification:** Shorthand (FHIR)  
**Labels:** Block-Vote-3  
**Created:** 2020-05-19  
**Updated:** 2020-10-12  

## Description

<p>The reference is good enough for a specification, but not good enough to teach people how to use it.  The example is very limited.  There should be a little bit more of an introductory approach to how to use SUSHI for practical work in this guide.  Think about the first half of the K&amp;R which introduced The C Programming Language </p>

## Comments

### lynn_laakso (2020-10-12)

<p>Re-opening after publication of STU1</p>

### lynn_laakso (2020-10-12)

<p>Reverted previous resolution: Considered for Future Use made 2020-07-06 00:00:00.0 with vote Moesel/Rhodes 11-0-1//(Impact: null; Category: null; Version: null)//Improving the documentation is an ongoing process. We recently introduced the Overview to try and address the "what is it all about" type of question. It could always be better, but together with the tutorials (available here: <a href="https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track)</a> there is quite a bit of documentation. We propose to defer re-writing the documentation to get a release of a reasonably good version in a timely way.</p>

### mark_kramer (2020-05-21)

<p>We recently introduced the Overview to try and fill this gap. The tutorials should also be considered part of the package (available here: <a href="https://confluence.hl

... *(truncated, 4194 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-27292" (1 results)

- [jira] FHIR-27292 → [confluence] 2020
  **Source:** Doc should be more pedagogical
  **Type:** mentions
  **Context:** ...on. It could always be better, but together with the tutorials (available here: https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track) there is q...
  **Score:** 0.06
  **Updated:** 2020-10-12T23:45:06+00:00
**Warnings:**
- Value 'FHIR-27292' is not a valid Zulip message ID

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

Now let me search for any GitHub references related to this ticket.

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-27292.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-27292.md",
  "file_text": "# FHIR-27292: Doc should be more pedagogical\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-27292](https://jira.hl7.org/browse/FHIR-27292) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Specification** | Shorthand (FHIR) |\n| **Work Group** | FHIR Infrastructure |\n| **Reporter** | Keith W. Boone |\n| **Assignee** | Unassigned |\n| **Labels** | Block-Vote-3 |\n| **Created** | 2020-05-19 |\n| **Updated** | 2020-10-12 |\n| **Resolution** | Unresolved |\n\n## Summary\n\nKeith W. Boone requests that the FHIR Shorthand (FSH) specification documentation take a more pedagogical (teaching-oriented) approach rather than serving solely as a reference specification. The reporter notes that while the reference material is adequate as a spec, it lacks introductory material to teach practical usage. He specifically cites the first half of Kernighan & Ritchie's \"The C Programming Language\" as a model \u2014 a narrative, tutorial-style introduction before the formal reference. The reporter also notes that the examples are \"very limited\" and calls for more practical, worked examples of using SUSHI.\n\n## Keywords\n\n- FHIR Shorthand (FSH)\n- SUSHI\n- Documentation\n- Pedagogical / tutorial\n- Specification readability\n- Onboarding / introductory material\n\n## Prior Discussion & History\n\n### Comment History (3 comments)\n\n1. **mark_kramer (2020-05-21):** Acknowledged the gap and noted that an Overview section was recently introduced. Pointed to external tutorials on Confluence ([2020-05 FHIR Shorthand Track](https://confluence.hl7.org/display/FHIR/2020-05+FHIR+Shorthand+Track)) as complementary learning material.\n\n2. **lynn_laakso (2020-10-12):** Documented the previous resolution \u2014 *Considered for Future Use* with vote Moesel/Rhodes 11-0-1. The rationale stated: \"Improving the documentation is an ongoing process. We recently introduced the Overview\u2026 We propose to defer re-writing the documentation to get a release of a reasonably good version in a timely way.\"\n\n3. **lynn_laakso (2020-10-12):** Re-opened the ticket after publication of STU1, reverting the previous \"Considered for Future Use\" resolution.\n\n### Zulip Conversations\n\nNo Zulip discussions found referencing FHIR-27292.\n\n### GitHub Items\n\nNo GitHub issues or pull requests found referencing FHIR-27292.\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-27166](https://jira.hl7.org/browse/FHIR-27166) | Missing reference section | Published | Persuasive | Also addresses FSH spec documentation gaps \u2014 requests a formal references section listing specification dependencies. |\n| [FHIR-27277](https://jira.hl7.org/browse/FHIR-27277) | Revisit SUSHI section based on latest SUSHI / IG Publisher integration discussions 

... *(truncated, 7351 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-27292.md with 7163 characters
```

</details>


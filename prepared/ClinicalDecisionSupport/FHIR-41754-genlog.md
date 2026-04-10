# Session Log: FHIR-41754

**Phase:** prepared
**Work Group:** ClinicalDecisionSupport
**Source File:** `prepared/ClinicalDecisionSupport/FHIR-41754.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-41754` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:43:58 UTC |
| **Duration** | 91s |
| **Total Tool Calls** | 17 |
| **Total Tokens** | 349,875 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-41754
## Work Group: Clinical Decision Support
## Output File: C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-41754.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-41754", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-41754", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-41754", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-41754.md
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
  "id": "FHIR-41754",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-41754: Clarify parameter values

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Clinical Decision Support
- **specification:** Clinical Quality Language (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bryn Rhodes
- **Created:** 2023-08-14T16:23:26+00:00
- **Updated:** 2024-08-26T14:40:45+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-41754

## Content
<p>Current language states:</p>

<p>&gt; In other words, the value for the default of a parameter must be able to be calculated at compile-time.</p>

<p>But this does not make clear the intended semantics that the value that is calculated at compile-time must be the same as the value that would be calculated at run-time.</p>

<p>The specific case in question is the use of Today(), Now(), and TimeOfDay(), because although they could in theory be calculated at compile-time, they would in general not be the same value as what would be calculated at run-time, at least per run.</p>

## Comments (2)

### JIRAUSER25154 — 2023-10-31T13:58:01+00:00
<p>Most languages have a clear concept of what constitutes a constant e.g. [C#|<a href="https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/constants" class="external-link" target="_blank" rel="nofollow noopener">https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/classes-and-structs/constants</a>.]  I'd say we should just stay aligned with prior art and declare that parameter default values can only be literal expressions.</p>

### JIRAUSER23970 — 2023-08-14T17:41:04+00:00
<p>The value of `Now()` (and derived functions) is required by the spec to remain constant during the period of execution of the CQL (i.e. run-time). It'd be pretty surprising, IMO, for `Now()` to be fixed at compile-time and it would significantly reduce the usability of ELM. For example, if you have a rolling window of `Encounter` (e.g. "encounters during the last 2 days"), and `Now()` was fixed at compile-time you'd have to recompile the CQL continuously for that value to be updated. Distribution of ELM-based artifacts would become much more difficult because they would need to be continuously updated as well. Alternatively, you could generally prohibit the use of ELM and only allow the use of CQL for compliant implementations such that value of `Now()` was continuously recompiled and the fixed value updated during every execution.</p>

<p>It seems the best resolution is to make clear that "compile-time" means anything that could be calculated at compile time and that would also remain constant at runtime. This would forbid the use of certain built-in functions like `Now()` in default parameter values but the behavior would otherwise remain the same.</p>


## Snapshot
# FHIR-41754: Clarify parameter values

**Status:** Triaged  
**Type:** Technical Correction  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Bryn Rhodes  
**Work Group:** Clinical Decision Support  
**Specification:** Clinical Quality Language (FHIR)  
**Created:** 2023-08-14  
**Updated:** 2024-08-26  

## Description

<p>Current language states:</p>

<p>&gt; In other words, the value for the default of a parameter must be able to be calculated at compile-time.</p>

<p>But this does not make clear the intended semantics that the value that is calculated at compile-time must be the same as the value that would be calculated at run-time.</p>

<p>The specific case in question is the use of Today(), Now(), and TimeOfDay(), because although they could in theory be calculated at compile-time, they would in general not be the same value as what would be calculated at run-time, at least per run.</p>

## Comments

### JIRAUSER25154 (2023-10-31)

<p>Most languages have a clear concept of what constitutes a constant e.g. [C#|<a href="https://learn.microsoft.com/en-us/dotnet/csharp/p

... *(truncated, 5561 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-41754".
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

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-41326",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-41326: Provide a "default comparison precision"

- **status:** Applied
- **type:** Change Request
- **priority:** Medium
- **work_group:** Clinical Decision Support
- **specification:** Clinical Quality Language (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Bryn Rhodes
- **Created:** 2023-05-23T20:41:25+00:00
- **Updated:** 2025-07-22T06:14:42+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-41326

## Content
<p>Date and time comparison in CQL supports specifying the precision of the comparison. By default, comparisons will be performed to the millisecond precision. However, clinical logic often involves comparisons only to the minute, so it would be useful to provide a mechanism for specifying a default comparison precision, avoiding the need for authors to specify minute precision for all date/time comparisons.</p>

<p>The proposed approach would be to define a "directive" that would be able to be specified as part of a library and would only apply to the expressions and function definitions within that library.</p>

<p>Note that defining a parameter that would provide this capability should not be considered viable since it would change runtime behavior of the logic, and this should be an author-time consideration. It is part of the intent of the logic and should not be varied by run-time considerations.</p>

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-41754.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\ClinicalDecisionSupport\\FHIR-41754.md",
  "file_text": "# FHIR-41754: Clarify parameter values\n\n## Summary\n\n| Field          | Value                              |\n|----------------|------------------------------------|\n| **Ticket**     | [FHIR-41754](https://jira.hl7.org/browse/FHIR-41754) |\n| **Status**     | Triaged                            |\n| **Type**       | Technical Correction               |\n| **Priority**   | Medium                             |\n| **Resolution** | Unresolved                         |\n| **Work Group** | Clinical Decision Support          |\n| **Specification** | Clinical Quality Language (FHIR) |\n| **Reporter**   | Bryn Rhodes                        |\n| **Assignee**   | Unassigned                         |\n| **Created**    | 2023-08-14                         |\n| **Updated**    | 2024-08-26                         |\n\n## Description\n\nThe CQL specification currently states that \"the value for the default of a parameter must be able to be calculated at compile-time.\" However, this language does not adequately clarify that the compile-time value must also be the same as the value that would be computed at run-time.\n\nThe specific concern involves functions like `Today()`, `Now()`, and `TimeOfDay()`. While these can technically be evaluated at compile-time, their values would generally differ from what would be computed at run-time (since the date/time changes between compilation and execution). The ticket requests that the specification language be tightened to exclude such time-dependent functions from parameter default values.\n\n## Keywords\n\n`CQL`, `parameter`, `default value`, `compile-time`, `run-time`, `Now()`, `Today()`, `TimeOfDay()`, `constant expression`, `literal`, `ELM`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-48682](https://jira.hl7.org/browse/FHIR-48682) | Consider parameter constraints | Applied (Persuasive) | Closely related \u2014 extends parameter semantics in CQL by adding constraint definitions; directly builds on parameter default value concepts discussed in this ticket. |\n| [FHIR-41326](https://jira.hl7.org/browse/FHIR-41326) | Provide a \"default comparison precision\" | Applied (Persuasive) | Tangentially related \u2014 also a CQL specification change by the same reporter that addresses default behavior and explicitly notes that parameters should not change runtime behavior of logic. |\n\n## Zulip Discussions\n\nNo Zulip conversations referencing FHIR-41754 or the specific topic of parameter default compile-time semantics were found.\n\n## GitHub Items\n\nNo GitHub issues or pull requests referencing FHIR-41754 were found.\n\n## Comment Analysis\n\nTwo comments provide substantive input:\n\n1. **JIRAUSER23970 (2023-08-14):** Argues against fixing `Now()` at compile-time because the CQL spec requires `Now()` to remain constant only during a 

... *(truncated, 6790 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-41754.md with 6614 characters
```

</details>


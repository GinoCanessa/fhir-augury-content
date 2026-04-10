# Session Log: FHIR-36106

**Phase:** prepared
**Work Group:** ClinicalDecisionSupport
**Source File:** `prepared/ClinicalDecisionSupport/FHIR-36106.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-36106` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:23:46 UTC |
| **Duration** | 105s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 302,344 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-36106
## Work Group: Clinical Decision Support
## Output File: C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-36106.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-36106", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-36106", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-36106", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-36106.md
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
  "id": "FHIR-36106",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-36106: DataRequirement reference to canonical(StructureDefinition) should also permit Questionniare (and maybe ObservationDefinition)

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Clinical Decision Support
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Brian Postlethwaite
- **Created:** 2022-02-24T22:53:22+00:00
- **Updated:** 2022-08-03T20:47:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-36106

## Content
<p>The use case we're wanting to support is where we want to have answers to a specific Quesitonnaire (via QuestionnaireResponse) trigger the requirement to complete another Questionnaire be completed via a PlanDefinition.</p>

<p>The QuestionnaireResponse that is entered isn't based on a profile, it's based on the Questionnaire, so want to be able to reference that definition.</p>

<p>(also would like to suggest that maybe ObservationDefinition could also be included)</p>

## Comments (3)

### bryn.rhodes — 2022-08-03T20:47:05+00:00
<p>Discussing in CPG-on-FHIR, there are definitely potential advantages for some use cases, can we work through a specific example to get details worked out?</p>

### bryn.rhodes — 2022-07-29T19:31:01+00:00
<p>This is an interesting and common use case, but it's a fairly significant expansion of what a data requirement fundamentally is. It would mean that we could talk about data requirements not only in terms of FHIR resource types and profiles, but in terms of Questionnaires and potentially other definitional type resources like ObservationDefinition and SpecimenDefinition. Note that there is precedent for that in the ActivityDefinition, and doing it as an expansion of data requirements would support that use case more cleanly (those feel a bit out of place in ActivityDefinition anyway).</p>

<p>Needs discussion at an upcoming CDS and/or CPG-on-FHIR call. Will add to agendas there.</p>

### mckenzie — 2022-05-09T17:43:41+00:00
<p>CDS has the primary interest in this data type, so FHIR-I would like a CDS opinion before proceeding to evaluate the change.  Please put in a proposed resolution and toss it back to us once you've had time to discuss.</p>


## Snapshot
# FHIR-36106: DataRequirement reference to canonical(StructureDefinition) should also permit Questionniare (and maybe ObservationDefinition)

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Brian Postlethwaite  
**Work Group:** Clinical Decision Support  
**Specification:** FHIR Core (FHIR)  
**Created:** 2022-02-24  
**Updated:** 2022-08-03  

## Description

<p>The use case we're wanting to support is where we want to have answers to a specific Quesitonnaire (via QuestionnaireResponse) trigger the requirement to complete another Questionnaire be completed via a PlanDefinition.</p>

<p>The QuestionnaireResponse that is entered isn't based on a profile, it's based on the Questionnaire, so want to be able to reference that definition.</p>

<p>(also would like to suggest that maybe ObservationDefinition could also be included)</p>

## Comments

### bryn.rhodes (2022-08-03)

<p>Discussing in CPG-on-FHIR, there are definitely potential advantages for some use cases, can we work through a specific example to get details worked out?</p>

### bryn.rhodes (2022-07-29)

<p>This is an interesting and common use case, but it's a fairly significant expansion of what a data requirement fundamentally is. It would mean that we could talk about data requirements not only in terms of FHIR resource types and profiles, but in terms of Questionnaires and potentially other definitional type resources like ObservationDefinition and SpecimenDefinition. Note that there is precedent for that in the ActivityDefinition, and doing it as an expansion of data requirements would support that us

... *(truncated, 4444 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-36106".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-36106.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\ClinicalDecisionSupport\\FHIR-36106.md",
  "file_text": "# FHIR-36106: DataRequirement reference to canonical(StructureDefinition) should also permit Questionnaire (and maybe ObservationDefinition)\n\n## Ticket Summary\n\n| Field | Value |\n|---|---|\n| **Key** | [FHIR-36106](https://jira.hl7.org/browse/FHIR-36106) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | FHIR Core (FHIR) |\n| **Work Group** | Clinical Decision Support |\n| **Reporter** | Brian Postlethwaite |\n| **Assignee** | Unassigned |\n| **Created** | 2022-02-24 |\n| **Updated** | 2022-08-03 |\n\n## Description\n\nBrian Postlethwaite requests that `DataRequirement.profile` (currently typed as `canonical(StructureDefinition)`) be expanded to also permit references to **Questionnaire** and possibly **ObservationDefinition**.\n\nThe motivating use case is a PlanDefinition-driven workflow where a completed QuestionnaireResponse for one Questionnaire triggers a requirement to complete a different Questionnaire. Because QuestionnaireResponse is based on a Questionnaire (not a StructureDefinition profile), the current DataRequirement type binding is too restrictive to express this requirement.\n\nThe reporter also suggests that ObservationDefinition could be useful as an additional permitted target.\n\n## Keywords\n\n`DataRequirement`, `canonical`, `StructureDefinition`, `Questionnaire`, `QuestionnaireResponse`, `ObservationDefinition`, `PlanDefinition`, `trigger`, `profile`, `definitional resources`\n\n## Comment History\n\n1. **mckenzie (2022-05-09):** FHIR-I defers to CDS for evaluation. Requested CDS provide a proposed resolution before FHIR-I proceeds.\n2. **bryn.rhodes (2022-07-29):** Acknowledged as an interesting and common use case but noted it represents a \"fairly significant expansion\" of what DataRequirement fundamentally is \u2014 moving from FHIR resource types and profiles to definitional resources like Questionnaire, ObservationDefinition, and SpecimenDefinition. Noted there is precedent in ActivityDefinition. Scheduled for CDS and/or CPG-on-FHIR discussion.\n3. **bryn.rhodes (2022-08-03):** Discussed in CPG-on-FHIR. Acknowledged potential advantages for some use cases. Requested a specific worked example to get details sorted out.\n\n## Related Jira Tickets\n\n| Key | Title | Status | Relevance |\n|---|---|---|---|\n| [FHIR-32898](https://jira.hl7.org/browse/FHIR-32898) | QuestionnaireResponse should allow instantiates | Applied (Persuasive with Modification) | Directly related \u2014 addresses QuestionnaireResponse's relationship to triggering protocols/PlanDefinitions. |\n| [FHIR-35941](https://jira.hl7.org/browse/FHIR-35941) | Explain boundaries between Questionnaire and QuestionnaireResponse and Composition | Published (Persuasive with Modification) | Context \u2014 clarifies resource boundary questions relevant to how 

... *(truncated, 9307 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\ClinicalDecisionSupport\FHIR-36106.md with 9124 characters
```

</details>


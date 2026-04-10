# Session Log: FHIR-27821

**Phase:** planned
**Work Group:** ClinicalDecisionSupport
**Source File:** `planned/ClinicalDecisionSupport/FHIR-27821.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `6bb6405b-1d1b-4b0b-b4a9-631f765aa3bb` |
| **Session Summary** | Create Ticket Implementation Plans |
| **Agent ID** | `plan-FHIR-27821` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:33:08 UTC |
| **Duration** | 1371s |
| **Total Tool Calls** | 26 |
| **Total Tokens** | 714,582 |

---

## Task Prompt

````markdown
You are planning the implementation of FHIR Jira ticket FHIR-27821 ("PlanDefinition.action.definition[x] list issues") for the "Clinical Decision Support" work group.

Your job is to produce a structured implementation plan report and save it to:
C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-27821.md

## Data Access

Use MCP tools directly (prefixed with `FhirAugury-`).

### MCP Tool Reference

| MCP Tool | Purpose |
|----------|---------|
| `FhirAugury-get_item` | Fetch full details of an item from a source |
| `FhirAugury-cross_referenced` | Get all cross-references (both directions) for a value |
| `FhirAugury-refers_to` | Get outgoing cross-references from an item |
| `FhirAugury-referred_by` | Get incoming cross-references to an item |
| `FhirAugury-content_search` | Unified text search across all sources |
| `FhirAugury-get_keywords` | Get extracted keywords for an item |
| `FhirAugury-related_by_keyword` | Find items related by keyword similarity |

## Known GitHub Repository Cache

Repositories cloned under `cache/github/repos/`: HL7_fhir, HL7_UTG, HL7_fhir-extensions, plus incubator repos.

## Workflow

### Step 1: Gather Ticket Details (run in parallel)
1a. `FhirAugury-get_item(source="jira", id="FHIR-27821", includeComments=true, includeContent=true, includeSnapshot=true)`
1b. `FhirAugury-cross_referenced(value="FHIR-27821", limit=50)`
1c. `FhirAugury-get_keywords(source="jira", id="FHIR-27821", limit=30)`

### Step 2-4: Determine repos, analyze impact, build report using standard format.

## Important Rules
- Use only data from MCP and cached repositories. Do not fabricate.
- Be specific. Include actual file paths verified to exist.
- Read the resolution description carefully — it dictates what to implement.
- Only "Applied", "Persuasive", "Persuasive with Modification" require implementation.

Save the final report to: C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-27821.md

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
  "id": "FHIR-27821",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-27821: PlanDefinition.action.definition[x] list issues

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Clinical Decision Support
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Brian S. Alper
- **reporter:** Peter Bomberg
- **labels:** Block-Vote-1, eCTDM3
- **Created:** 2020-06-15T15:21:44+00:00
- **Updated:** 2025-03-18T09:09:28+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-27821

## Content
<p>If plandefinition is to be used for non clinical aspects, such as the master schedule for inspections and other procedures then the PlanDefinition.action.definition<span class="error">&#91;x&#93;</span> list either becomes extensible (in which case we add procedure) or procedure needs to be added to the list otherwise we have to add an intermediate level (activitiydefinition) that adds no  value solely to link the procedure to the plandefinition.</p>

## Comments (12)

### bryn.rhodes — 2025-03-18T09:09:28+00:00
<p>Per the resolution, we need an example of a PlanDefinition representing a manufacturing protocol. I assume the PQ/CMC project has several of these as part of their implementation guides?</p>

### bryn.rhodes — 2023-03-12T18:26:58+00:00
<p>Need to work with BR&amp;R to get a specific example we can include in the specification</p>

### bryn.rhodes — 2022-02-08T18:16:59+00:00
<p>We discussed this with BR&amp;R during the last WGM and clarified that the PlanDefinition is in definitional space, but that the RequestGroup resource is the "instance" of a PlanDefinition, so that when you have a need to reference a particular Procedure in the PlanDefinition, that would be an ActivityDefinition (or even just an action of kind "ServiceRequest") to identify what Procedure needs to be done in the abstract, and a RequestGroup instance to represent an actual orchestration referencing instances of Procedure.</p>

<p>Perhaps the thing to do here is include an example PlanDefinition modeling these types of activities for inclusion as an example in the specification?</p>

### peter.bomberg — 2021-10-06T03:36:34+00:00
<p>added examples</p>

### peter.bomberg — 2021-10-06T03:27:29+00:00
<p>Hello Bryn, a couple examples.</p>

<p>Psychical Security Assessments consist of a series of predefined activity definitions/packages, often with sub activities depending on the type/nature or the assessment.  We need a method of managing this as a single unit. Note: we are not talking about the executed inspection but the objective and the associated activities. The activities are often reused to support several objectives and are managed as a sub unit (versioned, approved, etc.).</p>

<p> </p>

<p>Another type is an environment inspection, there are many sub activities (Air quality, lighting, airflow, temp, humidity, etc..) each of these has one or more tasks associated with it, again not the instance but the definition (who, how, when, why, etc.).</p>

<p> </p>

<p>I hope this helps and clarifies how we would use an overall objective definition to point to one or more sub activities that in turn have one or more associated tasks.</p>

<p> </p>

### bryn.rhodes — 2021-07-07T16:17:33+00:00
<p>CDS discussed 7/7, can we get a specific example of how you would like to use PlanDefinition actions to reference Procedure? We are also looking for other examples from the CDS WG to help inform the design.</p>

### peter.bomberg — 2021-07-04T18:18:43+00:00
<p>Hello Bryn, any thoughts on how to move this Jira forward?</p>

### peter.bomberg — 2021-05-28T14:33:54+00:00
<p>The problem is task represents a single and isolated action, not a sequence of tasks that relate to a common objective.</p>

<p>Tasks also are not managed as a package, a procedure definition that involves 20 discrete tasks can be used in several plans, as an example physical security inspections relate to initial inspections, annu

... *(truncated, 11775 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-27821" (3 results)

- [jira] FHIR-27821 → [fhir] PlanDefinition.action.definition
  **Source:** PlanDefinition.action.definition[x] list issues
  **Type:** mentions
  **Context:** ...ects, such as the master schedule for inspections and other procedures then the PlanDefinition.action.definition [x] list either becomes extensible (in which ca...
  **Score:** 0.64
  **Updated:** 2025-03-18T09:09:28+00:00
- [jira] FHIR-27821 → [fhir] PlanDefinition.action.definition[x]
  **Source:** PlanDefinition.action.definition[x] list issues
  **Type:** mentions
  **Context:** ...nition) that adds no value solely to link the procedure to the plandefinition. 	PlanDefinition.action.definition[x] list issues Add an example of a PlanDefiniti...
  **Score:** 0.64
  **Updated:** 2025-03-18T09:09:28+00:00
- [jira] FHIR-27821 → [fhir] ActivityDefinition.product
  **Source:** PlanDefinition.action.definition[x] list issues
  **Type:** mentions
  **Context:** ... however extending ActivityDefinition to support non clinical activities in the ActivityDefinition.product [x] might be an easier and cleaner approach. However ...
  **Score:** 0.64
  **Updated:** 2025-03-18T09:09:28+00:00
**Warnings:**
- Value 'FHIR-27821' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-27821
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| plandefinition.action.definition | fhir_path | 3 | 14.177 |
| plandefinition | fhir_path | 10 | 10.588 |
| activitiydefinition | word | 1 | 9.280 |
| action | word | 6 | 7.265 |
| inspection | word | 1 | 6.783 |
| ectdm3 | word | 1 | 6.435 |
| procedure | word | 4 | 6.395 |
| intermediate | word | 1 | 6.103 |
| solely | word | 1 | 6.043 |
| manufacture | word | 1 | 5.786 |
| schedule | fhir_path | 1 | 5.391 |
| list | fhir_path | 4 | 5.278 |
| aspect | word | 1 | 4.805 |
| definition | word | 6 | 4.643 |
| protocol | word | 1 | 4.544 |
| master | word | 1 | 4.026 |
| extensible | word | 1 | 3.911 |
| span | word | 2 | 3.691 |
| level | word | 1 | 3.044 |
| 93 | word | 1 | 3.014 |
| 91 | word | 1 | 2.995 |
| clinical | word | 1 | 2.983 |
| represent | word | 1 | 2.882 |
| example | word | 1 | 2.876 |
| issue | word | 2 | 2.853 |
| add | word | 5 | 2.836 |
| error | word | 1 | 2.410 |
| case | word | 1 | 2.130 |
| block | word | 1 | 1.965 |
| comment | word | 1 | 1.755 |

```

</details>

### Turn 2

**Assistant:**

Now I have all the information needed. Let me create the implementation plan report:

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-27821.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\planned\\ClinicalDecisionSupport\\FHIR-27821.md",
  "file_text": "# Implementation Plan: FHIR-27821\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-27821](https://jira.hl7.org/browse/FHIR-27821) |\n| **Title** | PlanDefinition.action.definition[x] list issues |\n| **Status** | Resolved \u2014 change required |\n| **Resolution** | Persuasive with Modification |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Work Group** | Clinical Decision Support |\n| **Specification** | FHIR Core (FHIR) |\n| **Assignee** | Brian S. Alper |\n| **Reporter** | Peter Bomberg |\n| **Labels** | Block-Vote-1, eCTDM3 |\n| **Created** | 2020-06-15 |\n| **Updated** | 2025-03-18 |\n\n## Resolution Description\n\n> Add an example of a PlanDefinition that represents a manufacturing protocol as described in the examples in the comments.\n\n## Problem Statement\n\nThe original request asked for `PlanDefinition.action.definition[x]` to support referencing `Procedure` resources directly (or for the binding to become extensible) so that non-clinical use cases (e.g., manufacturing protocols, physical security inspections, environment inspections) could be represented without requiring an intermediate `ActivityDefinition` layer.\n\nAfter extensive discussion between the reporter (Peter Bomberg) and CDS work group (Bryn Rhodes), the resolution was modified to:\n1. **Not** change the `definition[x]` type list or binding.\n2. Clarify that the existing mechanism \u2014 using `ActivityDefinition` with `kind=ServiceRequest` to describe abstract procedures, and `RequestOrchestration` for instances \u2014 already supports these use cases.\n3. **Add an example** PlanDefinition representing a manufacturing protocol to demonstrate this pattern.\n\n## Feature Proposal\n\nAdd a new PlanDefinition example resource file to the FHIR Core specification that illustrates a **manufacturing protocol** use case. The example should demonstrate:\n\n1. A `PlanDefinition` with `type` of `clinical-protocol` (or potentially no type, since this is non-clinical) that models a manufacturing/inspection protocol.\n2. Hierarchical actions with sub-activities (e.g., environment inspection \u2192 air quality, lighting, temperature, humidity sub-checks).\n3. Use of contained `ActivityDefinition` resources with `kind=ServiceRequest` to define each inspection/manufacturing step.\n4. Use of `definitionCanonical` references from actions to the contained `ActivityDefinition` resources.\n5. Sequencing relationships between actions using `relatedAction` where appropriate.\n\nThis demonstrates that non-clinical protocols can be represented using the existing PlanDefinition structure without modifying `definition[x]`.\n\n## Impact Analysis\n\n### Scope of Change\n\nThis is an **example-only** change. No structural modifications to the PlanDefinition resource, no new elements, no binding changes. The impact is limited to:\n- One ne

... *(truncated, 14469 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-27821.md with 14184 characters
```

</details>


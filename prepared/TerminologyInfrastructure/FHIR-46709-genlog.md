# Session Log: FHIR-46709

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-46709.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-46709` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:02:55 UTC |
| **Duration** | 96s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 283,479 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-46709
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-46709.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-46709", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-46709", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-46709", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-46709.md
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
  "id": "FHIR-46709",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-46709: SNOMED Change Set content inflexible

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** Terminology Change Set Exchange (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Michael Lawley
- **Created:** 2024-08-22T23:50:50+00:00
- **Updated:** 2025-03-26T23:52:04+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-46709

## Content
<p>The profile has explicit slices for ~75 of the current set of 105 active concept properties in SNOMED CT - how are the remaining ones handled?</p>

<p>National extensions of SNOMED CT may have additional properties (SNOMED CT-AU has about 20 extra). How are these handled?</p>

<p> </p>

## Comments (1)

### mjlawley — 2025-03-26T23:52:04+00:00
<p>Using a self-referential ValueSet like this (ie it's a ValueSet wrt SNOMED that is being used to constrain an update to SNOMED) it will need to be very clear and careful about versioning – which version the ValueSet is relative to.</p>

<p>Furthermore, if the change itself is adding a new property, then the expansion of the ValueSet will not contain that property for old versions of SNOMED, but it won't be expandable against the updated version because the ChangeSet itself describes the update.</p>


## Snapshot
# FHIR-46709: SNOMED Change Set content inflexible

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Persuasive  
**Assignee:** Unassigned  
**Reporter:** Michael Lawley  
**Work Group:** Terminology Infrastructure  
**Specification:** Terminology Change Set Exchange (FHIR)  
**Created:** 2024-08-22  
**Updated:** 2025-03-26  
**Resolved:** 2024-11-19  

## Description

<p>The profile has explicit slices for ~75 of the current set of 105 active concept properties in SNOMED CT - how are the remaining ones handled?</p>

<p>National extensions of SNOMED CT may have additional properties (SNOMED CT-AU has about 20 extra). How are these handled?</p>

<p> </p>

## Resolution Description

<p>We will adjust the modelling to use bindings to ValueSets for properties instead of slicing:</p>
<ul>
	<li>Create the following:
	<ul>
		<li>CodeSystem of CodeSystem property values and associated FHIR datatypes, indicating applicable source CodeSystem</li>
		<li>ValueSets for the properties associated with each individual CodeSystem (e.g., SNOMED Properties ValueSet, LOINC Properties ValueSet)</li>
	</ul>
	</li>
</ul>

## Comments

### mjlawley (2025-03-26)

<p>Using a self-referential ValueSet like this (ie it's a ValueSet wrt SNOMED that is being used to constrain an update to SNOMED) it will need to be very clear and careful about versioning – which version the ValueSet is relative to.</p>

<p>Furthermore, if the change itself is adding a new property, then the expansion of the ValueSet will not contain that property for old versions of SNOMED, but it won't be expandable against the updated version because the ChangeSet itself describes the update.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-46709".
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
  "values": "change set exchange terminology, SNOMED property slicing"
}
```

**Result:**
```
## Search Results (5 total, showing 5)

### [zulip] 431597198 — [fmg] FMG e-Vote for 2024-04-05
- **Score:** 0.11
- **Updated:** 2024-04-05T20:13:59+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fmg/topic/FMG%20e-Vote%20for%202024-04-05/near/431597198
- **Snippet:** Hi all! Here is the e-vote we discussed conducting on the updated <b>Terminology</b> <b>Change</b> <b>Set</b> <b>Exchange</b> IG Proposal: https...

### [zulip] 276805190 — [terminology] OMOP Vocab Concept Persistence
- **Score:** 0.00
- **Updated:** 2022-03-27T20:06:51+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/OMOP%20Vocab%20Concept%20Persistence/near/276805190
- **Snippet:** ...preserved, if one <b>set</b> changes in size (eg a new version), then all subsequent ids will <b>change</b>. Now, if there...

### [zulip] 417707875 — [genomics] Validation issue for HGVS/HGNC code
- **Score:** 0.00
- **Updated:** 2024-01-24T18:56:05+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/genomics/topic/Validation%20issue%20for%20HGVS%2FHGNC%20code/near/417707875
- **Snippet:** ...system": "http://loinc.org", "code": "48004-6" } ], "text": "DNA <b>change</b> (c.HGVS)" }, "valueCodeableConcept": { "coding": [ { "system": "http://varnomen.hgvs.org", "code...

### [zulip] 208929387 — [terminology] SNOMED CT Version Syntax
- **Score:** 0.00
- **Updated:** 2020-09-03T07:25:11+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/SNOMED%20CT%20Version%20Syntax/near/208929387
- **Snippet:** ...for MyHR when V2/V3 <b>change</b> over came in AMT_CODE_SYSTEM Australian Medicines <b>Terminology</b> - Version used (v2 or v3...

### [zulip] 166091168 — [bulk data] Block vote #1
- **Score:** 0.00
- **Updated:** 2019-05-20T14:50:16+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/bulk%20data/topic/Block%20vote%20%231/near/166091168
- **Snippet:** ...for common system data <b>set</b> like <b>terminology</b> data in addition to common clinical data <b>set</b> - BULKDATA #3 (Yunwei Wang) GF...


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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-46709.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-46709.md",
  "file_text": "# FHIR-46709: SNOMED Change Set content inflexible\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-46709](https://jira.hl7.org/browse/FHIR-46709) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Persuasive |\n| **Specification** | Terminology Change Set Exchange (FHIR) |\n| **Work Group** | Terminology Infrastructure |\n| **Reporter** | Michael Lawley |\n| **Assignee** | Unassigned |\n| **Created** | 2024-08-22 |\n| **Updated** | 2025-03-26 |\n\n## Problem Statement\n\nThe SNOMED CT Change Set profile in the Terminology Change Set Exchange IG defines explicit slices for approximately 75 of the 105 currently active SNOMED CT concept properties. This approach has two problems:\n\n1. **Incomplete coverage:** ~30 active SNOMED CT properties are not covered by the explicit slices, leaving no defined mechanism for handling them.\n2. **National extension inflexibility:** National extensions of SNOMED CT (e.g., SNOMED CT-AU) define additional properties (~20 extra for Australia). The rigid slicing approach provides no mechanism to accommodate these extension-specific properties.\n\n## Resolution Description (from Jira)\n\nThe resolution was marked **Persuasive**. The agreed approach is to replace explicit property slicing with ValueSet-based bindings:\n\n- Create a **CodeSystem of CodeSystem property values** with associated FHIR datatypes, indicating the applicable source CodeSystem.\n- Create **per-CodeSystem ValueSets** for properties (e.g., a \"SNOMED Properties ValueSet\", a \"LOINC Properties ValueSet\").\n\nThis allows extensibility: national extensions can define their own property ValueSets without requiring profile changes.\n\n## Commenter Concerns\n\n**Michael Lawley (2025-03-26):** Raised a versioning concern with self-referential ValueSets \u2014 a ValueSet defined relative to SNOMED CT that also constrains updates to SNOMED CT creates a circular dependency:\n- The ValueSet must be clear about which SNOMED CT version it references.\n- If the change set itself adds a new property, the ValueSet expansion for old SNOMED versions won't include it, but the updated version can't be used because the ChangeSet *is* the update.\n\n## Related Jira Tickets\n\n| Ticket | Title | Relevance |\n|--------|-------|-----------|\n| [FHIR-48265](https://jira.hl7.org/browse/FHIR-48265) | Increase specificity of change set metadata | Same specification (Terminology Change Set Exchange). Addresses granularity of change metadata \u2014 complements this ticket's property extensibility concern. Status: Applied, Resolution: Persuasive. |\n| [FHIR-27006](https://jira.hl7.org/browse/FHIR-27006) | CodeSystem.concept.property does not document a binding | Related core FHIR issue about missing property bindings on CodeSystem.concept.property. Resolved as Not Persuasive, but 

... *(truncated, 7267 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-46709.md with 7097 characters
```

</details>


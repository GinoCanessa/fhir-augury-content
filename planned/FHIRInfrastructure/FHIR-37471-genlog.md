# Session Log: FHIR-37471

**Phase:** planned
**Work Group:** FHIRInfrastructure
**Source File:** `planned/FHIRInfrastructure/FHIR-37471.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `3e333f90-0a2a-437a-b44b-59600ee4ecc6` |
| **Session Summary** | Continue Creating Ticket Plans |
| **Agent ID** | `plan-FHIR-37471` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 13:58:24 UTC |
| **Duration** | 409s |
| **Total Tool Calls** | 23 |
| **Total Tokens** | 626,849 |

---

## Task Prompt

````markdown
You are planning the implementation of FHIR Jira ticket FHIR-37471 ("Please add instance examples for each approved FHIR extension") for the "FHIR Infrastructure" work group.

Save report to: C:/ai/git/fhir-augury-content/planned/FHIRInfrastructure/FHIR-37471.md

## Repository Cache Check
Cached repos: HL7/fhir, HL7/UTG, HL7/fhir-extensions, HL7/admin-incubator, HL7/api-incubator-ig, HL7/capstmt, HL7/cg-incubator, HL7/ebm-incubator, HL7/fhir-testing-ig, HL7/immunization-incubator, HL7/oo-incubator.
If this ticket requires a repo NOT in this list, say: "REPO_NOT_CACHED: {owner/repo}" in your output.

## Data Access — Use MCP tools (prefixed with `FhirAugury-`).

## Workflow
### Step 1: Gather (parallel)
- `FhirAugury-get_item(source="jira", id="FHIR-37471", includeComments=true, includeContent=true, includeSnapshot=true)`
- `FhirAugury-cross_referenced(value="FHIR-37471", limit=50)`
- `FhirAugury-get_keywords(source="jira", id="FHIR-37471", limit=30)`

### Step 2-4: Determine repos, analyze impact, build report with all standard sections.

## Rules
- Use only MCP data and cached repos. Don't fabricate.
- Be specific with paths, elements, types.
- Only "Applied"/"Persuasive"/"Persuasive with Modification" need implementation.
- Search repo clones for real files.

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
  "id": "FHIR-37471",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-37471: Please add instance examples for each approved FHIR extension

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Gay Dolin
- **labels:** Deferred
- **Created:** 2022-05-17T21:13:03+00:00
- **Updated:** 2025-11-06T17:05:09+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-37471

## Content
<p>Please add instance examples for each approved FHIR extension</p>

## Comments (5)

### mckenzie — 2023-03-20T19:25:23+00:00
<p>Motion to re-open 2023-03-20 Grahame Grieve/Josh Mandel: 14-0-0</p>

### mckenzie — 2023-03-20T19:25:23+00:00
<p>Reverted previous resolution: Persuasive with Modification made 2022-05-23 00:00:00.0 with vote Grahame Grieve/Gino Canessa: 8-0-0//(Impact: Non-substantive; Category: Enhancement; Version: null)//Will refer to FMG to make this a quality consideration. </p>

### mckenzie — 2023-02-12T01:56:05+00:00
<p>Now that we have extensions in a separate IG, this is more complicated.  Will need to discuss within FHIR-I where to make examples live - and how to check if they're missing.</p>

### mckenzie — 2022-09-23T18:40:15+00:00
<p>This is no longer for FMG, it's FHIR-I.  We can now add this to official methodology.  Put forward a post-R5 tracker item for tools to spit out warnings about this.</p>

### rgeimer — 2022-05-23T20:52:06+00:00
<p>Please raise with FMG</p>


## Snapshot
# FHIR-37471: Please add instance examples for each approved FHIR extension

**Status:** Resolved - change required  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Persuasive with Modification  
**Assignee:** Unassigned  
**Reporter:** Gay Dolin  
**Work Group:** FHIR Infrastructure  
**Specification:** FHIR Core (FHIR)  
**Labels:** Deferred  
**Created:** 2022-05-17  
**Updated:** 2025-11-06  
**Resolved:** 2023-03-20  

## Description

<p>Please add instance examples for each approved FHIR extension</p>

## Resolution Description

<p>Now that we have moved extension definitions out of the core spec, we will do the following:</p>
<ol>
	<li>Update the publisher to be able to check the core spec and any dependency IGs for use of extensions defined in that IG</li>
	<li>Update the tooling to render such cross-referenced examples in the examples tab for the extension</li>
	<li>Spit out a warning if there are no examples that reference an extension either in the extension IG itself or an ancestor</li>
	<li>Set an expectation for work groups to clean up all said warnings.</li>
</ol>

## Comments

### mckenzie (2023-03-20)

<p>Motion to re-open 2023-03-20 Grahame Grieve/Josh Mandel: 14-0-0</p>

### mckenzie (2023-03-20)

<p>Reverted previous resolution: Persuasive with Modification made 2022-05-23 00:00:00.0 with vote Grahame Grieve/Gino Canessa: 8-0-0//(Impact: Non-substantive; Category: Enhancement; Version: null)//Will refer to FMG to make this a quality consideration. </p>

### mckenzie (2023-02-12)

<p>Now that we have extensions in a separate IG, this is more complicated.  Will need to discuss within FHIR-I where to make examples live - and how to check if they're missing.</p>

### mckenzie (2022-09-23)

<p>This is no longer for FMG, it's FHIR-I.  We can now add this to official methodology.  Put forward a post-R5 tracker item for tools to spit out warnings about this.</p>

### rgeimer (2022-05-23)

<p>Please raise with FMG</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-37471".
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-37471
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| spit | word | 1 | 6.952 |
| ancestor | word | 1 | 6.881 |
| warning | word | 2 | 6.258 |
| baseresource | word | 1 | 5.912 |
| example | word | 6 | 5.795 |
| instance | word | 3 | 5.167 |
| ol | word | 2 | 5.103 |
| clean | word | 1 | 4.989 |
| dependency | word | 1 | 4.972 |
| li | word | 8 | 4.769 |
| tab | word | 1 | 4.746 |
| render | word | 1 | 4.680 |
| cross | word | 1 | 4.625 |
| spec | word | 2 | 4.619 |
| extension | word | 8 | 4.585 |
| approve | word | 3 | 4.550 |
| expectation | word | 1 | 4.319 |
| publisher | word | 1 | 4.243 |
| defer | word | 1 | 3.962 |
| igs | word | 1 | 3.817 |
| check | word | 1 | 3.455 |
| tool | word | 1 | 3.453 |
| move | word | 1 | 3.228 |
| group | word | 1 | 3.035 |
| core | word | 2 | 3.020 |
| ig | word | 2 | 2.852 |
| reference | word | 2 | 2.774 |
| work | word | 1 | 2.744 |
| update | word | 2 | 2.703 |
| fhir | word | 3 | 2.555 |

```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\planned\FHIRInfrastructure\FHIR-37471.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\planned\\FHIRInfrastructure\\FHIR-37471.md",
  "file_text": "# FHIR-37471: Implementation Plan\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-37471](https://jira.hl7.org/browse/FHIR-37471) |\n| **Title** | Please add instance examples for each approved FHIR extension |\n| **Status** | Resolved \u2013 change required |\n| **Resolution** | Persuasive with Modification |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Work Group** | FHIR Infrastructure |\n| **Specification** | FHIR Core (FHIR) |\n| **Labels** | Deferred |\n| **Reporter** | Gay Dolin |\n| **Resolved** | 2023-03-20 (vote: Grahame Grieve/Josh Mandel 14-0-0) |\n\n### Resolution Description\n\n> Now that we have moved extension definitions out of the core spec, we will do the following:\n> 1. Update the publisher to be able to check the core spec and any dependency IGs for use of extensions defined in that IG\n> 2. Update the tooling to render such cross-referenced examples in the examples tab for the extension\n> 3. Spit out a warning if there are no examples that reference an extension either in the extension IG itself or an ancestor\n> 4. Set an expectation for work groups to clean up all said warnings.\n\n### Key Context from Comments\n\n- **2023-02-12 (mckenzie):** Extensions now live in a separate IG (`hl7.fhir.uv.extensions`), making this \"more complicated\" \u2014 need to determine where examples live and how to detect missing ones.\n- **2022-09-23 (mckenzie):** Shifted from FMG to FHIR-I. Can now add to official methodology. Requested post-R5 tooling tracker for warnings.\n\n---\n\n## Feature Proposal\n\n### Goal\n\nEnsure every approved FHIR extension has at least one discoverable usage example \u2014 either within its own IG, in the core spec, or in a dependency/ancestor IG \u2014 and that the IG Publisher provides clear feedback when examples are missing.\n\n### Current State\n\n1. **`HL7/fhir-extensions` repo** contains **~689 extension StructureDefinitions** with **zero example instances** in the IG itself.\n2. The IG configuration (`extensions-ig.xml`) sets `no-usage-check = true`, suppressing all missing-example warnings.\n3. The IG Publisher's validation (`PublisherProcessor.validateSD()`, line 718\u2013724) already warns when an extension has no examples \u2014 but only checks **local IG files** via `countUsages()`.\n4. The IG Publisher's renderer (`StructureDefinitionRenderer.references()`, lines 2307\u20132367) **already finds cross-IG examples** from three sources:\n   - Core spec R5 examples (via `sdmap.details` from `hl7.fhir.r5.core`)\n   - Dependency IGs (via `relatedIgs` loop)\n   - Special `r5-examples.json` + `hl7.fhir.r5.examples` package (for `hl7.fhir.uv.extensions` only)\n5. The `exampleList()` / `exampleTable()` methods (lines 1571\u20131615) only render **local IG examples** \u2014 cross-IG examples appear only in the `references()` \"Usage\" section.\n\n##

... *(truncated, 15211 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\planned\FHIRInfrastructure\FHIR-37471.md with 14856 characters
```

</details>


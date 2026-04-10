# Session Log: FHIR-28456

**Phase:** planned
**Work Group:** ClinicalDecisionSupport
**Source File:** `planned/ClinicalDecisionSupport/FHIR-28456.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `6bb6405b-1d1b-4b0b-b4a9-631f765aa3bb` |
| **Session Summary** | Create Ticket Implementation Plans |
| **Agent ID** | `plan-FHIR-28456` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:00:33 UTC |
| **Duration** | 195s |
| **Total Tool Calls** | 25 |
| **Total Tokens** | 787,688 |

---

## Task Prompt

````markdown
You are planning the implementation of FHIR Jira ticket FHIR-28456 ("Concern about optionality for metadata") for the "Clinical Decision Support" work group.

Your job is to produce a structured implementation plan report and save it to:
C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-28456.md

## Data Access

Use MCP tools directly (prefixed with `FhirAugury-`).

| MCP Tool | Purpose |
|----------|---------|
| `FhirAugury-get_item` | Fetch full details of an item from a source |
| `FhirAugury-cross_referenced` | Get all cross-references (both directions) for a value |
| `FhirAugury-content_search` | Unified text search across all sources |
| `FhirAugury-get_keywords` | Get extracted keywords for an item |
| `FhirAugury-related_by_keyword` | Find items related by keyword similarity |

## Known GitHub Repository Cache

Repositories cloned under `cache/github/repos/`: HL7_fhir, HL7_UTG, HL7_fhir-extensions, plus incubator repos.

## Workflow

### Step 1: Gather Ticket Details (run in parallel)
1a. `FhirAugury-get_item(source="jira", id="FHIR-28456", includeComments=true, includeContent=true, includeSnapshot=true)`
1b. `FhirAugury-cross_referenced(value="FHIR-28456", limit=50)`
1c. `FhirAugury-get_keywords(source="jira", id="FHIR-28456", limit=30)`

### Step 2-4: Determine repos, analyze impact, build report using standard format.

## Important Rules
- Use only data from MCP and cached repositories. Do not fabricate.
- Be specific. Include actual file paths verified to exist.
- Read the resolution description carefully — it dictates what to implement.
- Only "Applied", "Persuasive", "Persuasive with Modification" require implementation.

Save the final report to: C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-28456.md

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
  "id": "FHIR-28456",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-28456: Concern about optionality for metadata

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Clinical Decision Support
- **specification:** CDS Hooks (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Floyd Eisenberg
- **Created:** 2020-09-09T16:15:06+00:00
- **Updated:** 2025-10-15T16:41:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-28456

## Content
<p>Consider evaluating optionality with respect to requirements for evaluating the effectiveness of the CDS Hook. I.e., prefetch, url, topic, uuid for source, suggestions, actions. Retrospective analysis of effectiveness and efficiency requires significant metadata that will be missing with many of these elements being OPTIONAL.</p>

## Comments (5)

### feisenberg — 2025-10-08T14:07:36+00:00
<p>Agree with proposed modifications to guidance as discussed 8 October 2025 with Bryn, Isaac, Vadim</p>

### isaac.vetter — 2025-07-02T14:01:59+00:00
<p>Hey @Floyd Eisenberg, can you please join an upcoming CDS WG call to discuss this issue?</p>

### feisenberg — 2025-03-05T14:47:22+00:00
<p>Disagree with proposed resolution. Without metadata about overrides aggregate management of performance, reasons for override, system managers and guideline creators have no information to support greater efficiency, avoid overburdening the wrong actors, and improving the guideline. Please pull this ticket for discussion and coordinate so I can attend.</p>

### lynn_laakso — 2022-09-14T21:06:07+00:00
<p>re-open post STU2 publication</p>

### lynn_laakso — 2022-09-14T21:06:07+00:00
<p>Reverted previous resolution: Considered for Future Use made 2020-11-25 00:00:00.0 with vote Bas van den Heuvel/Matthew Burton: 13-0-0//(Impact: null; Category: null; Version: null)//&gt;Consider evaluating optionality with respect to requirements for evaluating the effectiveness of the CDS Hook. I.e., prefetch, url, topic, uuid for source, suggestions, actions. Retrospective analysis of effectiveness and efficiency requires significant metadata that will be missing with many of these elements being OPTIONAL.<br/>
 <br/>
Hey Floyd,<br/>
 <br/>
I think there's a couple categories of why the listed fields are optional, for example: suggestions and actions are optional because a CDS Service may not have discrete/actionable guidance for a given patient, whereas, prefetch is optional because a service may not request prefetch'd information or a CDS client may be unable to satisfy that request.   <br/>
 <br/>
We did try to make this STU2 spec release not break existing implementations built on the STU1 release. The size and type of feature added in STU2 reflects this – we didn't need to rip out or substantially alter the existing specification; rather, the STU2 spec simply adds some additional features and clarifications. <br/>
 <br/>
One of these new features – the feedback service, is actually, exactly intended to more easily enable "retrospective analysis of effectiveness" of the CDS Service. To your point, support of this feedback service is .... OPTIONAL, both for the service and the client. Again, the reasoning here was to not break backward compatibility. <br/>
 <br/>
As we see increased adoption of this feature and related, we're look for opportunities to unify implementations by making more features required, instead of optional. <br/>
 <br/>
Isaac<br/>
 <br/>
 </p>


## Snapshot
# FHIR-28456: Concern about optionality for metadata

**Status:** Resolved - change required  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Not Persuasive with Modification  
**Assignee:** Unassigned  
**Reporter:** Floyd Eisenberg  
**Work Group:** Clinical Decision Support  
**Specification:** CDS Hooks (FHIR)  
**Created:** 2020-09-09  
**Updated:** 2025-10-15  
**Resolved:** 2025-10-08  

## Description

<p>Consider evaluating optionality

... *(truncated, 7169 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-28456".
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-28456
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| effectiveness | word | 2 | 11.559 |
| optionality | word | 3 | 10.893 |
| retrospective | word | 1 | 7.900 |
| metadata | word | 3 | 7.833 |
| efficiency | word | 1 | 7.828 |
| uuid | word | 1 | 6.673 |
| topic | word | 2 | 6.535 |
| evaluate | word | 2 | 6.466 |
| prefetch | word | 1 | 6.213 |
| concern | word | 2 | 6.052 |
| optional | word | 2 | 5.837 |
| respect | word | 1 | 5.654 |
| seek | word | 1 | 5.415 |
| analysis | word | 1 | 5.285 |
| significant | word | 1 | 5.260 |
| stu | word | 1 | 4.751 |
| applicable | word | 1 | 4.666 |
| hook | word | 1 | 4.617 |
| suggestion | word | 1 | 4.423 |
| cds | word | 1 | 4.308 |
| action | word | 1 | 4.140 |
| feedback | word | 1 | 4.135 |
| source | word | 1 | 3.772 |
| missing | word | 1 | 3.666 |
| url | word | 1 | 3.455 |
| element | word | 3 | 3.394 |
| case | word | 2 | 3.372 |
| ballot | word | 1 | 3.265 |
| provide | word | 1 | 3.093 |
| guidance | word | 1 | 3.050 |

```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-28456.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\planned\\ClinicalDecisionSupport\\FHIR-28456.md",
  "file_text": "# FHIR-28456: Concern about optionality for metadata\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-28456](https://jira.hl7.org/browse/FHIR-28456) |\n| **Title** | Concern about optionality for metadata |\n| **Status** | Resolved \u2014 change required |\n| **Resolution** | Not Persuasive with Modification |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Work Group** | Clinical Decision Support |\n| **Specification** | CDS Hooks (FHIR) |\n| **Reporter** | Floyd Eisenberg |\n| **Created** | 2020-09-09 |\n| **Resolved** | 2025-10-08 |\n\n## Original Request\n\nThe submitter requested that the CDS Hooks specification evaluate the optionality of key metadata elements \u2014 specifically `prefetch`, `url`, `topic`, `uuid` (for source), `suggestions`, and `actions` \u2014 with respect to requirements for retrospective analysis of CDS Hook effectiveness and efficiency. The concern is that when these elements are OPTIONAL, implementations will frequently omit them, making it impossible to aggregate data for quality improvement and learning health system goals.\n\n## Resolution Description\n\n> We will add a ballot/STU note that:\n> We are seeking feedback on the use of topic in specific use cases.\n>\n> Review each optional element and provide guidance for how the element may be applicable within an example use case.\n\nThe resolution does **not** change any element from OPTIONAL to REQUIRED. Instead, it adds:\n1. A **ballot/STU note** seeking community feedback on the use of `source.topic` in specific use cases\n2. **Guidance text** for each relevant optional element explaining how it may be applicable, illustrated with example use cases\n\n## Feature Proposal\n\n### What Changes\n\nAdd non-normative guidance and a ballot note to the CDS Hooks specification to help implementers understand the value and applicability of optional metadata elements. This consists of:\n\n1. **STU Note on `source.topic`**: Insert a ballot/STU note (admonition block) near the `source.topic` field definition in the specification, seeking implementer feedback on how `topic` is used in practice and in which use cases it provides value.\n\n2. **Guidance paragraphs for optional elements**: For each of the following optional elements, add a brief guidance paragraph (or expand existing description) explaining when and why the element should be populated, with a concrete example use case:\n   - `card.uuid` \u2014 needed for feedback/audit trails\n   - `source.url` \u2014 provides traceability to the evidence source\n   - `source.topic` \u2014 enables filtering, categorization, and analytics\n   - `suggestions` / `suggestion.actions` \u2014 enable actionable decision support and outcome tracking\n   - `suggestion.uuid` \u2014 required for feedback tracking of accepted suggestions\n   - `prefetch` (on Discovery) \u2014 impr

... *(truncated, 13564 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\planned\ClinicalDecisionSupport\FHIR-28456.md with 13350 characters
```

</details>


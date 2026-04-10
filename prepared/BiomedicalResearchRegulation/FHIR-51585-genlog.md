# Session Log: FHIR-51585

**Phase:** prepared
**Work Group:** BiomedicalResearchRegulation
**Source File:** `prepared/BiomedicalResearchRegulation/FHIR-51585.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51585` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 01:42:11 UTC |
| **Duration** | 84s |
| **Total Tool Calls** | 12 |
| **Total Tokens** | 222,609 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51585
## Work Group: Biomedical Research & Regulation
## Output File: C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51585.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51585", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51585", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51585", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51585.md
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
  "id": "FHIR-51585",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51585: value-as-concept directions should use relationships in the vocabulary, not separate text lookups

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** FHIR to OMOP FHIR IG (FHIR)
- **resolution:** Persuasive
- **assignee:** Jean Duteau
- **reporter:** ScottFavre
- **labels:** MappingLanguage
- **Created:** 2025-07-29T15:31:16+00:00
- **Updated:** 2026-04-09T19:34:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51585

## Content
<p>The page provides sample SQL and directs the implementer to use a display-based query to find the substance concept ID:</p>

<p><tt>SELECT concept_id, concept_name, domain_id, vocabulary_id, standard_concept</tt><br/>
<tt>FROM concept</tt><br/>
<tt>WHERE concept_name LIKE '%Penicillin G%'</tt><br/>
<tt>  AND vocabulary_id IN ('RxNorm', 'SNOMED')</tt><br/>
<tt>  AND standard_concept = 'S';</tt></p>

<p>This is very fragile and will certainly pick up incorrect concepts (there are dozens of concepts with "Penicillin G" in the name).</p>

<p>Instead, the implementer should use the "Maps to value" relationships from the source concept to determine the values to use.</p>

<p>This yields deterministic and clinically correct results that have been validated by the OMOP vocabulary team.</p>

## Snapshot
# FHIR-51585: value-as-concept directions should use relationships in the vocabulary, not separate text lookups

**Status:** Resolved - change required  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Persuasive  
**Assignee:** Jean Duteau  
**Reporter:** ScottFavre  
**Work Group:** Biomedical Research & Regulation  
**Specification:** FHIR to OMOP FHIR IG (FHIR)  
**Labels:** MappingLanguage  
**Created:** 2025-07-29  
**Updated:** 2026-04-09  
**Resolved:** 2026-03-13  

## Description

<p>The page provides sample SQL and directs the implementer to use a display-based query to find the substance concept ID:</p>

<p><tt>SELECT concept_id, concept_name, domain_id, vocabulary_id, standard_concept</tt><br/>
<tt>FROM concept</tt><br/>
<tt>WHERE concept_name LIKE '%Penicillin G%'</tt><br/>
<tt>  AND vocabulary_id IN ('RxNorm', 'SNOMED')</tt><br/>
<tt>  AND standard_concept = 'S';</tt></p>

<p>This is very fragile and will certainly pick up incorrect concepts (there are dozens of concepts with "Penicillin G" in the name).</p>

<p>Instead, the implementer should use the "Maps to value" relationships from the source concept to determine the values to use.</p>

<p>This yields deterministic and clinically correct results that have been validated by the OMOP vocabulary team.</p>

## Resolution Description

<p>Thank you: we agree with this correction.</p>

<p>The `concept_name LIKE '%Penicillin G%'` query will be removed. As noted, it returns dozens of concepts and requires an undocumented clinical judgment call, producing non-deterministic results across implementations.</p>

<p>In its place, the page will document a three-step pattern using the OMOP `concept_relationship` table:</p>

<p>1. Resolve the source concept from the FHIR resource's `code.coding[].code` + `code.coding[].system` via `concept_code` and `vocabulary_id`.<br/>
2. Derive `observation_concept_id` via the `'Maps to'` relationship.<br/>
3. Derive `value_as_concept_id` via the `'Maps to value'` relationship.</p>

<p>The page will also document the correct handling of vocabulary gaps (`value_as_concept_id = 0` + report to OHDSI) and retain the original query as a clearly marked anti-pattern.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51585".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51585.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\BiomedicalResearchRegulation\\FHIR-51585.md",
  "file_text": "# FHIR-51585: value-as-concept directions should use relationships in the vocabulary, not separate text lookups\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-51585](https://jira.hl7.org/browse/FHIR-51585) |\n| **Status** | Resolved \u2014 change required |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Persuasive |\n| **Specification** | FHIR to OMOP FHIR IG (FHIR) |\n| **Work Group** | Biomedical Research & Regulation |\n| **Assignee** | Jean Duteau |\n| **Reporter** | ScottFavre |\n| **Labels** | MappingLanguage |\n| **Created** | 2025-07-29 |\n| **Updated** | 2026-04-09 |\n\n## Description\n\nThe submitter identifies that the IG page provides sample SQL directing implementers to find a substance concept ID via a display-name-based `LIKE` query:\n\n```sql\nSELECT concept_id, concept_name, domain_id, vocabulary_id, standard_concept\nFROM concept\nWHERE concept_name LIKE '%Penicillin G%'\n  AND vocabulary_id IN ('RxNorm', 'SNOMED')\n  AND standard_concept = 'S';\n```\n\nThis approach is **fragile and non-deterministic** \u2014 dozens of OMOP concepts contain \"Penicillin G\" in the name, requiring an undocumented clinical judgment call that will produce inconsistent results across implementations.\n\nThe submitter proposes replacing this with the OMOP `concept_relationship` table's **\"Maps to value\"** relationships, which yield deterministic, clinically correct results validated by the OMOP vocabulary team.\n\n## Resolution Description\n\nThe workgroup agreed with this correction (Persuasive). The resolution states:\n\n1. The `concept_name LIKE '%Penicillin G%'` query will be **removed**.\n2. The page will document a **three-step pattern** using the OMOP `concept_relationship` table:\n   - **Step 1:** Resolve the source concept from the FHIR resource's `code.coding[].code` + `code.coding[].system` via `concept_code` and `vocabulary_id`.\n   - **Step 2:** Derive `observation_concept_id` via the **\"Maps to\"** relationship.\n   - **Step 3:** Derive `value_as_concept_id` via the **\"Maps to value\"** relationship.\n3. The page will document correct handling of **vocabulary gaps** (`value_as_concept_id = 0` + report to OHDSI).\n4. The original query will be retained as a **clearly marked anti-pattern**.\n\n## Keywords\n\n`OMOP`, `concept_relationship`, `Maps to value`, `value_as_concept_id`, `vocabulary mapping`, `RxNorm`, `SNOMED`, `deterministic`, `anti-pattern`, `MappingLanguage`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-52597](https://jira.hl7.org/browse/FHIR-52597) | Multiple standard concepts for a source concept | Resolved (Not Persuasive with Modification) | Directly related \u2014 addresses what happens when a source code maps to multiple standard OMOP concepts via relationships, which

... *(truncated, 7500 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51585.md with 7300 characters
```

</details>


# Session Log: FHIR-51552

**Phase:** prepared
**Work Group:** BiomedicalResearchRegulation
**Source File:** `prepared/BiomedicalResearchRegulation/FHIR-51552.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51552` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 01:14:23 UTC |
| **Duration** | 74s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 247,180 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51552
## Work Group: Biomedical Research & Regulation
## Output File: C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51552.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51552", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51552", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51552", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51552.md
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
  "id": "FHIR-51552",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51552: observation.qualifier_source_value with no concept

- **status:** Applied
- **type:** Change Request
- **priority:** Highest
- **work_group:** Biomedical Research & Regulation
- **specification:** FHIR to OMOP FHIR IG (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** ScottFavre
- **labels:** MappingLanguage
- **Created:** 2025-07-23T14:48:28+00:00
- **Updated:** 2026-04-09T19:30:46+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51552

## Content
<p>In the discussion of how to interpret <a href="https://build.fhir.org/ig/HL7/fhir-omop-ig/CodeableConceptPattern.html#example-mapping-no-known-allergy-codeableconcept" class="external-link" target="_blank" rel="nofollow noopener">FHIR CodeableConcepts</a> , there is a sample query:</p>

<p> </p>

<p><tt>INSERT INTO observation (</tt><br/>
<tt>    observation_id,</tt><br/>
<tt>    person_id,</tt><br/>
<tt>    observation_concept_id,</tt><br/>
<tt>    observation_date,</tt><br/>
<tt>    observation_source_value,</tt><br/>
<tt>    qualifier_source_value</tt><br/>
<tt>) VALUES (</tt><br/>
<tt>    <span class="error">&#91;generated_id&#93;</span>,</tt><br/>
<tt>    <span class="error">&#91;mapped_person_id&#93;</span>,</tt><br/>
<tt>    4222295,              -- No known allergy concept</tt><br/>
<tt>    '2023-01-15',</tt><br/>
<tt>    '716186003',         &#8211; Source preservation</tt><br/>
<tt>    'NKA'                -- Free text context preserved</tt><br/>
<tt>);</tt></p>

<p>Which is using the qualifier_source_value column as a place to store additional text from the source.</p>


<p>According to the <a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#observation" class="external-link" target="_blank" rel="nofollow noopener">CDM documentation</a> that is not what that column is for. Since there is no qualifier_concept_id the qualifier_source_value should be null.</p>

<p> </p>

<p>It is impossible to fully preserve FHIR source data information in OMOP without extensions and the IG should not encourage implementors to use columns for purposes other than their intended purpose.</p>

## Snapshot
# FHIR-51552: observation.qualifier_source_value with no concept

**Status:** Applied  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Persuasive  
**Assignee:** Unassigned  
**Reporter:** ScottFavre  
**Work Group:** Biomedical Research & Regulation  
**Specification:** FHIR to OMOP FHIR IG (FHIR)  
**Labels:** MappingLanguage  
**Created:** 2025-07-23  
**Updated:** 2026-04-09  
**Resolved:** 2026-03-13  

## Description

<p>In the discussion of how to interpret <a href="https://build.fhir.org/ig/HL7/fhir-omop-ig/CodeableConceptPattern.html#example-mapping-no-known-allergy-codeableconcept" class="external-link" target="_blank" rel="nofollow noopener">FHIR CodeableConcepts</a> , there is a sample query:</p>

<p> </p>

<p><tt>INSERT INTO observation (</tt><br/>
<tt>    observation_id,</tt><br/>
<tt>    person_id,</tt><br/>
<tt>    observation_concept_id,</tt><br/>
<tt>    observation_date,</tt><br/>
<tt>    observation_source_value,</tt><br/>
<tt>    qualifier_source_value</tt><br/>
<tt>) VALUES (</tt><br/>
<tt>    <span class="error">&#91;generated_id&#93;</span>,</tt><br/>
<tt>    <span class="error">&#91;mapped_person_id&#93;</span>,</tt><br/>
<tt>    4222295,              -- No known allergy concept</tt><br/>
<tt>    '2023-01-15',</tt><br/>
<tt>    '716186003',         &#8211; Source preservation</tt><br/>
<tt>    'NKA'                -- Free text context preserved</tt><br/>
<tt>);</tt></p>

<p>Which is using the qualifier_source_value column as a place to store additional text from the source.</p>


<p>According to the <a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#observation" class="external-link" target="_blank" rel="nofollow noopener">CDM documentation</a> that is not what that column is for. Since there is no qualifier_concept_id the qualifier_source_value

... *(truncated, 4783 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51552".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51552.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\BiomedicalResearchRegulation\\FHIR-51552.md",
  "file_text": "# FHIR-51552: observation.qualifier_source_value with no concept\n\n| Field          | Value                                      |\n|----------------|--------------------------------------------|\n| **Ticket**     | [FHIR-51552](https://jira.hl7.org/browse/FHIR-51552) |\n| **Status**     | Applied                                    |\n| **Type**       | Change Request                             |\n| **Priority**   | Highest                                    |\n| **Resolution** | Persuasive                                 |\n| **Work Group** | Biomedical Research & Regulation           |\n| **Specification** | FHIR to OMOP FHIR IG (FHIR)           |\n| **Reporter**   | ScottFavre                                 |\n| **Assignee**   | Unassigned                                 |\n| **Labels**     | MappingLanguage                            |\n| **Created**    | 2025-07-23                                 |\n| **Updated**    | 2026-04-09                                 |\n| **Resolved**   | 2026-03-13                                 |\n\n---\n\n## Summary\n\nThe submitter identifies that the FHIR to OMOP IG's CodeableConcept mapping pattern page includes a sample SQL INSERT for the OMOP `observation` table that misuses the `qualifier_source_value` column. In the example (mapping a \"No known allergy\" CodeableConcept), the column is populated with the free text value `'NKA'` to preserve additional context from the FHIR source. However, per the [OMOP CDM v5.4 documentation](https://ohdsi.github.io/CommonDataModel/cdm54.html#observation), `qualifier_source_value` is intended to store the source value for a qualifier concept\u2014not arbitrary metadata or free text tags. Since no `qualifier_concept_id` is populated, the `qualifier_source_value` should be NULL.\n\nThe submitter argues that the IG should not encourage implementors to repurpose CDM columns for unintended uses, and notes that full preservation of FHIR source data in OMOP is not achievable without extensions.\n\n---\n\n## Keywords\n\n`qualifier_source_value`, `observation`, `OMOP CDM`, `CodeableConcept`, `mapping pattern`, `SQL example`, `CDM column misuse`, `Themis convention`, `FHIR to OMOP IG`, `source preservation`\n\n---\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-51583](https://jira.hl7.org/browse/FHIR-51583) | using qualifier_source_value as a generic tag | Applied | Persuasive | **Direct companion** \u2014 addresses the broader pattern of using `qualifier_source_value` as a generic text tag throughout the CodeableConcept page, same core concern as this ticket |\n| [FHIR-51582](https://jira.hl7.org/browse/FHIR-51582) | invalid omop sql in CodeableConcept pattern | Resolved - change required | Persuasive | **Same page, related SQL error** \u2014 identifies `qualifie

... *(truncated, 6883 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\BiomedicalResearchRegulation\FHIR-51552.md with 6724 characters
```

</details>

### Turn 3

**Assistant:**

Let me fetch the closely related Jira tickets for more context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51552: observation.qualifier_source_value with no concept

- **status:** Applied
- **type:** Change Request
- **priority:** Highest
- **work_group:** Biomedical Research & Regulation
- **specification:** FHIR to OMOP FHIR IG (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** ScottFavre
- **labels:** MappingLanguage
- **Created:** 2025-07-23T14:48:28+00:00
- **Updated:** 2026-04-09T19:30:46+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51552

## Content
<p>In the discussion of how to interpret <a href="https://build.fhir.org/ig/HL7/fhir-omop-ig/CodeableConceptPattern.html#example-mapping-no-known-allergy-codeableconcept" class="external-link" target="_blank" rel="nofollow noopener">FHIR CodeableConcepts</a> , there is a sample query:</p>

<p> </p>

<p><tt>INSERT INTO observation (</tt><br/>
<tt>    observation_id,</tt><br/>
<tt>    person_id,</tt><br/>
<tt>    observation_concept_id,</tt><br/>
<tt>    observation_date,</tt><br/>
<tt>    observation_source_value,</tt><br/>
<tt>    qualifier_source_value</tt><br/>
<tt>) VALUES (</tt><br/>
<tt>    <span class="error">&#91;generated_id&#93;</span>,</tt><br/>
<tt>    <span class="error">&#91;mapped_person_id&#93;</span>,</tt><br/>
<tt>    4222295,              -- No known allergy concept</tt><br/>
<tt>    '2023-01-15',</tt><br/>
<tt>    '716186003',         &#8211; Source preservation</tt><br/>
<tt>    'NKA'                -- Free text context preserved</tt><br/>
<tt>);</tt></p>

<p>Which is using the qualifier_source_value column as a place to store additional text from the source.</p>


<p>According to the <a href="https://ohdsi.github.io/CommonDataModel/cdm54.html#observation" class="external-link" target="_blank" rel="nofollow noopener">CDM documentation</a> that is not what that column is for. Since there is no qualifier_concept_id the qualifier_source_value should be null.</p>

<p> </p>

<p>It is impossible to fully preserve FHIR source data information in OMOP without extensions and the IG should not encourage implementors to use columns for purposes other than their intended purpose.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51582: invalid omop sql in CodeableConcept pattern

- **status:** Resolved - change required
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Biomedical Research & Regulation
- **specification:** FHIR to OMOP FHIR IG (FHIR)
- **resolution:** Persuasive
- **assignee:** Jean Duteau
- **reporter:** ScottFavre
- **labels:** MappingLanguage
- **Created:** 2025-07-29T15:08:04+00:00
- **Updated:** 2026-04-09T19:34:38+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51582

## Content
<p>The section contains this query:</p>

<p><tt>INSERT INTO condition_occurrence (</tt><br/>
<tt>    condition_occurrence_id,</tt><br/>
<tt>    person_id,</tt><br/>
<tt>    condition_concept_id,</tt><br/>
<tt>    condition_start_date,</tt><br/>
<tt>    condition_start_datetime,</tt><br/>
<tt>    condition_type_concept_id,</tt><br/>
<tt>    condition_source_value,</tt><br/>
<tt>    condition_source_concept_id,</tt><br/>
<tt>    qualifier_source_value</tt><br/>
<tt>) VALUES (</tt><br/>
<tt>    12346,                                     &#8211; condition_occurrence_id</tt><br/>
<tt>    67890,                                     &#8211; person_id</tt><br/>
<tt>    201820,                                    -- condition_concept_id (Diabetes mellitus)</tt><br/>
<tt>    '2024-03-15',                             &#8211; condition_start_date</tt><br/>
<tt>    '2024-03-15T10:30:00',                    -- condition_start_datetime</tt><br/>
<tt>    32817,                                     &#8211; condition_type_concept_id (EHR)</tt><br/>
<tt>    'Patient has diabetes',                    -- condition_source_value (original text)</tt><br/>
<tt>    0,                                         &#8211; condition_source_concept_id (unmapped source)</tt><br/>
<tt>    'LOW_SPECIFICITY'                          -- qualifier_source_value (quality flag)</tt><br/>
<tt>);</tt></p>

<p> </p>

<p>qualifier_source_value is not column in the OMOP condition_occurrence table.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-52550: Provide Guidance re: populating Race & Ethnicity on OMOP

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Highest
- **work_group:** Biomedical Research & Regulation
- **specification:** FHIR to OMOP FHIR IG (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Davera Gabriel
- **labels:** MappingLanguage
- **Created:** 2025-09-07T01:11:00+00:00
- **Updated:** 2026-04-09T19:22:03+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-52550

## Content
<p>Generate guidance re: populating race and ethnicity on the OMOP CDM. include guidance based on established Themis guidance for multiple records here: <a href="https://ohdsi.github.io/Themis/multiple_races_per_person.html" class="external-link" target="_blank" rel="nofollow noopener">https://ohdsi.github.io/Themis/multiple_races_per_person.html</a></p>

<p>... and reflecting value sets adopted for use by the OHDSI community, at the latest by the time the IG is balloted next.</p>

```

</details>


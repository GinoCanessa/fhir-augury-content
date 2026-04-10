# Session Log: FHIR-51453

**Phase:** prepared
**Work Group:** Devices
**Source File:** `prepared/Devices/FHIR-51453.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51453` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:55:21 UTC |
| **Duration** | 84s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 219,426 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51453
## Work Group: Devices
## Output File: C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-51453.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51453", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51453", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51453", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-51453.md
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
  "id": "FHIR-51453",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51453: Clarify use of LOINC and SNOMED CT for device observations

- **status:** Triaged
- **type:** Comment
- **priority:** Medium
- **work_group:** Devices
- **specification:** Point of Care Devices (FHIR)
- **resolution:** Considered - No action required
- **assignee:** Unassigned
- **reporter:** THIMOHOELTER
- **labels:** R1NFAN
- **Created:** 2025-07-08T13:07:39+00:00
- **Updated:** 2026-03-30T18:01:24+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51453

## Content
<p>"LOINC and SNOMED nomenclature systems have concept codes for the majority of the most often used device observations, and when they are known for a particular device observation they should certainy made available in device data."</p>

<p>To support this, it is recommended to define a slice on code.coding with a binding to the MDC Metric Nomenclature, which would help clarify the use of SNOMED&amp;LOINC in device observations.</p>

## Comments (2)

### erikmoll — 2026-03-25T10:26:19+00:00
<p>After checking current content, no changes are needed.</p>

### erikmoll — 2026-03-09T15:52:24+00:00
<p>I would suggest to just add a note to the Overview page - <a href="https://build.fhir.org/ig/HL7/uv-pocd/overview.html#value-of-the-mdc-nomenclature-model:" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/uv-pocd/overview.html#value-of-the-mdc-nomenclature-model:</a></p>

<p>LOINC and SNOMED nomenclature systems have concept codes for the majority of the most often used device observations, and when they are known for a particular device observation they should made available in device data.</p>

<p>And do not change the Observation profile that is used only to define the structural mapping from IEEE 11073-10201/10207 to FHIR.</p>


## Snapshot
# FHIR-51453: Clarify use of LOINC and SNOMED CT for device observations

**Status:** Triaged  
**Type:** Comment  
**Priority:** Medium  
**Resolution:** Considered - No action required  
**Assignee:** Unassigned  
**Reporter:** THIMOHOELTER  
**Work Group:** Devices  
**Specification:** Point of Care Devices (FHIR)  
**Labels:** R1NFAN  
**Created:** 2025-07-08  
**Updated:** 2026-03-30  
**Resolved:** 2026-03-25  

## Description

<p>"LOINC and SNOMED nomenclature systems have concept codes for the majority of the most often used device observations, and when they are known for a particular device observation they should certainy made available in device data."</p>

<p>To support this, it is recommended to define a slice on code.coding with a binding to the MDC Metric Nomenclature, which would help clarify the use of SNOMED&amp;LOINC in device observations.</p>

## Resolution Description

<p>The overview page already contains a remark on LOINC and SNOMED codes here:</p>

<p><a href="https://hl7.org/fhir/uv/pocd/2021Sep/overview.html#value-of-the-mdc-nomenclature-model" class="external-link" target="_blank" rel="nofollow noopener">https://hl7.org/fhir/uv/pocd/2021Sep/overview.html#value-of-the-mdc-nomenclature-model</a></p>

<p>The device metric and observation profiles already require MDC codes to be used.</p>

<p>No further changes are needed to resolve this issue.</p>

## Comments

### erikmoll (2026-03-25)

<p>After checking current content, no changes are needed.</p>

### erikmoll (2026-03-09)

<p>I would suggest to just add a note to the Overview page - <a href="https://build.fhir.org/ig/HL7/uv-pocd/overview.html#value-of-the-mdc-nomenclature-model:" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/uv-pocd/overview.html#value-of-the-mdc-nomenclature-model:</a></p>

<p>LOINC and SNOMED nomenclature systems have concept codes for the majority of the most often used device observations, and when they are known for a particular device observation they should made available in device data.</p>

<p>And do not change the Observation profile that is used only to defi

... *(truncated, 4072 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51453".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-51453.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Devices\\FHIR-51453.md",
  "file_text": "# FHIR-51453: Clarify use of LOINC and SNOMED CT for device observations\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-51453](https://jira.hl7.org/browse/FHIR-51453) |\n| **Status** | Triaged |\n| **Type** | Comment |\n| **Priority** | Medium |\n| **Work Group** | Devices |\n| **Specification** | Point of Care Devices (FHIR) |\n| **Resolution** | Considered - No action required |\n| **Reporter** | THIMOHOELTER |\n| **Labels** | R1NFAN |\n| **Created** | 2025-07-08 |\n| **Updated** | 2026-03-30 |\n\n## Description\n\nThe submitter requests clarification on the use of LOINC and SNOMED CT terminology systems for device observations in the PoCD IG. The ticket quotes existing IG text acknowledging that \"LOINC and SNOMED nomenclature systems have concept codes for the majority of the most often used device observations\" and proposes defining a slice on `code.coding` with a binding to the MDC Metric Nomenclature to better clarify how SNOMED and LOINC codes should be used alongside MDC codes in device observations.\n\n## Keywords\n\n- MDC Nomenclature, LOINC, SNOMED CT, IEEE 11073, device observations\n- Point of Care Devices (PoCD), Observation.code, code.coding slice, terminology binding\n\n## Discussion & Comments\n\n### erikmoll (2026-03-09)\nSuggested adding a note to the [PoCD Overview page](https://build.fhir.org/ig/HL7/uv-pocd/overview.html#value-of-the-mdc-nomenclature-model) stating that LOINC and SNOMED codes should be made available when known for a particular device observation. Recommended **not** changing the Observation profile, which is used only to define the structural mapping from IEEE 11073-10201/10207 to FHIR.\n\n### erikmoll (2026-03-25)\nAfter checking current content, confirmed no changes are needed.\n\n### Resolution Description\nThe overview page already contains a remark on LOINC and SNOMED codes at [overview.html#value-of-the-mdc-nomenclature-model](https://hl7.org/fhir/uv/pocd/2021Sep/overview.html#value-of-the-mdc-nomenclature-model). The device metric and observation profiles already require MDC codes. No further changes are needed.\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-15373](https://jira.hl7.org/browse/FHIR-15373) | Clarify requirement (or not) for MDC code - 2018-Jan PoCD #40 | Resolved - No Change | Not Persuasive | Questioned whether MDC codes should be required in PoCD Observation.code; concluded MDC requirement is appropriate for the PoCD scope. |\n| [FHIR-26547](https://jira.hl7.org/browse/FHIR-26547) | Use of MDC Metric Nomenclature in PoCD IG | Resolved - No Change | Considered - Question answered | Asked why the same MDC valueset is used for both DeviceMetric.type and Observation.code, and why there is no valueset expansion. |\n| [FHIR-24877](https://jira.hl7.org/browse/FHIR-248

... *(truncated, 7168 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-51453.md with 7030 characters
```

</details>


# Session Log: FHIR-52998

**Phase:** prepared
**Work Group:** Hl7AustraliaFhir
**Source File:** `prepared/Hl7AustraliaFhir/FHIR-52998.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-52998` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 00:52:15 UTC |
| **Duration** | 110s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 267,356 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-52998
## Work Group: HL7 Australia FHIR
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-52998.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-52998", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-52998", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-52998", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-52998.md
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
  "id": "FHIR-52998",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-52998: Location.physicalType includes VI code :: suggest remove

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Australia FHIR
- **specification:** AU Base (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Stephen Chu
- **Created:** 2025-09-29T00:11:33+00:00
- **Updated:** 2025-10-26T23:48:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-52998

## Content
<p>AU Core Location.type includes a code for virtual location (which is appropriate).<br/>
<a href="https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-v3-ServiceDeliveryLocationRoleType-extended.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-v3-ServiceDeliveryLocationRoleType-extended.html</a></p>

<p>But AU Core Location.physicalType also include a code for "a local that is virtual in nature) <a href="https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-location-physical-type-extended.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-location-physical-type-extended.html</a><br/>
Location.physicalType defintion = "physical form of the location, e.g. building, room, vehicle, road". <br/>
As such, inclusion of "vi" - a location that is virtual in nature is not appropriate.</p>




## Comments (3)

### JIRAUSER25123 — 2025-10-26T23:48:00+00:00
<p>Triaged and accepted by AU FHIR Work Group co-chairs as applicable to AU Base 27/10/2025.</p>

### JIRAUSER26384 — 2025-10-15T22:25:39+00:00
<p>Just confirming that from a PCA perspective, we don't have any issues with the change suggested by Stephen and will ensure our IG is aligned if/when the change is actioned.</p>

### JIRAUSER25123 — 2025-09-30T22:40:06+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=chuscmi" class="user-hover" rel="chuscmi">Stephen Chu</a>, AU Core inherits the terminology from AU Base. This ticket will be moved to AU Base which defines the inclusion of this HL7 International concept and how it is used for a Location resource when implementing FHIR within Australia.</p>

<p>Noting the work on the introduction and use of the virtual concepts into AU Base Location was undertaken by the Agency's PCA project in AU Base release 4.0.0 in 2022.</p>

<p> </p>


## Snapshot
# FHIR-52998: Location.physicalType includes VI code :: suggest remove

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Stephen Chu  
**Work Group:** HL7 Australia FHIR  
**Specification:** AU Base (FHIR)  
**Created:** 2025-09-29  
**Updated:** 2025-10-26  

## Description

<p>AU Core Location.type includes a code for virtual location (which is appropriate).<br/>
<a href="https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-v3-ServiceDeliveryLocationRoleType-extended.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-v3-ServiceDeliveryLocationRoleType-extended.html</a></p>

<p>But AU Core Location.physicalType also include a code for "a local that is virtual in nature) <a href="https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-location-physical-type-extended.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/hl7au/au-fhir-base/ValueSet-au-location-physical-type-extended.html</a><br/>
Location.physicalType defintion = "physical form of the location, e.g. building, room, vehicle, road". <br/>
As such, inclusion of "vi" - a location that is virtual in nature is not appropriate.</p>




## Comments

### JIRAUSER25123 (2025-10-26)

<p>Triaged and accepted by AU FHIR Work Group co-chairs as applicable to AU Base 27/10/2025.</p>

### JIRAUSER26384 (2025-10-15)

<p>Just confirming that from a PCA perspective, we don

... *(truncated, 4708 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-52998" (2 results)

- [jira] FHIR-52998 → [fhir] Location.type
  **Source:** Location.physicalType includes VI code :: suggest remove
  **Type:** mentions
  **Context:** AU Core Location.type includes a code for virtual location (which is appropriate). https...
  **Score:** 0.91
  **Updated:** 2025-10-26T23:48:00+00:00
- [jira] FHIR-52998 → [fhir] Location.physicalType
  **Source:** Location.physicalType includes VI code :: suggest remove
  **Type:** mentions
  **Context:** ...r-base/ValueSet-au-v3-ServiceDeliveryLocationRoleType-extended.html But AU Core Location.physicalType also include a code for "a local that is virtual in nature...
  **Score:** 0.91
  **Updated:** 2025-10-26T23:48:00+00:00
**Warnings:**
- Value 'FHIR-52998' is not a valid Zulip message ID

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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-52998.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7AustraliaFhir\\FHIR-52998.md",
  "file_text": "# FHIR-52998: Location.physicalType includes VI code :: suggest remove\n\n## 1. Summary\n\n| Field | Value |\n|---|---|\n| **Ticket** | [FHIR-52998](https://jira.hl7.org/browse/FHIR-52998) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Specification** | AU Base (FHIR) |\n| **Work Group** | HL7 Australia FHIR |\n| **Reporter** | Stephen Chu |\n| **Assignee** | Unassigned |\n| **Created** | 2025-09-29 |\n| **Updated** | 2025-10-26 |\n\nStephen Chu reports that the AU Base `au-location-physical-type-extended` ValueSet includes a \"vi\" (virtual) code for `Location.physicalType`, but this is semantically inappropriate. The FHIR definition of `physicalType` is \"physical form of the location, e.g. building, room, vehicle, road\" \u2014 a virtual location has no physical form. Meanwhile, `Location.type` already appropriately includes virtual location codes via the `ServiceDeliveryLocationRoleType - AU Extended` ValueSet, making the \"vi\" code in `physicalType` redundant and conceptually misplaced.\n\n## 2. Keywords\n\n`Location.physicalType`, `Location.type`, virtual location, VI code, AU Base, `au-location-physical-type-extended`, `ServiceDeliveryLocationRoleType`, ValueSet, terminology, physical form\n\n## 3. Related Discussions & Cross-References\n\n### Jira Tickets\n\n| Ticket | Title | Status | Relevance |\n|---|---|---|---|\n| [FHIR-36815](https://jira.hl7.org/browse/FHIR-36815) | Add code for \"virtual\" location | Published (Persuasive with Modification) | International request to add \"vi\" to `Location.physicalType` in FHIR core. PA WG acknowledged the need for virtual appointment support but considered broader changes. The existence of this code in AU Base was cited as prior art. |\n| [FHIR-45129](https://jira.hl7.org/browse/FHIR-45129) | Removal of MS on location.physicalType | Resolved - No Change (Not Persuasive) | AU Core ballot request to remove Must Support from `Location.physicalType`. Rejected, but indicates ongoing community questions about the element's maturity and value. |\n| [FHIR-45122](https://jira.hl7.org/browse/FHIR-45122) | Change valueset on Location.type | Resolved - No Change (Not Persuasive) | AU Core ballot request to change the `Location.type` ValueSet. Rejected, but reflects community scrutiny of AU location terminology bindings. |\n| [FHIR-10017](https://jira.hl7.org/browse/FHIR-10017) | Location describing a ward or POC doesn't have a good match in the Location.physicalType ValueSet | \u2014 | Demonstrates broader dissatisfaction with `Location.physicalType` ValueSet coverage in FHIR core. |\n| FHIR-33341 | Consider adding info about video meeting details to Appointment | \u2014 | Referenced in FHIR-36815 comments and Zulip as the broader tracker for virtual appointment support in FHIR R5. |\n\n### Zulip Conversations\n\n| Stream | Topic | Date Range | Summary |\n|-

... *(truncated, 8707 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-52998.md with 8508 characters
```

</details>


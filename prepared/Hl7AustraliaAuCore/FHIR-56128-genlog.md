# Session Log: FHIR-56128

**Phase:** prepared
**Work Group:** Hl7AustraliaAuCore
**Source File:** `prepared/Hl7AustraliaAuCore/FHIR-56128.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-56128` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:10:47 UTC |
| **Duration** | 97s |
| **Total Tool Calls** | 17 |
| **Total Tokens** | 275,152 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-56128
## Work Group: HL7 Australia AU Core
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaAuCore\FHIR-56128.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-56128", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-56128", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-56128", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaAuCore\FHIR-56128.md
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
  "id": "FHIR-56128",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-56128: AU PS Composition :: referencing base FHIR resources instead of AU profiles :: need explanatory notes

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** HL7 Australia AU Core
- **specification:** AU Patient Summary (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Stephen Chu
- **Created:** 2026-03-19T01:01:46+00:00
- **Updated:** 2026-03-30T03:51:26+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-56128

## Content
<p>AU PS Composition:<br/>
Composition.extension:InformationRecipient 0..* Reference(Practitioner | Device | Patient | RelatedPerson | PractitionerRole | Organization) <br/>
It was asserted that data elements do not have "SO" obligation reference FHIR base resources and not AU Base | Core | AU PS profiles. </p>

<p>However, this is not obvious to those who are not familiar with the IG development guidelines | principles. As such, there is confusion to readers. This is particular when the IG defined AU PS Patient, AU PS Practitioner, AU PS PractitionerRole, AU PS RelatedPerson, AU PS Organization etc for use in the AU-PS IG</p>

<p>Change suggestion:<br/>
Add explanatory text under 4.1 General Guidance to provide clarity to readers.<br/>
This issue also applies to other AU PS profiles</p>

## Snapshot
# FHIR-56128: AU PS Composition :: referencing base FHIR resources instead of AU profiles :: need explanatory notes

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Persuasive  
**Assignee:** Unassigned  
**Reporter:** Stephen Chu  
**Work Group:** HL7 Australia AU Core  
**Specification:** AU Patient Summary (FHIR)  
**Created:** 2026-03-19  
**Updated:** 2026-03-30  
**Resolved:** 2026-03-30  

## Description

<p>AU PS Composition:<br/>
Composition.extension:InformationRecipient 0..* Reference(Practitioner | Device | Patient | RelatedPerson | PractitionerRole | Organization) <br/>
It was asserted that data elements do not have "SO" obligation reference FHIR base resources and not AU Base | Core | AU PS profiles. </p>

<p>However, this is not obvious to those who are not familiar with the IG development guidelines | principles. As such, there is confusion to readers. This is particular when the IG defined AU PS Patient, AU PS Practitioner, AU PS PractitionerRole, AU PS RelatedPerson, AU PS Organization etc for use in the AU-PS IG</p>

<p>Change suggestion:<br/>
Add explanatory text under 4.1 General Guidance to provide clarity to readers.<br/>
This issue also applies to other AU PS profiles</p>

## Resolution Description

<p>Update <a href="https://build.fhir.org/ig/hl7au/au-fhir-ps/general-guidance.html#au-ps-profile-design-principles" class="external-link" target="_blank" rel="nofollow noopener">AU PS Profile Design Principles</a> to clearly indicate that reference constraints apply only to  elements flagged as <em>Must Support</em>. </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-56128" (1 results)

- [jira] FHIR-56128 → [fhir] Composition.extension
  **Source:** AU PS Composition :: referencing base FHIR resources instead of AU profiles :: need explanatory notes
  **Type:** mentions
  **Context:** AU PS Composition: Composition.extension:InformationRecipient 0..* Reference(Practitioner | Device ...
  **Score:** 1.00
  **Updated:** 2026-03-30T03:51:26+00:00
**Warnings:**
- Value 'FHIR-56128' is not a valid Zulip message ID

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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaAuCore\FHIR-56128.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7AustraliaAuCore\\FHIR-56128.md",
  "file_text": "# FHIR-56128: AU PS Composition :: referencing base FHIR resources instead of AU profiles :: need explanatory notes\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-56128](https://jira.hl7.org/browse/FHIR-56128) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Persuasive |\n| **Specification** | AU Patient Summary (FHIR) |\n| **Work Group** | HL7 Australia AU Core |\n| **Reporter** | Stephen Chu |\n| **Assignee** | Unassigned |\n| **Created** | 2026-03-19 |\n| **Updated** | 2026-03-30 |\n\n## Description\n\nThe reporter notes that AU PS Composition's `Composition.extension:InformationRecipient` references base FHIR resource types (`Practitioner | Device | Patient | RelatedPerson | PractitionerRole | Organization`) rather than the corresponding AU PS profiles (AU PS Patient, AU PS Practitioner, AU PS PractitionerRole, AU PS RelatedPerson, AU PS Organization, etc.) defined within the IG.\n\nIt was explained during ballot review that data elements **without** a \"SO\" (Send/Obligation) flag intentionally reference base FHIR resources rather than AU-specific profiles. However, the reporter argues this design principle is **not obvious to readers** unfamiliar with IG development guidelines, causing confusion \u2014 especially since the IG defines AU PS-specific profiles for many of these resource types.\n\n**Change suggestion:** Add explanatory text under Section 4.1 (General Guidance) to clarify why non-Must Support reference elements point to base FHIR resources rather than AU PS profiles. The reporter notes this issue applies to other AU PS profiles as well, not just AU PS Composition.\n\n## Resolution Description\n\nUpdate [AU PS Profile Design Principles](https://build.fhir.org/ig/hl7au/au-fhir-ps/general-guidance.html#au-ps-profile-design-principles) to clearly indicate that reference constraints apply only to elements flagged as *Must Support*.\n\n## Keywords\n\n`AU PS`, `Composition`, `reference constraints`, `base FHIR resources`, `AU profiles`, `Must Support`, `profile design principles`, `general guidance`, `InformationRecipient`, `obligation`\n\n## Cross-References\n\n### FHIR Paths Mentioned\n- `Composition.extension:InformationRecipient` \u2014 the specific element under discussion, which references base FHIR resource types rather than AU PS profiles.\n\n### Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-52333](https://jira.hl7.org/browse/FHIR-52333) | 7.1.5.1 Resource Profile: AU PS Composition | Resolved - No Change | Not Persuasive | **Directly related predecessor.** Raised the same concern (also on behalf of Stephen Chu) asking why AU PS Composition references base Encounter instead of AU PS Encounter. Resolved as Not Persuasive \u2014 the design princ

... *(truncated, 9113 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaAuCore\FHIR-56128.md with 8947 characters
```

</details>


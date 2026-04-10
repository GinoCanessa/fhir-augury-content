# Session Log: FHIR-48663

**Phase:** prepared
**Work Group:** Hl7AustraliaFhir
**Source File:** `prepared/Hl7AustraliaFhir/FHIR-48663.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-48663` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:33:22 UTC |
| **Duration** | 89s |
| **Total Tool Calls** | 19 |
| **Total Tokens** | 265,040 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-48663
## Work Group: HL7 Australia FHIR
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-48663.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-48663", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-48663", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-48663", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-48663.md
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
  "id": "FHIR-48663",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-48663: Undefined meaning of Must Support for referenced AU Core profiles

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Australia FHIR
- **specification:** AU eRequesting (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** StephanieOng
- **Created:** 2024-10-17T04:40:02+00:00
- **Updated:** 2024-10-20T06:47:51+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48663

## Content
<p><ins>Issue</ins>:</p>

<p>eRequesting does not inherit AU Core Obligations as the actors are different.</p>

<p>In eRequesting, the meaning of <em>Must Support</em> for referenced AU Core profiles has not yet been defined. Without a clear definition, the obligations for systems to meaningfully support these elements are ambiguous, affecting implementation.</p>

<p><ins>Proposal</ins>:</p>

<p>It is proposed to define in narrative, the default meaning of <em>Must Support</em> for referenced AU Core profiles, for each eRequesting actor.</p>

<p><ins>Background</ins>:</p>

<p>This issue arose from discussions in the AU eRequesting co-chairs/facilitators meeting held on 10 October 2025, in response to <a href="https://jira.hl7.org/browse/FHIR-47008" class="external-link" rel="nofollow">FHIR-47008</a>. It was agreed to raise this issue with the proposed solution of narrative definitions for Release 1 to clarify <em>Must Support</em> obligations.<br/>
It was also discussed that the roadmap for eRequesting IG may include progressing the narrative Obligations to explicit Obligation only profiles. </p>

## Snapshot
# FHIR-48663: Undefined meaning of Must Support for referenced AU Core profiles

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** StephanieOng  
**Work Group:** HL7 Australia FHIR  
**Specification:** AU eRequesting (FHIR)  
**Created:** 2024-10-17  
**Updated:** 2024-10-20  

## Description

<p><ins>Issue</ins>:</p>

<p>eRequesting does not inherit AU Core Obligations as the actors are different.</p>

<p>In eRequesting, the meaning of <em>Must Support</em> for referenced AU Core profiles has not yet been defined. Without a clear definition, the obligations for systems to meaningfully support these elements are ambiguous, affecting implementation.</p>

<p><ins>Proposal</ins>:</p>

<p>It is proposed to define in narrative, the default meaning of <em>Must Support</em> for referenced AU Core profiles, for each eRequesting actor.</p>

<p><ins>Background</ins>:</p>

<p>This issue arose from discussions in the AU eRequesting co-chairs/facilitators meeting held on 10 October 2025, in response to <a href="https://jira.hl7.org/browse/FHIR-47008" class="external-link" rel="nofollow">FHIR-47008</a>. It was agreed to raise this issue with the proposed solution of narrative definitions for Release 1 to clarify <em>Must Support</em> obligations.<br/>
It was also discussed that the roadmap for eRequesting IG may include progressing the narrative Obligations to explicit Obligation only profiles. </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-48663".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-48663.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7AustraliaFhir\\FHIR-48663.md",
  "file_text": "# FHIR-48663: Undefined meaning of Must Support for referenced AU Core profiles\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-48663](https://jira.hl7.org/browse/FHIR-48663) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | AU eRequesting (FHIR) |\n| **Work Group** | HL7 Australia FHIR |\n| **Reporter** | StephanieOng |\n| **Assignee** | Unassigned |\n| **Created** | 2024-10-17 |\n| **Updated** | 2024-10-20 |\n\n## Problem Statement\n\nThe AU eRequesting IG references several AU Core profiles (e.g., AU Core Patient, Practitioner, PractitionerRole, Organization, Encounter), but does **not** inherit AU Core's obligations because the actors in eRequesting are different from those in AU Core. As a result, the meaning of *Must Support* on elements within these referenced AU Core profiles is undefined for eRequesting actors (AU eRequesting Placer, Filler, Server, Patient). This ambiguity creates implementation uncertainty \u2014 developers cannot determine what obligations they have for Must Support elements in AU Core profiles when operating within the eRequesting context.\n\nThe ticket proposes defining, in narrative form, the default meaning of Must Support for referenced AU Core profiles for each eRequesting actor. The long-term roadmap envisions progressing from narrative definitions to explicit obligation-only profiles.\n\nThis issue arose from the AU eRequesting co-chairs/facilitators meeting on 10 October 2025, in direct response to discussions on [FHIR-47008](https://jira.hl7.org/browse/FHIR-47008) (Mandatory Patient Class for diagnostic requests).\n\n## Keywords\n\n`Must Support`, `obligations`, `AU Core`, `AU eRequesting`, `actors`, `conformance`, `narrative obligations`, `obligation profiles`, `Placer`, `Filler`, `Patient`, `Server`\n\n## Related Tickets\n\n| Ticket | Title | Status | Resolution | Relationship |\n|--------|-------|--------|------------|-------------|\n| [FHIR-47008](https://jira.hl7.org/browse/FHIR-47008) | Mandatory Patient Class (Inpatient, Outpatient\u2026) for diagnostic requests | Applied | Persuasive | Trigger \u2014 discussions on this ticket led to FHIR-48663 being raised |\n| [FHIR-51636](https://jira.hl7.org/browse/FHIR-51636) | Proposal for Default Obligations on Must Support Elements and Actor Conformance Requirements | Applied | Persuasive | Directly addresses this gap \u2014 establishes agreed default obligations for eRequesting actors |\n| [FHIR-51637](https://jira.hl7.org/browse/FHIR-51637) | Review of Default Obligations & Conformance Requirements | Applied | Persuasive with Modification | Extends FHIR-51636 with default supported profile conformance and search parameter requirements |\n| [FHIR-51874](https://jira.hl7.org/browse/FHIR-51874) | Create AU eRequesting profiles for AU

... *(truncated, 8410 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7AustraliaFhir\FHIR-48663.md with 8241 characters
```

</details>


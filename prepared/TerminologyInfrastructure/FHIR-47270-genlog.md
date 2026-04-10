# Session Log: FHIR-47270

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-47270.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-47270` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:20:39 UTC |
| **Duration** | 103s |
| **Total Tool Calls** | 18 |
| **Total Tokens** | 318,264 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-47270
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-47270.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-47270", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-47270", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-47270", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-47270.md
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
  "id": "FHIR-47270",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-47270: Duplication of code systems and value sets with THO (using different URLs)

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Extensions Pack (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **labels:** DupResources
- **Created:** 2024-09-10T08:57:09+00:00
- **Updated:** 2026-01-26T20:52:40+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-47270

## Content
<p>There are many extensions in the extension pack use coded values. The binding of the values refers to ValueSets. The codes in these ValueSets refer to codes from CodeSystems.</p>

<p>When accessing the html/json/xml of these ValueSets and CodeSystems it returns html pages and definition that are stored in the extension pack.</p>

<p>The same code systems and value sets are also defined in THO. </p>

<p>The urls used for the ValueSets and CodeSystems in THO are different from the ones used in the extension pack.</p>

<p>E.g. ValueSet  ImplantStatus</p>
<ul>
	<li>Extension pack: <a href="http://hl7.org/fhir/ValueSet/implantStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/implantStatus</a></li>
	<li>THO : <a href="http://terminology.hl7.org/ValueSet/implantStatus" class="external-link" target="_blank" rel="nofollow noopener">http://terminology.hl7.org/ValueSet/implantStatus</a><br/>
Code System ImplantStatus</li>
	<li>Extension pack: <a href="http://hl7.org/fhir/implantStatus" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/implantStatus</a></li>
	<li>THO: <a href="http://terminology.hl7.org/CodeSystem/implantStatus" class="external-link" target="_blank" rel="nofollow noopener">http://terminology.hl7.org/CodeSystem/implantStatus</a></li>
</ul>


<p>Is this correct (I assume not)? FHIR should decide on one location for these ValueSets and CodeSystems and should not duplicate them. If one of these is there due to historical reasons, it should be clearly marked as deprecated. If there is a good reason to duplicate them, then the URLs and content should be aligned.</p>

## Comments (5)

### carmela_couderc — 2026-01-12T21:19:35+00:00
<p>See comments from submitter</p>

### carmela_couderc — 2026-01-06T12:35:06+00:00
<p>Thanks. I've scheduled this for Q1 Wednesday Jan 29 for the joint meeting with FHIR-I. Please note that the ticket may be resolved prior to the WGM as a great deal of progress has already been made on this issue. See notes in linked ticket. </p>

### bvdh — 2026-01-06T08:20:51+00:00
<p>I've removed my "In Person" request. Please go ahead and process this event and I will monitor based on the content in the Jira ticket. I will attend the Jan WGM and can join the session where this will be discussed. Discussing it during the joint session with FHIR-i will make the logistics easier for me.</p>

### carmela_couderc — 2026-01-05T21:16:28+00:00
<p>Hi <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=bvdh" class="user-hover" rel="bvdh">Bas van den Heuvel</a>  will you be at the January 2026 WGM, or can you attend a TI Tracker call? (5 pm Eastern Mondays) OR could you remove the in-person request?</p>

### carmela_couderc — 2024-10-28T18:45:31+00:00
<p>Note: the identified code system and value set appear on the list attached on <a href="https://jira.hl7.org/browse/FHIR-47498" class="external-link" rel="nofollow">https://jira.hl7.org/browse/FHIR-47498</a></p>


## Snapshot
# FHIR-47270: Duplication of code systems and value sets with THO (using different URLs)

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Bas van den Heuvel  
**Work Group:** Terminology Infrastructure  
**Specification:** FHIR Extensions Pack (FHIR)  
**Labels:** DupResources  
**Created:** 2024-09-10  
**

... *(truncated, 7006 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-47270" (2 results)

- [zulip] 469033143 → [jira] FHIR-47270
  **Source:** [fhir/infrastructure-wg] ValueSets and CodeSystems in the extension pack
  **Type:** mentions
  **Context:** ... the proper location for these CodeSystems and ValueSets?<br> Filed in <a href="https://jira.hl7.org/browse/FHIR-47270">FHIR-47270</a>.</p>
  **Score:** 0.17
  **Updated:** 2024-09-10T08:57:53+00:00
- [zulip] 570455506 → [jira] FHIR-47270
  **Source:** [fmg] Extensions Pack
  **Type:** mentions
  **Context:** ... to allow constraining values allowed for 'string' properties</li> <li><a href="http://jira.hl7.org/browse/FHIR-47270">FHIR-47270</a> Duplication of code system...
  **Score:** 0.00
  **Updated:** 2026-01-28T02:08:13+00:00
**Warnings:**
- Value 'FHIR-47270' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (2 total, showing 2)

### [zulip] 469033143 — [fhir/infrastructure-wg] ValueSets and CodeSystems in the extension pack
- **Score:** 0.17
- **Updated:** 2024-09-10T08:57:53+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhir%2Finfrastructure-wg/topic/ValueSets%20and%20CodeSystems%20in%20the%20extension%20pack/near/469033143
- **Snippet:** ...What is the proper location for these CodeSystems and ValueSets? Filed in <b>FHIR-47270</b> .

### [zulip] 570455506 — [fmg] Extensions Pack
- **Score:** 0.00
- **Updated:** 2026-01-28T02:08:13+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fmg/topic/Extensions%20Pack/near/570455506
- **Snippet:** ...extension to allow constraining values allowed for 'string' properties <b>FHIR-47270</b> Duplication of code systems and value sets with THO...


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-47270.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-47270.md",
  "file_text": "# FHIR-47270: Duplication of code systems and value sets with THO (using different URLs)\n\n## Summary\n\n**Status:** Triaged | **Priority:** Highest | **Type:** Change Request\n**Specification:** FHIR Extensions Pack (FHIR) | **Work Group:** Terminology Infrastructure\n**Reporter:** Bas van den Heuvel | **Assignee:** Unassigned\n**Labels:** DupResources\n**Created:** 2024-09-10 | **Updated:** 2026-01-26\n**URL:** https://jira.hl7.org/browse/FHIR-47270\n\nThe reporter identifies that multiple CodeSystems and ValueSets exist in both the FHIR Extensions Pack and HL7 Terminology (THO), with **different canonical URLs**. For example, the `ImplantStatus` ValueSet uses `http://hl7.org/fhir/ValueSet/implantStatus` in the Extensions Pack but `http://terminology.hl7.org/ValueSet/implantStatus` in THO; similarly the CodeSystem uses `http://hl7.org/fhir/implantStatus` vs. `http://terminology.hl7.org/CodeSystem/implantStatus`. The reporter argues FHIR should standardize on a single location and URL, deprecating or retiring the other.\n\n## Keywords\n\n`duplicate`, `CodeSystem`, `ValueSet`, `THO`, `Extensions Pack`, `canonical URL`, `implantStatus`, `terminology`, `DupResources`, `deprecation`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-47498](https://jira.hl7.org/browse/FHIR-47498) | Duplicate Terminology Resources Against THO | Waiting for Input | **Directly related.** Catalogues 14 CS/VS pairs duplicated between Extensions Pack and THO; references a tracking spreadsheet. A subgroup formed at Sep 2025 WGM to resolve; progress tracked by Reuben Daniels and Jessica Bota. |\n| [FHIR-55033](https://jira.hl7.org/browse/FHIR-55033) | Address duplicate terminology artefacts between FHIR core, Extensions Pack, and THO | Triaged | **Directly related.** Filed Jan 2026 by Reuben Daniels with analysis/recommendations in a shared spreadsheet. Appears to be the umbrella resolution tracker. |\n| [FHIR-51491](https://jira.hl7.org/browse/FHIR-51491) | Work group extension binding should use THO VS; Extensions Pack CS/VS deprecated | Submitted | **Related pattern.** Specific case requesting the HL7 Workgroup extension binding switch from Extensions Pack to THO and Extensions Pack artefacts be deprecated. |\n| [FHIR-49183](https://jira.hl7.org/browse/FHIR-49183) | DeviceAlert codesystems should be moved to THO | Resolved \u2013 Not Persuasive | **Related pattern.** Request to move DeviceAlert terminology from FHIR core to THO for use in extensions. Resolved as not persuasive (Devices WG). |\n| [FHIR-44402](https://jira.hl7.org/browse/FHIR-44402) | Code Systems and Valuesets should be anchored in THO | Resolved \u2013 Not Persuasive | **Related pattern.** Broader request that CS/VS URLs should be anchored in THO per TSC-approved terminology guidance. |\n| [FHIR-53036](https://jira.hl7.org

... *(truncated, 8905 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-47270.md with 8738 characters
```

</details>


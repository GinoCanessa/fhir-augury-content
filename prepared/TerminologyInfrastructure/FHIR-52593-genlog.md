# Session Log: FHIR-52593

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-52593.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-52593` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:05:42 UTC |
| **Duration** | 112s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 274,039 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-52593
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52593.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-52593", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-52593", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-52593", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52593.md
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
  "id": "FHIR-52593",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-52593: Consider adding "Deprecated" as a "Artifact Status"

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** Canonical Resource Management Infrastructure (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Gay Dolin
- **Created:** 2025-09-07T20:23:29+00:00
- **Updated:** 2026-04-07T18:02:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-52593

## Content
<p>The artifact Status list (<a href="https://hl7.org/fhir/uv/crmi/2025Sep/artifact-lifecycle.html#artifact-status" class="external-link" target="_blank" rel="nofollow noopener">https://hl7.org/fhir/uv/crmi/2025Sep/artifact-lifecycle.html#artifact-status</a>) appears to be missing the status <b>"Deprecated."</b></p>

<p>VSAC supports both <b>Retired</b> and <b>Deprecated</b>, and "Deprecated" has also been used historically in C-CDA. To align with VSAC and common IT usage, please consider adding <b>"Deprecated"</b> as a distinct status and clarifying its meaning in contrast to <b>"Retired." Of note is that you also use "Deprecated" as a status in the CRMI IG artifacts.</b></p>

<p><b>Proposed definition of Deprecated:</b></p>
<ul>
	<li><b>Definition:</b> Still available/valid, but discouraged for use.</li>
</ul>


<ul>
	<li><b>Purpose:</b> Signals to implementers that there is a better, newer, or safer alternative, and they should migrate away from the deprecated item.</li>
</ul>


<ul>
	<li><b>Status:</b> The feature, function, or standard continues to exist and usually still works for backward compatibility.</li>
</ul>


## Comments (5)

### bryn.rhodes — 2025-10-22T15:56:27+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=GDolin" class="user-hover" rel="GDolin">Gay Dolin</a>, the definition for deprecated makes sense, but then what is the distinction between deprecated and retired?</p>

### bryn.rhodes — 2025-09-24T15:24:37+00:00
<p>Consider the following extensions:</p>

<p><a href="https://hl7.org/fhir/extensions/ValueSet-template-status-code.html" class="external-link" target="_blank" rel="nofollow noopener">https://hl7.org/fhir/extensions/ValueSet-template-status-code.html</a></p>

<p><a href="https://hl7.org/fhir/extensions/ValueSet-standards-status.html" class="external-link" target="_blank" rel="nofollow noopener">https://hl7.org/fhir/extensions/ValueSet-standards-status.html</a></p>

<p>maybe lifecycleStatus?</p>

### bryn.rhodes — 2025-09-24T15:19:01+00:00
<p>Perhaps a "releaseStatus", one of "pre-release", "release", "deprecated"</p>

### bryn.rhodes — 2025-09-24T15:15:43+00:00
<p>We do use the core specification's "standards-status" extension to indicate when features of CRMI are "deprecated" (<a href="https://github.com/search?q=repo%3AHL7%2Fcrmi-ig%20deprecated&amp;type=code" class="external-link" target="_blank" rel="nofollow noopener">https://github.com/search?q=repo%3AHL7%2Fcrmi-ig%20deprecated&amp;type=code</a>) so perhaps an extension with a separate status for deprecation is the right approach?</p>

### bryn.rhodes — 2025-09-24T15:13:36+00:00
<p>The challenge here is that we are just using the status element from the canonical resources, so to add this status we would have to add it to all of the canonical resources in FHIR (i.e. it would be an R6 base specification change). And looking at the publication status codes, it seems like "retired" (should not be used) includes the concept of "deprecated"? Maybe this could be indicated with a separate flag?</p>


## Snapshot
# FHIR-52593: Consider adding "Deprecated" as a "Artifact Status"

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Persuasive with Modification  
**Assignee:** Unassigned  
**Reporter:** Gay Dolin  
**Work Group:** Terminology Infrastructure  
**Specification:** Canonical Resource Management Infrastructure (FHIR)  
**Created:** 2025-09-0

... *(truncated, 7552 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-52593".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52593.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-52593.md",
  "file_text": "# FHIR-52593: Consider adding \"Deprecated\" as an \"Artifact Status\"\n\n## Quick Reference\n\n| Field | Value |\n|---|---|\n| **Ticket** | [FHIR-52593](https://jira.hl7.org/browse/FHIR-52593) |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Status** | Triaged |\n| **Resolution** | Persuasive with Modification |\n| **Work Group** | Terminology Infrastructure |\n| **Specification** | Canonical Resource Management Infrastructure (FHIR) |\n| **Reporter** | Gay Dolin |\n| **Assignee** | Unassigned |\n| **Created** | 2025-09-07 |\n| **Updated** | 2026-04-07 |\n\n---\n\n## Summary\n\nThe submitter requests that **\"Deprecated\"** be added as a distinct artifact status in the CRMI artifact lifecycle, separate from **\"Retired\"**. The rationale is that VSAC supports both Retired and Deprecated statuses, \"Deprecated\" has been used historically in C-CDA, and CRMI itself already uses \"Deprecated\" as a standards-status on some of its own IG artifacts.\n\n**Proposed definition of Deprecated:**\n- **Definition:** Still available/valid, but discouraged for use.\n- **Purpose:** Signals to implementers that a better, newer, or safer alternative exists, and they should migrate away.\n- **Status:** The feature/standard continues to exist and usually still works for backward compatibility.\n\n**Resolution description (from ticket):** The base FHIR lifecycle statuses for artifacts cannot be modified, but the need can be met using the `valueset-workflowStatusDescription` extension. This extension will be added to the ShareableValueSet pattern and its use for describing \"deprecated\" and \"retired\" status will be documented.\n\n---\n\n## Keywords\n\n`deprecated`, `artifact status`, `retired`, `PublicationStatus`, `CRMI`, `VSAC`, `valueset-workflowStatusDescription`, `ShareableValueSet`, `lifecycle`, `standards-status`\n\n---\n\n## Ticket Comments Summary\n\n**Bryn Rhodes** (5 comments, Sep\u2013Oct 2025) explored several angles:\n1. **Base FHIR constraint**: Adding \"Deprecated\" to PublicationStatus would require changes to all canonical resources in FHIR (an R6 base specification change). The current \"retired\" status (\"should not be used\") arguably subsumes \"deprecated.\"\n2. **Extension approach**: CRMI already uses the `standards-status` extension to mark features as deprecated. A separate extension or flag for deprecation may be the right approach.\n3. **Alternative proposals**: Suggested a \"releaseStatus\" extension (values: pre-release, release, deprecated), or a \"lifecycleStatus\" extension. Referenced `template-status-code` and `standards-status` value sets from the FHIR extensions pack.\n4. **Clarification requested**: Asked the submitter to clarify the precise distinction between \"deprecated\" and \"retired.\"\n\n---\n\n## Related Jira Tickets\n\n### FHIR-31028 \u2014 Need to add Deprecated to PublicationStatus 

... *(truncated, 10298 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52593.md with 9987 characters
```

</details>


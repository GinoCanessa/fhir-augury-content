# Session Log: FHIR-49671

**Phase:** prepared
**Work Group:** TerminologyServicesManagementGroup
**Source File:** `prepared/TerminologyServicesManagementGroup/FHIR-49671.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-49671` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:43:58 UTC |
| **Duration** | 129s |
| **Total Tool Calls** | 18 |
| **Total Tokens** | 455,030 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-49671
## Work Group: Terminology Services Management Group
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyServicesManagementGroup\FHIR-49671.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-49671", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-49671", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-49671", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyServicesManagementGroup\FHIR-49671.md
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
  "id": "FHIR-49671",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-49671: Handling private codes in FHIR

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Services Management Group
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **Created:** 2025-01-27T15:38:20+00:00
- **Updated:** 2026-01-19T09:21:55+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-49671

## Content
<p>Several (existing, older, or communication related) codes systems have the concept of a <em>private code</em>. A <em>private code</em> is a code for which the code system indicates that it does not define the meaning and the field can be used by implementers as they wish.</p>

<p>An example of such code includes the <a href="https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_7.8.html" class="external-link" target="_blank" rel="nofollow noopener">DICOM 7.8 Private Data Elements</a>.</p>

<p>They typically appear in codes that used in messages where the code system is implicit.</p>

<p> </p>

<p>The FHIR specification should provide guidance on:</p>
<ul>
	<li>whether private codes can be expressed in FHIR and</li>
	<li>if so, how.</li>
</ul>


<p>There has been a discussion on this topic in <a href="https://chat.fhir.org/#narrow/channel/179252-IG-creation/topic/supporting.20private.20codes.20in.20code.20system" class="external-link" target="_blank" rel="nofollow noopener">#IG creation &gt; supporting private codes in code system - FHIR Community - Zulip.</a></p>

<p>Options mentioned in discussion are:</p>
<ul>
	<li>Do not represent -&gt; when topic is expressed in FHIR an appropriate system needs to be provided that scopes the private code.</li>
	<li>Include the code without code system when meaning is not known.</li>
	<li>Include the code as a normal code in the CodeSystem (might require an extension on code system to link a code to a range of code).</li>
</ul>


<p>I propose that FHIR states that:</p>
<ul>
	<li>FHIR resources can use private codes from code systems that define them</li>
	<li>Implementations SHOULD:
	<ul>
		<li>For CodeableConcepts:
		<ul>
			<li>add a more descriptive code whenever a private code is used .</li>
			<li>include the original private code.</li>
		</ul>
		</li>
		<li>For Codings
		<ul>
			<li>add a more descriptive code whenever a private code is used .</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>


<p>Additionally, an extension should be defined on CodeSystem allowing expression that a range of codes has the same definition (preventing adding thousands of codes with the same definition).</p>

## Comments (1)

### esilver — 2025-01-28T17:45:08+00:00
<p>Guidance on use of <tt>system</tt> values is needed in this context (can "private" codes be part of a standard code system? does each "set" of private codes need a corresponding code system? ...) I think I know answers for these, but they should be clearly documented.</p>


## Snapshot
# FHIR-49671: Handling private codes in FHIR

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Bas van den Heuvel  
**Work Group:** Terminology Services Management Group  
**Specification:** FHIR Core (FHIR)  
**Created:** 2025-01-27  
**Updated:** 2026-01-19  

## Description

<p>Several (existing, older, or communication related) codes systems have the concept of a <em>private code</em>. A <em>private code</em> is a code for which the code system indicates that it does not define the meaning and the field can be used by implementers as they wish.</p>

<p>An example of such code includes the <a href="https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_7.8.html" class="external-link" target="_blank" rel="nofollow noopener">DICOM 7.8 Private Data Elements</a>.</p>

<p>They typically appear in codes that used in messages where the code system is implicit.</p>

<p> </p>

<p>The FHIR

... *(truncated, 5874 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-49671".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyServicesManagementGroup\FHIR-49671.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyServicesManagementGroup\\FHIR-49671.md",
  "file_text": "# FHIR-49671: Handling private codes in FHIR\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-49671](https://jira.hl7.org/browse/FHIR-49671) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | FHIR Core (FHIR) |\n| **Work Group** | Terminology Services Management Group |\n| **Reporter** | Bas van den Heuvel |\n| **Assignee** | Unassigned |\n| **Created** | 2025-01-27 |\n| **Updated** | 2026-01-19 |\n\n## Description Summary\n\nSeveral code systems (especially older or communication-related ones) define ranges of \"private codes\" \u2014 codes whose meaning is not fixed by the code system authority, but left for implementers to assign locally. A key example is [DICOM 7.8 Private Data Elements](https://dicom.nema.org/dicom/2013/output/chtml/part05/sect_7.8.html). IEEE 11073 MDC is another prominent case where the upper 4K of each 64K partition is reserved for private/vendor codes.\n\nThe ticket requests that the FHIR specification provide guidance on:\n1. Whether private codes can be expressed in FHIR\n2. If so, how they should be represented\n\nThe reporter proposes:\n- FHIR resources **can** use private codes from code systems that define them\n- For **CodeableConcepts**: implementations SHOULD include both the original private code and a more descriptive code\n- For **Codings**: implementations SHOULD add a more descriptive code alongside the private code\n- An **extension on CodeSystem** should be defined to express that a range of codes shares the same definition (avoiding adding thousands of codes individually)\n\n## Keywords\n\n`private codes`, `code system`, `CodeSystem extension`, `regex`, `CodeableConcept`, `Coding`, `DICOM`, `IEEE 11073 MDC`, `private data elements`, `validator`, `terminology`, `supplements`\n\n## Comments Summary\n\n| Author | Date | Key Points |\n|--------|------|------------|\n| Elliot Silver | 2025-01-28 | Guidance on `system` values is needed: Can private codes be part of a standard code system? Does each set of private codes need its own code system? Should be clearly documented. |\n\n## Related Jira Tickets\n\n### Closely Related\n\n| Key | Title | Status | Relationship |\n|-----|-------|--------|-------------- |\n| [FHIR-50851](https://jira.hl7.org/browse/FHIR-50851) | Define an extension for CodeSystem to allow defining private code system spaces | Resolved \u2014 Persuasive with Modification | **Directly addresses** the extension proposal in this ticket. Defines a regex-based extension on CodeSystem to mark private code spaces so validators don't flag them as invalid. Filed by Grahame Grieve. WG: Terminology Infrastructure. |\n| [FHIR-50922](https://jira.hl7.org/browse/FHIR-50922) | CodeSystem supplements should be allowed to reference private codes | Applied \u2014 Per

... *(truncated, 11466 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyServicesManagementGroup\FHIR-49671.md with 11265 characters
```

</details>


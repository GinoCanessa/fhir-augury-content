# Session Log: FHIR-10322

**Phase:** prepared
**Work Group:** StructuredDocuments
**Source File:** `prepared/StructuredDocuments/FHIR-10322.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-10322` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 22:00:01 UTC |
| **Duration** | 103s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 218,786 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-10322
## Work Group: Structured Documents
## Output File: C:\ai\git\fhir-augury-content\prepared\StructuredDocuments\FHIR-10322.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-10322", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-10322", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-10322", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\StructuredDocuments\FHIR-10322.md
````

---

## Agent Execution Log

### Turn 1

**Assistant:**

Let me fetch the most closely related tickets for additional context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-10322: Composition.type value set does not exist - "http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22"

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Structured Documents
- **specification:** US C-CDA on FHIR (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Corey Spears
- **Created:** 2016-07-14T04:44:44+00:00
- **Updated:** 2024-03-12T21:09:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10322

## Content
<p>"<a href="http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22</a>" is not a valid valueset. It needs to be added.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-10323: The Composition.type is not binded to a valueset

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Structured Documents
- **specification:** US C-CDA on FHIR (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Corey Spears
- **Created:** 2016-07-14T04:46:11+00:00
- **Updated:** 2024-03-12T21:08:53+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10323

## Content
<p>Need to point to "<a href="http://hl7.org/fhir/ValueSet/2.16.840.1.113883.11.20.9.31" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/2.16.840.1.113883.11.20.9.31</a>" and the valueset needs to be added to the build.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-10338: Composition.type needs to have a valueset binding

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Structured Documents
- **specification:** US C-CDA on FHIR (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Corey Spears
- **Created:** 2016-07-14T05:16:01+00:00
- **Updated:** 2024-03-12T21:09:02+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10338

## Content
<p>Composition.type needs to be changed to reflect that identified for transfer summary in CCDA (And the valueset added to the build)<br class="atl-forced-newline" />Should look something like the folloing after the value set is added<br class="atl-forced-newline" />      &lt;binding&gt;<br class="atl-forced-newline" />          &lt;strength value="required" /&gt;<br class="atl-forced-newline" />          &lt;valueSetReference&gt;<br class="atl-forced-newline" />              &lt;reference value="<a href="http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.2.4" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.2.4</a>" /&gt;<br class="atl-forced-newline" />              &lt;display value="TransferDocumentType" /&gt;<br class="atl-forced-newline" />          &lt;/valueSetReference&gt;<br class="atl-forced-newline" />      &lt;/binding&gt;</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-28078: DocumentReference.type valueset should be same as Composition.type

- **status:** Applied
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** John Moehrke
- **Created:** 2020-07-16T14:54:40+00:00
- **Updated:** 2025-09-09T18:27:39+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-28078

## Content
<p>Composition.type now is recommending all LOINC codes that are of DOC type. This is the appropriate valueSet for DocumentReference too. Where the current DocumentReference.type is the old HITSP C80 defined document types. </p>

<p>Recommend change DocumentReference.type vocabulary binding from valueset-c80-doc-typecodes to <a href="http://build.fhir.org/valueset-doc-typecodes.html" class="external-link" target="_blank" rel="nofollow noopener">valueset-doc-typecodes</a></p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-55633: Fix the terminology binding for type and category to align with US Core and FHIR Clinical Document

- **status:** Applied
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** Patient Empowerment
- **specification:** US PACIO Advance Directive Interoperability (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Lisa R. Nelson
- **Created:** 2026-02-06T21:27:50+00:00
- **Updated:** 2026-02-06T22:11:14+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-55633

## Content
<p>We need to align the value set binding for the type and category elements of each of the indicated profiles. </p>

<p>Also there is an extension on type that needs to be removed because it does not align with any other profiles on DocumentReference or Composition. </p>

<p> </p>

```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-10322",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-10322: Composition.type value set does not exist - "http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22"

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Structured Documents
- **specification:** US C-CDA on FHIR (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Corey Spears
- **Created:** 2016-07-14T04:44:44+00:00
- **Updated:** 2024-03-12T21:09:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-10322

## Content
<p>"<a href="http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22</a>" is not a valid valueset. It needs to be added.</p>

## Comments (2)

### lynn_laakso — 2024-03-12T21:09:00+00:00
<p>re-open post STU1.2 publication</p>

### lynn_laakso — 2024-03-12T21:00:29+00:00
<p>original related URL: <a href="http://build.fhir.org/ccda/ccda-history-and-physical-composition.html" class="external-link" target="_blank" rel="nofollow noopener">http://build.fhir.org/ccda/ccda-history-and-physical-composition.html</a></p>


## Snapshot
# FHIR-10322: Composition.type value set does not exist - "http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22"

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Corey Spears  
**Work Group:** Structured Documents  
**Specification:** US C-CDA on FHIR (FHIR)  
**Created:** 2016-07-14  
**Updated:** 2024-03-12  

## Description

<p>"<a href="http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22</a>" is not a valid valueset. It needs to be added.</p>

## Comments

### lynn_laakso (2024-03-12)

<p>re-open post STU1.2 publication</p>

### lynn_laakso (2024-03-12)

<p>original related URL: <a href="http://build.fhir.org/ccda/ccda-history-and-physical-composition.html" class="external-link" target="_blank" rel="nofollow noopener">http://build.fhir.org/ccda/ccda-history-and-physical-composition.html</a></p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-10322" (2 results)

- [jira] FHIR-10322 → [fhir] Composition.type
  **Source:** Composition.type value set does not exist - "http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22"
  **Type:** mentions
  **Context:** ...t/2.16.840.1.113883.1.11.20.22 " is not a valid valueset. It needs to be added. Composition.type value set does not exist - "http://hl7.org/fhir/ValueSet/2.16.8...
  **Score:** 0.32
  **Updated:** 2024-03-12T21:09:00+00:00
- [zulip] 153838137 → [jira] FHIR-10322
  **Source:** [committers] tracker-item
  **Type:** mentions
  **Context:** GF#10322 : Composition.type value set does not exist - "http://hl7.org/fhir/Valu...
  **Score:** 0.01
  **Updated:** 2016-07-14T04:41:08+00:00
**Warnings:**
- Value 'FHIR-10322' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\StructuredDocuments\FHIR-10322.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\StructuredDocuments\\FHIR-10322.md",
  "file_text": "# FHIR-10322: Composition.type value set does not exist \u2014 \"http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22\"\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-10322](https://jira.hl7.org/browse/FHIR-10322) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | US C-CDA on FHIR (FHIR) |\n| **Work Group** | Structured Documents |\n| **Reporter** | Corey Spears |\n| **Assignee** | Unassigned |\n| **Created** | 2016-07-14 |\n| **Updated** | 2024-03-12 |\n\n## Description\n\nThe reporter identifies that the ValueSet URL `http://hl7.org/fhir/ValueSet/2.16.840.1.113883.1.11.20.22` referenced by `Composition.type` in the C-CDA on FHIR Implementation Guide does not resolve to a valid ValueSet. The OID `2.16.840.1.113883.1.11.20.22` corresponds to a CDA-era value set identifier (HPDocumentType) that was used as a FHIR ValueSet canonical URL, but the ValueSet was never created or published at that URL.\n\nThe original related page was the [C-CDA History and Physical Composition](http://build.fhir.org/ccda/ccda-history-and-physical-composition.html) profile page.\n\nPer comments from lynn_laakso (2024-03-12), the ticket was re-opened post STU1.2 publication, indicating the issue persists.\n\n## Keywords\n\n`Composition.type`, `ValueSet`, `C-CDA on FHIR`, `History and Physical`, `OID`, `terminology binding`, `2.16.840.1.113883.1.11.20.22`, `HPDocumentType`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relationship |\n|--------|-------|--------|-------------|\n| [FHIR-10321](https://jira.hl7.org/browse/FHIR-10321) | Composition.type value set does not exist \u2014 \u202620.2.3 | Triaged | Same reporter, same day, same issue for different OID-based ValueSet (2.16.840.1.113883.1.11.20.2.3) |\n| [FHIR-10323](https://jira.hl7.org/browse/FHIR-10323) | The Composition.type is not binded to a valueset | Triaged | Same reporter, same day; requests binding to OID 2.16.840.1.113883.11.20.9.31 |\n| [FHIR-10338](https://jira.hl7.org/browse/FHIR-10338) | Composition.type needs to have a valueset binding | Triaged | Same reporter, same day; requests transfer summary ValueSet binding (OID 2.16.840.1.113883.1.11.20.2.4) |\n| [FHIR-10339](https://jira.hl7.org/browse/FHIR-10339) | Composition.type needs to have a valueset binding | Duplicate | Duplicate of FHIR-10338 |\n| [FHIR-28078](https://jira.hl7.org/browse/FHIR-28078) | DocumentReference.type valueset should be same as Composition.type | Applied (Persuasive) | Resolved the broader question: Composition.type now recommends LOINC DOC-type codes |\n| [FHIR-55633](https://jira.hl7.org/browse/FHIR-55633) | Fix the terminology binding for type and category to align with US Core and FHIR Clinical Document | Applied (Persuasive) | Related alignment of type/category bindings in downst

... *(truncated, 7415 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\StructuredDocuments\FHIR-10322.md with 7265 characters
```

</details>


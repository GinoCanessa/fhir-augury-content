# Session Log: FHIR-51210

**Phase:** prepared
**Work Group:** Hl7Europe
**Source File:** `prepared/Hl7Europe/FHIR-51210.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51210` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:44:13 UTC |
| **Duration** | 95s |
| **Total Tool Calls** | 18 |
| **Total Tokens** | 296,273 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51210
## Work Group: HL7 Europe
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51210.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51210", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51210", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51210", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51210.md
````

---

## Agent Execution Log

### Turn 1

**Assistant:**

Let me get details on the closely related tickets.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51210: Review header model map

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-24T08:10:49+00:00
- **Updated:** 2026-03-02T15:31:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51210

## Content
<p><b>Group 1 Mapping from Imaging report header model to Imaging Composition</b></p>

<p>documentMetadata should not be unmappped</p>

<p>documentMetadata.documentId explain in the comment when this mapping applies</p>

<p>documentMetadata.documentType, not convinced it should be mapped to category, documentType in the other guides is mapped to the composition.type </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51215: Review header map group 2

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-24T08:19:12+00:00
- **Updated:** 2026-03-02T15:28:58+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51215

## Content
<p><b><ins>Group 2</ins></b> <ins>Mapping from</ins> Imaging report header model <ins>to</ins> Imaging Diagnostic Report</p>

<p>I’d expect to see substalliaty the large amount of information of group1  mapped also in group 2</p>

<p>Similar consideration for type and formatCode for group 1 applies also here</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-48528: Remove mapping of nonXML body

- **status:** Applied
- **type:** Change Request
- **priority:** Medium
- **work_group:** Structured Documents
- **specification:** FHIR Clinical Documents (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Benjamin Flessner
- **Created:** 2024-10-03T16:37:53+00:00
- **Updated:** 2025-08-11T22:19:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48528

## Content
<blockquote><p>This IG maps CDA's NonXMLBody into Composition.section. To communicate, say, a PDF document using this approach, one would populate the Composition, where that Composition has a single Composition.section with a Composition.section.entry that references the PDF (e.g. as a FHIR <a href="https://hl7.org/fhir/R4/binary.html" class="external-link" target="_blank" rel="nofollow noopener">Binary</a> or FHIR <a href="https://hl7.org/fhir/R4/documentreference.html" class="external-link" target="_blank" rel="nofollow noopener">DocumentReference</a>). A use case for communicating a PDF in this way, as opposed to simply communicating a DocumentReference, is where a clinical document management system needs to have uniform document metadata for clinical documents in a range of formats.</p></blockquote>
<p>I had thought during original design that this was only going to be proposed as a possible alternative to using DocumentReference alone, but this reads like a requirement which I strongly oppose.</p>

<p>Composition composes resources (i.e. structures), so corresponds to a structured document. CDA shoehorned unstructured content into the nonXMLBody element to exchange these documents with the same metadata. But FHIR can (and does for many other types of documents, including "clinical" ones) represent the same metadata in DocumentReference.</p>

<p>If there are some pieces of the CDA header metadata missing in DocumentReference, perhaps the IG should create a profile on that resource as well (or expand the context of extensions to include DocumentReference along with Composition).</p>

<p>If this absolutely is going to be the recommended approach, then there needs to be a separate profile for unstructured documents that limits section to 1..1 and enforces the requirements of entry / code / title / text (should probably be 0..0?). But again, this is not how CDA is modeled (Unstructured documents do not use a single section with an entry referencing base64 content or an external URL), so it doesn't seem like the right approach for this IG.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-50354: A comment element should be added to ConceptMap to explain noMap mapping rules

- **status:** Applied
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Reuben Daniels
- **Created:** 2025-04-23T07:29:52+00:00
- **Updated:** 2025-11-04T00:19:27+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-50354

## Content
<p>When a ConceptMap mapping rule assigns a value of 'true' to noMap, there does not exist an element to provide a comment to explain why  no mapping to a target concept exists for a particular source concept.  The comment element under target cannot be used due to constraint cmd-4 which forbids the presence of the target element when noMap has a value of 'true'.</p>

<p>The above is in contrast to ConceptMap in R4 which represented noMap using the 'unmatched' equivalence value in the corresponding target element which then allowed use of target.comment.</p>

<p>The following disposition is proposed:</p>

<p>1. Add a ConceptMap.group.element.comment element to ConceptMap defined as follows:</p>
<div class='table-wrap'>
<table class='confluenceTable'><tbody>
<tr>
<td class='confluenceTd'>Definition</td>
<td class='confluenceTd'>A description of the source of the mapping rule which may include  why  no mapping to a target concept exists for a particular source concept if noMap has a value of 'true'.</td>
</tr>
<tr>
<td class='confluenceTd'>Short Display</td>
<td class='confluenceTd'>A description of the source of the mapping rule</td>
</tr>
<tr>
<td class='confluenceTd'>Cardinality</td>
<td class='confluenceTd'>0..1</td>
</tr>
<tr>
<td class='confluenceTd'>Type</td>
<td class='confluenceTd'>string</td>
</tr>
<tr>
<td class='confluenceTd'>Summary</td>
<td class='confluenceTd'>false</td>
</tr>
</tbody></table>
</div>


<p>2. Add the following constraint:</p>

<p>ID: cmd-12 or next available</p>

<p>Level: Rule</p>

<p>Location:  ConceptMap.group.element</p>

<p>Description: If ConceptMap.group.element.noMap is present and has a value of 'true', there SHALL be some comments, unless the status is 'draft'.</p>

<p>Expression: comment.exists() or (%resource.status = 'draft') or (noMap != true)</p>

```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-51210",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51210: Review header model map

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-24T08:10:49+00:00
- **Updated:** 2026-03-02T15:31:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51210

## Content
<p><b>Group 1 Mapping from Imaging report header model to Imaging Composition</b></p>

<p>documentMetadata should not be unmappped</p>

<p>documentMetadata.documentId explain in the comment when this mapping applies</p>

<p>documentMetadata.documentType, not convinced it should be mapped to category, documentType in the other guides is mapped to the composition.type </p>

## Comments (5)

### JIRAUSER28670 — 2025-07-21T12:33:12+00:00
<p>documentId has gone away as well.</p>

### JIRAUSER28670 — 2025-07-21T12:30:25+00:00
<p>It seems that there is no more documentMetadata field in the new refactored logical model <a href="https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSImagingReport.html" class="external-link" target="_blank" rel="nofollow noopener">Imaging report model - EHDS Logical Information Models v0.1.0</a> </p>

<p>Can we consider this change stable <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=rlindstrom" class="user-hover" rel="rlindstrom">Rutt Lindstrom</a> ?</p>

### giorgio — 2025-07-14T12:21:05+00:00
<p>documentMetadata is generically represented by the Composition (realtedTo)</p>

### giorgio — 2025-07-14T12:20:08+00:00
<p>a documentID can represent the identifer of the document (indipendently by its version) or the identifier of an instance of a document. These are mapped into two different elements: the first in the Composiiton the second in the Bundle</p>

### JIRAUSER28670 — 2025-07-09T11:50:29+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=giorgio" class="user-hover" rel="giorgio">Giorgio Cangioli</a> </p>
<ul>
	<li><a href="https://build.fhir.org/ig/hl7-eu/imaging/branches/0.1.0-ballot/StructureDefinition-EHDSImagingReportHeader-definitions.html#EHDSImagingReportHeader.documentMetadata" class="external-link" target="_blank" rel="nofollow noopener">documentMetadata</a> is the backbone element, there is no such element to map it to in Composition. The children elements are the ones that are being mapped to the corresponding targets in the Composition elements.</li>
	<li>Can you please clarify what do you mean by "explain in the comment when this mapping applies". Is this a comment about the "is related to" attribute?</li>
</ul>


<p> </p>


## Snapshot
# FHIR-51210: Review header model map

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Persuasive with Modification  
**Assignee:** Unassigned  
**Reporter:** Giorgio Cangioli  
**Work Group:** HL7 Europe  
**Specification:** EU Imaging Study Report (R5) (FHIR)  
**Labels:** block-vote-5  
**Created:** 2025-06-24  
**Updated:** 2026-03-02  
**Resolved:** 2026-03-02  

## Description

<p><b>Group 1 Mapping from Imaging report header model to Imaging Composition</b></p>

<p>documentMetadata should not be unmappped</p>

<p>documentMetadata.documentId explain in the comment when this mapping applies</p>

<p>documentMetadata.documentType, not convinced it should be mapped to category, documentType in the other guides is mapped to the composition.type </p>

## Resolution Description

<p>This section has been updated making this comment obsolete.</p>

## Comments

### JIRAUSER28670 (2025-07-21)

<p>documentId has gone away as well.</p>

### JIRAUSER28670 (2025-07-21)

<p>It seems that there is no more documentMetadata field in the new refactored logical model <a href="https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-

... *(truncated, 5531 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51210".
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

**Assistant:**

Now let me search for related Zulip discussions and Jira tickets about the imaging report header mapping topic.

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "imaging report header model map documentMetadata",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-51210 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 73.758 | jira | FHIR-51215 | Review header map group 2 | ehdsimagingreportheader, header, map, imaging, model, mapping, review, deprecate, report, group, apply, 5, block, type, update, vote, 1 |
| 56.469 | jira | FHIR-51672 | Update mapping for metadata elements | documenttype, ehdsimagingreportheader, header, map, metadata, composition, mapping, update |
| 51.469 | jira | FHIR-51210:79206 | FHIR-51210:79206 | documentmetadata, ehdsimagingreportheader, map, composition, mapping, explain, apply, comment |
| 50.566 | jira | FHIR-51171:69648 | FHIR-51171:69648 | documenttype, header, map, metadata, imaging, model, composition, mapping, report, category, type, 1 |
| 44.725 | jira | FHIR-51152 | Please review unmapped or missing elements in conpcetMap | header, map, model, composition, mapping, review, group, 5, block, vote |
| 42.715 | jira | FHIR-51152:79273 | FHIR-51152:79273 | map, imaging, model, composition, mapping, report, group, 5 |
| 42.512 | jira | FHIR-51733 | Include encounter in the header mapping | ehdsimagingreportheader, header, map, imaging, model, mapping, report, type, 1 |
| 41.907 | jira | FHIR-53600 | Update Xt-EHR mapping table | documenttype, header, imaging, model, composition, mapping, report, apply, category, comment, type, update, 1 |
| 39.531 | jira | FHIR-43193 | Representation of narrative | map, model, composition, mapping, report, group, guide, 5, comment, section, 1 |
| 38.819 | jira | FHIR-51151 | Group 1 seems to be a self mapping | map, imaging, model, mapping, report, group, comment, make, 1 |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-51210
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| documentmetadata | word | 3 | 15.668 |
| documentid | word | 2 | 13.988 |
| documenttype | word | 3 | 13.855 |
| metadata.documentid | word | 1 | 10.913 |
| metadata.documenttype | word | 1 | 10.913 |
| unmappped | word | 1 | 10.913 |
| ehdsimagingreportheader | word | 1 | 9.648 |
| header | word | 3 | 7.538 |
| map | word | 5 | 7.347 |
| obsolete | word | 1 | 7.179 |
| convinced | word | 1 | 7.012 |
| metadata | word | 2 | 6.734 |
| imaging | word | 2 | 6.633 |
| model | word | 3 | 6.072 |
| composition | fhir_path | 2 | 5.701 |
| mapping | word | 2 | 5.018 |
| explain | word | 1 | 4.123 |
| review | word | 2 | 3.671 |
| deprecate | word | 1 | 3.500 |
| report | word | 1 | 3.495 |

```

</details>

### Turn 4

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 5

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51210.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7Europe\\FHIR-51210.md",
  "file_text": "# FHIR-51210: Review header model map\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-51210](https://jira.hl7.org/browse/FHIR-51210) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Persuasive with Modification |\n| **Work Group** | HL7 Europe |\n| **Specification** | EU Imaging Study Report (R5) (FHIR) |\n| **Reporter** | Giorgio Cangioli |\n| **Assignee** | Unassigned |\n| **Labels** | block-vote-5 |\n| **Created** | 2025-06-24 |\n| **Updated** | 2026-03-02 |\n\n## Description\n\nThe reporter (Giorgio Cangioli) raises three concerns about **Group 1 Mapping from the Imaging report header model to Imaging Composition** in the EU Imaging Study Report IG:\n\n1. **`documentMetadata` should not be unmapped** \u2014 the backbone element is listed as unmapped, but the reporter believes it should have a mapping target.\n2. **`documentMetadata.documentId`** \u2014 the mapping comment should explain *when* this mapping applies (i.e., clarify whether it identifies the document independent of version vs. a specific document instance).\n3. **`documentMetadata.documentType`** \u2014 the reporter is not convinced it should be mapped to `Composition.category`; in other guides, `documentType` is mapped to `Composition.type`.\n\n## Resolution Description\n\n> This section has been updated making this comment obsolete.\n\nThe resolution indicates that the underlying Xt-EHR logical model was refactored, removing the `documentMetadata` field entirely from `EHDSImagingReport`. This structural change in the upstream model made the original mapping concerns moot, as the elements in question no longer exist in the source model.\n\n## Keywords\n\n`documentMetadata`, `documentId`, `documentType`, `EHDSImagingReportHeader`, `header`, `map`, `mapping`, `Composition`, `imaging`, `model`, `review`\n\n## Comment Thread Summary\n\nThe ticket has 5 comments spanning 2025-07-09 to 2025-07-21 between Giorgio Cangioli and JIRAUSER28670 (likely the IG editor):\n\n1. **JIRAUSER28670 (2025-07-09):** Asked for clarification \u2014 `documentMetadata` is a backbone element with no direct Composition target; children are mapped individually. Requested explanation of what \"explain in the comment when this mapping applies\" means.\n2. **Giorgio (2025-07-14):** Explained that `documentID` can represent either the document identifier (version-independent) or a specific instance identifier, mapped to `Composition` and `Bundle` respectively.\n3. **Giorgio (2025-07-14):** Stated that `documentMetadata` is generically represented by the `Composition` (via `relatedTo`).\n4. **JIRAUSER28670 (2025-07-21):** Noted that the refactored Xt-EHR logical model ([EHDSImagingReport](https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSImagingReport.html)) no longer contains the `documentMetadata` field. Aske

... *(truncated, 8110 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51210.md with 7958 characters
```

</details>

### Turn 6

**Assistant:**

Let me fetch closely related mapping tickets and search for Zulip discussions about the EU Imaging spec.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51210: Review header model map

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-24T08:10:49+00:00
- **Updated:** 2026-03-02T15:31:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51210

## Content
<p><b>Group 1 Mapping from Imaging report header model to Imaging Composition</b></p>

<p>documentMetadata should not be unmappped</p>

<p>documentMetadata.documentId explain in the comment when this mapping applies</p>

<p>documentMetadata.documentType, not convinced it should be mapped to category, documentType in the other guides is mapped to the composition.type </p>

## Comments (5)

### JIRAUSER28670 — 2025-07-21T12:33:12+00:00
<p>documentId has gone away as well.</p>

### JIRAUSER28670 — 2025-07-21T12:30:25+00:00
<p>It seems that there is no more documentMetadata field in the new refactored logical model <a href="https://build.fhir.org/ig/Xt-EHR/xt-ehr-common/StructureDefinition-EHDSImagingReport.html" class="external-link" target="_blank" rel="nofollow noopener">Imaging report model - EHDS Logical Information Models v0.1.0</a> </p>

<p>Can we consider this change stable <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=rlindstrom" class="user-hover" rel="rlindstrom">Rutt Lindstrom</a> ?</p>

### giorgio — 2025-07-14T12:21:05+00:00
<p>documentMetadata is generically represented by the Composition (realtedTo)</p>

### giorgio — 2025-07-14T12:20:08+00:00
<p>a documentID can represent the identifer of the document (indipendently by its version) or the identifier of an instance of a document. These are mapped into two different elements: the first in the Composiiton the second in the Bundle</p>

### JIRAUSER28670 — 2025-07-09T11:50:29+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=giorgio" class="user-hover" rel="giorgio">Giorgio Cangioli</a> </p>
<ul>
	<li><a href="https://build.fhir.org/ig/hl7-eu/imaging/branches/0.1.0-ballot/StructureDefinition-EHDSImagingReportHeader-definitions.html#EHDSImagingReportHeader.documentMetadata" class="external-link" target="_blank" rel="nofollow noopener">documentMetadata</a> is the backbone element, there is no such element to map it to in Composition. The children elements are the ones that are being mapped to the corresponding targets in the Composition elements.</li>
	<li>Can you please clarify what do you mean by "explain in the comment when this mapping applies". Is this a comment about the "is related to" attribute?</li>
</ul>


<p> </p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51215: Review header map group 2

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-24T08:19:12+00:00
- **Updated:** 2026-03-02T15:28:58+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51215

## Content
<p><b><ins>Group 2</ins></b> <ins>Mapping from</ins> Imaging report header model <ins>to</ins> Imaging Diagnostic Report</p>

<p>I’d expect to see substalliaty the large amount of information of group1  mapped also in group 2</p>

<p>Similar consideration for type and formatCode for group 1 applies also here</p>

## Comments (1)

### JIRAUSER28670 — 2025-07-09T12:35:23+00:00
<p>To solve toegether with <a href="https://jira.hl7.org/browse/FHIR-51282" title="HL7 II: DiagnosticReport should hold references to all relevant information" class="issue-link" data-issue-key="FHIR-51282"><del>FHIR-51282</del></a></p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51152: Please review unmapped or missing elements in conpcetMap

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-19T15:12:16+00:00
- **Updated:** 2026-03-03T09:41:04+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51152

## Content
<p>There are several model elements (e.g header, body in the EHDSImagingReportMap) that are or not included in the group maps or left unmatched  even when a mapping could be identified. (e.g header or body for composition)</p>

<p>Please review them and add the missing mappings.</p>

<p> </p>

## Comments (3)

### bvdh — 2026-03-03T09:40:18+00:00
<p>In various calls it has been decided not to use ConceptMaps. </p>

<p>The mappings are in a markdown table. Mappings of the main resources are in EU core, the Imaging Specific mappings are in the imaging specification.</p>

<p>As such this ticket can be closed.</p>

### bvdh — 2025-10-07T09:53:19+00:00
<p>This requires alignment between the different IG's has started. Bas will bring the resilts of that dsicussion back to the group for approval and discuaaion.</p>

### giorgio — 2025-06-19T15:15:09+00:00
<p>Some examples in the EHDSImagingReportMap:</p>

<p><b>Group 2</b> Mapping from Imaging report model to Imaging Composition</p>

<p>imagingReportHeader and imagingReportStructuredBody may be relatedTo the whole Composition</p>

<p>dicomStudyMetadata  could be mapped into the <span class="error">&#91;event:imagingstudy|#Composition.event:imagingstudy&#93;</span></p>

<p><b>Group 3</b> Mapping from Imaging report model to Imaging Diagnostic Report</p>

<p>imagingReportHeader and imagingReportStructuredBody may be relatedTo the whole DiagnosticReport</p>

<p>dicomStudyMetadata  mapping to the  <a href="#DiagnosticReport.study" target="_blank" rel="noopener">study</a> element</p>

<p><b>Group 5</b> Mapping from Imaging report model to IM Imaging Study</p>

<p>dicomStudyMetadata should be mapped as relatedTo to the whole ImagingStudy</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51300: The report (and manifest) require more fields than is needed

- **status:** Resolved - No Change
- **type:** Change Request
- **priority:** Highest
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Retracted
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **labels:** Block-Vote-3
- **Created:** 2025-06-27T12:12:33+00:00
- **Updated:** 2026-03-02T15:18:58+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51300

## Content
<p>The report specification has obligations related to data elements from the XtEHR specification. All of these are marked as "SHALL-populate-if-known". This is much to restrictive as many of these elements are not required for an imaging report.</p>

<p>The specification should restrict the SHALL-populate-if-known set to a minimal set, others may be marked as SHOULD-populate or MAY-populate. In addition, the specification should be explicit on what fields are to be made editable in the UI. Reducing that set to a set is feasible and implementable.</p>

## Comments (3)

### bvdh — 2025-12-09T10:26:02+00:00
<p><span class="image-wrap" style=""><img src="https://jira.hl7.org/secure/attachment/26509/26509_image-2025-12-09-11-25-35-332.png" style="border: 0px solid black" /></span></p>

### JIRAUSER28578 — 2025-10-28T11:09:05+00:00
<p>See discussion here: </p>

<p><a href="https://confluence.hl7.org/x/fCFYFw" class="external-link" target="_blank" rel="nofollow noopener">Proposed Scope Cuts for Reducing Complexity</a></p>

### bvdh — 2025-10-13T12:29:15+00:00
<p>Comments from imaging meeting on 7 oct:</p>
<blockquote><p>We need feedback from XtEHR and community on what is the best approach to this topic.</p>

<p>Some are useful but not part of the core. Epic can provide an initial list for this. Germany is looking to this as well. </p>

<p>Different aspects here:</p>
<ol>
	<li>what to include (SHALL/SHOULD/MAY populate (if known).</li>
	<li>what viewers are requires to show (SHALL/SHOULD/MAY display)</li>
	<li>what are applications required to handle/understand</li>
	<li>are all clients viewers - some consumers use it as source and should not be required to render it.</li>
	<li>some fields are optional but if you add them you need to do it as specified.</li>
</ol>


<p>Ideally XtEHR 8.1 need to provide this, we should wait until that input is present.</p>

<p>This content (what fields we think are key) could be input in 7.2</p>

<p>We willl have a core group - Josh/Charles/Bas/Marc - in two weeks.</p></blockquote>


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 536614817 — [EHDS - European Health Data Space] Documents vs Resources
- **Score:** 0.53
- **Updated:** 2025-08-28T14:06:45+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/EHDS%20-%20European%20Health%20Data%20Space/topic/Documents%20vs%20Resources/near/536614817
- **Snippet:** ...Lab Results - EHDSLaboratoryReport (<b>EU</b> Lab Document) - EHDSLaboratoryOrder (~DiagnosticReport) - Result Data (Observation) <b>Imaging</b> Results - EHDSImagingReport (<b>EU</b> <b>Imaging</b> <b>Report</b> Document) - <b>Imaging</b> Result...

### [zulip] 536670471 — [EHDS - European Health Data Space] Documents vs Resources
- **Score:** 0.29
- **Updated:** 2025-08-28T19:19:44+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/EHDS%20-%20European%20Health%20Data%20Space/topic/Documents%20vs%20Resources/near/536670471
- **Snippet:** ...Lab Results - EHDSLaboratoryReport (<b>EU</b> Lab Document) - EHDSLaboratoryOrder (~DiagnosticReport) - Result Data (Observation) <b>Imaging</b> Results - EHDSImagingReport (<b>EU</b> <b>Imaging</b> <b>Report</b> Document) - <b>Imaging</b> Result...

### [zulip] 500866840 — [europe] HL7 Imaging Studies and Report FHIR IG
- **Score:** 0.26
- **Updated:** 2025-02-20T12:33:30+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/HL7%20Imaging%20Studies%20and%20Report%20FHIR%20IG/near/500866840
- **Snippet:** I added a few thoughts on github: https://github.com/hl7-<b>eu</b>/<b>imaging</b>/issues

### [zulip] 499028467 — [europe] HL7 Imaging Studies and Report FHIR IG
- **Score:** 0.26
- **Updated:** 2025-02-11T14:57:11+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/HL7%20Imaging%20Studies%20and%20Report%20FHIR%20IG/near/499028467
- **Snippet:** https://health.ec.europa.<b>eu</b>/publications/ehn-guidelines-medical-<b>imaging</b>-studies-and-reports_en

### [zulip] 513584935 — [europe] HL7 Imaging Studies and Report FHIR IG
- **Score:** 0.16
- **Updated:** 2025-04-22T11:34:31+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/HL7%20Imaging%20Studies%20and%20Report%20FHIR%20IG/near/513584935
- **Snippet:** ...https://github.com/hl7-<b>eu</b>/<b>imaging</b>/tree/xtehrMapping . The build can be found at : https://build.fhir.org/ig/hl7...

### [zulip] 500168312 — [europe] HL7 Imaging Studies and Report FHIR IG
- **Score:** 0.15
- **Updated:** 2025-02-17T12:13:53+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/HL7%20Imaging%20Studies%20and%20Report%20FHIR%20IG/near/500168312
- **Snippet:** ...to confluence ( https://confluence.hl7.org/spaces/HEU/pages/321160132/2024-02+HL7+<b>EU</b>+WGM+-+<b>EU</b>-a-thon+-+<b>imaging</b>+discussions ).

### [zulip] 449227277 — [europe] EU Discharge Report
- **Score:** 0.14
- **Updated:** 2024-07-05T06:12:50+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/EU%20Discharge%20Report/near/449227277
- **Snippet:** same considerations can be done for The Diagnostic <b>Imaging</b> <b>Report</b> and the European Patient Summary

### [zulip] 517257579 — [europe] FCAT 39: EHDS track
- **Score:** 0.13
- **Updated:** 2025-05-10T13:13:47+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/FCAT%2039%3A%20EHDS%20track/near/517257579
- **Snippet:** ...hl7-<b>eu</b>/<b>imaging</b> at connecthaton39 Build: Home - HL7 Europe <b>Imaging</b> Study <b>Report</b> v0.1.0-ballot Shared drive: <b>Imaging</b> - Google...

### [zulip] 520014747 — [europe] HL7 Europe Ballot Round – Base, Imaging , Extensions (R4/R5)
- **Score:** 0.02
- **Updated:** 2025-05-23T10:01:58+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/europe/topic/HL7%20Europe%20Ballot%20Round%20%E2%80%93%20Base%2C%20Imaging%20%2C%20Extensions%20%28R4%2FR5%29/near/520014747
- **Snippet:** ...HL7 Europe <b>Imaging</b> Study <b>Report</b> FHIR IG (R5) STU1 – Ballot :document: IG: https://hl7.<b>eu</b>/fhir/<b>imaging</b>-r5/0.1...

#

... *(truncated, 4366 chars total)*
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "imaging manifest report mapping, EHDSImagingReportMap Group 6",
  "sources": "github",
  "limit": 10
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingstudy/imagingstudy-notes.xml — source/imagingstudy/imagingstudy-notes.xml
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingstudy/imagingstudy-notes.xml
- **Snippet:** ...Therefore, the requested procedure associated with a particular <b>imaging</b> study would typically be encoded as the ServiceRequest that the <b>imaging</b>...

### [github] HL7/fhir:source/imagingmanifest/imagingmanifest-spreadsheet.xml — source/imagingmanifest/imagingmanifest-spreadsheet.xml
- **Score:** 0.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingmanifest/imagingmanifest-spreadsheet.xml
- **Snippet:** ...For example, a radiologist selected a set of <b>imaging</b> SOP instances to attach in a diagnostic <b>report</b>, and a CAD...

### [github] HL7/fhir:source/imagingmanifest/imagingmanifest-spreadsheet.xml — source/imagingmanifest/imagingmanifest-spreadsheet.xml
- **Score:** 0.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/imagingmanifest/imagingmanifest-spreadsheet.xml
- **Snippet:** ...For example, a radiologist sele

... *(truncated, 4100 chars total)*
```

</details>

### Turn 7

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51210: Review header model map

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** block-vote-5
- **Created:** 2025-06-24T08:10:49+00:00
- **Updated:** 2026-03-02T15:31:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51210

## Content
<p><b>Group 1 Mapping from Imaging report header model to Imaging Composition</b></p>

<p>documentMetadata should not be unmappped</p>

<p>documentMetadata.documentId explain in the comment when this mapping applies</p>

<p>documentMetadata.documentType, not convinced it should be mapped to category, documentType in the other guides is mapped to the composition.type </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51733: Include encounter in the header mapping

- **status:** Triaged
- **type:** Change Request
- **priority:** High
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** HynekKruzik
- **Created:** 2025-08-12T09:57:49+00:00
- **Updated:** 2025-11-04T12:33:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51733

## Content
<p>Xt-EHR Header Authorship is the only mandatory element containing information about producer of the imaging report. Cardinality of this element is 1..* and includes mandatory author of type EHDSAuthor. EHDSAuthor includes optional Organization element.</p>

<p>This model actually allows inclusion of one or more authors from zero to more organizations and the IG follows this model. This will represent a potential problem with identification of a healthcare provider organization which is actualy releasing a report. And we should resolve this problem according to my opinion. </p>

<p>In fact, the organization which released the report should be equal to the organization responsible for the respective encounter. If we will agree on this, then we should ensure that encounter information will be always present and contains information about the  organization. </p>

<p> </p>

<p>My recommendation is to:</p>
<ol>
	<li>Adjust cardinality of encounter resource</li>
	<li>Add mapping from header.authorship to the encounter.organization</li>
	<li>Add Obligation for consumer to display encounter organization information</li>
	<li>Provide guidance for displaying of the  report</li>
</ol>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51211: Clarification on Group 6 Mapping

- **status:** Triaged
- **type:** Comment
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (R5) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** blocked, manifest
- **Created:** 2025-06-24T08:12:38+00:00
- **Updated:** 2026-03-02T15:29:26+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51211

## Content
<p><b>Group 6</b> Mapping from Imaging report model to IM ImagingStudy Manifest</p>

<p>Not clear this mapping since we are in the report space and I’d expect to have some mapping to the report bundle not to the manifest bundle.</p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51151: Group 1 seems to be a self mapping

- **status:** Resolved - No Change
- **type:** Technical Correction
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (FHIR)
- **resolution:** Not Persuasive
- **assignee:** Unassigned
- **reporter:** Giorgio Cangioli
- **labels:** blocked
- **Created:** 2025-06-19T15:06:17+00:00
- **Updated:** 2025-09-09T13:29:56+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51151

## Content
<p><b>Group 1</b> Mapping from <a href="https://hl7.eu/fhir/imaging-r5/StructureDefinition-EHDSImagingReport.html" class="external-link" target="_blank" rel="nofollow noopener">Imaging report model</a> to <a href="https://hl7.eu/fhir/imaging-r5/StructureDefinition-EHDSImagingReport.html" class="external-link" target="_blank" rel="nofollow noopener">Imaging report model</a></p>

<p> </p>

<p>Group 1 Mapping seems to be a mapping on itself..if this is the case please remove it</p>

```

</details>


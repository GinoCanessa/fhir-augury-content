# Session Log: FHIR-51273

**Phase:** prepared
**Work Group:** Hl7Europe
**Source File:** `prepared/Hl7Europe/FHIR-51273.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51273` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 00:37:56 UTC |
| **Duration** | 104s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 274,326 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51273
## Work Group: HL7 Europe
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51273.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51273", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51273", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51273", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51273.md
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
  "id": "FHIR-51273",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51273: Further Guidance Should Be Given on Endpoint Image Access Across Networks and Behind NCPs

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Europe
- **specification:** EU Imaging Study Report (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** JoshPriebe
- **labels:** manifest
- **Created:** 2025-06-27T09:28:25+00:00
- **Updated:** 2025-12-17T14:22:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51273

## Content
<p>It is unclear from the implementation guide how access to the endpoints (IID, WADO-RS) are controlled. This should be specified so clients and hosts can achieve consistent access methods to images.</p>
<ul>
	<li>Do the authors envision that all queries would be proxied through the NCP, with the NCP providing endpoints that would direct reference resolution to the appropriate record holders? If so, how is this managed?</li>
	<li>Alternatively, is direct access allowed?</li>
	<li>Would the NCPs themselves support IID viewing?</li>
	<li>Who could be hosting the viewer (source, intermediary, local, all of the above), and how widely are they deploying access? If an IID viewer is communicated cross-border, is there an expectation to localize the viewer to the destination?</li>
	<li>Are concepts from from <a href="https://drive.google.com/drive/u/0/folders/1VIy0PMgQY4b9TeVzN1CVKo2hRlIo3ilo" class="external-link" target="_blank" rel="nofollow noopener">XC-WADO</a> or <a href="https://github.com/jmandel/smart-imaging" class="external-link" target="_blank" rel="nofollow noopener">SMART Imaging Access</a> / <a href="https://github.com/bvdh/smart-multi-auth/blob/main/input/pagecontent/solution-dual-smart-launch.md" class="external-link" target="_blank" rel="nofollow noopener">SMART Multi Auth</a> leveraged?</li>
</ul>


<p> </p>

<p>One idea to help implementers would be to create end-to-end sequence diagrams for the key envisioned workflows, along the lines of the below. Ideally, this would include information on the pre-coordination steps anticipated and expected authentication/authorization and endpoint discovery flows behind NCPs, even if some details are left to national infrastructure.</p>

<p><span class="image-wrap" style=""><img src="https://jira.hl7.org/secure/attachment/26129/26129_image-2025-06-27-10-25-26-992.png" height="754" width="509" style="border: 0px solid black" /></span></p>

<p> Expanding on the functional process steps (described on Page 9 of the <a href="https://health.ec.europa.eu/publications/ehn-guidelines-medical-imaging-studies-and-reports_en" class="external-link" target="_blank" rel="nofollow noopener">Guidelines on medical imaging studies and reports</a>, Release 1.1, Nov 2024, page 9) with diagrams for the key workflows would help the implementer community during implementation. This would reduce both cost and the time to implement.</p>

<p><span class="image-wrap" style=""><img src="https://jira.hl7.org/secure/attachment/26128/26128_image-2025-06-27-10-25-55-025.png" height="733" width="634" style="border: 0px solid black" /></span></p>

<p>Furthermore, creating such documentation now ensures a consistent understanding of the envisioned flows during design and further balloting of this specification. This would be very helpful to add with the <a href="https://build.fhir.org/ig/hl7-eu/imaging/branches/qa-fixes-ballot1/transactions.html" class="external-link" target="_blank" rel="nofollow noopener">Transactions page</a> under development.</p>

<p> </p>

<p> </p>

## Comments (2)

### JIRAUSER28578 — 2025-12-17T14:22:05+00:00
<p>XC-WADO + MADO handle the representation of the manifest and conveyance of the image links. It gestures at transport via MHD/XCA/XDS.</p>

<p>What's missing is the authorization to access the WADO-RS endpoint. Imagine a consumer has a manifest, which gives them the info to build a URL. What happens when they launch that URL? How is this endpoint authoriz

... *(truncated, 9119 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51273".
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

**Assistant:**

Let me search for additional Zulip context on the key imaging topics.

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "WADO endpoint imaging access NCP, SMART Imaging Access authorization"
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
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-51273
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| ncps | word | 4 | 11.134 |
| iid | word | 3 | 7.260 |
| viewer | word | 3 | 6.495 |
| envision | word | 3 | 6.412 |
| ncp | word | 2 | 6.357 |
| wado | word | 3 | 6.123 |
| access | word | 7 | 5.130 |
| manifest | word | 3 | 5.006 |
| image | word | 5 | 4.723 |
| endpoint | fhir_path | 4 | 4.675 |
| proxied | word | 1 | 4.208 |
| 754 | word | 1 | 4.208 |
| style | word | 4 | 4.175 |
| 733 | word | 1 | 4.016 |
| imimageiidviewerendpoint | word | 1 | 4.016 |
| host | word | 2 | 3.916 |
| 634 | word | 1 | 3.890 |
| endpoints | word | 2 | 3.842 |
| li | word | 10 | 3.833 |
| imwadoendpoint | word | 1 | 3.796 |
| xc | word | 1 | 3.557 |
| network | word | 2 | 3.520 |
| obligation | word | 2 | 3.347 |
| border | word | 3 | 3.334 |
| flow | word | 2 | 3.278 |
| direct | word | 2 | 3.208 |
| localize | word | 1 | 3.192 |
| 509 | word | 1 | 3.160 |
| imaging | word | 2 | 3.152 |
| 0px | word | 2 | 3.062 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51273.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7Europe\\FHIR-51273.md",
  "file_text": "# FHIR-51273: Further Guidance Should Be Given on Endpoint Image Access Across Networks and Behind NCPs\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-51273](https://jira.hl7.org/browse/FHIR-51273) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Specification** | EU Imaging Study Report (FHIR) |\n| **Work Group** | HL7 Europe |\n| **Reporter** | JoshPriebe |\n| **Created** | 2025-06-27 |\n| **Updated** | 2025-12-17 |\n| **Labels** | manifest |\n\n## Description Summary\n\nThe submitter requests that the EU Imaging Study Report IG provide explicit guidance on how access to imaging endpoints (IID and WADO-RS) is controlled in cross-border scenarios involving National Contact Points (NCPs). The ticket raises several key questions:\n\n1. **Proxy vs. direct access** \u2014 Should all queries be proxied through the NCP, with the NCP providing endpoints that resolve references to record holders? Or is direct access to imaging endpoints permitted?\n2. **NCP viewer support** \u2014 Would NCPs themselves support IID viewing?\n3. **Viewer hosting and localization** \u2014 Who hosts the viewer (source, intermediary, local, or all), and is there an expectation to localize viewers for the destination country?\n4. **Leveraging existing standards** \u2014 Should the IG leverage concepts from XC-WADO, SMART Imaging Access, or SMART Multi Auth?\n5. **Sequence diagrams** \u2014 The submitter proposes creating end-to-end sequence diagrams for key workflows, including pre-coordination steps, authentication/authorization flows, and endpoint discovery behind NCPs.\n\nThe submitter argues that such documentation would reduce implementation cost and time, ensure consistent understanding of envisioned flows during further balloting, and complement the [Transactions page](https://build.fhir.org/ig/hl7-eu/imaging/branches/qa-fixes-ballot1/transactions.html) under development.\n\n## Comments Summary\n\nTwo comments provide substantive responses:\n\n- **JIRAUSER30266 (2025-12-16):** Points to the IHE XC-WADO profile as the solution, noting it can be grouped with the IHE MADO Profile to gain access to retrieve URLs via the imaging study manifest (MADO) and format them for cross-border retrieval per XC-WADO.\n\n- **JIRAUSER28578 (2025-12-17):** Agrees that XC-WADO + MADO handle manifest representation and image link conveyance (via MHD/XCA/XDS transport), but identifies **authorization to the WADO-RS endpoint** as the missing piece. Specifically: when a consumer has a manifest and builds a WADO-RS URL, what happens when they launch it? How is the endpoint authorized? Is it assumed to go through the same auth and NCP pipes (which would route heavy DICOM bits through many hops), or does authorization need to be separately negotiated?\n\n## Keywords\n\n`NCP` \u00b7 `IID` \u00b7 `WADO-RS` \u00b7 `viewer` \u00b7 `

... *(truncated, 8962 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7Europe\FHIR-51273.md with 8705 characters
```

</details>


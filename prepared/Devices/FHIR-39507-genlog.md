# Session Log: FHIR-39507

**Phase:** prepared
**Work Group:** Devices
**Source File:** `prepared/Devices/FHIR-39507.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-39507` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:30:22 UTC |
| **Duration** | 121s |
| **Total Tool Calls** | 19 |
| **Total Tokens** | 356,748 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-39507
## Work Group: Devices
## Output File: C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-39507.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-39507", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-39507", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-39507", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-39507.md
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
  "id": "FHIR-39507",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-39507: Insufficient guidance on how devices should deal with Patient and Location resources

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Devices
- **specification:** Point of Care Devices (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Javier Espina
- **labels:** block-vote-1
- **Created:** 2022-11-28T17:46:58+00:00
- **Updated:** 2026-03-25T10:13:10+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-39507

## Content
<p>The RESTFUL transfer page describes some FHIR-generic options for transferring device-sourced data. However I could not find clear recommendation in the IG on the approach to follow regarding the Patient and Location resources. For instance, creating and including it in the device-data bundle vs. having a pointer to the resource on the destination FHIR server (when is the latter possible?). Another example is the alignment with additional resource profiles that a specific hospital may have. Such further guidance would probably require identifying some uses cases / deployment archetypes.</p>

<p>This may be connected to ongoing discussions on workflow aspects at the O&amp;O WG as well (#Order Logical Model Application to FHIR).</p>

## Comments (5)

### erikmoll — 2026-03-25T10:13:10+00:00
<p>A preview is available here: <a href="https://build.fhir.org/ig/HL7/uv-pocd/branches/FHIR-39507/profiles.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/uv-pocd/branches/FHIR-39507/profiles.html</a></p>

<p> </p>

### javier_espina — 2026-03-19T16:55:34+00:00
<p>This proposed resolution sounds like it could be sufficient for the current version (1.X Edition )of the IG. Just one comment on the propose text: the brief future work description should match with the project scope (I haven't cross-checked)</p>

### erikmoll — 2026-03-19T12:30:09+00:00
<p>We can add this text to the profiles overview:</p>
<h3><a name="PatientandLocationResourceHandling"></a>Patient and Location Resource Handling</h3>

<p>Point-of-care devices generate observations that reference Patient and Location resources, but the device or gateway typically is not the authoritative source for these resources. This section provides guidance on how to handle Patient and Location references in different deployment scenarios.</p>
<h4><a name="ReferencePatterns"></a>Reference Patterns</h4>

<p>There are three patterns for including Patient and Location references in device data, and the choice depends on the deployment context:</p>
<ol>
	<li><b>Reference existing resources</b>: When the destination FHIR server is the system of record for Patient and Location resources (the most common scenario in enterprise deployments), the device or gateway resolves references by searching with known identifiers before submitting observations. This requires the device or gateway to have access to patient and location identifiers, typically received through an ADT feed or device association workflow.</li>
</ol>


<ol>
	<li><b>Conditional create in the bundle</b>: When the device or gateway has sufficient identity information but does not know whether the resource already exists on the server, it can include a Patient or Location resource in the transaction bundle with a conditional create request (<tt>ifNoneExist</tt>). The server will use the existing resource if found, or create a new one. This approach requires strong identifiers (such as MRN for Patient or a unique name for Location) to avoid creating duplicates. See the <a href="https://file+.vscode-resource.vscode-cdn.net/Users/nly99011/Documents/GitHub/uv-pocd/input/pagecontent/transfer.html#conditional-create" class="external-link" target="_blank" rel="nofollow noopener">RESTful Transfer</a> page for examples.</li>
</ol>


<ol>
	<li><b>Include in the bundle</b>: When the device is the source of truth for the resource (rare for Patient, but possible for Loca

... *(truncated, 17371 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-39507".
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

Let me check for GitHub branches/PRs related to this ticket.

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-39507
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| gateway | word | 7 | 7.097 |
| h4 | word | 8 | 7.041 |
| deployment | word | 6 | 6.976 |
| location | fhir_path | 21 | 6.618 |
| device | word | 21 | 5.951 |
| destination | word | 4 | 4.790 |
| archetype | word | 2 | 3.967 |
| ol | word | 6 | 3.951 |
| patient | fhir_path | 20 | 3.902 |
| conditional | word | 3 | 3.775 |
| adt | word | 2 | 3.586 |
| transfer | word | 3 | 3.581 |
| mrn | word | 2 | 3.397 |
| bundle | fhir_path | 5 | 3.369 |
| server | word | 6 | 3.290 |
| pattern | word | 4 | 3.094 |
| resource | word | 20 | 3.084 |
| identifier | word | 5 | 3.024 |
| create | word | 7 | 2.931 |
| insufficient | word | 2 | 2.929 |

```

</details>

<details>
<summary>`github-mcp-server-search_code` — FHIR-39507 repo:HL7/uv-pocd</summary>

**Result:**
```
{"total_count":0,"incomplete_results":false}
```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-39507.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Devices\\FHIR-39507.md",
  "file_text": "# FHIR-39507: Insufficient guidance on how devices should deal with Patient and Location resources\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-39507](https://jira.hl7.org/browse/FHIR-39507) |\n| **Status** | Triaged |\n| **Resolution** | Persuasive |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Work Group** | Devices |\n| **Specification** | Point of Care Devices (FHIR) |\n| **Reporter** | Javier Espina |\n| **Labels** | block-vote-1 |\n| **Created** | 2022-11-28 |\n| **Updated** | 2026-03-25 |\n\nThe reporter notes that the PoCD IG's RESTful transfer page describes FHIR-generic options for transferring device-sourced data, but lacks clear guidance on how to handle **Patient** and **Location** resources specifically. Key questions include: when to create and include these resources in a device-data bundle versus referencing existing resources on the destination FHIR server, and how to align with additional resource profiles that a specific hospital may require. The reporter suggests that deployment archetypes and use cases should be identified to provide this guidance, and notes a possible connection to workflow discussions in the Orders & Observations WG.\n\n## Details\n\n### Proposed Resolution\n\nThe resolution (marked **Persuasive**) proposes adding a new section to the PoCD IG profiles overview page titled **\"Patient and Location Resource Handling\"** with the following subsections:\n\n1. **Reference Patterns** \u2014 Three patterns for including Patient and Location references in device data:\n   - **Reference existing resources**: The device/gateway resolves references by searching with known identifiers before submitting observations (most common in enterprise deployments).\n   - **Conditional create in the bundle**: Include Patient/Location in a transaction bundle with `ifNoneExist`; requires strong identifiers (e.g., MRN) to avoid duplicates.\n   - **Include in the bundle**: The device is the source of truth for the resource (rare for Patient; possible for Location in mobile/temporary setups).\n\n2. **Minimum Identity Requirements** \u2014 Patient references should include at least an MRN or facility-specific identifier from an ADT system. Location references should include at least a bed label or location identifier matchable against server resources.\n\n3. **Conformance to Destination Profiles** \u2014 The IG does not profile Patient or Location for clinical use; implementers should conform to profiles required by their deployment context (e.g., US Core, IPA).\n\n4. **Future Work** \u2014 Deployment archetypes and workflow integration patterns (including device observations and clinical orders) are deferred to future versions.\n\n### Comment History\n\n- **esilver (2022-11-28)**: Suggested considering whether the guidance should be prescriptive or present potential approaches with pros/co

... *(truncated, 8948 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Devices\FHIR-39507.md with 8791 characters
```

</details>

### Turn 4

**Assistant:**

Let me fetch details on the most closely related Jira tickets from the same specification area.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-39507: Insufficient guidance on how devices should deal with Patient and Location resources

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Devices
- **specification:** Point of Care Devices (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Javier Espina
- **labels:** block-vote-1
- **Created:** 2022-11-28T17:46:58+00:00
- **Updated:** 2026-03-25T10:13:10+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-39507

## Content
<p>The RESTFUL transfer page describes some FHIR-generic options for transferring device-sourced data. However I could not find clear recommendation in the IG on the approach to follow regarding the Patient and Location resources. For instance, creating and including it in the device-data bundle vs. having a pointer to the resource on the destination FHIR server (when is the latter possible?). Another example is the alignment with additional resource profiles that a specific hospital may have. Such further guidance would probably require identifying some uses cases / deployment archetypes.</p>

<p>This may be connected to ongoing discussions on workflow aspects at the O&amp;O WG as well (#Order Logical Model Application to FHIR).</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33885: confusing stated with respect

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Security
- **specification:** FHIR Data Segmentation for Privacy (FHIR)
- **resolution:** Persuasive
- **assignee:** Mohammad Jafari
- **reporter:** John Moehrke
- **labels:** jan22-block-vote-editorial
- **Created:** 2021-09-16T00:51:50+00:00
- **Updated:** 2023-04-17T19:39:44+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33885

## Content
<p>last paragraph of section 1.2. This is not clear to me the message being sent. I will assert that the FHIR core says nothing like this, indeed the point of FHIR core is that it is policy-less. So I think the intention of this paragraph is to explain that policy and guidance are needed. That conformance claims to the DS4P IG impart some policy and behavior requirements like indicated in this paragraph. That imparting policy is indeed very important. I stress this, which is also stressed in the text you have quoted from the FHIR core security label page.</p>
<blockquote><p><b><del>While stated with respect to FHIR content, this</del></b> <ins><b>As quoted above from the</b></ins> <a href="http://hl7.org/fhir/security-labels.html" class="external-link" target="_blank" rel="nofollow noopener">FHIR Security Label Module</a> caveat <ins><b>that, policies must be implemented,</b> </ins> holds for <b><del>other</del></b> labeled content <b><del>as well</del></b>: “The intent of a security label is that the recipient of resources or bundles with security tags is obligated to enforce the handling caveats of the tags and carry the security labels forward as appropriate.” And, regardless of the content syntax, “Security Labels enable more data to flow as they enable policy fragments to accompany the resource data.”</p></blockquote>
<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-25602: Clarify action when required data is not available

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** US CARIN Blue Button (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Craig Newman
- **labels:** Block-Vote-2a, MustSupport, Narrative
- **Created:** 2020-01-24T13:03:57+00:00
- **Updated:** 2020-11-23T17:50:46+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-25602

## Content
<p>Currently reads:</p>

<p>In situations where information on a particular data element is not present and the reason for absence is unknown, Health Plan API actors SHALL NOT include the data elements in the resource instance returned as part of the query results.</p>

<p> </p>

<p>What should happen if the missing data element is required (minimum cardinality of 1)? Should the whole resource not be returned? Should there be some indication that such information exists but cannot be returned? Some clarification may be helpful even it's just pointing back to general FHIR recommendations for handling this situation in general.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26212: New IG for messaging fundamentals

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Infrastructure & Messaging
- **specification:** US Da Vinci Alerts (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Nick Radov
- **labels:** why-messaging
- **Created:** 2020-02-13T20:42:10+00:00
- **Updated:** 2024-08-28T17:51:35+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26212

## Content
<p>I don't think we should do that in this IG. Instead define a new IG for foundational Da Vinci messaging guidelines and put it there. We will likely using the messaging paradigm in additional future IGs beyond just Alerts so we won't want to repeat ourselves.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Note To Balloters  <br/>
We are actively seeking input on whether additional guidance should be documented in this guide on FHIR-related errors (in addition to normal HTTP errors related to security, header and content type negotiation issues). For example, whether to define a minimum set of error response code, such as those listed here. Additionally, what additional guidance to specify how the Sender can provide a more reliable delivery of notifications to the intended recipient(s). For example, defining what actions the Sender must take when it receives a particular error response code.</p>

```

</details>


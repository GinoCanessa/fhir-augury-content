# Session Log: FHIR-33362

**Phase:** prepared
**Work Group:** CrossgroupProjects
**Source File:** `prepared/CrossgroupProjects/FHIR-33362.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-33362` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:10:48 UTC |
| **Duration** | 105s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 262,489 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-33362
## Work Group: Cross-Group Projects
## Output File: C:\ai\git\fhir-augury-content\prepared\CrossgroupProjects\FHIR-33362.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-33362", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-33362", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-33362", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\CrossgroupProjects\FHIR-33362.md
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
  "id": "FHIR-33362",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-33362: NAICS codes are significantly different from military MOS and other occupational codes.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Military Service (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Keith Salzman
- **labels:** Block-Vote-3
- **Created:** 2021-09-02T20:45:31+00:00
- **Updated:** 2023-05-30T15:35:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33362

## Content
<p>Is it being proposed to match specific military occupational or duty codes to NAICS codes?  If so, how?</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<p>(<b>Comment 12 - imported by: Chris Shawn</b>)</p>

## Comments (2)

### lynn_laakso — 2023-05-30T15:35:21+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2023-05-30T15:35:21+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-07-28 00:00:00.0 with vote Sean Muir/Eric Haas: 11-0-1//(Impact: null; Category: null; Version: null)//No, but perhaps future version will </p>


## Snapshot
# FHIR-33362: NAICS codes are significantly different from military MOS and other occupational codes.

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Keith Salzman  
**Work Group:** Cross-Group Projects  
**Specification:** US Military Service (FHIR)  
**Labels:** Block-Vote-3  
**Created:** 2021-09-02  
**Updated:** 2023-05-30  

## Description

<p>Is it being proposed to match specific military occupational or duty codes to NAICS codes?  If so, how?</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<p>(<b>Comment 12 - imported by: Chris Shawn</b>)</p>

## Comments

### lynn_laakso (2023-05-30)

<p>re-open post STU1 publication</p>

### lynn_laakso (2023-05-30)

<p>Reverted previous resolution: Considered for Future Use made 2022-07-28 00:00:00.0 with vote Sean Muir/Eric Haas: 11-0-1//(Impact: null; Category: null; Version: null)//No, but perhaps future version will </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-33362".
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
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "US Military Service, military service history veteran"
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 498001678 — [implementers] VA run_synthia data
- **Score:** 0.20
- **Updated:** 2025-02-05T23:27:02+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/VA%20run_synthia%20data/near/498001678
- **Snippet:** Take a look at this guide: https://hl7.org/fhir/<b>us</b>/<b>military</b>-<b>service</b>/

### [zulip] 433346649 — [implementers] Extension:Context
- **Score:** 0.07
- **Updated:** 2024-04-15T17:16:59+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Extension%3AContext/near/433346649
- **Snippet:** ...https://hl7.org/fhir/<b>us</b>/<b>military</b>-<b>service</b>/STU1/StructureDefinition-<b>military</b>-<b>service</b>-veteran-status.html i m trying to use this...

### [zulip] 362224531 — [Announcements] New Publication
- **Score:** 0.06
- **Updated:** 2023-05-30T15:42:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Announcements/topic/New%20Publication/near/362224531
- **Snippet:** ...<b>Military</b> <b>Service</b> History and Status, Release 1 - <b>US</b> Realm: http://hl7.org/fhir/<b>us</b>/<b>military</b>-<b>service</b>/STU1

### [zulip] 475353048 — [implementers] HL7 ADT PID.27 - Veteran's Military Status
- **Score:** 0.04
- **Updated:** 2024-10-07T17:38:32+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/HL7%20ADT%20PID.27%20-%20Veteran%27s%20Military%20Status/near/475353048
- **Snippet:** ...<b>service</b>. PID.27 is for veterans (only). All of these fields are probably only ever used in the <b>US</b> (where...

### [zulip] 209568802 — [military_service] Connectathon 25
- **Score:** 0.01
- **Updated:** 2020-09-09T21:07:03+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/military_service/topic/Connectathon%2025/near/209568802
- **Snippet:** @Ioana Singureanu the IG called <b>military</b> <b>service</b>, is that <b>US</b> only?

### [zulip] 201287019 — [implementers] Observation or extension
- **Score:** 0.01
- **Updated:** 2020-06-18T15:49:56+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Observation%20or%20extension/near/201287019
- **Snippet:** ...zoom.<b>us</b>/j/98656497049 ) if you have any questions or add your comments to the Confluence page. <b>Military</b>-<b>Service</b>-History...

### [zulip] 153900275 — [committers] ✔ ig-build
- **Score:** 0.00
- **Updated:** 2017-08-02T23:57:02+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/%E2%9C%94%20ig-build/near/153900275
- **Snippet:** @Eric Haas Did the <b>us</b>-core patient profile used to include an extension for <b>military</b> <b>service</b>?

### [zulip] 283334992 — [implementers] Problematic extensions
- **Score:** 0.00
- **Updated:** 2022-05-23T15:24:25+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Problematic%20extensions/near/283334992
- **Snippet:** ...diagnostics": "Unknown extension http://hl7.org/fhir/<b>us</b>/<b>military</b>-<b>service</b>/StructureDefinition/<b>military</b>-<b>service</b>-veteran-status", "location": [ "Patient.extension[5]", "Line...

### [zulip] 153974233 — [IG creation] Getting invalid URL for body-site-instance extension url
- **Score:** 0.00
- **Updated:** 2018-07-07T20:45:55+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IG%20creation/topic/Getting%20invalid%20URL%20for%20body-site-instance%20extension%20url/near/153974233
- **Snippet:** ...Unable to find Extension 'http://hl7.org/fhir/<b>us</b>/qicore/StructureDefinition/qicore-<b>military</b>-<b>service</b>' referenced at http://hl7.org/fhir...

### [zulip] 443994085 — [implementers] individual-pronoun
- **Score:** 0.00
- **Updated:** 2024-06-11T13:00:49+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/individual-pronoun/near/443994085
- **Snippet:** ...codingstandard:hsi" } ] } }, { "url": " http://hl7.org/fhir/<b>us</b>/<b>military</b>-<b>service</b>/StructureDefinition/<b>mil

... *(truncated, 4093 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-33362
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| wage | word | 2 | 11.441 |
| military | word | 5 | 11.140 |
| naics | word | 3 | 11.111 |
| mos | word | 2 | 10.919 |
| compensate | word | 2 | 9.277 |
| occupational | word | 3 | 8.823 |
| volunteer | word | 2 | 7.915 |
| training | word | 2 | 7.618 |
| employ | word | 2 | 7.587 |
| business | word | 6 | 7.549 |
| company | word | 2 | 7.091 |
| conduct | word | 2 | 7.035 |
| kind | word | 4 | 6.636 |
| significantly | word | 2 | 6.536 |
| position | word | 2 | 6.006 |
| person | fhir_path | 4 | 5.921 |
| branch | word | 2 | 5.813 |
| duty | word | 1 | 5.779 |
| determined | word | 2 | 5.233 |
| h3 | word | 4 | 5.103 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\CrossgroupProjects\FHIR-33362.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\CrossgroupProjects\\FHIR-33362.md",
  "file_text": "# FHIR-33362: NAICS codes are significantly different from military MOS and other occupational codes\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-33362](https://jira.hl7.org/browse/FHIR-33362) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Work Group** | Cross-Group Projects |\n| **Specification** | US Military Service (FHIR) |\n| **Reporter** | Keith Salzman |\n| **Assignee** | Unassigned |\n| **Labels** | Block-Vote-3 |\n| **Created** | 2021-09-02 |\n| **Updated** | 2023-05-30 |\n\n## Description\n\nThe submitter questions whether the IG proposes to match specific military occupational or duty codes (e.g., Military Occupational Specialty \u2014 MOS) to NAICS (North American Industry Classification System) codes, and if so, how that mapping would work. The concern is that NAICS codes classify businesses by industry activity, which is fundamentally different from military occupational specialty codes that classify individual job roles and duties within the armed services.\n\n**Existing Wording:** The value set description references \"Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.\"\n\n**Proposed Wording:** The proposed wording is identical to the existing wording \u2014 the submitter did not provide an alternative, instead raising a question about the appropriateness and methodology of mapping military codes to NAICS codes.\n\n## Ticket History\n\n- **2021-09-02:** Ticket created by Keith Salzman (imported as Comment 12 by Chris Shawn).\n- **2022-07-28:** Previously resolved as \"Considered for Future Use\" with vote Sean Muir/Eric Haas: 11-0-1. Comment: \"No, but perhaps future version will.\"\n- **2023-05-30:** Lynn Laakso re-opened the ticket post-STU1 publication, reverting the previous resolution.\n\n## Keywords\n\nNAICS, MOS, military occupational codes, duty codes, business classification, industry codes, occupational data, value set, US Military Service IG\n\n## Related Jira Tickets\n\n| Key | Title | Status | Resolution | Relevance |\n|-----|-------|--------|------------|-----------|\n| [FHIR-33356](https://jira.hl7.org/browse/FHIR-33356) | Recommended discussing this with active duty OM specialists | Published | Persuasive with Modification | Same reporter (Salzman), same IG; recommends consulting Occupational Medicine SMEs about military health data capture, including systems like DOEHRS |\n| [FHIR-33351](https://jira.hl7.org/browse/FHIR-33351) | Should be written to support equiv

... *(truncated, 10035 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\CrossgroupProjects\FHIR-33362.md with 9832 characters
```

</details>

### Turn 4

**Assistant:**

Now let me check for any Zulip discussions about this IG and get details on another related ticket.

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 507330134 — [implementers] Modeling Combat Casualty Care in FHIR
- **Score:** 0.31
- **Updated:** 2025-03-21T17:19:37+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Modeling%20Combat%20Casualty%20Care%20in%20FHIR/near/507330134
- **Snippet:** ...had expanded past <b>military</b> <b>history</b>/<b>status</b> (which is definitely helpful) but this seemed to be the extent for this <b>IG</b>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33362: NAICS codes are significantly different from military MOS and other occupational codes.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Military Service (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Keith Salzman
- **labels:** Block-Vote-3
- **Created:** 2021-09-02T20:45:31+00:00
- **Updated:** 2023-05-30T15:35:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33362

## Content
<p>Is it being proposed to match specific military occupational or duty codes to NAICS codes?  If so, how?</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<p>(<b>Comment 12 - imported by: Chris Shawn</b>)</p>

## Comments (2)

### lynn_laakso — 2023-05-30T15:35:21+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2023-05-30T15:35:21+00:00
<p>Reverted previous resolution: Considered for Future Use made 2022-07-28 00:00:00.0 with vote Sean Muir/Eric Haas: 11-0-1//(Impact: null; Category: null; Version: null)//No, but perhaps future version will </p>


```

</details>

### Turn 5

**Assistant:**

Let me fetch more details on the related open tickets and search for any broader Zulip discussions.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33362: NAICS codes are significantly different from military MOS and other occupational codes.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Military Service (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Keith Salzman
- **labels:** Block-Vote-3
- **Created:** 2021-09-02T20:45:31+00:00
- **Updated:** 2023-05-30T15:35:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33362

## Content
<p>Is it being proposed to match specific military occupational or duty codes to NAICS codes?  If so, how?</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Value Set Description Concepts describing the kind of business that compensates the person for work (e.g., wages, training) or assigns work to a volunteer, as reported by the person. The kind of business is determined based on the primary business activity conducted by the company, organization, or individual (for those who are self-employed), or, for a military position, the self-reported branch of service.</p>

<p>(<b>Comment 12 - imported by: Chris Shawn</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33353: Address clinical conditions that represent risks to the patient based on career exposures-include or defer for future

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Military Service (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Keith Salzman
- **labels:** Block-Vote-3
- **Created:** 2021-09-02T20:45:18+00:00
- **Updated:** 2023-05-30T15:35:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33353

## Content
<p>…health risks…The implication is that the required codes for risk status (i.e. Post Traumatic Stress, Asbestos exposure, burn pit exposure, depleted uranium exposure, are part of this IG and the profiles and extensions that would capture these conditions would feed the data for review by the provider or input by the patient. Acknowledging this need specifically and accounting for it  either in the deferred section, or in the documentation of how this information is captured for review should be a part of this IG</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The clinician may be working with Veteran in the community and must assess the health risks associate with military service.</p>

<p>(<b>Comment 3 - imported by: Chris Shawn</b>)</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33442: Military Service Episode bindings may be too strict

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Military Service (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Craig Newman
- **labels:** Block-Vote-2
- **Created:** 2021-09-08T15:39:08+00:00
- **Updated:** 2022-05-03T21:20:17+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33442

## Content
<p>All of the value set bindings for the .component slices are Required which may render the profile unusable for non-US settings. A binding strength of Extensible or Preferred may make the IG more implementable in outside of the US.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33681: resources should be defined in this IG

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Cross-Group Projects
- **specification:** US Military Service (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** John Moehrke
- **labels:** Block-Vote-3
- **Created:** 2021-09-14T22:55:10+00:00
- **Updated:** 2023-05-30T15:33:53+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33681

## Content
<p>Find references to resources not defined by a standards organization. </p>

<p>For example, the extension *<a href="https://www.logicahealth.org/solutions/solor/military-service*" class="external-link" target="_blank" rel="nofollow noopener">https://www.logicahealth.org/solutions/solor/military-service*</a></p>

<p>should be defined in this IG and thus have a canonical URI based on hl7.org and the canonical URI of this IG.</p>

<p> </p>

<p>exceptions for vocabulary standards bodies.</p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 362224531 — [Announcements] New Publication
- **Score:** 0.04
- **Updated:** 2023-05-30T15:42:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Announcements/topic/New%20Publication/near/362224531
- **Snippet:** ...<b>Military</b> <b>Service</b> History and Status, Release 1 - US Realm: http://hl7.org/fhir/us/<b>military</b>-<b>service</b>/STU1

### [zulip] 252702893 — [Death on FHIR] Decedent's Military Service
- **Score:** 0.02
- **Updated:** 2021-09-09T22:00:57+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Death%20on%20FHIR/topic/Decedent%27s%20Military%20Service/near/252702893
- **Snippet:** For Madelyn Patel record, in spreadsheet it says Y for <b>Military</b> <b>Service</b> but Canary expects Unknown

### [zulip] 253324652 — [Death on FHIR] Decedent's Military Service
- **Score:** 0.01
- **Updated:** 2021-09-14T21:10:23+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Death%20on%20FHIR/topic/Decedent%27s%20Military%20Service/near/253324652
- **Snippet:** In that case you can use null in the case the <b>Military</b> <b>service</b> is unknown, it would look like this...

### [zulip] 252703354 — [Death on FHIR] Decedent's Military Service
- **Score:** 0.01
- **Updated:** 2021-09-09T22:05:04+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Death%20on%20FHIR/topic/Decedent%27s%20Military%20Service/near/252703354
- **Snippet:** Logged as NVSS-263 -- will investigate.

### [zulip] 209550472 — [Announcements] new streams
- **Score:** 0.00
- **Updated:** 2020-09-09T18:37:46+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Announcements/topic/new%20streams/near/209550472
- **Snippet:** Ioana Singureanu created a new stream #<b>military</b>_<b>service</b> .

### [zulip] 253326691 — [Death on FHIR] Decedent's Military Service
- **Score:** 0.00
- **Updated:** 2021-09-14T21:25:48+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Death%20on%20FHIR/topic/Decedent%27s%20Military%20Service/near/253326691
- **Snippet:** not passing null , setting the value "UNK"

### [zulip] 209626720 — [connectathon mgmt] Military Service History and Status Track
- **Score:** 0.00
- **Updated:** 2020-09-10T11:47:36+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/connectathon%20mgmt/topic/Military%20Service%20History%20and%20Status%20Track/near/209626720
- **Snippet:** #<b>military</b>_<b>service</b> stream available for engagement/communication. We're planning to keep the Zoom stream in Whova available all day...

### [zulip] 253322589 — [Death on FHIR] Decedent's Military Service
- **Score:** 0.00
- **Updated:** 2021-09-14T20:55:58+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Death%20on%20FHIR/topic/Decedent%27s%20Military%20Service/near/253322589
- **Snippet:** setting value to the member "MilitaryServiceBoolean" of DeathRecord.

### [zulip] 253311717 — [Death on FHIR] Decedent's Military Service
- **Score:** 0.00
- **Updated:** 2021-09-14T19:43:08+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Death%20on%20FHIR/topic/Decedent%27s%20Military%20Service/near/253311717
- **Snippet:** Canary validated the file and error out.... image.png

### [zulip] 209568802 — [military_service] Connectathon 25
- **Score:** 0.00
- **Updated:** 2020-09-09T21:07:03+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/military_service/topic/Connectathon%2025/near/209568802
- **Snippet:** @Ioana Singureanu the IG called <b>military</b> <b>service</b>, is that US only?


```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-33686 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 31.461 | jira | FHIR-24114 | Section 5.4.2.1 Polling - ClaimResponse search criteria and expected response are in conflict | query, bundle, return, search, item, define, block, resource, vote |
| 30.252 | jira | FHIR-36394:39101 | FHIR-36394:39101 | query, bring, return, relevant, search, item, 3, define, set, resource |
| 29.795 | jira | FHIR-44920 | Reporting Issues in Matching | query, composition, bundle, return, relevant, block, resource, vote |
| 29.627 | jira | FHIR-55394 | How to order resource entries when multiple ClaimResponses in a Bundle? | query, rest, service, bundle, return, item, resource |
| 29.161 | jira | FHIR-23553 | How does this profile describes that the search didn't return any matches? - CDex #171 | query, bundle, return, search, 3, set, block, resource, vote |
| 28.829 | jira | FHIR-33576 | US Military Service/SOLOR Military Service History and Status Value set | military, service, 3, set, block, vote |
| 28.484 | jira | FHIR-34775 | Describe a minimal required FHIR RESTful transaction | query, rest, simple, return, search, 3, block, resource, vote |
| 28.469 | jira | FHIR-36431 | Inconsistency in how value sets & libraries are returned | query, simple, return, relevant, search, set, block, resource, vote |
| 28.402 | jira | FHIR-35271 | AEOB Query should take a different approach | query, rest, simple, bundle, search, define |
| 28.285 | jira | FHIR-33578 | Where is a section or profile to delineate specific exposure risks? | military, service, missing, 3, block, vote |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>


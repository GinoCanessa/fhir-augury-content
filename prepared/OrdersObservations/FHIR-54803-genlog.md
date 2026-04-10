# Session Log: FHIR-54803

**Phase:** prepared
**Work Group:** OrdersObservations
**Source File:** `prepared/OrdersObservations/FHIR-54803.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `52256f69-5fb6-416b-be46-75c24182f098` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-54803` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 13:12:06 UTC |
| **Duration** | 97s |
| **Total Tool Calls** | 19 |
| **Total Tokens** | 356,294 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-54803
## Work Group: Orders & Observations
## Output File: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-54803.md

## Data Access
Use FhirAugury MCP tools (preferred) or CLI fallback at: C:\ai\git\fhir-augury\src\FhirAugury.Cli\bin\Release\net10.0\FhirAugury.Cli.exe

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-54803", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-54803", limit=50)

## Step 2: Fetch Related Jira Tickets
For each Jira ticket found in cross-references, fetch its details.

## Step 3: Fetch Zulip Conversations
For each Zulip cross-reference, get the thread. Also search:
FhirAugury-content_search(values="FHIR-54803", sources="zulip", limit=10)

## Step 4: Note GitHub Items

## Step 5: Build the Report using the standard template with sections: Title/metadata, Summary, Details (description + comments), Keywords, Related Zulip Discussions, Related GitHub Items, three Proposed Dispositions (A: Accept, B: Alternative, C: Decline), and Recommendation.

## Important Rules
- Use ONLY data from the MCP or CLI. Do not fabricate details.
- Be specific in dispositions — name resources, elements, constraints.
- The recommendation must pick one.

## Final Step
Save the completed report to the output file path above.
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
  "id": "FHIR-54803",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-54803: Text summaries for vital signs mix category and code requirements

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Erik Moll
- **labels:** VitalSigns
- **Created:** 2026-01-19T14:29:09+00:00
- **Updated:** 2026-02-27T16:36:12+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-54803

## Content
<p>There are remainders of the previous approach in the textual summaries for the OxSat profile and the BP profile:</p>

<p>OxSat has this text:</p>
<ul>
	<li>a fixed <tt>Observation.category.coding.code</tt>= <b>'2708-6'</b></li>
</ul>


<p>This should be:</p>
<ul>
	<li>a fixed <tt>Observation.<b><font color="#de350b">code</font></b>.coding.code</tt>= <b>'2708-6'</b></li>
</ul>


<p>==</p>

<p>BP has this:</p>
<ul>
	<li>a fixed <tt>Observation.category.coding.system</tt>=<b>'http ://loinc.org'</b></li>
</ul>


<p>This should be:</p>
<ul>
	<li>a fixed <tt>Observation.<b><font color="#de350b">code</font></b>.coding.system</tt>=<b>'http ://loinc.org'</b></li>
</ul>


<p>==</p>

<p>Also the text structure around these statements need to be reworked.</p>

<p>==</p>

<p>Also the other vital sign profiles should be checked for such remainders of the previous approach.</p>

<p> </p>

<p> </p>

## Snapshot
# FHIR-54803: Text summaries for vital signs mix category and code requirements

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Erik Moll  
**Work Group:** Orders & Observations  
**Specification:** FHIR Core (FHIR)  
**Labels:** VitalSigns  
**Created:** 2026-01-19  
**Updated:** 2026-02-27  

## Description

<p>There are remainders of the previous approach in the textual summaries for the OxSat profile and the BP profile:</p>

<p>OxSat has this text:</p>
<ul>
	<li>a fixed <tt>Observation.category.coding.code</tt>= <b>'2708-6'</b></li>
</ul>


<p>This should be:</p>
<ul>
	<li>a fixed <tt>Observation.<b><font color="#de350b">code</font></b>.coding.code</tt>= <b>'2708-6'</b></li>
</ul>


<p>==</p>

<p>BP has this:</p>
<ul>
	<li>a fixed <tt>Observation.category.coding.system</tt>=<b>'http ://loinc.org'</b></li>
</ul>


<p>This should be:</p>
<ul>
	<li>a fixed <tt>Observation.<b><font color="#de350b">code</font></b>.coding.system</tt>=<b>'http ://loinc.org'</b></li>
</ul>


<p>==</p>

<p>Also the text structure around these statements need to be reworked.</p>

<p>==</p>

<p>Also the other vital sign profiles should be checked for such remainders of the previous approach.</p>

<p> </p>

<p> </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-54803" (2 results)

- [jira] FHIR-54803 → [fhir] Observation.category.coding.code
  **Source:** Text summaries for vital signs mix category and code requirements
  **Type:** mentions
  **Context:** ...ummaries for the OxSat profile and the BP profile: OxSat has this text: a fixed Observation.category.coding.code = '2708-6' This should be: a fixed Observation....
  **Score:** 0.99
  **Updated:** 2026-02-27T16:36:12+00:00
- [jira] FHIR-54803 → [fhir] Observation.category.coding.system
  **Source:** Text summaries for vital signs mix category and code requirements
  **Type:** mentions
  **Context:** ...d be: a fixed Observation. code .coding.code = '2708-6' == BP has this: a fixed Observation.category.coding.system = 'http ://loinc.org' This should be: a fixed...
  **Score:** 0.99
  **Updated:** 2026-02-27T16:36:12+00:00
**Warnings:**
- Value 'FHIR-54803' is not a valid Zulip message ID

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
  "values": "vital signs text summaries category code, vital signs profile OxSat BP text summary",
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
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-54803
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| oxsat | word | 2 | 11.246 |
| 2708 | word | 2 | 9.394 |
| remainder | word | 2 | 7.991 |
| observation.category.coding.system | fhir_path | 1 | 7.283 |
| bp | word | 2 | 6.678 |
| coding | word | 6 | 6.583 |
| tt | word | 8 | 6.544 |
| observation.category.coding.code | fhir_path | 1 | 6.439 |
| mix | word | 2 | 6.183 |
| vital | word | 3 | 6.026 |
| font | word | 4 | 5.657 |
| sign | word | 3 | 5.567 |
| fixed | word | 4 | 5.355 |
| observation | fhir_path | 7 | 5.202 |
| category | word | 6 | 5.178 |
| http | word | 2 | 5.114 |
| de350b | word | 2 | 5.112 |
| ul | word | 8 | 4.710 |
| vitalsigns | word | 1 | 4.578 |
| rework | word | 1 | 4.533 |
| li | word | 8 | 4.387 |
| loinc | word | 2 | 4.382 |
| textual | word | 1 | 4.087 |
| org | word | 2 | 4.078 |
| color | word | 2 | 4.051 |
| text | word | 4 | 3.929 |
| approach | word | 2 | 3.898 |
| previous | word | 2 | 3.676 |
| summary | word | 3 | 3.658 |
| 6 | word | 2 | 3.457 |
| code | word | 7 | 3.412 |
| requirement | word | 2 | 3.054 |
| system | word | 3 | 2.990 |
| profile | word | 3 | 2.627 |
| check | word | 1 | 2.607 |
| structure | word | 1 | 2.604 |
| statement | word | 1 | 2.431 |

```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-54803 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 59.782 | jira | FHIR-54521 | Inconsistency in Observationvitalsignsbase | coding, tt, vital, sign, observation, ul, vitalsigns, li, loinc, text, summary, code, profile, statement |
| 55.808 | jira | FHIR-44798:71947 | FHIR-44798:71947 | vital, font, sign, observation, category, de350b, ul, li, loinc, color, code, profile |
| 55.060 | jira | FHIR-33613:79371 | FHIR-33613:79371 | coding, vital, sign, fixed, observation, category, ul, li, loinc, summary, code, requirement, system, profile |
| 53.648 | jira | FHIR-43960:72559 | FHIR-43960:72559 | bp, vital, sign, fixed, observation, ul, vitalsigns, li, loinc, code, profile, structure |
| 52.897 | jira | FHIR-45617 | Vital Signs Profile Semantically Ambiguous | bp, coding, vital, sign, fixed, observation, category, vitalsigns, loinc, 6, code, profile |
| 52.879 | jira | FHIR-43960:72557 | FHIR-43960:72557 | bp, vital, sign, observation, category, ul, vitalsigns, li, loinc, org, code, profile, structure |
| 52.866 | jira | FHIR-30688 | Don't require redundant data without criteria for doing so that we can apply anywhere | 2708, coding, vital, sign, fixed, observation, ul, li, loinc, 6, code, system, profile |
| 52.298 | jira | FHIR-48175 | Codes should always be defined by value AND system | coding, observation.category.coding.code, vital, sign, observation, category, ul, li, text, code, system |
| 52.212 | jira | FHIR-50705 | Breaking change in R6 VitalSigns profile undermines stability of normative Observation and threatens interoperability | tt, vital, sign, observation, category, vitalsigns, rework, li, loinc, previous, code, system, profile |
| 51.840 | jira | FHIR-31934 | Incorrect LOINC code | 2708, vital, sign, observation, category, vitalsigns, loinc, 6, code, system, profile |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>

### Turn 3

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "vital signs profile text error, Observation.category.coding.code oxygen saturation"
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 499088069 — [conformance] Validation error on USCore BMI with dataAbsentReason
- **Score:** 0.27
- **Updated:** 2025-02-11T19:57:22+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/conformance/topic/Validation%20error%20on%20USCore%20BMI%20with%20dataAbsentReason/near/499088069
- **Snippet:** ...It also derives from FHIR <b>vital</b>-sign <b>profile</b> "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/vitalsigns", And its "<b>Text</b> Summary" states...

### [zulip] 499076601 — [conformance] Validation error on USCore BMI with dataAbsentReason
- **Score:** 0.25
- **Updated:** 2025-02-11T18:47:49+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/conformance/topic/Validation%20error%20on%20USCore%20BMI%20with%20dataAbsentReason/near/499076601
- **Snippet:** ...hl7.org/CodeSystem/observation-category", "code" : "<b>vital</b>-<b>signs</b>", "display" : "<b>Vital</b> <b>Signs</b>" }], "<b>text</b>" : "<b>Vital</b> <b>Signs</b>" }], "code" : { "coding" : [{ "system" : "http://loinc.org...

### [zulip] 524770457 — [conformance] us-core pediatric-bmi-for-age validator error
- **Score:** 0.16
- **Updated:** 2025-06-18T19:26:39+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/conformance/topic/us-core%20pediatric-bmi-for-age%20validator%20error/near/524770457
- **Snippet:** ...terminology.hl7.org/CodeSystem/observation-category", "code": "<b>vital</b>-<b>signs</b>", "display": "<b>Vital</b> <b>Signs</b>" } ] } ], "code": { "coding": [ { "system": "http://loinc.org", "code": "59574...

### [zulip] 402306126 — [argonaut] Vital Signs Connectathon: Epic
- **Score:** 0.08
- **Updated:** 2023-11-15T18:42:41+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/argonaut/topic/Vital%20Signs%20Connectathon%3A%20Epic/near/402306126
- **Snippet:** ...against the specification or a <b>profile</b>." } ], "<b>text</b>": "Content invalid against the specification or a <b>profile</b>." }, "diagnostics": "Invalid unit given: Cel...

### [zulip] 436225614 — [Orders and Observation WG] Vital Signs panel - agenda topic for WGM
- **Score:** 0.07
- **Updated:** 2024-04-30T08:59:28+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Orders%20and%20Observation%20WG/topic/Vital%20Signs%20panel%20-%20agenda%20topic%20for%20WGM/near/436225614
- **Snippet:** ...any of the <b>vital</b> <b>signs</b> listed below, the implementation SHALL conform to this <b>profile</b> for the <b>vital</b> sign observation." A...

### [zulip] 445464872 — [implementers] Synthea us-core 4.0.0 load into GCP with profile validation
- **Score:** 0.01
- **Updated:** 2024-06-18T21:27:18+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Synthea%20us-core%204.0.0%20load%20into%20GCP%20with%20profile%20validation/near/445464872
- **Snippet:** ...<b>text</b>": "could not look up referenced resource" }, "diagnostics": "in http://hl7.org/fhir/us/core/StructureDefinition/us-core-<b>vital</b>-<b>signs</b>...

### [zulip] 153997950 — [finnish PHR] 500 Internal Server Error
- **Score:** 0.00
- **Updated:** 2018-09-19T06:40:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/finnish%20PHR/topic/500%20Internal%20Server%20Error/near/153997950
- **Snippet:** ...ok: { "resourceType": "Observation", "meta": { "<b>profile</b>": [ " http://phr.kanta.fi/StructureDefinition/fiphr-bodyweight-stu3 " ] }, "language": "fi", "<b>text</b>": { "status": "generated", "div": "<div...

### [zulip] 154023754 — [implementers] Hapi Fhir Composite Search Questions
- **Score:** 0.00
- **Updated:** 2018-12-07T15:35:17+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Hapi%20Fhir%20Composite%20Search%20Questions/near/154023754
- **Snippet:** ...hl7.org/fhir/observation-category ", "code": "<b>vital</b>-<b>signs</b>", "display": "<b>Vital</b> <b>Signs</b>" } ], "<b>text</b>": "<b>Vital</b> <b>Signs</b>" } ], "code": { "coding": [ { "system": " http://

... *(truncated, 4984 chars total)*
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 4

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-54803.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\OrdersObservations\\FHIR-54803.md",
  "file_text": "# FHIR-54803: Text summaries for vital signs mix category and code requirements\n\n| Field         | Value                        |\n|---------------|------------------------------|\n| **Ticket**    | [FHIR-54803](https://jira.hl7.org/browse/FHIR-54803) |\n| **Status**    | Triaged                      |\n| **Type**      | Change Request               |\n| **Priority**  | Highest                      |\n| **Work Group**| Orders & Observations        |\n| **Specification** | FHIR Core (FHIR)        |\n| **Reporter**  | Erik Moll                    |\n| **Labels**    | VitalSigns                   |\n| **Created**   | 2026-01-19                   |\n| **Updated**   | 2026-02-27                   |\n\n---\n\n## Summary\n\nThe text summaries (human-readable narrative descriptions) for certain vital signs profiles contain errors where `Observation.category` is referenced instead of `Observation.code`. Specifically:\n\n- **Oxygen Saturation (OxSat) profile:** The text summary incorrectly states a fixed `Observation.category.coding.code` = `'2708-6'`, when it should read `Observation.code.coding.code` = `'2708-6'`.\n- **Blood Pressure (BP) profile:** The text summary incorrectly states a fixed `Observation.category.coding.system` = `'http://loinc.org'`, when it should read `Observation.code.coding.system` = `'http://loinc.org'`.\n\nThe reporter also notes that the text structure around these statements needs reworking, and that all other vital sign profiles should be audited for similar remnants of a previous modeling approach.\n\n---\n\n## Details\n\n### Description\n\nThe ticket identifies leftover text from a previous approach to vital signs profiling that incorrectly attributes LOINC code/system bindings to `Observation.category` rather than `Observation.code`. These are purely errors in the human-readable text summaries \u2014 the underlying profile constraints likely already target the correct element paths. Two specific instances are called out:\n\n1. **OxSat profile** \u2014 Text says `Observation.category.coding.code` = `'2708-6'`; should say `Observation.code.coding.code` = `'2708-6'`.\n2. **BP profile** \u2014 Text says `Observation.category.coding.system` = `'http://loinc.org'`; should say `Observation.code.coding.system` = `'http://loinc.org'`.\n\nThe reporter requests:\n- Correcting these two specific errors.\n- Reworking the text structure around these statements for clarity.\n- Auditing all other vital sign profiles for similar remnants.\n\n### Comments\n\nNo comments on this ticket.\n\n---\n\n## Keywords\n\n`vital signs`, `text summary`, `OxSat`, `oxygen saturation`, `blood pressure`, `BP`, `Observation.category`, `Observation.code`, `LOINC`, `2708-6`, `profile narrative`, `VitalSigns`\n\n---\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relevance |\n|--------|-------|--------|-----------|\n| [FHIR-54521](https://jira

... *(truncated, 9064 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-54803.md with 8912 characters
```

</details>

### Turn 5

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-54803: Text summaries for vital signs mix category and code requirements

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Erik Moll
- **labels:** VitalSigns
- **Created:** 2026-01-19T14:29:09+00:00
- **Updated:** 2026-02-27T16:36:12+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-54803

## Content
<p>There are remainders of the previous approach in the textual summaries for the OxSat profile and the BP profile:</p>

<p>OxSat has this text:</p>
<ul>
	<li>a fixed <tt>Observation.category.coding.code</tt>= <b>'2708-6'</b></li>
</ul>


<p>This should be:</p>
<ul>
	<li>a fixed <tt>Observation.<b><font color="#de350b">code</font></b>.coding.code</tt>= <b>'2708-6'</b></li>
</ul>


<p>==</p>

<p>BP has this:</p>
<ul>
	<li>a fixed <tt>Observation.category.coding.system</tt>=<b>'http ://loinc.org'</b></li>
</ul>


<p>This should be:</p>
<ul>
	<li>a fixed <tt>Observation.<b><font color="#de350b">code</font></b>.coding.system</tt>=<b>'http ://loinc.org'</b></li>
</ul>


<p>==</p>

<p>Also the text structure around these statements need to be reworked.</p>

<p>==</p>

<p>Also the other vital sign profiles should be checked for such remainders of the previous approach.</p>

<p> </p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-43353: Required binding on Vital Signs components too restrictive

- **status:** Applied
- **type:** Change Request
- **priority:** Highest
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** John D.L. Nolen
- **reporter:** Pieter Edelman
- **Created:** 2023-12-07T10:47:07+00:00
- **Updated:** 2024-08-11T14:43:22+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-43353

## Content
<p>The FHIR core Vital Signs profile defines a restricted ValueSet for all the units that may be used for vital signs measurements: <a href="http://hl7.org/fhir/ValueSet/ucum-vitals-common" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/ucum-vitals-common</a>. This ValueSet is bound to <tt>Observation.value<span class="error">&#91;x&#93;</span></tt> and <tt>Observation.component.value<span class="error">&#91;x&#93;</span></tt> with a <em>required</em> binding strength in the Vital Signs base profile.</p>

<p>It makes sense to have this <em>required</em> binding on <tt>Observation.value<span class="error">&#91;x&#93;</span></tt>, as there's a clear relation to the LOINC codes used in <tt>Observation.code</tt> and the units allowed for the measurement. However, there is no such relation between the LOINC code and the <tt>Observation.components</tt> that could be used as part of the Observation.</p>

<p>By binding this ValueSet with a <em>required</em> binding to <tt>Observation.component.value<span class="error">&#91;x&#93;</span></tt>, the Vital Signs profile basically states that no other <tt>Observation.component</tt> may be used than the ones that FHIR core profile envisions.</p>

<p>For example, in the Dutch realm there's a requirement to add Korotkoff sounds to a blood pressure measurement. This particular measurement is expressed as a coded SNOMED value, not as a quantity. The <em>required</em> ValueSet binding on <tt>Observation.component.value<span class="error">&#91;x&#93;</span></tt> prohibits the use of an <tt>Observation.component</tt> for this part to <em>any</em> blood pressure measurement.</p>

<p>The binding is also not needed. There is just one case where <tt>Observation.component</tt>s are used in the core Vital Signs profiles (the Blood Pressure profile) and in this case, the units are fixed for the component slices.</p>

<p>So the question is if the binding of this ValueSet can be removed from <tt>Observation.component.value<span class="error">&#91;x&#93;</span></tt> in the Vital Signs core profile, as it is unneeded and restricts downstream extensibility.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-43960: CLONE - Clarify that the LOINC 85354-9 is used for all blood pressure measurements

- **status:** Resolved - No Change
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Not Persuasive
- **assignee:** Marti Velezis
- **reporter:** Eric Haas
- **labels:** OO, OOMainCall, Ready-to-Discuss, VitalSigns
- **Created:** 2024-01-20T00:49:06+00:00
- **Updated:** 2025-10-31T14:20:43+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-43960

## Content
<p>To avoid confusion from the reader, explain that the average blood pressure (or other types of blood pressure measurements) is treated as a further refinement of the blood pressure profile and, therefore use the LOINC 85354-9 is used for all blood pressure measurements and additional LOINC codings to represent the types of blood pressure measurement such as average value.   this is an inherited constraint from the FHIR Core Blood Pressure Profile <a href="https://hl7.org/fhir/R4/observation.html" class="external-link" target="_blank" rel="nofollow noopener">https://hl7.org/fhir/R4/observation.html</a><br/>
 </p>
<blockquote><p>implementations use this Resource when expressing the profile-specific concepts as structured data, they SHALL conform to the following profiles:</p></blockquote>
<p> <br/>
(edit final version)</p>

<p> </p>

<p>Discussed this issue in <a href="https://confluence.hl7.org/display/WGB/WGM+Information+and+Agendas+-+January+2024+Virtual" class="external-link" target="_blank" rel="nofollow noopener"> January 2024 Virtual WGM  Tuesday Q3 Call. </a></p>

<p>in relation to </p>
<ol>
	<li><a href="http://jira.hl7.org/browse/FHIR-43538" class="external-link" rel="nofollow">FHIR-43538</a> Confusing use of Observation.code values (hbuitendijk)</li>
</ol>


<p>Which include Hans Buitendijk and Grahame Grieve. Summarizing:</p>
<ol>
	<li>Not clear in the Profile documentation if the "magic codes" include component codes</li>
	<li>Currently, the FHIR validator enforces that rule clients get average BP measurements when they use the BP "magic code".  There was disagreement on whether they should.</li>
	<li>Some systems may actually calculate average blood pressure on the fly when blood pressure are fetched. ( unclear on context )</li>
</ol>



<p>Cloned tracker from US Core <a href="https://jira.hl7.org/browse/FHIR-43959" title="Clarify that the LOINC 85354-9 is used for all blood pressure measurements" class="issue-link" data-issue-key="FHIR-43959"><del>FHIR-43959</del></a></p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-43538: Confusing use of Observation.code values

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Cross-Group Projects
- **specification:** US Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Hans Buitendijk
- **labels:** BAM-Reviewed, EH-Review, Vitals
- **Created:** 2024-01-05T21:54:26+00:00
- **Updated:** 2024-05-08T19:23:08+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-43538

## Content
<p>The tables provides a slice for uscore-avg-bp to state the average BP panel code (96607-7).  However, it still requires the use of 85354-9 as well which is creating some challenges:</p>
<ul>
	<li>These two codes are not equivalent, so should not be used within the same instance of Observation.code</li>
	<li>Arguing that 85354-9 includes 8478-0 does not work either as then uscore-avg-bp should have be set to that, not 96607-7</li>
	<li>Since they need to be equivalent, the consumer of this resource may just read 85354-9 and think they know what they have, but they don't and it totally different.</li>
</ul>


<p>There is the challenge that this profile is a profile on the Blood Pressure Profile that requires the use of 85354-9.  As that would at least be confusing, if not actually incorrect, suggest to base Average Blood Pressure Profile directly on the Vital Signs Profile thus removing the need to include 85354-9 altogether and avoid the contradiction and potential for misinterpretation.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-24876: LOINC magic code is unclear

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Devices
- **specification:** Personal Healthcare Devices (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Lloyd McKenzie
- **labels:** PHDIG_BV2024.01
- **Created:** 2019-09-30T04:45:12+00:00
- **Updated:** 2024-10-18T14:39:38+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-24876

## Content
<p>The term "LOINC magic code" is not sufficient here.  Need something similar to the following language:</p>

<p>         The HL7 core specification has defined <span class="error">&#91;profiles&#93;</span> for a number of specific vital signs.  These profiles define specific LOINC codes that SHALL be present as Observation.code or Observation.component.code values.  They also mandate specific structures for each type of Observation (e.g. blood pressures cannot have an Observation.value and must declare systolic and diastolic as component values). They also mandate the unit of measure in which the observation values must be expressed.</p>

<p>         In addition to complying with the profiles listed here, systems SHALL comply with the base HL7 vital signs profiles if conveying one of the concepts covered by a mandatory profile.</p>

```

</details>


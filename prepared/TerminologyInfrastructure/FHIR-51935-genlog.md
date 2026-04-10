# Session Log: FHIR-51935

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-51935.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51935` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 22:49:26 UTC |
| **Duration** | 126s |
| **Total Tool Calls** | 17 |
| **Total Tokens** | 280,304 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51935
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51935.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51935", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51935", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51935", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51935.md
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
  "id": "FHIR-51935",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51935: Coding omitted from required binding discussion, etc.

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** TEXTONLY
- **Created:** 2025-08-25T15:31:27+00:00
- **Updated:** 2026-04-09T20:47:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51935

## Content
<p>The discussion of required bindings discusses CodeableConcept and code, but omits Coding (except as part of CodeableConcept). The rules for required binding on Coding should be included.</p>

<p>===</p>

<p>The following statement is unclear as to whether it is scoped to only CodeableConcepts or to code/Coding as well, and whether this applies to the repeated Coding elements within a CodeableConcept:</p>
<blockquote><p>If a required binding is applied to an element with maximum cardinality &gt; 1, the binding applies to all the elements.</p></blockquote>
<p>(Also, I dislike use of "&gt; 1" in the midst of narrative.)</p>

<p>Suggest changing to "If a required binding is applied to an element of type CodeableConcept with maximum cardinality greater than 1, the binding applies to each repetition of the element."</p>

<p>Similar text occurs in other bindings, review and update if necessary.</p>

<p>===</p>

<p> </p>
<blockquote><p>One of the Coding values SHALL be from the specified value set</p></blockquote>
<p>It is unclear whether {{code }}and {{system }}must both be specified in order for the value to meet this requirement; is supplying only {{code }}sufficient? Are there circumstances when a {{version }}must also be specified?</p>

<p>This is also unclear for other binding strengths.</p>

## Comments (4)

### carmela_couderc — 2026-03-23T22:19:46+00:00
<p>Discussed on the 2026-03-23 TI tracker call.</p>

<p>Attendees agree consistency is good. We can use the extensible section as a template and post to Zulip - vote on a future call. </p>

### carmela_couderc — 2025-11-20T17:01:02+00:00
<p>Good question - for some reason the process for triaging tickets broke at some point this fall. I manage the TI tickets, but not until they are triaged.  I'm looking into what happened, and trying to get all submitted tickets addressed - especially if the change request is non-substantive or provides a clarification. </p>

<p> </p>

### esilver — 2025-11-20T16:24:25+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=carmela_couderc" class="user-hover" rel="carmela_couderc">Carmela A. Couderc</a>, how is it that a ticket submitted in August only got triaged in November, too late to make the R6 cutoff?</p>

### esilver — 2025-08-26T15:01:18+00:00
<p>Also, that required bindings can't be satisfied with use of CodeableConcept.text.</p>


## Snapshot
# FHIR-51935: Coding omitted from required binding discussion, etc.

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Persuasive  
**Assignee:** Unassigned  
**Reporter:** Elliot Silver  
**Work Group:** Terminology Infrastructure  
**Specification:** FHIR Core (FHIR)  
**Labels:** TEXTONLY  
**Created:** 2025-08-25  
**Updated:** 2026-04-09  
**Resolved:** 2025-12-01  

## Description

<p>The discussion of required bindings discusses CodeableConcept and code, but omits Coding (except as part of CodeableConcept). The rules for required binding on Coding should be included.</p>

<p>===</p>

<p>The following statement is unclear as to whether it is scoped to only CodeableConcepts or to code/Coding as well, and whether this applies to the repeated Coding elements within a CodeableConcept:</p>
<blockquote><p>If a required binding is applied to an element with maximum cardinality &gt; 1, the binding applies to all the elements.</p></blockquote>
<p>(Also, I dislike use of "&gt; 1" in the midst of narrative.)</p>

<p>Sugges

... *(truncated, 6042 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51935".
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

Now let me search for related Zulip discussions and Jira tickets on the topic of required bindings and Coding.

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "required binding Coding CodeableConcept terminology",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 483755767 — [implementers] Where to put terminology binding for coded data types
- **Score:** 0.14
- **Updated:** 2024-11-21T17:50:28+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Where%20to%20put%20terminology%20binding%20for%20coded%20data%20types/near/483755767
- **Snippet:** ...A <b>required</b> <b>binding</b> says "This element cannot be present unless there is a <b>coding</b> present drawn from the value set...

### [zulip] 257448845 — [terminology] Codeable Concept Required Binding and Text element
- **Score:** 0.02
- **Updated:** 2021-10-13T22:27:02+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Codeable%20Concept%20Required%20Binding%20and%20Text%20element/near/257448845
- **Snippet:** ...<b>Required</b> <b>binding</b> The following rules apply when <b>required</b> bindings are used with the <b>CodeableConcept</b> data type: at least one <b>Coding</b>...

### [zulip] 358196983 — [IG creation] Vocab error in extenstion
- **Score:** 0.02
- **Updated:** 2023-05-14T03:16:09+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IG%20creation/topic/Vocab%20error%20in%20extenstion/near/358196983
- **Snippet:** ...on a <b>terminology</b> when used in an extension. When the same <b>binding</b> it used in a defined <b>codeableConcept</b> just the...

### [zulip] 153997981 — [australia] AU base terminology binding
- **Score:** 0.01
- **Updated:** 2018-09-19T07:18:46+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/australia/topic/AU%20base%20terminology%20binding/near/153997981
- **Snippet:** ...<b>binding</b> strength question - on further discussion I think we can maintain <b>Required</b> strength on all of the <b>CodeableConcept</b>.<b>coding</b> slices...

### [zulip] 178964912 — [terminology] Multiple bindings
- **Score:** 0.01
- **Updated:** 2019-10-24T15:39:38+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Multiple%20bindings/near/178964912
- **Snippet:** By my reading, a <b>required</b> <b>binding</b> on a <b>CodeableConcept</b> says that one, but not necessarily all, of the <b>Coding</b> values...

### [zulip] 215481358 — [CARIN IG for Blue Button®] v0.1.9 published to CI Build
- **Score:** 0.00
- **Updated:** 2020-11-03T16:58:27+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/CARIN%20IG%20for%20Blue%20Button%C2%AE/topic/v0.1.9%20published%20to%20CI%20Build/near/215481358
- **Snippet:** ...<b>CodeableConcept</b> Specifies the type of claim. (e.g., inpatient insitutional, outpatient institutional, physician, etc.) (16) <b>Binding</b>: ClaimTypeCodes (<b>required</b>) <b>Required</b> Pattern...

### [zulip] 218750910 — [CARIN IG for Blue Button®] EOB.diagnosis.type
- **Score:** 0.00
- **Updated:** 2020-12-03T20:37:34+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/CARIN%20IG%20for%20Blue%20Button%C2%AE/topic/EOB.diagnosis.type/near/218750910
- **Snippet:** ...type S 1..1 <b>CodeableConcept</b> Timing or nature of the diagnosis <b>Binding</b>: C4BB Claim Inpatient Institutional Diagnosis Type (<b>required</b>) This...

### [zulip] 153872006 — [implementers] How should valueset bindings be profiled in codeableConcept?
- **Score:** 0.00
- **Updated:** 2017-02-16T14:43:46+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/How%20should%20valueset%20bindings%20be%20profiled%20in%20codeableConcept%3F/near/153872006
- **Snippet:** ...<b>Binding</b> to Observation.code.<b>coding</b>.code doesn't make sense as that won't control the code system. <b>Binding</b> Observation...

### [zulip] 197552605 — [connectathon mgmt] Terminology Services Track
- **Score:** 0.00
- **Updated:** 2020-05-14T13:22:46+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/connectathon%20mgmt/topic/Terminology%20Services%20Track/near/197552605
- **Snippet:** ...The best you could do is two optional slices on <b>CodeableConcept</b>.<b>

... *(truncated, 4657 chars total)*
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [jira] FHIR-51935 — Coding omitted from required binding discussion, etc.
- **Score:** 1.00
- **Updated:** 2026-04-09T15:47:21-05:00
- **URL:** https://jira.hl7.org/browse/FHIR-51935
- **Snippet:** The <b>discussion</b> of <b>required</b> bindings discusses CodeableConcept and code, but omits <b>Coding</b> (except as part of CodeableConcept). The rules for...


```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-51935 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 50.186 | jira | FHIR-51975 | Clarify language about required bindings in relation to CodeableConcept | coding, binding, codeableconcept, codeableconcepts, textonly, apply, require, strength, element, code, rule, statement |
| 48.027 | jira | FHIR-17480:32469 | FHIR-17480:32469 | coding, maximum, binding, codeableconcept, apply, require, repetition, cardinality, gt, strength, element, applied, code, rule, 1, value, discuss |
| 46.890 | jira | FHIR-32857 | For Condition, US Core is binding *all* repetitions of category instead of slicing | maximum, binding, apply, require, repetition, cardinality, strength, element, applied, extensible, code, 1 |
| 46.744 | jira | FHIR-31381 | US Core general guidance about missing data for coded data elements need clarification | coding, omit, binding, codeableconcept, require, cardinality, gt, strength, element, section, extensible, code, rule, 1, order |
| 46.322 | jira | FHIR-40249 | Preferred Binding Strength - Guidance for code data type | coding, binding, codeableconcept, textonly, similar, strength, section, datatype, code, value, included |
| 46.293 | jira | FHIR-38962 | Aren't the rules defined for the code datatype applicable for the CodeableConcept datatype as well? | coding, binding, codeableconcept, textonly, apply, require, element, datatype, code, rule |
| 43.425 | jira | FHIR-54588:80721 | FHIR-54588:80721 | binding, apply, require, discussion, ti, strength, improve, extensible, separate, tracker, 1, value, content, discuss |
| 42.942 | jira | FHIR-34626 | Add further clarification between slicing a binding (4.1.0) vs using extensible binding (4.0.0) | maximum, binding, apply, require, repetition, cardinality, strength, element, section, applied, extensible, code, rule, 1 |
| 42.261 | jira | FHIR-18038 | Change the binding strength of administrative gender to extensible | coding, binding, codeableconcept, require, similar, strength, datatype, extensible, code, scope, value, discuss |
| 41.663 | jira | FHIR-9550 | Binding for CodeableConcepts without the Coding component | coding, binding, codeableconcept, codeableconcepts, require, strength, element, datatype, code, value, requirement |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-51935
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| coding | word | 7 | 6.808 |
| omit | word | 3 | 6.780 |
| maximum | word | 2 | 6.231 |
| binding | word | 12 | 6.037 |
| codeableconcept | word | 4 | 5.895 |
| dislike | word | 1 | 5.780 |
| blockquote | word | 4 | 5.757 |
| unclear | word | 3 | 5.508 |
| codeableconcepts | word | 1 | 4.788 |
| attendees | word | 1 | 4.565 |
| textonly | word | 1 | 4.521 |
| apply | word | 3 | 4.246 |
| repeated | word | 1 | 4.086 |
| require | word | 7 | 4.001 |
| repetition | word | 1 | 3.991 |
| similar | word | 2 | 3.979 |
| enhance | word | 1 | 3.938 |
| circumstance/circumstances | word | 1 | 3.884 |
| cardinality | word | 2 | 3.830 |
| discussion | word | 3 | 3.817 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51935.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-51935.md",
  "file_text": "# FHIR-51935: Coding omitted from required binding discussion, etc.\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-51935](https://jira.hl7.org/browse/FHIR-51935) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Persuasive |\n| **Specification** | FHIR Core (FHIR) |\n| **Work Group** | Terminology Infrastructure |\n| **Reporter** | Elliot Silver |\n| **Assignee** | Unassigned |\n| **Labels** | TEXTONLY |\n| **Created** | 2025-08-25 |\n| **Updated** | 2026-04-09 |\n\nElliot Silver reports that the FHIR spec's [required binding section](https://hl7.org/fhir/terminologies.html#required) discusses the `CodeableConcept` and `code` datatypes but omits the `Coding` datatype (except as a component of CodeableConcept). The ticket raises three related issues:\n\n1. **Missing Coding coverage:** The required binding rules do not address `Coding` as a standalone datatype.\n2. **Ambiguous cardinality statement:** The statement _\"If a required binding is applied to an element with maximum cardinality > 1, the binding applies to all the elements\"_ is unclear about whether it applies only to CodeableConcept or also to code/Coding, and whether \"all the elements\" refers to repetitions of the element or to repeated Coding elements within a CodeableConcept.\n3. **Unclear system/code/version requirements:** It is not specified whether both `system` and `code` must be present to satisfy the binding, or whether `version` is sometimes required. This ambiguity exists across binding strengths.\n\nThe reporter also notes (in comments) that the section should clarify that required bindings cannot be satisfied solely by `CodeableConcept.text`.\n\n## Resolution Description\n\n> Replace / enhance the content in the required binding section with something similar to what is in the extensible binding section where each datatype is a separate entry and there are specifics provided.\n>\n> TI tracker call attendees agree that the information in this section could be improved.\n\n## Keywords\n\n`binding`, `Coding`, `CodeableConcept`, `required`, `cardinality`, `datatype`, `code`, `extensible`, `TEXTONLY`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relationship |\n|--------|-------|--------|------------|-------------|\n| [FHIR-51975](https://jira.hl7.org/browse/FHIR-51975) | Clarify language about required bindings in relation to CodeableConcept | Resolved \u2013 change required | Persuasive | Same work group; addresses confusion about whether required binding restricts additional codings within a CodeableConcept. Very closely related \u2014 both seek to clarify the required binding section. |\n| [FHIR-38962](https://jira.hl7.org/browse/FHIR-38962) | Aren't the rules defined for the code datatype applicable for the CodeableConcept datatype as well? | Publis

... *(truncated, 10053 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51935.md with 9871 characters
```

</details>


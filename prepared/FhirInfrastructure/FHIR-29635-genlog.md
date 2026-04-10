# Session Log: FHIR-29635

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-29635.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29635` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:25:48 UTC |
| **Duration** | 101s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 263,988 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29635
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29635.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29635", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29635", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29635", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Title, metadata, Summary, Details, Keywords, Related Zulip, Related GitHub, three Proposed Dispositions (A: Accept, B: Alternative, C: Decline), and Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29635.md
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
  "id": "FHIR-29635",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29635: Add syntax to easily set "unit" on a Quantity

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** Shorthand (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Nick Freiter
- **Created:** 2020-10-30T15:55:39+00:00
- **Updated:** 2020-11-03T14:44:44+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29635

## Content
<p>FSH supports an easy syntax for specifying a Quantity when the units are taken from UCUM:</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java">
* valueQuantity = 155.0 <span class="code-quote">'[lb_av]'</span></pre>
</div></div>
<p>But there is no way to specify the `unit` field when doing this. It might make sense to support a syntax like:</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java">
* valueQuantity = 155.0 <span class="code-quote">'[lb_av]'</span> <span class="code-quote">"lb"</span></pre>
</div></div>
<p>where the <tt>valueQuantity.unit</tt> would then get set to "lb". The <tt>unit</tt> is meant to be a human readable value, and there is plenty of precedent for setting human readable values as strings at the end of assignments, so I don't think users would find this a confusing addition.</p>

## Snapshot
# FHIR-29635: Add syntax to easily set "unit" on a Quantity

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Nick Freiter  
**Work Group:** FHIR Infrastructure  
**Specification:** Shorthand (FHIR)  
**Created:** 2020-10-30  
**Updated:** 2020-11-03  

## Description

<p>FSH supports an easy syntax for specifying a Quantity when the units are taken from UCUM:</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java">
* valueQuantity = 155.0 <span class="code-quote">'[lb_av]'</span></pre>
</div></div>
<p>But there is no way to specify the `unit` field when doing this. It might make sense to support a syntax like:</p>
<div class="code panel" style="border-width: 1px;"><div class="codeContent panelContent">
<pre class="code-java">
* valueQuantity = 155.0 <span class="code-quote">'[lb_av]'</span> <span class="code-quote">"lb"</span></pre>
</div></div>
<p>where the <tt>valueQuantity.unit</tt> would then get set to "lb". The <tt>unit</tt> is meant to be a human readable value, and there is plenty of precedent for setting human readable values as strings at the end of assignments, so I don't think users would find this a confusing addition.</p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29635".
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

Now let me check the UCUM annotations Zulip thread and fetch keywords for the ticket.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "limit": 15,
  "stream": "shorthand",
  "topic": "UCUM Codes that contain human readable annotations"
}
```

**Result:**
```
# shorthand > UCUM Codes that contain human readable annotations

**Messages:** 15
**First message:** 2024-06-20 12:38:56+00:00
**Last message:** 2024-06-21 16:20:39+00:00
**Participants:** Richard Langford, Chris Moesel, Lloyd McKenzie, Elliot Silver, John Silva, Rik Smithies, John Moehrke

## Messages

### Richard Langford — 2024-06-20 12:38:56+00:00
Hi all, Please see below warnings. image.png If I am understanding this warning correctly, we should not define UCUM codings? -> * valueQuantity = $UCUM_UNIT#{copies}/mL Or is this warning trying to say that when defining a UCUM coding where the code uses the reserved FSH keywords '{ }' then rather dont define the UCUM coding? Please can you help me understand? Thanks

### Chris Moesel — 2024-06-20 13:01:09+00:00
This warning is coming from the IG Publisher (not SUSHI), so it's not strictly related to FSH. I believe the concern that the warning raises is that anything in { } is considered an annotation in UCUM. These annotations are not meaningful for computation; they're more like comments for humans. When doing comparisons on UCUM units, {copies} will be treated as equivalent to {anything-else-in-curly-braces} as well as to 1 . For this reason, it's recommended to use 1 in its place in the quantity code and to put the annotation in the unit (which is intended for humans). In your case, this might look like: * valueQuantity = $UCUM_UNIT#1/mL "{copies}/mL" Since this is UCUM, however, you can use FSH's special syntax for UCUM (since it is so common), which is just to put the units in single-quotes and it will be assumed to be UCUM. E.g., * valueQuantity = '1/mL' "{copies}/mL" That said, avoiding annotations in the code is considered a warning / best practice suggestion, so it's up to you whether or not you want to follow it. There is more discussion about this in another thread here: https://chat.fhir.org/#narrow/stream/179252-IG-creation/topic/source.20of.20new.20warning.20popping.20up/near/392030710

### Richard Langford — 2024-06-20 13:04:45+00:00
this is very helpful, thanks @Chris Moesel

### Lloyd McKenzie — 2024-06-20 14:38:02+00:00
The issue is twofold: The content of annotations is not standardized, which creates a high likelihood of computable non-interoperability for systems that treat the code as a string Annotations are ignored when checking for computable equivalence by more sophisticated systems - so "{copies}/mL" is considered equivalent to "1/mL". I.e. the annotation isn't doing anything useful. Because we have an ability to distinguish "what to show humans" from "what to compute on" in FHIR, the recommendation is to use that capability.

### Chris Moesel — 2024-06-20 14:54:07+00:00
I did just notice, however, that you're working in a profile, not an instance. So implementers will need to conform to whatever you put in that Quantity's pattern in the profile. I think that requiring a specific Quantity system and code is fairly common, but I'm not sure what the best practice is regarding fixing the human-readable unit . @Lloyd McKenzie - is fixing a Quantity's unit in a profile discouraged (similar to a Coding's display )? Or is it considered to be a reasonable approach?

### Elliot Silver — 2024-06-20 15:44:14+00:00
Chris Moesel said : Lloyd McKenzie - is fixing a Quantity's unit in a profile discouraged (similar to a Coding's display )? Or is it considered to be a reasonable approach? I suspect that fixing it should be discouraged, especially in multilingual environments. Which for that matter, brings up another problem with annotations: is it {copies}/mL or {copias}/mL or {Kopien}/mL ?

### Richard Langford — 2024-06-20 16:16:12+00:00
Chris Moesel said : I did just notice, however, that you're working in a profile, not an instance. So implementers will need to conform to whatever you put in that Quantity's pattern in the profile. I think that requiring a specific Quantity system and code is fairly common, but I'm not sure what the be

... *(truncated, 7013 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-29635
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| lb | word | 4 | 12.147 |
| av | word | 2 | 8.720 |
| 155 | word | 2 | 8.398 |
| unit | word | 7 | 8.157 |
| valuequantity | word | 3 | 7.900 |
| syntax | word | 4 | 7.375 |
| quantity | word | 4 | 6.692 |
| quote | word | 3 | 6.666 |
| div | word | 8 | 6.660 |
| codecontent | word | 2 | 5.696 |
| readable | word | 2 | 5.597 |
| easily | word | 2 | 5.540 |
| panelcontent | word | 2 | 5.496 |
| 1px | word | 2 | 5.485 |
| java | word | 2 | 5.416 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29635.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-29635.md",
  "file_text": "# FHIR-29635: Add syntax to easily set \"unit\" on a Quantity\n\n## Metadata\n| Field          | Value                                                        |\n| -------------- | ------------------------------------------------------------ |\n| **Ticket**     | [FHIR-29635](https://jira.hl7.org/browse/FHIR-29635)        |\n| **Status**     | Triaged                                                      |\n| **Type**       | Change Request                                               |\n| **Priority**   | Medium                                                       |\n| **Resolution** | Unresolved                                                   |\n| **Reporter**   | Nick Freiter                                                 |\n| **Assignee**   | Unassigned                                                   |\n| **Work Group** | FHIR Infrastructure                                          |\n| **Spec**       | Shorthand (FHIR)                                             |\n| **Created**    | 2020-10-30                                                   |\n| **Updated**    | 2020-11-03                                                   |\n\n## Summary\n\nThis ticket requests adding FSH syntax to set the human-readable `Quantity.unit` field when using the UCUM shortcut notation for Quantity assignments. Currently, the FSH Quantity shortcut syntax (`* valueQuantity = 155.0 '[lb_av]'`) sets the `value`, `system`, and `code` fields but provides no way to specify the `unit` (display) string. The proposal is to allow an optional quoted string after the UCUM code:\n\n```fsh\n* valueQuantity = 155.0 '[lb_av]' \"lb\"\n```\n\nThis would set `valueQuantity.unit` to `\"lb\"`. The reporter argues this is intuitive since FSH already uses trailing quoted strings for human-readable display values in other contexts.\n\n## Details\n\n**Background:** FHIR's `Quantity` datatype has both a computable `code` (e.g., UCUM code `[lb_av]`) and a human-readable `unit` string (e.g., `\"lb\"`). FSH provides a convenient shorthand for setting UCUM-based quantities using single-quoted codes, but prior to this request the `unit` field could only be set via a separate assignment rule (e.g., `* valueQuantity.unit = \"lb\"`).\n\n**Implementation Status:** This feature was **already implemented** in SUSHI 1.1.0 (released January 2021), approximately two months after this ticket was filed. The SUSHI 1.1.0 release notes explicitly state: _\"Extends Quantity syntax to include unit string (proposed FSH STU2 feature).\"_ The syntax is now in widespread use in the FSH community, as evidenced by recent Zulip discussions (2024) demonstrating usage such as `* valueQuantity = '1/mL' \"{copies}/mL\"`.\n\n**Current Spec Status:** Although the feature has been implemented in SUSHI and is in active use, this Jira ticket remains in \"Triaged\" status and has never been formally resolved. Th

... *(truncated, 7736 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29635.md with 7568 characters
```

</details>


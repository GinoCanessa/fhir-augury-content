# Session Log: FHIR-49525

**Phase:** prepared
**Work Group:** ImplementableTechnologySpecifications
**Source File:** `prepared/ImplementableTechnologySpecifications/FHIR-49525.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-49525` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:58:32 UTC |
| **Duration** | 112s |
| **Total Tool Calls** | 11 |
| **Total Tokens** | 282,994 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-49525
## Work Group: Implementable Technology Specifications
## Output File: C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-49525.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-49525", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-49525", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-49525", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-49525.md
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
  "id": "FHIR-49525",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-49525: Quantity math and unit conversion

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **labels:** Discuss
- **Created:** 2025-01-20T11:13:20+00:00
- **Updated:** 2026-03-30T05:22:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-49525

## Content
<p>The specification is silent on the unit that is the result of a calculation.<br/>
The result of '1 'kg' + 100 'g' might be 1.100 'kg' or 1100 'g'. I think the implementation should be free to choose the preferred approach.</p>

<p>The specification should make this more clear and indicate that when a specific unit ('kg' instead of 'g') is needed, toQuantity should be used.</p>

## Comments (7)

### brian.postlethwaite — 2026-02-26T05:15:23+00:00
<p>More discussion over here:</p>

<p><a href="https://chat.fhir.org/#narrow/channel/179266-fhirpath/topic/FHIR-49525.20Quantity.20Math/with/575933717" class="external-link" target="_blank" rel="nofollow noopener">#fhirpath &gt; FHIR-49525 Quantity Math</a></p>

### bryn.rhodes — 2025-11-30T20:48:37+00:00
<p>Propose that in <a href="https://build.fhir.org/ig/HL7/FHIRPath/#comparison" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/FHIRPath/#comparison</a> we change the sentence:</p>

<p>&gt; The comparison will be made using the most granular unit of either input.</p>

<p>to:</p>

<p>&gt; Implementations that support UCUM unit conversion SHALL perform the comparison by converting the arguments to common UCUM <span class="error">&#91;base units&#93;</span>(<a href="https://ucum.org/ucum#section-Base-Units" class="external-link" target="_blank" rel="nofollow noopener">https://ucum.org/ucum#section-Base-Units</a>). Implementers can refer to the <span class="error">&#91;NLM Base Unit Conversion&#93;</span>(<a href="https://ucum.nlm.nih.gov/ucum-service.html#toBaseUnits" class="external-link" target="_blank" rel="nofollow noopener">https://ucum.nlm.nih.gov/ucum-service.html#toBaseUnits</a>) service for more information.</p>

<p>And in <a href="https://build.fhir.org/ig/HL7/FHIRPath/#math-1" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/FHIRPath/#math-1</a></p>

<p>&gt; The unit of the result will be the most granular unit of either input.</p>

<p>To: Implementations that support UCUM unit conversion SHALL perform the operation by converting the arguments to common UCUM <span class="error">&#91;base units&#93;</span>(<a href="https://ucum.org/ucum#section-Base-Units" class="external-link" target="_blank" rel="nofollow noopener">https://ucum.org/ucum#section-Base-Units</a>). Implementers can refer to the <span class="error">&#91;NLM Base Unit Conversion&#93;</span>(<a href="https://ucum.nlm.nih.gov/ucum-service.html#toBaseUnits" class="external-link" target="_blank" rel="nofollow noopener">https://ucum.nlm.nih.gov/ucum-service.html#toBaseUnits</a>) service for more information.</p>


### bvdh — 2025-09-23T14:02:07+00:00
<blockquote><p>BrianPos: The text in section 6.6 Math that went to ballot contains this:</p>

<p><em>"The unit of the result will be the most granular unit of either input."</em></p>

<p>Which appears to be quite specific to your question?<br/>
 </p></blockquote>

<p>yes that would do it</p>

### bvdh — 2025-08-27T08:39:10+00:00
<blockquote><p>BrianPos: The text in section 6.6 Math that went to ballot contains this:</p>

<p><em>"The unit of the result will be the most granular unit of either input."</em></p>

<p>Which appears to be quite specific to your question?</p></blockquote>

<p>I missed that - the language is directive but not formal - can we change it to:</p>
<blockquote><p><em>"The unit of the result SHALL be the most granular unit of either input."</em>

... *(truncated, 12717 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-49525" (9 results)

- [zulip] 583799780 → [jira] FHIR-49525
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** I thought we had already addressed this in the resolution for this comment: https://jira.hl7.org/browse/FHIR-49525 , which is one of the ones that is suppos...
  **Score:** 1.00
  **Updated:** 2026-04-06T13:10:43+00:00
- [zulip] 583802686 → [jira] FHIR-49525
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** ... Bryn, I didn't read that tracker. I like the intended resolution from <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a> "convert both units to the...
  **Score:** 0.88
  **Updated:** 2026-04-06T13:33:41+00:00
- [zulip] 575933717 → [jira] FHIR-49525
  **Source:** [fhirpath] FHIR-49525 Quantity Math
  **Type:** mentions
  **Context:** ...says if precision is a concern, use round() to a desired precision. <p><a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a> refers only to quantity ba...
  **Score:** 0.73
  **Updated:** 2026-02-26T05:14:45+00:00
- [zulip] 583183656 → [jira] FHIR-49525
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** ...-2026-03-quantity-preview/</a> with green highlights...<br> Check that <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a>, <a href="http://jira.hl7....
  **Score:** 0.64
  **Updated:** 2026-04-02T05:25:48+00:00
- [zulip] 575935808 → [jira] FHIR-49525
  **Source:** [fhirpath] Definite durations above seconds in date time arithmetic
  **Type:** mentions
  **Context:** ...250</a> <a href="http://jira.hl7.org/browse/FHIR-53249">FHIR-53249</a> <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a></p> <p>If anyone is intere...
  **Score:** 0.58
  **Updated:** 2026-02-26T05:34:10+00:00
- [zulip] 583824030 → [jira] FHIR-49525
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** ...is is "what precision should be preserved?".    There is an example in <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a> that shows </p> <blockquot...
  **Score:** 0.44
  **Updated:** 2026-04-06T15:49:29+00:00
- [zulip] 575697272 → [jira] FHIR-49525
  **Source:** [fhirpath] ITS Conference Call
  **Type:** mentions
  **Context:** ...250</a> <a href="http://jira.hl7.org/browse/FHIR-53249">FHIR-53249</a> <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a></p> <p>But before we jump ...
  **Score:** 0.36
  **Updated:** 2026-02-25T06:02:36+00:00
- [zulip] 545155832 → [jira] FHIR-49525
  **Source:** [fhirpath] ITS Conference Call
  **Type:** mentions
  **Context:** ...-49518</a> Please specify expected behavior and not implementation<br> <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a> Quantity math and unit con...
  **Score:** 0.26
  **Updated:** 2025-10-16T02:19:52+00:00
- [zulip] 570364225 → [jira] FHIR-49525
  **Source:** [fhirpath] Block vote for fhirpath
  **Type:** mentions
  **Context:** ...ntion" data-user-id="366686">@Jing Tang</span>)</em><br> <em>(removed) <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a> <strong>Not Persuasive wit...
  **Score:** 0.00
  **Updated:** 2026-01-27T16:19:28+00:00
**Warnings:**
- Value 'FHIR-49525' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 582894006 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 1.00
- **Updated:** 2026-03-31T20:46:16+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582894006
- **Snippet:** Essentially yes.

### [zulip] 582972953 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.89
- **Updated:** 2026-04-01T08:13:43+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582972953
- **Snippet:** Lol, that works!

### [zulip] 582886935 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.78
- **Updated:** 2026-03-31T20:03:23+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582886935
- **Snippet:** (1.toString() + ' \'cm\'').toQuantity() ?

### [zulip] 582887560 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.67
- **Updated:** 2026-03-31T20:07:03+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582887560
- **Snippet:** Quantity {code: "cm", value: 1} ?

### [zulip] 582887636 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.57
- **Updated:** 2026-03-31T20:07:26+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582887636
- **Snippet:** With the new instance creator stuf?

### [zulip] 582886585 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.57
- **Updated:** 2026-03-31T20:01:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582886585
- **Snippet:** 1.toQuantity('cm') should be empty.

### [zulip] 582887706 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.18
- **Updated:** 2026-03-31T20:07:57+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582887706
- **Snippet:** So I guess not a fan of my proposed shortcut.

### [zulip] 576251752 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.00
- **Updated:** 2026-02-27T12:47:32+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/576251752
- **Snippet:** I suspect that most UCUM libraries can easily convert to base units.

### [zulip] 582875329 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.00
- **Updated:** 2026-03-31T18:58:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582875329
- **Snippet:** 1 cm + 1 should be an error. The units are not commensurate.

### [zulip] 582894075 — [fhirpath] FHIR-49525 Quantity Math
- **Score:** 0.00
- **Updated:** 2026-03-31T20:46:47+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/FHIR-49525%20Quantity%20Math/near/582894075
- **Snippet:** Hadn't thought of your suggested use of the instance creation thing.


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-49525.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\ImplementableTechnologySpecifications\\FHIR-49525.md",
  "file_text": "# FHIR-49525: Quantity math and unit conversion\n\n## Ticket Summary\n\n| Field          | Value                                    |\n|----------------|------------------------------------------|\n| **Key**        | [FHIR-49525](https://jira.hl7.org/browse/FHIR-49525) |\n| **Type**       | Change Request                           |\n| **Priority**   | Highest                                  |\n| **Status**     | Triaged                                  |\n| **Resolution** | Not Persuasive with Modification         |\n| **Specification** | FHIRPath (FHIR)                       |\n| **Work Group** | Implementable Technology Specifications  |\n| **Reporter**   | Bas van den Heuvel (bvdh)                |\n| **Assignee**   | Unassigned                               |\n| **Labels**     | Discuss                                  |\n| **Created**    | 2025-01-20                               |\n| **Updated**    | 2026-03-30                               |\n| **Resolved**   | 2025-10-22                               |\n\n## Problem Statement\n\nThe FHIRPath specification does not clearly define what unit the result of a Quantity-based arithmetic operation should have. For example, `1 'kg' + 100 'g'` could yield either `1.100 'kg'` or `1100 'g'`. The submitter argues that the spec should be explicit about this behavior and recommends that when a specific unit is needed, `toQuantity(unit)` should be used to convert the result.\n\n## Resolution Description\n\nThe resolution has been updated to **defer to [FHIR-56190](https://jira.hl7.org/browse/FHIR-56190)** (\"Extensive clarifications of handling quantities, and specifically unit conversions and calendar/time valued quantities\"), which is a comprehensive rewrite of the Quantity handling sections in FHIRPath.\n\nThe original resolution (prior to deferral) proposed:\n1. Adding a cross-reference to the Date/Time Arithmetic section at the end of the first sentence in the [Math section](https://build.fhir.org/ig/HL7/FHIRPath/#math-1).\n2. Retaining the existing rule: *\"The unit of the result will be the most granular unit of either input.\"*\n3. Adding a clarifying note: the most granular unit SHALL be determined by comparing the conversion factor of the unit to the UCUM base unit, selecting the largest factor.\n4. Recommending `toQuantity(unit)` for explicit unit control, e.g., `(1 'cm' + 20 'mm').toQuantity('m')`.\n\n## Comment History Summary\n\n| Date       | Author          | Key Point |\n|------------|-----------------|-----------|\n| 2025-01-29 | bvdh            | Original resolution doesn't address the ticket; proposes implementation should freely choose units, and users should use `toQuantity` for explicit unit selection. |\n| 2025-08-13 | bryn.rhodes     | Questions the request \u2014 spec already states implementations shall use UCUM; free-choice of units contradicts tha

... *(truncated, 13195 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-49525.md with 12963 characters
```

</details>

### Turn 3

**Assistant:**

Now let me read the full ticket content and fetch the related Zulip threads and referenced Jira tickets.

<details>
<summary>`powershell` — Read full ticket content</summary>

**Arguments:**
```json
{
  "command": "Get-Content \"C:\\Users\\ginoc\\AppData\\Local\\Temp\\1775773426869-copilot-tool-output-6os10p.txt\" -Raw",
  "description": "Read full ticket content"
}
```

**Result:**
```
Output too large to read at once (30.7 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\copilot-tool-output-1775773434876-6w5ps1.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
# [jira] FHIR-53249: Quantity equivalence is ambiguous- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** JingTang
- **labels:** Discuss
- **Created:** 2025-10-27T18:30:26+00:00
- **Updated:** 2026-03-30T05:22:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53249## Content
<ol><li>In the <a href="https://bu
<exited with exit code 0>
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
Output too large to read at once (21.1 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\1775773434193-copilot-tool-output-0qwmpf.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
# fhirpath > Quanity equivalence unit granularity

**Messages:** 44
**First message:** 2025-11-22 20:22:37+00:00
**Last message:** 2026-04-07 13:12:14+00:00
**Participants:** Yury Sedinkin😎, Notification Bot, Jing Tang, Paul Lynch, Brian Postlethwaite, Bryn Rhodes, Vasilii Kupriakov, Brian Kaney, Grahame Grieve, John Silva

## Messages

### Yury Sedinkin😎 — 2025-11-22 20:22:37+00:00
I checked fhirpath.js, and I think it is an implementation issue. I don't use the most granular unit. 
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# fhirpath > Quanity equality unit granularity

**Messages:** 4
**First message:** 2025-10-10 13:50:52+00:00
**Last message:** 2025-10-27 18:32:57+00:00
**Participants:** Jing Tang

## Messages

### Jing Tang — 2025-10-10 13:50:52+00:00
I just want to raise visibility of this issue to the community as well. This expression is implemented differently in different FHIRPath engines: 4 'g' ~ 4040 'mg' :test_tube: Test with FHIRPath-Lab

### Jing Tang — 2025-10-10 13:52:00+00:00
I raised this PR, thinking that it's a typo that should be corrected: https://github.com/FHIR/fhir-test-cases/pull/243 In any case I think the spec is clear. So it's probably just an implementation issue.

### Jing Tang — 2025-10-27 18:31:53+00:00
Discussed this with Bryn we actually think there's an issue here: I summarised it in this jira ticket: https://jira.hl7.org/browse/FHIR-53249 and added this comment in the PR I raised: https://github.com/FHIR/fhir-test-cases/pull/243#issuecomment-3452655006

### Jing Tang — 2025-10-27 18:32:57+00:00
sorry the thread should be called: "quantity equivalence unit granularity", not equality.

---
*URL: https://chat.fhir.org/#narrow/stream/fhirpath/topic/Quanity%20equality%20unit%20granularity*

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-49525: Quantity math and unit conversion

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **labels:** Discuss
- **Created:** 2025-01-20T11:13:20+00:00
- **Updated:** 2026-03-30T05:22:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-49525

## Content
<p>The specification is silent on the unit that is the result of a calculation.<br/>
The result of '1 'kg' + 100 'g' might be 1.100 'kg' or 1100 'g'. I think the implementation should be free to choose the preferred approach.</p>

<p>The specification should make this more clear and indicate that when a specific unit ('kg' instead of 'g') is needed, toQuantity should be used.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53250: Calendar duration equivalence has conflicts

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** JingTang
- **labels:** Discuss
- **Created:** 2025-10-27T18:52:55+00:00
- **Updated:** 2026-03-30T05:22:38+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53250

## Content
<p>See discussion here <a href="https://chat.fhir.org/#narrow/channel/179266-fhirpath/topic/Transitivity.20and.20determinism.20of.20equivalence.20for.20durations/with/547348774" class="external-link" target="_blank" rel="nofollow noopener">#fhirpath &gt; Transitivity and determinism of equivalence for durations</a></p>

<p>The following relationships can't all be true, or we end up with a conflict:</p>



<p>1 year ~ 1 'a' ~ 365.25 'd' (the final conversion is defined in ucum)<br/>
1 year ~ 365 days ~ 365 'd'</p>

<p>Bryn suggested in his reply that 1 year ~ 365 days is not true.</p>

<p>But there is this sentence: </p>



<p>Implementations that do support units shall do so as specified by <a href="https://build.fhir.org/ig/HL7/FHIRPath/#UCUM" class="external-link" target="_blank" rel="nofollow noopener">[UCUM]</a> as well as the calendar durations as defined in the toQuantity function.</p>

<p>under 6.1.2.1 quantity equivalence <a href="https://build.fhir.org/ig/HL7/FHIRPath/#quantity-equivalence." class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/FHIRPath/#quantity-equivalence.</a></p>

<p>Proposal: remove that sentence. As well as adding in the toQuantity documentation that the calendar duration conversion factorrs are only to be used by toQuantity function to explicitly convert to a different duration. They cannot be used implicitly in determining equivalence or equality or in comparison.</p>

```

</details>

### Turn 4

**Assistant:**

Now let me fetch the related Jira tickets and check for GitHub references.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-49525: Quantity math and unit conversion

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **labels:** Discuss
- **Created:** 2025-01-20T11:13:20+00:00
- **Updated:** 2026-03-30T05:22:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-49525

## Content
<p>The specification is silent on the unit that is the result of a calculation.<br/>
The result of '1 'kg' + 100 'g' might be 1.100 'kg' or 1100 'g'. I think the implementation should be free to choose the preferred approach.</p>

<p>The specification should make this more clear and indicate that when a specific unit ('kg' instead of 'g') is needed, toQuantity should be used.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53249: Quantity equivalence is ambiguous

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** JingTang
- **labels:** Discuss
- **Created:** 2025-10-27T18:30:26+00:00
- **Updated:** 2026-03-30T05:22:21+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53249

## Content
<ol>
	<li>In the <a href="https://build.fhir.org/ig/HL7/FHIRPath/#quantity-equivalence" class="external-link" target="_blank" rel="nofollow noopener">quantity equivalence</a> section, it does not actually mention how the equivalence should be determined. It only talks about the handling of different units. <b>It should say: the two quantity values should be converted to the same unit if possible under UCUM, and then the equivalence is determined by the equivalence of the numeric parts using the definition of decimal equivalence.</b></li>
	<li>In the same section, it states: <em>"The comparison will be made using the most granular unit of either input."</em>. But in the decimal equivalence section just above, it states: <em>"comparison is done on values rounded to the precision of the least precise operand"</em>. This creates an odd situation: you would convert the two quantities to the most granular unit, but then you are comparing the two values using to the less precise one, essentially undoing the conversion to the more granular unit? For example, this test case: 4 'g' ~ 4040 'mg'. We will need to convert them to 4000 'mg'  and 4040 'mg. But then determining the equivalene of decimals... we decide they are equivalent, since the 4000 only has 1 digit of significance.... but then why the conversion in the first place? The intention of the spec here isn't clear. <b>Propose: either remove the part about using the most granular unit, or make it clear that we should not be following the same rules as decimal equivalence.</b></li>
</ol>


<p>Also see: <a href="https://github.com/FHIR/fhir-test-cases/pull/243" class="external-link" target="_blank" rel="nofollow noopener">https://github.com/FHIR/fhir-test-cases/pull/243</a></p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53250: Calendar duration equivalence has conflicts

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** JingTang
- **labels:** Discuss
- **Created:** 2025-10-27T18:52:55+00:00
- **Updated:** 2026-03-30T05:22:38+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53250

## Content
<p>See discussion here <a href="https://chat.fhir.org/#narrow/channel/179266-fhirpath/topic/Transitivity.20and.20determinism.20of.20equivalence.20for.20durations/with/547348774" class="external-link" target="_blank" rel="nofollow noopener">#fhirpath &gt; Transitivity and determinism of equivalence for durations</a></p>

<p>The following relationships can't all be true, or we end up with a conflict:</p>



<p>1 year ~ 1 'a' ~ 365.25 'd' (the final conversion is defined in ucum)<br/>
1 year ~ 365 days ~ 365 'd'</p>

<p>Bryn suggested in his reply that 1 year ~ 365 days is not true.</p>

<p>But there is this sentence: </p>



<p>Implementations that do support units shall do so as specified by <a href="https://build.fhir.org/ig/HL7/FHIRPath/#UCUM" class="external-link" target="_blank" rel="nofollow noopener">[UCUM]</a> as well as the calendar durations as defined in the toQuantity function.</p>

<p>under 6.1.2.1 quantity equivalence <a href="https://build.fhir.org/ig/HL7/FHIRPath/#quantity-equivalence." class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/FHIRPath/#quantity-equivalence.</a></p>

<p>Proposal: remove that sentence. As well as adding in the toQuantity documentation that the calendar duration conversion factorrs are only to be used by toQuantity function to explicitly convert to a different duration. They cannot be used implicitly in determining equivalence or equality or in comparison.</p>

```

</details>

<details>
<summary>`FhirAugury-refers_to`</summary>

**Result:**
```
No refers-to references found for "FHIR-56190".
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-56190
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| conversion | word | 44 | 9.561 |
| unit | word | 44 | 7.913 |
| quantity | word | 34 | 7.168 |
| equality | word | 10 | 6.084 |
| ucum | word | 14 | 5.738 |
| equivalence | word | 10 | 5.583 |
| toquantity | word | 6 | 4.769 |
| commensurable | word | 4 | 4.606 |
| decimal | word | 9 | 4.535 |
| implicit | word | 9 | 4.496 |
| valued | word | 8 | 4.450 |
| br | word | 108 | 4.329 |
| calendar | word | 6 | 3.933 |
| arithmetic | word | 5 | 3.860 |
| example | word | 19 | 3.807 |
| comparable | word | 5 | 3.704 |
| reason | word | 16 | 3.679 |
| time | word | 19 | 3.609 |
| compare | word | 7 | 3.483 |
| division | word | 4 | 3.242 |
| multiplication | word | 3 | 3.150 |
| section | word | 21 | 3.060 |
| li | word | 20 | 3.044 |
| refer | word | 10 | 2.936 |
| empty | word | 6 | 2.846 |
| comparison | word | 5 | 2.805 |
| ul | word | 14 | 2.725 |
| date | word | 8 | 2.624 |
| mo | word | 3 | 2.592 |
| month | word | 4 | 2.453 |

```

</details>


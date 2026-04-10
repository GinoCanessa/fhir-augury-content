# Session Log: FHIR-53249

**Phase:** prepared
**Work Group:** ImplementableTechnologySpecifications
**Source File:** `prepared/ImplementableTechnologySpecifications/FHIR-53249.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-53249` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 22:23:39 UTC |
| **Duration** | 134s |
| **Total Tool Calls** | 19 |
| **Total Tokens** | 411,912 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-53249
## Work Group: Implementable Technology Specifications
## Output File: C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-53249.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-53249", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-53249", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-53249", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-53249.md
````

---

## Agent Execution Log

### Turn 1

**Assistant:**

Let me fetch the other related Jira tickets mentioned in the discussions.

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
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-55471: Arithmetic and toQuantity are not NOT explicitly define for Long

- **status:** Resolved - change required
- **type:** Change Request
- **priority:** Medium
- **work_group:** Implementable Technology Specifications
- **specification:** FHIRPath (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Josh Mandel
- **labels:** Applied, Fit-For-Teleconference
- **Created:** 2026-01-28T15:17:07+00:00
- **Updated:** 2026-03-24T04:52:04+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-55471

## Content
<p>The spec does NOT explicitly define Long arithmetic or toQuantity!<br/>
    "  - Spec says +,-,*,/ are 'for Integer, Decimal, and Quantity'<br/>
    "  - Spec says div/mod are 'for Integer and Decimal<br/>
    "  - Long is NOT mentioned in arithmetic operator definitions<br/>
    "  - Reasonable interpretation: Long behaves like Integer for arithmetic<br/>
    "  - Alternative: Long could convert to Decimal (via implicit conversion)</p>


```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-53249",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
Output too large to read at once (30.2 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\1775773426869-copilot-tool-output-6os10p.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
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
	<li>In t
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-53249" (7 results)

- [zulip] 559053545 → [jira] FHIR-53249
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** Commented on https://jira.hl7.org/browse/FHIR-53249 . <p>Commented on <a href="https://jira.h...
  **Score:** 0.78
  **Updated:** 2025-11-24T14:06:30+00:00
- [zulip] 558841051 → [jira] FHIR-53249
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** ...an implementation issue. I don't use the most granular unit. Added a comment to https://jira.hl7.org/browse/FHIR-53249 . Thanks for finding this! <p>I checked f...
  **Score:** 0.55
  **Updated:** 2025-11-22T20:22:37+00:00
- [zulip] 547347600 → [jira] FHIR-53249
  **Source:** [fhirpath] Quanity equality unit granularity
  **Type:** mentions
  **Context:** ...n we actually think there's an issue here: I summarised it in this jira ticket: https://jira.hl7.org/browse/FHIR-53249 and added this comment in the PR I raised...
  **Score:** 0.44
  **Updated:** 2025-10-27T18:31:53+00:00
- [zulip] 583183656 → [jira] FHIR-53249
  **Source:** [fhirpath] Quanity equivalence unit granularity
  **Type:** mentions
  **Context:** ...k that <a href="http://jira.hl7.org/browse/FHIR-49525">FHIR-49525</a>, <a href="http://jira.hl7.org/browse/FHIR-53249">FHIR-53249</a>, <a href="http://jira.hl7....
  **Score:** 0.42
  **Updated:** 2026-04-02T05:25:48+00:00
- [zulip] 575935808 → [jira] FHIR-53249
  **Source:** [fhirpath] Definite durations above seconds in date time arithmetic
  **Type:** mentions
  **Context:** ...afting: <a href="http://jira.hl7.org/browse/FHIR-53250">FHIR-53250</a> <a href="http://jira.hl7.org/browse/FHIR-53249">FHIR-53249</a> <a href="http://jira.hl7.o...
  **Score:** 0.38
  **Updated:** 2026-02-26T05:34:10+00:00
- [zulip] 575697272 → [jira] FHIR-53249
  **Source:** [fhirpath] ITS Conference Call
  **Type:** mentions
  **Context:** ...s) <br> <a href="http://jira.hl7.org/browse/FHIR-53250">FHIR-53250</a> <a href="http://jira.hl7.org/browse/FHIR-53249">FHIR-53249</a> <a href="http://jira.hl7.o...
  **Score:** 0.23
  **Updated:** 2026-02-25T06:02:36+00:00
- [zulip] 570364225 → [jira] FHIR-53249
  **Source:** [fhirpath] Block vote for fhirpath
  **Type:** mentions
  **Context:** ...ion" data-user-id="191972">@Steve Munini</span> )</p> <p><em>(removed) <a href="http://jira.hl7.org/browse/FHIR-53249">FHIR-53249</a> <strong>Persuasive</strong...
  **Score:** 0.00
  **Updated:** 2026-01-27T16:19:28+00:00
**Warnings:**
- Value 'FHIR-53249' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (7 total, showing 7)

### [zulip] 559053545 — [fhirpath] Quanity equivalence unit granularity
- **Score:** 0.78
- **Updated:** 2025-11-24T14:06:30+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/Quanity%20equivalence%20unit%20granularity/near/559053545
- **Snippet:** Commented on https://jira.hl7.org/browse/<b>FHIR-53249</b> .

### [zulip] 558841051 — [fhirpath] Quanity equivalence unit granularity
- **Score:** 0.55
- **Updated:** 2025-11-22T20:22:37+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/Quanity%20equivalence%20unit%20granularity/near/558841051
- **Snippet:** ...Added a comment to https://jira.hl7.org/browse/<b>FHIR-53249</b> . Thanks for finding this!

### [zulip] 547347600 — [fhirpath] Quanity equality unit granularity
- **Score:** 0.44
- **Updated:** 2025-10-27T18:31:53+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/Quanity%20equality%20unit%20granularity/near/547347600
- **Snippet:** ...https://jira.hl7.org/browse/<b>FHIR-53249</b> and added this comment in the PR I raised: https://github.com/FHIR...

### [zulip] 583183656 — [fhirpath] Quanity equivalence unit granularity
- **Score:** 0.42
- **Updated:** 2026-04-02T05:25:48+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/Quanity%20equivalence%20unit%20granularity/near/583183656
- **Snippet:** ...Check that FHIR-49525 , <b>FHIR-53249</b> , FHIR-53250 (which have Bryn's dispositions in there) are all then redundant and...

### [zulip] 575935808 — [fhirpath] Definite durations above seconds in date time arithmetic
- **Score:** 0.38
- **Updated:** 2026-02-26T05:34:10+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/Definite%20durations%20above%20seconds%20in%20date%20time%20arithmetic/near/575935808
- **Snippet:** ...FHIR-53250 <b>FHIR-53249</b> FHIR-49525 If anyone is interested to join, Paul Lynch and I will be co-editing...

### [zulip] 575697272 — [fhirpath] ITS Conference Call
- **Score:** 0.23
- **Updated:** 2026-02-25T06:02:36+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/ITS%20Conference%20Call/near/575697272
- **Snippet:** ...calandar unit handling (and maybe implicit conversions) FHIR-53250 <b>FHIR-53249</b> FHIR-49525 But before we jump into those I...

### [zulip] 570364225 — [fhirpath] Block vote for fhirpath
- **Score:** 0.00
- **Updated:** 2026-01-27T16:19:28+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/fhirpath/topic/Block%20vote%20for%20fhirpath/near/570364225
- **Snippet:** ...Join function and empty collection handling ( @Steve Munini ) (removed) <b>FHIR-53249</b> Persuasive Quantity equivalence is ambiguous ( @Jing Tang ) (removed) FHIR...


```

</details>

### Turn 3

**Assistant:**

Now I have all the data needed. Let me create the report.

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-53249.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\ImplementableTechnologySpecifications\\FHIR-53249.md",
  "file_text": "# FHIR-53249: Quantity equivalence is ambiguous\n\n## Quick Reference\n\n| Field           | Value                                      |\n|-----------------|--------------------------------------------|\n| **Ticket**      | [FHIR-53249](https://jira.hl7.org/browse/FHIR-53249) |\n| **Status**      | Triaged                                    |\n| **Type**        | Change Request                             |\n| **Priority**    | Medium                                     |\n| **Resolution**  | Persuasive                                 |\n| **Work Group**  | Implementable Technology Specifications    |\n| **Specification** | FHIRPath (FHIR)                          |\n| **Reporter**    | Jing Tang                                  |\n| **Assignee**    | Unassigned                                 |\n| **Labels**      | Discuss                                    |\n| **Created**     | 2025-10-27                                 |\n| **Updated**     | 2026-03-30                                 |\n\n---\n\n## Summary\n\nThis ticket identifies two ambiguities in the FHIRPath specification's [quantity equivalence](https://build.fhir.org/ig/HL7/FHIRPath/#quantity-equivalence) section:\n\n1. **Missing equivalence algorithm**: The quantity equivalence section describes how to handle different units but never explicitly states *how* equivalence is determined. The reporter proposes stating: \"the two quantity values should be converted to the same unit if possible under UCUM, and then equivalence is determined by the equivalence of the numeric parts using the definition of decimal equivalence.\"\n\n2. **Contradictory precision rules**: The section states comparisons use \"the most granular unit of either input,\" but the decimal equivalence section says \"comparison is done on values rounded to the precision of the least precise operand.\" These rules conflict \u2014 converting to the most granular unit and then rounding to the least precise operand effectively undoes the conversion. Example: `4 'g' ~ 4040 'mg'` converts to `4000 'mg' ~ 4040 'mg'`, but under decimal equivalence, `4000` has only 1 significant digit so they'd be equivalent \u2014 making the conversion pointless.\n\nThe reporter proposes either removing the \"most granular unit\" language or clarifying that quantity equivalence should not follow the same rules as decimal equivalence.\n\n---\n\n## Keywords\n\n`FHIRPath`, `quantity`, `equivalence`, `UCUM`, `unit conversion`, `precision`, `granularity`, `decimal equivalence`, `base units`, `calendar duration`\n\n---\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relationship |\n|--------|-------|--------|------------|--------------|\n| [FHIR-49525](https://jira.hl7.org/browse/FHIR-49525) | Quantity math and unit conversion | Triaged | Not Persuasive with Modification | Bryn's proposed resolution (co

... *(truncated, 13052 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-53249.md with 12838 characters
```

</details>

### Turn 4

**Assistant:**

Let me read the full ticket content and fetch the key Zulip threads and related Jira tickets.

<details>
<summary>`powershell` — Read full ticket output</summary>

**Arguments:**
```json
{
  "command": "Get-Content \"C:\\Users\\ginoc\\AppData\\Local\\Temp\\1775774462105-copilot-tool-output-wrr6yy.txt\" -Raw",
  "description": "Read full ticket output",
  "initial_wait": 10
}
```

**Result:**
```
Output too large to read at once (31.5 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\copilot-tool-output-1775774470727-dxwgsv.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
# [jira] FHIR-53250: Calendar duration equivalence has conflicts- **status:** Triaged
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
- **URL:** https://jira.hl7.org/browse/FHIR-53250## Content
<p>See
<exited with exit code 0>
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "stream": "fhirpath",
  "topic": "Transitivity and determinism of equivalence for durations",
  "limit": 100
}
```

**Result:**
```
# fhirpath > Transitivity and determinism of equivalence for durations

**Messages:** 44
**First message:** 2025-09-24 16:32:50+00:00
**Last message:** 2026-01-12 19:34:02+00:00
**Participants:** Jing Tang, Paul Lynch, Bryn Rhodes, Gino Canessa, Brian Postlethwaite, Richard Townley-O'Neill

## Messages

### Jing Tang — 2025-09-24 16:32:50+00:00
I cannot find earlier discussions on this but I am sure the community is aware of this situation: 1 year ~ 1 'a' ~ 365.25 'd' (the final conversion is defined in ucum) 1 year ~ 365 days ~ 365 'd' But obviously 365.25 'd' !~ 365 'd' So we get to a point where equivalence is not transitive. Is this something we want to fix? If not, should we make it clear that equivalence is not transitive? A bigger problem is that equivalence is not even deterministic at the moment. 1 year ~ 365 'd' can be true or false depending on how you convert. I feel we should at least define a fixed path to convert two duration quantities when checking equivalence. For example, the year needs to be converted to 'a' first before checking for equivalence using ucum rules. I am keen to create a proposal but I also feel this is not something to be patched but requires an overall direction first. PS I saw this discussion: #fhirpath > Quantity arithmetic with calendar & definite duration unit which is relevant but that's quite a separate issue. I think equivalence is a more foundational/primitive operation than arithmetics.

### Paul Lynch — 2025-09-24 17:40:18+00:00
FYI, here is a case where the expected transitive nature of equality is missing: #fhirpath > Equality for primitives with extensions @ 💬

### Bryn Rhodes — 2025-09-30 14:16:02+00:00
I don't think this demonstrates that equivalence is not transitive because it is not strictly equivalence. This expression: 1 year ~ 365 days is sneaking in a conversion that is approximate, so we've crossed out of strict "definite duration calculations" and we can't expect the equivalence property to hold across that.

### Jing Tang — 2025-09-30 15:52:08+00:00
Is this meant to be false then? 1 year ~ 365 days :test_tube: Test with FHIRPath-Lab

### Jing Tang — 2025-09-30 15:54:28+00:00
I have written down my thoughts here: https://github.com/jingtang10/kotlin-fhirpath?tab=readme-ov-file#calendar-durations-in-fhirpath-vs-definite-durations-in-ucum Please let me know if I've got anything wrong here and how I can help. Thanks!

### Jing Tang — 2025-09-30 16:24:30+00:00
PS: and if 1 year ~ 365 days is not true i'd love to add that to the fhir test cases

### Jing Tang — 2025-10-27 18:38:50+00:00
Revisiting this, actually @Bryn Rhodes , there's this sentence in the spec under Quantity Equivalence: Implementations that do support units shall do so as specified by [UCUM] as well as the calendar durations as defined in the toQuantity function . So this is to say that the conversion factors defined in the toQuantity can actually be used to determine calendar duration equivalence. So this is in contravention to what you indicated.

### Jing Tang — 2025-10-27 18:52:21+00:00
I created https://jira.hl7.org/browse/FHIR-53250

### Paul Lynch — 2025-11-18 16:26:40+00:00
Jing Tang said : PS: and if 1 year ~ 365 days is not true i'd love to add that to the fhir test cases https://www.hl7.org/fhirpath/#toquantityunit-string-quantity says, 1 year = 365 days. I think that implies 1 year ~ 365 days also.

### Jing Tang — 2025-11-18 17:41:17+00:00
I'm not sure it is what it's saying. It says "For calendar durations, FHIRPath defines the following conversion factors:" but that doesn't necessarily mean they are equivalent or equal. So to bryn's point, conversion needs to happen explicitly, rather than implicitly. In other words I think: 1 year.toQuantity('days') ~ 365 days should be true but 1 year ~ 365 days shouldn't. By the way I raised https://jira.hl7.org/browse/FHIR-53250 to make this clear in the spec. I think accepting 1 year = 365 days or 1 year ~ 365 days 

... *(truncated, 13336 chars total)*
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


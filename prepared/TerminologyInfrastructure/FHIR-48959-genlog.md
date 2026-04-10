# Session Log: FHIR-48959

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-48959.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-48959` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:05:38 UTC |
| **Duration** | 102s |
| **Total Tool Calls** | 12 |
| **Total Tokens** | 268,554 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-48959
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-48959.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-48959", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-48959", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-48959", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-48959.md
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
  "id": "FHIR-48959",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-48959: Clarify ValueSet behavior with CodeSystem fragments

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Fragment, TEXTONLY
- **Created:** 2024-12-06T16:53:55+00:00
- **Updated:** 2026-04-06T12:39:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48959

## Content
<p>"The CodeSystem referenced in a <tt>ValueSet.compose</tt> may reference a CodeSystem fragment."</p>
<ul>
	<li>The compose may also reference the canonical URL of a CodeSystem which is represented by multiple fragments on the server. Please provide guidance around this situation.</li>
</ul>


<p>Section 4.9.10 should include consideration of CodeSystem fragments in creating an expansion (including adding them to the dragon text). As an example, an expansion based on a system with one set of fragments present may be different than an expansion based on a system with another set of fragments present, without being identified in the expansion parameters.</p>

<p>There are likely other considerations that should be mentioned.</p>

<p> </p>

<p>Also, the Request for Feedback callout indicates "Ongoing feedback is welcome at <span class="error">&#91;link to be provided&#93;</span>". Please provide link.</p>

## Comments (4)

### carmela_couderc — 2026-03-12T20:52:16+00:00
<p>See comment entered today. </p>

### carmela_couderc — 2026-03-12T20:51:59+00:00
<p>Section 4.9.6.5 Referencing Code System Fragments </p>

<p>Current text:</p>

<p>While most Code Systems are in essence one fragment and, therefore, do not have identifiable fragments, some Code Systems can be made up of a collection of distinct segments. SNOMED CT is an example of such a Code System. The SNOMED CT International Edition is the base fragment and can be used alone, but there are many distinct additional fragments that can be added to the international core to create what is known as a SNOMED CT Edition. </p>

<p>The CodeSystem referenced in ValueSet.compose may reference a CodeSystem fragment. </p>

<p>Change to:</p>

<p>REMOVE 2nd paragraph.  </p>

<p>A CodeSystem fragment MAY be used to generate an expansion in the absence of the complete code system.  </p>

<p>A CodeSystem fragment cannot be referenced directly. ValueSet definitions reference fragments in the same way the CodeSystem is referenced. For fragments represented as FHIR CodeSystem resources, CodeSystem.content = fragment indicates the CodeSystem resource represents a fragment. </p>

<p>Next change:</p>

<p>Section 4.9.10 explains how to create an expansion and currently does not reference anything about fragments. This is the focus of this ticket. </p>

<p>Current text:</p>

<p>Otherwise: For each compose.include</p>
<ol>
	<li>add a 4th bullet
	<ol>
		<li>If the expansion is based on one or more fragments of the CodeSystem, the server MUST include the *<b>to be defined</b>* extension to flag which CodeSystems relied on fragments - the complete CodeSystem was not available.   </li>
	</ol>
	</li>
</ol>


<p>An expansion for "all codes" may be invalid for a code system fragment depending on the situation. </p>

<p> </p>

### carmela_couderc — 2025-09-17T15:58:22+00:00
<p>Discussed at the 2025-09-17 WGM, Q2 Wednesday. </p>

<p>Attendees would like to ask the implementer community. Lots of discussion about code system versions, multiple fragments from the same version or multiple fragments from different versions. </p>

<p>A suggested resolution: If multiple fragments exist for the same code system version, the code system concepts should be unioned for the expansion. </p>

<p>RD will submit a zulip chat. </p>

### carmela_couderc — 2025-08-18T21:32:13+00:00
<p><a href="https://build.fhir.org/valueset.html#fragments" class="external-link" target="_blank" rel="nofollow noopen

... *(truncated, 13537 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-48959" (5 results)

- [jira] FHIR-48959 → [fhir] ValueSet.compose
  **Source:** Clarify ValueSet behavior with CodeSystem fragments
  **Type:** mentions
  **Context:** "The CodeSystem referenced in a ValueSet.compose may reference a CodeSystem fragment." The compose may also refe...
  **Score:** 1.00
  **Updated:** 2026-04-06T12:39:33+00:00
- [jira] FHIR-48959 → [fhir] CodeSystem.content
  **Source:** Clarify ValueSet behavior with CodeSystem fragments
  **Type:** mentions
  **Context:** ...deSystem is referenced. For fragments represented as FHIR CodeSystem resources, CodeSystem.content = fragment indicates the CodeSystem resource represents a fra...
  **Score:** 1.00
  **Updated:** 2026-04-06T12:39:33+00:00
- [zulip] 532938974 → [jira] FHIR-48959
  **Source:** [terminology] Adding codes to fragment CS
  **Type:** mentions
  **Context:** ... filed <a href="http://jira.hl7.org/browse/FHIR-48960">FHIR-48960</a>, <a href="http://jira.hl7.org/browse/FHIR-48959">FHIR-48959</a> on these questions (althou...
  **Score:** 0.22
  **Updated:** 2025-08-05T15:21:12+00:00
- [zulip] 486556226 → [jira] FHIR-48959
  **Source:** [terminology] Fragments and closure
  **Type:** mentions
  **Context:** Added FHIR-48959 around ValueSet expansion. <p>Added <a href="http://jira.hl7.org/browse/FHIR-48959">FHIR-48959</a> around ValueSet expansion....
  **Score:** 0.22
  **Updated:** 2024-12-06T16:54:10+00:00
- [zulip] 582882594 → [jira] FHIR-48959
  **Source:** [terminology] Tracker item FHIR-48959
  **Type:** mentions
  **Context:** ...g discussion in the Terminology Infrastructure (TI) WG on tracker item <a href="http://jira.hl7.org/browse/FHIR-48959">FHIR-48959</a> (<em>Clarify ValueSet beha...
  **Score:** 0.00
  **Updated:** 2026-03-31T19:40:13+00:00
**Warnings:**
- Value 'FHIR-48959' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 583013599 — [terminology] Tracker item FHIR-48959
- **Score:** 1.00
- **Updated:** 2026-04-01T11:33:31+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/583013599
- **Snippet:** @Michael Lawley

### [zulip] 582954900 — [terminology] Tracker item FHIR-48959
- **Score:** 1.00
- **Updated:** 2026-04-01T06:18:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/582954900
- **Snippet:** good question!

### [zulip] 583164969 — [terminology] Tracker item FHIR-48959
- **Score:** 0.81
- **Updated:** 2026-04-02T01:21:55+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/583164969
- **Snippet:** unless it actually is.

### [zulip] 583134855 — [terminology] Tracker item FHIR-48959
- **Score:** 0.72
- **Updated:** 2026-04-01T21:11:41+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/583134855
- **Snippet:** they're just functionally complete

### [zulip] 582886807 — [terminology] Tracker item FHIR-48959
- **Score:** 0.72
- **Updated:** 2026-03-31T20:02:44+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/582886807
- **Snippet:** I prefer #1 over #3

### [zulip] 583167510 — [terminology] Tracker item FHIR-48959
- **Score:** 0.63
- **Updated:** 2026-04-02T01:57:08+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/583167510
- **Snippet:** though that should be a supplement

### [zulip] 582882881 — [terminology] Tracker item FHIR-48959
- **Score:** 0.38
- **Updated:** 2026-03-31T19:41:49+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/582882881
- **Snippet:** not #2. Given our existing approach, I prefer #1

### [zulip] 486556226 — [terminology] Fragments and closure
- **Score:** 0.16
- **Updated:** 2024-12-06T16:54:10+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Fragments%20and%20closure/near/486556226
- **Snippet:** Added <b>FHIR-48959</b> around ValueSet expansion.

### [zulip] 582947246 — [terminology] Tracker item FHIR-48959
- **Score:** 0.07
- **Updated:** 2026-04-01T05:10:18+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/582947246
- **Snippet:** Prefer #1 - an output parameter with the relevant Code System Content Mode(s).

### [zulip] 583164077 — [terminology] Tracker item FHIR-48959
- **Score:** 0.00
- **Updated:** 2026-04-02T01:11:23+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Tracker%20item%20FHIR-48959/near/583164077
- **Snippet:** I don't. I don't know about others. But why does that matter?


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-48959.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-48959.md",
  "file_text": "# FHIR-48959: Clarify ValueSet behavior with CodeSystem fragments\n\n## Summary\n\n| Field          | Value                                      |\n|----------------|--------------------------------------------|\n| **Ticket**     | [FHIR-48959](https://jira.hl7.org/browse/FHIR-48959) |\n| **Status**     | Triaged                                    |\n| **Type**       | Change Request                             |\n| **Priority**   | Medium                                     |\n| **Resolution** | Persuasive with Modification               |\n| **Reporter**   | Elliot Silver                              |\n| **Assignee**   | Unassigned                                 |\n| **Work Group** | Terminology Infrastructure                 |\n| **Specification** | FHIR Core (FHIR)                        |\n| **Labels**     | Fragment, TEXTONLY                          |\n| **Created**    | 2024-12-06                                 |\n| **Updated**    | 2026-04-06                                 |\n| **Resolved**   | 2026-03-12                                 |\n\n## Problem Statement\n\nThe FHIR specification does not adequately address how ValueSet expansion should behave when the underlying CodeSystem is represented by one or more fragments. Specifically:\n\n1. **Section 4.9.6.5 (Referencing Code System Fragments):** The current text states \"The CodeSystem referenced in a `ValueSet.compose` may reference a CodeSystem fragment\" but does not address the case where the canonical URL references a CodeSystem represented by *multiple* fragments on the server.\n2. **Section 4.9.10 (Expansion):** The expansion algorithm makes no mention of fragments. An expansion based on one set of fragments may differ from an expansion based on a different set, yet nothing in the expansion parameters would identify this difference.\n3. A \"Request for Feedback\" callout in the spec contains a placeholder link (`[link to be provided]`) that was never populated.\n\n## Keywords\n\n`ValueSet`, `CodeSystem`, `fragment`, `expansion`, `compose`, `CodeSystem.content`, `ValueSet.compose`, `SNOMED CT`, `TerminologyCapabilities`, `$expand`, `$validate-code`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relationship |\n|--------|-------|--------|-------------|\n| [FHIR-48960](https://jira.hl7.org/browse/FHIR-48960) | Clarify fragment and supplement relationships | Triaged (Persuasive with Modification) | Sibling ticket filed by same reporter on same day; covers fragment-to-fragment and fragment-to-supplement relationships |\n| [FHIR-33947](https://jira.hl7.org/browse/FHIR-33947) | Clarify the use of fragment | Applied | Prior ticket that relaxed rules on who can publish fragments; referenced in WG discussion as historical precedent (Madrid meeting) |\n| [FHIR-48958](https://jira.hl7.org/browse/FHIR-48958) | Clarify expectations around canonical version uniquen

... *(truncated, 11698 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-48959.md with 11485 characters
```

</details>

### Turn 3

<details>
<summary>`powershell` — Read full ticket content</summary>

**Arguments:**
```json
{
  "command": "Get-Content \"C:\\Users\\ginoc\\AppData\\Local\\Temp\\1775767815601-copilot-tool-output-cofe22.txt\" -Raw",
  "description": "Read full ticket content"
}
```

**Result:**
```
Output too large to read at once (26.5 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\copilot-tool-output-1775767824573-z4qira.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
# [jira] FHIR-48960: Clarify fragment and supplement relationships- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Fragment
- **Created:** 2024-12-06T17:22:34+00:00
- **Updated:** 2026-04-06T12:39:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48960## Content
<p>Please 
<exited with exit code 0>
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# terminology > Fragments and closure

**Messages:** 43
**First message:** 2024-12-05 01:03:40+00:00
**Last message:** 2024-12-11 01:17:23+00:00
**Participants:** Elliot Silver, Forest, Rutt Lindström, Michael Lawley, John Moehrke, Lloyd McKenzie, Kai Kewley, Gino Canessa, Grahame Grieve

## Messages

### Elliot Silver — 2024-12-05 01:03:40+00:00
While writing about some terminology issues, I came across a collection of questions around partial code systems. If I have two or more fragments for the same version of the same code system: What behavior is expected if I try to validate a code against the code system? Should the system "synthesize" a combined code system and check whether the value is in one of the fragments? Should the system pick one (arbitrary?) fragment and check whether the value is in that one? Is a check expected to ensure that any concept is only defined in one fragment, or that the definition in one fragment is consistent? identical? with the definition in another fragment? Is there any way to identify that a collection of fragments constitute the entire code system. Are supplements limited to the content of a single fragment, or can they apply to a collection of fragments of the same system?

### Forest — 2024-12-05 01:05:33+00:00
Ideally, maybe it's a terminology governance issue. So need stakeholders come to a consensus on it.

### Elliot Silver — 2024-12-05 01:06:55+00:00
An implementation governance issue, or an HL7 governance issue?

### Rutt Lindström — 2024-12-05 07:56:36+00:00
I would try it out, but I'm afraid I'd break my terminology server having multiple CodeSystem instances claiming that they are the same CodeSystem and version. I think it's not even clear what a terminology server or validator should respond when only one fragment is present. Logically, it should only give a warning when the code is not present in the fragment, but we struggled with validator giving an error instead. Also, CS supplement is defined for CodeSystem+version. It would not know which exact resource to supplement, so I don't think there is a way to supplement different fragments.

### Michael Lawley — 2024-12-05 08:55:24+00:00
There is no specific expected behaviour in this case wrt the FHIR spec

### Michael Lawley — 2024-12-05 09:04:13+00:00
https://build.fhir.org/codesystem.html#fragments

### Rutt Lindström — 2024-12-05 09:43:36+00:00
Oh, I'm very surprised to see, that "Fragments can only be published by the code system authority, or according to a process defined by the authority, if they have defined one" I thought the main reason for creating fragments is to show something in an IG when you don't have the full authorised code system under your control. And I'm sure I've used it somewhere... I wonder what's the maximum penalty for an offence like this? :grimacing:

### John Moehrke — 2024-12-05 13:54:48+00:00
FMG has stopped some IGs that have tried to do that. Not perfect, but we are trying.

### John Moehrke — 2024-12-05 13:56:08+00:00
the fragment would be used by an authority when that authority doesn't want to publish everything. I suspect: Like some of the snomed official fragments available for various authorized use-cases.

### Lloyd McKenzie — 2024-12-05 14:11:26+00:00
There is no rule that stops a server from storing multiple instances with the same canonical and version. There are a number of use-cases that will require servers to do so.

### Kai Kewley — 2024-12-06 10:27:28+00:00
Lloyd McKenzie said : There is no rule that stops a server from storing multiple instances with the same canonical and version. There are a number of use-cases that will require servers to do so. Do you have an example use case for that please Lloyd?

### Lloyd McKenzie — 2024-12-06 13:54:31+00:00
Questionnaire where you've got a modular form and an assembled form. ValueSet where you've got the base definition and then a few snapshots with different expansions. Library where you 

... *(truncated, 11903 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# terminology > Adding codes to fragment CS

**Messages:** 50
**First message:** 2025-08-03 06:07:38+00:00
**Last message:** 2025-09-04 04:53:21+00:00
**Participants:** Jose Costa Teixeira, Rutt Lindström, Lloyd McKenzie, Robert McClure, Grahame Grieve, Elliot Silver, Carmela Couderc, Michaela Ziegler, Frank Oemig, Carol Macumber

## Messages

### Jose Costa Teixeira — 2025-08-03 06:07:38+00:00
For a code defined in THO where content is fragment or not present, can an IG simply add those as a CS? Supplement?

### Rutt Lindström — 2025-08-03 12:40:12+00:00
If you need it for a valueset binding, you should be able to just add the codes you need directly to your valueset. I think it gave an informational warning about not being able to validate, which is ok. If you need to add displays, you might want a CS supplement, too.

### Lloyd McKenzie — 2025-08-03 14:18:01+00:00
You cannot add codes using a CS Supplement. A supplement can add properties and designations, it can't define codes.

### Jose Costa Teixeira — 2025-08-03 19:21:33+00:00
Lloyd McKenzie said : You cannot add codes using a CS Supplement. A supplement can add properties and designations, it can't define codes. That is my question. Does this also apply to fragments ?

### Lloyd McKenzie — 2025-08-03 23:13:46+00:00
A supplement can't add codes at all. A supplement can define properties to codes. If you see a supplement that defines properties on codes that aren't in your fragment, you could guess that those codes are legal, but that's not what the supplement is for, and I wouldn't expect any terminology service to be checking supplements to find additional codes not found in whatever definitional fragment the TS has.

### Robert McClure — 2025-08-04 17:16:33+00:00
A fragment is crafted by someone to provide some, but not all, of the official code system concepts. If you need some more of the official concepts to be included in the fragment, contact the entity the created the fragment to see if more can be added. What specific code system is in play here?

### Jose Costa Teixeira — 2025-08-05 05:18:15+00:00
https://terminology.hl7.org/6.5.0/CodeSystem-icd-o-3.html

### Grahame Grieve — 2025-08-05 05:59:27+00:00
you can make more fragements

### Jose Costa Teixeira — 2025-08-05 06:02:07+00:00
In my ig?

### Grahame Grieve — 2025-08-05 06:03:24+00:00
a fragment, not a supplement

### Jose Costa Teixeira — 2025-08-05 06:03:51+00:00
Right, i missed that.

### Jose Costa Teixeira — 2025-08-05 06:04:49+00:00
Also for CS where content is not-present?

### Grahame Grieve — 2025-08-05 06:05:21+00:00
you can just define that one

### Robert McClure — 2025-08-05 15:13:33+00:00
I suppose more than one fragment can exist - we can do nothing to control that. @Grahame Grieve how does the publisher resolve multiple fragments for the same code system? Does it create a union? That would be dangerous so version identification is a key aspect.

### Elliot Silver — 2025-08-05 15:21:12+00:00
@Robert McClure , I'd previously filed FHIR-48960 , FHIR-48959 on these questions (although asking for clarity in the spec, not for publisher behavior), however, they haven't moved beyond initial triage in 8 months.

### Grahame Grieve — 2025-08-05 18:42:30+00:00
how does the publisher resolve multiple fragments for the same code system? I have no idea

### Robert McClure — 2025-08-06 15:36:27+00:00
@Elliot Silver Yep, no one seems to be ready to touch this one. Perhaps this should be a connectathon breakout to at least gather input on the issues and how existing servers are managing this. @Carmela Couderc @Carol Macumber @Reuben Daniels @Grahame Grieve @Michael Lawley @Peter Jordan

### Carmela Couderc — 2025-08-06 16:45:26+00:00
August 18 TI tracker call will focus on code system related tickets. @Elliot Silver please join the call at 5 eastern and we will discuss FHIR-48960 A proposal documented in the ticket would be welcome.

### Elliot 

... *(truncated, 9197 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-48959",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-48959: Clarify ValueSet behavior with CodeSystem fragments

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Fragment, TEXTONLY
- **Created:** 2024-12-06T16:53:55+00:00
- **Updated:** 2026-04-06T12:39:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48959

## Content
<p>"The CodeSystem referenced in a <tt>ValueSet.compose</tt> may reference a CodeSystem fragment."</p>
<ul>
	<li>The compose may also reference the canonical URL of a CodeSystem which is represented by multiple fragments on the server. Please provide guidance around this situation.</li>
</ul>


<p>Section 4.9.10 should include consideration of CodeSystem fragments in creating an expansion (including adding them to the dragon text). As an example, an expansion based on a system with one set of fragments present may be different than an expansion based on a system with another set of fragments present, without being identified in the expansion parameters.</p>

<p>There are likely other considerations that should be mentioned.</p>

<p> </p>

<p>Also, the Request for Feedback callout indicates "Ongoing feedback is welcome at <span class="error">&#91;link to be provided&#93;</span>". Please provide link.</p>

```

</details>

### Turn 4

**Assistant:**

Let me fetch the most relevant related tickets and the Zulip thread.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-48959: Clarify ValueSet behavior with CodeSystem fragments

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Fragment, TEXTONLY
- **Created:** 2024-12-06T16:53:55+00:00
- **Updated:** 2026-04-06T12:39:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48959

## Content
<p>"The CodeSystem referenced in a <tt>ValueSet.compose</tt> may reference a CodeSystem fragment."</p>
<ul>
	<li>The compose may also reference the canonical URL of a CodeSystem which is represented by multiple fragments on the server. Please provide guidance around this situation.</li>
</ul>


<p>Section 4.9.10 should include consideration of CodeSystem fragments in creating an expansion (including adding them to the dragon text). As an example, an expansion based on a system with one set of fragments present may be different than an expansion based on a system with another set of fragments present, without being identified in the expansion parameters.</p>

<p>There are likely other considerations that should be mentioned.</p>

<p> </p>

<p>Also, the Request for Feedback callout indicates "Ongoing feedback is welcome at <span class="error">&#91;link to be provided&#93;</span>". Please provide link.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-28612: Define an extension to indicate whether a code system has an incomplete statement of code system definition

- **status:** Resolved - No Change
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Retracted
- **assignee:** Unassigned
- **reporter:** Grahame Grieve
- **labels:** R5
- **Created:** 2020-09-24T22:36:45+00:00
- **Updated:** 2022-07-28T04:37:53+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-28612

## Content
<p>CodeSystem.content allows to indicate that a CodeSystem contains none, some, or all of the concepts in the code system. But there's no way for us to indicate that about the metadata of the code system, including the properties and filters - and we have quite a few code systems that are incomplete in some way in this regard in UTG</p>

<p>We agreed during the Sept 2020 virtual meeting to create an extension to describe the status of these code systems to help tools understand which code systems definitions to use (or ignore) in which circumstances. </p>

<p>This task is to prompt the committee to come up with a formal definition and approve actually defining it </p>

<p>Question from Rob McClure - does this need to cover value set? (my response: I don't know of a situation like this with value set)</p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53375: Improve/clarify the definition of the 'example' concept in the Code System Content Mode code system

- **status:** Waiting for Input
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Reuben Daniels
- **reporter:** Reuben Daniels
- **labels:** TEXTONLY
- **Created:** 2025-11-06T11:48:04+00:00
- **Updated:** 2026-02-19T16:14:04+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53375

## Content
<p>Concepts from the <a href="https://build.fhir.org/codesystem-codesystem-content-mode.html" class="external-link" target="_blank" rel="nofollow noopener">Code System Content Mode</a> code system are used to populate the CodeSystem.content element (through a required binding to the <a href="http://hl7.org/fhir/ValueSet/codesystem-content-mode" class="external-link" target="_blank" rel="nofollow noopener">Code System Content Mode</a> value set). One of the concepts from the code system with code 'example' is defined as:</p>

<p><em>A subset of the valid externally defined concepts are included in the code system resource. There is no specific purpose or documented intent other than for illustrative purposes. This example content mode should not be used if the content is better represented in a fragment.</em></p>

<p>This definition is problematic because:</p>

<p>1. It is open to various interpretations based on what meaning implementers apply to the terms:</p>
<ul>
	<li>"valid" (in what context?)</li>
	<li>"externally defined" (external to what?)</li>
	<li>"illustrative purposes" (illustrative of what?)</li>
</ul>


<p>2. The language "<em>This example content mode</em>" suggests that the content mode is itself is an 'example' leading to further confusion.</p>

<p>This change request is to develop a better definition which addresses the above issues and ideally provides some concrete examples (pun unintended) that describe how this concept is appropriately and correctly to be used in CodeSystem resource instances.</p>

<p>Noting that policies about 'example code systems' exist and are being developed in HL7 (e.g. in TSMG and FMG), it would be helpful to have this definition clarified so that it it may be referenced where appropriate in policies.</p>

<p> </p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-54129: CodeSystem Text Technical Corrections

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Carmela A. Couderc
- **Created:** 2026-01-13T19:53:29+00:00
- **Updated:** 2026-01-20T04:52:51+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-54129

## Content
<p>4.8 <a href="https://build.fhir.org/codesystem.html#4.8" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/codesystem.html#4.8</a> </p>

<p><b>Current text:</b> The CodeSystem resource is used to declare the existence of an describe a code system or code system supplement and its key properties, and optionally define a part or all of its content. </p>

<p><b>Change to:</b></p>

<p>The CodeSystem resource is used to declare the existence of and describe a code system, code system fragment or code system supplement and its attributes, and optionally define its content. </p>

<p>4.8.1 Scope and Usage <a href="https://build.fhir.org/codesystem.html#scope" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/codesystem.html#scope</a> </p>

<p><b>Current text:</b></p>

<p>The FHIR terminology specification is based on the concepts of code system and value set originally defined in core principles.</p>

<p><b>Change to:</b></p>

<p>The FHIR terminology specification is based on the concepts of code system originally defined in core principles.</p>

<p><b>Current text:</b></p>

<p>The CodeSystem resource is used to declare the existence of a code system and its key properties. </p>

<p><b>Change to:</b></p>

<p>The CodeSystem resource is used to declare the existence of a code system and its attributes. Here are examples of CodeSystem elements. </p>

<p>There is a bulleted list in this section, <a href="https://build.fhir.org/codesystem.html#scope" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/codesystem.html#scope</a> </p>

<p>3rd bullet: </p>

<p><b>Current text:</b></p>
<ul>
	<li>Some key properties of the code system itself - e.g. whether it exhibits concept permanence, whether it defines a compositional grammar, and whether the codes that it defines are case sensitive</li>
</ul>


<p><b>Change to:</b></p>
<ul>
	<li>Whether the code system exhibits concept permanence, whether it defines a compositional grammar, and whether the <font color="#FF0000">concept codes</font> that it defines are case sensitive</li>
</ul>


<p>Text under the bulleted list</p>

<p><b>Current text:</b></p>

<p>In addition, the CodeSystem resource may list some or all of the concepts in the code system, along with their basic properties (code, display, definition), designations, and additional properties. </p>

<p><b>Change to:</b></p>

<p>In addition, the CodeSystem resource may list some or all of the concepts in the code system, along with code, display, definition designations, and properties. </p>

<p>2nd paragraph under the bulleted list</p>

<p><b>Current text:</b></p>

<p>Instead, the focus is on publishing the properties and optionally the content of a code system for use throughout the FHIR eco-system, such as to support value set expansion and validation. </p>

<p><b>Change to:</b></p>

<p>The focus is on publishing the attributes and optionally the content of a code system for use throughout the FHIR eco-system, such as to support value set expansion and validation. </p>

<p>Same paragraph</p>

<p><b>Current text:</b></p>

<p>Note that the important existing (large) code systems (SNOMED CT, LOINC, RxNorm, ICD family, etc.) all have their own maintenance systems and distribution formats, and CodeSystem is generally not an efficient way to distribute their content, though it is used as one way of declaring the filters and properties associated with those code systems.</p>

<p><b

... *(truncated, 7874 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "stream": "committers/announce",
  "topic": "\u2714 New Validation Rules coming your way",
  "limit": 20
}
```

**Result:**
```
No messages found in stream 'committers/announce', topic '✔ New Validation Rules coming your way'.
```

</details>

### Turn 5

**Assistant:**

Let me get details on the most relevant related tickets.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-48959: Clarify ValueSet behavior with CodeSystem fragments

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Fragment, TEXTONLY
- **Created:** 2024-12-06T16:53:55+00:00
- **Updated:** 2026-04-06T12:39:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48959

## Content
<p>"The CodeSystem referenced in a <tt>ValueSet.compose</tt> may reference a CodeSystem fragment."</p>
<ul>
	<li>The compose may also reference the canonical URL of a CodeSystem which is represented by multiple fragments on the server. Please provide guidance around this situation.</li>
</ul>


<p>Section 4.9.10 should include consideration of CodeSystem fragments in creating an expansion (including adding them to the dragon text). As an example, an expansion based on a system with one set of fragments present may be different than an expansion based on a system with another set of fragments present, without being identified in the expansion parameters.</p>

<p>There are likely other considerations that should be mentioned.</p>

<p> </p>

<p>Also, the Request for Feedback callout indicates "Ongoing feedback is welcome at <span class="error">&#91;link to be provided&#93;</span>". Please provide link.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-54129: CodeSystem Text Technical Corrections

- **status:** Triaged
- **type:** Technical Correction
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Carmela A. Couderc
- **Created:** 2026-01-13T19:53:29+00:00
- **Updated:** 2026-01-20T04:52:51+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-54129

## Content
<p>4.8 <a href="https://build.fhir.org/codesystem.html#4.8" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/codesystem.html#4.8</a> </p>

<p><b>Current text:</b> The CodeSystem resource is used to declare the existence of an describe a code system or code system supplement and its key properties, and optionally define a part or all of its content. </p>

<p><b>Change to:</b></p>

<p>The CodeSystem resource is used to declare the existence of and describe a code system, code system fragment or code system supplement and its attributes, and optionally define its content. </p>

<p>4.8.1 Scope and Usage <a href="https://build.fhir.org/codesystem.html#scope" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/codesystem.html#scope</a> </p>

<p><b>Current text:</b></p>

<p>The FHIR terminology specification is based on the concepts of code system and value set originally defined in core principles.</p>

<p><b>Change to:</b></p>

<p>The FHIR terminology specification is based on the concepts of code system originally defined in core principles.</p>

<p><b>Current text:</b></p>

<p>The CodeSystem resource is used to declare the existence of a code system and its key properties. </p>

<p><b>Change to:</b></p>

<p>The CodeSystem resource is used to declare the existence of a code system and its attributes. Here are examples of CodeSystem elements. </p>

<p>There is a bulleted list in this section, <a href="https://build.fhir.org/codesystem.html#scope" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/codesystem.html#scope</a> </p>

<p>3rd bullet: </p>

<p><b>Current text:</b></p>
<ul>
	<li>Some key properties of the code system itself - e.g. whether it exhibits concept permanence, whether it defines a compositional grammar, and whether the codes that it defines are case sensitive</li>
</ul>


<p><b>Change to:</b></p>
<ul>
	<li>Whether the code system exhibits concept permanence, whether it defines a compositional grammar, and whether the <font color="#FF0000">concept codes</font> that it defines are case sensitive</li>
</ul>


<p>Text under the bulleted list</p>

<p><b>Current text:</b></p>

<p>In addition, the CodeSystem resource may list some or all of the concepts in the code system, along with their basic properties (code, display, definition), designations, and additional properties. </p>

<p><b>Change to:</b></p>

<p>In addition, the CodeSystem resource may list some or all of the concepts in the code system, along with code, display, definition designations, and properties. </p>

<p>2nd paragraph under the bulleted list</p>

<p><b>Current text:</b></p>

<p>Instead, the focus is on publishing the properties and optionally the content of a code system for use throughout the FHIR eco-system, such as to support value set expansion and validation. </p>

<p><b>Change to:</b></p>

<p>The focus is on publishing the attributes and optionally the content of a code system for use throughout the FHIR eco-system, such as to support value set expansion and validation. </p>

<p>Same paragraph</p>

<p><b>Current text:</b></p>

<p>Note that the important existing (large) code systems (SNOMED CT, LOINC, RxNorm, ICD family, etc.) all have their own maintenance systems and distribution formats, and CodeSystem is generally not an efficient way to distribute their content, though it is used as one way of declaring the filters and properties associated with those code systems.</p>

<p><b

... *(truncated, 7874 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53375: Improve/clarify the definition of the 'example' concept in the Code System Content Mode code system

- **status:** Waiting for Input
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Reuben Daniels
- **reporter:** Reuben Daniels
- **labels:** TEXTONLY
- **Created:** 2025-11-06T11:48:04+00:00
- **Updated:** 2026-02-19T16:14:04+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53375

## Content
<p>Concepts from the <a href="https://build.fhir.org/codesystem-codesystem-content-mode.html" class="external-link" target="_blank" rel="nofollow noopener">Code System Content Mode</a> code system are used to populate the CodeSystem.content element (through a required binding to the <a href="http://hl7.org/fhir/ValueSet/codesystem-content-mode" class="external-link" target="_blank" rel="nofollow noopener">Code System Content Mode</a> value set). One of the concepts from the code system with code 'example' is defined as:</p>

<p><em>A subset of the valid externally defined concepts are included in the code system resource. There is no specific purpose or documented intent other than for illustrative purposes. This example content mode should not be used if the content is better represented in a fragment.</em></p>

<p>This definition is problematic because:</p>

<p>1. It is open to various interpretations based on what meaning implementers apply to the terms:</p>
<ul>
	<li>"valid" (in what context?)</li>
	<li>"externally defined" (external to what?)</li>
	<li>"illustrative purposes" (illustrative of what?)</li>
</ul>


<p>2. The language "<em>This example content mode</em>" suggests that the content mode is itself is an 'example' leading to further confusion.</p>

<p>This change request is to develop a better definition which addresses the above issues and ideally provides some concrete examples (pun unintended) that describe how this concept is appropriately and correctly to be used in CodeSystem resource instances.</p>

<p>Noting that policies about 'example code systems' exist and are being developed in HL7 (e.g. in TSMG and FMG), it would be helpful to have this definition clarified so that it it may be referenced where appropriate in policies.</p>

<p> </p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-28612: Define an extension to indicate whether a code system has an incomplete statement of code system definition

- **status:** Resolved - No Change
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Retracted
- **assignee:** Unassigned
- **reporter:** Grahame Grieve
- **labels:** R5
- **Created:** 2020-09-24T22:36:45+00:00
- **Updated:** 2022-07-28T04:37:53+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-28612

## Content
<p>CodeSystem.content allows to indicate that a CodeSystem contains none, some, or all of the concepts in the code system. But there's no way for us to indicate that about the metadata of the code system, including the properties and filters - and we have quite a few code systems that are incomplete in some way in this regard in UTG</p>

<p>We agreed during the Sept 2020 virtual meeting to create an extension to describe the status of these code systems to help tools understand which code systems definitions to use (or ignore) in which circumstances. </p>

<p>This task is to prompt the committee to come up with a formal definition and approve actually defining it </p>

<p>Question from Rob McClure - does this need to cover value set? (my response: I don't know of a situation like this with value set)</p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-35454: Defining URLshould be anchored in THO not hl7.org/fhir. Only those with required binding to a 'code' data type should be anchored in hl7.fhir.org.1

- **status:** Resolved - No Change
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Core (FHIR)
- **resolution:** Not Persuasive
- **assignee:** Unassigned
- **reporter:** Joan Harper
- **labels:** Block-Vote-2, EH-Review, Terminology
- **Created:** 2022-01-10T21:14:06+00:00
- **Updated:** 2022-04-04T15:15:19+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-35454

## Content
<p>The Value Set canonical url should be anchored in terminology.hl7.org (THO), not hl7.org/fhir.  A UTG ticket should be created to register the Value Set in THO.</p>

<p>(<b>Comment 1 - imported by: Ron G. Parker</b>)</p>

```

</details>

### Turn 6

**Assistant:**

Good, I have related tickets and some Zulip threads. Let me fetch details on the most relevant items.

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-48959",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-48959: Clarify ValueSet behavior with CodeSystem fragments

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Fragment, TEXTONLY
- **Created:** 2024-12-06T16:53:55+00:00
- **Updated:** 2026-04-06T12:39:33+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-48959

## Content
<p>"The CodeSystem referenced in a <tt>ValueSet.compose</tt> may reference a CodeSystem fragment."</p>
<ul>
	<li>The compose may also reference the canonical URL of a CodeSystem which is represented by multiple fragments on the server. Please provide guidance around this situation.</li>
</ul>


<p>Section 4.9.10 should include consideration of CodeSystem fragments in creating an expansion (including adding them to the dragon text). As an example, an expansion based on a system with one set of fragments present may be different than an expansion based on a system with another set of fragments present, without being identified in the expansion parameters.</p>

<p>There are likely other considerations that should be mentioned.</p>

<p> </p>

<p>Also, the Request for Feedback callout indicates "Ongoing feedback is welcome at <span class="error">&#91;link to be provided&#93;</span>". Please provide link.</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-39640",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-39640: Need clarification and example for using SNOMED CT US Edition

- **status:** Published
- **type:** Change Request
- **priority:** Highest
- **work_group:** Cross-Group Projects
- **specification:** US Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Eric Haas
- **reporter:** Yunwei Wang
- **labels:** Block-Vote-2, EH-Review
- **Created:** 2022-12-16T18:31:38+00:00
- **Updated:** 2023-05-03T23:11:32+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-39640

## Content
<p>Need clarification on this guidance:</p>

<p>US Core uses the US Edition of SNOMED CT, which is the official source of SNOMED CT for use in US healthcare systems. The US Edition is a standalone release that combines the content of the US Extension and the International releases of SNOMED CT. The proper URI should be used for terminology servers to validate US Edition only codes. <a href="http://snomed.info/sct" class="external-link" target="_blank" rel="nofollow noopener">http://snomed.info/sct</a> should means an unspecified edition/version. the US Edition URI is <a href="http://snomed.info/sct/731000124108" class="external-link" target="_blank" rel="nofollow noopener">http://snomed.info/sct/731000124108</a>.</p>

<p>Does this mean that all SNOMED code using in US Core resources shall have "http://snomed.info/sct/731000124108" as code system value?</p>

<p>If so, why the values in US Core 6 does not use this code system url? for example: <a href="https://build.fhir.org/ig/HL7/US-Core/ValueSet-us-core-condition-code.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/US-Core/ValueSet-us-core-condition-code.html</a></p>

<p>Could you provide an example using this new code system url?</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-13408",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-13408: Clarification for the SNOMED CT "Version Issues" section

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Caroline Macumber
- **Created:** 2017-05-15T14:07:16+00:00
- **Updated:** 2019-01-07T23:42:41+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-13408

## Content
<p>Proposed verbiage addition shown below in <b>BOLD</b> to clarify the expected default behavior of a Terminology Service in Section 4.2.1.0.2 (linked here <a href="https://www.hl7.org/fhir/snomedct.html#4.2.1.0.2" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/snomedct.html#4.2.1.0.2</a>)</p>

<hr />

<p>         There is no single distribution that contains all defined SNOMED CT codes in all contexts of use. Instead the international release contains all concepts shared and agreed to be internationally relevant and each national release centre distributes this international release plus additional national content (to extend that international set). In addition, other release authorities may be designated. The <a href="http://snomed.org/uristandard" class="external-link" target="_blank" rel="nofollow noopener">SNOMED CT URI Specification </a> describes how to unambiguously reference a particular version of a distribution:</p>

<p>           [http://snomed.info/sct/[sctid]/version/[YYYYMMDD|http://snomed.info/sct/%5Bsctid%5D/version/%5BYYYYMMDD]]</p>

<p>         where <span class="error">&#91;sctid&#93;</span> is the concept id of the SNOMED CT distribution (e.g. 32506021000036107 for Australia), and the tail is the date of release (by custom, this is usually the last day of the month). Note that many implementations are in the habit of simple*y* using the date of release in the form YYYYMMDD (e.g. "20140531"), and assuming that the distribution is known. However this is not always safe, so implementations that populate the <em>version</em> element SHOULD use the full URI form* (as shown above). At minimum the URI SHOULD contain the concept id of the SNOMED CT distribution:*         </p>

<ul>
	<li><a href="http://snomed.info/sct/%5Bsctid]" class="external-link" target="_blank" rel="nofollow noopener">http://snomed.info/sct/[sctid</a>*</li>
</ul>


<p>                     *Implementers must note, if no <em>version</em> URI is provided when utilizing SNOMED CT, the Terminology Service may default to the most recent version of SNOMED CT International available on the service. Further, if the date of release is not provided, the Terminology Service may default to the most recent version of a named SNOMED CT distribution (e.g. 32506021000036107 for Australia). *</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-44904",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-44904: Resolve SNOMED Version challenge with value set

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** International Patient Summary (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Sheridan Cook
- **labels:** Block-Vote-2
- **Created:** 2024-03-06T14:39:30+00:00
- **Updated:** 2025-10-03T17:32:14+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-44904

## Content
<p>We're getting an error from the terminology server when we try to include our Canadian SNOMED edition (<a href="http://snomed.info/sct/20611000087101" class="external-link" target="_blank" rel="nofollow noopener">http://snomed.info/sct/20611000087101</a>) as the version in instances for Device (potentially others) that we don't re-profile for in Canada.</p>

<p>From what I can glean, the claiming of the SCT core module version in the medical devices IPS valueSet via compose.include.version - seems to result in the validator not recognizing that I could be supplying that same value but in my own national edition. </p>

<p>Our understanding is that SNOMED is the one asking us to convey the version this way in instances (see: <a href="https://terminology.hl7.org/SNOMEDCT.html" class="external-link" target="_blank" rel="nofollow noopener">https://terminology.hl7.org/SNOMEDCT.html</a>). </p>

<p>We believe this is an issue with the way the value set is defined or the way the validator is interacting with the valueSet (e.g., not performing a secondary check/waiving the error when the its a national version code for SNOMED)?</p>

<p>Here's the error message from the qa-tx file (full file attached):<br/>
"{"resourceType" : "Parameters","parameter" : [</p>
{"name" : "result","valueBoolean" : false}
<p>,</p>
{"name" : "system","valueUri" : "http://snomed.info/sct"}
<p>,</p>
{"name" : "code","valueCode" : "74566002"}
<p>,</p>
{"name" : "version","valueString" : "http://snomed.info/sct/900000000000207008/version/20230131"}
<p>,</p>
{"name" : "display","valueString" : "Crutch"}
<p>,{"name" : "issues","resource" : {"resourceType" : "OperationOutcome","issue" : [{"severity" : "error","code" : "invalid","details" : {"coding" : [</p>
{"system" : "http://hl7.org/fhir/tools/CodeSystem/tx-issue-type","code" : "vs-invalid"}
<p>],"text" : "The code system \"http://snomed.info/sct\" version \"http://snomed.info/sct/900000000000207008\" in the ValueSet include is different to the one in the value (\"http://snomed.info/sct/20611000087101\")"},"location" : <span class="error">&#91;&quot;Coding.version&quot;&#93;</span>,"expression" : <span class="error">&#91;&quot;Coding.version&quot;&#93;</span>}]}}]}</p>


```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "stream": "conformance",
  "topic": "Questionnaire validation, SNOMED CT codes, edition",
  "limit": 30
}
```

**Result:**
```
Output too large to read at once (21.3 KB). Saved to: C:\Users\ginoc\AppData\Local\Temp\1775778751225-copilot-tool-output-98i3y0.txt
Consider using tools like grep (for searching), head/tail (for viewing start/end), view with view_range (for specific sections), or jq (for JSON) to examine portions of the output.

Preview (first 500 chars):
# conformance > Questionnaire validation, SNOMED CT codes, edition

**Messages:** 30
**First message:** 2025-11-26 17:09:43+00:00
**Last message:** 2025-11-27 22:23:03+00:00
**Participants:** Jon Zammit, Lloyd McKenzie, Grahame Grieve, Rutt Lindström, David Otasek

## Messages

### Jon Zammit — 2025-11-26 17:09:43+00:00
Hey guys, Hopefully this is the right place to ask this question. I am using the FHIR command-line validator against a questionnaire which uses some newer SNOMED CT cod
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-30097",
  "includeContent": true,
  "includeComments": false,
  "includeSnapshot": false
}
```

**Result:**
```
# [jira] FHIR-30097: Clarification on asserting versions of SNOMED CT

- **status:** Resolved - No Change
- **type:** Change Request
- **priority:** High
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Retracted
- **assignee:** Unassigned
- **reporter:** Reuben Daniels
- **Created:** 2020-12-21T15:24:09+00:00
- **Updated:** 2022-07-19T01:24:12+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-30097

## Content
<p>The <em>Using SNOMED CT with FHIR</em> page of the FHIR specification states that when asserting versions of SNOMED CT In FHIR the following two SNOMED CT URIs <em>SHOULD</em> be adopted:</p>
<ul>
	<li>[http://snomed.info/sct/[sctid]/version/[YYYYMMDD]]</li>
	<li><a href="http://snomed.info/sct/[sctid]" class="external-link" target="_blank" rel="nofollow noopener">http://snomed.info/sct/[sctid]</a> </li>
</ul>


<p>However, neither of these are provided as mandatory (i.e. with a SHALL statement) and thus, any version value may be considered as acceptable. Further, not enough detail on behaviour when using the <a href="http://snomed.info/sct/[sctid]" class="external-link" target="_blank" rel="nofollow noopener">http://snomed.info/sct/[sctid]</a> URI is provided (compared to the [http://snomed.info/sct/[sctid]/version/[YYYYMMDD]] URI).</p>

<p>It is thus suggested that the page be updated with content which provides:</p>
<ul>
	<li>Semantics and behaviour when using the "version-less" edition URI [http://snomed.info/sct/[sctid]|http://snomed.info/sct/[sctid]_] ; and</li>
	<li>Mandating what qualifies as a valid URI to ensure implementers do not use version values outside of the above two URIs. </li>
</ul>


<p> </p>

```

</details>


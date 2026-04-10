# Session Log: FHIR-51614

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-51614.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-51614` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 22:15:51 UTC |
| **Duration** | 97s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 266,595 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51614
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51614.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51614", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51614", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51614", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51614.md
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
  "id": "FHIR-51614",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51614: Better guidance for translating codes

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Vadim Peretokin
- **labels:** TEXTONLY
- **Created:** 2025-08-01T05:12:59+00:00
- **Updated:** 2026-01-20T04:49:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51614

## Content
<p>In the context of translating codesystems, this is what the <a href="http://hl7.org/fhir/codesystem.html#designations" class="external-link" target="_blank" rel="nofollow noopener">CodeSystem</a> resource says about designations:</p>

<blockquote>
<p>In addition to the display and definition, a concept can have one or more <tt>designation</tt> elements. The display is equivalent to a special designation with an implied <tt>designation.use</tt> meaning "primary code/designation" and a language equal to the <a href="http://hl7.org/fhir/resource.html#language" class="external-link" target="_blank" rel="nofollow noopener">Resource Language</a>. The designations can provide additional displays for other language, as well as designations for other purposes. When using concepts, applications use the <tt>display</tt> and <tt>designation</tt> unless the language or usage in context provides a reason to use one of the designations.</p></blockquote>

<p>This is what the <a href="http://hl7.org/fhir/valueset.html#designations" class="external-link" target="_blank" rel="nofollow noopener">ValueSet</a> resource about them:</p>

<blockquote>
<p>In addition to the display, a concept can have one or more <tt>designation</tt> elements. The display is equivalent to a special designation with an implied <tt>designation.use</tt> of "primary code" and a language equal to the <a href="http://hl7.org/fhir/resource.html#language" class="external-link" target="_blank" rel="nofollow noopener">Resource Language</a>. The designations can provide additional displays for other languages, as well as designations for other purposes. When using concepts, applications use the <tt>display</tt> unless the language or usage in context provides a reason to use one of the designations.</p></blockquote>

<p>The text is pretty much the same, which is unfortunate, because there is a very big difference between the two! When translating 3rd party codesystems, designations should be <a href="https://chat.fhir.org/#narrow/channel/179252-IG-creation/topic/.E2.9C.94.20Translating.203rd.20party.20codesystems" class="external-link" target="_blank" rel="nofollow noopener">added to the codesystem supplements</a>, <b>not</b> valuesets. This is a bit of a footgun: without consulting Zulip, it's not possible to know the right way to use translation designations.</p>

<p>It would be great if the spec was clearer about this. Additionally, the IG publisher should give a warning/information message when adding <b>language designations</b> to valuesets - which is something you are unlikely to do. I imagine designations added to a valueset would be non-language ones, just like the LOINC code example in the spec.</p>

<p>See also the associated <a href="https://chat.fhir.org/#narrow/channel/179202-terminology/topic/Better.20guidance.20for.20translating.20codesystems" class="external-link" target="_blank" rel="nofollow noopener">Zulip discussion</a>.</p>

## Comments (1)

### mjlawley — 2025-08-03T01:16:41+00:00
<p>That test should really point the reader to the designation use code "<a href="http://terminology.hl7.org/CodeSystem/hl7TermMaintInfra" class="external-link" target="_blank" rel="nofollow noopener">http://terminology.hl7.org/CodeSystem/hl7TermMaintInfra</a>#preferredForLanguage" and that code should probably also be included in the <a href="http://hl7.org/fhir/ValueSet/designation-use" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/ValueSet/designation-use</a

... *(truncated, 7954 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-51614" (1 results)

- [zulip] 532225654 → [jira] FHIR-51614
  **Source:** [terminology] Better guidance for translating codesystems
  **Type:** mentions
  **Context:** https://jira.hl7.org/browse/FHIR-51614 <p><a href="https://jira.hl7.org/browse/F...
  **Score:** 0.51
  **Updated:** 2025-08-01T05:12:43+00:00
**Warnings:**
- Value 'FHIR-51614' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 532225654 — [terminology] Better guidance for translating codesystems
- **Score:** 0.51
- **Updated:** 2025-08-01T05:12:43+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Better%20guidance%20for%20translating%20codesystems/near/532225654
- **Snippet:** https://jira.hl7.org/browse/<b>FHIR-51614</b>


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51614.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-51614.md",
  "file_text": "# FHIR-51614: Better guidance for translating codes\n\n## Summary\n\n| Field          | Value                                |\n|----------------|--------------------------------------|\n| **Ticket**     | [FHIR-51614](https://jira.hl7.org/browse/FHIR-51614) |\n| **Status**     | Triaged                              |\n| **Type**       | Change Request                       |\n| **Priority**   | Medium                               |\n| **Work Group** | Terminology Infrastructure           |\n| **Specification** | FHIR Core (FHIR)                 |\n| **Reporter**   | Vadim Peretokin                      |\n| **Assignee**   | Unassigned                           |\n| **Labels**     | TEXTONLY                             |\n| **Created**    | 2025-08-01                           |\n| **Updated**    | 2026-01-20                           |\n\n## Problem Statement\n\nThe reporter identifies a usability gap in the FHIR spec regarding designations used for language translations. Both the CodeSystem and ValueSet resources contain nearly identical text describing how designations work, but there is a critical practical difference that is not clearly stated:\n\n- **CodeSystem supplements** are the correct mechanism for adding language translations to 3rd-party code systems.\n- **ValueSet designations** serve a different, more limited purpose \u2014 they assign alternative display text for use only within the context of a value set expansion, not for general-purpose translation.\n\nThe current spec text does not make this distinction clear, creating a \"footgun\" where implementers mistakenly add language designations to ValueSets instead of using CodeSystem supplements. The reporter had to consult Zulip to learn the correct approach.\n\nAdditionally, the reporter suggests the IG Publisher should emit a warning when language designations are added to ValueSets, since that pattern is almost always incorrect.\n\n## Key Discussion Points\n\n### Jira Comment (mjlawley, 2025-08-03)\n\nSuggests that the spec text should reference the designation use code `http://terminology.hl7.org/CodeSystem/hl7TermMaintInfra#preferredForLanguage` and that this code should be added to the `http://hl7.org/fhir/ValueSet/designation-use` ValueSet.\n\n### Zulip: [terminology] Better guidance for translating codesystems\n**URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Better%20guidance%20for%20translating%20codesystems  \n**Participants:** Vadim Peretokin, Grahame Grieve (2025-07-31 to 2025-08-01)\n\n- Vadim raised the issue and offered to file a ticket.\n- **Grahame Grieve** agreed a ticket should be filed. On the validator/IG Publisher suggestion, he noted: *\"I'm less sure about the validator bit \u2014 it's not wrong to put them in the value set, just a much restricted purpose.\"*\n\n### Zulip: [IG creation] \u2714 Translating 3rd party codesystems

... *(truncated, 9081 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51614.md with 8904 characters
```

</details>


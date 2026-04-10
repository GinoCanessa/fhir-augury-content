# Session Log: FHIR-53785

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-53785.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-53785` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 01:00:20 UTC |
| **Duration** | 111s |
| **Total Tool Calls** | 18 |
| **Total Tokens** | 324,672 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-53785
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-53785.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-53785", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-53785", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-53785", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-53785.md
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
  "id": "FHIR-53785",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-53785: Text Updates for Terminology Module Page

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Jessica Bota
- **Created:** 2026-01-05T16:16:52+00:00
- **Updated:** 2026-01-16T23:14:29+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53785

## Content
<p>In <b>4.0.1 Introduction</b> make the following changes:</p>

<p>1. Update the first sentence from:</p>

<p>"The Terminology Module provides an overview and guide to the FHIR resources, operations, coded datatypes and externally-defined standard and FHIR-defined terminologies that are used for representing and communicating coded, structured data in the FHIR core specification and profiles."</p>

<p>to:</p>

<p>"The Terminology Module is a foundational component of core FHIR specification.  Any terminology related resource type, operation or datatype is part of the Terminology Module."</p>

<p>2. Update the paragraph in 4.0.1 Introduction from:</p>

<p>"The primary terminology-related structures and their relationships are shown below:"</p>

<p>to</p>

<p>"The diagram below shows the relationship between terminology resource types." </p>

<p> </p>

<p>In <b>4.0.2 Index</b>, make the following changes:</p>

<p>1. Change name of section from "Operations" to "Terminology Specific Operations"</p>

<p>2. Add a column in the Operations section for NamingSystem and add links to the following operations:</p>

<p><a href="https://build.fhir.org/namingsystem-operation-preferred-id.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/namingsystem-operation-preferred-id.html</a> </p>

<p><a href="https://build.fhir.org/namingsystem-operation-translate-id.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/namingsystem-operation-translate-id.html</a> </p>

<p> </p>

<p>In <b>4.0.4 Common Use Cases</b>, make the following changes:</p>

<p>1. Replace "Create or reference a value set" with:</p>

<p>"Create, reference or expand a value set.<b>"</b></p>

<p>2. Replace the 3 "Record data" bullet points with one bullet point that states:</p>

<p>"Record codes, expressions and translations"</p>

<p>3. Collapse the "Validate" and "Look up" bullets into one bullet point that states:</p>

<p>"Validate or look up a display term for a code"</p>

<p>4. Replace "Map data between different terminologies" with:</p>

<p>"Create or reference a concept map"</p>

<p>5. Replace "Declare the capabilities of a terminology service" with:</p>

<p>"Operate a terminology service"</p>

<p> </p>

<p>In <b>4.0.5 Development Roadmap</b>, make the following changes:</p>

<p>1. Since all resources in FHIR are normative, update the text to say: </p>

<p>"The following terminology resources have been tested and are being used in production tooling are normative"</p>

<p>2. All resources should be listed together in one list</p>

## Comments (1)

### jsnell — 2026-01-05T16:20:59+00:00
<p>For historical purposes, this ticket was entered on behalf of TI co-chair review documented here: <a href="https://confluence.hl7.org/spaces/VOC/pages/256510055/FHIR+R6+Terminology+Content+Review" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/spaces/VOC/pages/256510055/FHIR+R6+Terminology+Content+Review</a></p>


## Snapshot
# FHIR-53785: Text Updates for Terminology Module Page

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Jessica Bota  
**Work Group:** Terminology Infrastructure  
**Specification:** FHIR Core (FHIR)  
**Created:** 2026-01-05  
**Updated:** 2026-01-16  

## Description

<p>In <b>4.0.1 Introduction</b> make the following changes:</p>

<p>1. Update the first sentence from:</p>

<p>"

... *(truncated, 6902 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-53785" (1 results)

- [jira] FHIR-53785 → [confluence] 256510055
  **Source:** Text Updates for Terminology Module Page
  **Type:** mentions
  **Context:** ...poses, this ticket was entered on behalf of TI co-chair review documented here: https://confluence.hl7.org/spaces/VOC/pages/256510055/FHIR+R6+Terminology+Conten...
  **Score:** 0.97
  **Updated:** 2026-01-16T23:14:29+00:00
**Warnings:**
- Value 'FHIR-53785' is not a valid Zulip message ID

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

Let me search for any Zulip discussion on the terminology content review and check for GitHub items.

<details>
<summary>`FhirAugury-query_zulip_messages` — terminology content review R6</summary>

**Result:**
```
No Zulip messages matched the query.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...

### [github] HL7/fhir:source/modules.html — source/modules.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules.html
- **Snippet:** ...Foundation <b>Module</b></a>)</li>
 <li>How are terminologies being used? (see <a href="<b>terminology</b>-<b>module</b>.html#uses"><b>Terminology</b> <b>Module</b></a...


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "terminology module, NamingSystem operations, terminology roadmap normative"
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 335045219 — [Terminology Infrastructure WG/committers] Terminology Module Development Roadmap
- **Score:** 0.04
- **Updated:** 2023-02-23T21:56:24+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Terminology%20Infrastructure%20WG%2Fcommitters/topic/Terminology%20Module%20Development%20Roadmap/near/335045219
- **Snippet:** ...I mean, TI co-chairs Can you please review the development roadmap in the <b>terminology</b> <b>module</b> page, thanks

### [zulip] 219680887 — [hapi] TerminologyCapabilities
- **Score:** 0.01
- **Updated:** 2020-12-12T01:09:47+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/hapi/topic/TerminologyCapabilities/near/219680887
- **Snippet:** http://hl7.org/fhir/<b>terminology</b>-<b>module</b>.html

### [zulip] 153843306 — [committers] Terminology Module
- **Score:** 0.01
- **Updated:** 2016-08-10T06:15:57+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/Terminology%20Module/near/153843306
- **Snippet:** thx

### [zulip] 153843305 — [committers] Terminology Module
- **Score:** 0.00
- **Updated:** 2016-08-10T06:15:55+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/Terminology%20Module/near/153843305
- **Snippet:** ok I'll look now

### [zulip] 153932203 — [terminology] Terminology Capabilty
- **Score:** 0.00
- **Updated:** 2018-01-28T20:01:53+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/Terminology%20Capabilty/near/153932203
- **Snippet:** yes, we need to make some updates to the <b>Terminology</b> <b>Module</b> page - and other places

### [zulip] 153955952 — [committers] tracker-item
- **Score:** 0.00
- **Updated:** 2018-05-04T12:26:38+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/tracker-item/near/153955952
- **Snippet:** GF#16295 : <b>Terminology</b> <b>module</b> introductory figure posted by fmacary

### [zulip] 153840881 — [committers] Conformance Module
- **Score:** 0.00
- **Updated:** 2016-07-25T08:07:40+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/Conformance%20Module/near/153840881
- **Snippet:** Dependency on the <b>terminology</b> <b>module</b> - it's there (under the image when discussing the dotted resources), but I'll make...

### [zulip] 153843303 — [committers] fhir-svn
- **Score:** 0.00
- **Updated:** 2016-08-10T06:09:07+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/fhir-svn/near/153843303
- **Snippet:** rhausam pushed to branch master @9610 : Initial commit of <b>Terminology</b> <b>module</b>.

### [zulip] 153843510 — [committers] fhir-svn
- **Score:** 0.00
- **Updated:** 2016-08-11T01:58:08+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/fhir-svn/near/153843510
- **Snippet:** rhausam pushed to branch master @9646 : Additional and updated <b>terminology</b> <b>module</b> content.

### [zulip] 153930251 — [committers] tracker-item
- **Score:** 0.00
- **Updated:** 2018-01-23T04:53:17+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/committers/topic/tracker-item/near/153930251
- **Snippet:** GF#14541 : <b>Terminology</b> <b>Module</b> needs CodeSystem $validate-code operation posted by rhausam


```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-53785.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-53785.md",
  "file_text": "# FHIR-53785: Text Updates for Terminology Module Page\n\n## Summary\n\n| Field         | Value                                      |\n|---------------|--------------------------------------------|\n| **Ticket**    | [FHIR-53785](https://jira.hl7.org/browse/FHIR-53785) |\n| **Type**      | Change Request                             |\n| **Priority**  | Highest                                    |\n| **Status**    | Triaged                                    |\n| **Resolution**| Unresolved                                 |\n| **Work Group**| Terminology Infrastructure                 |\n| **Specification** | FHIR Core (FHIR)                      |\n| **Reporter**  | Jessica Bota                               |\n| **Assignee**  | Unassigned                                 |\n| **Created**   | 2026-01-05                                 |\n| **Updated**   | 2026-01-16                                 |\n\n## Description\n\nThis ticket requests a set of editorial text updates to the [Terminology Module page](https://build.fhir.org/terminology-module.html) across four sections. The changes were entered on behalf of TI co-chair review as part of the broader **FHIR R6 Terminology Content Review** effort documented on [Confluence](https://confluence.hl7.org/spaces/VOC/pages/256510055/FHIR+R6+Terminology+Content+Review).\n\n### Specific Changes Requested\n\n**Section 4.0.1 Introduction:**\n1. Replace the opening sentence with a shorter, more direct statement: *\"The Terminology Module is a foundational component of core FHIR specification. Any terminology related resource type, operation or datatype is part of the Terminology Module.\"*\n2. Change the diagram lead-in text from *\"The primary terminology-related structures and their relationships are shown below:\"* to *\"The diagram below shows the relationship between terminology resource types.\"*\n\n**Section 4.0.2 Index:**\n1. Rename the \"Operations\" subsection to **\"Terminology Specific Operations\"**.\n2. Add a **NamingSystem** column in the Operations table linking to:\n   - [NamingSystem $preferred-id](https://build.fhir.org/namingsystem-operation-preferred-id.html)\n   - [NamingSystem $translate-id](https://build.fhir.org/namingsystem-operation-translate-id.html)\n\n**Section 4.0.4 Common Use Cases:**\n1. Replace *\"Create or reference a value set\"* \u2192 *\"Create, reference or expand a value set.\"*\n2. Consolidate three \"Record data\" bullet points into one: *\"Record codes, expressions and translations\"*\n3. Collapse \"Validate\" and \"Look up\" bullets into: *\"Validate or look up a display term for a code\"*\n4. Replace *\"Map data between different terminologies\"* \u2192 *\"Create or reference a concept map\"*\n5. Replace *\"Declare the capabilities of a terminology service\"* \u2192 *\"Operate a terminology service\"*\n\n**Section 4.0.5 Development Roadmap:**\n1. Upda

... *(truncated, 9279 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-53785.md with 9019 characters
```

</details>

### Turn 4

**Assistant:**

Let me fetch the most closely related tickets for additional context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53785: Text Updates for Terminology Module Page

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Jessica Bota
- **Created:** 2026-01-05T16:16:52+00:00
- **Updated:** 2026-01-16T23:14:29+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53785

## Content
<p>In <b>4.0.1 Introduction</b> make the following changes:</p>

<p>1. Update the first sentence from:</p>

<p>"The Terminology Module provides an overview and guide to the FHIR resources, operations, coded datatypes and externally-defined standard and FHIR-defined terminologies that are used for representing and communicating coded, structured data in the FHIR core specification and profiles."</p>

<p>to:</p>

<p>"The Terminology Module is a foundational component of core FHIR specification.  Any terminology related resource type, operation or datatype is part of the Terminology Module."</p>

<p>2. Update the paragraph in 4.0.1 Introduction from:</p>

<p>"The primary terminology-related structures and their relationships are shown below:"</p>

<p>to</p>

<p>"The diagram below shows the relationship between terminology resource types." </p>

<p> </p>

<p>In <b>4.0.2 Index</b>, make the following changes:</p>

<p>1. Change name of section from "Operations" to "Terminology Specific Operations"</p>

<p>2. Add a column in the Operations section for NamingSystem and add links to the following operations:</p>

<p><a href="https://build.fhir.org/namingsystem-operation-preferred-id.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/namingsystem-operation-preferred-id.html</a> </p>

<p><a href="https://build.fhir.org/namingsystem-operation-translate-id.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/namingsystem-operation-translate-id.html</a> </p>

<p> </p>

<p>In <b>4.0.4 Common Use Cases</b>, make the following changes:</p>

<p>1. Replace "Create or reference a value set" with:</p>

<p>"Create, reference or expand a value set.<b>"</b></p>

<p>2. Replace the 3 "Record data" bullet points with one bullet point that states:</p>

<p>"Record codes, expressions and translations"</p>

<p>3. Collapse the "Validate" and "Look up" bullets into one bullet point that states:</p>

<p>"Validate or look up a display term for a code"</p>

<p>4. Replace "Map data between different terminologies" with:</p>

<p>"Create or reference a concept map"</p>

<p>5. Replace "Declare the capabilities of a terminology service" with:</p>

<p>"Operate a terminology service"</p>

<p> </p>

<p>In <b>4.0.5 Development Roadmap</b>, make the following changes:</p>

<p>1. Since all resources in FHIR are normative, update the text to say: </p>

<p>"The following terminology resources have been tested and are being used in production tooling are normative"</p>

<p>2. All resources should be listed together in one list</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-54129: CodeSystem Text Technical Corrections

- **status:** Resolved - change required
- **type:** Technical Correction
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Carmela A. Couderc
- **Created:** 2026-01-13T19:53:29+00:00
- **Updated:** 2026-04-09T20:57:54+00:00
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

<p>The FHIR terminology specification is based on the concepts of code system defined in the Terminology Fundamentals.</p>

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
	<li>Whether the code system exhibits concept permanence, whether it defines a compositional grammar, and whether the <font color="#ff0000">concept codes</font> that it defines are case sensitive</li>
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

<p>Note that the important existing (large) code systems (SNOMED CT, LOINC, RxNorm, ICD family, etc.) all have their own maintenance systems and distribution formats, and CodeSystem is generally not an efficient way to distribute their content, though it is used as one way of declaring the filters and properties associated with those cod

... *(truncated, 7894 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-54107: Remove Section 4.3.0.1 External Code Systems and Reference THO

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Carmela A. Couderc
- **Created:** 2026-01-13T16:34:40+00:00
- **Updated:** 2026-01-17T15:59:40+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-54107

## Content
<p>The information in this section repeats content in THO. Now that the "Using xxx with HL7 Standards" has moved to THO, there is no need to maintain in two places. </p>

<p>Suggested changes:</p>

<p><a href="https://hl7.org/fhir/6.0.0-ballot4/terminologies-systems.html" class="external-link" target="_blank" rel="nofollow noopener"><ins>Remove section 4.3.0.1 from this page.</ins>  https://hl7.org/fhir/6.0.0-ballot4/terminologies-systems.html</a></p>

<p>Remove the sentence: Don't see what you're looking for here: See Registering Code Systems for further advice.</p>

<p>Change the existing text</p>

<p>From this:</p>

<p>This is a subset of a much larger list of known code systems, and only details code systems for which FHIR specific usage documentation is provided. For other code systems, see <a href="https://terminology.hl7.org/external_code_systems.html" class="external-link" target="_blank" rel="nofollow noopener">terminology.hl7.org </a>.</p>

<p>To:</p>

<p>For code systems defined external to HL7, see <a href="https://terminology.hl7.org/external_code_systems.html" class="external-link" target="_blank" rel="nofollow noopener">terminology.hl7.org </a>. Some code system publishers have provided information about how to use their code system with HL7 standards. You will find that information at the same link.</p>

<p>Important Notes changes</p>
<ol>
	<li>remove the first bullet</li>
	<li>change the second bullet
	<ol>
		<li>from: The external terminology content provided in the Defined Externally tab is provided for convenience and should not be considered authoritative nor normative.</li>
		<li>To: The external terminology content provided in the External Content tab is provided for convenience and should not be considered authoritative nor normative</li>
	</ol>
	</li>
</ol>


```

</details>

### Turn 5

**Assistant:**

Found a related ticket FHIR-53785. Let me gather its details and search for additional context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-53785: Text Updates for Terminology Module Page

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Jessica Bota
- **Created:** 2026-01-05T16:16:52+00:00
- **Updated:** 2026-01-16T23:14:29+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53785

## Content
<p>In <b>4.0.1 Introduction</b> make the following changes:</p>

<p>1. Update the first sentence from:</p>

<p>"The Terminology Module provides an overview and guide to the FHIR resources, operations, coded datatypes and externally-defined standard and FHIR-defined terminologies that are used for representing and communicating coded, structured data in the FHIR core specification and profiles."</p>

<p>to:</p>

<p>"The Terminology Module is a foundational component of core FHIR specification.  Any terminology related resource type, operation or datatype is part of the Terminology Module."</p>

<p>2. Update the paragraph in 4.0.1 Introduction from:</p>

<p>"The primary terminology-related structures and their relationships are shown below:"</p>

<p>to</p>

<p>"The diagram below shows the relationship between terminology resource types." </p>

<p> </p>

<p>In <b>4.0.2 Index</b>, make the following changes:</p>

<p>1. Change name of section from "Operations" to "Terminology Specific Operations"</p>

<p>2. Add a column in the Operations section for NamingSystem and add links to the following operations:</p>

<p><a href="https://build.fhir.org/namingsystem-operation-preferred-id.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/namingsystem-operation-preferred-id.html</a> </p>

<p><a href="https://build.fhir.org/namingsystem-operation-translate-id.html" class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/namingsystem-operation-translate-id.html</a> </p>

<p> </p>

<p>In <b>4.0.4 Common Use Cases</b>, make the following changes:</p>

<p>1. Replace "Create or reference a value set" with:</p>

<p>"Create, reference or expand a value set.<b>"</b></p>

<p>2. Replace the 3 "Record data" bullet points with one bullet point that states:</p>

<p>"Record codes, expressions and translations"</p>

<p>3. Collapse the "Validate" and "Look up" bullets into one bullet point that states:</p>

<p>"Validate or look up a display term for a code"</p>

<p>4. Replace "Map data between different terminologies" with:</p>

<p>"Create or reference a concept map"</p>

<p>5. Replace "Declare the capabilities of a terminology service" with:</p>

<p>"Operate a terminology service"</p>

<p> </p>

<p>In <b>4.0.5 Development Roadmap</b>, make the following changes:</p>

<p>1. Since all resources in FHIR are normative, update the text to say: </p>

<p>"The following terminology resources have been tested and are being used in production tooling are normative"</p>

<p>2. All resources should be listed together in one list</p>

## Comments (1)

### jsnell — 2026-01-05T16:20:59+00:00
<p>For historical purposes, this ticket was entered on behalf of TI co-chair review documented here: <a href="https://confluence.hl7.org/spaces/VOC/pages/256510055/FHIR+R6+Terminology+Content+Review" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/spaces/VOC/pages/256510055/FHIR+R6+Terminology+Content+Review</a></p>


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "zulip",
  "values": "TerminologyCapabilities, terminology module, terminology-module"
}
```

**Result:**
```
## Search Results (10 total, showing 10)

### [zulip] 447221438 — [terminology] WHO Code systems
- **Score:** 0.09
- **Updated:** 2024-06-26T13:38:38+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/WHO%20Code%20systems/near/447221438
- **Snippet:** <b>TerminologyCapabilities</b>.codeSystem.uri <b>TerminologyCapabilities</b>.codeSystem.version.code

### [zulip] 481550181 — [Terminology Service Test Cases] TerminologyCapabilities
- **Score:** 0.06
- **Updated:** 2024-11-10T10:49:01+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Terminology%20Service%20Test%20Cases/topic/TerminologyCapabilities/near/481550181
- **Snippet:** @Michael Lawley I'm extending the test cases to check the <b>TerminologyCapabilities</b> statement.

### [zulip] 153956110 — [terminology] TerminologyCapabilities
- **Score:** 0.01
- **Updated:** 2018-05-05T04:55:11+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/153956110
- **Snippet:** @Peter Jordan wouldn't [base]/<b>TerminologyCapabilities</b> return a Bundle containing all the <b>TerminologyCapabilities</b> stored on the server?

### [zulip] 174964361 — [hapi] TerminologyCapabilities
- **Score:** 0.01
- **Updated:** 2019-09-05T11:28:15+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/hapi/topic/TerminologyCapabilities/near/174964361
- **Snippet:** Our "fix" was to extend <b>TerminologyCapabilities</b> and add in implements IBaseConformance :-)

### [zulip] 154014330 — [terminology] TerminologyCapabilities
- **Score:** 0.00
- **Updated:** 2018-10-31T21:07:29+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/154014330
- **Snippet:** The vocab WG needs to make a formal proposal for <b>TerminologyCapabilities</b> resource

### [zulip] 153956831 — [terminology] TerminologyCapabilities
- **Score:** 0.00
- **Updated:** 2018-05-07T22:13:38+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/153956831
- **Snippet:** @Peter Jordan what are your three requests? 1. CapabilityStatement - /metadata 2. <b>TerminologyCapabilities</b> - /??? 3. OperationDefinition???

### [zulip] 153955497 — [terminology] TerminologyCapabilities
- **Score:** 0.00
- **Updated:** 2018-05-02T20:47:09+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/153955497
- **Snippet:** When responding metadata request, should a terminology server returns CapabilityStatement or <b>TerminologyCapabilities</b> or both?

### [zulip] 153955523 — [terminology] TerminologyCapabilities
- **Score:** 0.00
- **Updated:** 2018-05-02T21:16:59+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/153955523
- **Snippet:** ...The following request will return the (trial) <b>TerminologyCapabilities</b> resource from my server... GET http://its.patientsfirst.org.nz/RestService.svc...

### [zulip] 153955502 — [terminology] TerminologyCapabilities
- **Score:** 0.00
- **Updated:** 2018-05-02T20:54:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/153955502
- **Snippet:** Then what is the usage of <b>TerminologyCapabilities</b> resource? I though that is a replacement of CapabilityStatement.

### [zulip] 153956265 — [terminology] TerminologyCapabilities
- **Score:** 0.00
- **Updated:** 2018-05-06T21:21:09+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/TerminologyCapabilities/near/153956265
- **Snippet:** Not sure, but <b>TerminologyCapabilities</b>.codeSystem is 0...* and (interestingly) each codeSystem has a canonical uri element.


```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (10 total, showing 10)

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology</b>-<b>module</b>.html">
                    <span><b>Terminology</b></span>
                </a>
            </p>
            <p class="content">
                <a href="codesystem.html">CodeSystem...

### [github] HL7/fhir:source/modules-fragment.html — source/modules-fragment.html
- **Score:** 1.00
- **URL:** https://github.com/HL7/fhir/blob/main/source/modules-fragment.html
- **Snippet:** ...url('<b>terminology</b>.png');" href="<b>terminology<

... *(truncated, 4674 chars total)*
```

</details>


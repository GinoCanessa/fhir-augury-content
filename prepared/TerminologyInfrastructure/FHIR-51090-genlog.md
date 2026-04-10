# Session Log: FHIR-51090

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-51090.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `retry-FHIR-51090` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:44:43 UTC |
| **Duration** | 105s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 319,234 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-51090
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51090.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-51090", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-51090", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-51090", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51090.md
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
  "id": "FHIR-51090",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51090: Define default-system-version and deprecate system-version

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bryn Rhodes
- **labels:** Operation
- **Created:** 2025-06-12T23:38:31+00:00
- **Updated:** 2026-02-25T20:37:01+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51090

## Content
<p>The ValueSet/$expand and ValueSet/$validate-code operations have a system-version parameter for specifying the version of a code system used in the operation. They also both have a default-valueset-version parameter, which serves the same purpose but for value sets used in the operation. The default-valueset-version naming is a clearer indication of what is happening, so we propose to:</p>

<p>Add default-system-version, identical to system-version, and<br/>
Deprecate system-version</p>

<p>in both operations.</p>

## Comments (3)

### bryn.rhodes — 2026-02-25T20:37:01+00:00
<p>I agree, this hybrid wording is better</p>

### mjlawley — 2026-02-25T00:59:38+00:00
<p>We have pre-adopted support for all the variations in our R4 implementation.<br/>
As a general principle, we preference the more modern variants, but also require that if multiple "equivalent" (renamed) parameters are supplied that they have the same value - there is no "overriding" if the parameters are semantically equivalent.</p>

<p>I would prefer this hybrid rewording:</p>

<p>Specifies a default code system version to use for the operation, IF the value set definition itself does not specify which code system version to use. The format is the same as a canonical URL: <span class="error">&#91;system&#93;</span>|<span class="error">&#91;version&#93;</span> - e.g. <a href="http://loinc.org" class="external-link" target="_blank" rel="nofollow noopener">http://loinc.org</a>|2.56.<br/>
Note that this is a different parameter to systemVersion.</p>

<p>systemVersion is the version of the CodeSystem referenced in the system (IN) parameter, as opposed to any of the CodeSystems referenced in the ValueSet itself (themselves, in the case of included ValueSets).</p>

<p>Ontoserver uses it as a default system version fallback if an explicit default system-version has not been specified.</p>

### carmela_couderc — 2025-12-15T23:29:26+00:00
<p>Discussed on the 2025-12-15 tracker call. </p>

<p>The request is to rename system-version by going through the mechanics of deprecating system-version and adding default-system-version. </p>

<p>Discussion: concern about two ways to declare the code system. Leaning towards rejecting this proposal. </p>

<p>There are two parameters systemVersion and system-version. Agree these are similarly named. </p>

<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=mjlawley" class="user-hover" rel="mjlawley">Michael Lawley</a> Would like your opinion on whether this change would cause any issues? Attendees are concerned that this change (deprecating and adding) could cause issues. Does your server support all the different input parameters declaring versions of either code systems or value sets? Have you figured out which one overrides the other?</p>

<p>Attendees sense that the description of system-version could be updated to include the word "default" rather than create the deprecated/active scenario. </p>

<p>Current description:  Specifies a version to use for a system, if the value set does not specify which one to use. The format is the same as a canonical URL: <span class="error">&#91;system&#93;</span>|<span class="error">&#91;version&#93;</span> - e.g. <a href="http://loinc.org" class="external-link" target="_blank" rel="nofollow noopener">http://loinc.org</a>|2.56. Note that this is a different parameter to systemVersion</p>

<p>Change to:</p>

<p>Specifies a default code system version to use for the operation, IF the v

... *(truncated, 9120 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51090".
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
<summary>`FhirAugury-get_item`</summary>

**Arguments:**
```json
{
  "source": "jira",
  "id": "FHIR-51090",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-51090: Define default-system-version and deprecate system-version

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Terminology Infrastructure
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bryn Rhodes
- **labels:** Operation
- **Created:** 2025-06-12T23:38:31+00:00
- **Updated:** 2026-02-25T20:37:01+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51090

## Content
<p>The ValueSet/$expand and ValueSet/$validate-code operations have a system-version parameter for specifying the version of a code system used in the operation. They also both have a default-valueset-version parameter, which serves the same purpose but for value sets used in the operation. The default-valueset-version naming is a clearer indication of what is happening, so we propose to:</p>

<p>Add default-system-version, identical to system-version, and<br/>
Deprecate system-version</p>

<p>in both operations.</p>

## Comments (3)

### bryn.rhodes — 2026-02-25T20:37:01+00:00
<p>I agree, this hybrid wording is better</p>

### mjlawley — 2026-02-25T00:59:38+00:00
<p>We have pre-adopted support for all the variations in our R4 implementation.<br/>
As a general principle, we preference the more modern variants, but also require that if multiple "equivalent" (renamed) parameters are supplied that they have the same value - there is no "overriding" if the parameters are semantically equivalent.</p>

<p>I would prefer this hybrid rewording:</p>

<p>Specifies a default code system version to use for the operation, IF the value set definition itself does not specify which code system version to use. The format is the same as a canonical URL: <span class="error">&#91;system&#93;</span>|<span class="error">&#91;version&#93;</span> - e.g. <a href="http://loinc.org" class="external-link" target="_blank" rel="nofollow noopener">http://loinc.org</a>|2.56.<br/>
Note that this is a different parameter to systemVersion.</p>

<p>systemVersion is the version of the CodeSystem referenced in the system (IN) parameter, as opposed to any of the CodeSystems referenced in the ValueSet itself (themselves, in the case of included ValueSets).</p>

<p>Ontoserver uses it as a default system version fallback if an explicit default system-version has not been specified.</p>

### carmela_couderc — 2025-12-15T23:29:26+00:00
<p>Discussed on the 2025-12-15 tracker call. </p>

<p>The request is to rename system-version by going through the mechanics of deprecating system-version and adding default-system-version. </p>

<p>Discussion: concern about two ways to declare the code system. Leaning towards rejecting this proposal. </p>

<p>There are two parameters systemVersion and system-version. Agree these are similarly named. </p>

<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=mjlawley" class="user-hover" rel="mjlawley">Michael Lawley</a> Would like your opinion on whether this change would cause any issues? Attendees are concerned that this change (deprecating and adding) could cause issues. Does your server support all the different input parameters declaring versions of either code systems or value sets? Have you figured out which one overrides the other?</p>

<p>Attendees sense that the description of system-version could be updated to include the word "default" rather than create the deprecated/active scenario. </p>

<p>Current description:  Specifies a version to use for a system, if the value set does not specify which one to use. The format is the same as a canonical URL: <span class="error">&#91;system&#93;</span>|<span class="error">&#91;version&#93;</span> - e.g. <a href="http://loinc.org" class="external-link" target="_blank" rel="nofollow noopener">http://loinc.org</a>|2.56. Note that this is a different parameter to systemVersion</p>

<p>Change to:</p>

<p>Specifies a default code system version to use for the operation, IF the v

... *(truncated, 9120 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-51090".
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51090.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-51090.md",
  "file_text": "# FHIR-51090: Define default-system-version and deprecate system-version\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-51090](https://jira.hl7.org/browse/FHIR-51090) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | Terminology Infrastructure |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter** | Bryn Rhodes |\n| **Assignee** | Unassigned |\n| **Labels** | Operation |\n| **Created** | 2025-06-12 |\n| **Updated** | 2026-02-25 |\n\n## Description\n\nThe `ValueSet/$expand` and `ValueSet/$validate-code` operations have a `system-version` parameter for specifying the version of a code system used in the operation. They also both have a `default-valueset-version` parameter, which serves the same purpose but for value sets. The `default-valueset-version` naming is clearer, so the proposal is to:\n\n1. Add `default-system-version`, identical to `system-version`\n2. Deprecate `system-version`\n\nin both operations.\n\n## Keywords\n\n- `system-version`, `default-system-version`, `default-valueset-version`\n- `ValueSet/$expand`, `ValueSet/$validate-code`\n- parameter naming, deprecation, consistency\n- `systemVersion` (distinct parameter \u2014 version of CodeSystem referenced in `system` IN parameter)\n\n## Discussion History\n\n### Tracker Call \u2014 2025-12-15 (carmela_couderc)\n\nDiscussed on the 2025-12-15 tracker call. Key points:\n- **Concern** about having two ways to declare the code system version (deprecated `system-version` plus new `default-system-version`).\n- Attendees were **leaning towards rejecting** the deprecate-and-add proposal.\n- Noted the confusing similarity between `systemVersion` (CamelCase, a different parameter) and `system-version` (kebab-case).\n- Proposed **alternative**: update the *description* of `system-version` to include the word \"default\" rather than creating a deprecated/active scenario.\n- Proposed updated description: *\"Specifies a default code system version to use for the operation, IF the value set definition does not specify a code system version.\"*\n- Michael Lawley was asked for input on implementation impact.\n- Ticket was slated for the joint TI/FHIR-I session in January 2026.\n\n### Michael Lawley \u2014 2026-02-25\n\n- Ontoserver (R4) has pre-adopted support for all parameter name variations.\n- Requires that if multiple \"equivalent\" (renamed) parameters are supplied, they must have the same value \u2014 no overriding.\n- Prefers a **hybrid rewording**: *\"Specifies a default code system version to use for the operation, IF the value set definition itself does not specify which code system version to use. [...] Note that this is a different parameter to systemVersion.\"*\n- Clarified that `systemVersion` is the version of the CodeSystem referenced in the `sy

... *(truncated, 11174 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-51090.md with 10942 characters
```

</details>


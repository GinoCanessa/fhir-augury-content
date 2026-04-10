# Session Log: FHIR-53381

**Phase:** prepared
**Work Group:** Security
**Source File:** `prepared/Security/FHIR-53381.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-53381` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 20:05:38 UTC |
| **Duration** | 79s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 216,633 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-53381
## Work Group: Security
## Output File: C:\ai\git\fhir-augury-content\prepared\Security\FHIR-53381.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-53381", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-53381", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-53381", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Security\FHIR-53381.md
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
  "id": "FHIR-53381",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-53381: "Shall" statements too strong for all use cases

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Security
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** Block-Vote-2
- **Created:** 2025-11-06T22:38:02+00:00
- **Updated:** 2026-03-30T17:17:39+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-53381

## Content
<p>The security page includes a number of SHALL statements, including:</p>
<ul>
	<li><blockquote><p>Audit of the Access Control Decision: Any Access Control decision to deny an activity SHALL be recorded, and Access Control decisions to permit access SHOULD be recorded. The record SHOULD use the FHIR AuditEvent Resource.</p></blockquote></li>
</ul>


<p>This requirement to record any deny decision is too strong for all use cases for FHIR and an absence of this capability would prevent an implementation from claiming conformance with FHIR.</p>

<p>While it is certainly a best practice, and highly recommended, I don't think we can mandate that failure to log denied access means your implementation is non-compliant.</p>

<p>Please change this to a SHOULD, or make the language conditional on factors such as environment, logging capabilities, etc.</p>

<p>Review other SHALL statements to ensure that they are appropriate for all implementations in all environments.</p>

## Comments (3)

### john_moehrke — 2026-03-30T17:17:39+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=esilver" class="user-hover" rel="esilver">Elliot Silver</a> has agreed to this change on the call today.</p>

<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=lloyd" class="user-hover" rel="lloyd">Lloyd McKenzie</a> would changing to SHOULD be acceptable to you?</p>

### mckenzie — 2026-03-23T21:34:36+00:00
<p>It doesn't matter if it's good policy.  It's not reasonable to say "Any system that doesn't do this isn't FHIR conformant".  There will be some systems that don't maintain an audit log of <b>anything</b>.  And that's fine.  For example, a test server wouldn't necessarily need to have auditing capability.  Because there are use-cases where audit isn't necessary, and because it's not HL7's place to set expectations for audit in general, this shouldn't be any stronger than SHOULD.</p>

### john_moehrke — 2026-02-19T15:56:04+00:00
<p>not recording access control denies is very much not a good policy. It is these that show you where the edges of your policy are being probed, and where people are trying to go beyond their scope.</p>


## Snapshot
# FHIR-53381: "Shall" statements too strong for all use cases

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Persuasive  
**Assignee:** Unassigned  
**Reporter:** Elliot Silver  
**Work Group:** Security  
**Specification:** FHIR Core (FHIR)  
**Labels:** Block-Vote-2  
**Created:** 2025-11-06  
**Updated:** 2026-03-30  
**Resolved:** 2026-03-30  

## Description

<p>The security page includes a number of SHALL statements, including:</p>
<ul>
	<li><blockquote><p>Audit of the Access Control Decision: Any Access Control decision to deny an activity SHALL be recorded, and Access Control decisions to permit access SHOULD be recorded. The record SHOULD use the FHIR AuditEvent Resource.</p></blockquote></li>
</ul>


<p>This requirement to record any deny decision is too strong for all use cases for FHIR and an absence of this capability would prevent an implementation from claiming conformance with FHIR.</p>

<p>While it is certainly a best practice, and highly recommended, I don't think we can mandate that failure to log denied access means your implementation is non-compliant.</p>

<p>Please change this to a SHOULD, or make the language conditional on factors such as environment, logging capabilities, etc.</p>

<p>Review other SHALL statements to ensu

... *(truncated, 5312 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-53381".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Security\FHIR-53381.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Security\\FHIR-53381.md",
  "file_text": "# FHIR-53381: \"Shall\" statements too strong for all use cases\n\n## Ticket Summary\n\n| Field         | Value |\n|---------------|-------|\n| **Key**       | [FHIR-53381](https://jira.hl7.org/browse/FHIR-53381) |\n| **Status**    | Triaged |\n| **Type**      | Change Request |\n| **Priority**  | Medium |\n| **Resolution**| Persuasive |\n| **Work Group**| Security |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter**  | Elliot Silver |\n| **Assignee**  | Unassigned |\n| **Labels**    | Block-Vote-2 |\n| **Created**   | 2025-11-06 |\n| **Updated**   | 2026-03-30 |\n\n## Problem Statement\n\nThe FHIR security page (`security.html`) contains a **SHALL** statement requiring that any Access Control decision to deny an activity must be recorded (audited). The submitter argues this conformance requirement is too strong for all use cases\u2014some implementations (e.g., test servers) may legitimately not maintain audit logs, and mandating this would prevent them from claiming FHIR conformance. The submitter requests changing **SHALL** to **SHOULD**, or making the language conditional on environment/capabilities.\n\n### Quoted Language Under Dispute\n\n> \"Audit of the Access Control Decision: Any Access Control decision to deny an activity **SHALL** be recorded, and Access Control decisions to permit access **SHOULD** be recorded. The record **SHOULD** use the FHIR AuditEvent Resource.\"\n\n## Discussion Summary\n\nThree comments capture a substantive debate:\n\n1. **John Moehrke (2026-02-19)** \u2014 Defended the **SHALL**, noting that recording access control denials is critical security practice: \"It is these that show you where the edges of your policy are being probed, and where people are trying to go beyond their scope.\"\n\n2. **Lloyd McKenzie (2026-03-23)** \u2014 Supported the change, arguing it is unreasonable to declare systems non-conformant for lacking audit logging. Cited test servers as legitimate use cases where audit is unnecessary and noted \"it's not HL7's place to set expectations for audit in general.\"\n\n3. **John Moehrke (2026-03-30)** \u2014 Reported that Elliot Silver agreed to the proposed change on a call, and asked Lloyd McKenzie if changing to **SHOULD** would be acceptable.\n\nThe resolution description states: **\"Will change the SHALL to a SHOULD.\"**\n\n## Keywords\n\n`security`, `SHALL`, `SHOULD`, `conformance`, `audit`, `access control`, `deny`, `AuditEvent`, `security.html`, `best practice`\n\n## Related Tickets\n\n| Key | Title | Relevance |\n|-----|-------|-----------|\n| [FHIR-28908](https://jira.hl7.org/browse/FHIR-28908) | Do not include policy positions as conformance statements | Same theme: policy positions should not be encoded as conformance SHALL statements. Addressed US Da Vinci HRex but raises identical principle about audit/access control requirements being too prescriptive. Published; resolved Not

... *(truncated, 7127 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Security\FHIR-53381.md with 6953 characters
```

</details>


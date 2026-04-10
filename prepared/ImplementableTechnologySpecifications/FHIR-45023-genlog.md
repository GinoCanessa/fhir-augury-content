# Session Log: FHIR-45023

**Phase:** prepared
**Work Group:** ImplementableTechnologySpecifications
**Source File:** `prepared/ImplementableTechnologySpecifications/FHIR-45023.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-45023` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:31:16 UTC |
| **Duration** | 119s |
| **Total Tool Calls** | 19 |
| **Total Tokens** | 310,899 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-45023
## Work Group: Implementable Technology Specifications
## Output File: C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-45023.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-45023", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-45023", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-45023", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-45023.md
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
  "id": "FHIR-45023",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-45023: Need a canonicalization for Bundle that excludes .signature

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Implementable Technology Specifications
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** John Moehrke
- **Created:** 2024-03-21T15:12:54+00:00
- **Updated:** 2025-06-16T14:40:48+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-45023

## Content
<p>Both XML and JSON do not have a canonicalization that can be used with a Bundle.signature digital signature. There is a need for a canonicalization that excludes the .signature element so that the signature across the bundle can be calculated prior to inserting that signature. </p>

<p> </p>

<p>This is needed for any kind of Bundle, but might also need to be added to the #document canonicalization.</p>

## Comments (10)

### john_moehrke — 2025-06-16T14:40:48+00:00
<p><a href="https://chat.fhir.org/#narrow/channel/179247-Security-and-Privacy/topic/What.20to.20sign.3F" class="external-link" target="_blank" rel="nofollow noopener">https://chat.fhir.org/#narrow/channel/179247-Security-and-Privacy/topic/What.20to.20sign.3F</a></p>

### john_moehrke — 2024-07-30T16:23:25+00:00
<p>This is important to resolve by R6</p>

### john_moehrke — 2024-03-27T14:42:45+00:00
<p>should the exclusion be not on the whole Signature datatype, but just the Signature.data element of the Signature datatype? Meaning that the other elements of the signature do need to be populated prior to calculating the signature.</p>

### john_moehrke — 2024-03-27T14:41:29+00:00
<p>The canonicalization algorithm should be applicable to any FHIR resource that has an embedded signature element, where the signature is across that resource and will be embedded in that element? Thus it would be defined to cover the resource with the exclusion of the .signature element. This would work for the Bundle resource, but would also work for signing a Provenance.</p>

<p>This canonicalization could then be recommended to all the places where the Signature datatype has been included, AND where the signature will be embedded into that signature element. </p>

<p>That is, if that is possible.</p>

### john_moehrke — 2024-03-21T17:56:44+00:00
<p>I am told by <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=jmandel" class="user-hover" rel="jmandel">Josh Mandel</a>  that the JSON canonicalization needs to reference RFC8785</p>

### mckenzie — 2024-03-21T16:38:36+00:00
<p>I'm not arguing for that.  I think there are valid use-cases for Bundle.signature and we should define the technical infrastructure to allow it to be used consistently.</p>

### john_moehrke — 2024-03-21T16:19:14+00:00
<p>then should we remove the Bundle.signature element? Grahame asked for it to be targeting normative in R6.</p>

<p>Either solution is fine with me. Anyone needing a Bundle signature could just as easily use an extension.</p>

### mckenzie — 2024-03-21T15:57:56+00:00
<p>Agree that Bundle.signature is somewhat useless without it.  Though the fact that we've gotten this far without it suggests that there's only a small portion of the implementer community that will use it.</p>

### john_moehrke — 2024-03-21T15:14:44+00:00
<p>These pages are owned by ITS, but would seem FHIR-I and Security would be interested in the solution.</p>

### john_moehrke — 2024-03-21T15:13:43+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=lloyd" class="user-hover" rel="lloyd">Lloyd McKenzie</a> <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=GrahameGrieve" class="user-hover" rel="GrahameGrieve">Grahame Grieve</a>  – Would you agree we need this canonicalization?</p>


## Snapshot
# FHIR-45023: Need a canonicalization for Bundle that excludes .signature

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Ass

... *(truncated, 7394 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-45023" (7 results)

- [jira] FHIR-45023 → [zulip] 179247:What.20to.20sign.3F
  **Source:** Need a canonicalization for Bundle that excludes .signature
  **Type:** mentions
  **Context:** https://chat.fhir.org/#narrow/channel/179247-Security-and-Privacy/topic/What.20t...
  **Score:** 0.75
  **Updated:** 2025-06-16T14:40:48+00:00
- [jira] FHIR-45023 → [fhir] Bundle.signature
  **Source:** Need a canonicalization for Bundle that excludes .signature
  **Type:** mentions
  **Context:** Both XML and JSON do not have a canonicalization that can be used with a Bundle.signature digital signature. There is a need for a canonicalization that ...
  **Score:** 0.75
  **Updated:** 2025-06-16T14:40:48+00:00
- [zulip] 524004143 → [jira] FHIR-45023
  **Source:** [Security and Privacy] Signature
  **Type:** mentions
  **Context:** FHIR-45023 <p><a href="http://jira.hl7.org/browse/FHIR-45023">FHIR-45023</a></p>
  **Score:** 0.43
  **Updated:** 2025-06-13T19:38:35+00:00
- [zulip] 524085591 → [jira] FHIR-45023
  **Source:** [Security and Privacy] What to sign?
  **Type:** mentions
  **Context:** ...ask about this, btw: FHIR-45023 ) <p>(John has a task about this, btw: <a href="https://jira.hl7.org/browse/FHIR-45023">FHIR-45023</a>)</p>
  **Score:** 0.35
  **Updated:** 2025-06-14T20:12:27+00:00
- [zulip] 433597922 → [jira] FHIR-45023
  **Source:** [implementers] Signatures in Bundle for multiple purposes
  **Type:** mentions
  **Context:** ...or signatures using Bundle.signature. <p>I will note that I have filed <a href="http://jira.hl7.org/browse/FHIR-45023">FHIR-45023</a>, as it was observed that t...
  **Score:** 0.06
  **Updated:** 2024-04-16T20:16:06+00:00
- [zulip] 455163060 → [jira] FHIR-45023
  **Source:** [IPS] Signing the IPS
  **Type:** mentions
  **Context:** ...s leads me to feel that no one has even tried. I have reported this as <a href="http://jira.hl7.org/browse/FHIR-45023">FHIR-45023</a> which has not yet been dis...
  **Score:** 0.00
  **Updated:** 2024-07-30T16:23:05+00:00
- [zulip] 524774546 → [jira] FHIR-45023
  **Source:** [Security and Privacy] Signing and narrative
  **Type:** mentions
  **Context:** ...the current section json canonicalization with RFC 8785 (ITS)</li> <li><a href="https://jira.hl7.org/browse/FHIR-45023">FHIR-45023</a> Need a canonicalization f...
  **Score:** 0.00
  **Updated:** 2025-06-18T19:56:53+00:00
**Warnings:**
- Value 'FHIR-45023' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (5 total, showing 5)

### [zulip] 524004143 — [Security and Privacy] Signature
- **Score:** 0.43
- **Updated:** 2025-06-13T19:38:35+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Security%20and%20Privacy/topic/Signature/near/524004143
- **Snippet:** <b>FHIR-45023</b>

### [zulip] 524085591 — [Security and Privacy] What to sign?
- **Score:** 0.35
- **Updated:** 2025-06-14T20:12:27+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Security%20and%20Privacy/topic/What%20to%20sign%3F/near/524085591
- **Snippet:** (John has a task about this, btw: <b>FHIR-45023</b> )

### [zulip] 433597922 — [implementers] Signatures in Bundle for multiple purposes
- **Score:** 0.06
- **Updated:** 2024-04-16T20:16:06+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/Signatures%20in%20Bundle%20for%20multiple%20purposes/near/433597922
- **Snippet:** I will note that I have filed <b>FHIR-45023</b> , as it was observed that there is not a canonicalization defined...

### [zulip] 455163060 — [IPS] Signing the IPS
- **Score:** 0.00
- **Updated:** 2024-07-30T16:23:05+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/IPS/topic/Signing%20the%20IPS/near/455163060
- **Snippet:** ...I have reported this as <b>FHIR-45023</b> which has not yet been discussed by ITS as far as I can...

### [zulip] 524774546 — [Security and Privacy] Signing and narrative
- **Score:** 0.00
- **Updated:** 2025-06-18T19:56:53+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/Security%20and%20Privacy/topic/Signing%20and%20narrative/near/524774546
- **Snippet:** ...the current section json canonicalization with RFC 8785 (ITS) <b>FHIR-45023</b> Need a canonicalization for Bundle that excludes .signature (ITS...


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-45023.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\ImplementableTechnologySpecifications\\FHIR-45023.md",
  "file_text": "# FHIR-45023: Need a canonicalization for Bundle that excludes .signature\n\n## Quick Reference\n\n| Field | Value |\n|---|---|\n| **Ticket** | [FHIR-45023](https://jira.hl7.org/browse/FHIR-45023) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Work Group** | Implementable Technology Specifications |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter** | John Moehrke |\n| **Assignee** | Unassigned |\n| **Created** | 2024-03-21 |\n| **Updated** | 2025-06-16 |\n\n---\n\n## Summary\n\nBoth XML and JSON canonicalization algorithms defined in the FHIR specification lack a variant that excludes the `.signature` element from the canonicalized output. This makes Bundle.signature effectively unusable for digital signatures, since the signature must be calculated over the Bundle content *before* inserting the signature value \u2014 creating a circular dependency. The reporter requests a new canonicalization algorithm that excludes `.signature` to enable Bundle.signature to function correctly for any Bundle type, and potentially for the `#document` canonicalization variant as well.\n\nA secondary question raised in comments is whether the exclusion should cover the entire `Signature` datatype or only `Signature.data`, leaving `Signature.type`, `Signature.when`, and `Signature.who` within the signed content.\n\n---\n\n## Keywords\n\n`canonicalization`, `Bundle.signature`, `digital signature`, `Signature datatype`, `Signature.data`, `RFC 8785`, `JSON canonicalization`, `XML canonicalization`, `JWS`, `JOSE`, `#document`, `normative R6`\n\n---\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Relationship |\n|---|---|---|---|\n| [FHIR-46789](https://jira.hl7.org/browse/FHIR-46789) | Document signature | Applied (Persuasive w/ Mod) | Directly related \u2014 clarifies Bundle document signature guidance; owned by FHIR-I |\n| [FHIR-51098](https://jira.hl7.org/browse/FHIR-51098) | Add a new element for the canonicalization algorithm to Signature | Triaged | Related \u2014 proposes a new Signature element to expose the canonicalization method used |\n| [FHIR-50934](https://jira.hl7.org/browse/FHIR-50934) | Signatures should allow exclusion of section.text in Compositions | Applied (Persuasive w/ Mod) | Related \u2014 defines another canonicalization exclusion variant |\n| [FHIR-51133](https://jira.hl7.org/browse/FHIR-51133) | Reorganize all of the signature guidance | Resolved \u2013 No Change (Retracted) | Context \u2014 proposed consolidating fragmented signature guidance |\n| [FHIR-18443](https://jira.hl7.org/browse/FHIR-18443) | How is signature element excluded from canonicalization? | Published (Persuasive w/ Mod) | Predecessor \u2014 addressed a similar question in R4 era but did not fully resolve for Bundle.signature |\n| [FHIR-42961](https://ji

... *(truncated, 13089 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\ImplementableTechnologySpecifications\FHIR-45023.md with 12829 characters
```

</details>


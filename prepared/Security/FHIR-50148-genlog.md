# Session Log: FHIR-50148

**Phase:** prepared
**Work Group:** Security
**Source File:** `prepared/Security/FHIR-50148.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-50148` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:20:39 UTC |
| **Duration** | 94s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 241,774 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-50148
## Work Group: Security
## Output File: C:\ai\git\fhir-augury-content\prepared\Security\FHIR-50148.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-50148", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-50148", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-50148", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Security\FHIR-50148.md
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
  "id": "FHIR-50148",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-50148: Use JKUs in authentication requests

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Security
- **specification:** US UDAP Security (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** RashidKolaghassi
- **Created:** 2025-03-31T19:31:42+00:00
- **Updated:** 2025-12-09T21:59:34+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-50148

## Content
<p>During connectathon testing, we've encountered the largest JWTs. The majority of the content in the JWT is attributed to the cert, a relatively static piece of content.</p>

<p>Using X5Cs for all authentication requests bloats JWT sizes.</p>

<p>Enabling clients to register their JKU that points to their cert at registration time, enables servers to trust the JKU provided by the client. Severs may cache the JKU response for the allowed time per RFC requirements. </p>

<p>All subsequent authentication requests by the client would use JKUs, significantly reducing JWT sizes sent over the wire while maintaining the security and trust enabled by UDAP. </p>

## Comments (7)

### lynn_laakso — 2025-12-09T21:59:34+00:00
<p>re-open post STU2 publication</p>

### lynn_laakso — 2025-12-09T21:59:34+00:00
<p>Reverted previous resolution: Considered for Future Use made 2025-07-08 00:00:00.0 with vote David Pyke / Brett Stringham : 14 - 0 - 0//(Impact: null; Category: null; Version: null)//Please refer to the minutes for reasoning behind this deferred request</p>

<p><a href="https://confluence.hl7.org/spaces/FAST/pages/358259687/2025-07-08+Security+UDAP+Meeting" class="external-link" target="_blank" rel="nofollow noopener">2025-07-08 Security/UDAP Meeting - FAST - Confluence</a></p>

### JIRAUSER28349 — 2025-07-08T22:45:02+00:00
<p>Hi <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=Isaac.Vetter" class="user-hover" rel="Isaac.Vetter">Isaac Vetter</a>. The minutes were updated, and the reasons for the deferral were included.</p>

### isaac.vetter — 2025-07-08T20:47:02+00:00
<p>The referenced minutes do not currently contain any minutes:</p>

<p> </p>

<p><img src="https://jira.hl7.org/images/icons/attach/noimage.png" imagetext="image-2025-07-08-15-39-25-113.png|width=385,height=163" align="absmiddle" border="0" height="163" width="385" /></p>

<p> </p>

<p>By viewing the page in Edit mode, I see that Caroline Sharpe has these unsaved changes: </p>
<blockquote><p> </p></blockquote>
<div class='table-wrap'>
<table class='confluenceTable'><tbody>
<tr>
<td class='confluenceTd'><blockquote><p><em>Block Vote 3 - Jason Vogt / Joe Shook : 16 - 0 - 0</em> <br/>
<em>41244 - Not persuasive</em><br/>
<em>45249 - Not Persuasive</em><br/>
<em><a href="https://jira.hl7.org/browse/FHIR-50079?filter=23325" class="external-link" rel="nofollow">50079</a> - Persuasive</em><br/>
<em>51054 - Persuasive</em><br/>
<em>Vogt / Stringham : 14 - 0 - 0</em><br/>
<em>50148 - Deferred Request</em><br/>
<em>Pyke / Stringham : 14 - 0 - 0</em><br/>
<em>51244 - Persuasive</em><br/>
<em>Blackmon / Vogt : 12 - 0 - 0</em></p></blockquote></td>
</tr>
<tr>
<td class='confluenceTd'><blockquote><p><em>3</em></p></blockquote></td>
</tr>
<tr>
<td class='confluenceTd'><blockquote><p><em>Caroline &#124; HL7 - <a href="https://confluence.hl7.org/spaces/FAST/pages/358253966/2025-06-24+Security+UDAP+Meeting" class="external-link" target="_blank" rel="nofollow noopener">2025-06-24 Security/UDAP Meeting</a></em><br/>
<em><span class="error">&#91;Caroline \| HL7 - https://jira.hl7.org/issues/?filter=23325|https://jira.hl7.org/issues/?filter=23325&#93;</span></em><br/>
<em>VHAISANEWHAB - not here to vote</em><br/>
<em>JohnMcBride - me as well</em><br/>
<em>Caroline &#124; HL7 - 51054</em> <br/>
<em><a href="https://hl7.org/fhir/R4/security.html" class="external-link" target="_blank" rel="nofollow noopener">Luis Maas - Security - FHIR v4.0.1</a></em><br/>
<em><a href="https://hl7.org/fhir/R4/security.html" class="external-link

... *(truncated, 13206 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-50148".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Security\FHIR-50148.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Security\\FHIR-50148.md",
  "file_text": "# FHIR-50148: Use JKUs in authentication requests\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-50148](https://jira.hl7.org/browse/FHIR-50148) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | US UDAP Security (FHIR) |\n| **Work Group** | Security |\n| **Reporter** | RashidKolaghassi |\n| **Assignee** | Unassigned |\n| **Created** | 2025-03-31 |\n| **Updated** | 2025-12-09 |\n\n## Problem Statement\n\nDuring connectathon testing, excessively large JWTs were encountered. The root cause is that UDAP authentication currently requires embedding the full X.509 certificate chain via the `x5c` header parameter in every authentication JWT. Since certificates are relatively static content, this significantly bloats the JWT payload transmitted on every request.\n\nThe submitter proposes allowing clients to register a JKU (JSON Web Key Set URL) at registration time that points to their certificate. Servers could then trust the client-provided JKU and cache the JKU response per RFC requirements. Subsequent authentication requests would reference the JKU instead of embedding the full certificate chain, significantly reducing JWT sizes while maintaining UDAP's security and trust model.\n\n## Keywords\n\n`JKU`, `x5c`, `JWT`, `UDAP`, `authentication`, `certificate`, `registration`, `connectathon`, `token size`, `JSON Web Key Set`\n\n## Discussion History\n\n### April 22, 2025 \u2014 Motion Tabled\nIsaac Vetter proposed a motion: *\"UDAP to allow servers to authenticate clients with either x5c or a jku containing an x5c.\"* (Isaac Vetter / Esssien moved.) The motion was **tabled for additional conversation**.\n\n### June 24, 2025 \u2014 Deferred for Connectathon Timing\nJoe Lamy raised a key design question: *\"Is the request to change the spec so that all JWT generators SHALL use jku? Or MAY? If you do MAY, you will still have the 'problem' for those who do not choose jku.\"*\n\nThe workgroup discussed and concluded the change requires additional consideration due to the substantial impact it would have. With the upcoming connectathon, there was not enough time. Rashid was asked to consult with his technical team on how critical the issue is.\n\n### July 8, 2025 \u2014 Voted \"Considered for Future Use\" (Deferred)\nVote: David Pyke / Brett Stringham \u2014 **14-0-0** to defer the request. Minutes reference: [2025-07-08 Security/UDAP Meeting](https://confluence.hl7.org/spaces/FAST/pages/358259687/2025-07-08+Security+UDAP+Meeting). Isaac Vetter noted the minutes initially did not include reasoning for the deferral; this was subsequently corrected.\n\n### December 9, 2025 \u2014 Reopened Post-STU2\nLynn Laakso reverted the previous resolution and reopened the ticket for reconsideration after STU2 publication.\n\n## Related Jira Tickets\n\n| Ke

... *(truncated, 9042 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Security\FHIR-50148.md with 8892 characters
```

</details>


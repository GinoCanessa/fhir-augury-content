# Session Log: FHIR-39351

**Phase:** prepared
**Work Group:** Hl7TerminologyAuthority
**Source File:** `prepared/Hl7TerminologyAuthority/FHIR-39351.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-39351` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:17:32 UTC |
| **Duration** | 106s |
| **Total Tool Calls** | 13 |
| **Total Tokens** | 278,825 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-39351
## Work Group: HL7 Terminology Authority
## Output File: C:\ai\git\fhir-augury-content\prepared\Hl7TerminologyAuthority\FHIR-39351.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-39351", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-39351", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-39351", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules
- Use ONLY data from MCP/CLI. Do not fabricate.
- Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\Hl7TerminologyAuthority\FHIR-39351.md
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
  "id": "FHIR-39351",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-39351: ICD-10 GM canonical needs change

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** HL7 Terminology Authority
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Alexander Zautke
- **Created:** 2022-10-29T18:42:22+00:00
- **Updated:** 2025-10-20T19:45:16+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-39351

## Content
<p>HL7 Germany has adjusted the canonical for identifying "ICD-10 GM". The canonical should be changed to "http://fhir.de/CodeSystem/bfarm/icd-10-gm". Please also remove the link to "<a href="http://wiki.hl7.de/index.php?title=Kodesysteme" class="external-link" target="_blank" rel="nofollow noopener">http://wiki.hl7.de/index.php?title=Kodesysteme</a>" and use "<a href="https://ig.fhir.de/basisprofile-de/stable/Ressourcen-Condition-ICD-10-GM.html" class="external-link" target="_blank" rel="nofollow noopener">https://ig.fhir.de/basisprofile-de/stable/Ressourcen-Condition-ICD-10-GM.html</a>" instead.</p>

## Comments (9)

### jsnell — 2025-10-20T19:45:16+00:00
<p>We are planning to close this ticket. We cannot add this as an official url, but if you'd like to add an alternate identifier, that can be requested through the UTG Jira process: <a href="https://jira.hl7.org/browse/UP" class="external-link" rel="nofollow">https://jira.hl7.org/browse/UP</a> </p>

### carmela_couderc — 2023-03-20T16:47:13+00:00
<p>Hi <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=alexanderzautke" class="user-hover" rel="alexanderzautke">Alexander Zautke</a> The proposed resolution is one that Terminology Infrastructure (new name for Vocabulary WG) cannot implement because the the Using ICD with FHIR page has moved to terminology.hl7.org (THO). You will need to enter a ticket in the UP project to start the process. I'm tagging <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=marc.duteau" class="user-hover" rel="marc.duteau">Marc Duteau</a>  to see if he can help you get this change through.  </p>

### alexanderzautke — 2023-03-20T16:06:23+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=carmela_couderc" class="user-hover" rel="carmela_couderc">Carmela A. Couderc</a> Would it be possible to vote on the proposed resolution (see last comment) at one of our next calls over the next weeks? I'm happy to join if needed, but for me it would also be ok if you vote on it if I'm not present.</p>

### carmela_couderc — 2023-01-18T23:04:05+00:00
<p>Discussed at the joint Vocab/TSMG session, q3 Wednesday January 18, 2023</p>

<p><a href="https://terminology.hl7.org/ICD.html" class="external-link" target="_blank" rel="nofollow noopener">https://terminology.hl7.org/ICD.html</a> </p>

<p>There is some concern about the requested url. There is no way to supply a version. </p>

<p>In Germany, there is a new code system for ICD-10 every year.  </p>

<p>Adding a single code creates a new Code System, not a version of a code system. </p>

<p>Could this be handled in the same way SNOMED CT is handled. </p>

<p>Is the fact that ICD is a classification and not a code system impact the decision? </p>

<p>The request is to update the single identifier - not to support the yearly, new code system. </p>

<p><a href="https://terminology.hl7.org/ICD.html#icd-10-variants" class="external-link" target="_blank" rel="nofollow noopener">https://terminology.hl7.org/ICD.html#icd-10-variants</a></p>

<p> </p>

<p>Proposed resolution:</p>
<ol>
	<li>Update the Using ICD with FHIR page to include the proposed url, note the existing one as deprecated</li>
	<li>Update the link in the table as noted in the description of the ticket</li>
	<li>Create a THO metadata record for this code system</li>
</ol>


### carmela_couderc — 2023-01-09T23:13:01+00:00
<p>FYI <a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=reuben.daniels" class="user-hover" rel="reuben.daniels">Reuben Daniels</a> <a hre

... *(truncated, 12982 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-39351" (3 results)

- [zulip] 436717735 → [jira] FHIR-39351
  **Source:** [german/terminologien] Monatliche Meetings des TC Terminologien
  **Type:** mentions
  **Context:** https://jira.hl7.org/browse/FHIR-39351 <p><a href="https://jira.hl7.org/browse/F...
  **Score:** 0.12
  **Updated:** 2024-05-02T15:16:00+00:00
- [zulip] 412386532 → [jira] FHIR-39351
  **Source:** [german/terminologien] Monatliche Meetings des TC Terminologien
  **Type:** mentions
  **Context:** Themen nächstes Mal: Gendern JIRA Ticket #FHIR-39351 Terminologie Package und externe Codesysteme <p>Themen nächstes Mal:<...
  **Score:** 0.07
  **Updated:** 2024-01-11T17:08:05+00:00
- [zulip] 306876766 → [jira] FHIR-39351
  **Source:** [terminology] ICD-10 GM Canonical change
  **Type:** mentions
  **Context:** ...7 Germany would kindly request that the following tracker is formally approved: https://jira.hl7.org/browse/FHIR-39351 . We changed the canonical for "ICD-10 GM...
  **Score:** 0.00
  **Updated:** 2022-10-29T18:46:30+00:00
**Warnings:**
- Value 'FHIR-39351' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (3 total, showing 3)

### [zulip] 436717735 — [german/terminologien] Monatliche Meetings des TC Terminologien
- **Score:** 0.12
- **Updated:** 2024-05-02T15:16:00+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/german%2Fterminologien/topic/Monatliche%20Meetings%20des%20TC%20Terminologien/near/436717735
- **Snippet:** https://jira.hl7.org/browse/<b>FHIR-39351</b>

### [zulip] 412386532 — [german/terminologien] Monatliche Meetings des TC Terminologien
- **Score:** 0.07
- **Updated:** 2024-01-11T17:08:05+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/german%2Fterminologien/topic/Monatliche%20Meetings%20des%20TC%20Terminologien/near/412386532
- **Snippet:** Themen nächstes Mal: Gendern JIRA Ticket #<b>FHIR-39351</b> Terminologie Package und externe Codesysteme

### [zulip] 306876766 — [terminology] ICD-10 GM Canonical change
- **Score:** 0.00
- **Updated:** 2022-10-29T18:46:30+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/terminology/topic/ICD-10%20GM%20Canonical%20change/near/306876766
- **Snippet:** ...https://jira.hl7.org/browse/<b>FHIR-39351</b> . We changed the canonical for "ICD-10 GM". The old one is still...


```

</details>

### Turn 2

**Assistant:**

Now let me fetch the related Zulip threads for more context.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# terminology > ICD-10 GM Canonical change

**Messages:** 14
**First message:** 2022-10-29 18:46:30+00:00
**Last message:** 2024-01-12 11:29:38+00:00
**Participants:** Alexander Zautke, Michael Lawley, Robert McClure, Carmela Couderc, Frank Oemig, Mareike Przysucha, Patrick Werner

## Messages

### Alexander Zautke — 2022-10-29 18:46:30+00:00
HL7 Germany would kindly request that the following tracker is formally approved: https://jira.hl7.org/browse/FHIR-39351 . We changed the canonical for "ICD-10 GM". The old one is still mentioned in the core spec. I'm happy to adjust in a PR as well once it has been approved.

### Alexander Zautke — 2022-10-29 18:47:44+00:00
@Simone Heckmann @Patrick Werner FYI

### Michael Lawley — 2022-10-30 02:49:29+00:00
@Alexander Zautke is there a link to the background / discussion surrounding this change?

### Alexander Zautke — 2022-10-30 09:25:53+00:00
The background is that before we moved to a stable version of the German base profiles (v1.0.0), the way a ICD-10 GM code is represented was changed. We intentionally had a breaking change for representing post-coordinated codes. See https://ig.fhir.de/basisprofile-de/stable/Ressourcen-Condition-ICD-10-GM.html (German only, sorry!). Main change was that an asterisk and a dagger code are represented in two different Condition resources which are linked together. Same for "!" codes.

### Alexander Zautke — 2022-10-30 09:27:32+00:00
Because we had a breaking change in any case, we thought it would be best to fix the canonical to contain the correct organization name in it. We didn't want to support a misleading canonical for the years to come.

### Alexander Zautke — 2022-10-30 09:45:06+00:00
The discussion around it in the German Zulip stream can be found here: https://chat.fhir.org/#narrow/stream/179183-german-.28d-a-ch.29/topic/Breaking.20Change.3A.20Condition

### Alexander Zautke — 2022-10-30 09:45:37+00:00
If formally needed, the initial ticket for the change was this one here: https://github.com/hl7germany/basisprofil-de-r4/issues/244

### Michael Lawley — 2022-10-30 21:15:50+00:00
Thanks! That's very useful

### Robert McClure — 2022-11-06 13:16:08+00:00
@Carol Macumber @Reuben Daniels

### Alexander Zautke — 2023-01-09 16:16:09+00:00
@Carmela Couderc Thanks for your update on the ticket. Could elaborate a bit why you think that this change needs to go through UTG? The canonical is maintained by HL7 Germany and so far it's not part of THO as far as I can see: https://terminology.hl7.org/external_terminologies.html

### Carmela Couderc — 2023-01-09 16:30:40+00:00
Hi @Alexander Zautke I should have checked prior to sending the note in the ticket. Now I see that you just want to update the core spec to reflect something that is already in place. Will add this to the tracker call we have scheduled for today, and if not resolved then, we will get to it Q1 Monday at the Jan 2023 WGM.

### Frank Oemig — 2023-01-10 09:52:08+00:00
This is a matter of governance and provenance. In order not to do something that violates later cross-national communication important terminologies like ICD should be listed on UTG.

### Mareike Przysucha — 2024-01-11 17:24:27+00:00
@Alexander Zautke , @Patrick Werner : We (= Elisabeth and I) currently plan to discuss the topic next month at our German TC Terminology meeting. Can you attend?

### Patrick Werner — 2024-01-12 11:29:38+00:00
yes

---
*URL: https://chat.fhir.org/#narrow/stream/terminology/topic/ICD-10%20GM%20Canonical%20change*

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Arguments:**
```json
{
  "stream": "german/terminologien",
  "topic": "Monatliche Meetings des TC Terminologien",
  "limit": 50
}
```

**Result:**
```
No messages found in stream 'german/terminologien', topic 'Monatliche Meetings des TC Terminologien'.
```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-39351
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| gm | word | 5 | 15.879 |
| gm.html | word | 2 | 15.665 |
| icd | word | 3 | 9.911 |
| germany | word | 1 | 7.363 |
| canonical | word | 4 | 7.305 |
| adjusted | word | 1 | 6.350 |
| 10 | word | 3 | 5.730 |
| html | word | 2 | 5.240 |
| identify | word | 1 | 3.598 |
| hl7 | word | 1 | 3.337 |
| change | word | 3 | 3.233 |
| remove | word | 1 | 2.637 |
| noopener | word | 2 | 1.978 |
| blank | word | 2 | 1.970 |
| target | word | 2 | 1.926 |
| nofollow | word | 2 | 1.879 |
| external | word | 2 | 1.861 |
| link | word | 3 | 1.846 |
| rel | word | 2 | 1.695 |
| href | word | 2 | 1.579 |
| class | word | 2 | 1.396 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\Hl7TerminologyAuthority\FHIR-39351.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\Hl7TerminologyAuthority\\FHIR-39351.md",
  "file_text": "# FHIR-39351: ICD-10 GM canonical needs change\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-39351](https://jira.hl7.org/browse/FHIR-39351) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | HL7 Terminology Authority |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter** | Alexander Zautke |\n| **Assignee** | Unassigned |\n| **Created** | 2022-10-29 |\n| **Updated** | 2025-10-20 |\n\nHL7 Germany requests that the canonical URL for ICD-10 GM be updated from `http://fhir.de/CodeSystem/dimdi/icd-10-gm` to `http://fhir.de/CodeSystem/bfarm/icd-10-gm`, reflecting that DIMDI (Deutsches Institut f\u00fcr Medizinische Dokumentation und Information) was reorganized into BfArM (Bundesinstitut f\u00fcr Arzneimittel und Medizinprodukte). The ticket also asks to update the reference link from the old wiki (`http://wiki.hl7.de/index.php?title=Kodesysteme`) to the new IG page (`https://ig.fhir.de/basisprofile-de/stable/Ressourcen-Condition-ICD-10-GM.html`), and to update examples on the \"Using ICD with FHIR\" page.\n\n## Details\n\n### Background\nThe original canonical URL for ICD-10 GM (`http://fhir.de/CodeSystem/dimdi/icd-10-gm`) was established via FHIR-13723 in 2017, when ICD-10-GM was managed by DIMDI. HL7 Germany subsequently updated their base profiles (v1.0.0) with a breaking change to how post-coordinated ICD-10 GM codes (asterisk, dagger, \"!\" codes) are represented. As part of that breaking change, they also updated the canonical to reference BfArM, the successor organization.\n\n### Key Discussion Points\n1. **Canonical stability concern (Michael Lawley, 2022-10-30):** Embedding organization names in canonicals creates risk of future breakage. Suggested using `http://fhir.de/CodeSystem/icd-10-gm` instead, without an organization in the path.\n2. **UTG process requirement (Carmela Couderc, 2023-01-09):** The \"Using ICD with FHIR\" page has moved to terminology.hl7.org (THO). Changes must go through the UTG Jira process (UP project), not the FHIR tracker.\n3. **Joint Vocab/TSMG session (2023-01-18):** The group discussed versioning concerns (Germany issues a new ICD-10 code system annually) and proposed a three-part resolution: (a) update the ICD page to include the new URL and deprecate the old one, (b) update links as requested, (c) create a THO metadata record.\n4. **Implementation blocker (Carmela Couderc, 2023-03-20):** Terminology Infrastructure cannot implement directly because the page now lives in THO. Reporter needs to file a UP ticket.\n5. **Planned closure (jsnell, 2025-10-20):** The ticket is being planned for closure. The new URL cannot be added as an official URL in FHIR Core, but an alternate identifier can be requested through the UTG Jira process at https://jira.hl7.org/browse/UP.\n\n### Current St

... *(truncated, 8152 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\Hl7TerminologyAuthority\FHIR-39351.md with 7977 characters
```

</details>


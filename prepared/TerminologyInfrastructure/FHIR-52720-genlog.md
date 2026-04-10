# Session Log: FHIR-52720

**Phase:** prepared
**Work Group:** TerminologyInfrastructure
**Source File:** `prepared/TerminologyInfrastructure/FHIR-52720.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-52720` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:20:36 UTC |
| **Duration** | 112s |
| **Total Tool Calls** | 21 |
| **Total Tokens** | 351,405 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-52720
## Work Group: Terminology Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52720.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-52720", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-52720", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-52720", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Title, metadata, Summary, Details, Keywords, Related Zulip, Related GitHub, three Proposed Dispositions (A: Accept, B: Alternative, C: Decline), and Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52720.md
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
  "id": "FHIR-52720",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-52720: Terminology resource profile maturity levels need to be reviewed as they are high without justification

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Terminology Infrastructure
- **specification:** Canonical Resource Management Infrastructure (FHIR)
- **resolution:** Not Persuasive
- **assignee:** Unassigned
- **reporter:** Carmela A. Couderc
- **labels:** Terminology
- **Created:** 2025-09-08T16:08:35+00:00
- **Updated:** 2026-03-09T15:49:03+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-52720

## Content
<p>Maturity levels for the terminology profiles are not aligned with R5 or R4B levels. For example - ShareableCodeSystem is FMM level 0 in R5, but 4 in this IG. PublishableCodeSystem jumped from 0 to 3.  See attached table and adjust FMM levels after discussion with TI.</p>

## Comments (5)

### marc.duteau — 2026-03-09T15:49:03+00:00
<p>I conducted a review of the FMM levels for the above profiles against what is defined in the FHIR Maturity Model confluence page, which includes the fact that artifacts being moved, renamed, or refactored won't have their maturity reset unless FMG agrees it's significant enough to drop back down to 0 or 1.</p>

<p>Obviously, FMM 1 is the lowest level possible so the things at that level can't go lower and would need to meet the FMM 2 testing requirements to go higher.</p>

<p>The two FMM 2 profiles do seem to meet that requirement but they don't meet the requirements for evidence of broad review.</p>

<p>The four FMM 3 profiles definitely seem to meet that requirement but I would agree they're not quite there for FMM 4.</p>

<p>And shareable code system and shareable value set are both definitely at least FMM 4.</p>

<p> </p>

<p> </p>

<p>So all in all, I think the FMM levels make sense to me and, especially since the IG devs believe they meet the various testing requirements and I think we would agree that the shareable code system and value set profiles shouldn't have non-backward compatible changes without implementer consultation.</p>

<p> </p>

### carmela_couderc — 2026-02-23T23:43:04+00:00
<p>should not include an in-person request ticket in a block vote. suggest adding this to a main TI workgroup call agenda.</p>

### carmela_couderc — 2026-01-12T22:54:11+00:00
<p>Discussed at the 2026-01-12 TI tracker call. </p>

<p>This ticket, and TI owned artifacts in general - added to the joint CQI/CDS agenda during the January WGM </p>

### bryn.rhodes — 2025-10-22T15:54:35+00:00
<p>We think the profile levels are set appropriately, and are seeking review/approval from TI to continue as proposed.</p>

### bryn.rhodes — 2025-10-22T15:53:35+00:00
<p>The reason the FMM levels are 0 in the R4, R4B, and R5 specifications is that we weren't tracking/publishing FMM levels for profiles in the base specification. ShareableValueSet has been in the base specification since DSTU2, and ShareableCodeSystem since STU3.</p>

<p>In addition, the Shareable and Publishable profiles for all the other terminology resources have been in CRMI since STU1, so the maturity levels in the balloted specification reflect where they have been used in connectathon and/or production scenarios.</p>


## Snapshot
# FHIR-52720: Terminology resource profile maturity levels need to be reviewed as they are high without justification

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Not Persuasive  
**Assignee:** Unassigned  
**Reporter:** Carmela A. Couderc  
**Work Group:** Terminology Infrastructure  
**Specification:** Canonical Resource Management Infrastructure (FHIR)  
**Labels:** Terminology  
**Created:** 2025-09-08  
**Updated:** 2026-03-09  
**Resolved:** 2026-02-09  

## Description

<p>Maturity levels for the terminology profiles are not aligned with R5 or R4B levels. For example - ShareableCodeSystem is FMM level 0 in R5, but 4 in this IG. PublishableCodeSy

... *(truncated, 6916 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-52720".
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

Let me search for related Zulip discussions and Jira tickets using broader terms.

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "ShareableCodeSystem ShareableValueSet FMM maturity",
  "sources": "zulip",
  "limit": 10
}
```

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
No results found.
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52720.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\TerminologyInfrastructure\\FHIR-52720.md",
  "file_text": "# FHIR-52720: Terminology resource profile maturity levels need to be reviewed as they are high without justification\n\n## Metadata\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-52720](https://jira.hl7.org/browse/FHIR-52720) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Not Persuasive |\n| **Work Group** | Terminology Infrastructure |\n| **Specification** | Canonical Resource Management Infrastructure (FHIR) |\n| **Reporter** | Carmela A. Couderc |\n| **Labels** | Terminology |\n| **Created** | 2025-09-08 |\n| **Updated** | 2026-03-09 |\n\n## Summary\n\nThe reporter raises concern that FMM (FHIR Maturity Model) levels assigned to terminology profiles in the CRMI (Canonical Resource Management Infrastructure) IG are significantly higher than those in R5 or R4B, without adequate justification. Specifically, ShareableCodeSystem is FMM 0 in R5 but FMM 4 in CRMI, and PublishableCodeSystem jumped from 0 to 3. The reporter requests that FMM levels be adjusted after discussion with TI.\n\nThe resolution (Not Persuasive) states the workgroup discussed and agreed the maturity levels as proposed in the ballot are appropriate, listing the following levels:\n\n| Profile | FMM Level |\n|---------|-----------|\n| ShareableValueSet | 4 |\n| ShareableCodeSystem | 4 |\n| ShareableConceptMap | 1 |\n| ShareableNamingSystem | 1 |\n| ShareableTerminologyCapabilities | 2 |\n| PublishableCodeSystem | 3 |\n| PublishableConceptMap | 1 |\n| PublishableNamingSystem | 1 |\n| PublishableTerminologyCapabilities | 2 |\n| PublishableValueSet | 3 |\n| ComputableValueSet | 3 |\n| ExpandedValueSet | 3 |\n\n## Details\n\n### Reporter's Concern\nThe core issue is that FMM levels were 0 in R5 for these profiles, but in the CRMI IG they are significantly elevated (e.g., 4 for ShareableCodeSystem, 3 for PublishableCodeSystem) without visible justification for the jump.\n\n### IG Developer Response (bryn.rhodes, 2025-10-22)\nThe reason FMM levels were 0 in R4, R4B, and R5 is that HL7 was not tracking or publishing FMM levels for profiles in the base specification. ShareableValueSet has been in the base specification since DSTU2, and ShareableCodeSystem since STU3. Additionally, the Shareable and Publishable profiles for all other terminology resources have been in CRMI since STU1, so the maturity levels reflect actual use in connectathon and/or production scenarios.\n\n### Process Concern (carmela_couderc, 2026-02-23)\nThe reporter objected to including this ticket in a block vote, suggesting it should be added to a main TI workgroup call agenda for proper in-person discussion.\n\n### Independent Review (marc.duteau, 2026-03-09)\nMarc Duteau conducted a review of the FMM levels against the FHIR Maturity Model confluence page criteria. His findings:\n- **FMM 1 profiles** (ShareableConceptMap, Shareab

... *(truncated, 8668 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\TerminologyInfrastructure\FHIR-52720.md with 8514 characters
```

</details>


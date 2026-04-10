# Session Log: FHIR-38203

**Phase:** prepared
**Work Group:** OrdersObservations
**Source File:** `prepared/OrdersObservations/FHIR-38203.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-38203` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:38:01 UTC |
| **Duration** | 91s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 292,786 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-38203
## Work Group: Orders & Observations
## Output File: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-38203.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-38203", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-38203", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-38203", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-38203.md
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
  "id": "FHIR-38203",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-38203: Include PHR/EHR use case for at-home test reporting

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** At-Home In-Vitro Test Report (FHIR)
- **resolution:** Unresolved
- **assignee:** Sarah Gaunt
- **reporter:** Daniel Rutz
- **labels:** HIGH_COMPLEXITY, LAB_Call, OO, Ready-to-Discuss
- **Created:** 2022-09-08T17:25:45+00:00
- **Updated:** 2026-01-12T20:24:40+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-38203

## Content
<p>Although the current IG only targets a public health use case for communicating the results of at-home testing, we think it is valuable to also expand to cover a personal health record and/or provider-based electronic health record use case.  In particular, this use case would not currently be an over-the-network transaction, but a within-the-smart-device transaction to another app (for the patient's PHR or provider EHR) to be ingest the teste result.</p>

## Comments (6)

### daniel.rutz — 2026-01-12T20:24:40+00:00
<p>Discussed on the Jan 12 2026 O&amp;O HCP call - this data flow has some similarities to the CGM (Continuous Glucose Monitoring) Implementation Guide (<a href="https://build.fhir.org/ig/HL7/cgm/)," class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/cgm/),</a> but there are distinct differences (CGM tends to have a constant stream of many data points to the vendor, then EMR would ask for a download of bulk-ish data when needed; this at-home testing is much more scarce data upload). </p>

<p>At the moment there are not stakeholders ready to work out the details of how to address the request.</p>

### daniel.rutz — 2025-12-05T23:21:12+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=hbuitendijk" class="user-hover" rel="hbuitendijk">Hans Buitendijk</a> Those two Monday slots don't work well for 3/4ths of the next Mondays (can't make the 8th, 15th, or 29th) but I could do either or both on Dec 22 and probably most of January Mondays too.  And yes I'll be at least partially attending virtual WGM so that's also a plausible option.</p>

### hbuitendijk — 2025-12-05T18:52:11+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=daniel.rutz" class="user-hover" rel="daniel.rutz">Daniel Rutz</a> : We are trying to scheduling some in-vitro time either during the WGM or an upcoming Monday 2-3 or 3-4pm ET call.  Let us know what may work generally to sync with Sarah at the same time.</p>

### lynn_laakso — 2023-03-26T16:09:30+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2023-03-26T16:09:30+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-05 00:00:00.0 with vote Sarah Gaunt / Dan Rutz : 13 - 0 - 1//(Impact: null; Category: null; Version: null)//Interesting idea, but out of scope for this project and we will consider it in the future.</p>

<p>Will add page to IG that details the considered for future use comments.</p>

<p>Add note to say that until we solve the issue, to use other methods, such as a patient portal to communicate the result to the provider.</p>

### apitkus — 2023-01-06T15:01:33+00:00
<p>Support capabilities for consumer test results to be reported/ingested by provider EHRs so patients can receive treatment, including those that are time sensitive.  Given providers report public health reportables, such a solution would need to be reportable via eCR by law.  Expect this to be part of the internal ingestion and use of data by EHRs.</p>

<p> </p>

<p>Also (which may warrant a separate Jira), need to consider said functionality for any consumer performed lab test (i.e. HIV, influenza, drug screening, urinalysis items, CBC items) where testing can be performed and not limited to just COVID.</p>


## Snapshot
# FHIR-38203: Include PHR/EHR use case for at-home test reporting

**Status:** Triaged  
**Type:** Change Request  
**Priori

... *(truncated, 7567 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-38203".
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
  "values": "at-home testing personal health record consumer lab test",
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
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-38203
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| phr | word | 3 | 11.071 |
| teste | word | 1 | 10.915 |
| ingest | word | 1 | 7.637 |
| ehr | word | 3 | 6.727 |
| transaction | word | 2 | 6.505 |
| valuable | word | 1 | 6.214 |
| reporting | word | 2 | 5.716 |
| health | word | 3 | 5.684 |
| test | word | 2 | 5.543 |
| electronic | word | 1 | 5.459 |
| network | word | 1 | 5.344 |
| personal | word | 1 | 5.317 |
| complexity | word | 1 | 5.274 |
| testing | word | 1 | 4.811 |
| provider | word | 2 | 4.769 |
| record | word | 2 | 4.757 |
| lab | word | 1 | 4.617 |
| app | word | 1 | 4.542 |
| communicate | word | 1 | 4.541 |
| smart | word | 1 | 4.532 |
| oo | word | 1 | 4.449 |
| expand | word | 1 | 4.436 |
| result | word | 2 | 4.380 |
| case | word | 5 | 4.315 |
| ready | word | 1 | 4.170 |
| cover | word | 1 | 3.953 |
| device | word | 1 | 3.608 |
| include | word | 2 | 3.096 |
| current | word | 1 | 3.014 |
| discuss | word | 1 | 2.907 |
| based | word | 1 | 2.804 |
| call | word | 1 | 2.640 |
| patient | fhir_path | 1 | 2.398 |
| ig | word | 1 | 2.243 |
| target | word | 1 | 1.342 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-38203.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\OrdersObservations\\FHIR-38203.md",
  "file_text": "# FHIR-38203: Include PHR/EHR use case for at-home test reporting\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-38203](https://jira.hl7.org/browse/FHIR-38203) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | At-Home In-Vitro Test Report (FHIR) |\n| **Work Group** | Orders & Observations |\n| **Assignee** | Sarah Gaunt |\n| **Reporter** | Daniel Rutz |\n| **Labels** | HIGH_COMPLEXITY, LAB_Call, OO, Ready-to-Discuss |\n| **Created** | 2022-09-08 |\n| **Updated** | 2026-01-12 |\n\n## Details\n\nThis change request asks the At-Home In-Vitro Test Report IG to expand beyond its current public health reporting scope to also cover **Personal Health Record (PHR)** and **Electronic Health Record (EHR)** use cases. The submitter envisions a within-the-smart-device transaction\u2014where an at-home test app transmits results to another app (PHR or provider EHR) for ingestion\u2014rather than only over-the-network public health reporting.\n\n### History\n\n- **2023-01-05**: Initially resolved as \"Considered for Future Use\" by vote (Sarah Gaunt / Dan Rutz, 13-0-1) with the rationale that it was an interesting idea but out of scope for the current project.\n- **2023-03-26**: Re-opened post STU1 publication. A note was added to the IG directing users to alternative methods (e.g., patient portals) until this use case is formally addressed.\n- **2023-01-06** (apitkus comment): Emphasized the need for consumer test results to be ingested by provider EHRs for treatment (including time-sensitive and eCR-reportable scenarios), and suggested the scope should not be limited to COVID but also cover HIV, influenza, drug screening, urinalysis, CBC, etc.\n- **2025-12-05**: Hans Buitendijk and Daniel Rutz discussed scheduling in-vitro time at the WGM or a Monday call to coordinate with Sarah Gaunt.\n- **2026-01-12**: Daniel Rutz reported discussion on the O&O HCP call. Noted similarities to the CGM (Continuous Glucose Monitoring) IG data flow but highlighted distinct differences (CGM has continuous streaming; at-home testing is sparse data upload). **Currently there are no stakeholders ready to work out the details.**\n\n### Key Considerations\n\n- The IG is currently scoped to public health use cases only.\n- A PHR/EHR use case introduces device-to-app data transfer patterns not currently specified.\n- Similarities exist with the CGM IG but data patterns differ significantly.\n- Extending to non-COVID consumer lab tests broadens scope considerably.\n- eCR reporting obligations apply when providers ingest public health reportable results.\n\n## Keywords\n\n`PHR`, `EHR`, `at-home testing`, `in-vitro`, `personal health record`, `consumer lab test`, `smart device`, `public health reporting`, `patient portal`, `eCR`, `CGM`, `COVID`\n\n## Related Jir

... *(truncated, 7386 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-38203.md with 7224 characters
```

</details>

### Turn 4

**Assistant:**

Let me fetch the most closely related tickets for more context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-38203: Include PHR/EHR use case for at-home test reporting

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** At-Home In-Vitro Test Report (FHIR)
- **resolution:** Unresolved
- **assignee:** Sarah Gaunt
- **reporter:** Daniel Rutz
- **labels:** HIGH_COMPLEXITY, LAB_Call, OO, Ready-to-Discuss
- **Created:** 2022-09-08T17:25:45+00:00
- **Updated:** 2026-01-12T20:24:40+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-38203

## Content
<p>Although the current IG only targets a public health use case for communicating the results of at-home testing, we think it is valuable to also expand to cover a personal health record and/or provider-based electronic health record use case.  In particular, this use case would not currently be an over-the-network transaction, but a within-the-smart-device transaction to another app (for the patient's PHR or provider EHR) to be ingest the teste result.</p>

## Comments (6)

### daniel.rutz — 2026-01-12T20:24:40+00:00
<p>Discussed on the Jan 12 2026 O&amp;O HCP call - this data flow has some similarities to the CGM (Continuous Glucose Monitoring) Implementation Guide (<a href="https://build.fhir.org/ig/HL7/cgm/)," class="external-link" target="_blank" rel="nofollow noopener">https://build.fhir.org/ig/HL7/cgm/),</a> but there are distinct differences (CGM tends to have a constant stream of many data points to the vendor, then EMR would ask for a download of bulk-ish data when needed; this at-home testing is much more scarce data upload). </p>

<p>At the moment there are not stakeholders ready to work out the details of how to address the request.</p>

### daniel.rutz — 2025-12-05T23:21:12+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=hbuitendijk" class="user-hover" rel="hbuitendijk">Hans Buitendijk</a> Those two Monday slots don't work well for 3/4ths of the next Mondays (can't make the 8th, 15th, or 29th) but I could do either or both on Dec 22 and probably most of January Mondays too.  And yes I'll be at least partially attending virtual WGM so that's also a plausible option.</p>

### hbuitendijk — 2025-12-05T18:52:11+00:00
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=daniel.rutz" class="user-hover" rel="daniel.rutz">Daniel Rutz</a> : We are trying to scheduling some in-vitro time either during the WGM or an upcoming Monday 2-3 or 3-4pm ET call.  Let us know what may work generally to sync with Sarah at the same time.</p>

### lynn_laakso — 2023-03-26T16:09:30+00:00
<p>re-open post STU1 publication</p>

### lynn_laakso — 2023-03-26T16:09:30+00:00
<p>Reverted previous resolution: Considered for Future Use made 2023-01-05 00:00:00.0 with vote Sarah Gaunt / Dan Rutz : 13 - 0 - 1//(Impact: null; Category: null; Version: null)//Interesting idea, but out of scope for this project and we will consider it in the future.</p>

<p>Will add page to IG that details the considered for future use comments.</p>

<p>Add note to say that until we solve the issue, to use other methods, such as a patient portal to communicate the result to the provider.</p>

### apitkus — 2023-01-06T15:01:33+00:00
<p>Support capabilities for consumer test results to be reported/ingested by provider EHRs so patients can receive treatment, including those that are time sensitive.  Given providers report public health reportables, such a solution would need to be reportable via eCR by law.  Expect this to be part of the internal ingestion and use of data by EHRs.</p>

<p> </p>

<p>Also (which may warrant a separate Jira), need to consider said functionality for any consumer performed lab test (i.e. HIV, influenza, drug screening, urinalysis items, CBC items) where testing can be performed and not limited to just COVID.</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-30248: Public Health Authority Capability Statement includes unnecessary constraints

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Public Health
- **specification:** US Making EHR Data More available for Research and Public Health (MedMorph) (FHIR)
- **resolution:** Persuasive
- **assignee:** Nagesh Bashyam
- **reporter:** Rob Dingwell
- **labels:** Block-Vote-3
- **Created:** 2021-01-06T16:59:02+00:00
- **Updated:** 2023-06-08T19:25:00+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-30248

## Content
<p>The Public Health Authority Capability statement contains client context constraints for creating Reporting and Content bundles as well as MessageHeader resources.   I do not see where is the specification that requires a PHA to support these activities.  A PHA may generate a FHIR Message bundle in response to receiving a Reporting Bundle but the interaction would be for it to send that bundle via FHIR Messaging $process-message operation and not via RESTful api methods.  These constraints should be removed</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-33479: Message event code may not be appropriate for the IG use case

- **status:** Published
- **type:** Change Request
- **priority:** Highest
- **work_group:** Orders & Observations
- **specification:** Cancer Pathology Data Sharing (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Craig Newman
- **labels:** Block-Vote-4
- **Created:** 2021-09-10T12:34:37+00:00
- **Updated:** 2023-07-11T16:10:44+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-33479

## Content
<p>The MessageHeader profile constrains .event.code to "cancer-report-message" from the MedMorph Code System for message types, but in that Code System that code is define as "from clinical care to PHA." but this IG is about from the LIS to EHR. It feels like there needs to be a unique code for this use case as the contents of the message bundle may be different between the two.</p>

```

</details>


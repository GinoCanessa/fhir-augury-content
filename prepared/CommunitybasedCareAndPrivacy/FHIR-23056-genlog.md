# Session Log: FHIR-23056

**Phase:** prepared
**Work Group:** CommunitybasedCareAndPrivacy
**Source File:** `prepared/CommunitybasedCareAndPrivacy/FHIR-23056.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-23056` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 18:11:00 UTC |
| **Duration** | 85s |
| **Total Tool Calls** | 11 |
| **Total Tokens** | 219,312 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-23056
## Work Group: Community-Based Care and Privacy
## Output File: C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-23056.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-23056", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-23056", limit=50)

## Step 2: Fetch Related Jira Tickets
For each Jira ticket in cross-references, fetch details via FhirAugury-get_item.

## Step 3: Fetch Zulip Conversations
For each Zulip cross-reference, get the thread. Also: FhirAugury-content_search(values="FHIR-23056", sources="zulip", limit=10)

## Step 4: Note GitHub Items

## Step 5: Build the Report using the standard ticket review structure with Summary, Details, Keywords, Related Zulip Discussions, Related GitHub Items, and three Proposed Dispositions (A: Accept, B: Alternative, C: Decline) plus a Recommendation.

## Rules
- Use ONLY data from MCP/CLI. Do not fabricate.
- Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-23056.md
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
  "id": "FHIR-23056",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-23056: Service Information - Service Unit Quantity - representing more complex service internal/quantity scenarios

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Community-Based Care and Privacy
- **specification:** US Electronic Long-Term Services & Supports (ELTSS) (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Chirag Bhatt
- **Created:** 2019-08-04T18:16:50+00:00
- **Updated:** 2024-12-05T10:02:50+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-23056

## Content
<p>In reference to Additional Mapping Details: </p>

<p>         2) quantityQuantity can be used to represent simple quantities such as "1 installation" or "5 trips". quantityRatio can be used to represent quantities with intervals such as "8 hours a day" or "7 units per week". Either quantityQuantity or quantityRatio can be used, but not both for the same ServiceRequest.<br class="atl-forced-newline" />4) numerator and denominator are used to represent a quantity with an interval. For example, to represent 8 hours a day, numerator -&gt; value would be "8" and numerator -&gt; unit would be "hour", while denominator -&gt; value would be "1" and denominator -&gt; unit would be "day". </p>

<p>         Comment: This provides a very good guidance on how to populate quantity and units. However, there are instances in LTSS home services that are little more complex e.g. "2 hours twice a day, one AM and one PM" or "4 hours each afternoon/PM" or "Mon and Thu of each week", etc. These will need to be handled differently. May be these special situations will require using occurrenceTiming-&gt;timeOfDay or dayOfWeek etc. But note that it will get complex if quantityRatio and occurrenceTiming elements are used in combination to represent single concept. So it will be better to use occurrenceTiming can be used by itself for all situations without using quantityRatio since numerator and denominator are probably not meant for representing multiple occurrence.</p>

## Comments (4)

### bheale — 2024-12-05T10:02:50+00:00
<p>I believe this is nuanced. Coding the denominator and numerator units is more precise. Occurrence would indicate the number of repetitions of a service. That is, for everyday for ten days (occurrenceTiming) I will give 3 shots per day (quantityRatio). Using both occurrence and quantity captures this kind of complexity. In the example the service timing is "everyday for ten days," the service is "3 times per day I give a shot."</p>

<p>But for the specific timings discussed, there is a discussion here: <a href="https://hl7.org/fhir/us/eltss/2024Jan/implementation.html#quantities-ucum-and-the-timing-data-type" class="external-link" target="_blank" rel="nofollow noopener">https://hl7.org/fhir/us/eltss/2024Jan/implementation.html#quantities-ucum-and-the-timing-data-type</a> <br/>
The example in the IG reference is "Give ServicePlan.quantity 5 with unit=<span class="error">&#91;USD&#93;</span>/day with the occurrenceTiming.boundsPeriod of May 31, 2023 to June 23, 2023 on occurrenceTiming.dayOfWeek = Mon and Wed at occurrenceTiming.timeOfDay = 3 pm." This translates to every Mon and Wed at 3 pm, from May 31, 2023 to June 23, 2023, give 5 per day. If quanityRatio is used then instead of the unitless 5, you could use the numerator of a code for dollar and have dollar per day. This would give better precision. </p>

### lynn_laakso — 2024-05-27T02:37:58+00:00
<p>re-open post STU2 publication</p>

### lynn_laakso — 2024-05-27T02:37:58+00:00
<p>Reverted previous resolution: Considered for Future Use made 2020-07-21 00:00:00.0 with vote Amber Patel/Kathleen Connor: 12-0-1//(Impact: null; Category: null; Version: null)//This depends on what happens with 23054 and 23055 (i.e., cardinality on occurrence). </p>

<p>occurrenceTiming seems to be the right data element to describe timing with frequency ("how many"), duration (hrs, days, etc.) and period ("per day", 

... *(truncated, 9681 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-23056".
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
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-23056
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| quantityratio | word | 4 | 13.507 |
| occurrencetiming | word | 3 | 9.894 |
| quantityquantity | word | 2 | 9.697 |
| numerator | word | 4 | 8.969 |
| denominator | word | 4 | 8.767 |
| hour | word | 5 | 8.613 |
| quantity | word | 8 | 8.189 |
| unit | word | 6 | 7.716 |
| day | word | 4 | 7.025 |
| complex | word | 4 | 6.356 |
| pm | word | 2 | 6.258 |
| interval | word | 2 | 6.212 |
| dayofweek | word | 1 | 5.886 |
| ltss | word | 1 | 5.741 |
| week | word | 2 | 5.704 |
| service | word | 7 | 5.530 |
| installation | word | 1 | 5.526 |
| represent | word | 8 | 5.523 |
| timeofday | word | 1 | 5.482 |
| gt | word | 5 | 5.286 |
| afternoon | word | 1 | 5.241 |
| internal | word | 2 | 5.236 |
| thu | word | 1 | 5.161 |
| 8 | word | 3 | 4.689 |
| trip | word | 1 | 4.648 |
| situation | word | 2 | 4.549 |
| mon | word | 1 | 4.387 |
| scenario | word | 2 | 4.326 |
| differently | word | 1 | 3.686 |
| occurrence | word | 1 | 3.630 |

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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-23056.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\CommunitybasedCareAndPrivacy\\FHIR-23056.md",
  "file_text": "# FHIR-23056: Service Information \u2013 Service Unit Quantity \u2013 Representing More Complex Service Quantity/Timing Scenarios\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-23056](https://jira.hl7.org/browse/FHIR-23056) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Work Group** | Community-Based Care and Privacy |\n| **Specification** | US Electronic Long-Term Services & Supports (eLTSS) (FHIR) |\n| **Reporter** | Chirag Bhatt |\n| **Created** | 2019-08-04 |\n| **Updated** | 2024-12-05 |\n\n---\n\n## Summary\n\nThis ticket requests improved guidance (and potentially structural changes) for representing complex service quantity and timing scenarios in the eLTSS ServiceRequest profile. The original submitter notes that while `quantityQuantity` handles simple quantities (e.g., \"1 installation\") and `quantityRatio` handles rate-based quantities (e.g., \"8 hours a day\"), real-world LTSS home services often involve more complex scheduling such as \"2 hours twice a day, one AM and one PM,\" \"4 hours each afternoon,\" or \"Mon and Thu of each week.\" The submitter suggests that `occurrenceTiming` (with `timeOfDay`, `dayOfWeek`, etc.) may be more appropriate for these cases, but cautions that combining `quantityRatio` and `occurrenceTiming` to represent a single concept introduces complexity.\n\nThe ticket was originally resolved as \"Considered for Future Use\" in 2020 (vote 12-0-1) with a note that it depends on the outcome of related tickets FHIR-23054 and FHIR-23055 regarding `occurrence` cardinality. It was reopened post-STU2 publication in May 2024. A December 2024 comment from bheale argues that the two elements serve complementary roles \u2014 `quantityRatio` for precise coded units of service quantity (e.g., dollar per day) and `occurrenceTiming` for scheduling (e.g., specific days and times) \u2014 and points to existing IG guidance that already illustrates combined usage.\n\n---\n\n## Details\n\n### Core Issue\n\nThe eLTSS IG maps service quantities to `ServiceRequest.quantity[x]` using either `quantityQuantity` (simple) or `quantityRatio` (rate). For complex LTSS scenarios involving day-of-week, time-of-day, or multi-occurrence patterns, the submitter questions whether `quantityRatio` is appropriate or whether `occurrenceTiming` should be used instead (or exclusively).\n\n### Current IG Approach (STU2)\n\nThe eLTSS STU2 IG adopted the following pattern:\n- **`occurrenceTiming.boundsPeriod`** \u2014 service start/end dates\n- **`occurrenceTiming.dayOfWeek` / `timeOfDay`** \u2014 scheduling specifics\n- **`quantity` or `quantityRatio`** \u2014 the amount of service delivered per unit of time\n\nThe IG provides a composite example: *\"Give ServicePlan.quantity 5 with unit=[USD]/day with the occurrenceTiming.boundsPeriod of May 31, 2023 to June 23, 2023 on occurre

... *(truncated, 8721 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-23056.md with 8457 characters
```

</details>


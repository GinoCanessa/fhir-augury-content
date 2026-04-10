# Session Log: FHIR-47773

**Phase:** prepared
**Work Group:** OrdersObservations
**Source File:** `prepared/OrdersObservations/FHIR-47773.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-47773` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 00:40:33 UTC |
| **Duration** | 131s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 293,646 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-47773
## Work Group: Orders & Observations
## Output File: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-47773.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-47773", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-47773", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-47773", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-47773.md
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
  "id": "FHIR-47773",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-47773: Search DeviceAssociation by location

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Orders & Observations
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Elliot Silver
- **labels:** HCP, OO, Ready-to-Discuss
- **Created:** 2024-09-13T23:28:48+00:00
- **Updated:** 2026-02-02T20:45:05+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-47773

## Content
<p><a href="https://jira.hl7.org/secure/ViewProfile.jspa?name=emetz" class="user-hover" rel="emetz">Eldon Metz</a> (account possibly inactive) has requested:</p>

<p>Ability to convey and search by location at the time of association or disassociation. This one I need to dive into more on the FHIR side to know what to ask for. I think for patients, the location is joined via the Encounter resource. How do Device locations get tracked in FHIR? Assigned patient location isn’t precise enough, we support RTLS so the device location can change as the patient goes down the corridor from one room to another. In HL7v2, we use PRT.9 to convey / track this. I bring this one up as it would also be a pretty big deficiency in searching if we couldn’t constrain by this. Maybe it is already possible.</p>

## Comments (12)

### marti_velezis — 2026-02-02T20:45:05+00:00
<p>20260130 OO WGQ1 David Barwin / Riki Merrick : against: 0, abstain: 1, in favor: 11</p>

### marti_velezis — 2026-02-02T20:31:15+00:00
<p>David Barwin / Riki Merrick : against: 0, abstain: 1, in favor: 11</p>

### marti_velezis — 2026-02-02T20:31:15+00:00
<p>Reverted previous resolution: Considered for Future Use made 2025-10-24 00:00:00.0 with vote Lorraine Constable / Elliot Silver: 4-0-0//(Impact: null; Category: null; Version: null)//We will reopen before R6 Normative publication to resolve.</p>

### esilver — 2025-10-22T14:00:02+00:00
<p>Please provide extension content.</p>

### esilver — 2025-10-22T13:59:32+00:00
<p>Dev WG supports the extension approach.</p>

### esilver — 2025-10-22T13:58:22+00:00
<p>Suggestion to do the first option (add elements) as extensions.</p>

### esilver — 2025-10-01T00:07:35+00:00
<p>The use case is the ability to identify devices at a location at a point in time, particularly those times when a device was associated with a patient, or disassociated with them. Device.location is only current location, and _history isn't required or searchable.</p>

<p>Discussed two options: add location elements to DeviceAssociation, or use DeviceAssociation to association a device to a location with a relationship of "located in"</p>

<p>We probably don't want an arbitrary list of locations in DeviceAssociation that continues to grow as a person walks around, e.g. for GPS tracking.</p>
<ul>
	<li>Add location elements to DeviceAssociation
	<ul>
		<li>This probably requires two elements associationStartLocation, associationEndLocation.</li>
		<li>Add search parameter for searching by either element</li>
		<li>Limits to only recording those to points in time (which are the relevant points in time for the use case)</li>
		<li>Easy to record "given to this patient when they were in the doctor's office" (device associated with patient, startLocation=office)</li>
	</ul>
	</li>
	<li>Support "located in" associations
	<ul>
		<li>Seems like bending the definition of "association" but probably is ok.</li>
		<li>Would allow being associated with locations for arbitrary lengths of time, independent of other associations (such as with a patient)</li>
		<li>Would benefit from making `period` into occurrence<span class="error">&#91;x&#93;</span> of type Perod, DateTime to allow recording of point-in-time locations</li>
		<li>Might be confusing with a device associated with a location for the purposes of monitoring, etc. vs for position tracking</li>
		<li>Less direct ability to record "given to this patient when they were in the doctor's office" (device associate

... *(truncated, 18184 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-47773".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-47773.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\OrdersObservations\\FHIR-47773.md",
  "file_text": "# FHIR-47773: Search DeviceAssociation by location\n\n## Summary\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-47773](https://jira.hl7.org/browse/FHIR-47773) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Reporter** | Elliot Silver |\n| **Assignee** | Unassigned |\n| **Work Group** | Orders & Observations |\n| **Specification** | FHIR Core (FHIR) |\n| **Labels** | HCP, OO, Ready-to-Discuss |\n| **Created** | 2024-09-13 |\n| **Updated** | 2026-02-02 |\n\n## Description\n\nEldon Metz (PCIM WG) requests the ability to convey and search by **location at the time of device association or disassociation** within `DeviceAssociation`. In HL7v2, `PRT.9` (\"Participant Location\") tracks this information for the IHE PCIM profile. Currently, `Device.location` only reflects the device's current location, and `_history` is neither required nor searchable, making it impossible to determine where a device was when it was associated with or disassociated from a patient.\n\n**Use case:** A reporting system tracking device utilization or billing needs to filter by the location where a device was used (e.g., ER vs OR vs ICU). A patient monitor may be associated in the ER and move with the patient to the ICU; the association-start location is the most clinically and operationally valuable data point.\n\n## Discussion History\n\n1. **Hans Buitendijk (2024-09-27):** Asked Elliot to clarify which locations are of interest from start to end of association.\n\n2. **Eldon Metz / PCIM WG (2024-10-16):** Proposed a backbone element structure for DeviceAssociation:\n   - `location` BackboneElement 0..* \u2014 \"List of locations recorded during device association\"\n     - `location` Reference(Location) 1..1\n     - `reportedTime` dateTime 1..1\n   - Initially captures start/end locations; extensible for future location tracking over time.\n\n3. **Elliot Silver (2024-12-23):** Acknowledged the PCIM input; expressed concern about an unlimited list of locations.\n\n4. **HCP (2025-09-29):** Elliot tasked with providing two options for the group to review.\n\n5. **Elliot Silver (2025-10-01):** Presented three options:\n   - **Option 1 \u2014 Add location elements:** `associationStartLocation` and `associationEndLocation` on DeviceAssociation, plus a search parameter. Simple, limited to the relevant time points.\n   - **Option 2 \u2014 \"Located in\" associations:** Use DeviceAssociation to associate a device with a Location via a relationship type. More flexible but potentially confusing and indirect.\n   - **Option 3 \u2014 List resource:** A List with subject=Device and location items. Reasonable but unclear where to describe it in core.\n\n6. **Elliot Silver (2025-10-22):** Reported that the suggestion is to implement **Option 1 as extensions**. Dev WG supports the extension ap

... *(truncated, 8256 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\OrdersObservations\FHIR-47773.md with 8077 characters
```

</details>


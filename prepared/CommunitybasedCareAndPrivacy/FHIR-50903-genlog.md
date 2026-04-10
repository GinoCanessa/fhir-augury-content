# Session Log: FHIR-50903

**Phase:** prepared
**Work Group:** CommunitybasedCareAndPrivacy
**Source File:** `prepared/CommunitybasedCareAndPrivacy/FHIR-50903.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-50903` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 23:08:28 UTC |
| **Duration** | 89s |
| **Total Tool Calls** | 10 |
| **Total Tokens** | 244,567 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-50903
## Work Group: Community-Based Care and Privacy
## Output File: C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-50903.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-50903", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-50903", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-50903", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure with Title, metadata, Summary, Details, Keywords, Related Zulip, Related GitHub, three Proposed Dispositions (A: Accept, B: Alternative, C: Decline), and Recommendation.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-50903.md
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
  "id": "FHIR-50903",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-50903: TreatmentDirective: which FHIR core resource for this purpose?

- **status:** Triaged
- **type:** Question
- **priority:** Medium
- **work_group:** Community-Based Care and Privacy
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Eduard de Rijcke
- **Created:** 2025-05-15T07:54:14+00:00
- **Updated:** 2025-09-15T18:33:35+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-50903

## Content
<p>Currently, we are researching how to implement <a href="https://zibs.nl/wiki/TreatmentDirective2-v1.0(2020EN)" class="external-link" target="_blank" rel="nofollow noopener">TreatmentDirective</a> (which contains a joint decision between a health professional and a patient or his representative(s) about the desirability of performing a certain treatment) in the Netherlands.</p>

<p>For example, some topics that a Patient/representative could agree and register with the health professional:</p>
<ul>
	<li>Admission to the intensive care unit</li>
	<li>Cardiopulmonary resuscitation</li>
	<li>Artificial respiration</li>
</ul>


<p>With the options:</p>
<ol>
	<li>Execute</li>
	<li>Do not execute</li>
	<li>Other<br/>
<em>(Example: do not execute artificial respiration in a hospital)</em></li>
</ol>


<p>Now we are considering which HL7 FHIR R4 resource is compatible with this kind of information.</p>

<p>First, we thought the <a href="https://hl7.org/fhir/R4/consent.html" class="external-link" target="_blank" rel="nofollow noopener">Consent</a> resource, but now we are doubting whether to use <a href="https://www.hl7.org/fhir/R4/servicerequest.html" class="external-link" target="_blank" rel="nofollow noopener">ServiceRequest</a> resource like <a href="https://build.fhir.org/ig/HL7/fhir-pacio-adi/index.html" class="external-link" target="_blank" rel="nofollow noopener">PACIO</a> (<a href="https://build.fhir.org/ig/HL7/fhir-pacio-adi/ServiceRequest-Example-Smith-Johnson-CPR-ServiceRequest1.html" class="external-link" target="_blank" rel="nofollow noopener">example stu2</a>). Both resources have their pros and cons. Consent describes more of an agreement between both parties, and ServiceRequest is more used for planned/requested actions. So, does PACIO choose the right resource for this TreatmentDirective purpose?</p>

<p>The only main issue both resources have only two options (ProvisionType: Deny/Permit or doNotPerform: boolean). So now we're thinking of using an extension to support this other (condition) option.</p>

<p><em><a href="https://chat.fhir.org/#narrow/channel/179166-implementers/topic/TreatmentDirective.3A.20which.20resource.20is.20for.20this.20purpose.3F" class="external-link" target="_blank" rel="nofollow noopener">Zulip</a></em> </p>

<p><b><em><ins>Extra information after WGM Q3 meeting in Madrid at PatientCare:</ins></em></b></p>

<p><a href="https://confluence.hl7.org/download/attachments/324961395/20250513_HL7WGMadrid_TreatmentDirective.pptx?version=1&amp;modificationDate=1747209289624&amp;api=v2" class="external-link" target="_blank" rel="nofollow noopener">20250513_HL7WGMadrid_TreatmentDirective.pptx</a> with the context behind which resource should be used?</p>
<ul>
	<li>Goal - informal wishes, "dance at wedding" or "die at home"</li>
	<li>ServiceRequest - DNR orders, supports Do Not Perform, PACIO profiles – may reference supporting info of where is came from - must come from patient or related person who knows patient well</li>
	<li>Consent - legal directives, IPS includes advance directives</li>
	<li>Observation – patient preferences, PACIO profiles</li>
</ul>


<p><a href="https://confluence.hl7.org/spaces/PC/pages/324961395/2025+May+Patient+Care+WGM+Agenda+and+Minutes#id-2025MayPatientCareWGMAgendaandMinutes-13May2025" class="external-link" target="_blank" rel="nofollow noopener"><em>Source</em></a></p>

<p><b>Latest update (14th May)</b><b>{</b>}</p>

<p>PACIO is using ServiceRequest but IPS is using Consent.</p>

<p>So this

... *(truncated, 12851 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-50903" (1 results)

- [zulip] 518231067 → [jira] FHIR-50903
  **Source:** [implementers] TreatmentDirective: which resource is for this purpose?
  **Type:** mentions
  **Context:** ...ira ticket because there are more options to discuss and need to be harmonized: https://jira.hl7.org/browse/FHIR-50903 <p>I've created a Jira ticket because the...
  **Score:** 0.38
  **Updated:** 2025-05-15T07:55:51+00:00
**Warnings:**
- Value 'FHIR-50903' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 518231067 — [implementers] TreatmentDirective: which resource is for this purpose?
- **Score:** 0.38
- **Updated:** 2025-05-15T07:55:51+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/implementers/topic/TreatmentDirective%3A%20which%20resource%20is%20for%20this%20purpose%3F/near/518231067
- **Snippet:** ...https://jira.hl7.org/browse/<b>FHIR-50903</b>


```

</details>

### Turn 2

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-50903.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\CommunitybasedCareAndPrivacy\\FHIR-50903.md",
  "file_text": "# FHIR-50903: TreatmentDirective: which FHIR core resource for this purpose?\n\n## Metadata\n| Field         | Value |\n|---------------|-------|\n| **Ticket**    | [FHIR-50903](https://jira.hl7.org/browse/FHIR-50903) |\n| **Type**      | Question |\n| **Priority**  | Medium |\n| **Status**    | Triaged |\n| **Resolution**| Unresolved |\n| **Work Group**| Community-Based Care and Privacy |\n| **Specification** | FHIR Core (FHIR) |\n| **Reporter**  | Eduard de Rijcke |\n| **Assignee**  | Unassigned |\n| **Created**   | 2025-05-15 |\n| **Updated**   | 2025-09-15 |\n\n## Summary\n\nThe reporter (from Nictiz / HL7 Netherlands) asks which FHIR core resource best represents a **TreatmentDirective** \u2014 a joint decision between a health professional and a patient (or representative) about the desirability of performing specific treatments (e.g., ICU admission, CPR, artificial respiration). The Dutch \"zib\" (health information building block) [TreatmentDirective2](https://zibs.nl/wiki/TreatmentDirective2-v1.0(2020EN)) models three outcomes: *Execute*, *Do not execute*, and *Other* (conditional execution).\n\nThe core question is whether **Consent** or **ServiceRequest** is the correct resource:\n- **Consent** represents legal directives and agreements; IPS uses it for advance directives.\n- **ServiceRequest** is actionable and supports `doNotPerform`; PACIO ADI IG uses it for DNR orders.\n- Neither resource natively supports three-valued outcomes \u2014 both are binary (permit/deny or doNotPerform boolean), requiring an extension for the conditional \"other\" option.\n\nThe issue was discussed at the **May 2025 WGM in Madrid** (Patient Care session), where the resource landscape was mapped: Goal for informal wishes, ServiceRequest for DNR orders (PACIO), Consent for legal directives (IPS), and Observation for patient preferences (PACIO). A harmonization gap between PACIO (ServiceRequest) and IPS (Consent) was identified, and Rob Hausam was informed.\n\nAs of September 2025, the reporter's team chose **Consent for R4** (documented on [Simplifier](https://simplifier.net/nictiz-r4-zib2020/documentation-zib-treatmentdirective2)), noting it worked \"well enough\" in testing, but expressed hope for a better solution in R6.\n\n## Details\n\n### Background \u2014 The Dutch TreatmentDirective Model\nThe zib TreatmentDirective2 captures a clinical agreement between provider and patient about specific treatments. It goes beyond simple advance directives: it includes a three-valued `TreatmentPermitted` element (Yes / Yes-But / No), the specific treatment, verification status, and links to advance directives. The \"Yes-But\" (JA_MAAR) conditional scenario is the key challenge \u2014 neither Consent (permit/deny) nor ServiceRequest (doNotPerform boolean) can express it without an extension.\n\n### Resource Evaluation from WGM Madrid (May 2025)\n| 

... *(truncated, 9673 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\CommunitybasedCareAndPrivacy\FHIR-50903.md with 9465 characters
```

</details>


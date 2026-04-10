# Session Log: FHIR-29978

**Phase:** prepared
**Work Group:** PatientCare
**Source File:** `prepared/PatientCare/FHIR-29978.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29978` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 00:28:02 UTC |
| **Duration** | 94s |
| **Total Tool Calls** | 14 |
| **Total Tokens** | 258,023 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29978
## Work Group: Patient Care
## Output File: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-29978.md

## Data Access
Use FhirAugury MCP tools (preferred).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29978", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29978", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29978", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-29978.md
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
  "id": "FHIR-29978",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29978: Clarify IG's scope by expanding the narrative

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** US PACIO Cognitive Status (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Vreeman
- **Created:** 2020-12-15T04:04:59+00:00
- **Updated:** 2021-11-04T14:58:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29978

## Content
<p>The narrative does not truly describe the scope of this IG. Please help readers and implementers by addressing the central issue: how does this IG define "cognitive status" and what kinds of information is it intended to cover.</p>

<p>Let's unpack this issue a little further. </p>

<p>What anchoring framework or standard terminology is used as the basis for defining the domain?  Should it include assessments related to intellectual disabilities, learning disorders, or substance-induced impairments? What about the range of neuropsychological functional abilities/limitations? We recommend that both PACIO IGs anchor their labels and concept domains to the most well-established international framework for describing functioning and disability: the WHO's International Classification of Functioning, Disability and Health (ICF).  The ICF framework will also be part of future ICD-11 which increases the validity of the framework and facilitates a stucture that can be used globally. Such a framework will be invaluable when trying to represent content from complex domains.</p>

<p>Further, "status" implies a singular axis of assessment. From both the ICF and the CMS-required assessment instruments, it is clear that several dimensions of functioning can be described (current performance, capability, goals, etc) and are related to both physiological, personal, and environmental factors. "Status" does not adequately capture this breadth. Rather, we propose (in conjunction with our recommendation to merge the IGs) that a simpler umbrella term of "functioning" be applied and that subdomain areas be identified as needed using the ICF's conceptual framework. For example, mental functioning. This is consistent with the current proposals in the USCDI.</p>

<p>Last, the scope of both IGs should be clarified with respect to the kinds of data (e.g. Resource types) that have been modeled. Rightly so, there has been heavy focus on Observations. Is it intended to only cover content contained in the CMS-required assessment instruments? Further, it is not clear whether representation of Conditions (diagnoses), Goals, Medications, Interventions, etc are in scope (now or in the future).</p>

## Comments (3)

### lynn_laakso — 2021-11-04T14:58:59+00:00
<p>re-opening for consideration post STU1 publication</p>

### lynn_laakso — 2021-11-04T14:58:59+00:00
<p>Reverted previous resolution: Considered for Future Use made 2021-06-28 00:00:00.0 with vote Caleb Wan / Jay Lyle: 6 - 0 - 0//(Impact: null; Category: null; Version: null)//* Other ballot comments also raised this issue of the need of a definition for cognitive status. In addressing those ballot comments, PACIO has come up with a definition and also added statements to emphasize that the IG is intended to include more broadly clinical domains in mental functioning observations. PACIO is using the conceptual framework of the International Classification of Function (ICF) and will in the future to expand the IG to cover information such as memory functions, orientation functions, attention functions, mood, etc.</p>
<ul>
	<li>Another issue the ballot comment raised concerns the IG title “Cognitive Status.” It was pointed out that the term “status” used in the title implies a singular axis of assessment and does not adequately capture several dimensions of functioning. Will set aside this issue for future consideration and will address it along with <a href="https://jira.hl7.org/browse/FHIR-29977" title="Merge the Functional Status IG 

... *(truncated, 8450 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29978".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-29978.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\PatientCare\\FHIR-29978.md",
  "file_text": "# FHIR-29978: Clarify IG's scope by expanding the narrative\n\n## Quick Reference\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-29978](https://jira.hl7.org/browse/FHIR-29978) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Specification** | US PACIO Cognitive Status (FHIR) |\n| **Work Group** | Patient Care |\n| **Reporter** | Daniel Vreeman |\n| **Assignee** | Unassigned |\n| **Created** | 2020-12-15 |\n| **Updated** | 2021-11-04 |\n\n## Summary\n\nDaniel Vreeman requests that the PACIO Cognitive Status IG narrative be substantially expanded to clarify the IG's scope. Three specific concerns are raised:\n\n1. **Domain definition**: The IG does not define \"cognitive status\" or identify what kinds of information it covers. The reporter recommends anchoring the IG to the WHO's International Classification of Functioning, Disability and Health (ICF) framework, which aligns with future ICD-11 and provides a globally recognized structure for functioning and disability domains.\n\n2. **Terminology (\"status\" vs. \"functioning\")**: The term \"status\" implies a singular axis of assessment, but the ICF and CMS-required assessment instruments describe multiple dimensions of functioning (current performance, capability, goals, etc.) influenced by physiological, personal, and environmental factors. The reporter proposes using the umbrella term \"functioning\" with ICF-based subdomain labels (e.g., \"mental functioning\"), consistent with USCDI proposals. This is linked to the companion proposal to merge the Cognitive Status and Functional Status IGs (FHIR-29977).\n\n3. **Resource type scope**: The IG focuses heavily on Observations from CMS-required assessment instruments. It is unclear whether Conditions, Goals, Medications, Interventions, or other resource types are in scope now or in the future.\n\n## Keywords\n\n`cognitive status`, `functional status`, `ICF`, `International Classification of Functioning`, `scope`, `narrative`, `PACIO`, `functioning`, `assessment`, `CMS`, `USCDI`, `domain`, `mental functioning`, `Observation`\n\n## Comment History\n\n| Date | Author | Summary |\n|------|--------|---------|\n| 2020-12-15 | jiraadmin | Imported from spreadsheet by jduteau (comment #26) |\n| 2021-11-04 | lynn_laakso | Reverted previous resolution of \"Considered for Future Use\" (ballot vote: Caleb Wan / Jay Lyle, 6-0-0). Notes: PACIO has since defined \"cognitive status\" and broadened the IG to include mental functioning observations, adopting the ICF conceptual framework. The title concern (\"status\" vs broader term) is deferred for future consideration alongside FHIR-29977 (merge IGs). |\n| 2021-11-04 | lynn_laakso | Re-opening for consideration post STU1 publication |\n\n## Related Tickets\n\n| Ticket | Title | Status | Relationship |\n|--------|-------|-----

... *(truncated, 8356 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\PatientCare\FHIR-29978.md with 8161 characters
```

</details>

### Turn 3

**Assistant:**

Good. Let me get details on the closely related sibling tickets and a relevant Zulip thread.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29978: Clarify IG's scope by expanding the narrative

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** US PACIO Cognitive Status (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Vreeman
- **Created:** 2020-12-15T04:04:59+00:00
- **Updated:** 2021-11-04T14:58:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29978

## Content
<p>The narrative does not truly describe the scope of this IG. Please help readers and implementers by addressing the central issue: how does this IG define "cognitive status" and what kinds of information is it intended to cover.</p>

<p>Let's unpack this issue a little further. </p>

<p>What anchoring framework or standard terminology is used as the basis for defining the domain?  Should it include assessments related to intellectual disabilities, learning disorders, or substance-induced impairments? What about the range of neuropsychological functional abilities/limitations? We recommend that both PACIO IGs anchor their labels and concept domains to the most well-established international framework for describing functioning and disability: the WHO's International Classification of Functioning, Disability and Health (ICF).  The ICF framework will also be part of future ICD-11 which increases the validity of the framework and facilitates a stucture that can be used globally. Such a framework will be invaluable when trying to represent content from complex domains.</p>

<p>Further, "status" implies a singular axis of assessment. From both the ICF and the CMS-required assessment instruments, it is clear that several dimensions of functioning can be described (current performance, capability, goals, etc) and are related to both physiological, personal, and environmental factors. "Status" does not adequately capture this breadth. Rather, we propose (in conjunction with our recommendation to merge the IGs) that a simpler umbrella term of "functioning" be applied and that subdomain areas be identified as needed using the ICF's conceptual framework. For example, mental functioning. This is consistent with the current proposals in the USCDI.</p>

<p>Last, the scope of both IGs should be clarified with respect to the kinds of data (e.g. Resource types) that have been modeled. Rightly so, there has been heavy focus on Observations. Is it intended to only cover content contained in the CMS-required assessment instruments? Further, it is not clear whether representation of Conditions (diagnoses), Goals, Medications, Interventions, etc are in scope (now or in the future).</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29977: Merge the Functional Status IG and Cognitive Status IG.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Care
- **specification:** US PACIO Cognitive Status (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Vreeman
- **labels:** Fit-For-Teleconference, future
- **Created:** 2020-12-15T04:04:57+00:00
- **Updated:** 2021-11-04T14:58:58+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29977

## Content
<p>After reviewing both PACIO IGs (Functional Status and Cognitive Status), it is unclear why two separate IGs are needed. There is substantial overlap between the two implementation guides, and no discernable differences in the driving use cases. To the reader, it feels as though they are &gt; 80% of the narrative is the same. Although a few parts (e.g. extensions) differ, the detail of the profiles and element bindings are basically the same. Splitting them into two IGs and having different profile names for subsections of content drawn from the same overall instrument (e.g. the CMS-required patient assessment instruments like MDS, OASIS, etc) imposes additional burden on implementers (and receivers). The rationale for splitting the IGs was not described in the IG. We propose merging the two IGs into a common core for functioning data, with the small number of domain-specific profiles that are needed being organized into subsections. Looking ahead to the other kinds of content being contemplated by the PACIO project, we believe this will be a more robust foundation.</p>

<p>Is there value in having two IGs? Please stongly consider merging the two IGs.</p>

```

</details>

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# implementers > Cognitive and Functional Status

**Messages:** 3
**First message:** 2021-07-07 20:09:01+00:00
**Last message:** 2021-07-07 21:45:15+00:00
**Participants:** Amy Allen, Lloyd McKenzie

## Messages

### Amy Allen — 2021-07-07 20:09:01+00:00
In order to provide all the data required via FHIR for generating a CDA (using e1 VDT test data), we need to be able to deliver cognitive and functional status. We previously included this data in STU3 Observation. Neither Observation nor Condition category value sets really accommodate this data type which has been known as impairments. This is not really the documentation of an assessment, it is more of a statement that patient has a "dependence on cane". Curious how/where others have included this type of information and whether or not Observation is the right place.

### Lloyd McKenzie — 2021-07-07 20:11:46+00:00
Observation is definitely the right place. The value set defined for Observation is just an example. It's not intended to cover all possible observation type. You might look at these two IGs: http://hl7.org/fhir/us/pacio-cs , http://hl7.org/fhir/us/pacio-fs

### Amy Allen — 2021-07-07 21:45:15+00:00
Thank you, I will review that documentation

---
*URL: https://chat.fhir.org/#narrow/stream/implementers/topic/Cognitive%20and%20Functional%20Status*

```

</details>

### Turn 4

**Assistant:**

Let me fetch the most closely related tickets for fuller context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29978: Clarify IG's scope by expanding the narrative

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** US PACIO Cognitive Status (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Vreeman
- **Created:** 2020-12-15T04:04:59+00:00
- **Updated:** 2021-11-04T14:58:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29978

## Content
<p>The narrative does not truly describe the scope of this IG. Please help readers and implementers by addressing the central issue: how does this IG define "cognitive status" and what kinds of information is it intended to cover.</p>

<p>Let's unpack this issue a little further. </p>

<p>What anchoring framework or standard terminology is used as the basis for defining the domain?  Should it include assessments related to intellectual disabilities, learning disorders, or substance-induced impairments? What about the range of neuropsychological functional abilities/limitations? We recommend that both PACIO IGs anchor their labels and concept domains to the most well-established international framework for describing functioning and disability: the WHO's International Classification of Functioning, Disability and Health (ICF).  The ICF framework will also be part of future ICD-11 which increases the validity of the framework and facilitates a stucture that can be used globally. Such a framework will be invaluable when trying to represent content from complex domains.</p>

<p>Further, "status" implies a singular axis of assessment. From both the ICF and the CMS-required assessment instruments, it is clear that several dimensions of functioning can be described (current performance, capability, goals, etc) and are related to both physiological, personal, and environmental factors. "Status" does not adequately capture this breadth. Rather, we propose (in conjunction with our recommendation to merge the IGs) that a simpler umbrella term of "functioning" be applied and that subdomain areas be identified as needed using the ICF's conceptual framework. For example, mental functioning. This is consistent with the current proposals in the USCDI.</p>

<p>Last, the scope of both IGs should be clarified with respect to the kinds of data (e.g. Resource types) that have been modeled. Rightly so, there has been heavy focus on Observations. Is it intended to only cover content contained in the CMS-required assessment instruments? Further, it is not clear whether representation of Conditions (diagnoses), Goals, Medications, Interventions, etc are in scope (now or in the future).</p>

## Comments (3)

### lynn_laakso — 2021-11-04T14:58:59+00:00
<p>re-opening for consideration post STU1 publication</p>

### lynn_laakso — 2021-11-04T14:58:59+00:00
<p>Reverted previous resolution: Considered for Future Use made 2021-06-28 00:00:00.0 with vote Caleb Wan / Jay Lyle: 6 - 0 - 0//(Impact: null; Category: null; Version: null)//* Other ballot comments also raised this issue of the need of a definition for cognitive status. In addressing those ballot comments, PACIO has come up with a definition and also added statements to emphasize that the IG is intended to include more broadly clinical domains in mental functioning observations. PACIO is using the conceptual framework of the International Classification of Function (ICF) and will in the future to expand the IG to cover information such as memory functions, orientation functions, attention functions, mood, etc.</p>
<ul>
	<li>Another issue the ballot comment raised concerns the IG title “Cognitive Status.” It was pointed out that the term “status” used in the title implies a singular axis of assessment and does not adequately capture several dimensions of functioning. Will set aside this issue for future consideration and will address it along with <a href="https://jira.hl7.org/browse/FHIR-29977" title="Merge the Functional Status IG 

... *(truncated, 4279 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-30036: Decription of what functional status is will provide clarity.

- **status:** Published
- **type:** Change Request
- **priority:** High
- **work_group:** Patient Care
- **specification:** US PACIO Functional Status (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Matt Elrod
- **Created:** 2020-12-16T00:33:05+00:00
- **Updated:** 2021-11-04T14:56:16+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-30036

## Content
<p>There are no details about what functional status is and how it will be defined and used in this IG.  A new section should added to included a "Functional Status" section. </p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>n/a</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Functional Status:<br/>
Functional status is often used to describe how a person is able to interact with their environment and is a foundation to patient centered care.  It is used in reporting outcomes for clinical care, quality improvement activities, quality measure reporting, and research.   Identifying a decline in functional status has been shown to be a first sign in declining health for individuals with chronic conditions and indicative of the severity of an acute illness.  Functional status is often used as a risk factor assessment tool; prognostic indicator hospital readmission; and predictor of morbidity and mortality.  Information related to functional status is often a major focus for seeking healthcare and making end of life decisions.   There have even been discussion to include functional status a the sixth vital sign.  <br/>
Domains with in functional status include Domestic Life/ Instrumental Activities of Daily Living (IADLs), Mobility, and Self-care.  Using the conceptual framework of the International Classification of Function (ICF), these domains can be further broken down in to more specific data elements.  For example,  mobility includes aspects such as rolling over, transferring, walking short distances, etc.  While this domains and data elements can be represented in data structures for observation, there is not an agreed upon standard to represent the discrete data elements.  <br/>
Therefor this IG will leverage standardized patients assessments that are used for reporting to CMS related to functional status domains.</p>

## Comments (2)

### matt_elrod — 2021-08-20T18:14:58+00:00
<p>Agree with updates</p>

### jiraadmin — 2020-12-16T00:33:07+00:00
<p>Imported from spreadsheet by jduteau - comment #45</p>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-38054: Reference to ICF should provide more detailed mapping

- **status:** Published
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Care
- **specification:** US PACIO Personal Functioning and Engagement (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Floyd Eisenberg
- **labels:** Block-Vote-3, STU2-Block-Vote-1
- **Created:** 2022-08-31T13:46:03+00:00
- **Updated:** 2025-07-23T17:51:02+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-38054

## Content
<p>1. Background states, <br/>
"Examples of domains that ICF defines that the IG can be applied to include but are not limited to:<br/>
Mental functions captured as a part of evaluating an individual's cognitive status<br/>
Mobility and Self-care captured as a part of evaluating an individual's functional status<br/>
Communication, voice, and speech functions captured as a part of evaluating an individual's spoken language communication, swallowing, and hearing<br/>
More information on the concepts that may be included in this IG can be found in the ICF Browser."<br/>
While this is helpful, merely reference to the ICF domains fails to provide a clear direction of how to apply the ICF domains to the artifacts and examples identified in the IG.  Specifically, the Social Security Act requirements each include multiple ICF domains within the standardized patient assessment data through commonly used PAC assessment instruments:</p>
<ul>
	<li>Minimum Data Set (MDS) for SNFs</li>
	<li>Inpatient Rehabilitation Facility - Patient Assessment Information (IRF - PAI) for IRFs</li>
	<li>LTCH Continuity Assessment Record and Evaluation (CARE) Data Set (LCDS) for LTCHs</li>
	<li>Outcome and Assessment Information Set (OASIS) for HHAs.<br/>
At least one example of a mapping from such an instrument to ICF domains would be helpful. It will also help if any reference can be provided to existing work that maps ICF domains to comment forms and terminologies (specifically LOINC and perhaps SNOMED). The existing content leaves the process completely up to the reader.</li>
</ul>


```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-38618: Question use of Personal and Engagement in the IG Title

- **status:** Published
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Care
- **specification:** US PACIO Personal Functioning and Engagement (FHIR)
- **resolution:** Not Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Michelle L. Dougherty
- **labels:** Block-Vote-1
- **Created:** 2022-09-13T03:04:03+00:00
- **Updated:** 2024-01-05T17:48:57+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-38618

## Content
<p>Clarity is needed on why the term personal and engagement is in the IG title. The background description does not include context. The IG describes an individuals funtioning  from the perspective of the body, the individual, and society. There isn't a need to state that it is "personal" functioning.  The IG does not describe what is meant by engagement and the types of observations that one would expect to see that isn't covered by functioning in ICF.  Recommend modifying the title to remove personal and better clarify the term engagement. If that isn't possible, recommend documentation to help the reader understand why this IG must use the term personal when other IGs that represent an individual's care/treatment/result don't use the term personal.  </p>

```

</details>

### Turn 5

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29978: Clarify IG's scope by expanding the narrative

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Patient Care
- **specification:** US PACIO Cognitive Status (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Vreeman
- **Created:** 2020-12-15T04:04:59+00:00
- **Updated:** 2021-11-04T14:58:59+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29978

## Content
<p>The narrative does not truly describe the scope of this IG. Please help readers and implementers by addressing the central issue: how does this IG define "cognitive status" and what kinds of information is it intended to cover.</p>

<p>Let's unpack this issue a little further. </p>

<p>What anchoring framework or standard terminology is used as the basis for defining the domain?  Should it include assessments related to intellectual disabilities, learning disorders, or substance-induced impairments? What about the range of neuropsychological functional abilities/limitations? We recommend that both PACIO IGs anchor their labels and concept domains to the most well-established international framework for describing functioning and disability: the WHO's International Classification of Functioning, Disability and Health (ICF).  The ICF framework will also be part of future ICD-11 which increases the validity of the framework and facilitates a stucture that can be used globally. Such a framework will be invaluable when trying to represent content from complex domains.</p>

<p>Further, "status" implies a singular axis of assessment. From both the ICF and the CMS-required assessment instruments, it is clear that several dimensions of functioning can be described (current performance, capability, goals, etc) and are related to both physiological, personal, and environmental factors. "Status" does not adequately capture this breadth. Rather, we propose (in conjunction with our recommendation to merge the IGs) that a simpler umbrella term of "functioning" be applied and that subdomain areas be identified as needed using the ICF's conceptual framework. For example, mental functioning. This is consistent with the current proposals in the USCDI.</p>

<p>Last, the scope of both IGs should be clarified with respect to the kinds of data (e.g. Resource types) that have been modeled. Rightly so, there has been heavy focus on Observations. Is it intended to only cover content contained in the CMS-required assessment instruments? Further, it is not clear whether representation of Conditions (diagnoses), Goals, Medications, Interventions, etc are in scope (now or in the future).</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-29977: Merge the Functional Status IG and Cognitive Status IG.

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** Patient Care
- **specification:** US PACIO Cognitive Status (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Daniel Vreeman
- **labels:** Fit-For-Teleconference, future
- **Created:** 2020-12-15T04:04:57+00:00
- **Updated:** 2021-11-04T14:58:58+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29977

## Content
<p>After reviewing both PACIO IGs (Functional Status and Cognitive Status), it is unclear why two separate IGs are needed. There is substantial overlap between the two implementation guides, and no discernable differences in the driving use cases. To the reader, it feels as though they are &gt; 80% of the narrative is the same. Although a few parts (e.g. extensions) differ, the detail of the profiles and element bindings are basically the same. Splitting them into two IGs and having different profile names for subsections of content drawn from the same overall instrument (e.g. the CMS-required patient assessment instruments like MDS, OASIS, etc) imposes additional burden on implementers (and receivers). The rationale for splitting the IGs was not described in the IG. We propose merging the two IGs into a common core for functioning data, with the small number of domain-specific profiles that are needed being organized into subsections. Looking ahead to the other kinds of content being contemplated by the PACIO project, we believe this will be a more robust foundation.</p>

<p>Is there value in having two IGs? Please stongly consider merging the two IGs.</p>

```

</details>


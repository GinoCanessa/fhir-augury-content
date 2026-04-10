# Session Log: FHIR-26719

**Phase:** prepared
**Work Group:** FinancialMgmt
**Source File:** `prepared/FinancialMgmt/FHIR-26719.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-26719` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 22:55:05 UTC |
| **Duration** | 92s |
| **Total Tool Calls** | 11 |
| **Total Tokens** | 216,955 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-26719
## Work Group: Financial Mgmt
## Output File: C:\ai\git\fhir-augury-content\prepared\FinancialMgmt\FHIR-26719.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-26719", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-26719", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-26719", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FinancialMgmt\FHIR-26719.md
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
  "id": "FHIR-26719",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-26719: Define Provider Network Contracting Status in the adjudication section of the EOB Resource

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Future-EOB.resource
- **Created:** 2020-04-07T08:59:07+00:00
- **Updated:** 2025-10-30T14:20:06+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26719

## Content
<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
<a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). Description:  Indicates that the Provider has a contract with the Plan (regardless of the network) as of the effective date of service or admission.  Values are contracted | non-contracted.<br/>
The data element resides in all claims.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The IG defines the Provider Network Contracting Status for several types of providers; i.e., billing, attending, refering, performing, PCP, site as supporting.info</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Define these data elements within the adjudication section</p>

## Comments (4)

### corey_spears — 2025-10-30T14:20:06+00:00
<p>This ticket was originally submitted for the CARIN BB IG, but is a FHIR Core request.</p>

### lynn_laakso — 2022-11-28T16:09:51+00:00
<p>re-open post STU2 publication</p>

### lynn_laakso — 2022-11-28T16:09:51+00:00
<p>Reverted previous resolution: Considered for Future Use made 2020-07-21 00:00:00.0 with vote Mark Roberts/Pat Taylor: 18-0-5//(Impact: null; Category: null; Version: null)//Consider in the next FHIR version</p>

### mark_roberts — 2020-04-09T18:26:04+00:00
<p>Comment #62</p>


## Snapshot
# FHIR-26719: Define Provider Network Contracting Status in the adjudication section of the EOB Resource

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Patricia Taylor  
**Work Group:** Financial Mgmt  
**Specification:** FHIR Core (FHIR)  
**Labels:** Future-EOB.resource  
**Created:** 2020-04-07  
**Updated:** 2025-10-30  

## Description

<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
<a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). Description:  Indicates that the Provider has a contract with the Plan (regardless of the network) as of the effective date of service or admission.  Values are contracted | non-contracted.<br/>
The data element resides in all claims.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The IG defines the Provider Network Contracting Status for several types of providers; i.e., billing, attending, refering, performing, PCP, site as supporting.info</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Define these data elements within the adjudication section</p>

## Comments

### corey_spears (2025

... *(truncated, 4485 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-26719".
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
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FinancialMgmt\FHIR-26719.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FinancialMgmt\\FHIR-26719.md",
  "file_text": "# FHIR-26719: Define Provider Network Contracting Status in the adjudication section of the EOB Resource\n\n## Ticket Summary\n\n| Field         | Value                                                                                     |\n|---------------|-------------------------------------------------------------------------------------------|\n| **Key**       | [FHIR-26719](https://jira.hl7.org/browse/FHIR-26719)                                     |\n| **Status**    | Triaged                                                                                   |\n| **Type**      | Change Request                                                                            |\n| **Priority**  | Medium                                                                                    |\n| **Resolution**| Unresolved                                                                                |\n| **Work Group**| Financial Mgmt                                                                            |\n| **Spec**      | FHIR Core (FHIR)                                                                         |\n| **Reporter**  | Patricia Taylor                                                                           |\n| **Assignee**  | Unassigned                                                                                |\n| **Labels**    | Future-EOB.resource                                                                       |\n| **Created**   | 2020-04-07                                                                                |\n| **Updated**   | 2025-10-30                                                                                |\n\n## Description\n\nThe ticket requests that Provider Network Contracting Status be defined as a data element within the adjudication section of the ExplanationOfBenefit (EOB), Claim, and ClaimResponse resources in FHIR Core, rather than as `supportingInfo`.\n\n**Current State:** The CARIN Blue Button IG defines Provider Network Contracting Status for various provider types (billing, attending, referring, performing, PCP, site) as `supportingInfo` elements.\n\n**Proposed Change:** Move these data elements into the adjudication section of the EOB resource. The contracting status indicates whether a provider has a contract with the payer plan (regardless of network) as of the effective date of service or admission, with values: `contracted` | `non-contracted`.\n\n## Keywords\n\n`provider network`, `contracting status`, `adjudication`, `ExplanationOfBenefit`, `EOB`, `Claim`, `ClaimResponse`, `supportingInfo`, `CARIN Blue Button`, `FHIR Core`\n\n## Comment History\n\n| Date       | Author        | Summary                                                                                      |\n|------------|---------------|--------------------------------------------------------------------------------

... *(truncated, 10683 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FinancialMgmt\FHIR-26719.md with 10518 characters
```

</details>

### Turn 3

**Assistant:**

Let me fetch the related Zulip thread and the most relevant related tickets.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# CARIN IG for Blue Button® > CPCDS EOB Data Fields

**Messages:** 15
**First message:** 2020-06-08 14:39:07+00:00
**Last message:** 2021-04-21 16:03:49+00:00
**Participants:** Christopher Marchand, Amol Vyas, Pat Taylor, Kate Dech, John Achoukian, Michele Mottini, Ryan Howells, Bryan Briegel

## Messages

### Christopher Marchand — 2020-06-08 14:39:07+00:00
Hi team - what field in the CPCDS EOB file would represent the main billing code or visit type (i.e. medium complex office visit)?

### Christopher Marchand — 2020-06-12 15:56:41+00:00
@Amol Vyas any insight on the above ^ ? I do not see any field representing this in CPCDS EOB.

### Amol Vyas — 2020-06-14 21:14:13+00:00
Christopher Marchand said : Hi team - what field in the CPCDS EOB file would represent the main billing code or visit type (i.e. medium complex office visit)? Amol Vyas any insight on the above ^ ? I do not see any field representing this in CPCDS EOB. Hi Christopher, per the type (profile) of the adjudicated claim/EOB, I believe you will find this information in one of couple of profile structures. For institutional/facility (inpatient/outpatient) claims - Type Of Bill (Type Of Care sub-field). Note that Type Of Bill structure will be consolidated into one field in the upcoming update to the IG. For professional/non-clinician claims - Procedure Codes (CPT/HCPCS Level 1, 2) For more information, the current IG page and the May FHIR Connectathon CARIN BB track 's latest materials page , list the a) CARIN BB profile mapping and b) CARIN BB profile comparison in the their current and updated versions, respectively. We will be deploying these and other updates that are approved as part of the IG's HL7 ballot reconciliation process so far to the build environment soon. @Pat Taylor , @MaryKay McDaniel : Please feel free to validate above.

### Christopher Marchand — 2020-07-16 13:48:40+00:00
@Amol Vyas , @Pat Taylor , @MaryKay McDaniel Do you have a date when you will have the IG updated with the latest mapping documents and specs? I am struggling to follow all the changes and notice that there are conflicting materials on different pages and sources which is making development complicated.

### Pat Taylor — 2020-07-20 14:53:04+00:00
The mapping document and specs should reflect the one dated May 15th. The next published version will include the May 15th version. We are working on another update and are targeting completing it within the next two weeks. The most current version is attached to JIRA-26741 @Amol Vyas @MaryKay McDaniel @Saul Kravitz @Mark Roberts

### Kate Dech — 2020-07-21 19:12:15+00:00
@Pat Taylor , @Amol Vyas , @MaryKay McDaniel , @Saul Kravitz , @Mark Roberts - Can you also update the CPCDS Mapping spreadsheet that is published on the CARIN Confluence page? I have been using that as the guide so it's good to know that there is a more recent version - and one soon to follow in a few weeks. Also I have specific questions about the adjudication amount type categories from the original mapping to the 0513 version. There had been a category code for Allowed. That isn't in the current set. Is Eligible to be used in it's place? There had been a category code for Payment (generically to represent the total, not the split out between payment to provider and payment to patient). Is Benefit to be used in its place? You still have PaidByPatient and in the IG the definition is "The amount paid by the patient at the point of service." That is a very different description than what I see in the Data Element Index of the mapping artifact. That description is more about what the payer determined the total member responsibility: "Amount that is calculated by the processor and returned to the pharmacy as the total amount to be paid by the patient to the pharmacy; the patient’s total cost share, including copayments, amounts applied to deductible, over maximum amounts, penalties, etc." My business cohorts think this desciption more aptly f

... *(truncated, 8682 chars total)*
```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26719: Define Provider Network Contracting Status in the adjudication section of the EOB Resource

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Future-EOB.resource
- **Created:** 2020-04-07T08:59:07+00:00
- **Updated:** 2025-10-30T14:20:06+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26719

## Content
<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
<a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). Description:  Indicates that the Provider has a contract with the Plan (regardless of the network) as of the effective date of service or admission.  Values are contracted | non-contracted.<br/>
The data element resides in all claims.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The IG defines the Provider Network Contracting Status for several types of providers; i.e., billing, attending, refering, performing, PCP, site as supporting.info</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Define these data elements within the adjudication section</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26992: Replace CARIN Blue Button Adjudication Amount Category Value Set with Adjudication CARINBB Value Set

- **status:** Published
- **type:** Change Request
- **priority:** Highest
- **work_group:** Financial Mgmt
- **specification:** US CARIN Blue Button (FHIR)
- **resolution:** Persuasive with Modification
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Block-Vote-3f, C4BB
- **Created:** 2020-04-29T12:01:56+00:00
- **Updated:** 2020-11-23T17:51:13+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26992

## Content
<p>Ballot feedback was that the Terminology Section of the IG requires a major overall, renaming the Value Sets and Code Systems and updating links.  Following is a recommended resolution for the categories of adjudication amounts:</p>

<p>1)  Delete Value Set <a href="https://build.fhir.org/ig/HL7/carin-bb/ValueSet-CARIN-BB-Adjudication-Amount-Category.html" class="external-link" target="_blank" rel="nofollow noopener">CARIN Blue Button Adjudication Amount Category Value Set</a></p>

<p>2)  Delete Code System CARIN-BB-Adjudication-Category</p>

<p>3)  Define Value Set AdjudicationCarinBBValueCodes</p>

<p>4)  Title:  Adjudication CARINBB Value Codes</p>

<p>5) Description:  Describes the various amount fields used when payers receive and adjudicate a claim</p>

<p>6) <a href="http://hl7.org/fhir/us/ValueSet/adjudication-carinbb-value-codes" class="external-link" target="_blank" rel="nofollow noopener">http://hl7.org/fhir/us/ValueSet/adjudication-carinbb-value-codes</a> where values include the following codes from the Code System <a href="https://www.hl7.org/fhir/codesystem-adjudication.html:" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/codesystem-adjudication.html:</a> submitted | eligible | deductible |coinsurance | copay | noncovered | priorpayerpaid | benefit | paidbypatient | paidtoprovider | paidtopatient | memberliability | discount | drugcost</p>

<p>7)  Using this Code System assumes that values have been added as harmonized with CARIN RTPBC</p>

<p>8)  Bind the ValueSet with binding strength required to the the slice adjudicationamounttype, data element item.adjudication.category, adjudication.category and total.category in the Inpatient Facility and Outpatient Institutional Profiles</p>

<p>9)  Bind the ValueSet with binding strength required to the slice adjudicationamounttype, data element item.adjudication.category and total.category in the Professional and Non-Clinician Profile</p>

<p>10)  Bind the ValueSet with binding strength required to the slice adjudicationamounttype, data element total.category in the Pharmacy Profile</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-32776: Add more guidance on the expected use of adjudication and supportingInfo

- **status:** Published
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Persuasive
- **assignee:** Unassigned
- **reporter:** Corey Spears
- **Created:** 2021-05-25T17:53:34+00:00
- **Updated:** 2023-03-30T20:28:11+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-32776

## Content
<p>After working on developing the CARIN BB IG profiling the ExplanationOfBenefit, it seems that the ExplanationOfBenefit resource could add more guidance on repeating elements that are likely to be sliced or otherwise have more specific meaning based on a child category element.</p>

<p>The information presented in adjudication (EoB.adjudication and EoB.item.adjudication), total, and supportingInfo has a different context based on the category code presented in each (e.g. an adjudication occurrence may represent an amount paid by the patient. Another could represent amount paid to the provider). This structure should be further explained in the standard</p>

<p> </p>

<p>Additionally, there are several parts of the EoB (careTeam, Diagnosis, Procedure, supportingIno) that are linked to item and addItem by sequence numbers. Some guidance specifically pointing this out would likely be welcomed by implementers and IG developers alike. (particularly for something like the instance where the name does not match as is the case where informationSequence is supposed to link to a supportingInfo.sequence occurrence)</p>

<p>I would suggest adding this guidance to the section above Search Parameters.</p>

<p>I would also suggest guidance on the use and expectation of those sequence numbers. Is it possible to have a item.InformationSequence that references a supportingInfo occurrence that does not exist? Does there need to be an invariant added that would require a sequence reference to a sequence that exists.?</p>

<p> </p>

<p> </p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-51208: Inconsistency related to NonCovered amount

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** US CARIN Blue Button (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Ankita Srivastava
- **labels:** STU3
- **Created:** 2025-06-24T06:44:48+00:00
- **Updated:** 2026-01-29T06:20:15+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-51208

## Content
<p>Hi Team,</p>

<p>Depending on the denial code, the non-covered amount may be the responsibility of the provider or member. But according to the FHIR definition, the same essence is not present:</p>

<p>"Noncovered: The portion of the cost of this service that was deemed not eligible by the insurer because the service or member was not covered by the subscriber contract."</p>

<p> </p>

<p>May I please request the elaborative details here to avoid any confusion?</p>

<p> </p>

<p>Also, Notes on Fields section under ExplanationOfBenefit-Inpatient-Institutional has conflicting calculations:</p>

<p>"total.amount:  Eligible amount = submitted amount - the noncovered amount - discount.  The subscriber pays the member liability = deductible + coinsurance + copay + noncovered.  (part of the member liability may have already been paid to the provider as paidbypatient). The eligible amount - the member liability is the payment amount to the provider (paidtoprovider) or the subscriber (paidtopatient)"</p>

<p> </p>

<p>Here, noncovered amount is subtracted from the submitted amount to get the Eligible amount.</p>

<p>Then, considering noncovered amount as member's liability it is included while calculating the member liability amount again.</p>

<p>And then member liability portion (which has noncovered component as well) is subtracted from the eligible amount to get the paidtoprovider/paidtopatient amount.</p>

<p> </p>

<p>That means noncovered amount was subtracted twice here to get the paidtoprovider/paidtopatient amount.</p>

<p> </p>

<p>Could you please rectify the calculation issue here?</p>

<p> </p>

<p> </p>

<p> </p>

```

</details>

### Turn 4

**Assistant:**

Let me fetch the most closely related tickets for context.

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26719: Define Provider Network Contracting Status in the adjudication section of the EOB Resource

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Future-EOB.resource
- **Created:** 2020-04-07T08:59:07+00:00
- **Updated:** 2025-10-30T14:20:06+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26719

## Content
<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
<a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). Description:  Indicates that the Provider has a contract with the Plan (regardless of the network) as of the effective date of service or admission.  Values are contracted | non-contracted.<br/>
The data element resides in all claims.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The IG defines the Provider Network Contracting Status for several types of providers; i.e., billing, attending, refering, performing, PCP, site as supporting.info</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Define these data elements within the adjudication section</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26721: Define the various payer adjudication amount fields in the EOB adjudication section

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Future-EOB.resource
- **Created:** 2020-04-07T08:59:08+00:00
- **Updated:** 2025-10-30T14:21:35+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26721

## Content
<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
 <a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). Description: Describes the various amount fields used when payers receive and adjudicate a claim. <br/>
 Values are submitted | eligible | deductible |coinsurance | copay | noncovered | priorpayerpaid | benefit | paidbypatient | paidtoprovider | paidtopatient | memberliability | discount | drugcost<br/>
 The data element resides in all claims.</p>
<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>

<p>The IG defines the Adjudication Amount Category as supporting.info</p>
<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>

<p>Define these data elements within the adjudication section</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26720: Define Claim Received Date as an EOB backbone element

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Future-EOB.resource
- **Created:** 2020-04-07T08:59:07+00:00
- **Updated:** 2025-10-30T14:20:52+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26720

## Content
<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
<a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). The data element resides in all claims.</p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The IG defines Claim Received Date as supporting.info</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Define this date in a way similar to created</p>

```

</details>

<details>
<summary>`FhirAugury-get_item`</summary>

**Result:**
```
# [jira] FHIR-26717: Define NCPDP data elements as EOB backbone data elements

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Financial Mgmt
- **specification:** FHIR Core (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Patricia Taylor
- **labels:** Future-EOB.resource
- **Created:** 2020-04-07T08:59:05+00:00
- **Updated:** 2025-10-30T14:19:23+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-26717

## Content
<p>H.Resources (Claim / ClaimResponse / ExplanationOfBenefits). I.HTML Page Names (<a href="https://www.hl7.org/fhir/claim.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claim.html</a><br/>
<a href="https://www.hl7.org/fhir/claimresponse.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/claimresponse.html</a></p>

<p><a href="https://www.hl7.org/fhir/explanationofbenefit.html" class="external-link" target="_blank" rel="nofollow noopener">https://www.hl7.org/fhir/explanationofbenefit.html</a>). These NCPDP data elements are required on all retail pharmacy claims.  </p>

<h3><a name="ExistingWording%3A"></a>Existing Wording:</h3>
<p>The IG defines several NCPDP data elements as supporting.info</p>

<h3><a name="ProposedWording%3A"></a>Proposed Wording:</h3>
<p>Define Days supply, DAW product selection code, Refill number, Prescription origin code, Plan reported brand-generic code as Claim / ClaimResponse / EOB backbone data elements</p>

```

</details>


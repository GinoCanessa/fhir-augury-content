# Session Log: FHIR-29357

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-29357.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-29357` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 21:49:43 UTC |
| **Duration** | 103s |
| **Total Tool Calls** | 16 |
| **Total Tokens** | 265,414 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-29357
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29357.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-29357", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-29357", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-29357", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29357.md
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
  "id": "FHIR-29357",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-29357: Discover supported events

- **status:** Triaged
- **type:** Change Request
- **priority:** Highest
- **work_group:** FHIR Infrastructure
- **specification:** SMART Web Messaging (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Bas van den Heuvel
- **Created:** 2020-10-21T19:01:29+00:00
- **Updated:** 2022-05-06T18:26:04+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-29357

## Content
<p>How does a client know what events are supported by the host?</p>

## Comments (4)

### lynn_laakso — 2022-05-06T18:26:04+00:00
<p>re-open after publication of STU1</p>

### lynn_laakso — 2022-05-06T18:26:04+00:00
<p>Reverted previous resolution: Considered for Future Use made 2021-02-19 00:00:00.0 with vote Gino Canessa / Bas van den Heuvel: 8-0-0//(Impact: null; Category: null; Version: null)//This was voted deferred after a lengthy discussion: <a href="https://confluence.hl7.org/pages/viewpage.action?pageId=104565559#SMARTWebMessagingBallotReconciliationCC20210219-CapabilitiesandDiscovery" class="external-link" target="_blank" rel="nofollow noopener">https://confluence.hl7.org/pages/viewpage.action?pageId=104565559#SMARTWebMessagingBallotReconciliationCC20210219-CapabilitiesandDiscovery</a> </p>

<p>From the discussion:</p>
<h4><a name="Proposal%3AWe%27llencourageimplementerstousethenewhandshakeprotocolfordetailedandcontextuallyawarediscoveryofwhatwebmessagingfeaturesanappisallowedtouse.%28Wealreadyhavelanguagetothiseffect.%29"></a>Proposal: We'll encourage implementers to use the new handshake protocol for detailed and contextually-aware discovery of what web messaging features an app is allowed to use. (We already have language to this effect.)</h4>
<h4><a name="Wedon%27twanttooverspecifyatthisstage%3BprovidingmoredetailaboutdiscoveryisagoodtargetforafutureSMWrelease%2Cwhenwehavesomeimplementationexperiencetobuildon."></a>We don't want to over-specify at this stage; providing more detail about discovery is a good target for a future SMW release, when we have some implementation experience to build on.</h4>
<h4><a name="1%29Weshouldaddtothehandshakedocumentationanotethatwearelookingtostandardizemoreofthisbehaviorinafuturerelease%2Cbasedonimplementationexperience."></a>1) We should add to the handshake documentation a note that we are looking to standardize more of this behavior in a future release, based on implementation experience.</h4>
<h4><a name="2%29Weshoulddefinea%22smartwebmessaging%22valuethatserversMAYincludeintheir.wellknown%2Fsmartconfigurationfile%2Cwithinthe%22capabilities%22array.%C2%A0"></a>2) We should define a "smart-web-messaging" value that servers MAY include in their .well-known/smart-configuration file, within the "capabilities[]" array. </h4>

<p>Future pull requests that implement these changes should be linked to this issue in the comments.</p>

<p> </p>

### carl-anderson-msft — 2021-02-19T05:10:48+00:00
<p>A shared document has been created to collect design considerations that will go into the specification of this topic.</p>

<p><a href="https://docs.google.com/document/d/1CUoQbsXv_gcWrqIFF-hme8qrqztRUQqp1yArVNkVWzE/edit?usp=sharing" class="external-link" target="_blank" rel="nofollow noopener">https://docs.google.com/document/d/1CUoQbsXv_gcWrqIFF-hme8qrqztRUQqp1yArVNkVWzE/edit?usp=sharing</a></p>

### jiraadmin — 2020-10-21T19:01:30+00:00
<p>Imported from spreadsheet by jduteau - comment #24</p>


## Snapshot
# FHIR-29357: Discover supported events

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Highest  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Bas van den Heuvel  
**Work Group:** FHIR Infrastructure  
**Specification:** SMART Web Messaging (FHIR)  
**Created:** 2020-10-21  
**Updated:** 2022-05-06  

## Description

<p>How does a client know what events are supported by the host?</p>

## Comments

### lynn_laakso (2022-05-06)

<p>re-open after publication o

... *(truncated, 6801 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
No cross-referenced references found for "FHIR-29357".
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

Now let me search for related Jira tickets and Zulip discussions about SMART Web Messaging discovery and capabilities.

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "values": "SMART Web Messaging discover events capabilities",
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

**Arguments:**
```json
{
  "values": "SMART Web Messaging discovery capabilities handshake",
  "sources": "jira",
  "limit": 10
}
```

**Result:**
```
No results found.
```

</details>

<details>
<summary>`FhirAugury-related_by_keyword`</summary>

**Result:**
```
## Items Related to jira:FHIR-29357 (by keyword similarity)

| Score | Source | ID | Title | Shared Keywords |
|------:|--------|-------|-------|-----------------|
| 21.488 | jira | FHIR-28646 | Not all developers host there own CDS Server | discover, host, client |
| 20.345 | jira | FHIR-43611 | bot clients | discover, event, client |
| 18.586 | jira | FHIR-28684:79413 | FHIR-28684:79413 | discover, host, client, support |
| 18.583 | jira | FHIR-3361 | Message endpoints should be associated with the event protocol | host, event, support |
| 18.505 | jira | FHIR-36675:28730 | FHIR-36675:28730 | discover, client, support |
| 18.471 | jira | FHIR-47954 | In what way can a Client discover support of the framework | discover, client, support |
| 18.346 | jira | FHIR-31463 | Discovery? | discover, client, support |
| 18.273 | jira | FHIR-48986:74631 | FHIR-48986:74631 | discover, host, client |
| 17.798 | jira | FHIR-36928:40881 | FHIR-36928:40881 | host, event, support |
| 17.798 | jira | FHIR-36928:40884 | FHIR-36928:40884 | host, event, support |

⚠️ Related-by-keyword failed for source 'GitHub': Response status code does not indicate success: 404 (Not Found).
⚠️ Related-by-keyword failed for source 'Zulip': Response status code does not indicate success: 404 (Not Found).

```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-29357
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| discover | word | 2 | 10.806 |
| host | word | 1 | 9.048 |
| event | word | 3 | 7.084 |
| client | word | 1 | 5.706 |
| support | word | 3 | 4.474 |

```

</details>

### Turn 3

**Assistant:**

Let me fetch the most relevant Zulip threads and search for GitHub items.

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# smart > SMART Web Messaging & SDC

**Messages:** 20
**First message:** 2025-01-23 08:35:45+00:00
**Last message:** 2025-06-11 07:36:27+00:00
**Participants:** Axel Vanraes, Josh Mandel, Brendan Keeler, Cooper Thompson, Philip Wilford, Lloyd McKenzie, Pete O'Toole

## Messages

### Axel Vanraes — 2025-01-23 08:35:45+00:00
We are integrating an SDC app that captures form data in the form of QuestionnaireResponses. The EHR is a native .NET solution and we are integrated with an embedded browser. Now the EHR needs a realtime feed of the QuestionnaireResponses. I think SMART Web Messaging is a good solution for this. Should I use the scratchpad messages for this use case? Or do I introduce a new messageType?

### Josh Mandel — 2025-01-23 15:01:13+00:00
To my knowledge.(and to my disappointment, because I think it still addresses an unmet need) there have been no real world implementations of smart web messaging -- just want to make sure this is clear as you get started. Have you looked at fhircast as a possibility here, or is that ruled out because you don't have a server in the mix? Anyhow, if you were using web messaging I would use scratch pad if you want to think of these questionnaire responses as something that appears in the EHR UI but aren't yet saved/ finalized to the EHR.

### Axel Vanraes — 2025-01-23 19:18:01+00:00
Have you looked at fhircast as a possibility here, or is that ruled out because you don't have a server in the mix? Not yet, but at this point in time we don't have a server. However, the EHR company is busy setting up FHIR infrastructure so it might be interesting. Currently, we were using MessageEvents anyway and want to move to FHIR based data models for all our integrations so SMART Web Messaging looked like a natural next step. I would use scratch pad if you want to think of these questionnaire responses as something that appears in the EHR UI but aren't yet saved/ finalized to the EHR. Cool I think it's worth at least a prototype! Thx for confirming this approach.

### Brendan Keeler — 2025-02-06 05:30:57+00:00
As an aside, first time I'm hearing about SMART web messaging and it's objectively sick

### Brendan Keeler — 2025-02-06 05:31:36+00:00
Feels like the logical fit for the AI copilot era, to allow for order and condition suggestions

### Brendan Keeler — 2025-02-06 05:32:35+00:00
That being said, in terms of better context synchronization, we first need to do <checks notes> CDS Hooks and FHIRcast

### Axel Vanraes — 2025-02-20 07:48:21+00:00
@Josh Mandel we have a basic implementation of the protocol. Just one major issue: How does the EHR communicate back to the app if a message type is unsupported?

### Axel Vanraes — 2025-02-20 07:48:54+00:00
Any ideas? Or do we add our own error fields?

### Josh Mandel — 2025-02-20 14:49:43+00:00
Very cool. There is not a standardized approach to error handling. One thing we suggest obliquely is that during the handshake you could supply a set of the message types that you do support... Or otherwise expect developers to read your documentation. You could also consider responding with an error message to any requests that you don't support, but this might violate the semantics of the message.. for example the unsupported message type might be one that is not supposed to receive any response at all so app developers might not be listening for one in general.

### Cooper Thompson — 2025-02-20 14:54:04+00:00
Gino and I had a long discussion about this "negotiation of what is supported" problem in the context of Subscriptions, and I think it applies here too. In my experience, apps usually want to do the negotiation of what features an EHR supports weeks or months before an end user tries to use an app. In "real life" the run-time auto-discovery features like querying the CapabilityStatement of the PRD endpoint you are connecting to don't really get used much (except for figuring out URLs, but even those often get pre-coordin

... *(truncated, 7429 chars total)*
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Arguments:**
```json
{
  "limit": 10,
  "sources": "github",
  "values": "FHIR-29357,smart web messaging discover events"
}
```

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
  "limit": 10,
  "sources": "zulip",
  "values": "smart web messaging handshake protocol discovery capabilities"
}
```

**Result:**
```
No results found.
```

</details>

### Turn 4

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29357.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-29357.md",
  "file_text": "# FHIR-29357: Discover supported events\n\n## Ticket Summary\n\n| Field | Value |\n|-------|-------|\n| **Key** | [FHIR-29357](https://jira.hl7.org/browse/FHIR-29357) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Highest |\n| **Resolution** | Unresolved |\n| **Specification** | SMART Web Messaging (FHIR) |\n| **Work Group** | FHIR Infrastructure |\n| **Reporter** | Bas van den Heuvel |\n| **Assignee** | Unassigned |\n| **Created** | 2020-10-21 |\n| **Updated** | 2022-05-06 |\n\n## Description\n\nHow does a client know what events (message types) are supported by the host EHR in SMART Web Messaging?\n\n## Keywords\n\n`discover`, `event`, `host`, `client`, `support`\n\n## History & Prior Discussions\n\nThis ticket was originally filed during the initial ballot of SMART Web Messaging (Oct 2020). During ballot reconciliation on 2021-02-19, it was voted **8-0-0** (Gino Canessa / Bas van den Heuvel) to defer as **\"Considered for Future Use\"** after lengthy discussion ([Confluence: Capabilities and Discovery](https://confluence.hl7.org/pages/viewpage.action?pageId=104565559#SMARTWebMessagingBallotReconciliationCC20210219-CapabilitiesandDiscovery)).\n\nThe reconciliation produced two concrete proposals:\n\n1. **Handshake note:** Add to the handshake documentation a note that the WG is looking to standardize discovery behavior in a future release, based on implementation experience.\n2. **`.well-known` capability:** Define a `\"smart-web-messaging\"` value that servers MAY include in their `.well-known/smart-configuration` file within the `capabilities[]` array.\n\nCarl Anderson (Microsoft) created a [shared design document](https://docs.google.com/document/d/1CUoQbsXv_gcWrqIFF-hme8qrqztRUQqp1yArVNkVWzE/edit?usp=sharing) to collect design considerations for this topic (Feb 2021).\n\nAfter publication of STU1 (May 2022), Lynn Laakso re-opened this ticket to be addressed in a future cycle.\n\n## Related Jira Tickets\n\n| Key | Title | Status | Specification | Relevance |\n|-----|-------|--------|---------------|-----------|\n| [FHIR-47954](https://jira.hl7.org/browse/FHIR-47954) | In what way can a Client discover support of the framework | Applied | FHIR Application Feature Framework IG | Same discovery pattern \u2014 client determining what capabilities a server supports without downloading entire CapabilityStatement |\n| [FHIR-31463](https://jira.hl7.org/browse/FHIR-31463) | Discovery? | Resolved \u2013 No Change | FHIR R5 Subscriptions Backport | Parallel question: how a client discovers supported Payload Types and Channel Types |\n| [FHIR-3361](https://jira.hl7.org/browse/FHIR-3361) | Message endpoints should be associated with the event protocol | Published | FHIR Core | Related to associating endpoints with event protocols in messaging |\n\n## Related Zulip Conversations\n\n### [smart > SMART Web Messaging & SD

... *(truncated, 8426 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-29357.md with 8247 characters
```

</details>


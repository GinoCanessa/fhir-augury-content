# Session Log: FHIR-44648

**Phase:** prepared
**Work Group:** FhirInfrastructure
**Source File:** `prepared/FhirInfrastructure/FHIR-44648.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `52256f69-5fb6-416b-be46-75c24182f098` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-44648` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-10 13:26:59 UTC |
| **Duration** | 74s |
| **Total Tool Calls** | 7 |
| **Total Tokens** | 181,523 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-44648
## Work Group: FHIR Infrastructure
## Output File: C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-44648.md

## Data Access
Use FhirAugury MCP tools (preferred) or CLI fallback at: C:\ai\git\fhir-augury\src\FhirAugury.Cli\bin\Release\net10.0\FhirAugury.Cli.exe

## Steps
1. Gather in parallel: FhirAugury-get_item(source="jira", id="FHIR-44648", includeComments=true, includeContent=true, includeSnapshot=true) AND FhirAugury-cross_referenced(value="FHIR-44648", limit=50)
2. Fetch Related Jira Tickets for each Jira cross-reference.
3. Fetch Zulip threads for each Zulip cross-reference + FhirAugury-content_search(values="FHIR-44648", sources="zulip", limit=10)
4. Note GitHub Items
5. Build Report: Title/metadata, Summary, Details (description + comments), Keywords, Related Zulip Discussions, Related GitHub Items, three Proposed Dispositions (A: Accept, B: Alternative, C: Decline), and Recommendation.

## Rules: Use ONLY data from MCP/CLI. Be specific in dispositions. Recommendation must pick one.
## Save to the output file path above.
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
  "id": "FHIR-44648",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-44648: authorize-post capability conflicts with current browser cross-origin policies

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** FHIR Infrastructure
- **specification:** SMART on FHIR (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Dan Cinnamon
- **Created:** 2024-02-01T22:49:25+00:00
- **Updated:** 2024-04-24T12:50:40+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-44648

## Content
<p>Since the SMART launch v2 was originally launched, significant cross origin policy changes have been introduced by browser vendors.  There are various reasons for introducing these new policy changes, but they're mostly in the spirit of protecting users against attacks such as cross site request forgery attacks, in addition to reducing the prevalence of marketing tracker cookies.</p>

<p>The current behavior of the authorize-post capability is such that a SMART client application will perform a cross-origin form post to the authorization server. Depending upon the security flags on the authorization server cookies- this behavior would cause browsers to not send critical cookies that the authorization server may rely on such as SSO session cookies, "remember me" cookies, "known device" tracking cookies, and maybe others that help drive a consistent user experience. Without these cookies being sent- those commonly implemented authorization server features will no longer function when authorize-post is used.</p>

<p>The impacts of this will be felt most by the practitioner community, where an expectation of SSO may exist between multiple applications.</p>

<p>Regardless of the end user experience, it is in general no longer best practice to perform these cross-origin form posts, and therefore the OpenID working group has instead recommended the use of the new RFC-9126 (pushed authorization requests) to solve the challenges that authorize-post was meant to solve.  More detail on that will be provided in another issue.</p>

<p>This issue is a proposal to deprecate the authorize-post capability in it's current form.  A separate issue will be filed to propose adoption of RFC-9126 to serve the long term needs of the SMART/FHIR community.  Thank you for your consideration.</p>

<p> </p>

## Snapshot
# FHIR-44648: authorize-post capability conflicts with current browser cross-origin policies

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Dan Cinnamon  
**Work Group:** FHIR Infrastructure  
**Specification:** SMART on FHIR (FHIR)  
**Created:** 2024-02-01  
**Updated:** 2024-04-24  

## Description

<p>Since the SMART launch v2 was originally launched, significant cross origin policy changes have been introduced by browser vendors.  There are various reasons for introducing these new policy changes, but they're mostly in the spirit of protecting users against attacks such as cross site request forgery attacks, in addition to reducing the prevalence of marketing tracker cookies.</p>

<p>The current behavior of the authorize-post capability is such that a SMART client application will perform a cross-origin form post to the authorization server. Depending upon the security flags on the authorization server cookies- this behavior would cause browsers to not send critical cookies that the authorization server may rely on such as SSO session cookies, "remember me" cookies, "known device" tracking cookies, and maybe others that help drive a consistent user experience. Without these cookies being sent- those commonly implemented authorization server features will no longer function when authorize-post is used.</p>

<p>The impacts of this will be felt most by the practitioner community, where an expectation of SSO may exist between multiple applications.</p>

<p>Regardless of the end user experience, it is in general no longer best practice to

... *(truncated, 4557 chars total)*
```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-44648" (2 results)

- [zulip] 420847632 → [jira] FHIR-44648
  **Source:** [smart] Deprecating authorize-post?
  **Type:** mentions
  **Context:** http://jira.hl7.org/browse/FHIR-44648 <p><a href="http://jira.hl7.org/browse/FHI...
  **Score:** 0.10
  **Updated:** 2024-02-11T01:23:25+00:00
- [zulip] 419504457 → [jira] FHIR-44648
  **Source:** [smart] Deprecating authorize-post?
  **Type:** mentions
  **Context:** ...se. Otherwise, let's consider our options. <p>I'd like to talk through <a href="http://jira.hl7.org/browse/FHIR-44648">FHIR-44648</a> which <span class="user-me...
  **Score:** 0.00
  **Updated:** 2024-02-02T17:43:17+00:00
**Warnings:**
- Value 'FHIR-44648' is not a valid Zulip message ID

```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# smart > Deprecating authorize-post?

**Messages:** 31
**First message:** 2024-02-02 17:43:17+00:00
**Last message:** 2024-02-26 17:34:02+00:00
**Participants:** Josh Mandel, Cooper Thompson, John Moehrke, Alexander Zautke, Dan Cinnamon, Mikael Rinnetmäki, Sujeito de Sorte, Jens Villadsen, Tom Jones

## Messages

### Josh Mandel — 2024-02-02 17:43:17+00:00
I'd like to talk through FHIR-44648 which @Dan Cinnamon raised based on experience at Okta. Is anyone using POST-based authorization as a client? Has anyone encountered a scenario where GET-based authz was failing because "authz URL was too long"? If the answer to both are "No", I'd suggest we either deprecate or (loudly) mark as "planned for deprecation" the authorize-post functionality in the upcoming 2.2 release. Otherwise, let's consider our options.

### Cooper Thompson — 2024-02-02 17:45:10+00:00
We do support POST-based auth, and have documented it and suggested it in some cases. But I don't think we have easy access to reporting on whether it has actually been used.

### Cooper Thompson — 2024-02-02 17:46:14+00:00
We have run into URL length issues on GET for sure. Not in the browser that I'm aware, but in API gateways that are handling the request between the browser and our servers.

### Josh Mandel — 2024-02-02 17:51:38+00:00
Thanks @Cooper Thompson , that's important to know! Would love to hear from others.

### Josh Mandel — 2024-02-02 17:52:43+00:00
It'd also be important to know if authorize-post is being successfully used -- in particular, if Epic's authz server is receiving whatever session cookies it needs in order to offer a seamless flow (no double sign-in) with current-generation browsers?

### John Moehrke — 2024-02-02 18:04:38+00:00
to be clear. this question is only about the authorize-post, not generally use of http post. rigth?

### Josh Mandel — 2024-02-02 18:07:29+00:00
Correct. The question here is about submitting an authorization request to the authorize endpoint using HTTP post. This requires basically asking the browser to do a form submission and browser vendors have been locking down behaviors around which cookies are included in that submission. (The conventional flow here involves doing a browser redirect, rather than a form submission, which does a GET and includes whatever cookies are associated with the target origin.)

### Alexander Zautke — 2024-02-02 18:21:06+00:00
We support it, but only due to regulatory demand. I think we haven’t seen any issues with GET-based requests so far.

### Dan Cinnamon — 2024-02-02 18:55:06+00:00
Just a bit of color since I'm on... just wanted to note that the JIRA doesn't challenge the need for dealing with long URLs and big requests. It's just that the exact mechanism needs to evolve along with browser behavior, and another JIRA proposes another (also OIDC standard) why of dealing with it that also enables some additional security benefits.

### Josh Mandel — 2024-02-02 18:57:25+00:00
Indeed! Right now I am focused on what we should try to do during the current ballot reconciliation to give the community a heads up. We don't want to deprecate functionality before including a replacement if it is filling a critical need .

### Mikael Rinnetmäki — 2024-02-03 13:56:06+00:00
We've run into issues with long urls on GET based authz. Not with browsers, though. We've been able to resolve the issues with changes to server and load balancer configurations. About the same as @Cooper Thompson , I believe.

### Mikael Rinnetmäki — 2024-02-03 13:56:12+00:00
We haven't moved to POST.

### Sujeito de Sorte — 2024-02-04 11:41:37+00:00
Hi @Josh Mandel , GET has a limit of 2048 characters. Therefore, the size authentication code or an absurdly long URL before the query string can have an impact. But discussions about GET vs POST in a thread with @John Moehrke don't bring back good memories. I'll stop here. Lol.. Tks. See you!

### Jens Villadsen — 2024-02-04 12:38:37+00:00

... *(truncated, 14505 chars total)*
```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (2 total, showing 2)

### [zulip] 420847632 — [smart] Deprecating authorize-post?
- **Score:** 0.10
- **Updated:** 2024-02-11T01:23:25+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/smart/topic/Deprecating%20authorize-post%3F/near/420847632
- **Snippet:** http://jira.hl7.org/browse/<b>FHIR-44648</b>

### [zulip] 419504457 — [smart] Deprecating authorize-post?
- **Score:** 0.00
- **Updated:** 2024-02-02T17:43:17+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/smart/topic/Deprecating%20authorize-post%3F/near/419504457
- **Snippet:** I'd like to talk through <b>FHIR-44648</b> which @Dan Cinnamon raised based on experience at Okta. Is anyone using...


```

</details>

<details>
<summary>`FhirAugury-get_keywords`</summary>

**Result:**
```
## Keywords for jira:FHIR-44648
Content type: issue

| Keyword | Type | Count | BM25 Score |
|---------|------|------:|------------|
| cookie/cooky | word | 7 | 14.967 |
| 9126 | word | 2 | 9.056 |
| origin | word | 5 | 8.724 |
| browser | word | 4 | 8.265 |
| cross | word | 6 | 7.709 |
| sso | word | 2 | 7.568 |
| authorize | word | 6 | 7.548 |
| attack | word | 2 | 6.582 |
| post | word | 8 | 6.415 |
| authorization | word | 5 | 5.688 |
| policy | word | 4 | 5.618 |
| forgery | word | 1 | 5.606 |
| rfc | word | 2 | 5.341 |
| solve | word | 2 | 5.111 |
| capability | word | 4 | 5.037 |
| smart | word | 3 | 4.957 |
| form | word | 3 | 4.617 |
| conflict | word | 2 | 4.595 |
| prevalence | word | 1 | 4.530 |
| experience | word | 2 | 4.405 |
| launch | word | 2 | 4.403 |
| server | word | 4 | 4.197 |
| marketing | word | 1 | 4.174 |
| spirit | word | 1 | 4.110 |
| behavior | word | 2 | 4.019 |
| introduce | word | 2 | 3.997 |
| openid | word | 1 | 3.937 |
| current | word | 4 | 3.786 |
| community | word | 2 | 3.777 |
| felt | word | 1 | 3.726 |
| long | word | 2 | 3.679 |
| application | word | 2 | 3.618 |
| perform | word | 2 | 3.608 |
| protect | word | 1 | 3.594 |
| remember | word | 1 | 3.589 |
| drive | word | 1 | 3.347 |
| push | word | 1 | 3.065 |
| originally | word | 1 | 3.054 |
| commonly | word | 1 | 3.029 |
| adoption | word | 1 | 3.027 |
| rely | word | 1 | 3.000 |
| session | word | 1 | 2.982 |
| serve | word | 1 | 2.959 |
| critical | word | 1 | 2.930 |
| challenge | word | 1 | 2.910 |
| user | word | 3 | 2.891 |
| vendor | word | 1 | 2.819 |
| feature | word | 1 | 2.794 |
| significant | word | 1 | 2.761 |
| reduce | word | 1 | 2.721 |

```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-44648.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\FhirInfrastructure\\FHIR-44648.md",
  "file_text": "# FHIR-44648: authorize-post capability conflicts with current browser cross-origin policies\n\n## Metadata\n\n| Field | Value |\n|-------|-------|\n| **Ticket** | [FHIR-44648](https://jira.hl7.org/browse/FHIR-44648) |\n| **Status** | Triaged |\n| **Type** | Change Request |\n| **Priority** | Medium |\n| **Resolution** | Unresolved |\n| **Work Group** | FHIR Infrastructure |\n| **Specification** | SMART on FHIR (FHIR) |\n| **Reporter** | Dan Cinnamon |\n| **Assignee** | Unassigned |\n| **Created** | 2024-02-01 |\n| **Updated** | 2024-04-24 |\n\n## Summary\n\nThis ticket proposes deprecating the SMART `authorize-post` capability due to evolving browser cross-origin cookie policies. The `authorize-post` mechanism performs a cross-origin form POST to the authorization server, which causes modern browsers to withhold critical cookies (SSO session, \"remember me\", device tracking) unless the authorization server has set its cookies to `SameSite=None`. The reporter (Dan Cinnamon, Okta) noted that the OpenID working group recommends RFC-9126 (Pushed Authorization Requests / PAR) as a successor to solve the same problems with additional security benefits.\n\nHowever, subsequent investigation on Zulip by both the reporter and Josh Mandel revealed that the urgency is lower than initially believed: the `authorize-post` flow involves a top-level browser navigation and is therefore **not** classified as a \"third-party request\" by current browser deprecation efforts. The main concern is that authorization servers must use the least secure cookie setting (`SameSite=None`), but current-generation browsers still support this. Both Dan Cinnamon and Josh Mandel agreed that deprecation need not be rushed and could be handled as part of a broader discussion about aligning SMART launch with current identity standards (including PAR and DPoP).\n\n## Details\n\n### Description\n\nSince SMART launch v2 was originally published, browser vendors have introduced significant cross-origin policy changes to combat cross-site request forgery and reduce marketing tracker cookies. The `authorize-post` capability causes a SMART client to perform a cross-origin form POST to the authorization server. Depending on cookie security flags, browsers will not send critical cookies (SSO session cookies, \"remember me\" cookies, device tracking cookies), breaking commonly implemented authorization server features.\n\nThe impact is most significant for the practitioner community where SSO expectations exist across multiple applications. Cross-origin form POSTs are no longer considered best practice; the OpenID working group recommends RFC-9126 (Pushed Authorization Requests) as the replacement. A companion ticket was planned to propose PAR adoption for the SMART/FHIR community.\n\n### Comments\n\nNo comments were attached to this Jira ticket. The substantive discussion took place o

... *(truncated, 8330 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\FhirInfrastructure\FHIR-44648.md with 8170 characters
```

</details>


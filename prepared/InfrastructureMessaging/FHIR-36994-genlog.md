# Session Log: FHIR-36994

**Phase:** prepared
**Work Group:** InfrastructureMessaging
**Source File:** `prepared/InfrastructureMessaging/FHIR-36994.md`

---

## Session Information

| Field | Value |
|-------|-------|
| **Session ID** | `f87a5def-b7e0-4b3b-ae40-d0467cd19b74` |
| **Session Summary** | Continue Preparing Tickets |
| **Agent ID** | `prep-FHIR-36994` |
| **Agent Type** | general-purpose |
| **Model** | claude-opus-4.6-1m |
| **Task Started** | 2026-04-09 19:31:16 UTC |
| **Duration** | 107s |
| **Total Tool Calls** | 15 |
| **Total Tokens** | 262,223 |

---

## Task Prompt

````markdown
You are preparing a FHIR Jira ticket for workgroup review.

## Ticket: FHIR-36994
## Work Group: Infrastructure & Messaging
## Output File: C:\ai\git\fhir-augury-content\prepared\InfrastructureMessaging\FHIR-36994.md

## Data Access
Use FhirAugury MCP tools (preferred) or fhir-augury CLI (fallback).

## Step 1: Gather Ticket and Cross-References (run in parallel)
- FhirAugury-get_item(source="jira", id="FHIR-36994", includeComments=true, includeContent=true, includeSnapshot=true)
- FhirAugury-cross_referenced(value="FHIR-36994", limit=50)

## Step 2-4: Fetch related Jira tickets, Zulip conversations (also search: FhirAugury-content_search(values="FHIR-36994", sources="zulip", limit=10)), and note GitHub items.

## Step 5: Build the Report using the standard ticket review structure.

## Rules - Use ONLY data from MCP/CLI. Do not fabricate. Be specific in dispositions. The recommendation must pick one.

## Final Step
Save to: C:\ai\git\fhir-augury-content\prepared\InfrastructureMessaging\FHIR-36994.md
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
  "id": "FHIR-36994",
  "includeComments": true,
  "includeContent": true,
  "includeSnapshot": true
}
```

**Result:**
```
# [jira] FHIR-36994: Hubs should not report event conformance

- **status:** Triaged
- **type:** Change Request
- **priority:** Medium
- **work_group:** Infrastructure & Messaging
- **specification:** FHIRCast (FHIR)
- **resolution:** Unresolved
- **assignee:** Unassigned
- **reporter:** Evan Schnell
- **Created:** 2022-04-29T21:01:33+00:00
- **Updated:** 2023-12-27T14:43:49+00:00
- **URL:** https://jira.hl7.org/browse/FHIR-36994

## Content
<p>Currently, the <a href="http://hl7.org/fhir/uv/fhircast/2022May/2-7-Conformance.html#wellknown-endpoint" class="external-link" target="_blank" rel="nofollow noopener">Hub conformance statement</a> specifies which events are supported. However, that is not so nice for a Hub, if event customization is a feature. So can’t we have an Hub just pass on custom events regardless from if the EMR that hosts the Hub listens to those events?</p>

<p>Consider integration between an ImageViewer and Dictation system with EMR/RIS as hub.  The EMR/RIS should propagate any events it does not recognize, right?  </p>

## Snapshot
# FHIR-36994: Hubs should not report event conformance

**Status:** Triaged  
**Type:** Change Request  
**Priority:** Medium  
**Resolution:** Unresolved  
**Assignee:** Unassigned  
**Reporter:** Evan Schnell  
**Work Group:** Infrastructure & Messaging  
**Specification:** FHIRCast (FHIR)  
**Created:** 2022-04-29  
**Updated:** 2023-12-27  

## Description

<p>Currently, the <a href="http://hl7.org/fhir/uv/fhircast/2022May/2-7-Conformance.html#wellknown-endpoint" class="external-link" target="_blank" rel="nofollow noopener">Hub conformance statement</a> specifies which events are supported. However, that is not so nice for a Hub, if event customization is a feature. So can’t we have an Hub just pass on custom events regardless from if the EMR that hosts the Hub listens to those events?</p>

<p>Consider integration between an ImageViewer and Dictation system with EMR/RIS as hub.  The EMR/RIS should propagate any events it does not recognize, right?  </p>



```

</details>

<details>
<summary>`FhirAugury-cross_referenced`</summary>

**Result:**
```
## Cross-References for "FHIR-36994" (1 results)

- [zulip] 284941341 → [jira] FHIR-36994
  **Source:** [FHIRcast] Hubs and Apps
  **Type:** mentions
  **Context:** ... apps assuming that the hub will be "their hub" and the problems highlighted by https://jira.hl7.org/browse/FHIR-36994 . Unfortunately, I won't be able to atten...
  **Score:** 0.03
  **Updated:** 2022-06-03T22:49:27+00:00
**Warnings:**
- Value 'FHIR-36994' is not a valid Zulip message ID

```

</details>

<details>
<summary>`FhirAugury-content_search`</summary>

**Result:**
```
## Search Results (1 total, showing 1)

### [zulip] 284941341 — [FHIRcast] Hubs and Apps
- **Score:** 0.03
- **Updated:** 2022-06-03T22:49:27+00:00
- **URL:** https://chat.fhir.org/#narrow/stream/FHIRcast/topic/Hubs%20and%20Apps/near/284941341
- **Snippet:** ...the problems highlighted by https://jira.hl7.org/browse/<b>FHIR-36994</b> . Unfortunately, I won't be able to attend due...


```

</details>

### Turn 2

<details>
<summary>`FhirAugury-get_zulip_thread`</summary>

**Result:**
```
# FHIRcast > Agnostic hub

**Messages:** 25
**First message:** 2022-11-17 08:18:03+00:00
**Last message:** 2023-01-18 17:06:43+00:00
**Participants:** Paulius Galinauskas, Bas van den Heuvel, Aris van Dijk, Elliot Silver, Eric Martin, Isaac Vetter, kamal gnanadesikan, Catie Ladd

## Messages

### Paulius Galinauskas — 2022-11-17 08:18:03+00:00
Hey everyone, A related question to topic https://chat.fhir.org/#narrow/stream/179271-FHIRcast/topic/Hubs.20and.20Apps The standard does not explicitly spell this out and I was not able to find an answer neither in Zulip, nor in Jira. Is a hub agnostic towards the events it passes or does it need to know the events before passing them around? I.e. do all events must be registered with a hub before using them?

### Bas van den Heuvel — 2022-11-17 08:52:30+00:00
The Hub is not agnostic to the events that are being passed, some events (context change and content exchange) place specific requirements on the hub. The events it supported is published on its conformance endpoint ( https://build.fhir.org/ig/HL7/fhircast-docs/2-7-Conformance.html#conformance ). The Hub is only required to forward these events.

### Aris van Dijk — 2022-11-23 10:10:09+00:00
Bas van den Heuvel said : The Hub is not agnostic to the events that are being passed, some events (context change and content exchange) place specific requirements on the hub. The events it supported is published on its conformance endpoint ( https://build.fhir.org/ig/HL7/fhircast-docs/2-7-Conformance.html#conformance ). The Hub is only required to forward these events. Can't we make content sharing an a specific additional claim in the conformance statement, instead of having to list all supported events? The concept of a hub is that it should be used by many applications, so wouldn't it be more beneficial if the hub would simply handle all custom events in the default way?

### Bas van den Heuvel — 2022-11-23 12:34:03+00:00
I'm not sure I understand what you are suggesting. Do you object against the long list of events or the fact that the hub can decide what events it supports?

### Aris van Dijk — 2022-11-23 14:20:11+00:00
Indeed the hub cannot decide upfront which events are supported. The hub is there not for one known application but for multiple unknown applications that have to talk to each other. I think there are good use cases for some custom events in the applications we are developing that are not part of any FHIRcast standard yet. That would imply that we have to build our own hub that supports those events, and then connect to other third party hubs for integration that do not support those events. This then becomes no longer a hub-and-spokes model, but point-to-point integrations between multiple hubs. The worst of both worlds...

### Paulius Galinauskas — 2022-12-01 15:05:38+00:00
I do agree with @Aris van Dijk , if the hubs are not message agnostic, it makes the standard difficult to adopt, since there are only handful of events that cover very few scenarios. @Bas van den Heuvel , could you elaborate on the decision why the hubs must be message-aware? Are there discussions about this topic?

### Bas van den Heuvel — 2022-12-01 15:21:21+00:00
Several reasons came up. The ones that I remember include :1 some of the first hour implementers want to control what events are supported, 2 the security model is event specific, 3 most events require specific behaviour of the hub.

### Bas van den Heuvel — 2022-12-01 15:25:33+00:00
The topic you are raising is an interesting one and is probably something to discuss further in a FHiRcast telco or during the Jan WGM. Please file a Jira ticket on this topic and link it to this Zulip thread.

### Paulius Galinauskas — 2022-12-02 08:50:38+00:00
1 some of the first hour implementers want to control what events are supported That's not really a strong argument. the security model is event specific I'm not really aware about it. Could you point me to the corre

... *(truncated, 12721 chars total)*
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
<summary>`FhirAugury-refers_to`</summary>

**Result:**
```
No refers-to references found for "FHIR-36994".
```

</details>

### Turn 3

<details>
<summary>`create` — create a new file at C:\ai\git\fhir-augury-content\prepared\InfrastructureMessaging\FHIR-36994.md.</summary>

**Arguments:**
```json
{
  "path": "C:\\ai\\git\\fhir-augury-content\\prepared\\InfrastructureMessaging\\FHIR-36994.md",
  "file_text": "# FHIR-36994: Hubs should not report event conformance\n\n## Summary\n\n| Field          | Value                                |\n|----------------|--------------------------------------|\n| **Ticket**     | [FHIR-36994](https://jira.hl7.org/browse/FHIR-36994) |\n| **Status**     | Triaged                              |\n| **Type**       | Change Request                       |\n| **Priority**   | Medium                               |\n| **Resolution** | Unresolved                           |\n| **Work Group** | Infrastructure & Messaging           |\n| **Specification** | FHIRCast (FHIR)                   |\n| **Reporter**   | Evan Schnell                         |\n| **Assignee**   | Unassigned                           |\n| **Created**    | 2022-04-29                           |\n| **Updated**    | 2023-12-27                           |\n\n## Description\n\nThe submitter argues that the FHIRCast [Hub conformance statement](http://hl7.org/fhir/uv/fhircast/2022May/2-7-Conformance.html#wellknown-endpoint) \u2014 which specifies which events a Hub supports \u2014 is problematic when event customization is a feature. If a Hub (e.g., an EMR/RIS) only reports support for its own known events, it blocks third-party applications (e.g., ImageViewers, Dictation systems) from exchanging custom events through that Hub.\n\nThe core question: **Should a Hub propagate events it does not itself recognize?** The submitter contends that an EMR/RIS acting as a Hub should pass through any events between subscribers, even if the EMR itself does not listen to or understand those events.\n\n## Keywords\n\n`FHIRCast`, `Hub`, `conformance`, `custom events`, `event propagation`, `pass-through`, `agnostic hub`, `well-known endpoint`, `eventsSupported`, `integration`\n\n## Related Jira Tickets\n\n| Ticket | Title | Status | Resolution | Relevance |\n|--------|-------|--------|------------|-----------|\n| [FHIR-39545](https://jira.hl7.org/browse/FHIR-39545) | Hubs should be agnostic towards events they pass | Deferred | Considered for Future Use | **Directly related** \u2014 filed as a follow-up to this same concern. Argues that hubs requiring pre-registration of events makes adoption difficult when custom events are needed for tight integrations. |\n| [FHIR-37325](https://jira.hl7.org/browse/FHIR-37325) | Clear guidance around usage and maintenance of custom Libraries | Applied | Persuasive with Modification | Requests ability for implementations to define additional events beyond the FHIRCast Event Library; addresses the same custom event extensibility gap. |\n| [FHIR-37223](https://jira.hl7.org/browse/FHIR-37223) | Under-represented implications to the spec | Applied | Persuasive with Modification | Raises concerns about the broad implications of content sharing on hub behavior, including what hubs are required to return \u2014 related to hub responsibilit

... *(truncated, 10479 chars total)*
```

**Result:**
```
Created file C:\ai\git\fhir-augury-content\prepared\InfrastructureMessaging\FHIR-36994.md with 10295 characters
```

</details>


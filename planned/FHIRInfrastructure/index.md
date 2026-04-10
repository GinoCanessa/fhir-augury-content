# FHIR Infrastructure — Planned Tickets

This index lists all **29** planned tickets for the **FHIR Infrastructure** work group, grouped by specification and target artifact (repository).

> **Planned tickets** have approved resolutions with implementation plans. Work through them in the order shown — tickets are sorted so that prerequisites come before dependents.

---

## Table of Contents

- [FHIR Core (FHIR)](#fhir-core-fhir)
- [FHIR Extensions Pack (FHIR)](#fhir-extensions-pack-fhir)
- [FHIR R5 Subscriptions Backport (FHIR)](#fhir-r5-subscriptions-backport-fhir)
- [US DAF Research (FHIR)](#us-daf-research-fhir)
- [US Patient Reported Outcomes (PRO) (FHIR)](#us-patient-reported-outcomes-pro-fhir)
- [Unspecified](#unspecified)

---

## FHIR Core (FHIR)

*17 ticket(s) targeting the **FHIR Core (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-40580 | Typo: HealthcareService is misspelled as HealthCareService | Resolved — change required | 2023-03-10 | [FHIR-40580](./FHIR-40580.md) · [Jira](https://jira.hl7.org/browse/FHIR-40580) |
| FHIR-37471 | Please add instance examples for each approved FHIR extension | Resolved – change required | 2023-03-20 (vote: Grahame Grieve/Josh Mandel 14-0-0) | [FHIR-37471](./FHIR-37471.md) · [Jira](https://jira.hl7.org/browse/FHIR-37471) |
| FHIR-43426 | Explain the use of "?" in Differential Elements on Detailed Description Tab | Resolved – change required | 2024-05-06 | [FHIR-43426](./FHIR-43426.md) · [Jira](https://jira.hl7.org/browse/FHIR-43426) |
| FHIR-47623 | NamingSystem - link to managing organization | Resolved - change required | 2024-09-13 | [FHIR-47623](./FHIR-47623.md) · [Jira](https://jira.hl7.org/browse/FHIR-47623) |
| FHIR-40600 | Typo in Resource Definitions spec | Resolved – change required | 2024-09-16 | [FHIR-40600](./FHIR-40600.md) · [Jira](https://jira.hl7.org/browse/FHIR-40600) |
| FHIR-53722 | Deprecated elements should be withdrawn where applicable in R6 | Resolved — change required | 2026-01-26 | [FHIR-53722](./FHIR-53722.md) · [Jira](https://jira.hl7.org/browse/FHIR-53722) |
| FHIR-55165 | Group.membership has no escape valve | Resolved - change required | 2026-03-16 | [FHIR-55165](./FHIR-55165.md) · [Jira](https://jira.hl7.org/browse/FHIR-55165) |
| FHIR-44496 | Add missing "of" | Resolved — change required | — | [FHIR-44496](./FHIR-44496.md) · [Jira](https://jira.hl7.org/browse/FHIR-44496) |
| FHIR-47199 | List of deprecated resources need update from R5 | Resolved — change required | — | [FHIR-47199](./FHIR-47199.md) · [Jira](https://jira.hl7.org/browse/FHIR-47199) |
| FHIR-53636 | Clarify that Element.id prohibits all whitespace, not just the space character | Resolved – change required | — | [FHIR-53636](./FHIR-53636.md) · [Jira](https://jira.hl7.org/browse/FHIR-53636) |
| FHIR-55156 | CapabilityStatement.rest.interaction.code has no escape valve | Resolved — change required | — | [FHIR-55156](./FHIR-55156.md) · [Jira](https://jira.hl7.org/browse/FHIR-55156) |

### HL7/UTG

*5 ticket(s) affecting [HL7/UTG](https://github.com/HL7/UTG).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-43804 | Typo | Resolved — change required | 2024-01-19 | [FHIR-43804](./FHIR-43804.md) · [Jira](https://jira.hl7.org/browse/FHIR-43804) |
| FHIR-50788 | FHIR build crashes on Questionnaire Example because it uses UCUM unit [lb_i] | Resolved — change required | 2025-05-22 | [FHIR-50788](./FHIR-50788.md) · [Jira](https://jira.hl7.org/browse/FHIR-50788) |
| FHIR-54716 | Typo in questionnaire rule que-10 | Resolved — change required | 2026-02-05 | [FHIR-54716](./FHIR-54716.md) · [Jira](https://jira.hl7.org/browse/FHIR-54716) |
| FHIR-46381 | Clarify CapabilityStatement.rest.resource.searchInclude value for wildcard include | Resolved – change required | — | [FHIR-46381](./FHIR-46381.md) · [Jira](https://jira.hl7.org/browse/FHIR-46381) |
| FHIR-53900 | Contained Resources, Note to Implementers | Resolved — change required | — | [FHIR-53900](./FHIR-53900.md) · [Jira](https://jira.hl7.org/browse/FHIR-53900) |

### HL7/capstmt

*1 ticket(s) affecting [HL7/capstmt](https://github.com/HL7/capstmt).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-46381 | Clarify CapabilityStatement.rest.resource.searchInclude value for wildcard include | Resolved – change required | — | [FHIR-46381](./FHIR-46381.md) · [Jira](https://jira.hl7.org/browse/FHIR-46381) |

### HL7/fhir

*1 ticket(s) affecting [HL7/fhir](https://github.com/HL7/fhir).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-46244 | Extension for R5 elements - errors if extension points to element w/ R5 DataType | Resolved - change required | — | [FHIR-46244](./FHIR-46244.md) · [Jira](https://jira.hl7.org/browse/FHIR-46244) |

### HL7/fhir-extensions

*6 ticket(s) affecting [HL7/fhir-extensions](https://github.com/HL7/fhir-extensions).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-43804 | Typo | Resolved — change required | 2024-01-19 | [FHIR-43804](./FHIR-43804.md) · [Jira](https://jira.hl7.org/browse/FHIR-43804) |
| FHIR-50788 | FHIR build crashes on Questionnaire Example because it uses UCUM unit [lb_i] | Resolved — change required | 2025-05-22 | [FHIR-50788](./FHIR-50788.md) · [Jira](https://jira.hl7.org/browse/FHIR-50788) |
| FHIR-54716 | Typo in questionnaire rule que-10 | Resolved — change required | 2026-02-05 | [FHIR-54716](./FHIR-54716.md) · [Jira](https://jira.hl7.org/browse/FHIR-54716) |
| FHIR-46244 | Extension for R5 elements - errors if extension points to element w/ R5 DataType | Resolved - change required | — | [FHIR-46244](./FHIR-46244.md) · [Jira](https://jira.hl7.org/browse/FHIR-46244) |
| FHIR-46381 | Clarify CapabilityStatement.rest.resource.searchInclude value for wildcard include | Resolved – change required | — | [FHIR-46381](./FHIR-46381.md) · [Jira](https://jira.hl7.org/browse/FHIR-46381) |
| FHIR-53900 | Contained Resources, Note to Implementers | Resolved — change required | — | [FHIR-53900](./FHIR-53900.md) · [Jira](https://jira.hl7.org/browse/FHIR-53900) |

---

## FHIR Extensions Pack (FHIR)

*3 ticket(s) targeting the **FHIR Extensions Pack (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-50952 | The FMM extension contexts should be Element not Resource | Resolved – change required | 2025-08-18 | [FHIR-50952](./FHIR-50952.md) · [Jira](https://jira.hl7.org/browse/FHIR-50952) |
| FHIR-50852 | Define an extension to bind an element to a concept domain | Resolved — change required | — | [FHIR-50852](./FHIR-50852.md) · [Jira](https://jira.hl7.org/browse/FHIR-50852) |

### HL7/fhir-extensions

*1 ticket(s) affecting [HL7/fhir-extensions](https://github.com/HL7/fhir-extensions).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-44327 | Correct table of content numbering | Resolved — change required | 2024-01-22 | [FHIR-44327](./FHIR-44327.md) · [Jira](https://jira.hl7.org/browse/FHIR-44327) |

---

## FHIR R5 Subscriptions Backport (FHIR)

*5 ticket(s) targeting the **FHIR R5 Subscriptions Backport (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-43081 | Add authorization information to notifications | Resolved — change required | 2023-11-08 | [FHIR-43081](./FHIR-43081.md) · [Jira](https://jira.hl7.org/browse/FHIR-43081) |
| FHIR-43610 | Make the related query examples consistent | Resolved – change required | — | [FHIR-43610](./FHIR-43610.md) · [Jira](https://jira.hl7.org/browse/FHIR-43610) |
| FHIR-43730 | Bundle type history vs collection | Resolved — change required | — | [FHIR-43730](./FHIR-43730.md) · [Jira](https://jira.hl7.org/browse/FHIR-43730) |

### HL7/fhir-subscription-backport-ig

*2 ticket(s) affecting [HL7/fhir-subscription-backport-ig](https://github.com/HL7/fhir-subscription-backport-ig).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-44108 | Update examples/links for R4B backport-related-query | Resolved — change required | 2024-01-22 | [FHIR-44108](./FHIR-44108.md) · [Jira](https://jira.hl7.org/browse/FHIR-44108) |
| FHIR-45365 | Extensions should have cardinality set correctly | Resolved — change required | 2024-04-26 | [FHIR-45365](./FHIR-45365.md) · [Jira](https://jira.hl7.org/browse/FHIR-45365) |

---

## US DAF Research (FHIR)

*1 ticket(s) targeting the **US DAF Research (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-12532 | DAF Query Responder typos & links | Resolved - change required | 2018-07-08 | [FHIR-12532](./FHIR-12532.md) · [Jira](https://jira.hl7.org/browse/FHIR-12532) |

---

## US Patient Reported Outcomes (PRO) (FHIR)

*2 ticket(s) targeting the **US Patient Reported Outcomes (PRO) (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-22089 | Additional search parameters for SDC Questionnaire | Resolved – change required | 2019-09-17 | [FHIR-22089](./FHIR-22089.md) · [Jira](https://jira.hl7.org/browse/FHIR-22089) |

### HL7/patient-reported-outcomes

*1 ticket(s) affecting [HL7/patient-reported-outcomes](https://github.com/HL7/patient-reported-outcomes).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-22084 | Add additional requirements for SMART on FHIR — PRO #44 | Resolved — change required | 2019-09-17 | [FHIR-22084](./FHIR-22084.md) · [Jira](https://jira.hl7.org/browse/FHIR-22084) |

---

## Unspecified

*1 ticket(s) targeting the **Unspecified** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-55162 | Spelling/abbreviation issues on page: examplescenario | Resolved – change required | — | [FHIR-55162](./FHIR-55162.md) · [Jira](https://jira.hl7.org/browse/FHIR-55162) |

---

*Generated automatically. Re-run `generate-indexes.py` to update.*

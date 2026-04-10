# Imaging Integration — Prepared Tickets

This index lists all **29** prepared tickets for the **Imaging Integration** work group, grouped by specification.

> **Prepared tickets** have been reviewed and have proposed dispositions ready for work-group consideration. They are sorted by date within each group so the oldest outstanding items are addressed first.

---

## Table of Contents

- [DICOM SR to FHIR Resource Mapping IG (FHIR)](#dicom-sr-to-fhir-resource-mapping-ig-fhir)
- [FHIR Core (FHIR)](#fhir-core-fhir)
- [FHIRCast (FHIR)](#fhircast-fhir)
- [Radiation Dose Summary for Diagnostic Procedures on FHIR (FHIR)](#radiation-dose-summary-for-diagnostic-procedures-on-fhir-fhir)
- [Unspecified](#unspecified)

---

## DICOM SR to FHIR Resource Mapping IG (FHIR)

*25 ticket(s) targeting the **DICOM SR to FHIR Resource Mapping IG (FHIR)** specification.*

#### Related Group: FHIR-47223

> FHIR-47223 and FHIR-47367, FHIR-47368, FHIR-47370, FHIR-47372, FHIR-47377, FHIR-47382, FHIR-47383, FHIR-47384, FHIR-47386, FHIR-47392, FHIR-47460, FHIR-47485, FHIR-47487, FHIR-47489, FHIR-47506, FHIR-47510, FHIR-47513, FHIR-47515, FHIR-47525, FHIR-47641, FHIR-47655 are related and should be worked together. They reference each other in their prerequisites or related-tickets sections — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-47223 | The Example section looks like a mix of normative content and examples | Triaged | 2024-09-09 | [FHIR-47223](./FHIR-47223.md) · [Jira](https://jira.hl7.org/browse/FHIR-47223) |
| FHIR-47367 | Why Derived Imaging Measurement is excluded in mapping to an Algorithm Identification Device | Triaged | 2024-09-11 | [FHIR-47367](./FHIR-47367.md) · [Jira](https://jira.hl7.org/browse/FHIR-47367) |
| FHIR-47368 | Unclear sentence | Triaged | 2024-09-11 | [FHIR-47368](./FHIR-47368.md) · [Jira](https://jira.hl7.org/browse/FHIR-47368) |
| FHIR-47370 | Wrong (non-existing) profiles depicted in the diagram | Triaged | 2024-09-11 | [FHIR-47370](./FHIR-47370.md) · [Jira](https://jira.hl7.org/browse/FHIR-47370) |
| FHIR-47372 | Specify parent device profile in the AlgorithmIdentificationMapping profile | Triaged | 2024-09-11 | [FHIR-47372](./FHIR-47372.md) · [Jira](https://jira.hl7.org/browse/FHIR-47372) |
| FHIR-47377 | Misalignment in the diagrams representing Imaging Measurements Container | Triaged | 2024-09-11 | [FHIR-47377](./FHIR-47377.md) · [Jira](https://jira.hl7.org/browse/FHIR-47377) |
| FHIR-47382 | Why only use preliminary flag and not completion flag and verification flag? | Triaged | 2024-09-11 | [FHIR-47382](./FHIR-47382.md) · [Jira](https://jira.hl7.org/browse/FHIR-47382) |
| FHIR-47383 | There is no mapping section for Device Algorithm Identification | Triaged | 2024-09-11 | [FHIR-47383](./FHIR-47383.md) · [Jira](https://jira.hl7.org/browse/FHIR-47383) |
| FHIR-47384 | Not aligned graphical representations of Imaging Measurements Container | Triaged | 2024-09-11 | [FHIR-47384](./FHIR-47384.md) · [Jira](https://jira.hl7.org/browse/FHIR-47384) |
| FHIR-47386 | Not clear how to map the two elements that end up in BodyStructure resources | Triaged | 2024-09-11 | [FHIR-47386](./FHIR-47386.md) · [Jira](https://jira.hl7.org/browse/FHIR-47386) |
| FHIR-47392 | What is parent BodyStructureFindingSite? | Triaged | 2024-09-11 | [FHIR-47392](./FHIR-47392.md) · [Jira](https://jira.hl7.org/browse/FHIR-47392) |
| FHIR-47460 | Using code and value with hasMember in Measurements Group goes against modeling pattern from FHIR | Triaged | 2024-09-12 | [FHIR-47460](./FHIR-47460.md) · [Jira](https://jira.hl7.org/browse/FHIR-47460) |
| FHIR-47485 | Not possible to write text evaluations within the Qualitative Evaluation | Triaged | 2024-09-12 | [FHIR-47485](./FHIR-47485.md) · [Jira](https://jira.hl7.org/browse/FHIR-47485) |
| FHIR-47487 | Not clear what is represented with every column in the examples subsections | Triaged | 2024-09-12 | [FHIR-47487](./FHIR-47487.md) · [Jira](https://jira.hl7.org/browse/FHIR-47487) |
| FHIR-47489 | Suggest adding "resource" after the name of the resource in each subsection | Triaged | 2024-09-12 | [FHIR-47489](./FHIR-47489.md) · [Jira](https://jira.hl7.org/browse/FHIR-47489) |
| FHIR-47506 | Practitioner resource instead of Device resource is created | Triaged | 2024-09-12 | [FHIR-47506](./FHIR-47506.md) · [Jira](https://jira.hl7.org/browse/FHIR-47506) |
| FHIR-47510 | Suggestion to rename the section, to align with the rest of the examples | Triaged | 2024-09-12 | [FHIR-47510](./FHIR-47510.md) · [Jira](https://jira.hl7.org/browse/FHIR-47510) |
| FHIR-47513 | Observation instead of Device resource is created | Triaged | 2024-09-12 | [FHIR-47513](./FHIR-47513.md) · [Jira](https://jira.hl7.org/browse/FHIR-47513) |
| FHIR-47515 | Seems like there is a mistake in the example | Triaged | 2024-09-12 | [FHIR-47515](./FHIR-47515.md) · [Jira](https://jira.hl7.org/browse/FHIR-47515) |
| FHIR-47525 | Suggestion to include both DICOM and FHIR representations | Triaged | 2024-09-12 | [FHIR-47525](./FHIR-47525.md) · [Jira](https://jira.hl7.org/browse/FHIR-47525) |
| FHIR-47641 | Profiles description is missing | Triaged | 2024-09-13 | [FHIR-47641](./FHIR-47641.md) · [Jira](https://jira.hl7.org/browse/FHIR-47641) |
| FHIR-47655 | Suggestion to align and link section 4 with the Mappings defined for every profile | Triaged | 2024-09-13 | [FHIR-47655](./FHIR-47655.md) · [Jira](https://jira.hl7.org/browse/FHIR-47655) |

#### Other Tickets

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-47347 | Missing container in the table | Triaged | 2024-09-11 | [FHIR-47347](./FHIR-47347.md) · [Jira](https://jira.hl7.org/browse/FHIR-47347) |
| FHIR-47479 | Missing definition for ModValue and Derivation | Triaged | 2024-09-12 | [FHIR-47479](./FHIR-47479.md) · [Jira](https://jira.hl7.org/browse/FHIR-47479) |
| FHIR-47653 | Suggestion to add UML model of the profiles defined in this IG and how they are related | Triaged | 2024-09-13 | [FHIR-47653](./FHIR-47653.md) · [Jira](https://jira.hl7.org/browse/FHIR-47653) |

---

## FHIR Core (FHIR)

*1 ticket(s) targeting the **FHIR Core (FHIR)** specification.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-55650 | Code system may not used by Jurisdiction/implementation community | Triaged | 2026-02-10 | [FHIR-55650](./FHIR-55650.md) · [Jira](https://jira.hl7.org/browse/FHIR-55650) |

---

## FHIRCast (FHIR)

*1 ticket(s) targeting the **FHIRCast (FHIR)** specification.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-42817 | DICOM defined ValueSets are not compatible with publishing tools | Triaged | 2023-09-25 | [FHIR-42817](./FHIR-42817.md) · [Jira](https://jira.hl7.org/browse/FHIR-42817) |

---

## Radiation Dose Summary for Diagnostic Procedures on FHIR (FHIR)

*1 ticket(s) targeting the **Radiation Dose Summary for Diagnostic Procedures on FHIR (FHIR)** specification.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-37519 | Reserved trademarks like FHIR, HL7, IHE and SNOMED shall be used with the sign ® within the IG | Triaged | 2022-05-30 | [FHIR-37519](./FHIR-37519.md) · [Jira](https://jira.hl7.org/browse/FHIR-37519) |

---

## Unspecified

*1 ticket(s) targeting the **Unspecified** specification.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-35726 | Feedback on FHIR specification Radiation Dose Summary for Diagnostic Procedures on FHIR | Triaged **Priority:** Medium **Type:** Comment | 2022-01-11 **Updated:** 2024-10-06 **Labels:** None | [FHIR-35726](./FHIR-35726.md) · [Jira](https://jira.hl7.org/browse/FHIR-35726) |

---

*Generated automatically. Re-run `generate-indexes.py` to update.*

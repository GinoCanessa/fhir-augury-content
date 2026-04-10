# Biomedical Research And Regulation — Planned Tickets

This index lists all **40** planned tickets for the **Biomedical Research And Regulation** work group, grouped by specification and target artifact (repository).

> **Planned tickets** have approved resolutions with implementation plans. Work through them in the order shown — tickets are sorted so that prerequisites come before dependents.

---

## Table of Contents

- [CDISC Lab (FHIR)](#cdisc-lab-fhir)
- [CDISC Mappings (FHIR)](#cdisc-mappings-fhir)
- [FHIR Core (FHIR)](#fhir-core-fhir)
- [FHIR Extensions Pack (FHIR)](#fhir-extensions-pack-fhir)
- [FHIR to OMOP FHIR IG (FHIR)](#fhir-to-omop-fhir-ig-fhir)
- [US Coordinated Registry Network (CRN) (FHIR)](#us-coordinated-registry-network-crn-fhir)

---

## CDISC Lab (FHIR)

*3 ticket(s) targeting the **CDISC Lab (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

#### Dependency Group: FHIR-24125

> **FHIR-24125** must be completed before FHIR-24127. These tickets share prerequisite relationships — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-24125 | Move content from uploads page to Overview page. - CDISC_LAB #3 | Resolved - change required | 2021-10-27 | [FHIR-24125](./FHIR-24125.md) · [Jira](https://jira.hl7.org/browse/FHIR-24125) |
| FHIR-24127 | Recommend adding BRIDG to scope. - CDISC_LAB #4 | Resolved - change required | 2021-10-27 | [FHIR-24127](./FHIR-24127.md) · [Jira](https://jira.hl7.org/browse/FHIR-24127) |

#### Other Tickets

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-24123 | Corect spelling of 'transforming' in paragraph: - CDISC_LAB #2 | Resolved - change required | 2021-10-27 | [FHIR-24123](./FHIR-24123.md) · [Jira](https://jira.hl7.org/browse/FHIR-24123) |

---

## CDISC Mappings (FHIR)

*2 ticket(s) targeting the **CDISC Mappings (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-30536 | Revisit sex mapping | Resolved - change required | 2021-05-17 | [FHIR-30536](./FHIR-30536.md) · [Jira](https://jira.hl7.org/browse/FHIR-30536) |
| FHIR-35825 | The FHIR FHIRPath mapping for the AE has errors | Resolved - change required | 2022-01-18 | [FHIR-35825](./FHIR-35825.md) · [Jira](https://jira.hl7.org/browse/FHIR-35825) |

---

## FHIR Core (FHIR)

*13 ticket(s) targeting the **FHIR Core (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

#### Dependency Group: FHIR-43577

> **FHIR-43577** must be completed before FHIR-43579, FHIR-46450. These tickets share prerequisite relationships — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-43577 | Change research-subject-state value set in accordance with BRR consensus | Resolved - change required | 2024-01-29 | [FHIR-43577](./FHIR-43577.md) · [Jira](https://jira.hl7.org/browse/FHIR-43577) |
| FHIR-43579 | Change CodeSystem: StateChangeReason in accordance with BRR consensus | Resolved - change required | 2024-01-29 | [FHIR-43579](./FHIR-43579.md) · [Jira](https://jira.hl7.org/browse/FHIR-43579) |
| FHIR-46450 | Extend the subjectState.code definitions for on-study / off-study to cover their meaning in retrospective use | Resolved - change required | 2025-03-18 | [FHIR-46450](./FHIR-46450.md) · [Jira](https://jira.hl7.org/browse/FHIR-46450) |

#### Dependency Group: FHIR-39004

> **FHIR-39004** must be completed before FHIR-39003. These tickets share prerequisite relationships — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-39004 | Change Study Design Value Set content logical definition to use SEVCO once published in THO | Resolved - change required | 2025-03-13 | [FHIR-39004](./FHIR-39004.md) · [Jira](https://jira.hl7.org/browse/FHIR-39004) |
| FHIR-39003 | Remove external SEVCO codes from research-study-classifiers CodeSystem and add an external code system. | Resolved - change required | 2025-03-13 | [FHIR-39003](./FHIR-39003.md) · [Jira](https://jira.hl7.org/browse/FHIR-39003) |

#### Other Tickets

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-50461 | Add data-monitoring to ResearchStudyPartyRole CodeSystem | Resolved - change required | 2025-05-20 | [FHIR-50461](./FHIR-50461.md) · [Jira](https://jira.hl7.org/browse/FHIR-50461) |
| FHIR-53697 | Change binding for ResearchStudy.progressStatus.state | Resolved – change required | 2025-12-22 | [FHIR-53697](./FHIR-53697.md) · [Jira](https://jira.hl7.org/browse/FHIR-53697) |
| FHIR-53696 | Change binding for ResearchStudy.associatedParty.role | Resolved — change required | 2026-01-26 | [FHIR-53696](./FHIR-53696.md) · [Jira](https://jira.hl7.org/browse/FHIR-53696) |
| FHIR-53692 | Change ResearchStudy.primaryPurposeType 0..1 to ResearchStudy.purposeType 0..* | Resolved — change required | — | [FHIR-53692](./FHIR-53692.md) · [Jira](https://jira.hl7.org/browse/FHIR-53692) |

### HL7/UTG

*2 ticket(s) affecting [HL7/UTG](https://github.com/HL7/UTG).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-53693 | Add ResearchStudy.comparisonGroup.name 0..1 string | Resolved – change required | 2026-01-26 | [FHIR-53693](./FHIR-53693.md) · [Jira](https://jira.hl7.org/browse/FHIR-53693) |
| FHIR-53694 | Add DocumentReference as a type option for ResearchStudy.result 0..* Reference | Resolved – change required | 2026-01-26 | [FHIR-53694](./FHIR-53694.md) · [Jira](https://jira.hl7.org/browse/FHIR-53694) |

### HL7/ebm-incubator

*3 ticket(s) affecting [HL7/ebm-incubator](https://github.com/HL7/ebm-incubator).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-53693 | Add ResearchStudy.comparisonGroup.name 0..1 string | Resolved – change required | 2026-01-26 | [FHIR-53693](./FHIR-53693.md) · [Jira](https://jira.hl7.org/browse/FHIR-53693) |
| FHIR-53694 | Add DocumentReference as a type option for ResearchStudy.result 0..* Reference | Resolved – change required | 2026-01-26 | [FHIR-53694](./FHIR-53694.md) · [Jira](https://jira.hl7.org/browse/FHIR-53694) |
| FHIR-53698 | Change binding for ResearchStudy.studyDesign | Resolved – change required | 2026-01-26 | [FHIR-53698](./FHIR-53698.md) · [Jira](https://jira.hl7.org/browse/FHIR-53698) |

### HL7/fhir

*2 ticket(s) affecting [HL7/fhir](https://github.com/HL7/fhir).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-53693 | Add ResearchStudy.comparisonGroup.name 0..1 string | Resolved – change required | 2026-01-26 | [FHIR-53693](./FHIR-53693.md) · [Jira](https://jira.hl7.org/browse/FHIR-53693) |
| FHIR-56036 | Add UMC as a substances naming authority | Resolved – change required | — | [FHIR-56036](./FHIR-56036.md) · [Jira](https://jira.hl7.org/browse/FHIR-56036) |

### HL7/fhir-extensions

*3 ticket(s) affecting [HL7/fhir-extensions](https://github.com/HL7/fhir-extensions).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-53693 | Add ResearchStudy.comparisonGroup.name 0..1 string | Resolved – change required | 2026-01-26 | [FHIR-53693](./FHIR-53693.md) · [Jira](https://jira.hl7.org/browse/FHIR-53693) |
| FHIR-53694 | Add DocumentReference as a type option for ResearchStudy.result 0..* Reference | Resolved – change required | 2026-01-26 | [FHIR-53694](./FHIR-53694.md) · [Jira](https://jira.hl7.org/browse/FHIR-53694) |
| FHIR-53698 | Change binding for ResearchStudy.studyDesign | Resolved – change required | 2026-01-26 | [FHIR-53698](./FHIR-53698.md) · [Jira](https://jira.hl7.org/browse/FHIR-53698) |

---

## FHIR Extensions Pack (FHIR)

*1 ticket(s) targeting the **FHIR Extensions Pack (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-55916 | Add blindedRole extension on ResearchStudy | Resolved — change required | — | [FHIR-55916](./FHIR-55916.md) · [Jira](https://jira.hl7.org/browse/FHIR-55916) |

---

## FHIR to OMOP FHIR IG (FHIR)

*7 ticket(s) targeting the **FHIR to OMOP FHIR IG (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-51808 | Potential typo in Section 3.3 | Resolved — change required | 2025-08-15 | [FHIR-51808](./FHIR-51808.md) · [Jira](https://jira.hl7.org/browse/FHIR-51808) |
| FHIR-51584 | value-as-concept page uses invalid SNOMED codes for examples | Resolved — change required | 2025-09-17 | [FHIR-51584](./FHIR-51584.md) · [Jira](https://jira.hl7.org/browse/FHIR-51584) |

### HL7/fhir-omop-ig

*5 ticket(s) affecting [HL7/fhir-omop-ig](https://github.com/HL7/fhir-omop-ig).*

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-51674 | Narrative Formatting & Spelling | Resolved - change required | 2025-08-07 | [FHIR-51674](./FHIR-51674.md) · [Jira](https://jira.hl7.org/browse/FHIR-51674) |
| FHIR-52048 | Correct affiliation in acknowledgements | Resolved – change required | 2025-08-28 | [FHIR-52048](./FHIR-52048.md) · [Jira](https://jira.hl7.org/browse/FHIR-52048) |
| FHIR-52781 | Structural Mapping Errors | Resolved — change required | 2025-09-08 | [FHIR-52781](./FHIR-52781.md) · [Jira](https://jira.hl7.org/browse/FHIR-52781) |
| FHIR-51993 | Typo - reprsented | Resolved - change required | 2025-09-16 | [FHIR-51993](./FHIR-51993.md) · [Jira](https://jira.hl7.org/browse/FHIR-51993) |
| FHIR-51582 | Invalid OMOP SQL in CodeableConcept Pattern | Resolved — change required | 2026-03-13 | [FHIR-51582](./FHIR-51582.md) · [Jira](https://jira.hl7.org/browse/FHIR-51582) |

---

## US Coordinated Registry Network (CRN) (FHIR)

*14 ticket(s) targeting the **US Coordinated Registry Network (CRN) (FHIR)** specification.*

### (no repository identified)

*These tickets do not reference a specific repository. Review each ticket to determine the target artifact.*

#### Dependency Group: FHIR-21210

> **FHIR-21210** must be completed before FHIR-20966, FHIR-20967, FHIR-21014. These tickets share prerequisite relationships — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-21210 | Mappings of CDEs to FHIR section could be more useful | Resolved - change required | 2019-08-28 | [FHIR-21210](./FHIR-21210.md) · [Jira](https://jira.hl7.org/browse/FHIR-21210) |
| FHIR-20966 | Change "NLM's CDE Repository" to "NIH CDE Repository" | Resolved - change required | 2019-08-28 | [FHIR-20966](./FHIR-20966.md) · [Jira](https://jira.hl7.org/browse/FHIR-20966) |
| FHIR-20967 | Remove sentence from section about NIH CDE Repository | Resolved - change required | 2019-08-28 | [FHIR-20967](./FHIR-20967.md) · [Jira](https://jira.hl7.org/browse/FHIR-20967) |
| FHIR-21014 | Include Common Data Elements in the IG | Resolved - change required | 2019-08-28 | [FHIR-21014](./FHIR-21014.md) · [Jira](https://jira.hl7.org/browse/FHIR-21014) |

#### Dependency Group: FHIR-21211

> **FHIR-21211** must be completed before FHIR-21017. These tickets share prerequisite relationships — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-21211 | Change mapping of Hospital Discharge | Resolved - change required | 2019-08-28 | [FHIR-21211](./FHIR-21211.md) · [Jira](https://jira.hl7.org/browse/FHIR-21211) |
| FHIR-21017 | use procedure.location instead of location.identifier? | Resolved - change required | 2019-08-28 | [FHIR-21017](./FHIR-21017.md) · [Jira](https://jira.hl7.org/browse/FHIR-21017) |

#### Dependency Group: FHIR-21016

> **FHIR-21016** must be completed before FHIR-20789. These tickets share prerequisite relationships — complete them in the listed order.

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-21016 | Remove AdverseEvent? | Resolved - change required | 2019-10-23 | [FHIR-21016](./FHIR-21016.md) · [Jira](https://jira.hl7.org/browse/FHIR-21016) |
| FHIR-20789 | Use of AdverseEvent for tracking adverse events in WHT CRN | Resolved - change required | 2019-10-23 | [FHIR-20789](./FHIR-20789.md) · [Jira](https://jira.hl7.org/browse/FHIR-20789) |

#### Other Tickets

| Key | Title | Status | Date | Links |
|-----|-------|--------|------|-------|
| FHIR-20788 | Typos in WHT CRN IG | Resolved - change required | 2019-05-06 | [FHIR-20788](./FHIR-20788.md) · [Jira](https://jira.hl7.org/browse/FHIR-20788) |
| FHIR-21321 | Add to parenthetical statement and correct element name for manufactureDate - CRN #22 | Resolved - change required | 2019-07-02 | [FHIR-21321](./FHIR-21321.md) · [Jira](https://jira.hl7.org/browse/FHIR-21321) |
| FHIR-20958 | Number sections for ease of reading/commenting | Resolved - change required | 2019-08-28 | [FHIR-20958](./FHIR-20958.md) · [Jira](https://jira.hl7.org/browse/FHIR-20958) |
| FHIR-21013 | Patient.communication.language or Patient.communication.preferred? | Resolved - change required | 2019-08-28 | [FHIR-21013](./FHIR-21013.md) · [Jira](https://jira.hl7.org/browse/FHIR-21013) |
| FHIR-21209 | WHT CRN Overview - Background - Typo | Resolved - change required | 2019-08-28 | [FHIR-21209](./FHIR-21209.md) · [Jira](https://jira.hl7.org/browse/FHIR-21209) |
| FHIR-21015 | Include LOINC and other codes when specified | Resolved - change required | 2019-09-17 | [FHIR-21015](./FHIR-21015.md) · [Jira](https://jira.hl7.org/browse/FHIR-21015) |

---

*Generated automatically. Re-run `generate-indexes.py` to update.*

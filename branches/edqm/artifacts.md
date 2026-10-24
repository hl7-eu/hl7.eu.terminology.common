# Artifacts Summary - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* **Artifacts Summary**

## Artifacts Summary

This page provides a list of the FHIR artifacts defined as part of this implementation guide.

### Terminology: Value Sets 

These define sets of codes used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [Body Structure Laterality](ValueSet-lab-laterality-eu-lab.md) | Body Structure site laterality qualifier. It indicates the body site laterality from which a laboratory specimen is collected. (based on SNOMED CT) |
| [Body Structure Qualifier](ValueSet-lab-siteQualifier-eu-lab.md) | Body Structure site qualifier. It indicates the body site qualifier from which a laboratory specimen is collected. (based on SNOMED CT) |
| [Laboratory Certified Reference Material](ValueSet-lab-certifiedRefMaterial-eu-lab.md) | List of the coded concepts describing the certified reference material used for the calibration, typically used when the unit of the result is UCUM [IU]. |
| [Laboratory Code](ValueSet-lab-obsCode-eu-lab.md) | Laboratory observation codes. List of Laboratory observation codes derived from the LOINC and NPU code systems. |
| [Laboratory Code: LOINC](ValueSet-lab-obsCode-loinc-eu-lab.md) | Laboratory observation codes based on the LOINC code system. |
| [Laboratory Code: NPU](ValueSet-lab-obsCode-npu-eu-lab.md) | Laboratory observation codes based on the NPU code system. |
| [Laboratory Order](ValueSet-lab-orderCodes-eu-lab.md) | List of LOINC Laboratory codes of type 'Order' or 'Both. This value set is built upon the IPS value set 'Results Laboratory Observation - IPS' |
| [Laboratory Report Types](ValueSet-lab-reportType-eu-lab.md) | Laboratory Report Types. This version includes only one code as suggested by the eHN guideline. Category can be used for filtering per study type or specialty. |
| [Laboratory Specialty](ValueSet-lab-specialty-eu-lab.md) | Laboratory Specialties. Notes: Note 1: This value set is based on analysis of national coding practices in 8 European countries (AT, CZ, DE, FR, IE, IT, PT, SE) and agreed by involved lab experts as a common lab specialty value set. Note 2: Many European countries are using additional laboratory specialty types, which should be mapped towards this value set. Note 3: In case of documented need, this value set could be extended. |
| [Laboratory Study Types](ValueSet-lab-studyType-eu-lab.md) | Laboratory Study Types Notes: Note 1:26436-6 (Laboratory studies) enables issuing a report putting together observations from multiple specialties (disciplines) in the same text block, allowing delivery of a global interpretation comment at the end of the text block that will be rendered at the end of the report. Note 2:Mycology and parasitology, as well as bacteriology, are part of the 18725-2 (Microbiology studies (set)) studies. Note 3:Virology MAY be included in 18725-2 (MICROBIOLOGY STUDIES) or 18727-8 (SEROLOGY STUDIES) or split between both study types, depending upon the Content Creator Actor’s choice. |
| [Laboratory Techniques](ValueSet-lab-technique-eu-lab.md) | Laboratory technique (method of measurement) used for the result measurement (based on SNOMED CT). |
| [Results Blood Group - IPS](ValueSet-results-blood-group-uv-ips.md) | Blood group [Type] |
| [Results Coded Values Laboratory - IPS](ValueSet-results-coded-values-laboratory-uv-ips.md) | This value set is defined as the union of: (a) Blood group [Type]; (b) Presence/Absence Indicators (2.16.840.1.113883.11.22.52) (c) Microorganisms (2.16.840.1.113883.11.22.49) |
| [Results Microorganism - IPS](ValueSet-results-microorganism-uv-ips.md) | This is a value set of the SNOMED CT microorganism concepts for use in the Results section observation values. |
| [Results Presence/Absence - IPS](ValueSet-results-presence-absence-uv-ips.md) | Presence/Absence value set |
| [Specimen Additive](ValueSet-lab-specimenAdditive-eu-lab.md) | List of the specimen additives. Additives are commonly added to the vacutainer tubes to preserve the specimen for laboratory analysis |
| [Specimen Container](ValueSet-lab-specimenContainer-eu-lab.md) | List of the containers commonly used to collect specimens (e.g. urine, blood,..). |
| [Specimen Types](ValueSet-lab-specimenType-eu-lab.md) | Laboratory Specimen Types |
| [Types of species](ValueSet-lab-speciesType-eu-vs.md) | Types of animal species for non-human subjects |
| [eHDSI Laboratory Study Types](ValueSet-eHDSILabStudyType.md) |  |

### Terminology: Code Systems 

These define new code systems used by systems conforming to this implementation guide.

| | |
| :--- | :--- |
| [ATC classification system](CodeSystem-atc.md) | Anatomical Therapeutic Chemical (ATC) classification system |
| [EDQM](CodeSystem-edqm.md) | EDQM |
| [EMDN CodeSystem](CodeSystem-emdn.md) | European Medical Device Nomenclature |
| [Laboratory Code: example](CodeSystem-lab-localCs-eu-lab.md) | List of local coded concepts used for supporting the examples defined in this guide. |


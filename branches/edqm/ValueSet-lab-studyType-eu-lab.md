# Laboratory Study Types - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Laboratory Study Types**

## ValueSet: Laboratory Study Types 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-studyType-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:LabStudyTypesEuVs |
| **Copyright/Legal**: This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc | | |

 
Laboratory Study Types Notes: Note 1:26436-6 (Laboratory studies) enables issuing a report putting together observations from multiple specialties (disciplines) in the same text block, allowing delivery of a global interpretation comment at the end of the text block that will be rendered at the end of the report. Note 2:Mycology and parasitology, as well as bacteriology, are part of the 18725-2 (Microbiology studies (set)) studies. Note 3:Virology MAY be included in 18725-2 (MICROBIOLOGY STUDIES) or 18727-8 (SEROLOGY STUDIES) or split between both study types, depending upon the Content Creator Actor’s choice. 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

 

### Expansion

-------

 Explanation of the columns that may appear on this page: 

| | |
| :--- | :--- |
| Level | A few code lists that FHIR defines are hierarchical - each code is assigned a level. In this scheme, some codes are under other codes, and imply that the code they are under also applies |
| System | The source of the definition of the code (when the value set draws in codes defined elsewhere) |
| Code | The code (used as the code in the resource instance) |
| Display | The display (used in the*display*element of a[Coding](http://hl7.org/fhir/R4/datatypes.html#Coding)). If there is no display, implementers should not simply display the code, but map the concept into their application |
| Definition | An explanation of the meaning of the concept |
| Comments | Additional notes about how to use the code |



## Resource Content

```json
{
  "resourceType" : "ValueSet",
  "id" : "lab-studyType-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-studyType-eu-lab",
  "version" : "0.4.0",
  "name" : "LabStudyTypesEuVs",
  "title" : "Laboratory Study Types",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-10-24T21:00:57+00:00",
  "publisher" : "HL7 Europe",
  "contact" : [{
    "name" : "HL7 Europe",
    "telecom" : [{
      "system" : "url",
      "value" : "http://hl7europe.org"
    }]
  }],
  "description" : "Laboratory Study Types\nNotes:\nNote 1:26436-6 (Laboratory studies) enables issuing a report putting together observations from multiple specialties (disciplines) in the same text block, allowing delivery of a global interpretation comment at the end of the text block that will be rendered at the end of the report.\nNote 2:Mycology and parasitology, as well as bacteriology, are part of the 18725-2 (Microbiology studies (set)) studies.\nNote 3:Virology MAY be included in 18725-2 (MICROBIOLOGY STUDIES) or 18727-8 (SEROLOGY STUDIES) or split between both study types, depending upon the Content Creator Actor’s choice.",
  "copyright" : "This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc",
  "compose" : {
    "include" : [{
      "system" : "http://loinc.org",
      "concept" : [{
        "code" : "18717-9",
        "display" : "Blood bank studies (set)"
      },
      {
        "code" : "18719-5",
        "display" : "Chemistry studies (set)"
      },
      {
        "code" : "18722-9",
        "display" : "Fertility studies (set)"
      },
      {
        "code" : "18723-7",
        "display" : "Hematology studies (set)"
      },
      {
        "code" : "18725-2",
        "display" : "Microbiology studies (set)"
      },
      {
        "code" : "18728-6",
        "display" : "Toxicology studies (set)"
      },
      {
        "code" : "26436-6",
        "display" : "Laboratory studies (set)"
      }]
    }]
  }
}

```

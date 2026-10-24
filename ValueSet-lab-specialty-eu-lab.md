# Laboratory Specialty - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Laboratory Specialty**

## ValueSet: Laboratory Specialty 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-specialty-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:LabSpecialtyEuVs |
| **Copyright/Legal**: This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement | | |

 
Laboratory Specialties. Notes: Note 1: This value set is based on analysis of national coding practices in 8 European countries (AT, CZ, DE, FR, IE, IT, PT, SE) and agreed by involved lab experts as a common lab specialty value set. Note 2: Many European countries are using additional laboratory specialty types, which should be mapped towards this value set. Note 3: In case of documented need, this value set could be extended. 

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
  "id" : "lab-specialty-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-specialty-eu-lab",
  "version" : "0.4.0",
  "name" : "LabSpecialtyEuVs",
  "title" : "Laboratory Specialty",
  "status" : "draft",
  "experimental" : false,
  "date" : "2026-10-24T21:10:34+00:00",
  "publisher" : "HL7 Europe",
  "contact" : [{
    "name" : "HL7 Europe",
    "telecom" : [{
      "system" : "url",
      "value" : "http://hl7europe.org"
    }]
  }],
  "description" : "Laboratory Specialties.\nNotes:\nNote 1: This value set is based on analysis of national coding practices in 8 European countries (AT, CZ, DE, FR, IE, IT, PT, SE) and agreed by involved lab experts as a common lab specialty value set.\nNote 2: Many European countries are using additional laboratory specialty types, which should be mapped towards this value set.\nNote 3: In case of documented need, this value set could be extended.",
  "copyright" : "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement",
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "394596001",
        "display" : "Chemical pathology"
      },
      {
        "code" : "394916005",
        "display" : "Hematopathology"
      },
      {
        "code" : "421661004",
        "display" : "Blood banking and transfusion medicine"
      },
      {
        "code" : "394915009",
        "display" : "General pathology"
      },
      {
        "code" : "394598000",
        "display" : "Immunopathology"
      },
      {
        "code" : "408454008",
        "display" : "Clinical microbiology"
      },
      {
        "code" : "1236877003",
        "display" : "Genetic pathology"
      },
      {
        "code" : "1236878008",
        "display" : "Histocompatibility and Immunogenetics"
      }]
    }]
  }
}

```

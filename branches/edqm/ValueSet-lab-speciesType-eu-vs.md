# Types of species - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Types of species**

## ValueSet: Types of species 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-speciesType-eu-vs | *Version*:0.4.0 | |
| * Standards status: *[Draft](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 1 | *Computable Name*:LabSpeciesTypesEuVs |
| **Copyright/Legal**: This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement | | |

 
Types of animal species for non-human subjects 

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
  "id" : "lab-speciesType-eu-vs",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 1
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "draft"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-speciesType-eu-vs",
  "version" : "0.4.0",
  "name" : "LabSpeciesTypesEuVs",
  "title" : "Types of species",
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
  "description" : "Types of animal species for non-human subjects",
  "copyright" : "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement",
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "125097000",
        "display" : "Domestic goat"
      },
      {
        "code" : "125099002",
        "display" : "Sheep"
      },
      {
        "code" : "34618005",
        "display" : "Cow"
      },
      {
        "code" : "425134008",
        "display" : "Turkey"
      },
      {
        "code" : "47290002",
        "display" : "Chicken"
      },
      {
        "code" : "15778005",
        "display" : "Anser"
      },
      {
        "code" : "396620009",
        "display" : "Duck"
      },
      {
        "code" : "35354009",
        "display" : "Horse"
      },
      {
        "code" : "85626006",
        "display" : "Donkey"
      },
      {
        "code" : "132950000",
        "display" : "Mule"
      },
      {
        "code" : "448771007",
        "display" : "Domestic dog"
      },
      {
        "code" : "448169003",
        "display" : "Domestic cat"
      }]
    }]
  }
}

```

# Body Structure Qualifier - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Body Structure Qualifier**

## ValueSet: Body Structure Qualifier 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-siteQualifier-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:LabSiteQualifierEuVs |
| **Copyright/Legal**: This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement | | |

 
Body Structure site qualifier. It indicates the body site qualifier from which a laboratory specimen is collected. (based on SNOMED CT) 

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
  "id" : "lab-siteQualifier-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-siteQualifier-eu-lab",
  "version" : "0.4.0",
  "name" : "LabSiteQualifierEuVs",
  "title" : "Body Structure Qualifier",
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
  "description" : "Body Structure site qualifier. It indicates the body site qualifier from which a laboratory specimen is collected. (based on SNOMED CT)",
  "copyright" : "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement",
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "7771000",
        "display" : "Left"
      },
      {
        "code" : "24028007",
        "display" : "Right"
      },
      {
        "code" : "51440002",
        "display" : "Bilateral"
      },
      {
        "code" : "46053002",
        "display" : "Distal"
      },
      {
        "code" : "255554000",
        "display" : "Dorsal"
      },
      {
        "code" : "261183002",
        "display" : "Upper"
      },
      {
        "code" : "261122009",
        "display" : "Lower"
      },
      {
        "code" : "255561001",
        "display" : "Medial"
      },
      {
        "code" : "49370004",
        "display" : "Lateral"
      },
      {
        "code" : "264217000",
        "display" : "Superior"
      },
      {
        "code" : "261089000",
        "display" : "Inferior"
      },
      {
        "code" : "255551008",
        "display" : "Posterior"
      },
      {
        "code" : "351726001",
        "display" : "Below"
      },
      {
        "code" : "352730000",
        "display" : "Above"
      },
      {
        "code" : "40415009",
        "display" : "Proximal (qualifier value)"
      },
      {
        "code" : "255549009",
        "display" : "Anterior (qualifier value)"
      },
      {
        "code" : "26283006",
        "display" : "Superficial (qualifier value)"
      },
      {
        "code" : "795002",
        "display" : "Deep (qualifier value)"
      },
      {
        "code" : "57195005",
        "display" : "Basal (qualifier value)"
      },
      {
        "code" : "3583002",
        "display" : "Caudal (qualifier value)"
      },
      {
        "code" : "66787007",
        "display" : "Cephalic (qualifier value)"
      },
      {
        "code" : "255481003",
        "display" : "Left upper quadrant (qualifier value)"
      },
      {
        "code" : "255497008",
        "display" : "Right upper quadrant (qualifier value)"
      },
      {
        "code" : "255480002",
        "display" : "Left lower quadrant (qualifier value)"
      },
      {
        "code" : "255495000",
        "display" : "Right lower quadrant (qualifier value)"
      }]
    }]
  }
}

```

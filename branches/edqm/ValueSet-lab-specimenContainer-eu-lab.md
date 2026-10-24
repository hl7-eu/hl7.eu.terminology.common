# Specimen Container - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Specimen Container**

## ValueSet: Specimen Container 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-specimenContainer-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:LabSpecimenContainerEu |
| **Copyright/Legal**: This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement | | |

 
List of the containers commonly used to collect specimens (e.g. urine, blood,..). 

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
  "id" : "lab-specimenContainer-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-specimenContainer-eu-lab",
  "version" : "0.4.0",
  "name" : "LabSpecimenContainerEu",
  "title" : "Specimen Container",
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
  "description" : "List of the containers commonly used to collect specimens (e.g. urine, blood,..).",
  "copyright" : "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement",
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "702290003",
        "display" : "Cervical cytology microscopy slide"
      },
      {
        "code" : "706057008",
        "display" : "Cytology specimen container"
      },
      {
        "code" : "706052002",
        "display" : "Evacuated blood collection tube"
      },
      {
        "code" : "702292006",
        "display" : "Evacuated blood collection tube, K3EDTA/sodium fluoride"
      },
      {
        "code" : "767387006",
        "display" : "Evacuated blood collection tube with citrate and theophylline and adenosine and dipyramidole"
      },
      {
        "code" : "767384004",
        "display" : "Evacuated blood collection tube with clot activator"
      },
      {
        "code" : "767390000",
        "display" : "Evacuated blood collection tube with heparin lithium and gel separator"
      },
      {
        "code" : "767382000",
        "display" : "Evacuated blood collection tube with heparin sodium"
      },
      {
        "code" : "767660003",
        "display" : "Evacuated blood collection tube with sodium fluoride"
      },
      {
        "code" : "767389009",
        "display" : "Evacuated blood collection tube with tripotassium and ethylene diamine tetraacetic acid and aprotinin"
      },
      {
        "code" : "702279008",
        "display" : "Evacuated blood collection tube, gel separator"
      },
      {
        "code" : "702293001",
        "display" : "Evacuated blood collection tube, K2EDTA/aprotinin"
      },
      {
        "code" : "702278000",
        "display" : "Evacuated blood collection tube, no additive/metal-free"
      },
      {
        "code" : "702280006",
        "display" : "Evacuated blood collection tube, RNA stabiliser"
      },
      {
        "code" : "702281005",
        "display" : "Evacuated blood collection tube, thrombin/clot activator/gel separator"
      },
      {
        "code" : "702310001",
        "display" : "Evacuated saliva specimen container, sodium azide"
      },
      {
        "code" : "706056004",
        "display" : "Evacuated urine specimen container"
      },
      {
        "code" : "702302002",
        "display" : "Evacuated urine specimen container, boric acid (H3BO3)"
      },
      {
        "code" : "702288004",
        "display" : "Evacuated urine specimen container, boric acid (H3BO3)/sodium formate"
      },
      {
        "code" : "702289007",
        "display" : "Evacuated urine specimen container, ethyl paraben/sodium propionate/chlorhexidine"
      },
      {
        "code" : "702303007",
        "display" : "Evacuated urine specimen container, multiple preservative"
      },
      {
        "code" : "702308003",
        "display" : "Evacuated urine specimen container, no additive"
      },
      {
        "code" : "706047007",
        "display" : "Fecal specimen container"
      },
      {
        "code" : "706053007",
        "display" : "General specimen container"
      },
      {
        "code" : "702268003",
        "display" : "General specimen container, no additive, non-sterile"
      },
      {
        "code" : "702269006",
        "display" : "General specimen container, no additive, sterile"
      },
      {
        "code" : "874799005",
        "display" : "Microbial cryotube"
      },
      {
        "code" : "706050005",
        "display" : "Microcapillary blood collection tube"
      },
      {
        "code" : "702275002",
        "display" : "Microcapillary blood collection tube, ammonium heparin"
      },
      {
        "code" : "702276001",
        "display" : "Microcapillary blood collection tube, K2EDTA"
      },
      {
        "code" : "702277005",
        "display" : "Microcapillary blood collection tube, no additive"
      },
      {
        "code" : "702304001",
        "display" : "Microcapillary blood transfer tube, clot activator"
      },
      {
        "code" : "702306004",
        "display" : "Microcapillary blood transfer tube, EDTA"
      },
      {
        "code" : "702307008",
        "display" : "Microcapillary blood transfer tube, heparin"
      },
      {
        "code" : "702305000",
        "display" : "Microcapillary sodium fluoride blood transfer tube"
      },
      {
        "code" : "702224000",
        "display" : "Midstream urine specimen container"
      },
      {
        "code" : "706051009",
        "display" : "Non-evacuated blood collection tube"
      },
      {
        "code" : "702283008",
        "display" : "Non-evacuated blood collection tube with gel separator"
      },
      {
        "code" : "702297000",
        "display" : "Non-evacuated blood collection tube, clot activator"
      },
      {
        "code" : "702295008",
        "display" : "Non-evacuated blood collection tube, clot activator/gel separator"
      },
      {
        "code" : "702282003",
        "display" : "Non-evacuated blood collection tube, EDTA"
      },
      {
        "code" : "702299002",
        "display" : "Non-evacuated blood collection tube, K2EDTA"
      },
      {
        "code" : "702298005",
        "display" : "Non-evacuated blood collection tube, K3EDTA"
      },
      {
        "code" : "702284002",
        "display" : "Non-evacuated blood collection tube, lithium heparin"
      },
      {
        "code" : "702300005",
        "display" : "Non-evacuated blood collection tube, lithium heparin/gel separator, non-sterile"
      },
      {
        "code" : "702285001",
        "display" : "Non-evacuated blood collection tube, lithium heparin/gel separator, sterile"
      },
      {
        "code" : "702286000",
        "display" : "Non-evacuated blood collection tube, NaEDTA/sodium fluoride"
      },
      {
        "code" : "702256007",
        "display" : "Non-evacuated blood collection tube, no additive"
      },
      {
        "code" : "702287009",
        "display" : "Non-evacuated blood collection tube, potassium oxalate/sodium fluoride"
      },
      {
        "code" : "702296009",
        "display" : "Non-evacuated blood collection tube, sodium citrate"
      },
      {
        "code" : "702264001",
        "display" : "Non-sterile urine specimen container"
      },
      {
        "code" : "702309006",
        "display" : "Saliva specimen container, no additive"
      },
      {
        "code" : "706058003",
        "display" : "Secretory specimen container"
      },
      {
        "code" : "706046003",
        "display" : "Specimen receptacle"
      },
      {
        "code" : "702223006",
        "display" : "Sputum specimen container"
      },
      {
        "code" : "702244006",
        "display" : "Sterile urine specimen container"
      },
      {
        "code" : "702232008",
        "display" : "Sweat specimen container"
      },
      {
        "code" : "702294007",
        "display" : "Syringe-blood collection tube transfer"
      },
      {
        "code" : "706054001",
        "display" : "Urine specimen container"
      },
      {
        "code" : "767385003",
        "display" : "Aerobic blood culture bottle"
      },
      {
        "code" : "767383005",
        "display" : "Anaerobic blood culture bottle"
      }]
    }]
  }
}

```

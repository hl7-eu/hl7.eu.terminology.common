# Laboratory Code: example - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Laboratory Code: example**

## CodeSystem: Laboratory Code: example (Experimental) 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://example.org/lab-codes | *Version*:0.4.0 | |
| * Standards status: *[Informative](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 1 | *Computable Name*:LaboratoryLocalCS |

 
List of local coded concepts used for supporting the examples defined in this guide. 

 This Code system is referenced in the content logical definition of the following value sets: 

* This CodeSystem is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)



## Resource Content

```json
{
  "resourceType" : "CodeSystem",
  "id" : "lab-localCs-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 1
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "informative"
  }],
  "url" : "http://example.org/lab-codes",
  "version" : "0.4.0",
  "name" : "LaboratoryLocalCS",
  "title" : "Laboratory Code: example",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-10-24T21:00:57+00:00",
  "publisher" : "HL7 Europe",
  "contact" : [{
    "name" : "HL7 Europe",
    "telecom" : [{
      "system" : "url",
      "value" : "http://hl7europe.org"
    }]
  }],
  "description" : "List of local coded concepts used for supporting the examples defined in this guide.",
  "caseSensitive" : false,
  "content" : "complete",
  "count" : 6,
  "concept" : [{
    "code" : "3002989",
    "display" : "Hepatitis Panel, Acute with Reflex to HBsAg Confirmation and Reflex to HCV by Quantitative NAAT"
  },
  {
    "code" : "0020089",
    "display" : "Hepatitis B Surface Antigen"
  },
  {
    "code" : "0020092",
    "display" : "Hepatitis B Core Antibody, IgM"
  },
  {
    "code" : "0020093",
    "display" : "Hepatitis A Antibody, IgM"
  },
  {
    "code" : "3003128",
    "display" : "Hepatitis C Antibody by CIA Interp"
  },
  {
    "code" : "2002404",
    "display" : "Hepatitis C Antibody by CIA Index"
  }]
}

```

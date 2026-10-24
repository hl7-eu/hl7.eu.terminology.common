# Laboratory Order - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Laboratory Order**

## ValueSet: Laboratory Order 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-orderCodes-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:LabOrderCodesEuVs |
| **Copyright/Legal**: This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc | | |

 
List of LOINC Laboratory codes of type 'Order' or 'Both. This value set is built upon the IPS value set 'Results Laboratory Observation - IPS' 

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
  "id" : "lab-orderCodes-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-orderCodes-eu-lab",
  "version" : "0.4.0",
  "name" : "LabOrderCodesEuVs",
  "title" : "Laboratory Order",
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
  "description" : "List of LOINC Laboratory codes of type 'Order' or 'Both. This value set is built upon the IPS value set 'Results Laboratory Observation - IPS'",
  "copyright" : "This material contains content from LOINC (http://loinc.org). LOINC is copyright © 1995-2020, Regenstrief Institute, Inc. and the Logical Observation Identifiers Names and Codes (LOINC) Committee and is available at no cost under the license at http://loinc.org/license. LOINC® is a registered United States trademark of Regenstrief Institute, Inc",
  "compose" : {
    "include" : [{
      "system" : "http://loinc.org",
      "filter" : [{
        "property" : "ORDER_OBS",
        "op" : "=",
        "value" : "Order"
      }],
      "valueSet" : ["http://hl7.org/fhir/uv/ips/ValueSet/results-laboratory-observations-uv-ips"]
    },
    {
      "system" : "http://loinc.org",
      "filter" : [{
        "property" : "ORDER_OBS",
        "op" : "=",
        "value" : "Both"
      }],
      "valueSet" : ["http://hl7.org/fhir/uv/ips/ValueSet/results-laboratory-observations-uv-ips"]
    }]
  }
}

```

# Laboratory Code: NPU - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Laboratory Code: NPU**

## ValueSet: Laboratory Code: NPU 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-obsCode-npu-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:NpuVs |
| **Copyright/Legal**: This material contains content from NPU Terminology (http://npu-terminology.org). NPU is copyright International Federation of Clinical Chemistry (IFCC) and International Union of Pure and Applied Chemistry (IUPAC) and is available at no cost under the license at https://www.labterm.dk/. | | |

 
Laboratory observation codes based on the NPU code system. 

 **References** 

* Included into [Laboratory Code](ValueSet-lab-obsCode-eu-lab.md)

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
  "id" : "lab-obsCode-npu-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-obsCode-npu-eu-lab",
  "version" : "0.4.0",
  "name" : "NpuVs",
  "title" : "Laboratory Code: NPU",
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
  "description" : "Laboratory observation codes based on the NPU code system.",
  "copyright" : "This material contains content from NPU Terminology (http://npu-terminology.org). NPU is copyright International Federation of Clinical Chemistry (IFCC) and International Union of Pure and Applied Chemistry (IUPAC) and is available at no cost under the license at https://www.labterm.dk/.",
  "compose" : {
    "include" : [{
      "system" : "http://npu-terminology.org"
    }]
  }
}

```

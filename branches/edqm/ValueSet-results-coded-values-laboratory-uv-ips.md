# Results Coded Values Laboratory - IPS - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Results Coded Values Laboratory - IPS**

## ValueSet: Results Coded Values Laboratory - IPS 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7.org/fhir/uv/ips/ValueSet/results-coded-values-laboratory-uv-ips | *Version*:1.1.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:ResultsCodedValuesLaboratoryUvIps |
| *Other Identifiers:*http://art-decor.org/ns/oids/vs#2.16.840.1.113883.11.22.46 (use: official) | | |
| **Copyright/Legal**: The HL7 International IPS implementation guides incorporate SNOMED CT®, used by permission of the International Health Terminology Standards Development Organisation, trading as SNOMED International. SNOMED CT was originally created by the College of American Pathologists. SNOMED CT is a registered trademark of the International Health Terminology Standards Development Organisation, all rights reserved. Implementers of SNOMED CT should review [usage terms](http://www.snomed.org/snomed-ct/get-snomed-ct) or directly contact SNOMED International: info@snomed.org | | |

 
This value set is defined as the union of: (a) Blood group [Type]; (b) Presence/Absence Indicators (2.16.840.1.113883.11.22.52) (c) Microorganisms (2.16.840.1.113883.11.22.49) 

 **References** 

This value set is not used here; it may be used elsewhere (e.g. specifications and/or implementations that use this content)

### Logical Definition (CLD)

 

### Expansion

No Expansion for this valueset (Unknown Code System)

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
  "id" : "results-coded-values-laboratory-uv-ips",
  "meta" : {
    "profile" : ["http://hl7.org/fhir/StructureDefinition/shareablevalueset"]
  },
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2,
    "_valueInteger" : {
      "extension" : [{
        "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-conformance-derivedFrom",
        "valueCanonical" : "http://hl7.org/fhir/uv/ips/ImplementationGuide/ig-uv-ips"
      }]
    }
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use",
    "_valueCode" : {
      "extension" : [{
        "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-conformance-derivedFrom",
        "valueCanonical" : "http://hl7.org/fhir/uv/ips/ImplementationGuide/ig-uv-ips"
      }]
    }
  }],
  "url" : "http://hl7.org/fhir/uv/ips/ValueSet/results-coded-values-laboratory-uv-ips",
  "identifier" : [{
    "use" : "official",
    "system" : "http://art-decor.org/ns/oids/vs",
    "value" : "2.16.840.1.113883.11.22.46"
  }],
  "version" : "1.1.0",
  "name" : "ResultsCodedValuesLaboratoryUvIps",
  "title" : "Results Coded Values Laboratory - IPS",
  "status" : "active",
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
  "description" : "This value set is defined as the union of: (a) Blood group [Type]; (b) Presence/Absence Indicators (2.16.840.1.113883.11.22.52) (c) Microorganisms (2.16.840.1.113883.11.22.49)",
  "immutable" : false,
  "copyright" : "The HL7 International IPS implementation guides incorporate SNOMED CT®, used by permission of the International Health Terminology Standards Development Organisation, trading as SNOMED International. SNOMED CT was originally created by the College of American Pathologists. SNOMED CT is a registered trademark of the International Health Terminology Standards Development Organisation, all rights reserved. Implementers of SNOMED CT should review [usage terms](http://www.snomed.org/snomed-ct/get-snomed-ct) or directly contact SNOMED International: info@snomed.org",
  "compose" : {
    "include" : [{
      "valueSet" : ["http://hl7.org/fhir/uv/ips/ValueSet/results-blood-group-uv-ips"]
    },
    {
      "valueSet" : ["http://hl7.org/fhir/uv/ips/ValueSet/results-presence-absence-uv-ips"]
    },
    {
      "valueSet" : ["http://hl7.org/fhir/uv/ips/ValueSet/results-microorganism-uv-ips"]
    }]
  }
}

```

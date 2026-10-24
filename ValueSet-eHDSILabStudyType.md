# eHDSI Laboratory Study Types - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **eHDSI Laboratory Study Types**

## ValueSet: eHDSI Laboratory Study Types 

| | |
| :--- | :--- |
| *Official URL*:http://terminology.ehdsi.eu/ValueSet/eHDSILabStudyType | *Version*:8.0.1 |
| Draft as of 2026-10-24 | *Computable Name*:eHDSILabStudyType |
| *Other Identifiers:*OID:1.3.6.1.4.1.12559.11.10.1.3.1.42.66 | |

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
  "id" : "eHDSILabStudyType",
  "url" : "http://terminology.ehdsi.eu/ValueSet/eHDSILabStudyType",
  "identifier" : [{
    "system" : "urn:ietf:rfc:3986",
    "value" : "urn:oid:1.3.6.1.4.1.12559.11.10.1.3.1.42.66"
  }],
  "version" : "8.0.1",
  "name" : "eHDSILabStudyType",
  "title" : "eHDSI Laboratory Study Types",
  "status" : "draft",
  "date" : "2026-10-24T21:10:34+00:00",
  "publisher" : "HL7 Europe",
  "contact" : [{
    "name" : "HL7 Europe",
    "telecom" : [{
      "system" : "url",
      "value" : "http://hl7europe.org"
    }]
  }],
  "compose" : {
    "include" : [{
      "system" : "http://loinc.org",
      "concept" : [{
        "code" : "18722-9"
      },
      {
        "code" : "26436-6"
      },
      {
        "code" : "18719-5"
      },
      {
        "code" : "18725-2"
      },
      {
        "code" : "18723-7"
      },
      {
        "code" : "18728-6"
      },
      {
        "code" : "18717-9"
      }]
    }]
  }
}

```

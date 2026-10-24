# Laboratory Techniques - EU Common Terminologies v0.4.0

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **Laboratory Techniques**

## ValueSet: Laboratory Techniques 

| | | |
| :--- | :--- | :--- |
| *Official URL*:http://hl7europe.org/fhir/terminology/common/ValueSet/lab-technique-eu-lab | *Version*:0.4.0 | |
| * Standards status: *[Trial-use](http://hl7.org/fhir/R4/versions.html#std-process) | [Maturity Level](http://hl7.org/fhir/versions.html#maturity): 2 | *Computable Name*:LabTechniqueEuVs |
| **Copyright/Legal**: This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement | | |

 
Laboratory technique (method of measurement) used for the result measurement (based on SNOMED CT). 

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
  "id" : "lab-technique-eu-lab",
  "extension" : [{
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-fmm",
    "valueInteger" : 2
  },
  {
    "url" : "http://hl7.org/fhir/StructureDefinition/structuredefinition-standards-status",
    "valueCode" : "trial-use"
  }],
  "url" : "http://hl7europe.org/fhir/terminology/common/ValueSet/lab-technique-eu-lab",
  "version" : "0.4.0",
  "name" : "LabTechniqueEuVs",
  "title" : "Laboratory Techniques",
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
  "description" : "Laboratory technique (method of measurement) used for the result measurement (based on SNOMED CT).",
  "copyright" : "This value set includes content from SNOMED CT, which is copyright © 2002+ International Health Terminology Standards Development Organisation (IHTSDO), and distributed by agreement between IHTSDO and HL7. Implementer use of SNOMED CT is not covered by this agreement",
  "compose" : {
    "include" : [{
      "system" : "http://snomed.info/sct",
      "concept" : [{
        "code" : "1259932009",
        "display" : "Loop-mediated isothermal amplification technique (qualifier value)"
      },
      {
        "code" : "1259933004",
        "display" : "Strand displacement amplification technique (qualifier value)"
      },
      {
        "code" : "1259934005",
        "display" : "Microparticle enzyme immunoassay technique (qualifier value)"
      },
      {
        "code" : "1259935006",
        "display" : "Chemiluminescent immunoassay technique (qualifier value)"
      },
      {
        "code" : "1259936007",
        "display" : "Enzyme-linked fluorescence assay technique (qualifier value)"
      },
      {
        "code" : "258035006",
        "display" : "High pressure liquid chromatography (qualifier value)"
      },
      {
        "code" : "258036007",
        "display" : "Immunoblotting (qualifier value)"
      },
      {
        "code" : "258037003",
        "display" : "Immunoradiometry (qualifier value)"
      },
      {
        "code" : "258066000",
        "display" : "Polymerase chain reaction technique (qualifier value)"
      },
      {
        "code" : "258075003",
        "display" : "Serotyping (qualifier value)"
      },
      {
        "code" : "258087005",
        "display" : "Agar dilution (qualifier value)"
      },
      {
        "code" : "258099003",
        "display" : "Fluorescence microscopy technique (qualifier value)"
      },
      {
        "code" : "264272003",
        "display" : "Conductivity technique (qualifier value)"
      },
      {
        "code" : "264275001",
        "display" : "Fluorescence polarization immunoassay technique (qualifier value)"
      },
      {
        "code" : "264788002",
        "display" : "Biotyping (qualifier value)"
      },
      {
        "code" : "278289002",
        "display" : "Microscopy technique (qualifier value)"
      },
      {
        "code" : "359838000",
        "display" : "Nephelometry (qualifier value)"
      },
      {
        "code" : "66691000052100",
        "display" : "Electrochemiluminescence immunoassay technique (qualifier value)"
      },
      {
        "code" : "66701000052100",
        "display" : "Fluorescent enzyme immunoassay technique (qualifier value)"
      },
      {
        "code" : "66711000052103",
        "display" : "Line immunoassay technique (qualifier value)"
      },
      {
        "code" : "66721000052106",
        "display" : "Recombinant immunoblot assay technique (qualifier value)"
      },
      {
        "code" : "66731000052108",
        "display" : "Immunochromatographic test technique (qualifier value)"
      },
      {
        "code" : "66741000052102",
        "display" : "Chemiluminescent microparticle immunoassay technique (qualifier value)"
      },
      {
        "code" : "68431000052104",
        "display" : "Enzyme-linked immunosorbent assay technique (qualifier value)"
      },
      {
        "code" : "702660003",
        "display" : "Test strip technique (qualifier value)"
      },
      {
        "code" : "702661004",
        "display" : "Light microscopy technique (qualifier value)"
      },
      {
        "code" : "702873001",
        "display" : "Calculation technique (qualifier value)"
      },
      {
        "code" : "702946003",
        "display" : "Coagulation technique (qualifier value)"
      },
      {
        "code" : "703444002",
        "display" : "Fluorescent immunoassay (qualifier value)"
      },
      {
        "code" : "703445001",
        "display" : "Ion selective electrode measurement technique (qualifier value)"
      },
      {
        "code" : "703447009",
        "display" : "Enzyme immunoassay technique (qualifier value)"
      },
      {
        "code" : "703448004",
        "display" : "Latex agglutination test technique (qualifier value)"
      },
      {
        "code" : "703449007",
        "display" : "Radioimmunoassay technique (qualifier value)"
      },
      {
        "code" : "703450007",
        "display" : "Electrophoresis technique (qualifier value)"
      },
      {
        "code" : "703454003",
        "display" : "Centrifugation technique (qualifier value)"
      },
      {
        "code" : "703458000",
        "display" : "Neutralization method (qualifier value)"
      },
      {
        "code" : "703459008",
        "display" : "Westergren technique (qualifier value)"
      },
      {
        "code" : "703725008",
        "display" : "Culture technique (qualifier value)"
      },
      {
        "code" : "703750006",
        "display" : "Aerobic culture technique (qualifier value)"
      },
      {
        "code" : "703751005",
        "display" : "Anaerobic culture technique (qualifier value)"
      },
      {
        "code" : "703752003",
        "display" : "Organism specific culture technique (qualifier value)"
      },
      {
        "code" : "70521000052109",
        "display" : "Affinity chromatography technique (qualifier value)"
      },
      {
        "code" : "70531000052106",
        "display" : "Agarose gel electrophoresis technique (qualifier value)"
      },
      {
        "code" : "70541000052100",
        "display" : "Chemiluminescence technique (qualifier value)"
      },
      {
        "code" : "70551000052102",
        "display" : "Enzyme-multiplied immunoassay technique (qualifier value)"
      },
      {
        "code" : "70561000052104",
        "display" : "Gas chromatography technique (qualifier value)"
      },
      {
        "code" : "70581000052105",
        "display" : "Capillary electrophoresis technique (qualifier value)"
      },
      {
        "code" : "70591000052107",
        "display" : "Pyrosequencing technique (qualifier value)"
      },
      {
        "code" : "70601000052104",
        "display" : "Real-time polymerase chain reaction technique (qualifier value)"
      },
      {
        "code" : "70611000052102",
        "display" : "Melting curve technique (qualifier value)"
      },
      {
        "code" : "70621000052105",
        "display" : "Spectrophotometric technique (qualifier value)"
      },
      {
        "code" : "708058007",
        "display" : "Flow cytometry technique (qualifier value)"
      },
      {
        "code" : "708061008",
        "display" : "Gram stain technique (qualifier value)"
      },
      {
        "code" : "708062001",
        "display" : "Immunodiffusion technique (qualifier value)"
      },
      {
        "code" : "708063006",
        "display" : "Immunoelectrophoresis technique (qualifier value)"
      },
      {
        "code" : "708064000",
        "display" : "Immunofixation technique (qualifier value)"
      },
      {
        "code" : "708075001",
        "display" : "Potassium hydroxide preparation technique (qualifier value)"
      },
      {
        "code" : "708097004",
        "display" : "Immunohistochemistry technique (qualifier value)"
      },
      {
        "code" : "708099001",
        "display" : "Rapid immunoassay technique (qualifier value)"
      },
      {
        "code" : "708104000",
        "display" : "Agglutination technique (qualifier value)"
      },
      {
        "code" : "708131002",
        "display" : "Anti human globulin test technique, direct (qualifier value)"
      },
      {
        "code" : "708133004",
        "display" : "Complement fixation technique (qualifier value)"
      },
      {
        "code" : "726449005",
        "display" : "Immunoassay technique (qualifier value)"
      },
      {
        "code" : "726748001",
        "display" : "Radioallergosorbent testing technique (qualifier value)"
      },
      {
        "code" : "767095001",
        "display" : "Direct immunofluorescence technique (qualifier value)"
      },
      {
        "code" : "767096000",
        "display" : "Indirect immunofluorescence technique (qualifier value)"
      },
      {
        "code" : "83561000052101",
        "display" : "Photometry technique (qualifier value)"
      },
      {
        "code" : "83581000052107",
        "display" : "Matrix assisted laser desorption ionization time of flight mass spectrometry technique (qualifier value)"
      },
      {
        "code" : "83591000052109",
        "display" : "Particle-enhanced turbidimetric immunoassay technique (qualifier value)"
      },
      {
        "code" : "83601000052101",
        "display" : "Potentiometry technique (qualifier value)"
      },
      {
        "code" : "83611000052104",
        "display" : "Turbidimetry technique (qualifier value)"
      },
      {
        "code" : "1304095001",
        "display" : "Refractometry (qualifier value)"
      },
      {
        "code" : "1304230000",
        "display" : "Viscometry (qualifier value)"
      },
      {
        "code" : "1304094002",
        "display" : "X-ray diffraction (qualifier value)"
      }]
    }]
  }
}

```

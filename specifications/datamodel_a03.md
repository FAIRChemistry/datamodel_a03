# CRC 1333 project A03, Lotsch group

This data model describes a COF preparation including information about chemical entities and the experimental procedure. Preliminary specifications according to the example PDF provided.

### Report

Defines a COF preparation by the products, reactants, reagents, and solvents used, as well as the experimental procedure itself. Preliminary specification according to the example PDF provided.

- __id*__
  - Type: string
  - Description: Unique identifier for the report
- __products__
  - Type: Compound
  - Multiple: True
  - Description: List of products resulting from the COF preparation
- __reactants__
  - Type: Compound
  - Multiple: True
  - Description: List of reactants that were used in the COF preparation
- __reagents__
  - Type: Compound
  - Multiple: True
  - Description: List of reagents that were used in the COF preparation
- __solvents__
  - Type: Compound
  - Multiple: True
  - Description: List of solvents that were used in the COF preparation
- __procedures__
  - Type: Procedure
  - Multiple: True
  - Description: List of procedures that were applied to the COF preparation
- __observations__
  - Type: string
  - Description: Free text for noting observations during the COF preparation
- __analyses__
  - Type: Analysis
  - Multiple: True
  - Description: Analyses that were performed for the COF preparation

### Compound

Describes a chemical compound. Preliminary specification according to the example PDF provided.

- __id*__
  - Type: string
  - Description: Unique identifier for the compound
- __name*__
  - Type: string
  - Description: Descriptive name of the compound
- __inchi__
  - Type: string
  - Description: InChI code that uniquely identifies the structure of a molecule
- __cas_number__
  - Type: string
  - Description: A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature.
- __quantity__
  - Type: string
  - Description: Quantity of compound (N, m, V, ...)
- __amount__
  - Type: posfloat
  - Description: Amount of the quantity of compound (numerical value)
- __unit__
  - Type: string
  - Description: Unit of the quantity of compound (SI unit)

### Procedure

Describes a procedure that was applied for a particular part of the COF preparation or the preparation as whole. Preliminary specification according to the example PDF provided.

- __id*__
  - Type: string
  - Description: Unique identifier for the procedure
- __name*__
  - Type: string
  - Description: Descriptive name of the method (e.g. work-up)
- __steps*__
  - Type: Step
  - Multiple: True
  - Description: Independent steps that make up the procedure
- __reference__
  - Type: string
  - Description: Reference to the original publication from which the method was adapted from.

### Step

Describes a part of a procedure through free text and optionally an associated analysis. Preliminary specification according to the example PDF provided.

- __description*__
  - Type: string
  - Description: Free text description of the step
- __analysis__
  - Type: Analysis
  - Description: Analysis performed in the step

### Analysis

Describes an anlysis that was performed for the COF preparation. Preliminary specification according to the example PDF provided.

- __id*__
  - Type: string
  - Description: Unique identifier for the analysis
- __name*__
  - Type: string
  - Description: Descriptive name of the analysis
- __location*__
  - Type: string
  - Description: Location were the results of the analysis can be retrieved


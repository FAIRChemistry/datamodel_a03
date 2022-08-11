# Lotsch

This data model describes a chemical process including information about chemical entities as well as their relationship to methods.

### Report

Reports on a chemical experiment, that includes Reactants and Reactants as well as the method. The Data model will natively be exported to the AnIML data format used to track data from analytical instruments.

- __reagents__
  - Type: Molecule
  - Multiple: True
  - Description: List of reagents that were used in the experiment
- __reactants__
  - Type: Molecule
  - Multiple: True
  - Description: List of reactants that were used in the experiment
- __measurements__
  - Type: Measurement
  - Multiple: True
  - Description: All measurements that were conducted in an experiment
- __methods__
  - Type: Method
  - Multiple: True
  - Description: Methods that were used in this experiment

### Molecule

Describes a molecule according to the PDF

- __id__
  - Type: string
  - Description: Unique identifier for a molecule/stock
- __inchi__
  - Type: string
  - Description: InChI code that uniquely identifies the structure of a molecule
- __cas_number__
  - Type: string
  - Description: A CAS Registry Number also referred to as CAS RN or informally CAS Number, is a unique numerical identifier assigned by the Chemical Abstracts Service (CAS), US to every chemical substance described in the open scientific literature.
- __used_mass__
  - Type: posfloat
  - Description: Mass that was weighed in and used in the experiment.

### Measurement

Describes a measurement that was made in a chemical experiment.

- __entry_id__
  - Type: string
  - Description: Unique identifier of the measurement
- __product_yield__
  - Type: posfloat
  - Description: Documented yield in mg

### Method

Describes a workflow that was done for a particular part of the experiment or the complete

- __name__
  - Type: string
  - Description: Name of the method (e.g. Preparation)
- __steps__
  - Type: Step
  - Multiple: True
  - Description: Steps that make up the procedure
- __reference__
  - Type: string
  - Description: Reference to the original publication from which the method was adapted from.

### Step

Describes a part of a workflow that includes free text description as well as parameters that were 

- __description__
  - Type: string
  - Description: Free text description of the step
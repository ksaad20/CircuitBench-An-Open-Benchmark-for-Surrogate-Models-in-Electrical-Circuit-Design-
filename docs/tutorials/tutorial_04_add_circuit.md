# Tutorial 04: Adding Your First Circuit

## Overview

This tutorial demonstrates how to add a new circuit to Circuit-Bench. A well-documented circuit should be reproducible, validated, and accompanied by sufficient metadata to enable benchmarking and reuse.

By the end of this tutorial, you will understand how to organize circuit files, document their provenance, validate their integrity, and prepare them for benchmarking.

---

# Learning Objectives

After completing this tutorial, you will be able to:

* Create a circuit directory.
* Organize circuit files.
* Document circuit metadata.
* Record licensing and citations.
* Validate circuit assets.
* Prepare a circuit for benchmark tasks.

---

# Prerequisites

Before starting, ensure that you have:

* Installed Circuit-Bench.
* Completed the previous tutorials.
* Reviewed the "Adding Circuits" developer guide.
* Selected a circuit that you are permitted to contribute.

---

# Step 1: Choose a Circuit Category

Place the circuit in the appropriate category.

Examples include:

* Analog
* Digital
* RF
* Power Electronics
* Passive
* Mixed-Signal

Choose the category that best represents the primary purpose of the circuit.

---

# Step 2: Create the Directory Structure

Create a directory for your circuit.

Example:

```text
circuits/
└── analog/
    └── cmos_inverter/
        ├── README.md
        ├── metadata.yaml
        ├── LICENSE
        ├── citation.bib
        ├── schematic.png
        ├── netlist.spice
        ├── simulation/
        ├── waveforms/
        ├── validation/
        ├── preprocessing.md
        ├── tasks.md
        └── statistics.json
```

This structure separates documentation, source files, simulation artifacts, and validation resources.

---

# Step 3: Add Circuit Documentation

Create a `README.md` describing:

* Circuit name
* Purpose
* Category
* Source
* Version
* Supported simulators
* Directory contents
* Usage notes

The README should provide enough information for another researcher to understand and use the circuit.

---

# Step 4: Record Metadata

Create a `metadata.yaml` file containing information such as:

* Circuit name
* Version
* Category
* Technology
* Source
* License
* Maintainer
* Supported benchmark tasks
* Date added

Metadata improves discoverability and reproducibility.

---

# Step 5: Add Source Files

Include the files needed to reproduce the circuit.

Depending on the design, these may include:

* SPICE netlists
* Verilog
* Verilog-A
* VHDL
* Schematic files
* Layout files
* Simulation configurations

Only include files that are permitted by the applicable license.

---

# Step 6: Add Licensing and Citation

Include:

* A `LICENSE` file or reference to the official license.
* A `citation.bib` file for published circuits or reference designs.

Always credit the original source.

---

# Step 7: Validate the Circuit

Before adding the circuit to the repository, verify:

* All required files are present.
* Metadata is complete.
* Source files are valid.
* Simulation inputs are available.
* Documentation is complete.

---

# Step 8: Document Benchmark Tasks

In `tasks.md`, describe how the circuit can be used.

Possible tasks include:

* Classification
* Fault diagnosis
* Simulation
* Parameter estimation
* Timing analysis
* Power estimation

---

# Step 9: Prepare Validation Artifacts

Store validation materials in the `validation/` directory.

Examples include:

* Expected outputs
* Validation reports
* Reference waveforms
* Simulation logs

These artifacts support reproducibility and quality assurance.

---

# Best Practices

* Use descriptive names.
* Preserve original circuit information.
* Keep metadata complete.
* Document simulator compatibility.
* Cite original authors.
* Avoid unnecessary binary files.
* Maintain a consistent directory structure.

---

# Troubleshooting

Common issues include:

* Missing metadata
* Invalid netlists
* Incomplete documentation
* Missing licenses
* Unsupported simulator formats

Review validation results before submitting new circuits.

---

# Next Steps

After successfully adding a circuit, consider:

* Adding additional benchmark tasks.
* Including reference simulation results.
* Expanding documentation.
* Contributing example workflows.
* Comparing results across benchmark datasets.

---

# Summary

In this tutorial, you learned how to:

* Organize circuit files.
* Document metadata.
* Record licensing and citations.
* Validate circuit assets.
* Prepare circuits for benchmarking.

These practices help ensure that Circuit-Bench remains a reproducible, extensible, and high-quality benchmark repository for the circuit research community.

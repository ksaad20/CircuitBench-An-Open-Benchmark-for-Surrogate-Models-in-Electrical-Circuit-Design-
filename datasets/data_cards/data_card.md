# Dataset Card

## Dataset Name

Data Cards

---

## Version

v1.0.0

---

## Description

The **Data Cards** dataset is a collection of standardized dataset documentation files used throughout Circuit-Bench. Rather than containing raw experimental data, this dataset provides structured metadata describing datasets, benchmarks, simulation collections, and evaluation resources. Each data card documents a dataset's purpose, provenance, contents, licensing, intended use, and limitations to improve transparency and reproducibility.

---

## Purpose

The Data Cards collection aims to:

- Standardize dataset documentation
- Improve dataset discoverability
- Support reproducible research
- Document benchmark provenance
- Facilitate FAIR data practices
- Help contributors understand available datasets
- Encourage responsible dataset use

---

## Domain

- Electronic Design Automation (EDA)
- Circuit Benchmarking
- Analog Electronics
- Digital Electronics
- Mixed-Signal Design
- RF Engineering
- Power Electronics
- Scientific Computing
- Machine Learning for Circuits

---

## Contents

Each data card may include:

- Dataset name
- Version
- Description
- Purpose
- Source
- Collection methodology
- Data format
- Directory structure
- Intended use
- Limitations
- Evaluation metrics
- Citation information
- License
- Maintainers
- Changelog

---

## Supported Dataset Categories

Examples include:

- Analog Circuits
- Digital Circuits
- Passive Components
- Active Components
- RF Circuits
- Power Electronics
- SPICE Tests
- APIs
- Benchmarks
- Netlists
- Waveforms
- Schematics
- DOIs
- Publications
- Educational Resources

---

## File Formats

Typical files include:

- `.md`
- `.yaml`
- `.json`
- `.csv`

---

## Directory Structure

```text
data_cards/
├── analog_dataset_card.md
├── digital_dataset_card.md
├── passive_dataset_card.md
├── active_dataset_card.md
├── rf_dataset_card.md
├── power_electronics_dataset_card.md
├── spice_tests_dataset_card.md
├── api_examples_dataset_card.md
├── dois_dataset_card.md
├── publications_dataset_card.md
└── README.md
```

---

## Applications

The Data Cards collection supports:

- Dataset documentation
- Repository organization
- Research reproducibility
- Benchmark transparency
- Contributor onboarding
- Metadata management
- Scientific publishing
- FAIR data implementation

---

## Quality Criteria

Each data card should provide:

- Complete metadata
- Clear dataset description
- Version information
- Licensing details
- Citation guidance
- Intended use
- Known limitations
- Contact information

---

## Limitations

- Data cards describe datasets but do not contain the datasets themselves.
- Metadata accuracy depends on contributor updates.
- External datasets may evolve independently of their documentation.

---

## Reproducibility

Every documented dataset should specify:

- Version
- Source
- License
- Citation
- Collection methodology
- File formats
- Directory organization
- Relevant benchmark or publication

---

## FAIR Compliance

The Data Cards collection promotes:

- **Findability** through standardized metadata
- **Accessibility** via clear documentation
- **Interoperability** using consistent formats
- **Reusability** through comprehensive dataset descriptions

---

## Citation

If you use the Data Cards collection, please cite the associated Circuit-Bench publication and repository. Individual datasets should also be cited according to their own documentation.

---

## License

Specify the applicable license (e.g., MIT, Apache-2.0, CC BY 4.0).

---

## Maintainers

Circuit-Bench Contributors

---

## Contact

Please open an issue or discussion in the repository for questions, corrections, or contributions.

---

## Changelog

### v1.0.0

- Initial release of standardized dataset documentation
- Added support for benchmark-specific dataset cards
- Established a consistent metadata template for Circuit-Bench datasets

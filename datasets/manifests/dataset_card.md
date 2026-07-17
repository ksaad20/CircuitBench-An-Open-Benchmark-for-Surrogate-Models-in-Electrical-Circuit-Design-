# Dataset Card: Manifests

## Dataset Name
**Manifests**

---

# Overview

The **Manifests** dataset consists of machine-readable manifest files that describe the structure, contents, metadata, and integrity information of benchmark datasets used throughout CircuitBench. These manifests provide a standardized interface for dataset discovery, validation, indexing, reproducibility, and automated tooling.

Rather than storing benchmark data directly, manifests describe the datasets and their associated resources.

---

# Purpose

This dataset supports:

- Dataset discovery
- Automatic dataset registration
- Dataset validation
- Version tracking
- Integrity verification
- Reproducible benchmarking
- Metadata standardization
- Continuous Integration (CI) pipelines
- API-driven dataset loading

---

# Scope

The manifests describe datasets across multiple benchmark categories, including:

- Analog circuits
- Digital circuits
- RF circuits
- Passive components
- Active components
- Power electronics
- Mixed-signal circuits
- Device models
- Simulation datasets
- Educational examples
- Research benchmarks

---

# Dataset Structure

Typical directory layout:

```text
datasets/
└── manifests/
    ├── analog.yaml
    ├── digital.yaml
    ├── rf.yaml
    ├── power.yaml
    ├── passive.yaml
    ├── active.yaml
    ├── mixed_signal.yaml
    ├── devices.yaml
    ├── educational.yaml
    └── research.yaml
```

Each manifest references one or more benchmark datasets.

---

# Manifest Fields

Typical fields include:

| Field | Description |
|---------|-------------|
| dataset_name | Dataset identifier |
| version | Dataset version |
| category | Benchmark category |
| description | Dataset summary |
| authors | Dataset contributors |
| license | License information |
| source | Original source |
| doi | DOI (if available) |
| citation | Citation text |
| homepage | Dataset homepage |
| download_url | Download location |
| checksum | Integrity hash |
| file_format | Data format |
| file_size | Dataset size |
| num_samples | Number of samples |
| labels | Available labels |
| tasks | Supported benchmark tasks |
| dependencies | Required software |
| created | Creation date |
| updated | Last modification |
| tags | Search keywords |

---

# Supported Formats

Manifest files may use:

- YAML
- JSON
- TOML

depending on repository configuration.

---

# Metadata Standard

Metadata follows principles from:

- FAIR
- Dublin Core
- DataCite
- RO-Crate
- Schema.org Dataset
- OpenML metadata conventions

---

# Intended Use

These manifests are intended for:

- Repository indexing
- Dataset validation
- Automated downloads
- Benchmark orchestration
- CI workflows
- Dataset discovery
- Documentation generation
- API integration
- Reproducible experiments

---

# Not Intended For

The manifests are **not** intended to:

- Store benchmark data directly
- Replace original datasets
- Serve as simulation outputs
- Contain executable code
- Replace dataset documentation

---

# Data Source

Manifest metadata may originate from:

- Repository maintainers
- Public benchmark repositories
- Original publications
- Dataset providers
- Community contributions

---

# Collection Process

Metadata is collected through:

- Manual curation
- Automated indexing
- CI validation
- Repository synchronization
- Community submissions

---

# Quality Assurance

Each manifest should undergo:

- Schema validation
- Metadata completeness checks
- Link verification
- Checksum verification
- Duplicate detection
- Version consistency validation
- CI testing

---

# Benchmark Tasks

Supported tasks include:

- Circuit classification
- Parameter prediction
- Fault detection
- Simulation benchmarking
- Symbol recognition
- Device modeling
- Netlist analysis
- Graph learning
- Timing analysis
- Analog optimization

---

# File Integrity

Integrity may be verified using:

- SHA-256
- SHA-512
- MD5 (legacy support)

---

# Versioning

Manifest versioning follows Semantic Versioning.

Example:

```text
1.0.0
1.1.0
2.0.0
```

---

# Update Policy

Manifests are updated when:

- New datasets are added
- Metadata changes
- Dataset versions change
- URLs are updated
- Integrity hashes change
- Licensing changes

---

# Licensing

Each referenced dataset retains its original license.

The manifest metadata itself is distributed under the repository license unless otherwise specified.

---

# Citation

If using a benchmark referenced by these manifests, cite:

1. The original dataset publication
2. The CircuitBench repository
3. Any associated benchmark publication

---

# Limitations

Possible limitations include:

- Missing metadata
- Broken external links
- Legacy datasets
- Incomplete citations
- Third-party licensing constraints
- External repository availability

---

# Ethical Considerations

Users should:

- Respect dataset licenses
- Cite original creators
- Verify metadata accuracy
- Avoid misuse of benchmark data
- Report metadata errors

---

# Maintenance

Maintained by the CircuitBench contributors.

Community pull requests for metadata improvements are encouraged.

---

# Contact

Please open a GitHub Issue or Pull Request for:

- Incorrect metadata
- Broken download links
- Missing citations
- Version updates
- New dataset registration

---

# Changelog

| Version | Changes |
|----------|----------|
| 1.0.0 | Initial manifest dataset card |
```

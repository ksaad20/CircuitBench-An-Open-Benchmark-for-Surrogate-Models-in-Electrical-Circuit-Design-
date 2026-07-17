# Dataset Card: Dataset Versions

## Overview

The `datasets/versions/` folder contains versioned releases of datasets used in Circuit-Bench. Each version represents a reproducible snapshot of a dataset at a specific point in time, allowing researchers to reproduce published benchmark results and compare model performance across consistent dataset releases.

---

## Purpose

Versioned datasets ensure:

- Reproducibility of benchmarking experiments
- Stable references for academic publications
- Transparent tracking of dataset evolution
- Compatibility with historical benchmark results
- Controlled introduction of new circuits and annotations

---

## Intended Applications

These dataset versions are suitable for:

- Circuit benchmarking
- Machine learning model evaluation
- Regression testing
- Academic reproducibility
- Benchmark competitions
- Performance comparison across software versions

---

## Dataset Organization

Typical contents may include:

```
versions/
├── v1.0/
├── v1.1/
├── v2.0/
├── latest/
└── CHANGELOG.md
```

Each version may contain:

- Circuit files
- Labels
- Metadata
- Documentation
- Checksums
- License information

---

## Versioning Policy

Circuit-Bench follows semantic versioning where appropriate.

### Major Version

Breaking changes such as:

- Dataset restructuring
- Label modifications
- File format changes

Example:

```
v2.0
```

### Minor Version

Backward-compatible additions:

- New circuits
- Additional metadata
- Improved annotations

Example:

```
v2.1
```

### Patch Version

Small corrections:

- Metadata fixes
- Typographical corrections
- Documentation updates

Example:

```
v2.1.1
```

---

## Reproducibility

Researchers are encouraged to:

- Cite the exact dataset version used.
- Archive benchmark results alongside version information.
- Record software versions and random seeds.

---

## Quality Assurance

Each release should undergo:

- Integrity verification
- Duplicate detection
- Schema validation
- Metadata validation
- Manual inspection
- Automated consistency checks

---

## Metadata

Each version should include metadata describing:

- Dataset version
- Release date
- Contributors
- License
- Source
- Number of circuits
- Number of tasks
- File formats
- Known limitations

---

## Recommended Citation

When publishing results, cite both:

1. Circuit-Bench
2. The exact dataset version

Example:

```
Circuit-Bench Dataset v1.0
```

---

## Limitations

Dataset versions may differ in:

- Circuit count
- Supported benchmark tasks
- Annotation quality
- Metadata completeness

Researchers should avoid comparing results across different versions without acknowledging these differences.

---

## Future Releases

Future versions may include:

- Additional analog circuits
- Digital benchmark expansion
- RF and microwave circuits
- Power electronics benchmarks
- Mixed-signal datasets
- Improved annotations
- Standardized metadata
- Larger benchmark suites

---

## License

Refer to the repository LICENSE and the license accompanying each dataset version.

---

## Contact

Issues, corrections, and version suggestions are welcome through the Circuit-Bench GitHub repository.

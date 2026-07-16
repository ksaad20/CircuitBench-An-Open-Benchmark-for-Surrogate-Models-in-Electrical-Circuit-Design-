# Circuit-Bench Benchmark Manifest

## Version

Circuit-Bench v1.0

Release date: 16.07.2026
DOI: 10.5281/zenodo.21387582
Git commit: git add docs/benchmark_specification.md README.md
git commit -m "Add formal benchmark specification for Circuit-Bench v1.0"
git push origin main

## Benchmark Scope

Circuit-Bench v1.0 provides a standardized benchmark for evaluating AI methods on electrical circuit analysis, optimization, surrogate modelling, and fault diagnosis using curated benchmark circuits and reproducible evaluation protocols.

## Benchmark Coverage

Each benchmark circuit should contain, where applicable:

- Circuit identifier
- Category
- Application domain
- Simulation model
- Input variables
- Output variables
- Ground-truth reference
- Evaluation task(s)
- Performance metrics
- Metadata

## Circuit Categories

Circuit-Bench v1.0 currently includes benchmark circuits from the following categories.

| Category | Included | Primary Applications | Example Circuits | Status |
|----------|----------|----------------------|------------------|--------|
| Analog | Yes | Signal conditioning, amplification | Operational amplifiers, active filters | Stable |
| Digital | Yes | Logic design and verification | Logic gates, combinational circuits, sequential circuits | Stable |
| Passive | Yes | Network analysis | RLC circuits, RC filters, RL networks | Stable |
| Power Electronics | Yes | Energy conversion | Buck converters, boost converters, buck-boost converters | Stable |
| RF | Yes | High-frequency analysis | Matching networks, resonant circuits | Experimental |
| Mixed-Signal | Planned | Analog–digital integration | ADCs, DACs | Future Release |
| Timing Analysis | Planned | Delay estimation | Timing benchmark circuits | Future Release |
| Fault Diagnosis | Yes | AI benchmarking | Open-circuit, short-circuit, component failure cases | Stable |

### Category Selection Criteria

Circuit categories are selected based on their importance in electrical engineering education, industrial design workflows, and AI-assisted circuit analysis. Each benchmark category contains representative circuits intended to evaluate machine learning algorithms under reproducible conditions.

## Exclusion Criteria

The following are excluded from Circuit-Bench:

- Incomplete circuit descriptions
- Proprietary circuits without redistribution rights
- Non-reproducible simulation results
- Circuits lacking benchmark metadata
- Duplicate benchmark instances

## Benchmark Tasks

## Dataset Inventory

## Metrics

## Baseline Models

## Supported Simulators

## Repository Structure

## Reproducibility

## Version Policy

Benchmark versions are immutable.

Version updates may introduce:

- additional benchmark circuits
- new benchmark tasks
- new metrics
- additional simulators

Existing benchmark identifiers and published benchmark results remain reproducible across releases whenever possible.

## Citation

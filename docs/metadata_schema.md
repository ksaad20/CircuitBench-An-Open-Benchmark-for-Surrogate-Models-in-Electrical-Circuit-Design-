# Circuit-Bench Metadata Schema

This document defines the mandatory metadata required for every benchmark circuit included in Circuit-Bench.

The purpose of this schema is to ensure reproducibility, discoverability, interoperability and standardized evaluation across benchmark releases.

## Required Metadata Fields

| Field | Required | Description |
|--------|----------|-------------|
| Circuit ID | Yes | Unique benchmark identifier |
| Circuit Name | Yes | Human-readable name |
| Category | Yes | Analog, Digital, RF, Power, Passive, etc. |
| Benchmark Task | Yes | Performance prediction, optimisation, etc. |
| Difficulty | Yes | Easy, Medium, Hard |
| Simulator | Yes | ngspice, PySpice, etc. |
| Input Variables | Yes | Benchmark inputs |
| Output Variables | Yes | Ground-truth outputs |
| Ground Truth | Yes | Reference solution |
| Units | Yes | Physical units |
| License | Yes | Usage license |
| Source | Yes | Literature or generated |
| Version | Yes | Benchmark version |

## Difficulty Levels

Easy

- Introductory benchmark
- Small circuit
- Low simulation complexity

Medium

- Multiple interacting components
- Moderate simulation time

Hard

- Complex topology
- Large parameter space
- High computational cost

## Circuit Identifier Format

Circuit identifiers follow

CB-<CATEGORY>-<NUMBER>

Examples

CB-ANA-001

CB-DIG-015

CB-PWR-023

CB-RF-004

CB-PAS-012

## Metadata Validation Rules

Every benchmark circuit must satisfy the following:

- Unique identifier
- Valid category
- Defined benchmark task
- Simulator specified
- Units documented
- Ground truth available
- Version recorded
- License specified

## Example Metadata Record

| Field | Value |
|--------|------|
| Circuit ID | CB-ANA-001 |
| Circuit Name | Active Low-Pass Filter |
| Category | Analog |
| Benchmark Task | Performance Prediction |
| Difficulty | Medium |
| Simulator | ngspice |
| Input Variables | Frequency |
| Output Variables | Gain |
| Ground Truth | SPICE simulation |
| Units | Hz, dB |
| License | Apache-2.0 |
| Source | Circuit-Bench |
| Version | v1.0 |

## Metadata Governance

Metadata changes are version controlled.

Published benchmark metadata must remain stable across releases unless a documented correction is required.

Deprecated metadata records remain archived for reproducibility.

git commit: git add docs/metadata_schema.md
git commit -m "Define standardized metadata schema for Circuit-Bench"
git push origin main

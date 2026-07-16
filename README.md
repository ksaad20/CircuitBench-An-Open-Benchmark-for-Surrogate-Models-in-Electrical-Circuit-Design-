# Circuit Bench - Benchmarking and evaluation standard for artificial intelligence driven electrical circuit design

![License](https://img.shields.io/github/license/ksaad20/Circuit-Bench)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![Black](https://img.shields.io/badge/code%20style-black-000000)
![Ruff](https://img.shields.io/badge/linter-ruff-red)
[![Tests](https://github.com/ksaad20/Circuit-Bench/actions/workflows/ci.yml/badge.svg)](https://github.com/ksaad20/Circuit-Bench/actions/workflows/ci.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21387582.svg)](https://doi.org/10.5281/zenodo.21387582)

## Architecture

![CircuitBench Architecture](docs/images/architecture.png)

Circuit Bench is an open benchmark designed to become the standard evaluation platform for artificial intelligence methods in electrical circuit design.

Circuit Bench is an open-source benchmark designed to provide a standardized platform for evaluating machine learning algorithms in electrical circuit analysis, optimization, and surrogate modeling. The project addresses the lack of a unified evaluation framework for AI-driven electrical engineering design by integrating reproducible circuit simulations, curated datasets, standardized performance metrics, and reference implementations of state-of-the-art machine learning models.

The benchmark contains a diverse collection of analog, digital, power electronic, RF, and passive circuit topologies simulated using open-source SPICE engines. Each circuit is evaluated under extensive parameter sweeps to generate high-quality datasets describing electrical behavior, including voltage, current, frequency response, transient response, efficiency, power dissipation, stability, and harmonic distortion.

Why Circuit Bench?

Current AI models for electrical circuit design are evaluated on different datasets, simulators, circuits, and metrics, making fair comparison difficult. Circuit Bench establishes a unified, reproducible, and extensible benchmark for objective evaluation across machine learning methods and engineering tasks.

CircuitBench enables researchers to compare machine learning models for a wide range of electrical engineering tasks, including:

1. Circuit performance prediction
2. Component parameter estimation
3. Automatic circuit optimization
4. Fault diagnosis
5. Sensitivity analysis
6. Surrogate modeling for accelerated simulation
7. Explainable artificial intelligence in circuit design

The framework supports both classical machine learning and modern deep learning approaches, allowing direct comparison between algorithms such as:

1. Linear Regression
2. Random Forest
3. Gradient Boosting
4. XGBoost
5. CatBoost
6. Support Vector Regression
7. Artificial Neural Networks
8. Graph Neural Networks
9. Physics-Informed Neural Networks
10. Gaussian Process Regression

Each algorithm is evaluated using standardized regression and classification metrics together with engineering-specific criteria, including prediction accuracy, computational efficiency, inference latency, robustness, calibration, uncertainty estimation, and interpretability.

CircuitBench emphasizes complete reproducibility through open datasets, executable notebooks, automated simulation pipelines, Docker environments, and transparent evaluation protocols.

The long-term goal of CircuitBench is to establish a community benchmark analogous to ImageNet for computer vision or GLUE for natural language processing, enabling rigorous and reproducible comparison of artificial intelligence methods for electrical engineering design.

Benchmark Suites

1. CircuitBench-Core

i. Passive circuits
ii. RLC networks
iii. Resonance
iv. Filters

2. CircuitBench-Analog

i. Operational amplifiers
ii. Oscillators
iii. Instrumentation amplifiers
iv. Active filters

3. CircuitBench-Digital

i. CMOS logic
ii. Timing analysis
iii. Noise margin
iv. Propagation delay

4. CircuitBench-Power

i. DC–DC converters
ii. Inverters
iii. Battery management circuits
iv. Motor drives

5. CircuitBench-RF

i. Matching networks
ii. Amplifiers
iii. Transmission lines
iv. Antennas

6. CircuitBench-Fault

i. Open circuits
ii. Short circuits
iii. Component degradation
iv. Sensor failures

7. CircuitBench-XAI

i. SHAP
ii. LIME
iii. Feature importance
iv. Uncertainty estimation

## Quick Start

Clone the repository

```bash
git clone https://github.com/ksaad20/Circuit-Bench.git
cd Circuit-Bench


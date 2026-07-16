# Circuit-Bench Official Benchmark Experiments


## Objective

The objective of the official benchmark experiments is to establish reproducible baseline performance for all benchmark tasks included in Circuit-Bench.

## Official Experiments

| Experiment ID | Task | Dataset | Baseline Models |
|---------------|------|---------|-----------------|
| EXP-001 | Performance Prediction | Analog | Linear Regression, Random Forest, XGBoost |
| EXP-002 | Component Estimation | Analog | Linear Regression, Random Forest, XGBoost |
| EXP-003 | Fault Diagnosis | Digital | Random Forest, SVM, MLP |
| EXP-004 | Circuit Optimization | Power | Random Forest, XGBoost |
| EXP-005 | Surrogate Modelling | Passive | MLP, Random Forest |

## Standard Evaluation Metrics

- MAE
- RMSE
- R²
- Runtime
- Peak Memory

## Required Repetitions

Each experiment should be repeated a minimum of three independent times using fixed random seeds.

Git Commit: Define official benchmark experiments

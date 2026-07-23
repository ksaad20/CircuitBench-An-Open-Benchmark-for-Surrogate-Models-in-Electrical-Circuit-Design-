---
name: Performance Issue
about: Report slow execution, excessive memory usage, scalability problems, or benchmarking performance regressions in Circuit Bench.
title: "[PERFORMANCE]: "
labels: ["performance", "triage"]
assignees: []
---

# Performance Issue

Thank you for reporting a performance issue. Detailed reports help us improve the efficiency, scalability, and reliability of Circuit Bench.

---

## Summary

Provide a brief description of the performance problem.

---

## Type of Performance Issue

Select all that apply.

- [ ] Slow execution
- [ ] High memory usage
- [ ] CPU bottleneck
- [ ] GPU bottleneck
- [ ] Disk I/O bottleneck
- [ ] Long benchmark runtime
- [ ] Performance regression
- [ ] Poor scalability
- [ ] Startup time
- [ ] CLI responsiveness
- [ ] Visualization performance
- [ ] Other

---

## Expected Performance

Describe the expected behavior or performance.

---

## Actual Performance

Describe the observed behavior.

Include measurements whenever possible.

---

## Steps to Reproduce

1.
2.
3.
4.

---

## Benchmark or Component

Which part of Circuit Bench is affected?

Examples:

- Benchmark Runner
- CLI
- Dataset Loader
- Visualization
- Metrics
- Reporting
- API
- Other

---

## Performance Measurements

If available, provide measurements.

| Metric | Expected | Actual |
|---------|---------:|-------:|
| Runtime | | |
| Memory Usage | | |
| CPU Usage | | |
| GPU Usage | | |
| Disk Usage | | |
| Other | | |

---

## Benchmark Configuration

If applicable, provide:

- Benchmark name:
- Dataset:
- Number of samples:
- Number of iterations:
- Random seed:
- Parallel workers:
- Configuration options:

---

## Environment

### Operating System

- [ ] Windows
- [ ] macOS
- [ ] Linux
- [ ] Other

Operating System Version:

---

### Python Version

```text
Python version
```

---

### Circuit Bench Version

```text
Version
```

---

### Hardware

CPU:

RAM:

GPU (if applicable):

Storage:

---

## Profiling Results (Optional)

If you profiled the application, include the results.

Examples:

- cProfile
- py-spy
- line_profiler
- perf
- flame graphs

```text
Paste profiling output here.
```

---

## Logs

Include any relevant logs or terminal output.

```text
Paste logs here.
```

---

## Additional Context

Include screenshots, benchmark reports, plots, or any additional information that may help diagnose the issue.

---

# Checklist

Please confirm the following before submitting.

- [ ] I searched existing issues before creating this report.
- [ ] I can consistently reproduce this performance issue.
- [ ] I included benchmark measurements where possible.
- [ ] I provided my environment information.
- [ ] I included relevant logs or profiling data if available.
- [ ] I have removed any sensitive or confidential information.

---

Thank you for helping improve the performance and scalability of **Circuit Bench**. Well-documented performance reports help ensure the project remains fast, efficient, and reproducible across diverse hardware and workloads.

"""
Run all dataset validation routines.
"""

from validate_checksums import validate_checksums
from validate_dataset import validate_dataset
from validate_metadata import validate_metadata

print("=" * 60)
print("CircuitBench Dataset Validation")
print("=" * 60)

results = [
    validate_dataset(),
    validate_metadata(),
    validate_checksums(),
]

print("=" * 60)

if all(results):
    print("All dataset validation checks passed.")
else:
    print("Dataset validation failed.")

print("=" * 60)

"""
Tests for CircuitBench explainability utilities.
"""

import pandas as pd
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor

from src.explainability.ice import (
    ICEPlots,
)
from src.explainability.partial_dependence import (
    PartialDependence,
)
from src.explainability.permutation_importance import (
    PermutationImportance,
)


def create_model():
    X, y = make_regression(
        n_samples=200,
        n_features=6,
        random_state=42,
    )

    X = pd.DataFrame(
        X,
        columns=[f"Feature_{i}" for i in range(6)],
    )

    model = RandomForestRegressor(
        random_state=42,
        n_estimators=50,
    )

    model.fit(
        X,
        y,
    )

    return model, X, y


def test_permutation_importance():
    model, X, y = create_model()

    result = PermutationImportance.compute(
        model,
        X,
        y,
        n_repeats=5,
    )

    assert len(result.feature_names) == X.shape[1]
    assert result.importances_mean.shape[0] == X.shape[1]

    df = PermutationImportance.to_dataframe(result)

    assert not df.empty


def test_partial_dependence():
    model, X, _ = create_model()

    result = PartialDependence.compute(
        model,
        X,
        [0],
    )

    assert result is not None


def test_partial_dependence_plot():
    model, X, _ = create_model()

    fig, ax = PartialDependence.plot(
        model,
        X,
        [0],
    )

    assert fig is not None
    assert ax is not None


def test_two_way_partial_dependence():
    model, X, _ = create_model()

    fig, _ = PartialDependence.two_way(
        model,
        X,
        (0, 1),
    )

    assert fig is not None


def test_ice():
    model, X, _ = create_model()

    values, curves = ICEPlots.compute(
        model,
        X,
        feature=0,
    )

    assert len(values) > 0
    assert curves.shape[0] == len(X)


def test_ice_plot():
    model, X, _ = create_model()

    fig, ax = ICEPlots.plot(
        model,
        X,
        feature=0,
    )

    assert fig is not None
    assert ax is not None


def test_importance_dataframe():
    model, X, y = create_model()

    result = PermutationImportance.compute(
        model,
        X,
        y,
        n_repeats=3,
    )

    df = PermutationImportance.to_dataframe(result)

    assert "feature" in df.columns
    assert "importance" in df.columns

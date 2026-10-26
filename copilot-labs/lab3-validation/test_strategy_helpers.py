import numpy as np
import pandas as pd
import pytest

from strategy_helpers import add_strategy_features, build_segment_calibration


def test_add_strategy_features_computes_expected_columns() -> None:
    df = pd.DataFrame(
        {
            "utilization": [0.8, 0.2, np.nan],
            "tenure_months": [3, 9, 0],
            "risk_band": ["Subprime", "Prime", "Subprime"],
        }
    )

    out = add_strategy_features(df)

    assert "util_to_tenure" in out.columns
    assert "high_util_subprime" in out.columns
    assert out["util_to_tenure"].iloc[0] == pytest.approx(0.8 / 4)
    assert out["util_to_tenure"].iloc[1] == pytest.approx(0.2 / 10)
    assert np.isnan(out["util_to_tenure"].iloc[2])
    assert out["high_util_subprime"].tolist() == [1, 0, 0]
    assert "util_to_tenure" not in df.columns
    assert "high_util_subprime" not in df.columns


def test_add_strategy_features_missing_columns_raises() -> None:
    df = pd.DataFrame({"utilization": [0.1], "risk_band": ["Prime"]})
    with pytest.raises(ValueError):
        add_strategy_features(df)


def test_build_segment_calibration_outputs_expected_structure_and_flags() -> None:
    rows = 100
    df = pd.DataFrame(
        {
            "risk_band": ["Prime"] * 60 + ["Subprime"] * 40,
            "default_60d": ([0] * 54 + [1] * 6) + ([0] * 24 + [1] * 16),
        }
    )
    y_prob = np.array([0.1] * 60 + [0.8] * 40)

    out = build_segment_calibration(df, y_prob)

    assert list(out.columns) == [
        "risk_band",
        "account_count",
        "mean_predicted_probability",
        "actual_default_rate",
        "flag_under_50",
    ]
    assert len(out) == 2
    assert int(out["account_count"].sum()) == rows
    assert out.iloc[0]["risk_band"] == "Subprime"
    assert bool(out.loc[out["risk_band"] == "Subprime", "flag_under_50"].iloc[0])
    assert not bool(out.loc[out["risk_band"] == "Prime", "flag_under_50"].iloc[0])


def test_build_segment_calibration_invalid_inputs_raise() -> None:
    df = pd.DataFrame(
        {"risk_band": ["Prime", "Subprime"], "default_60d": [0, 1]}
    )
    with pytest.raises(ValueError):
        build_segment_calibration(df, [0.1])
    with pytest.raises(ValueError):
        build_segment_calibration(df, [0.1, np.nan])

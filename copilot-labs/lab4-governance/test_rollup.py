import pandas as pd
import pytest

from rollup import compute_monthly_rollup, make_monitoring_sample
from validators import validate_rollup_outputs


@pytest.fixture
def monitoring_sample():
    return make_monitoring_sample()


def test_compute_monthly_rollup_expected_values(monitoring_sample):
    result = compute_monthly_rollup(monitoring_sample)

    expected = pd.DataFrame(
        [
            ("2025-12", "Near-Prime", 2, 3450.00, 0.5000),
            ("2025-12", "Prime", 2, 2300.00, 0.5000),
            ("2025-12", "Subprime", 3, 1866.67, 0.6667),
        ],
        columns=["perf_month", "risk_band", "active_accounts", "mean_balance", "dlq_30_rate"],
    )

    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected)
    assert set(result["risk_band"]) == {"Near-Prime", "Prime", "Subprime"}
    assert len(result) == 3


@pytest.mark.parametrize(
    "builder, expected_message",
    [
        (
            lambda df: df.drop(columns=["dpd"]),
            "Missing required columns: {'dpd'}",
        ),
        (
            lambda df: df.iloc[0:0],
            "Input DataFrame is empty",
        ),
        (
            lambda df: pd.concat(
                [df, df.iloc[[0]].copy()],
                ignore_index=True,
            ),
            r"Duplicate \(account_id, perf_month\) keys found",
        ),
        (
            lambda df: df.assign(status="charged_off"),
            "Zero active valid rows after filtering status == 'charged_off' and dpd > 365",
        ),
    ],
)
def test_compute_monthly_rollup_invalid_inputs(monitoring_sample, builder, expected_message):
    df = builder(monitoring_sample)
    with pytest.raises(ValueError, match=expected_message):
        compute_monthly_rollup(df)


def test_validate_rollup_outputs_invalid_rate_raises():
    invalid = pd.DataFrame(
        {
            "perf_month": ["2025-12", "2025-12"],
            "risk_band": ["Prime", "Near-Prime"],
            "active_accounts": [2, 2],
            "mean_balance": [2300.0, 3450.0],
            "dlq_30_rate": [0.5, 1.2],
        }
    )

    with pytest.raises(ValueError, match=r"Invalid dlq_30_rate detected; values must be within \[0.0, 1.0\]"):
        validate_rollup_outputs(invalid)

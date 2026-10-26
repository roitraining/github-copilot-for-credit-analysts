import numpy as np
import pandas as pd

from credit_rules import assign_delinquency_bucket, calc_utilization, compute_30dpd_rate


def test_calc_utilization_returns_nan_for_missing_values() -> None:
    """Returns NaN when utilization inputs are missing."""
    assert np.isnan(calc_utilization(None, 1000))
    assert np.isnan(calc_utilization(100, None))


def test_compute_30dpd_rate_returns_nan_for_empty_dataframe() -> None:
    """Returns NaN when there are no active valid rows."""
    df = pd.DataFrame(columns=["status", "delinquency_days"])
    assert np.isnan(compute_30dpd_rate(df))


def test_assign_delinquency_bucket_flags_9999_as_error() -> None:
    """Treats delinquency_days values above 365 as data errors."""
    assert assign_delinquency_bucket(9999) == "Error"


def test_compute_30dpd_rate_excludes_charged_off_and_invalid_rows() -> None:
    """Excludes charged-off and >365 rows from numerator and denominator."""
    df = pd.DataFrame(
        [
            {"status": "active", "delinquency_days": 40},
            {"status": "active", "delinquency_days": 10},
            {"status": "active", "delinquency_days": 9999},
            {"status": "charged_off", "delinquency_days": 80},
        ]
    )

    assert compute_30dpd_rate(df) == 0.5


def test_compute_30dpd_rate_returns_nan_without_active_valid_rows() -> None:
    """Returns NaN when filtering removes all rows."""
    df = pd.DataFrame(
        [
            {"status": "charged_off", "delinquency_days": 90},
            {"status": "active", "delinquency_days": 9999},
            {"status": "active", "delinquency_days": np.nan},
        ]
    )

    assert np.isnan(compute_30dpd_rate(df))

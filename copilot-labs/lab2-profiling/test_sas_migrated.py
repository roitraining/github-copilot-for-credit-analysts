import numpy as np
import pandas as pd

from sas_migrated import build_roll_flags


def test_build_roll_flags_excludes_charged_off_and_dpd_gt_365():
    df = pd.DataFrame(
        [
            {"account_id": "A1", "status": "active", "dpd": 0, "balance": 100.0, "credit_limit": 1000.0, "utilization": 0.10},
            {"account_id": "A2", "status": "charged_off", "dpd": 60, "balance": 200.0, "credit_limit": 1000.0, "utilization": 0.20},
            {"account_id": "A3", "status": "active", "dpd": 366, "balance": 300.0, "credit_limit": 1000.0, "utilization": 0.30},
            {"account_id": "A4", "status": "active", "dpd": 365, "balance": 400.0, "credit_limit": 1000.0, "utilization": 0.40},
        ]
    )

    out = build_roll_flags(df)

    assert set(out["account_id"]) == {"A1", "A4"}


def test_build_roll_flags_assigns_missing_for_nan_utilization():
    df = pd.DataFrame(
        [
            {"account_id": "B1", "status": "active", "dpd": 10, "balance": 100.0, "credit_limit": 1000.0, "utilization": np.nan},
            {"account_id": "B2", "status": "active", "dpd": 10, "balance": 900.0, "credit_limit": 1000.0, "utilization": 0.90},
        ]
    )

    out = build_roll_flags(df).set_index("account_id")

    assert out.loc["B1", "util_tier"] == "Missing"
    assert out.loc["B1", "util_tier"] != "High"
    assert out.loc["B2", "util_tier"] == "High"


def test_build_roll_flags_dpd_flag_and_util_tier_bands():
    df = pd.DataFrame(
        [
            {"account_id": "C1", "status": "active", "dpd": 0, "balance": 100.0, "credit_limit": 1000.0, "utilization": 0.29},
            {"account_id": "C2", "status": "active", "dpd": 30, "balance": 300.0, "credit_limit": 1000.0, "utilization": 0.75},
            {"account_id": "C3", "status": "active", "dpd": 29, "balance": 900.0, "credit_limit": 1000.0, "utilization": 0.76},
        ]
    )

    out = build_roll_flags(df).set_index("account_id")

    assert out.loc["C1", "dlq_30_flag"] == 0
    assert out.loc["C2", "dlq_30_flag"] == 1
    assert out.loc["C3", "dlq_30_flag"] == 0

    assert out.loc["C1", "util_tier"] == "Low"
    assert out.loc["C2", "util_tier"] == "Medium"
    assert out.loc["C3", "util_tier"] == "High"

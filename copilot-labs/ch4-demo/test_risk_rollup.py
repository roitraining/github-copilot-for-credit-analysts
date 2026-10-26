import pandas as pd
import pytest

from risk_rollup import calc_delinquency


def test_calc_delinquency_exact_rates_excludes_charged_off():
    df = pd.DataFrame(
        [
            {"account_id": "P1", "risk_band": "Prime", "status": "current", "dpd": 0},
            {"account_id": "P2", "risk_band": "Prime", "status": "delinquent", "dpd": 45},
            {"account_id": "P3", "risk_band": "Prime", "status": "charged_off", "dpd": 120},
            {"account_id": "N1", "risk_band": "Near-Prime", "status": "current", "dpd": 10},
            {"account_id": "N2", "risk_band": "Near-Prime", "status": "delinquent", "dpd": 30},
            {"account_id": "N3", "risk_band": "Near-Prime", "status": "charged_off", "dpd": 90},
            {"account_id": "S1", "risk_band": "Subprime", "status": "delinquent", "dpd": 60},
            {"account_id": "S2", "risk_band": "Subprime", "status": "current", "dpd": 5},
            {"account_id": "S3", "risk_band": "Subprime", "status": "delinquent", "dpd": 35},
            {"account_id": "S4", "risk_band": "Subprime", "status": "charged_off", "dpd": 180},
        ]
    )

    rates = calc_delinquency(df)

    assert rates.to_dict() == {
        "Prime": 0.5,       # 1 bad / 2 active (charged_off excluded)
        "Near-Prime": 0.5,  # 1 bad / 2 active (charged_off excluded)
        "Subprime": 2 / 3,  # 2 bad / 3 active (charged_off excluded)
    }


def test_calc_delinquency_raises_for_missing_required_columns():
    df = pd.DataFrame(
        [
            {"account_id": "A1", "risk_band": "Prime", "status": "current"},
        ]
    )

    with pytest.raises(ValueError, match="Missing required columns"):
        calc_delinquency(df)


def test_calc_delinquency_raises_for_duplicate_account_id():
    df = pd.DataFrame(
        [
            {"account_id": "A1", "risk_band": "Prime", "status": "current", "dpd": 0},
            {"account_id": "A1", "risk_band": "Prime", "status": "delinquent", "dpd": 45},
        ]
    )

    with pytest.raises(ValueError, match="Duplicate account_id values found"):
        calc_delinquency(df)


def test_calc_delinquency_raises_for_band_with_zero_active_accounts():
    df = pd.DataFrame(
        [
            {"account_id": "A1", "risk_band": "Prime", "status": "current", "dpd": 0},
            {"account_id": "A2", "risk_band": "Subprime", "status": "charged_off", "dpd": 120},
        ]
    )

    with pytest.raises(ValueError, match="Zero active accounts for risk_band"):
        calc_delinquency(df)


def test_calc_delinquency_raises_for_rate_outside_bounds(monkeypatch):
    original_truediv = pd.Series.__truediv__

    def _bad_truediv(self, other):
        result = original_truediv(self, other)
        return result + 1.0

    monkeypatch.setattr(pd.Series, "__truediv__", _bad_truediv)

    df = pd.DataFrame(
        [
            {"account_id": "A1", "risk_band": "Prime", "status": "current", "dpd": 0},
            {"account_id": "A2", "risk_band": "Prime", "status": "delinquent", "dpd": 30},
        ]
    )

    with pytest.raises(ValueError, match="outside \\[0.0, 1.0\\]"):
        calc_delinquency(df)

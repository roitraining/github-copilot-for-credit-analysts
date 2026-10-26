import pandas as pd

from features import engineer_features


def test_engineer_features_creates_expected_columns_and_values():
    df = pd.DataFrame(
        [
            {
                "account_id": "A1",
                "risk_band": "Prime",
                "balance": 500.0,
                "credit_limit": 1000.0,
                "utilization": 0.2,
                "delinquency_days": 0,
            },
            {
                "account_id": "A2",
                "risk_band": "Near-Prime",
                "balance": 1200.0,
                "credit_limit": 1000.0,
                "utilization": 0.5,
                "delinquency_days": 30,
            },
            {
                "account_id": "A3",
                "risk_band": "Subprime",
                "balance": 250.0,
                "credit_limit": 1000.0,
                "utilization": 0.8,
                "delinquency_days": 9999,
            },
            {
                "account_id": "A4",
                "risk_band": "Prime",
                "balance": 200.0,
                "credit_limit": 1000.0,
                "utilization": None,
                "delinquency_days": 10,
            },
        ]
    )

    result = engineer_features(df)

    assert "available_credit" in result.columns
    assert "is_delinquent_30" in result.columns
    assert "utilization_bucket" in result.columns

    assert result["available_credit"].tolist() == [500.0, 0.0, 750.0, 800.0]
    assert result["is_delinquent_30"].tolist() == [0, 1, 0, 0]
    assert result["utilization_bucket"].tolist() == ["Low", "Medium", "High", "Unknown"]

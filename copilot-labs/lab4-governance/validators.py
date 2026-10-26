import pandas as pd


REQUIRED_COLUMNS = {
    "account_id",
    "perf_month",
    "risk_band",
    "status",
    "balance",
    "dpd",
}


def validate_monitoring_inputs(df: pd.DataFrame) -> pd.DataFrame:
    missing_cols = REQUIRED_COLUMNS.difference(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    if df.empty:
        raise ValueError("Input DataFrame is empty")

    if df.duplicated(subset=["account_id", "perf_month"]).any():
        raise ValueError("Duplicate (account_id, perf_month) keys found")

    valid = df[(df["status"] != "charged_off") & (df["dpd"] <= 365)].copy()
    if valid.empty:
        raise ValueError(
            "Zero active valid rows after filtering status == 'charged_off' and dpd > 365"
        )

    return valid


def validate_rollup_outputs(rollup: pd.DataFrame) -> None:
    invalid_dlq = (
        rollup["dlq_30_rate"].isna()
        | (rollup["dlq_30_rate"] < 0.0)
        | (rollup["dlq_30_rate"] > 1.0)
    )
    if invalid_dlq.any():
        raise ValueError("Invalid dlq_30_rate detected; values must be within [0.0, 1.0]")

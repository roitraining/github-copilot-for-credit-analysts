import numpy as np
import pandas as pd


def calc_utilization(balance: float, credit_limit: float) -> float:
    # Return balance / credit_limit rounded to 4 decimals; return np.nan if credit_limit <= 0 or inputs are null
    if balance is None or credit_limit is None or credit_limit <= 0:
        return np.nan
    return round(balance / credit_limit, 4)


def assign_delinquency_bucket(dpd: int) -> str:
    # Return 'Error' if dpd < 0 or dpd > 365, 'Current' if dpd == 0, '1-29 DPD' if 1 <= dpd <= 29, and '30+ DPD' if dpd >= 30
    if dpd < 0 or dpd > 365:
        return 'Error'
    if dpd == 0:
        return 'Current'
    if 1 <= dpd <= 29:
        return '1-29 DPD'
    return '30+ DPD'


def compute_30dpd_rate(df: pd.DataFrame) -> float:
    """Compute 30+ DPD rate on active rows with valid delinquency observations."""
    active_valid_rows = df[
        (df["status"] != "charged_off")
        & (df["delinquency_days"].notna())
        & (df["delinquency_days"] <= 365)
    ]
    if len(active_valid_rows) == 0:
        return np.nan

    bad_rows = active_valid_rows[active_valid_rows["delinquency_days"] >= 30]
    return len(bad_rows) / len(active_valid_rows)

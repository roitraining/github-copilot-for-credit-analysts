import numpy as np
import pandas as pd


def build_roll_flags(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Filter to status != 'charged_off' and dpd <= 365 on a copy of df
    out = df[(df["status"] != "charged_off") & (df["dpd"].fillna(0) <= 365)].copy()

    # 2. Compute util_ratio as balance / credit_limit (np.nan when credit_limit <= 0)
    out["util_ratio"] = np.where(out["credit_limit"] > 0, out["balance"] / out["credit_limit"], np.nan)

    # 3. Create dlq_30_flag: 1 when dpd >= 30 else 0 (treating NaN dpd as 0)
    out["dlq_30_flag"] = (out["dpd"].fillna(0) >= 30).astype(int)

    # 4. Create util_tier: 'Missing' when utilization is NaN, 'Low' when < 0.30, 'Medium' when <= 0.75, else 'High'
    def tier(util):
        if pd.isna(util):
            return "Missing"
        elif util < 0.30:
            return "Low"
        elif util <= 0.75:
            return "Medium"
        else:
            return "High"

    out["util_tier"] = out["utilization"].apply(tier)

    return out
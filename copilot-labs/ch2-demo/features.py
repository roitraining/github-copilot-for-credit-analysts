import numpy as np
import pandas as pd

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # Calculate available_credit as credit_limit minus balance, floored at 0
    out["available_credit"] = (out["credit_limit"] - out["balance"]).clip(lower=0)

    # Create is_delinquent_30 as 1 when delinquency_days >= 30 and delinquency_days <= 365, else 0
    out["is_delinquent_30"] = np.where((out["delinquency_days"] >= 30) & (out["delinquency_days"] <= 365), 1, 0)

    # Bucket utilization into 'Low' (<0.3), 'Medium' (0.3 to 0.7), and 'High' (>0.7) using np.select
    conditions = [
        out["utilization"] < 0.3,
        (out["utilization"] >= 0.3) & (out["utilization"] <= 0.7),
        out["utilization"] > 0.7
    ]
    choices = ["Low", "Medium", "High"]
    out["utilization_bucket"] = np.select(conditions, choices, default="Unknown")

    return out

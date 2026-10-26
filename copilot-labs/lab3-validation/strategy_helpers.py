from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import pandas as pd


def add_strategy_features(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = {"utilization", "tenure_months", "risk_band"}
    missing = sorted(required_cols.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns for feature engineering: {missing}")

    out = df.copy()
    out["util_to_tenure"] = out["utilization"] / (out["tenure_months"] + 1)
    out["high_util_subprime"] = (
        (out["utilization"] > 0.75) & (out["risk_band"] == "Subprime")
    ).astype(int)
    return out


def build_segment_calibration(
    df: pd.DataFrame, y_prob: Iterable[float]
) -> pd.DataFrame:
    required_cols = {"risk_band", "default_60d"}
    missing = sorted(required_cols.difference(df.columns))
    if missing:
        raise ValueError(f"Missing required columns for calibration: {missing}")

    y_prob_arr = np.asarray(list(y_prob), dtype=float)
    if y_prob_arr.ndim != 1:
        raise ValueError("y_prob must be one-dimensional.")
    if len(df) != y_prob_arr.shape[0]:
        raise ValueError("Length of y_prob must match the number of rows in df.")
    if np.isnan(y_prob_arr).any():
        raise ValueError("y_prob must not contain NaN values.")

    with_pred = df.copy()
    with_pred["pred_prob"] = y_prob_arr

    calibration = (
        with_pred.groupby("risk_band", as_index=False)
        .agg(
            account_count=("default_60d", "size"),
            mean_predicted_probability=("pred_prob", "mean"),
            actual_default_rate=("default_60d", "mean"),
        )
        .sort_values("mean_predicted_probability", ascending=False)
        .reset_index(drop=True)
    )
    calibration["flag_under_50"] = calibration["account_count"] < 50
    return calibration

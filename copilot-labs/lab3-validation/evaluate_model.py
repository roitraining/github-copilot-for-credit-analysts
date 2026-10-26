import json
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import brier_score_loss, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DECISION_TIME_FEATURES = [
    "balance",
    "credit_limit",
    "utilization",
    "tenure_months",
    "risk_band",
]
EXCLUDED_COLUMNS = [
    "account_id",
    "application_month",
    "post_decision_dpd",
    "default_60d",
]
TARGET_COL = "default_60d"


def compute_ks(y_true: Iterable[int], y_prob: Iterable[float]) -> float:
    y_true_arr = np.asarray(y_true)
    y_prob_arr = np.asarray(y_prob, dtype=float)

    if y_true_arr.size == 0 or y_prob_arr.size == 0:
        raise ValueError("y_true and y_prob must be non-empty.")
    if y_true_arr.shape[0] != y_prob_arr.shape[0]:
        raise ValueError("y_true and y_prob must have the same length.")
    if np.isnan(y_true_arr.astype(float)).any() or np.isnan(y_prob_arr).any():
        raise ValueError("y_true and y_prob must not contain NaN values.")

    unique_classes = np.unique(y_true_arr)
    if unique_classes.size < 2:
        raise ValueError("y_true must contain at least two classes.")

    sorted_idx = np.argsort(-y_prob_arr)
    sorted_true = y_true_arr[sorted_idx]

    bad = (sorted_true == 1).astype(float)
    good = (sorted_true == 0).astype(float)

    total_bad = bad.sum()
    total_good = good.sum()
    if total_bad == 0 or total_good == 0:
        raise ValueError("y_true must contain both good and bad classes.")

    cum_bad_rate = np.cumsum(bad) / total_bad
    cum_good_rate = np.cumsum(good) / total_good
    return float(np.max(np.abs(cum_bad_rate - cum_good_rate)))


def build_decile_table(y_true: Iterable[int], y_prob: Iterable[float]) -> pd.DataFrame:
    y_true_arr = np.asarray(y_true)
    y_prob_arr = np.asarray(y_prob, dtype=float)

    if y_true_arr.size == 0 or y_prob_arr.size == 0:
        raise ValueError("y_true and y_prob must be non-empty.")
    if y_true_arr.shape[0] != y_prob_arr.shape[0]:
        raise ValueError("y_true and y_prob must have the same length.")
    if np.isnan(y_true_arr.astype(float)).any() or np.isnan(y_prob_arr).any():
        raise ValueError("y_true and y_prob must not contain NaN values.")

    sorted_idx = np.argsort(-y_prob_arr)
    sorted_true = y_true_arr[sorted_idx]
    sorted_prob = y_prob_arr[sorted_idx]

    row_positions = np.arange(sorted_true.shape[0])
    decile_slices = np.array_split(row_positions, 10)
    total_bad = float((sorted_true == 1).sum())

    rows = []
    cumulative_bad = 0
    for i, pos in enumerate(decile_slices, start=1):
        if pos.size == 0:
            account_count = 0
            bad_count = 0
            actual_bad_rate = np.nan
            mean_pred = np.nan
        else:
            dec_true = sorted_true[pos]
            dec_prob = sorted_prob[pos]
            account_count = int(dec_true.shape[0])
            bad_count = int((dec_true == 1).sum())
            actual_bad_rate = float(bad_count / account_count)
            mean_pred = float(dec_prob.mean())

        cumulative_bad += bad_count
        if total_bad > 0:
            cum_bad_capture = float(cumulative_bad / total_bad)
        else:
            cum_bad_capture = np.nan

        rows.append(
            {
                "decile": i,
                "account_count": account_count,
                "bad_count": bad_count,
                "actual_bad_rate": actual_bad_rate,
                "mean_predicted_prob": mean_pred,
                "cum_bad_capture_rate": cum_bad_capture,
            }
        )

    return pd.DataFrame(rows)


def build_pipeline() -> Pipeline:
    numeric_features = ["balance", "credit_limit", "utilization", "tenure_months"]
    categorical_features = ["risk_band"]

    preprocess = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numeric_features,
            ),
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            ),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocess", preprocess),
            ("clf", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )


def main() -> None:
    overlap = set(DECISION_TIME_FEATURES).intersection(EXCLUDED_COLUMNS)
    if overlap:
        raise ValueError(f"Excluded columns found in features: {sorted(overlap)}")

    df = pd.read_csv("modeling_data.csv")

    train_mask = df["application_month"] < "2025-10"
    test_mask = ~train_mask

    train_df = df.loc[train_mask].copy()
    test_df = df.loc[test_mask].copy()
    if train_df.empty or test_df.empty:
        raise ValueError("Out-of-time split produced an empty train or test set.")

    model = build_pipeline()
    model.fit(train_df[DECISION_TIME_FEATURES], train_df[TARGET_COL])

    y_test = test_df[TARGET_COL].to_numpy()
    y_prob = model.predict_proba(test_df[DECISION_TIME_FEATURES])[:, 1]

    roc_auc = roc_auc_score(y_test, y_prob)
    ks = compute_ks(y_test, y_prob)
    brier = brier_score_loss(y_test, y_prob)

    metrics = {
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "roc_auc": float(roc_auc),
        "ks": float(ks),
        "brier_score": float(brier),
    }
    with open("metrics_output.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    decile_df = build_decile_table(y_test, y_prob)
    decile_df.to_csv("decile_table.csv", index=False)

    print(f"Train rows: {metrics['train_rows']}")
    print(f"Test rows: {metrics['test_rows']}")
    print(f"Holdout ROC AUC: {metrics['roc_auc']:.4f}")
    print(f"Holdout KS: {metrics['ks']:.4f}")
    print(f"Holdout Brier score: {metrics['brier_score']:.4f}")


if __name__ == "__main__":
    main()

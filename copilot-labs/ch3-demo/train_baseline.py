from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def compute_ks(y_true: pd.Series | np.ndarray, y_score: pd.Series | np.ndarray) -> float:
    """Return the KS statistic for a binary target and predicted probabilities."""
    y_true_array = np.asarray(y_true, dtype=int)
    y_score_array = np.asarray(y_score, dtype=float)

    order = np.argsort(-y_score_array)
    y_sorted = y_true_array[order]
    score_sorted = y_score_array[order]

    positives = y_sorted.sum()
    negatives = len(y_sorted) - positives
    if positives == 0 or negatives == 0:
        return 0.0

    cumulative_true_positive = np.cumsum(y_sorted)
    cumulative_true_negative = np.cumsum(1 - y_sorted)
    tpr = cumulative_true_positive / positives
    fpr = cumulative_true_negative / negatives
    ks_statistic = np.max(np.abs(tpr - fpr))
    return float(ks_statistic)


def build_decile_table(y_true: pd.Series | np.ndarray, y_score: pd.Series | np.ndarray) -> pd.DataFrame:
    """Build a 10-bin decile table for scored holdout rows."""
    evaluation_df = pd.DataFrame({"actual": np.asarray(y_true, dtype=int), "score": np.asarray(y_score, dtype=float)})
    evaluation_df = evaluation_df.sort_values("score", ascending=False).reset_index(drop=True)
    evaluation_df["decile"] = pd.cut(
        np.arange(len(evaluation_df)),
        bins=10,
        labels=False,
        include_lowest=True,
    ) + 1

    decile_table = (
        evaluation_df.groupby("decile", as_index=False)
        .agg(
            count=("actual", "size"),
            avg_score=("score", "mean"),
            avg_actual_rate=("actual", "mean"),
            min_score=("score", "min"),
            max_score=("score", "max"),
        )
        .sort_values("decile")
        .reset_index(drop=True)
    )
    return decile_table


def make_synthetic_modeling_data(path: str = "modeling_accounts.csv") -> pd.DataFrame:
    """Create a synthetic monthly credit-modeling dataset and persist it to CSV."""
    rng = np.random.default_rng(42)
    records = []
    months = [f"2025-{month:02d}" for month in range(1, 13)]

    risk_weights = {
        "Prime": -2.2,
        "Near-Prime": 0.4,
        "Subprime": 1.9,
    }
    risk_probabilities = {"Prime": 0.55, "Near-Prime": 0.30, "Subprime": 0.15}

    for month in months:
        for idx in range(25):
            risk_band = rng.choice(
                list(risk_probabilities.keys()),
                p=list(risk_probabilities.values()),
            )
            balance = max(500.0, float(rng.normal(8500, 3200)))
            credit_limit = max(1000.0, float(balance * rng.uniform(1.5, 2.8) + rng.normal(500, 1200)))
            utilization = float(rng.uniform(0.05, 0.95))

            risk_score = risk_weights[risk_band]
            balance_signal = 0.00006 * max(balance - 8000, 0)
            default_probability = 1 / (
                1 + np.exp(-(risk_score + 3.4 * utilization + balance_signal - 1.5))
            )
            default_60d = int(rng.random() < default_probability)

            records.append(
                {
                    "account_id": f"{month}-{idx + 1:03d}",
                    "application_month": month,
                    "risk_band": risk_band,
                    "balance": round(balance, 2),
                    "credit_limit": round(credit_limit, 2),
                    "utilization": utilization,
                    "default_60d": default_60d,
                }
            )

    df = pd.DataFrame(records)
    null_indices = rng.choice(len(df), size=15, replace=False)
    df.loc[df.index.isin(null_indices), "utilization"] = np.nan

    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    return df


def main() -> None:
    df = make_synthetic_modeling_data("modeling_accounts.csv")

    train_df = df[df["application_month"] < "2025-10"].copy()
    test_df = df[df["application_month"] >= "2025-10"].copy()

    feature_columns = [
        column
        for column in df.columns
        if column not in {"account_id", "application_month", "default_60d"}
    ]
    numeric_features = [
        column for column in feature_columns if column != "risk_band"
    ]
    categorical_features = ["risk_band"]

    X_train = train_df[feature_columns]
    y_train = train_df["default_60d"]
    X_test = test_df[feature_columns]
    y_test = test_df["default_60d"]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                numeric_features,
            ),
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features,
            ),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )

    model.fit(X_train, y_train)
    test_probabilities = model.predict_proba(X_test)[:, 1]
    test_auc = roc_auc_score(y_test, test_probabilities)
    test_ks = compute_ks(y_test, test_probabilities)
    decile_table = build_decile_table(y_test, test_probabilities)

    output_dir = Path(__file__).resolve().parent
    metrics = {
        "train_rows": int(len(train_df)),
        "test_rows": int(len(test_df)),
        "roc_auc": float(test_auc),
        "ks": float(test_ks),
    }
    (output_dir / "metrics_output.json").write_text(json.dumps(metrics, indent=2))
    decile_table.to_csv(output_dir / "decile_table.csv", index=False)

    print(f"Train rows: {len(train_df)}")
    print(f"Test rows: {len(test_df)}")
    print(f"Test ROC AUC: {test_auc:.4f}")
    print(f"Test KS: {test_ks:.4f}")
    print(f"Decile table written to {output_dir / 'decile_table.csv'}")
    print(f"Metrics written to {output_dir / 'metrics_output.json'}")


if __name__ == "__main__":
    main()

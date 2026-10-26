import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    df = pd.read_csv("modeling_data.csv")

    excluded_columns = [
        "account_id",
        "application_month",
        "post_decision_dpd",
        "default_60d",
    ]
    decision_time_features = [
        "balance",
        "credit_limit",
        "utilization",
        "tenure_months",
        "risk_band",
    ]
    target_col = "default_60d"

    train_mask = df["application_month"] < "2025-10"
    test_mask = ~train_mask

    train_df = df.loc[train_mask].copy()
    test_df = df.loc[test_mask].copy()

    if train_df.empty or test_df.empty:
        raise ValueError("Out-of-time split produced an empty train or test set.")

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

    model = Pipeline(
        steps=[
            ("preprocess", preprocess),
            ("clf", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )

    X_train = train_df[decision_time_features]
    y_train = train_df[target_col]
    X_test = test_df[decision_time_features]
    y_test = test_df[target_col]

    overlap = set(decision_time_features).intersection(excluded_columns)
    if overlap:
        raise ValueError(f"Excluded columns found in features: {sorted(overlap)}")

    model.fit(X_train, y_train)
    test_probs = model.predict_proba(X_test)[:, 1]
    holdout_auc = roc_auc_score(y_test, test_probs)

    print(f"Train count: {len(train_df)}")
    print(f"Test count: {len(test_df)}")
    print(f"Holdout ROC AUC: {holdout_auc:.4f}")


if __name__ == "__main__":
    main()

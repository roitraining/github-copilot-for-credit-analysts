import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.read_csv("modeling_accounts.csv")

train_df = df[df["application_month"] < "2025-10"].copy()
test_df = df[df["application_month"] >= "2025-10"].copy()

feature_columns = [
    col for col in df.columns if col not in {"account_id", "application_month", "default_60d"}
]
numeric_features = [col for col in feature_columns if col != "risk_band"]
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
        ("categorical", OneHotEncoder(handle_unknown="ignore"), categorical_features),
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

print(f"Train rows: {len(train_df)}")
print(f"Test rows: {len(test_df)}")
print(f"Test ROC AUC: {roc_auc_score(y_test, test_probabilities):.4f}")

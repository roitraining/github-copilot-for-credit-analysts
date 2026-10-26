import pandas as pd

from validators import validate_monitoring_inputs, validate_rollup_outputs


def make_monitoring_sample() -> pd.DataFrame:
    data = [
        ("ACC-101", "2025-12", "Prime", "active", 1200.0, 0),
        ("ACC-102", "2025-12", "Prime", "active", 3400.0, 45),
        ("ACC-103", "2025-12", "Prime", "charged_off", 5000.0, 180),
        ("ACC-104", "2025-12", "Near-Prime", "active", 2800.0, 15),
        ("ACC-105", "2025-12", "Near-Prime", "active", 4100.0, 60),
        ("ACC-106", "2025-12", "Subprime", "active", 1900.0, 30),
        ("ACC-107", "2025-12", "Subprime", "active", 2200.0, 90),
        ("ACC-108", "2025-12", "Subprime", "active", 1500.0, 0),
    ]
    return pd.DataFrame(
        data,
        columns=["account_id", "perf_month", "risk_band", "status", "balance", "dpd"],
    )


def compute_monthly_rollup(df: pd.DataFrame) -> pd.DataFrame:
    valid = validate_monitoring_inputs(df)

    valid["bad_30"] = valid["dpd"] >= 30

    rollup = (
        valid.groupby(["perf_month", "risk_band"], as_index=False)
        .agg(
            active_accounts=("account_id", "size"),
            mean_balance=("balance", "mean"),
            bad_count=("bad_30", "sum"),
        )
        .assign(
            mean_balance=lambda x: x["mean_balance"].round(2),
            dlq_30_rate=lambda x: (x["bad_count"] / x["active_accounts"]).round(4),
        )
        [["perf_month", "risk_band", "active_accounts", "mean_balance", "dlq_30_rate"]]
    )

    validate_rollup_outputs(rollup)

    return rollup


if __name__ == "__main__":
    sample_df = make_monitoring_sample()
    print(compute_monthly_rollup(sample_df))
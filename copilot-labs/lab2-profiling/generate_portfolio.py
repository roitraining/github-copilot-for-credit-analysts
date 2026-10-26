import numpy as np
import pandas as pd


def generate_portfolio() -> pd.DataFrame:
    rng = np.random.default_rng(42)
    n_rows = 500

    account_ids = np.array([f"ACC-{i}" for i in range(2001, 2501)])
    rng.shuffle(account_ids)

    vintage_quarters = rng.choice(
        ["2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4"],
        size=n_rows,
        p=[0.24, 0.26, 0.30, 0.20],
    )
    perf_months = rng.choice(
        ["2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12"],
        size=n_rows,
        p=[0.17, 0.16, 0.16, 0.15, 0.18, 0.18],
    )
    risk_bands = rng.choice(
        ["Prime", "Near-Prime", "Subprime"],
        size=n_rows,
        p=[0.45, 0.35, 0.20],
    )

    credit_limits = rng.uniform(1000, 25000, size=n_rows).round(2)
    utilizations = rng.uniform(0.0, 1.2, size=n_rows)
    balances = np.minimum(utilizations * credit_limits, 20000).round(2)
    utilizations = balances / credit_limits

    status = np.array(["active"] * n_rows, dtype=object)
    dpd = rng.choice([0, 15, 30, 60, 90], size=n_rows, p=[0.67, 0.22, 0.07, 0.03, 0.01])

    df = pd.DataFrame(
        {
            "account_id": account_ids,
            "vintage_quarter": vintage_quarters,
            "perf_month": perf_months,
            "risk_band": risk_bands,
            "status": status,
            "balance": balances,
            "credit_limit": credit_limits,
            "utilization": utilizations.round(4),
            "dpd": dpd,
        }
    )

    # Pattern 3: concentrated 30+ DPD rise in Nov/Dec for 2025-Q3 Near-Prime/Subprime cohorts.
    concentrated_idx = rng.choice(df.index.to_numpy(), size=70, replace=False)
    df.loc[concentrated_idx, "vintage_quarter"] = "2025-Q3"
    df.loc[concentrated_idx, "perf_month"] = rng.choice(["2025-11", "2025-12"], size=70, p=[0.48, 0.52])
    df.loc[concentrated_idx, "risk_band"] = rng.choice(["Near-Prime", "Subprime"], size=70, p=[0.58, 0.42])
    df.loc[concentrated_idx, "dpd"] = rng.choice([30, 60, 90], size=70, p=[0.54, 0.30, 0.16])

    # Keep delinquency outside the concentrated slice relatively low for a visible rise.
    concentrated_mask = (
        (df["vintage_quarter"] == "2025-Q3")
        & (df["perf_month"].isin(["2025-11", "2025-12"]))
        & (df["risk_band"].isin(["Near-Prime", "Subprime"]))
    )
    other_mask = ~concentrated_mask
    other_30_plus = df.index[other_mask & df["dpd"].between(30, 365)]
    if len(other_30_plus) > 22:
        demote_idx = rng.choice(other_30_plus.to_numpy(), size=len(other_30_plus) - 22, replace=False)
        df.loc[demote_idx, "dpd"] = rng.choice([0, 15], size=len(demote_idx), p=[0.75, 0.25])

    # Pattern 1: exactly 18 Near-Prime rows with missing utilization.
    near_prime_idx = df.index[df["risk_band"] == "Near-Prime"].to_numpy()
    if len(near_prime_idx) < 18:
        needed = 18 - len(near_prime_idx)
        convert_pool = df.index[df["risk_band"] != "Near-Prime"].to_numpy()
        convert_idx = rng.choice(convert_pool, size=needed, replace=False)
        df.loc[convert_idx, "risk_band"] = "Near-Prime"
        near_prime_idx = df.index[df["risk_band"] == "Near-Prime"].to_numpy()
    missing_util_idx = rng.choice(near_prime_idx, size=18, replace=False)
    df.loc[missing_util_idx, "utilization"] = np.nan

    # Pattern 2a: exactly 6 rows with dpd = 9999 error code.
    all_idx = df.index.to_numpy()
    error_dpd_idx = rng.choice(all_idx, size=6, replace=False)
    df.loc[error_dpd_idx, "dpd"] = 9999

    # Pattern 2b: exactly 25 charged-off rows.
    charged_off_idx = rng.choice(all_idx, size=25, replace=False)
    df["status"] = "active"
    df.loc[charged_off_idx, "status"] = "charged_off"

    return df


def main() -> None:
    df = generate_portfolio()
    df.to_csv("portfolio_history.csv", index=False)


if __name__ == "__main__":
    main()

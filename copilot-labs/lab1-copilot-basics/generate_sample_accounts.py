"""Generate synthetic credit account data for simulator demos."""

from __future__ import annotations

import numpy as np
import pandas as pd


def _build_accounts_dataframe(seed: int = 42) -> pd.DataFrame:
    """Create 100 synthetic credit accounts with policy edge cases included."""
    rng = np.random.default_rng(seed)
    row_count = 100

    account_ids = [f"ACC-{account_number}" for account_number in range(1001, 1101)]
    risk_bands = rng.choice(
        ["Prime", "Near-Prime", "Subprime"],
        size=row_count,
        p=[0.42, 0.33, 0.25],
    )

    statuses = np.array(["active"] * 92 + ["charged_off"] * 8, dtype=object)
    rng.shuffle(statuses)

    balances = rng.integers(200, 15001, size=row_count)
    credit_limits = rng.integers(1000, 20001, size=row_count)

    utilizations = np.round(balances / credit_limits, 4).astype(object)
    blank_utilization_indices = rng.choice(row_count, size=4, replace=False)
    utilizations[blank_utilization_indices] = np.nan

    delinquency_days = rng.choice([0, 15, 30, 60, 90], size=row_count).astype(int)
    error_delinquency_indices = rng.choice(row_count, size=2, replace=False)
    delinquency_days[error_delinquency_indices] = 9999

    return pd.DataFrame(
        {
            "account_id": account_ids,
            "risk_band": risk_bands,
            "status": statuses,
            "balance": balances,
            "credit_limit": credit_limits,
            "utilization": utilizations,
            "delinquency_days": delinquency_days,
        }
    )


def main() -> None:
    """Generate sample_accounts.csv in the current working directory."""
    accounts_df = _build_accounts_dataframe(seed=42)
    accounts_df.to_csv("sample_accounts.csv", index=False)
    print("Created sample_accounts.csv with 100 synthetic accounts.")


if __name__ == "__main__":
    main()

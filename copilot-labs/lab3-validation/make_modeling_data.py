import numpy as np
import pandas as pd


SEED = 42
N_ROWS = 1000
TARGET_BAD_RATE = 0.12


def calibrate_intercept(linear_score: np.ndarray, target_rate: float) -> float:
    low, high = -10.0, 10.0
    for _ in range(80):
        mid = (low + high) / 2.0
        probs = 1.0 / (1.0 + np.exp(-(linear_score + mid)))
        if probs.mean() < target_rate:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def main() -> None:
    rng = np.random.default_rng(SEED)

    account_id = [f"ACC-{i}" for i in range(3001, 4001)]

    months = np.array([f"2025-{m:02d}" for m in range(1, 13)])
    application_month = np.resize(months, N_ROWS)
    rng.shuffle(application_month)

    risk_band = rng.choice(
        ["Prime", "Near-Prime", "Subprime"],
        size=N_ROWS,
        p=[0.50, 0.30, 0.20],
    )

    credit_limit = np.empty(N_ROWS, dtype=float)
    for i, band in enumerate(risk_band):
        if band == "Prime":
            limit = rng.normal(12000, 3500)
        elif band == "Near-Prime":
            limit = rng.normal(7000, 2200)
        else:
            limit = rng.normal(3500, 1400)
        credit_limit[i] = np.clip(limit, 500, 30000)

    util_raw = np.empty(N_ROWS, dtype=float)
    for i, band in enumerate(risk_band):
        if band == "Prime":
            util_raw[i] = rng.beta(2.2, 5.8)
        elif band == "Near-Prime":
            util_raw[i] = rng.beta(2.2, 3.9)
        else:
            util_raw[i] = rng.beta(2.3, 2.9)

    balance_noise = rng.normal(0, 0.03 * credit_limit)
    balance = np.clip((util_raw * credit_limit) + balance_noise, 0, credit_limit)
    utilization = np.clip(balance / credit_limit, 0.0, 1.0)

    tenure_months = np.empty(N_ROWS, dtype=int)
    for i, band in enumerate(risk_band):
        if band == "Prime":
            tenure = rng.normal(62, 24)
        elif band == "Near-Prime":
            tenure = rng.normal(44, 22)
        else:
            tenure = rng.normal(26, 16)
        tenure_months[i] = int(np.clip(np.round(tenure), 1, 120))

    risk_points = np.select(
        [risk_band == "Prime", risk_band == "Near-Prime", risk_band == "Subprime"],
        [0.0, 0.45, 1.05],
    )
    low_tenure_pressure = np.maximum(0, (24 - tenure_months) / 24)
    high_tenure_relief = np.maximum(0, (tenure_months - 24) / 96)

    linear_score = (
        (2.9 * utilization)
        + risk_points
        + (0.95 * low_tenure_pressure)
        - (0.15 * high_tenure_relief)
    )

    intercept = calibrate_intercept(linear_score, TARGET_BAD_RATE)
    default_prob = 1.0 / (1.0 + np.exp(-(linear_score + intercept)))
    default_60d = rng.binomial(1, default_prob).astype(int)

    post_decision_dpd = np.where(
        default_60d == 1,
        np.clip(np.round(rng.normal(85, 24, size=N_ROWS)), 35, 180),
        np.clip(np.round(rng.normal(4, 5, size=N_ROWS)), 0, 35),
    ).astype(int)
    non_default_leak_idx = (default_60d == 0) & (rng.random(N_ROWS) < 0.04)
    post_decision_dpd[non_default_leak_idx] = rng.integers(
        20, 46, size=non_default_leak_idx.sum()
    )

    utilization_with_nulls = utilization.copy()
    null_idx = rng.choice(N_ROWS, size=40, replace=False)
    utilization_with_nulls[null_idx] = np.nan

    df = pd.DataFrame(
        {
            "account_id": account_id,
            "application_month": application_month,
            "risk_band": risk_band,
            "balance": np.round(balance, 2),
            "credit_limit": np.round(credit_limit, 2),
            "utilization": np.round(utilization_with_nulls, 4),
            "tenure_months": tenure_months,
            "post_decision_dpd": post_decision_dpd,
            "default_60d": default_60d,
        }
    )
    df.to_csv("modeling_data.csv", index=False)


if __name__ == "__main__":
    main()

import numpy as np
import pandas as pd


def print_null_audit(df: pd.DataFrame) -> None:
    print("=== 1. Null Audit ===")
    total_rows = len(df)
    overall = pd.DataFrame(
        {
            "null_count": df.isna().sum(),
            "null_pct": (df.isna().sum() / total_rows * 100).round(2),
        }
    )
    print("\nOverall nulls by column:")
    print(overall.to_string())

    print("\nNulls by risk_band:")
    for risk_band, group in df.groupby("risk_band", sort=True):
        grp_rows = len(group)
        summary = pd.DataFrame(
            {
                "null_count": group.isna().sum(),
                "null_pct": (group.isna().sum() / grp_rows * 100).round(2),
            }
        )
        print(f"\n[{risk_band}]")
        print(summary.to_string())


def print_anomaly_audit(df: pd.DataFrame) -> None:
    print("\n=== 2. Anomaly Audit ===")
    dpd_error = df["dpd"] > 365
    high_util = df["utilization"] > 1.0
    charged_off = df["status"] == "charged_off"
    any_anomaly = dpd_error | high_util | charged_off

    duplicate_mask = df.duplicated(subset=["account_id", "perf_month"], keep=False)

    print(f"Rows with dpd > 365: {int(dpd_error.sum())}")
    print(f"Rows with utilization > 1.0: {int(high_util.sum())}")
    print(f"Rows with status == 'charged_off': {int(charged_off.sum())}")
    print(f"Rows meeting any anomaly rule: {int(any_anomaly.sum())}")
    print(f"Duplicate rows on (account_id, perf_month): {int(duplicate_mask.sum())}")


def print_distribution_summary(df: pd.DataFrame) -> None:
    print("\n=== 3. Distribution Summary ===")
    active_non_error = df[(df["status"] == "active") & (df["dpd"] <= 365)]
    q = active_non_error[["balance", "utilization"]].quantile([0.05, 0.50, 0.95]).round(4)
    q.index = ["5th", "50th", "95th"]
    print("Quantiles for active, non-error rows:")
    print(q.to_string())


def build_hypotheses_table(df: pd.DataFrame) -> str:
    filtered = df[(df["status"] != "charged_off") & (df["dpd"] <= 365)].copy()
    filtered["is_q4"] = filtered["perf_month"].isin(["2025-11", "2025-12"])
    filtered["is_30_plus"] = filtered["dpd"].between(30, 365)

    grouped = (
        filtered.groupby(["risk_band", "vintage_quarter", "is_q4"], as_index=False)
        .agg(rows=("account_id", "size"), delinquent_30_plus=("is_30_plus", "sum"))
        .assign(rate=lambda x: x["delinquent_30_plus"] / np.maximum(x["rows"], 1))
    )

    pivot = grouped.pivot_table(
        index=["risk_band", "vintage_quarter"],
        columns="is_q4",
        values=["rows", "delinquent_30_plus", "rate"],
        fill_value=0.0,
    )
    pivot.columns = [f"{metric}_{'q4' if is_q4 else 'pre_q4'}" for metric, is_q4 in pivot.columns]
    pivot = pivot.reset_index()

    for col in [
        "rows_pre_q4",
        "rows_q4",
        "delinquent_30_plus_pre_q4",
        "delinquent_30_plus_q4",
        "rate_pre_q4",
        "rate_q4",
    ]:
        if col not in pivot.columns:
            pivot[col] = 0.0

    pivot["count_increase"] = pivot["delinquent_30_plus_q4"] - pivot["delinquent_30_plus_pre_q4"]
    pivot["rate_increase_pp"] = (pivot["rate_q4"] - pivot["rate_pre_q4"]) * 100
    pivot["q4_share_of_30_plus"] = np.where(
        pivot["delinquent_30_plus_q4"].sum() > 0,
        pivot["delinquent_30_plus_q4"] / pivot["delinquent_30_plus_q4"].sum() * 100,
        0.0,
    )

    top_three = pivot.sort_values(
        by=["count_increase", "rate_increase_pp", "q4_share_of_30_plus"],
        ascending=False,
    ).head(3)

    rows = []
    for i, row in enumerate(top_three.itertuples(index=False), start=1):
        cohort = f"{row.risk_band} / {row.vintage_quarter}"
        signal = (
            f"Q4 30+ DPD={int(row.delinquent_30_plus_q4)} vs pre-Q4={int(row.delinquent_30_plus_pre_q4)}; "
            f"rate +{row.rate_increase_pp:.1f}pp; Q4 share {row.q4_share_of_30_plus:.1f}%."
        )
        check = (
            f"Compare 30+ DPD rate in {cohort} between pre-Q4 and Q4, "
            f"then test significance (e.g., two-proportion z-test) with n_pre={int(row.rows_pre_q4)} "
            f"and n_q4={int(row.rows_q4)}."
        )
        priority = ["High", "High", "Medium"][i - 1]
        rows.append((f"H{i}: {cohort} cohort drove Q4 rise", signal, check, priority))

    header = "| Hypothesis | Data Signal Observed | Verification Check | Priority |"
    divider = "|---|---|---|---|"
    body = [
        f"| {hyp} | {signal} | {check} | {priority} |"
        for hyp, signal, check, priority in rows
    ]
    return "\n".join([header, divider, *body]) + "\n"


def main() -> None:
    df = pd.read_csv("portfolio_history.csv")

    print_null_audit(df)
    print_anomaly_audit(df)
    print_distribution_summary(df)

    print("\n=== 4. Hypothesis Markdown Table ===")
    hypotheses_md = build_hypotheses_table(df)
    print(hypotheses_md)

    with open("hypotheses.md", "w", encoding="utf-8") as f:
        f.write(hypotheses_md)
    print("Saved hypotheses markdown to hypotheses.md")


if __name__ == "__main__":
    main()

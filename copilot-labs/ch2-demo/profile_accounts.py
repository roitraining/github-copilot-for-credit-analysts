import pandas as pd


INPUT_FILE = "sample_accounts.csv"


def main() -> None:
    df = pd.read_csv(INPUT_FILE)

    print("Null count and null percentage by column:")
    null_counts = df.isna().sum()
    null_percentages = df.isna().mean() * 100
    for column in df.columns:
        print(f"- {column}: {null_counts[column]} nulls ({null_percentages[column]:.2f}%)")

    print("\nPercentiles (5th, 50th, 95th):")
    percentiles = df[["balance", "utilization"]].quantile([0.05, 0.50, 0.95])
    for column in ["balance", "utilization"]:
        p5 = percentiles.loc[0.05, column]
        p50 = percentiles.loc[0.50, column]
        p95 = percentiles.loc[0.95, column]
        print(f"- {column}: p5={p5:.4f}, p50={p50:.4f}, p95={p95:.4f}")

    error_rows = (df["delinquency_days"] > 365).sum()
    print(f"\nError rows (delinquency_days > 365): {error_rows}")

    print("\nSummary by risk_band:")
    summary = (
        df.groupby("risk_band", dropna=False)
        .agg(account_count=("account_id", "count"), mean_balance=("balance", "mean"))
        .reset_index()
    )
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()

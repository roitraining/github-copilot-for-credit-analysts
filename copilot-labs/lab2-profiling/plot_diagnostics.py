import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def main() -> None:
    sns.set_theme(style="whitegrid")

    df = pd.read_csv("portfolio_history.csv")
    filtered = df[(df["status"] == "active") & (df["dpd"] <= 365)].copy()

    risk_order = ["Prime", "Near-Prime", "Subprime"]
    vintage_order = ["2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4"]
    month_order = ["2025-07", "2025-08", "2025-09", "2025-10", "2025-11", "2025-12"]

    filtered["risk_band"] = pd.Categorical(filtered["risk_band"], categories=risk_order, ordered=True)
    filtered["vintage_quarter"] = pd.Categorical(
        filtered["vintage_quarter"], categories=vintage_order, ordered=True
    )
    filtered["perf_month"] = pd.Categorical(filtered["perf_month"], categories=month_order, ordered=True)

    monthly_dlq = (
        filtered.assign(is_30_plus=filtered["dpd"] >= 30)
        .groupby(["perf_month", "risk_band"], observed=False, as_index=False)["is_30_plus"]
        .mean()
        .rename(columns={"is_30_plus": "dlq_30_rate"})
    )

    heatmap_data = (
        filtered.assign(is_30_plus=filtered["dpd"] >= 30)
        .groupby(["vintage_quarter", "risk_band"], observed=False, as_index=False)["is_30_plus"]
        .mean()
        .pivot(index="vintage_quarter", columns="risk_band", values="is_30_plus")
        .reindex(index=vintage_order, columns=risk_order)
    )

    active_accounts = (
        filtered.groupby("risk_band", observed=False)["account_id"]
        .nunique()
        .reindex(risk_order)
        .fillna(0)
    )

    fig, ax = plt.subplots(2, 2, figsize=(14, 10))

    sns.lineplot(
        data=monthly_dlq,
        x="perf_month",
        y="dlq_30_rate",
        hue="risk_band",
        hue_order=risk_order,
        marker="o",
        ax=ax[0, 0],
    )
    ax[0, 0].set_title("Monthly 30+ DPD Rate by Risk Band")
    ax[0, 0].set_xlabel("perf_month")
    ax[0, 0].set_ylabel("dlq_30_rate")
    ax[0, 0].tick_params(axis="x", rotation=45)

    peak_point = monthly_dlq[monthly_dlq["perf_month"] == "2025-12"].loc[
        monthly_dlq[monthly_dlq["perf_month"] == "2025-12"]["dlq_30_rate"].idxmax()
    ]
    peak_x = "2025-12"
    peak_y = peak_point["dlq_30_rate"]
    ax[0, 0].annotate(
        f"2025-12 peak: {peak_y:.1%}",
        xy=(peak_x, peak_y),
        xytext=(peak_x, peak_y + 0.03),
        textcoords="data",
        arrowprops={"arrowstyle": "->", "color": "black"},
        ha="center",
        va="bottom",
        fontsize=9,
    )

    sns.boxplot(
        data=filtered,
        x="risk_band",
        y="utilization",
        order=risk_order,
        ax=ax[0, 1],
    )
    ax[0, 1].axhline(0.80, color="red", linestyle="--", linewidth=1.5, label="High Util Cutoff (0.80)")
    ax[0, 1].legend()
    ax[0, 1].set_title("Utilization Distribution by Risk Band")
    ax[0, 1].set_xlabel("risk_band")
    ax[0, 1].set_ylabel("utilization")

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".1%",
        cmap="YlOrRd",
        cbar_kws={"label": "30+ DPD Rate"},
        ax=ax[1, 0],
    )
    ax[1, 0].set_title("30+ DPD Rate by Vintage Quarter and Risk Band")
    ax[1, 0].set_xlabel("risk_band")
    ax[1, 0].set_ylabel("vintage_quarter")

    bars = ax[1, 1].bar(active_accounts.index.astype(str), active_accounts.values)
    for bar, count in zip(bars, active_accounts.values):
        ax[1, 1].text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.5,
            str(int(count)),
            ha="center",
            va="bottom",
            fontsize=9,
        )
    ax[1, 1].set_title("Active Account Count by Risk Band")
    ax[1, 1].set_xlabel("risk_band")
    ax[1, 1].set_ylabel("active_account_count")

    fig.tight_layout()
    fig.savefig("diagnostics.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()

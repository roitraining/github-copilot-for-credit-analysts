import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


INPUT_FILE = "sample_accounts.csv"
OUTPUT_FILE = "portfolio_summary.png"
RISK_ORDER = ["Prime", "Near-Prime", "Subprime"]


def main() -> None:
    df = pd.read_csv(INPUT_FILE)
    clean_df = df[df["delinquency_days"] <= 365].copy()

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.countplot(
        data=clean_df,
        x="risk_band",
        order=RISK_ORDER,
        ax=axes[0],
    )
    axes[0].set_title("Account Count by Risk Band")
    axes[0].set_xlabel("Risk Band")
    axes[0].set_ylabel("Account Count")
    for bar in axes[0].patches:
        height = bar.get_height()
        axes[0].annotate(
            f"{int(height)}",
            (bar.get_x() + bar.get_width() / 2, height),
            ha="center",
            va="bottom",
            xytext=(0, 3),
            textcoords="offset points",
        )

    sns.boxplot(
        data=clean_df,
        x="risk_band",
        y="utilization",
        order=RISK_ORDER,
        ax=axes[1],
    )
    axes[1].axhline(
        y=0.80,
        color="red",
        linestyle="--",
        label="High Utilization Threshold",
    )
    axes[1].set_title("Utilization by Risk Band")
    axes[1].set_xlabel("Risk Band")
    axes[1].set_ylabel("Utilization")
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(OUTPUT_FILE)
    plt.close(fig)


if __name__ == "__main__":
    main()

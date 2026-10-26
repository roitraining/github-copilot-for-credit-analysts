import csv
import random


OUTPUT_FILE = "sample_accounts.csv"
ROW_COUNT = 50
RISK_BANDS = ["Prime", "Near-Prime", "Subprime"]


def generate_rows() -> list[dict[str, object]]:
    random.seed(42)
    rows: list[dict[str, object]] = []

    for i in range(ROW_COUNT):
        risk_band = RISK_BANDS[i % len(RISK_BANDS)]
        account_id = f"ACC{i + 1:05d}"

        if risk_band == "Prime":
            credit_limit = round(random.uniform(8000, 30000), 2)
            utilization = round(random.uniform(0.10, 0.70), 4)
        elif risk_band == "Near-Prime":
            credit_limit = round(random.uniform(4000, 18000), 2)
            utilization = round(random.uniform(0.20, 0.90), 4)
        else:
            credit_limit = round(random.uniform(1500, 12000), 2)
            utilization = round(random.uniform(0.30, 0.98), 4)

        balance = round(credit_limit * utilization, 2)
        delinquency_days = random.choice([0, 0, 0, 15, 30, 60, 90, 120])

        rows.append(
            {
                "account_id": account_id,
                "risk_band": risk_band,
                "balance": balance,
                "credit_limit": credit_limit,
                "utilization": utilization,
                "delinquency_days": delinquency_days,
            }
        )

    blank_utilization_indices = random.sample(range(ROW_COUNT), 4)
    error_delinquency_indices = random.sample(range(ROW_COUNT), 2)

    for idx in blank_utilization_indices:
        rows[idx]["utilization"] = ""

    for idx in error_delinquency_indices:
        rows[idx]["delinquency_days"] = 9999

    return rows


def write_csv(rows: list[dict[str, object]]) -> None:
    fieldnames = [
        "account_id",
        "risk_band",
        "balance",
        "credit_limit",
        "utilization",
        "delinquency_days",
    ]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = generate_rows()
    write_csv(rows)
    print(f"Wrote {len(rows)} rows to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()

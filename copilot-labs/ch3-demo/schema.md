# Credit Modeling Schema (modeling_accounts.csv)
- `account_id` (string): unique identifier (exclude from features)
- `application_month` (string): YYYY-MM format from 2025-01 to 2025-12
- `risk_band` (string): Prime, Near-Prime, or Subprime
- `balance` (float): balance at application in USD
- `credit_limit` (float): credit limit at application in USD
- `utilization` (float): ratio 0.0 to 1.0 (may contain nulls)
- `default_60d` (int): 1 if 60+ days past due within 12 months, else 0 (target)

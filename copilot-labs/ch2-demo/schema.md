# Credit Accounts Schema (sample_accounts.csv)
- `account_id` (string): unique account identifier
- `risk_band` (string): Prime, Near-Prime, or Subprime
- `balance` (float): current balance in USD
- `credit_limit` (float): credit limit in USD
- `utilization` (float): ratio from 0.0 to 1.0 (may contain blanks)
- `delinquency_days` (int): days past due (9999 indicates a data error)

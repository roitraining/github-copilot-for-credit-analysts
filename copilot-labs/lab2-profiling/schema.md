# Credit Portfolio Schema (portfolio_history.csv)

- `account_id` (string): identifier formatted ACC-2001 to ACC-2500
- `vintage_quarter` (string): origination quarter ('2025-Q1', '2025-Q2', '2025-Q3', '2025-Q4')
- `perf_month` (string): reporting month ('2025-07', '2025-08', '2025-09', '2025-10', '2025-11', '2025-12')
- `risk_band` (string): 'Prime', 'Near-Prime', or 'Subprime'
- `status` (string): 'active' or 'charged_off'
- `balance` (float): current balance in USD (0 to 20000)
- `credit_limit` (float): credit limit in USD (1000 to 25000)
- `utilization` (float): ratio balance / credit_limit (0.0 to 1.2; may contain nulls)
- `dpd` (int): days past due (0, 15, 30, 60, 90, or 9999 for data error)
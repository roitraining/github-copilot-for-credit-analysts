# Credit Modeling Schema (modeling_data.csv)

- `account_id` (string): unique identifier (ACC-3001 to ACC-4000) - exclude from features
- `application_month` (string): origination month ('2025-01' through '2025-12') - use for time split only
- `risk_band` (string): 'Prime', 'Near-Prime', or 'Subprime' (known at application)
- `balance` (float): balance at application in USD
- `credit_limit` (float): credit limit at application in USD
- `utilization` (float): ratio 0.0 to 1.0 at application (contains ~40 nulls)
- `tenure_months` (int): months on book at application (1 to 120)
- `post_decision_dpd` (int): days past due measured 6 months AFTER decision - FORBIDDEN post-decision leak!
- `default_60d` (int): binary target (1 if 60+ DPD within 12 months, else 0)
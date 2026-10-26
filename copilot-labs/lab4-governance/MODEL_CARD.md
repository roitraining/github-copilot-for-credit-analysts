# Model Card: monitoring_rollup

## 1. Module Overview and Intended Use
- **Primary Function**: Monthly delinquency rollup for monitoring data, computed from the account-level input frame and aggregated to the `(perf_month, risk_band)` grain.
- **Output Grain**: `perf_month`, `risk_band`, `active_accounts`, `mean_balance`, and `dlq_30_rate`.

## 2. Input Schema and Exclusion Rules
- **Required Columns**: `account_id`, `perf_month`, `risk_band`, `status`, `balance`, and `dpd`.
- **Charged-Off and Sentinel Exclusions**: Rows with `status == 'charged_off'` are excluded before aggregation, and rows with `dpd > 365` are also excluded. The remaining rows are used to compute `active_accounts`, `mean_balance`, and `dlq_30_rate`; `bad_30` is defined as `dpd >= 30`.

## 3. Runtime Guards and Test Verification
- **Defensive ValueError Guards**:
  - `Missing required columns: {missing_cols}` when required columns are missing.
  - `Input DataFrame is empty` when the input DataFrame is empty.
  - `Duplicate (account_id, perf_month) keys found` when duplicate `(account_id, perf_month)` keys are present.
  - `Zero active valid rows after filtering status == 'charged_off' and dpd > 365` when no rows remain after applying the active-valid filter.
  - `Invalid dlq_30_rate detected; values must be within [0.0, 1.0]` when any output `dlq_30_rate` value is missing or outside `[0.0, 1.0]`.
- **Pytest Suite Summary**: `6 passed in 0.26s` from the recorded pytest run log.

## 4. Governance and Policy Sign-Off
- **Production Alert Threshold**: TODO (Human Policy Owner)
- **Model Risk Reviewer**: TODO (Human Reviewer)
- **Approval Status**: TODO: Pending Human Sign-Off

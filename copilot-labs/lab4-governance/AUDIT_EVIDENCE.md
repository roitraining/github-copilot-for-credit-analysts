# Audit Evidence

This evidence file is based only on the contents of rollup.py, validators.py, test_rollup.py, and pytest_run.txt.

## Scope of Refactoring

- Functions modularized and vectorized.
- `compute_monthly_rollup` in rollup.py calls `validate_monitoring_inputs` and `validate_rollup_outputs` from validators.py.
- The rollup logic keeps the grouped output at the `(perf_month, risk_band)` grain and computes `active_accounts`, `mean_balance`, and `dlq_30_rate` from the filtered input frame.

## Defensive Assertions Inventory

| File | Guard / Function | Condition | ValueError message |
|---|---|---|---|
| validators.py | `validate_monitoring_inputs` | Missing required columns | `Missing required columns: {missing_cols}` |
| validators.py | `validate_monitoring_inputs` | DataFrame is empty | `Input DataFrame is empty` |
| validators.py | `validate_monitoring_inputs` | Duplicate `(account_id, perf_month)` keys | `Duplicate (account_id, perf_month) keys found` |
| validators.py | `validate_monitoring_inputs` | No rows remain after filtering `status != 'charged_off'` and `dpd <= 365` | `Zero active valid rows after filtering status == 'charged_off' and dpd > 365` |
| validators.py | `validate_rollup_outputs` | Any `dlq_30_rate` value is missing or outside `[0.0, 1.0]` | `Invalid dlq_30_rate detected; values must be within [0.0, 1.0]` |

## Pytest Verification Log

The pytest run captured in pytest_run.txt reports:

- `6 passed in 0.26s`

| Test case | Result |
|---|---|
| `test_rollup.py::test_compute_monthly_rollup_expected_values` | PASSED |
| `test_rollup.py::test_compute_monthly_rollup_invalid_inputs[<lambda>-Missing required columns: {'dpd'}]` | PASSED |
| `test_rollup.py::test_compute_monthly_rollup_invalid_inputs[<lambda>-Input DataFrame is empty]` | PASSED |
| `test_rollup.py::test_compute_monthly_rollup_invalid_inputs[<lambda>-Duplicate \(account_id, perf_month\) keys found]` | PASSED |
| `test_rollup.py::test_compute_monthly_rollup_invalid_inputs[<lambda>-Zero active valid rows after filtering status == 'charged_off' and dpd > 365]` | PASSED |
| `test_rollup.py::test_validate_rollup_outputs_invalid_rate_raises` | PASSED |

## Reviewer Sign-Off Checklist

| Field | Value |
|---|---|
| Reviewer Name | TODO |
| Date | TODO |
| Decision | TODO |

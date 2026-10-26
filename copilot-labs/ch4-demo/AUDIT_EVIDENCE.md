# AUDIT EVIDENCE

## 1) Functions changed and vectorized

| File | Function | Vectorized evidence |
|---|---|---|
| `risk_rollup.py` | `calc_delinquency` | Uses Pandas boolean masks (`active_mask`, `bad_mask`), grouped aggregations (`groupby().size()`), indexed alignment (`reindex(fill_value=0)`), and vectorized division (`bad_counts / active_counts`) without row-wise loops. |

## 2) Runtime `ValueError` assertions added

The pytest suite now includes `pytest.raises(ValueError)` checks for:

1. Missing required columns (`Missing required columns ...`)
2. Duplicate `account_id` values
3. A risk band with zero active accounts
4. Output rate outside `[0.0, 1.0]` (forced via monkeypatch of Series division)

## 3) Pytest tests in `test_risk_rollup.py` and pass count

| Test name | Purpose | Result |
|---|---|---|
| `test_calc_delinquency_exact_rates_excludes_charged_off` | Verifies exact `dlq_30_rate` for Prime, Near-Prime, Subprime and confirms `charged_off` exclusion from denominator and numerator | Passed |
| `test_calc_delinquency_raises_for_missing_required_columns` | Missing required column path | Passed |
| `test_calc_delinquency_raises_for_duplicate_account_id` | Duplicate account ID path | Passed |
| `test_calc_delinquency_raises_for_band_with_zero_active_accounts` | Zero active accounts in a band path | Passed |
| `test_calc_delinquency_raises_for_rate_outside_bounds` | Output rate out-of-bounds guard path | Passed |

**Pass count:** **5 / 5 passed**  
**Command run:** `python3 -m pytest -q /Users/doug/copilot-labs/ch4-demo/test_risk_rollup.py` (executed in a temporary virtual environment due missing system pytest)

## 4) Human sign-off

- Reviewer: **TODO**
- Date: **TODO**
- Approval: **TODO**
- Notes: **TODO**

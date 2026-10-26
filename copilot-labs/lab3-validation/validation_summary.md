# Validation Summary

## 1) Model Overview

- **Target column:** `default_60d`
- **Train/Test split (out-of-time):**
  - Train: `application_month < '2025-10'`
  - Test (holdout): `application_month >= '2025-10'`
- **Feature list (from `train_pipeline.py`):**
  - `balance`
  - `credit_limit`
  - `utilization`
  - `tenure_months`
  - `risk_band`

## 2) Holdout Metrics Table

| Metric | Value |
|---|---:|
| train_rows | 751 |
| test_rows | 249 |
| roc_auc | 0.7794670846394984 |
| ks | 0.5021943573667712 |
| brier_score | 0.09188261281696718 |

## 3) 10-Bin Decile Capture Table

| decile | account_count | bad_count | actual_bad_rate | mean_predicted_prob | cum_bad_capture_rate |
|---:|---:|---:|---:|---:|---:|
| 1 | 25 | 9 | 0.36 | 0.29614707976776145 | 0.3103448275862069 |
| 2 | 25 | 7 | 0.28 | 0.20559958823533045 | 0.5517241379310345 |
| 3 | 25 | 3 | 0.12 | 0.15171173860591533 | 0.6551724137931034 |
| 4 | 25 | 4 | 0.16 | 0.12004036838809196 | 0.7931034482758621 |
| 5 | 25 | 3 | 0.12 | 0.0872628340662902 | 0.896551724137931 |
| 6 | 25 | 0 | 0.0 | 0.06420630522014671 | 0.896551724137931 |
| 7 | 25 | 1 | 0.04 | 0.050040606641864036 | 0.9310344827586207 |
| 8 | 25 | 0 | 0.0 | 0.03806383317235808 | 0.9310344827586207 |
| 9 | 25 | 2 | 0.08 | 0.029937076328705556 | 1.0 |
| 10 | 24 | 0 | 0.0 | 0.02169001551242385 | 1.0 |

## 4) Governance and Cutoff Sign-Off

- **Production score cutoff:** TODO
- **Policy exceptions:** TODO
- **Final approval status:** TODO

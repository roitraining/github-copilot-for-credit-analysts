-- 1) Delinquency trend query with month-over-month basis-point change
WITH filtered_portfolio AS (
    SELECT
        account_id,
        perf_month,
        risk_band,
        dpd
    FROM credit_analytics.portfolio_history
    WHERE status != 'charged_off'
      AND dpd <= 365
),
monthly_risk_metrics AS (
    SELECT
        perf_month,
        risk_band,
        COUNT(DISTINCT account_id) AS active_accounts,
        AVG(CASE WHEN dpd >= 30 THEN 1.0 ELSE 0.0 END) AS dlq_30_rate
    FROM filtered_portfolio
    GROUP BY perf_month, risk_band
)
SELECT
    perf_month,
    risk_band,
    active_accounts,
    dlq_30_rate,
    (
        dlq_30_rate
        - LAG(dlq_30_rate) OVER (
            PARTITION BY risk_band
            ORDER BY TO_DATE(perf_month || '-01')
        )
    ) * 10000 AS month_over_month_bp_change
FROM monthly_risk_metrics
ORDER BY TO_DATE(perf_month || '-01'), risk_band;


-- 2) Companion validation query for key duplicates and null checks
WITH duplicate_keys AS (
    SELECT
        account_id,
        perf_month,
        COUNT(*) AS key_count
    FROM credit_analytics.portfolio_history
    GROUP BY account_id, perf_month
    HAVING COUNT(*) > 1
),
null_checks AS (
    SELECT
        SUM(CASE WHEN risk_band IS NULL THEN 1 ELSE 0 END) AS null_risk_band_rows,
        SUM(CASE WHEN utilization IS NULL THEN 1 ELSE 0 END) AS null_utilization_rows
    FROM credit_analytics.portfolio_history
)
SELECT
    COALESCE((SELECT SUM(key_count - 1) FROM duplicate_keys), 0) AS duplicate_account_perf_month_rows,
    COALESCE((SELECT COUNT(*) FROM duplicate_keys), 0) AS duplicate_account_perf_month_keys,
    null_risk_band_rows,
    null_utilization_rows
FROM null_checks;

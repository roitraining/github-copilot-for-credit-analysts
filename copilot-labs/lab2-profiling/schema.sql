CREATE TABLE credit_analytics.portfolio_history (
    account_id VARCHAR(32) NOT NULL,
    vintage_quarter VARCHAR(16) NOT NULL,
    perf_month VARCHAR(7) NOT NULL,
    risk_band VARCHAR(24) NOT NULL,
    status VARCHAR(24) NOT NULL,
    balance DECIMAL(12, 2),
    credit_limit DECIMAL(12, 2),
    utilization DECIMAL(6, 4),
    dpd INTEGER
);
import pandas as pd

def calc_delinquency(df):
    """
    Calculate the 30+ day delinquency rate by risk band.

    Parameters
    ----------
    df : pandas.DataFrame
        Input data containing the required columns: ``account_id``,
        ``risk_band``, ``status``, and ``dpd``.

    Notes
    -----
    Rows with ``status == "charged_off"`` are excluded from the active-account
    denominator and from the delinquency numerator. The resulting delinquency
    rate is computed as the count of accounts with ``dpd >= 30`` among active
    accounts, divided by the total number of active accounts, grouped by
    ``risk_band``.

    Returns
    -------
    pandas.Series
        A Series indexed by ``risk_band`` with values named
        ``dlq_30_rate``. Each value is the delinquency rate for the corresponding
        risk band.

    Raises
    ------
    ValueError
        If any required column is missing from ``df``.
        If ``account_id`` contains duplicate values.
        If any risk band has zero active accounts after excluding
        ``status == "charged_off"`` rows.
        If any computed delinquency rate is outside the inclusive range
        ``[0.0, 1.0]``.
    """
    required_cols = {"account_id", "risk_band", "status", "dpd"}
    missing = required_cols.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    if df["account_id"].duplicated().any():
        raise ValueError("Duplicate account_id values found")

    bands = pd.Index(df["risk_band"].unique())
    active_mask = df["status"] != "charged_off"
    bad_mask = active_mask & (df["dpd"] >= 30)

    active_counts = (
        df.loc[active_mask]
        .groupby("risk_band", sort=False)["account_id"]
        .size()
        .reindex(bands, fill_value=0)
    )
    if (active_counts == 0).any():
        zero_bands = active_counts.index[active_counts == 0].tolist()
        raise ValueError(f"Zero active accounts for risk_band(s): {zero_bands}")

    bad_counts = (
        df.loc[bad_mask]
        .groupby("risk_band", sort=False)["account_id"]
        .size()
        .reindex(bands, fill_value=0)
    )

    rates = (bad_counts / active_counts).rename("dlq_30_rate")
    if ((rates < 0.0) | (rates > 1.0)).any():
        bad_rate_bands = rates.index[((rates < 0.0) | (rates > 1.0))].tolist()
        raise ValueError(f"Delinquency rate outside [0.0, 1.0] for risk_band(s): {bad_rate_bands}")

    return rates

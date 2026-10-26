import base64
from html import escape
from pathlib import Path

import pandas as pd


def markdown_table_to_html(markdown_text: str) -> str:
    lines = [line.strip() for line in markdown_text.splitlines() if line.strip()]
    table_lines = [line for line in lines if line.startswith("|") and line.endswith("|")]
    if len(table_lines) < 3:
        raise ValueError("hypotheses.md does not contain a valid Markdown table.")

    header_cells = [cell.strip() for cell in table_lines[0].strip("|").split("|")]
    body_lines = table_lines[2:]

    header_html = "".join(f"<th>{escape(cell)}</th>" for cell in header_cells)
    body_html_rows = []
    for line in body_lines:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        row_html = "".join(f"<td>{escape(cell)}</td>" for cell in cells)
        body_html_rows.append(f"<tr>{row_html}</tr>")

    return (
        '<table class="hypothesis-table">'
        f"<thead><tr>{header_html}</tr></thead>"
        f"<tbody>{''.join(body_html_rows)}</tbody>"
        "</table>"
    )


def image_to_base64(image_path: Path) -> str:
    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def build_summary_by_band(df: pd.DataFrame) -> dict[str, dict[str, float]]:
    filtered = df[(df["status"] == "active") & (df["dpd"] <= 365)].copy()
    filtered["is_30_plus"] = filtered["dpd"] >= 30

    summary = {}
    for band in ["Prime", "Near-Prime", "Subprime"]:
        subset = filtered[filtered["risk_band"] == band]
        summary[band] = {
            "row_count": int(len(subset)),
            "active_accounts": int(subset["account_id"].nunique()),
            "dlq_30_rate": float(subset["is_30_plus"].mean()) if len(subset) else 0.0,
            "avg_utilization": float(subset["utilization"].mean()) if len(subset) else 0.0,
        }

    summary["All Bands"] = {
        "row_count": int(len(filtered)),
        "active_accounts": int(filtered["account_id"].nunique()),
        "dlq_30_rate": float(filtered["is_30_plus"].mean()) if len(filtered) else 0.0,
        "avg_utilization": float(filtered["utilization"].mean()) if len(filtered) else 0.0,
    }
    return summary


def build_detail_rows(df: pd.DataFrame) -> str:
    filtered = df[(df["status"] == "active") & (df["dpd"] <= 365)].copy()
    filtered = filtered[
        ["account_id", "perf_month", "vintage_quarter", "risk_band", "balance", "utilization", "dpd"]
    ].sort_values(["perf_month", "risk_band", "account_id"])

    rows = []
    for row in filtered.itertuples(index=False):
        rows.append(
            "<tr "
            f'data-risk-band="{escape(str(row.risk_band))}">'
            f"<td>{escape(str(row.account_id))}</td>"
            f"<td>{escape(str(row.perf_month))}</td>"
            f"<td>{escape(str(row.vintage_quarter))}</td>"
            f"<td>{escape(str(row.risk_band))}</td>"
            f"<td>{row.balance:,.2f}</td>"
            f"<td>{row.utilization:.4f}</td>"
            f"<td>{int(row.dpd)}</td>"
            "</tr>"
        )
    return "".join(rows)


def main() -> None:
    csv_path = Path("portfolio_history.csv")
    diag_path = Path("diagnostics.png")
    hypotheses_path = Path("hypotheses.md")

    for p in [csv_path, diag_path, hypotheses_path]:
        if not p.exists():
            raise FileNotFoundError(f"Required input file not found: {p}")

    df = pd.read_csv(csv_path)
    hypotheses_html = markdown_table_to_html(hypotheses_path.read_text(encoding="utf-8"))
    diagnostics_image_src = image_to_base64(diag_path)
    summary = build_summary_by_band(df)
    detail_rows_html = build_detail_rows(df)

    summary_json = {
        key: {
            "row_count": value["row_count"],
            "active_accounts": value["active_accounts"],
            "dlq_30_rate": round(value["dlq_30_rate"] * 100, 2),
            "avg_utilization": round(value["avg_utilization"] * 100, 2),
        }
        for key, value in summary.items()
    }

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Portfolio EDA Report</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 24px;
      color: #222;
      background: #fafafa;
    }}
    h1, h2 {{
      margin-bottom: 8px;
    }}
    .section {{
      background: #fff;
      border: 1px solid #e6e6e6;
      border-radius: 8px;
      padding: 16px;
      margin-bottom: 18px;
    }}
    .filters {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin: 8px 0 12px;
    }}
    .filter-btn {{
      border: 1px solid #d0d0d0;
      background: #fff;
      padding: 8px 12px;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
    }}
    .filter-btn.active {{
      background: #1f6feb;
      color: #fff;
      border-color: #1f6feb;
    }}
    .kpis {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 10px;
      margin-bottom: 12px;
    }}
    .kpi {{
      background: #f6f8fa;
      border: 1px solid #e8ecf1;
      border-radius: 6px;
      padding: 10px;
    }}
    .kpi .label {{
      display: block;
      font-size: 12px;
      color: #555;
      margin-bottom: 4px;
    }}
    .kpi .value {{
      font-size: 18px;
      font-weight: bold;
    }}
    img {{
      max-width: 100%;
      border: 1px solid #ddd;
      border-radius: 6px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
    }}
    th, td {{
      border: 1px solid #e0e0e0;
      padding: 6px 8px;
      text-align: left;
    }}
    th {{
      background: #f3f6f8;
    }}
    .detail-table-wrap {{
      max-height: 360px;
      overflow: auto;
      border: 1px solid #e0e0e0;
      border-radius: 6px;
    }}
  </style>
</head>
<body>
  <h1>Credit Portfolio EDA Report</h1>
  <p>Data source: <code>portfolio_history.csv</code> filtered interactively by risk band.</p>

  <div class="section">
    <h2>Interactive Risk Band Filters</h2>
    <div class="filters">
      <button class="filter-btn active" data-band="All Bands">All Bands</button>
      <button class="filter-btn" data-band="Prime">Prime</button>
      <button class="filter-btn" data-band="Near-Prime">Near-Prime</button>
      <button class="filter-btn" data-band="Subprime">Subprime</button>
    </div>
    <div class="kpis">
      <div class="kpi"><span class="label">Rows</span><span class="value" id="kpi-rows"></span></div>
      <div class="kpi"><span class="label">Active Accounts</span><span class="value" id="kpi-accounts"></span></div>
      <div class="kpi"><span class="label">30+ DPD Rate</span><span class="value" id="kpi-dlq"></span></div>
      <div class="kpi"><span class="label">Avg Utilization</span><span class="value" id="kpi-util"></span></div>
    </div>
    <div class="detail-table-wrap">
      <table>
        <thead>
          <tr>
            <th>account_id</th>
            <th>perf_month</th>
            <th>vintage_quarter</th>
            <th>risk_band</th>
            <th>balance</th>
            <th>utilization</th>
            <th>dpd</th>
          </tr>
        </thead>
        <tbody id="detail-body">
          {detail_rows_html}
        </tbody>
      </table>
    </div>
  </div>

  <div class="section">
    <h2>Diagnostics Figure</h2>
    <img src="{diagnostics_image_src}" alt="Portfolio diagnostics charts" />
  </div>

  <div class="section">
    <h2>Hypotheses Table</h2>
    {hypotheses_html}
  </div>

  <script>
    const summary = {summary_json};
    const buttons = Array.from(document.querySelectorAll(".filter-btn"));
    const rows = Array.from(document.querySelectorAll("#detail-body tr"));

    function updateKPIs(band) {{
      const metrics = summary[band];
      document.getElementById("kpi-rows").textContent = metrics.row_count.toLocaleString();
      document.getElementById("kpi-accounts").textContent = metrics.active_accounts.toLocaleString();
      document.getElementById("kpi-dlq").textContent = metrics.dlq_30_rate.toFixed(2) + "%";
      document.getElementById("kpi-util").textContent = metrics.avg_utilization.toFixed(2) + "%";
    }}

    function applyFilter(band) {{
      rows.forEach((row) => {{
        const rowBand = row.getAttribute("data-risk-band");
        row.style.display = band === "All Bands" || rowBand === band ? "" : "none";
      }});
      buttons.forEach((btn) => btn.classList.toggle("active", btn.dataset.band === band));
      updateKPIs(band);
    }}

    buttons.forEach((btn) => {{
      btn.addEventListener("click", () => applyFilter(btn.dataset.band));
    }});

    applyFilter("All Bands");
  </script>
</body>
</html>
"""

    Path("eda_report.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    main()

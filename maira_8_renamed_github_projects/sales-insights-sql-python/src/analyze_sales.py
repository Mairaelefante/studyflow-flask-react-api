from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_orders.csv"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["order_date"])
    df["net_revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount_pct"])
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    valid = df[df["returned"].eq("No")]
    summary = (
        valid.groupby(["month", "region"], as_index=False)
        .agg(net_revenue=("net_revenue", "sum"), orders=("order_id", "count"), units=("quantity", "sum"))
        .sort_values(["month", "net_revenue"], ascending=[True, False])
    )
    summary["net_revenue"] = summary["net_revenue"].round(2)
    return summary


def create_visual(df: pd.DataFrame) -> None:
    monthly = df[df["returned"].eq("No")].groupby("month")["net_revenue"].sum()
    ax = monthly.plot(kind="bar", title="Monthly Net Revenue")
    ax.set_xlabel("Month")
    ax.set_ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(REPORTS / "monthly_revenue.png")
    plt.close()


def main() -> None:
    df = load_data(DATA)
    summary = build_summary(df)
    summary.to_csv(REPORTS / "monthly_region_summary.csv", index=False)
    create_visual(df)
    return_rate = (df["returned"].eq("Yes").mean() * 100).round(2)
    with open(REPORTS / "stakeholder_summary.md", "w", encoding="utf-8") as f:
        f.write("# Stakeholder Summary\n\n")
        f.write(f"Total orders analyzed: {len(df)}\n\n")
        f.write(f"Overall return rate: {return_rate}%\n\n")
        f.write("Key recommendation: monitor high-discount hardware orders and compare channel-level performance monthly.\n")


if __name__ == "__main__":
    main()

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

def main() -> None:
    df = pd.read_csv(ROOT / "data" / "customer_churn.csv")
    df.describe(include="all").to_csv(REPORTS / "eda_summary.csv")
    churn_by_plan = df.groupby("plan_type")["churned"].mean().sort_values(ascending=False)
    ax = churn_by_plan.plot(kind="bar", title="Churn Rate by Plan Type")
    ax.set_xlabel("Plan Type")
    ax.set_ylabel("Churn Rate")
    plt.tight_layout()
    plt.savefig(REPORTS / "churn_by_plan.png")
    plt.close()

if __name__ == "__main__":
    main()

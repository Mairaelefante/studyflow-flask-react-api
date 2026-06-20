from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)


def main() -> None:
    df = pd.read_csv(ROOT / "data" / "customer_churn.csv")
    X = df.drop(columns=["customer_id", "churned"])
    y = df["churned"]

    numeric = ["age", "monthly_spend", "support_tickets", "months_active", "uses_mobile_app"]
    categorical = ["plan_type"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
        ]
    )

    model = Pipeline(
        steps=[
            ("preprocess", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    report = classification_report(y_test, preds, zero_division=0)
    acc = accuracy_score(y_test, preds)
    cm = confusion_matrix(y_test, preds)

    with open(REPORTS / "model_report.md", "w", encoding="utf-8") as f:
        f.write("# Churn Model Report\n\n")
        f.write(f"Accuracy: {acc:.2f}\n\n")
        f.write("## Classification Report\n\n")
        f.write("```\n" + report + "\n```\n")
        f.write("## Confusion Matrix\n\n")
        f.write(str(cm))
        f.write("\n\n## Interpretation\n")
        f.write("This small portfolio dataset is used to demonstrate the workflow. A production model would require more data, validation, monitoring, and bias checks.\n")


if __name__ == "__main__":
    main()

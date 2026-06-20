from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "student_performance.csv"

def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    required = {"study_hours_week", "attendance_rate", "previous_score", "tutoring_support", "internet_access", "passed"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df

def build_features(df: pd.DataFrame):
    df = df.copy()
    df["study_attendance_interaction"] = df["study_hours_week"] * (df["attendance_rate"] / 100)
    features = ["study_hours_week", "attendance_rate", "previous_score", "tutoring_support", "internet_access", "study_attendance_interaction"]
    return df[features], df["passed"]

def train_and_evaluate():
    df = load_data(DATA_PATH)
    X, y = build_features(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    models = {
        "Logistic Regression": Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression(max_iter=1000))]),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print(f"
=== {name} ===")
        print(f"Accuracy: {accuracy_score(y_test, predictions):.3f}")
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, predictions))
        print("Classification Report:")
        print(classification_report(y_test, predictions, zero_division=0))

if __name__ == "__main__":
    train_and_evaluate()

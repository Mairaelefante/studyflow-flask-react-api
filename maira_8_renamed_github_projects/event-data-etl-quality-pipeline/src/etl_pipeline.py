from pathlib import Path
import logging
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "events.csv"
PROCESSED = ROOT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOGS / "etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def extract(path: Path) -> pd.DataFrame:
    logging.info("Extracting raw data from %s", path)
    return pd.read_csv(path)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting transformation")
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")
    df["value"] = pd.to_numeric(df["value"], errors="coerce").fillna(0)
    df = df.dropna(subset=["event_time", "user_id"])
    df = df.drop_duplicates(subset=["event_id"])
    df["event_date"] = df["event_time"].dt.date.astype(str)
    df["is_revenue_event"] = df["event_type"].eq("purchase")
    return df


def validate(df: pd.DataFrame) -> None:
    logging.info("Validating transformed data")
    required = {"event_id", "event_time", "user_id", "event_type", "source"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df["event_id"].duplicated().any():
        raise ValueError("Duplicate event_id detected")
    if df["user_id"].isna().any():
        raise ValueError("Null user_id detected after cleaning")


def load(df: pd.DataFrame) -> None:
    output = PROCESSED / "clean_events.csv"
    df.to_csv(output, index=False)
    daily = (
        df.groupby(["event_date", "event_type"], as_index=False)
        .agg(events=("event_id", "count"), revenue=("value", "sum"))
    )
    daily.to_csv(PROCESSED / "daily_event_summary.csv", index=False)
    logging.info("Saved processed files to %s", PROCESSED)


def main() -> None:
    df = extract(RAW)
    clean = transform(df)
    validate(clean)
    load(clean)
    print("ETL completed successfully")


if __name__ == "__main__":
    main()

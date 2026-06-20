from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_PATH = BASE_DIR / "data" / "raw_customers.csv"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_PATH = OUTPUT_DIR / "clean_customers.csv"

def standardize_columns(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    return df

def clean_customer_data(df):
    df = standardize_columns(df).drop_duplicates()
    df["country"] = df["country"].fillna("unknown").str.strip().str.title().replace({"Usa": "United States"})
    df["plan"] = df["plan"].str.strip().str.lower()
    df["monthly_spend"] = pd.to_numeric(df["monthly_spend"], errors="coerce")
    df["monthly_spend"] = df.groupby("plan")["monthly_spend"].transform(lambda s: s.fillna(s.median()))
    df["age"] = pd.to_numeric(df["age"], errors="coerce").fillna(df["age"].median()).astype(int)
    df["support_tickets"] = pd.to_numeric(df["support_tickets"], errors="coerce").fillna(0).astype(int)
    df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")
    df["last_login"] = pd.to_datetime(df["last_login"], errors="coerce")
    df["has_logged_in"] = df["last_login"].notna().astype(int)
    df["high_value_customer"] = (df["monthly_spend"] >= 29.99).astype(int)
    return df.sort_values("customer_id")

def main():
    clean_df = clean_customer_data(pd.read_csv(RAW_PATH))
    OUTPUT_DIR.mkdir(exist_ok=True)
    clean_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Saved cleaned data to {OUTPUT_PATH}")
    print(clean_df.head())

if __name__ == "__main__":
    main()

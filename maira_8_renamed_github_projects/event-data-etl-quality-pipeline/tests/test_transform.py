import pandas as pd
from src.etl_pipeline import transform


def test_transform_removes_invalid_rows():
    df = pd.DataFrame({
        "event_id": [1, 2],
        "event_time": ["2026-01-01 10:00:00", "bad_timestamp"],
        "user_id": ["U001", "U002"],
        "event_type": ["page_view", "purchase"],
        "value": [None, 10],
        "source": ["web", "mobile"],
    })
    clean = transform(df)
    assert len(clean) == 1
    assert clean.iloc[0]["user_id"] == "U001"

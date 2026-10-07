import pandas as pd
from src.data_processing import validate_schema, clean_data

def test_validate_schema_valid():
    df = pd.DataFrame({"Jam Tatap Muka": [1], "Jam Online": [2], "Nilai Akhir": [80]})
    is_valid, missing = validate_schema(df)
    assert is_valid is True
    assert len(missing) == 0

def test_validate_schema_invalid():
    df = pd.DataFrame({"Jam Tatap Muka": [1], "Nilai Akhir": [80]})
    is_valid, missing = validate_schema(df)
    assert is_valid is False
    assert "Jam Online" in missing

def test_clean_data_handles_missing_and_duplicates():
    df = pd.DataFrame({
        "Jam Tatap Muka": [10, 10, None, 15],
        "Jam Online": [15, 15, 12, 10],
        "Nilai Akhir": [80, 80, 85, None]
    })
    
    cleaned_df, stats = clean_data(df)
    
    assert cleaned_df.shape[0] == 1
    assert stats["duplicates_removed"] == 1
    assert stats["missing_removed"] == 2
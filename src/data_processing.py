import pandas as pd

def validate_schema(df: pd.DataFrame) -> tuple[bool, list[str]]:
    """
    Memeriksa apakah dataframe memiliki kolom yang diwajibkan.
    """
    required_columns = ["Jam Tatap Muka", "Jam Online", "Nilai Akhir"]
    missing = [col for col in required_columns if col not in df.columns]
    
    if missing:
        return False, missing
    return True, []

def clean_data(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Membersihkan data dari nilai kosong dan duplikat.
    Mengembalikan dataframe bersih dan metrik pembersihan.
    """
    initial_rows = df.shape[0]
    
    # Hapus duplikat
    df_clean = df.drop_duplicates()
    after_duplicates = df_clean.shape[0]
    
    # Hapus baris dengan nilai kosong (NaN)
    df_clean = df_clean.dropna(subset=["Jam Tatap Muka", "Jam Online", "Nilai Akhir"])
    after_missing = df_clean.shape[0]
    
    # Pastikan data numerik
    for col in ["Jam Tatap Muka", "Jam Online", "Nilai Akhir"]:
        df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce")
        
    df_clean = df_clean.dropna()
    final_rows = df_clean.shape[0]
    
    stats = {
        "duplicates_removed": initial_rows - after_duplicates,
        "missing_removed": after_duplicates - final_rows
    }
    
    return df_clean, stats

def get_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Mengembalikan matriks korelasi untuk kolom yang relevan."""
    return df[["Jam Tatap Muka", "Jam Online", "Nilai Akhir"]].corr()
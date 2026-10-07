import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Prediksi", layout="wide")

st.title("Prediksi Nilai Akhir")

if "df" not in st.session_state or st.session_state.df is None:
    st.warning("Data belum dimuat. Silakan kembali ke halaman utama.")
else:
    df = st.session_state.df
    
    if df.shape[0] < 5:
        st.error("Data tidak mencukupi untuk memprediksi.")
    else:
        # Latih ulang model menggunakan seluruh data untuk prediksi
        X = df[["Jam Tatap Muka", "Jam Online"]]
        y = df["Nilai Akhir"]
        
        model = LinearRegression()
        model.fit(X, y)
        
        st.markdown("Masukkan estimasi jam pembelajaran untuk melihat prediksi nilai akhir.")
        
        col1, col2 = st.columns(2)
        
        min_tm = float(X["Jam Tatap Muka"].min())
        max_tm = float(X["Jam Tatap Muka"].max())
        min_ol = float(X["Jam Online"].min())
        max_ol = float(X["Jam Online"].max())
        
        with col1:
            input_tm = st.number_input(
                "Jam Tatap Muka", 
                value=min_tm,
                help=f"Rentang pada data latih: {min_tm} - {max_tm}"
            )
            
        with col2:
            input_ol = st.number_input(
                "Jam Online", 
                value=min_ol,
                help=f"Rentang pada data latih: {min_ol} - {max_ol}"
            )
            
        is_extrapolation = (
            input_tm < min_tm or input_tm > max_tm or
            input_ol < min_ol or input_ol > max_ol
        )
        
        if is_extrapolation:
            st.warning("Perhatian: Nilai yang Anda masukkan berada di luar rentang observasi data latih (Ekstrapolasi). Hasil prediksi mungkin kurang akurat.")
            
        if st.button("Hitung Prediksi", type="primary"):
            prediction = model.predict(pd.DataFrame({
                "Jam Tatap Muka": [input_tm],
                "Jam Online": [input_ol]
            }))[0]
            
            st.success("Perhitungan Selesai")
            st.metric("Prediksi Nilai Akhir", f"{prediction:.2f}")
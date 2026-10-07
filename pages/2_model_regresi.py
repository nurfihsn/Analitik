import streamlit as st
from src.modeling import train_and_evaluate
from src.visualization import plot_actual_vs_predicted

st.set_page_config(page_title="Model Regresi", layout="wide")

st.title("Hasil Analisis Regresi Linier")

if "df" not in st.session_state or st.session_state.df is None:
    st.warning("Data belum dimuat. Silakan kembali ke halaman utama.")
else:
    df = st.session_state.df
    
    # Validasi jumlah data minimum
    if df.shape[0] < 5:
        st.error("Jumlah data terlalu sedikit untuk melatih model regresi. Diperlukan minimal 5 baris data.")
    else:
        model, metrics, X_test, y_test, y_pred = train_and_evaluate(df)
        
        st.subheader("Metrik Evaluasi Model")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("R-Squared (R²)", f"{metrics['r2']:.4f}")
        col2.metric("Mean Absolute Error (MAE)", f"{metrics['mae']:.2f}")
        col3.metric("Root Mean Squared Error (RMSE)", f"{metrics['rmse']:.2f}")
        col4.metric("Mean Squared Error (MSE)", f"{metrics['mse']:.2f}")
        
        st.write("---")
        
        st.subheader("Persamaan Regresi")
        coef_tm = model.coef_[0]
        coef_ol = model.coef_[1]
        intercept = model.intercept_
        
        st.code(f"Nilai Akhir = {intercept:.2f} + ({coef_tm:.2f} × Jam Tatap Muka) + ({coef_ol:.2f} × Jam Online)", language="text")
        
        st.markdown("### Interpretasi Koefisien")
        st.markdown(f"""
        - **Intersep ({intercept:.2f}):** Estimasi nilai akhir dasar apabila jam tatap muka dan jam online adalah nol.
        - **Jam Tatap Muka ({coef_tm:.2f}):** Jika asumsi variabel lain konstan, setiap penambahan 1 jam tatap muka berasosiasi dengan perubahan nilai akhir sebesar {coef_tm:.2f} poin.
        - **Jam Online ({coef_ol:.2f}):** Jika asumsi variabel lain konstan, setiap penambahan 1 jam online berasosiasi dengan perubahan nilai akhir sebesar {coef_ol:.2f} poin.
        """)
        
        st.write("---")
        st.subheader("Visualisasi Prediksi")
        fig = plot_actual_vs_predicted(y_test, y_pred)
        st.pyplot(fig, clear_figure=True)
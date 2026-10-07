import streamlit as st
import numpy as np
from src.linear_algebra import compute_design_matrix, compute_coefficients_pinv, format_matrix_latex

st.set_page_config(page_title="Aljabar Linier", layout="wide")

st.title("Landasan Matematika: Aljabar Linier")

st.markdown("""
Model Regresi Linier Berganda dapat diekspresikan dengan elegan menggunakan notasi matriks dalam Aljabar Linier:
""")

st.latex(r"y = X\beta + \epsilon")

st.markdown("""
Keterangan:
- **y**: Vektor target (Nilai Akhir)
- **X**: Matriks Desain (fitur input, ditambahkan kolom angka 1 untuk intersep)
- **β (Beta)**: Vektor koefisien yang dicari
- **ε (Epsilon)**: Vektor residu (kesalahan)
""")

if "df" not in st.session_state or st.session_state.df is None:
    st.warning("Unggah data terlebih dahulu di halaman utama untuk melihat kalkulasi matriks.")
else:
    df = st.session_state.df
    X_df = df[["Jam Tatap Muka", "Jam Online"]]
    y_series = df["Nilai Akhir"]
    
    X_design = compute_design_matrix(X_df)
    beta = compute_coefficients_pinv(X_design, y_series)
    
    st.write("---")
    st.subheader("Perhitungan dari Dataset Anda")
    st.markdown("Berikut adalah representasi matriks dari 5 baris pertama dataset yang Anda gunakan:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matriks Desain (X)**")
        st.latex(format_matrix_latex(X_design, max_rows=5, name="X"))
    
    with col2:
        st.markdown("**Vektor Target (y)**")
        st.latex(format_matrix_latex(y_series.to_numpy().reshape(-1, 1), max_rows=5, name="y"))
        
    st.write("---")
    st.subheader("Penyelesaian Kuadrat Terkecil (Least Squares)")
    st.markdown("""
    Secara teori, nilai koefisien yang meminimalkan kesalahan (residu) dihitung menggunakan **Persamaan Normal (Normal Equation)**:
    """)
    st.latex(r"\beta = (X^T X)^{-1} X^T y")
    
    st.markdown("""
    Namun, menghitung invers dari matriks $(X^T X)$ secara langsung tidak stabil secara numerik jika fitur saling berkorelasi tinggi (matriks singular atau hampir singular). 
    Oleh karena itu, aplikasi ini menggunakan **Invers Semu Moore-Penrose (Pseudo-Inverse)** yang jauh lebih stabil dan andal:
    """)
    st.latex(r"\beta = X^+ y")
    
    st.markdown("**Hasil Perhitungan Koefisien (Beta):**")
    st.latex(format_matrix_latex(beta.reshape(-1, 1), max_rows=3, name=r"\beta"))
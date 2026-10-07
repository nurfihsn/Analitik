import streamlit as st
from src.data_processing import get_correlation_matrix
from src.visualization import plot_correlation_heatmap, plot_distribution

st.set_page_config(page_title="Eksplorasi Data", layout="wide")

st.title("Eksplorasi Data")

if "df" not in st.session_state or st.session_state.df is None:
    st.warning("Data belum dimuat. Silakan kembali ke halaman utama untuk mengunggah data.")
else:
    df = st.session_state.df
    
    st.subheader("Pratinjau Dataset")
    st.dataframe(df, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Statistik Deskriptif")
        st.dataframe(df.describe(), use_container_width=True)
        
    with col2:
        st.subheader("Korelasi Antar Variabel")
        corr = get_correlation_matrix(df)
        fig_corr = plot_correlation_heatmap(corr)
        st.pyplot(fig_corr, clear_figure=True)
        
    st.write("---")
    st.subheader("Analisis Distribusi")
    
    feature_to_plot = st.selectbox("Pilih variabel untuk melihat distribusi:", df.columns)
    fig_dist = plot_distribution(df, feature_to_plot)
    st.pyplot(fig_dist, clear_figure=True)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.style.use("default")
sns.set_theme(style="whitegrid")

def plot_correlation_heatmap(corr_matrix: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.heatmap(corr_matrix, annot=True, cmap="Blues", fmt=".2f", ax=ax)
    ax.set_title("Matriks Korelasi")
    return fig

def plot_distribution(df: pd.DataFrame, column: str):
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df[column], kde=True, color="#3b82f6", bins=10, ax=ax)
    ax.set_title(f"Distribusi {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Frekuensi")
    return fig

def plot_actual_vs_predicted(y_actual, y_pred):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(y_actual, y_pred, alpha=0.7, color="#3b82f6")
    
    # Garis referensi ideal
    min_val = min(y_actual.min(), y_pred.min())
    max_val = max(y_actual.max(), y_pred.max())
    ax.plot([min_val, max_val], [min_val, max_val], "--", color="gray", label="Garis Ideal")
    
    ax.set_title("Nilai Aktual vs Prediksi")
    ax.set_xlabel("Aktual")
    ax.set_ylabel("Prediksi")
    ax.legend()
    return fig
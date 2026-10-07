import numpy as np
import pandas as pd

def compute_design_matrix(X_df: pd.DataFrame) -> np.ndarray:
    """
    Membuat Matriks Desain (X) dengan menambahkan kolom nilai 1
    sebagai intersep (bias) di kolom pertama.
    """
    X_mat = X_df.to_numpy()
    ones = np.ones((X_mat.shape[0], 1))
    return np.hstack((ones, X_mat))

def compute_coefficients_pinv(X_design: np.ndarray, y_series: pd.Series) -> np.ndarray:
    """
    Menghitung vektor koefisien (Beta) menggunakan invers semu (pseudo-inverse).
    Rumus: Beta = pinv(X) * y
    Pendekatan ini lebih stabil secara numerik dibanding (X^T X)^-1 X^T y.
    """
    y_vec = y_series.to_numpy()
    pinv_X = np.linalg.pinv(X_design)
    return pinv_X @ y_vec

def format_matrix_latex(mat: np.ndarray, max_rows: int = 5, name: str = "X") -> str:
    """
    Mengubah numpy array menjadi representasi string LaTeX untuk Streamlit.
    """
    rows = min(len(mat), max_rows)
    latex_str = f"{name} = \\begin{{bmatrix}}\n"
    
    for i in range(rows):
        row_vals = np.atleast_1d(mat[i])
        row_str = " & ".join([f"{val:.2f}" for val in row_vals])
        latex_str += f"{row_str} \\\\\n"
        
    if len(mat) > max_rows:
        cols = 1 if len(mat.shape) == 1 else mat.shape[1]
        latex_str += " & ".join(["\\vdots"] * cols) + " \\\\\n"
        
    latex_str += "\\end{bmatrix}"
    return latex_str
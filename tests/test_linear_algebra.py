import pandas as pd
import numpy as np
from src.linear_algebra import compute_design_matrix, compute_coefficients_pinv

def test_compute_design_matrix():
    df = pd.DataFrame({
        "X1": [2, 4],
        "X2": [3, 5]
    })
    
    X_design = compute_design_matrix(df)
    
    # Harus memiliki bentuk (2 observasi, 3 kolom termasuk bias)
    assert X_design.shape == (2, 3)
    # Kolom pertama harus bernilai 1
    np.testing.assert_array_equal(X_design[:, 0], np.array([1, 1]))
    # Sisa kolom harus sama dengan data asli
    np.testing.assert_array_equal(X_design[:, 1:], df.to_numpy())

def test_compute_coefficients():
    # Setup data sederhana y = 2 + 3*X1
    df_X = pd.DataFrame({"X1": [1, 2, 3]})
    y = pd.Series([5, 8, 11])
    
    X_design = compute_design_matrix(df_X)
    beta = compute_coefficients_pinv(X_design, y)
    
    # Toleransi untuk operasi floating point
    np.testing.assert_almost_equal(beta[0], 2.0, decimal=5)
    np.testing.assert_almost_equal(beta[1], 3.0, decimal=5)
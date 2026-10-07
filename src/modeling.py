import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def train_and_evaluate(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42):
    """
    Melatih model regresi linier dan menghitung metrik evaluasi.
    """
    X = df[["Jam Tatap Muka", "Jam Online"]]
    y = df["Nilai Akhir"]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    metrics = {
        "r2": r2_score(y_test, y_pred),
        "mse": mean_squared_error(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
        "mae": mean_absolute_error(y_test, y_pred)
    }
    
    return model, metrics, X_test, y_test, y_pred
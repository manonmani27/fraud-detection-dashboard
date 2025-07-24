import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):
    # Drop missing values (as you already had)
    df = df.dropna()

    # Encode categorical columns
    df = pd.get_dummies(df, columns=["location", "device", "time"])

    # Scale numeric columns
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df, scaler

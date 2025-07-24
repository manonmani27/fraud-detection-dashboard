import pandas as pd
from sklearn.model_selection import train_test_split
from src.preprocessing import preprocess_data
from src.model import train_model

df = pd.read_csv("data/transactions.csv")
X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]
X, _ = preprocess_data(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = train_model(X_train, y_train)

# Save the model to models/fraud_model.pkl
import joblib
joblib.dump(model, "models/fraud_model.pkl")

print("✅ Model trained and saved to models/fraud_model.pkl!")

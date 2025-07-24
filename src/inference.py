import joblib

def predict_fraud(X):
    model = joblib.load("models/fraud_model.pkl")
    return model.predict(X), model.predict_proba(X)[:, 1]
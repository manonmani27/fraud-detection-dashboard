from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(X, y):
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X, y)
    joblib.dump(clf, "models/fraud_model.pkl")
    return clf

# 💰 Fraud Detection Dashboard

An interactive web app built with Streamlit that detects potential financial fraud using machine learning.

## 🚀 Features

- 📁 Upload transaction CSV files
- 📊 View risk scores for each transaction
- 📈 Visualize fraud risk by location and device
- 🎛️ Filter by risk threshold, location, and device
- ⬇️ Download results as an Excel file
- 🛎️ (Optional) Trigger email alerts for high-risk transactions

## 🖼️ Demo Screenshot

![Dashboard Screenshot](https://raw.githubusercontent.com/manonmani27/fraud-detection-dashboard/main/assets/dashboard_preview.png)

## 📦 How to Use

1. Upload a CSV file with transaction data
2. Adjust the fraud risk threshold slider
3. Filter by device or location
4. View insights and download flagged results

## 📂 Sample Input Format

| transaction_id | amount | location | device | ... |
|----------------|--------|----------|--------|-----|
| TXN1234        | 120.45 | New York | Mobile | ... |

Use the provided `data/sample_transactions.csv` as a reference.

## 🧠 Model

- Trained using `sklearn` with a logistic regression model
- Pickle file: `models/fraud_model.pkl`

## 🔗 Live App

👉 [Launch Fraud Detection App on Streamlit](https://fraud-detection-dashboard.streamlit.app)

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- Matplotlib / Plotly

## 📄 License

MIT License

---

👤 Maintained by [@manonmani27](https://github.com/manonmani27)

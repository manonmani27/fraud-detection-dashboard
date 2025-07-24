# 💰 Fraud Detection Dashboard

An interactive web app built with Streamlit that detects potential financial fraud using machine learning.

## 🚀 Features

- 📁 Upload transaction CSV files
- 📊 View risk scores for each transaction
- 📈 Visualize fraud risk by location and device
- 🎛️ Filter by risk threshold, location, and device
- ⬇️ Download results as an Excel file
- 🛎️ (Optional) Trigger email alerts for high-risk transactions

## 🖼️ Demo Screenshots

### 🔍 Dashboard View – Page 1
![Page 1](assets/fraud_dashboard_1.jpg)

### 📊 Dashboard View – Page 2
![Page 2](assets/fraud_dashboard_2.jpg)

## 📦 How to Use

1. Upload a CSV file with transaction data  
   *(or let the app auto-load the sample file if none is uploaded)*
2. Adjust the fraud risk threshold slider
3. Filter by device or location
4. View insights and download flagged results

## 📂 Sample Input Format

A sample input file is available at: `data/sample_transactions.csv`

| transaction_id | amount | location | device | ... |
|----------------|--------|----------|--------|-----|
| TXN1234        | 120.45 | New York | Mobile | ... |

This file is automatically loaded in the app when no file is uploaded manually.

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


# 💳 Financial Fraud Detection Dashboard

This project is a machine learning-powered fraud detection dashboard that assigns **fraud risk scores** to transaction data. It uses a **logistic regression model** to identify potentially fraudulent transactions, providing an interactive interface for filtering and downloading predictions.

🔗 **Live App**: [Open in Streamlit Cloud](https://manonmani27-fraud-detection-dashboard.streamlit.app/)  
📂 **Repository**: [GitHub Repo](https://github.com/manonmani27/fraud-detection-dashboard)

---

## 📌 Features

- Upload transaction CSV files
- Predict and score fraud risk (0 to 1)
- Filter transactions by:
  - Location
  - Device (Web/Mobile)
  - Risk Threshold
- Visualizations:
  - Risk distribution histogram
  - Grouped bar charts (Device vs. Location)
- Download predictions as CSV

---

## 🧠 Model Details

- **Model**: Logistic Regression (scikit-learn)
- **Output**: Continuous risk score (0 to 1)
- **Accuracy**: ~95.2% on test data
- **Deployment**: Via Streamlit with a pickled model (`fraud_model.pkl`)

---

## 🖼️ Screenshots

> Drag and drop below to view full dashboard visuals

### 1. Main Dashboard & Data Preview

![Dashboard 1](https://raw.githubusercontent.com/manonmani27/fraud-detection-dashboard/main/0.png)

### 2. Filtered Transactions & Risk Scores

![Dashboard 2](https://raw.githubusercontent.com/manonmani27/fraud-detection-dashboard/main/00.png)

### 3. Average Risk by Device

![Dashboard 3](https://raw.githubusercontent.com/manonmani27/fraud-detection-dashboard/main/1.png)

### 4. Grouped Bar: Web vs Mobile by Location

![Dashboard 4](https://raw.githubusercontent.com/manonmani27/fraud-detection-dashboard/main/2.png)

### 5. Full Risk Table + Download Option

![Dashboard 5](https://raw.githubusercontent.com/manonmani27/fraud-detection-dashboard/main/3.png)

---

## 🗂️ Dataset Format

The uploaded `.csv` file must contain the following columns:

```csv
amount,location,device,time,is_fraud
1200,Mumbai,Mobile,10:30,0
3000,Delhi,Web,11:00,1
...
```

---

## ⚙️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- joblib
- matplotlib

---

## 📁 Folder Structure

```
fraud-detection-dashboard/
├── app.py
├── models/
│   └── fraud_model.pkl
├── src/
│   ├── inference.py
│   ├── model.py
│   └── preprocessing.py
├── data/
│   └── sample_transactions.csv
├── README.md
```

---

## 📥 Installation

```bash
git clone https://github.com/manonmani27/fraud-detection-dashboard.git
cd fraud-detection-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## 📢 Contact

**Manonmani**  
📧 manonmaniimurali@gmail.com

---

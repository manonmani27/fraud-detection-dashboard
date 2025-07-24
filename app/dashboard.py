import streamlit as st
import pandas as pd
import io
import base64
from src.preprocessing import preprocess_data
from src.inference import predict_fraud

# 🔹 App title
st.set_page_config(page_title="Financial Fraud Detector", layout="centered")
st.title("💰 Financial Fraud Detector")

# 🔹 File uploader
uploaded_file = st.file_uploader("📁 Upload a CSV file with transaction data", type="csv")

if uploaded_file:
    # 🔹 Load file
    df = pd.read_csv(uploaded_file, encoding='utf-8-sig')
    st.subheader("📊 Data Preview")
    st.write("Columns loaded:", df.columns.tolist())
    st.dataframe(df.head())

    # 🔹 Drop target column if present (only input features needed)
    if "is_fraud" in df.columns:
        df = df.drop("is_fraud", axis=1)

    # 🔹 Preprocess and Predict
    df_processed, _ = preprocess_data(df)
    y_pred, scores = predict_fraud(df_processed)
    df["Fraud Risk"] = scores

    # 🔸 Warn if high-risk fraud exists
    high_risk_df = df[df["Fraud Risk"] > 0.9]
    if not high_risk_df.empty:
        st.warning("🚨 High-risk fraud detected! (Fraud Risk > 0.9)")

    # 🔸 Risk Threshold Slider
    threshold = st.slider("📈 Show transactions with Fraud Risk above:", 0.0, 1.0, 0.7, 0.01)
    risky_df = df[df["Fraud Risk"] > threshold]
    st.subheader(f"🔴 Transactions with Fraud Risk > {threshold}")
    st.dataframe(risky_df)

    # 🔸 Filter by Location and Device
    st.subheader("🎯 Filter Fraud Risk by Location / Device")

    locations = df["location"].unique().tolist()
    devices = df["device"].unique().tolist()

    selected_location = st.selectbox("🌍 Select Location", ["All"] + locations)
    selected_device = st.selectbox("💻 Select Device", ["All"] + devices)

    filtered_df = df.copy()
    if selected_location != "All":
        filtered_df = filtered_df[filtered_df["location"] == selected_location]
    if selected_device != "All":
        filtered_df = filtered_df[filtered_df["device"] == selected_device]

    st.bar_chart(filtered_df["Fraud Risk"])

    # 🔸 Highlight high-risk rows
    def highlight_high_risk(row):
        return ['background-color: #ffcccc'] * len(row) if row["Fraud Risk"] > 0.7 else [''] * len(row)

    st.subheader("📋 Full Prediction Table")
    st.dataframe(df.style.apply(highlight_high_risk, axis=1))

    # 🔸 Excel Download
    def generate_excel_download_link(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Fraud Predictions')
        processed_data = output.getvalue()
        b64 = base64.b64encode(processed_data).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="fraud_predictions.xlsx">📥 Download Predictions as Excel</a>'
        return href

    st.markdown(generate_excel_download_link(df), unsafe_allow_html=True)

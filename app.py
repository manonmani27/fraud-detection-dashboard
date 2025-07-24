import streamlit as st
import pandas as pd
import io
import base64
import matplotlib.pyplot as plt
from src.preprocessing import preprocess_data
from src.inference import predict_fraud

# ----------------------------
# App Setup
# ----------------------------
st.set_page_config(page_title="💳 Fraud Detection Dashboard", layout="centered")
st.title("💰 Financial Fraud Detection Dashboard")

# ----------------------------
# File Upload
# ----------------------------
uploaded_file = st.file_uploader("📁 Upload a CSV file with transaction data", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    # Drop label column if present
    if "is_fraud" in df.columns:
        df = df.drop("is_fraud", axis=1)

    # ----------------------------
    # Preprocess & Predict
    # ----------------------------
    df_processed, _ = preprocess_data(df)
    y_pred, scores = predict_fraud(df_processed)
    df["Fraud Risk"] = scores

    # ----------------------------
    # Risk Alert
    # ----------------------------
    high_risk = df[df["Fraud Risk"] > 0.9]
    if not high_risk.empty:
        st.warning("🚨 High-risk fraud detected! (Fraud Risk > 0.9)")

    # ----------------------------
    # Risk Threshold Slider
    # ----------------------------
    threshold = st.slider("📈 Show transactions with Fraud Risk above:", 0.0, 1.0, 0.7, 0.01)
    filtered_df = df[df["Fraud Risk"] > threshold]
    st.subheader(f"🔍 Transactions with Risk > {threshold}")
    st.dataframe(filtered_df)

    # ----------------------------
    # Filter by Location and Device
    # ----------------------------
    st.subheader("🎛️ Filter by Location and Device")

    col1, col2 = st.columns(2)

    locations = df["location"].unique().tolist() if "location" in df.columns else []
    devices = df["device"].unique().tolist() if "device" in df.columns else []

    with col1:
        selected_location = st.selectbox("🌍 Select Location", ["All"] + locations)
    with col2:
        selected_device = st.selectbox("💻 Select Device", ["All"] + devices)

    filtered_plot_df = df.copy()
    if selected_location != "All":
        filtered_plot_df = filtered_plot_df[filtered_plot_df["location"] == selected_location]
    if selected_device != "All":
        filtered_plot_df = filtered_plot_df[filtered_plot_df["device"] == selected_device]

    # ----------------------------
    # 📊 Grouped Bar Chart (Web vs Mobile)
    # ----------------------------
    if "device" in df.columns and "location" in df.columns:
        grouped = df.groupby(["location", "device"])["Fraud Risk"].mean().unstack().fillna(0)

        st.subheader("📊 Avg Fraud Risk by Location & Device")
        fig, ax = plt.subplots(figsize=(10, 5))
        grouped.plot(kind="bar", ax=ax, color={"Web": "orange", "Mobile": "purple"})
        ax.set_title("Avg Fraud Risk: Web vs Mobile by Location")
        ax.set_ylabel("Avg Risk Score")
        ax.set_xlabel("Location")
        ax.legend(title="Device")
        st.pyplot(fig)

    # ----------------------------
    # Highlight High-Risk Rows
    # ----------------------------
    def highlight_risk(row):
        return ['background-color: #ffcccc'] * len(row) if row["Fraud Risk"] > 0.9 else [''] * len(row)

    st.subheader("📋 Full Table with Risk Scores")
    st.dataframe(df.style.apply(highlight_risk, axis=1))

    # ----------------------------
    # Excel Download
    # ----------------------------
    def download_link(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name="Fraud Predictions")
        processed_data = output.getvalue()
        b64 = base64.b64encode(processed_data).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="fraud_predictions.xlsx">📥 Download as Excel</a>'
        return href

    st.markdown("### ⬇️ Download Results")
    st.markdown(download_link(df), unsafe_allow_html=True)

else:
    st.info("👈 Upload a CSV file to begin.")

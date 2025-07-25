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
# File Upload with Fallback to Sample
# ----------------------------
uploaded_file = st.file_uploader("📁 Upload a CSV file with transaction data", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully.")
else:
    st.info("📄 No file uploaded. Using sample data from `data/sample_transactions.csv`.")
    df = pd.read_csv("data/sample_transactions.csv")

# ----------------------------
# Data Preview
# ----------------------------
st.subheader("📊 Data Preview")
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
# Predicted Risk (sorted) Table
# ----------------------------
st.subheader("🔎 Predicted Risk (sorted)")
sorted_df = df.sort_values(by="Fraud Risk", ascending=False)
st.dataframe(sorted_df[["amount", "location", "device", "time", "Fraud Risk"]])

# ----------------------------
# Fraud Risk Distribution Histogram
# ----------------------------
st.subheader("📊 Fraud Risk Distribution")
fig_hist, ax_hist = plt.subplots()
ax_hist.hist(df["Fraud Risk"], bins=10, color="orange", edgecolor="black")
ax_hist.set_title("Distribution of Fraud Risk Scores")
ax_hist.set_xlabel("Fraud Risk Score")
ax_hist.set_ylabel("Number of Transactions")
ax_hist.grid(True)
st.pyplot(fig_hist)

# ----------------------------
# Avg Fraud Risk by Location Bar Chart
# ----------------------------
if "location" in df.columns:
    st.subheader("📍 Avg. Fraud Risk by Location")
    avg_location = df.groupby("location")["Fraud Risk"].mean().sort_values()
    fig_loc, ax_loc = plt.subplots()
    avg_location.plot(kind="bar", color="blue", ax=ax_loc)
    ax_loc.set_ylabel("Avg Fraud Risk")
    ax_loc.set_xlabel("Location")
    ax_loc.grid(axis="y")
    st.pyplot(fig_loc)

# ----------------------------
# Avg Fraud Risk by Device Bar Chart
# ----------------------------
if "device" in df.columns:
    st.subheader("💻 Avg. Fraud Risk by Device")
    avg_device = df.groupby("device")["Fraud Risk"].mean().sort_values()
    fig_dev, ax_dev = plt.subplots()
    avg_device.plot(kind="bar", color="blue", ax=ax_dev)
    ax_dev.set_ylabel("Avg Fraud Risk")
    ax_dev.set_xlabel("Device")
    ax_dev.grid(axis="y")
    st.pyplot(fig_dev)

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
# CSV Download Button
# ----------------------------
csv = df.to_csv(index=False).encode('utf-8')
st.markdown("### 📥 Download Predictions")
st.download_button(
    label="Download as CSV",
    data=csv,
    file_name='fraud_predictions.csv',
    mime='text/csv',
)

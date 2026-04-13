import streamlit as st
import pandas as pd

df = pd.read_csv("processed_email.csv")

st.title("🔐 User Digital Twin - Insider Threat Detection")

# Data Preview
st.header("📊 Data Preview")
st.text(df.head().to_string())

# Suspicious Activities
st.header("🚨 Suspicious Activities")
anomalies = df[df['anomaly'] == -1]
st.text(
    anomalies[['user','hour','total_recipients','attachments','risk_score','reason']]
    .head(20)
    .to_string()
)

# Top Risky Activities
st.header("🔥 Top Risky Activities")
top = df.sort_values(by='risk_score', ascending=False).head(10)
st.text(
    top[['user','risk_score','reason']]
    .to_string()
)
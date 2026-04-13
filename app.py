import streamlit as st
import pandas as pd

df = pd.read_csv("processed_sample.csv")

st.title("🔐 User Digital Twin - Insider Threat Detection")

# Data Preview
st.header("📊 Data Preview")
st.dataframe(df.head())

# Suspicious Activities
st.header("🚨 Suspicious Activities")
anomalies = df[df['anomaly'] == -1]
st.dataframe(
    anomalies[['user','hour','total_recipients','attachments','risk_score','reason']].head(20)
)

# Top Risky Activities
st.header("🔥 Top Risky Activities")
top = df.sort_values(by='risk_score', ascending=False).head(10)
st.dataframe(top[['user','risk_score','reason']])


# app.py — Streamlit Dashboard
import streamlit as st
import pandas as pd
import subprocess
import os

st.set_page_config(layout="wide")
st.title("OmniFahad Real-Time Option Prediction")

ticker = st.text_input("Enter stock ticker", "AAPL")

if st.button("Run Real-Time Prediction"):
    with st.spinner("Running pipeline..."):
        subprocess.run(["python", "run_pipeline.py"])
        st.success("Pipeline executed.")

if os.path.exists("output/signals.csv"):
    df = pd.read_csv("output/signals.csv")
    st.subheader("Prediction Output")
    st.dataframe(df.tail(10))
    st.line_chart(df[["prediction"]].tail(100))
else:
    st.warning("No prediction data found. Run the pipeline first.")

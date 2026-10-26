import streamlit as st
import pandas as pd

st.set_page_config(page_title="Raíces", page_icon="🌱")
st.title("Raíces: Find Your Wellness Signature")
st.caption("Anonymous post-class surveys, turned into a Teaching Signature.")

uploaded = st.file_uploader("Upload a survey export (CSV)", type=["csv"])
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv("data/sample.csv")
    st.info("Showing sample data. Upload your own CSV to replace it.")

st.metric("Responses", len(df))
st.dataframe(df.head(20))

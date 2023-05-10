import pandas as pd
import streamlit as st
st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with"""
)

df = pd.read_csv("data/loan_data_shortened.csv")
st.bar_chart(data=df.head(10), x=["id"], y=["accepted"], use_container_width=True)

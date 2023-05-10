import pandas as pd
import streamlit as st

st.set_page_config(page_title="Inference", page_icon="🔎")

st.markdown("# Inference")
st.sidebar.header("Inference")

"""Please provide us data which fit: """

"""-"""

"""-"""

"""-"""


def predict(df):
    return df


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    dataframe = pd.read_csv(uploaded_file)
    # TODO:
    predictions = predict(dataframe)
    st.write(predictions.head(10))

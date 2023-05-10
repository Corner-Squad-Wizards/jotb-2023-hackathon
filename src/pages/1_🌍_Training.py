from io import StringIO

import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from urllib.error import URLError

st.set_page_config(page_title="Inference", page_icon="👟")

st.markdown("# Inference")
st.sidebar.header("Inference")

"""Please provide us data in csv format with columns: """

"""- debt_to_income"""

"""- loan_amount"""

"""- employment_length"""


"""- risk_score"""
"""- acepted (target variable)"""

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    dataframe = pd.read_csv(uploaded_file)

    """ ## Data Exploratory 🔎"""
    st.write(dataframe.head())
    """ ## Correlation matrix"""
    fig, ax = plt.subplots()
    sns.heatmap(dataframe.corr(), ax=ax)
    st.write(fig)

    if st.button("Train model"):
        # TODO: add train function
        st.write('Model successfully trained')

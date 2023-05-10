from io import StringIO

import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from db.utils import load_table
from processing.utils import create_model
from urllib.error import URLError

from src.processing.utils import get_validation_metrics

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
    # sns.heatmap(dataframe.corr(), ax=ax)
    # st.write(fig)

    if st.button("Train model"):
        # Add table to DB
        load_table(dataframe, "training_new_data")
        # Create and train new model
        model_name = create_model("LiveTraining", "accepted", "training_new_data")

        st.write('Model successfully trained')

    st.markdown("# Validations")
    st.sidebar.header("Validations")

    st.write("""Here you can find Precision, Recall, F-1 """)

    if st.button('Do validations'):
        # TODO: insert function for validations
        # validate_model("val_test")
        df = get_validation_metrics("val")
        print(df)
        di = df[["METRIC_NAME", "METRIC_VALUE"]].set_index("METRIC_NAME").to_dict()
        print(di)
        col1, col2, col3 = st.columns(3)
        col1.metric("Precision", float(di["METRIC_VALUE"]["Precision"]))
        col2.metric("Recall", float(di["METRIC_VALUE"]["Recall"]))
        col3.metric("F-1", float(di["METRIC_VALUE"]["F-Measure"]))

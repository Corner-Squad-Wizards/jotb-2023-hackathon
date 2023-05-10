import pandas as pd
from processing.utils import model_predict
import streamlit as st
import matplotlib.pyplot as plt

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
    if st.button("Predict"):
        # TODO: upload  validation set
        # predictions = predict(dataframe)
        predictions = model_predict("test1", "hk.loan_data_some")
        total = len(predictions)
        labels = "Accepted", "Rejected"

        st.markdown("# Predictions")
        head = predictions.sort_values(
            "probability_accepted", inplace=False, ascending=False
        ).head(10)
        st.write(head)

        st.markdown("# Real likelihood of being accepted")
        accepted_count = (predictions["accepted"] == 1).sum()
        sizes = [accepted_count, total - accepted_count]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        ax1.axis("equal")
        st.pyplot(fig1)

        st.markdown("# Predicted likelihood of being accepted")
        prediction_count = (predictions["prediction"] == "1").sum()
        p = predictions["prediction"]
        p.describe()
        sizes2 = [prediction_count, total - prediction_count]
        fig2, ax2 = plt.subplots()
        ax2.pie(sizes2, labels=labels, autopct="%1.1f%%", startangle=90)
        ax2.axis("equal")
        st.pyplot(fig2)

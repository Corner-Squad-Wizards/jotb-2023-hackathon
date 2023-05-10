import pandas as pd
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
        predictions = predict(dataframe)
        st.markdown("# Ordered predictions")
        st.write(predictions.head(10))
        st.markdown("# How many loan we sell?")
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        sizes = [15, 30, 45, 10]
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        st.pyplot(fig1)
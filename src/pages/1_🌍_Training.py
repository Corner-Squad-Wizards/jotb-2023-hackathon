from io import StringIO

import streamlit as st
import pandas as pd
from urllib.error import URLError

st.set_page_config(page_title="Inference", page_icon="👟")

st.markdown("# Inference")
st.sidebar.header("Inference")

"""Please provide us data which fit: """

"""-"""

"""-"""

"""-"""


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe.head())

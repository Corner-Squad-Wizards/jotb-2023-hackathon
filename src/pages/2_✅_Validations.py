from processing.utils import get_validation_metrics, validate_model
import streamlit as st
import pandas as pd
from io import StringIO

import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
from db.utils import load_table
from processing.utils import create_model, train_model, get_validation_metrics
from urllib.error import URLError

st.set_page_config(page_title="Validations", page_icon="✅")

st.markdown("# Validations")
st.sidebar.header("Validations")


def get_validations():
    return 0.9, 0.9, 0.9


st.write("""Here you can find Precision, Recall, F-1 """)


uploaded_file = st.file_uploader("Choose a file to validate the last model")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    # Add table to DB
    load_table(df,"validation_new_data")
    # Validate latest model on new data
    validate_model()
    # Get validation metrics
    metrics = get_validation_metrics()
    print("hola3")
    di = metrics[["METRIC_NAME", "METRIC_VALUE"]].set_index("METRIC_NAME").to_dict()
    print(di)
    col1, col2, col3 = st.columns(3)
    col1.metric("Precision", float(di["METRIC_VALUE"]["Precision"]))
    col2.metric("Recall", float(di["METRIC_VALUE"]["Recall"]))
    col3.metric("F-1", float(di["METRIC_VALUE"]["F-Measure"]))

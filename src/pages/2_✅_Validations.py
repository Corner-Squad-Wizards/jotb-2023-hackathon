from processing.utils import get_validation_metrics, validate_model
import streamlit as st

st.set_page_config(page_title="Validations", page_icon="✅")

st.markdown("# Validations")
st.sidebar.header("Validations")


def get_validations():
    return 0.9, 0.9, 0.9


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

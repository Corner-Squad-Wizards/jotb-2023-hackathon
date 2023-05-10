import streamlit as st
import pandas as pd
st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data.
""")


df = pd.read_csv("data/loan_data_shortened.csv")
st.bar_chart(data=df.head(20),x=["id"], y=["accepted"], use_container_width=True)
import streamlit as st

st.set_page_config(page_title="Validations", page_icon="✅")

st.markdown("# Validations")
st.sidebar.header("Validations")


def get_validations():
    return 0.9, 0.9, 0.9


st.write("""Here you can find Precision, Recall, F-1 """)

if st.button('Do validations'):
    # TODO: insert function for validations
    a, b, c = get_validations()
    col1, col2, col3 = st.columns(3)
    col1.metric("Precision", a)
    col2.metric("Recall", b)
    col3.metric("F-1", c)

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Envio e tratamento de arquivos",
    page_icon="📁",
    layout="wide")

col1, col2 = st.columns([11, 1])

col1.title("Envio e tratamento de arquivos")
col2.image("./assets/images/logo.png")

st.divider()

st.subheader("Enviar arquivo")
file = st.file_uploader("Escolha seu arquivo", type="xlsx")

if file:      
    df = pd.read_excel(file) 
    st.dataframe(df)



import streamlit as st

st.set_page_config(
    page_title="Envio e tratamento de arquivos",
    page_icon="📁",
    layout="wide")

col1, col2 = st.columns([11, 1])

col1.title("Envio e tratamento de arquivos")
col2.image("./assets/images/logo.png")

st.divider()

menu_lateral = st.sidebar

with menu_lateral:
    selected = st.selectbox("Escolha uma opção", ["Enviar arquivo", "Visualizar arquivo enviado"])

if selected:
    if selected == "Enviar arquivo":
        st.subheader("Enviar arquivo")
        st.file_uploader("Escolha seu arquivo", type="xlsx")

    if selected == "Visualizar arquivo enviado":
        st.subheader("Visualizar arquivo enviado")

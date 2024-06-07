import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Envio e tratamento de arquivos",
    page_icon="📁",
    layout="wide")

df = ""
file = ""

def receberArquivo(arq):
    global file
    file = arq

def criarDataFrame(arq):
    global df
    df = pd.read_excel(arq)

def getDataFrame():
    global df
    return df

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
        receberArquivo(st.file_uploader("Escolha seu arquivo", type="xlsx"))
       

    if selected == "Visualizar arquivo enviado":
        st.subheader("Visualizar arquivo enviado")
        if file:
            st.success('teste')
        else:
            st.error('teste')



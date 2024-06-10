import streamlit as st
import pandas as pd
import os


st.set_page_config(
    page_title="Envio e tratamento de arquivos",
    page_icon="📁",
    layout="wide")

col1, col2 = st.columns([11, 1])

with st.sidebar:
    selected = st.selectbox("Menu", ["Enviar arquivo", "Visualizar arquivo"])

col1.title("Envio e tratamento de arquivos")
col2.image("./assets/images/logo.png")

st.divider()

if selected == "Enviar arquivo":
    st.subheader("Enviar arquivo")
    file = st.file_uploader("Escolha seu arquivo", type="xlsx")
    if file:
        df = pd.read_excel(file)
        df.to_csv("./data/dados.csv", index=False)

if selected == "Visualizar arquivo":
    if os.path.exists("./data/dados.csv"):
        df = pd.read_csv("./data/dados.csv") 

        col1, col2 = st.columns(2)

        df_quantidade_de_vendas_por_vendedor = df.groupby("Cod_vendedor").size()
        df_group_vendedores = df.groupby("Cod_vendedor").sum()[["Quantidade", "Valor"]]
        df_group_vendedores["Qtd Vendas"] = df_quantidade_de_vendas_por_vendedor

        df_group_produtos = df.groupby("Cod_produto").sum()[["Quantidade", "Valor"]]

        col1.dataframe(df_group_vendedores)
        col2.dataframe(df_group_produtos)


        st.dataframe(df, use_container_width=True)



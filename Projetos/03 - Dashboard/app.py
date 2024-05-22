import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("Dashboard")

container = st.container(border=True)


with container:
    df = pd.read_excel("./data/vendas.xlsx")
    # st.dataframe(df)
    acumulado_vendas_por_cidade = df[['City', 'Total']].groupby('City').sum()
    media_vendas_por_cidade = df[[  'City', 'Total']].groupby('City').mean()
    
    quantidade_de_vendas = df.shape[0]

    st.write(df)

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Quantidade de vendas", value=quantidade_de_vendas)

    st.write(quantidade_de_vendas)

    col1, col2 = st.columns(2)
    with col1:
        st.scatter_chart(acumulado_vendas_por_cidade)


    with col2:
        st.area_chart(media_vendas_por_cidade)


    preco_por_tipo_de_pagamento = df[['Payment', 'Total']].groupby('Payment').sum()
    st.bar_chart(preco_por_tipo_de_pagamento)

    quantidade_vendidas_por_genero_e_tipo = df[['Gender', 'Customer type', 'Quantity']].groupby(['Gender', 'Customer type']).sum()
    st.write(quantidade_vendidas_por_genero_e_tipo)
    # st.bar_chart(quantidade_vendidas_por_genero_e_tipo, x='Customer type', y='Quantity')
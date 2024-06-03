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
    acumulado_vendas_por_cidade = df[['City', 'Total']].groupby('City').sum()
    media_vendas_por_cidade = df[[  'City', 'Total']].groupby('City').mean()
    
    quantidade_de_vendas = df.shape[0]
    media_de_vendas = round(df['Total'].mean(), 2)
    quantidade_vendida = df['Quantity'].sum()

    # st.write(df.describe())

    col1, col2, col3 = st.columns(3)

    with col1:
        content = st.container(border=True)
        with content:
            st.metric(label="Quantidade de vendas", value=quantidade_de_vendas)

    with col2:
        content = st.container(border=True)
        with content:
            st.metric(label="Média de vendas", value="R$ " + str(media_de_vendas))
    
    with col3:
        content = st.container(border=True)
        with content:
            st.metric(label="Quantidade vendida", value=quantidade_vendida)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Acumulado de vendas por Cidade")
        st.scatter_chart(acumulado_vendas_por_cidade)


    with col2:
        st.subheader("Média de vendas por Cidade")
        st.area_chart(media_vendas_por_cidade)


    preco_por_tipo_de_pagamento = df[['Payment', 'Total']].groupby('Payment').sum()
    st.subheader("Vendas por tipo de pagamento")
    st.bar_chart(preco_por_tipo_de_pagamento)

    quantidade_vendidas_por_genero_e_tipo = df[['Gender', 'Customer type', 'Quantity']].groupby(['Gender', 'Customer type']).sum()

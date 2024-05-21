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
    media_vendas_por_cidade = df[['City', 'Total']].groupby('City').mean()

    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots()
        ax.bar(acumulado_vendas_por_cidade.index, acumulado_vendas_por_cidade['Total'])
        ax.set_title('Acumulado de vendas por Cidade')
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        ax.bar(media_vendas_por_cidade.index, acumulado_vendas_por_cidade['Total'])
        ax.set_title('Média de vendas por Cidade')
        st.pyplot(fig)
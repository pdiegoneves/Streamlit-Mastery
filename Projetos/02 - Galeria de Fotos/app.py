import streamlit as st
import os
import pandas as pd

st.set_page_config(
    page_title="Galeria de imagens",
    page_icon="📸",
    layout="wide"
)

st.title("Galeria de imagens")

if os.path.exists('./data/imagens.csv'):
    df = pd.read_csv('./data/imagens.csv')


# for j in range(len(df)):
#     st.image(os.path.join("img", df["Nome do arquivo"][j]))
#     st.caption(df['Nome da imagem'][j])


for i in range(round(len(df) / 3)):
    col1, col2, col3 = st.columns(3)
    count = 1
    for j in range(len(df)):
        if count == 1:
            with col1:
                with st.container(border=True):
                    st.image(os.path.join("img", df["Nome do arquivo"][j]))
                    st.caption(df['Nome da imagem'][j])
                    count += 1
                    continue
        if count == 2:
            with col2:
                with st.container(border=True):
                    st.image(os.path.join("img", df["Nome do arquivo"][j]))
                    st.caption(df['Nome da imagem'][j])
                    count += 1
                    continue
        if count == 3:
            with col3:
                with st.container(border=True):
                    st.image(os.path.join("img", df["Nome do arquivo"][j]))
                    st.caption(df['Nome da imagem'][j])
                    count = 1
                    continue



import streamlit as st
import os

st.set_page_config(
    page_title="Galeria de imagens",
    page_icon="📸",
    layout="wide"
)

st.title("Galeria de imagens")

lista_de_imagens = os.listdir("img")

for i in range(round(len(lista_de_imagens) / 3)):
    col1, col2, col3 = st.columns(3)
    count = 1
    for imagem in lista_de_imagens:
        if imagem:
            if count == 1:
                col1.image(os.path.join("img", lista_de_imagens[i]))
                count += 1
                continue
            if count == 2:
                col2.image(os.path.join("img", lista_de_imagens[i + 1]))
                count += 1
                continue
            if count == 3:
                col3.image(os.path.join("img", lista_de_imagens[i + 2]))
                count = 1
                continue
                

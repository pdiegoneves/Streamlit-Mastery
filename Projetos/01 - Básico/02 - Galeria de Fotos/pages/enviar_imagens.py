import streamlit as st
from src.gravar_imagem import gravar_imagem
import pandas as pd
import os


st.title("Envie suas imagens aqui")


with st.form("Enviar Imagens", clear_on_submit=True):
    nome_do_arquivo = st.text_input("Nome da imagem")
    imagem = st.file_uploader("Escolha ou arraste uma imagem", type=["png", "jpg", "jpeg"])
    enviar = st.form_submit_button("Enviar")


if enviar:
    df_imagem = pd.DataFrame(
        [
            {
                'Nome da imagem' : nome_do_arquivo,
                'Nome do arquivo' : f'{imagem.file_id}-{imagem.name}'
            }
        ]
    )
    
    try:
        df = pd.read_csv(os.path.join('data', 'imagens.csv'))
        df = pd.concat([df, df_imagem], ignore_index=True)
        df.to_csv(os.path.join('data', 'imagens.csv'), index=False)
        if imagem:
            gravar_imagem(imagem)
    except FileNotFoundError:
        df_imagem.to_csv(os.path.join('data', 'imagens.csv'), index=False)
        if imagem:
            gravar_imagem(imagem)
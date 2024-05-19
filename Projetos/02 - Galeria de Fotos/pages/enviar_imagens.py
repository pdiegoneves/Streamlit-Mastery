import streamlit as st
from src.gravar_imagem import gravar_imagem

st.title("Envie suas imagens aqui")

imagem = st.file_uploader("Escolha ou arraste uma imagem", type=["png", "jpg", "jpeg"])

if imagem:
    st.image(imagem)
    st.text(imagem.file_id)
    gravar_imagem(imagem)


# UploadedFile(file_id='f5ac55e1-1f95-4b1a-954f-e2f5de6ea59b', name='logo.png', type='image/png', size=3944, _file_urls=file_id: "f5ac55e1-1f95-4b1a-954f-e2f5de6ea59b"
# upload_url: "/_stcore/upload_file/55e630bd-067d-434d-919a-08cf221fff66/f5ac55e1-1f95-4b1a-954f-e2f5de6ea59b"
# delete_url: "/_stcore/upload_file/55e630bd-067d-434d-919a-08cf221fff66/f5ac55e1-1f95-4b1a-954f-e2f5de6ea59b")

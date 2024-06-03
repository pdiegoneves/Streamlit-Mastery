import os

pasta_de_imagens = 'img'

def gravar_imagem(imagem):
    if not os.path.exists(pasta_de_imagens):
        os.makedirs(pasta_de_imagens)

    if imagem:
        nome_do_arquivo = f'{imagem.file_id}-{imagem.name}'
        caminho_do_arquivo = os.path.join(pasta_de_imagens, nome_do_arquivo)

        with open(caminho_do_arquivo, 'wb') as f:
            f.write(imagem.getbuffer())
import streamlit as st

st.set_page_config(
    page_title="FAQ - Streamlit",
    page_icon="./img/logo.png",
    layout="wide",
)

col1, col2 = st.columns([2, 10])

col1.image("./img/logo.png")
with col2:
    st.title("FAQ - Streamlit")
    st.caption("Frequently Asked Questions")

st.header("Perguntas frequentes sobre o Streamlit")

with st.expander("O que é Streamlit?"):
    st.write('Streamlit é uma biblioteca de código aberto em Python que facilita a criação de aplicativos da web interativos para visualização de dados. Com Streamlit, você pode transformar scripts Python em aplicativos da web interativos, sem necessidade de conhecimento em desenvolvimento web.')


with st.expander("Como testar o streamlit?"):
    st.text('No terminal digite')
    st.code('streamlit hello')

with st.expander("Como rodar o streamlit?"):
    st.text('No terminal digite')
    st.code('streamlit run main.py')
    st.caption('Onde main.py é o arquivo principal do Streamlit')	

with st.expander("Posso rodar o streamlit em outra porta?"):
    st.success('Sim, basta passar a porta que deseja')
    st.text('No terminal digite')
    st.code('streamlit run main.py --server.port 8080')
    st.caption('Onde main.py é o arquivo principal do Streamlit e 8080 é a porta')	

with st.expander("Como adicionar gráficos em um aplicativo Streamlit?"):
    st.markdown('Você pode adicionar gráficos em um aplicativo Streamlit utilizando bibliotecas de visualização de dados como **Matplotlib, Seaborn e Plotly**.') 
    st.markdown('Por exemplo, para exibir um gráfico Matplotlib, você pode usar st.pyplot(fig).')
    st.markdown('> onde fig é a figura gerada pelo Matplotlib.')

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):    
        st.markdown("###### Curso")
        st.text("Streamlit Mastery")

with col2:
    with st.container(border=True):
        st.markdown("###### Autor")
        st.text("Diego Neves")

with col3:
    with st.container(border=True):
        st.markdown("###### Co-Autor")
        st.caption("Chat GPT 3.5")
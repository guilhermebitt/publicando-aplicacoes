import streamlit as st
import requests

st.title('LEITOR DE CEP')
st.markdown('Feito no Senac')

cep = st.text_input('Digite o CEP:')
url = f'https://viacep.com.br/ws/{cep}/json/'
try:
  response = requests.get(url)
  dados = response.json()
  st.write(
    dados['localidade'],
    ' - ',
    dados['logradouro'],
    ' - ',
    dados['bairro'],
    ' / ',
    dados['uf']
           )
except:
  st.error('CEP incorreto ou inexistente!')

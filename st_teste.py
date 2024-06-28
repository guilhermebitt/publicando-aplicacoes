import streamlit as st
import request

cep = st.text_input('Digite o CEP:')
url = f'https://viacep.com.br/ws/{cep}/json/'
try:
  response = request.get(url)
  dados = response.json()
except:
  st.error('CEP incorreto ou inexistente')

st.title('SENAC')
st.markdown('Feito no Senac')

texto = st.text_input(
  label = 'Digite algo:',
  placeholder = 'aqui mesmo'
)
st.write(texto)

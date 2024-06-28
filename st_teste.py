import streamlit as st

st.title('SENAC')
st.markdown('Feito no Senac')

texto = st.text_input(
  label = 'Digite algo:'
  placeholder = 'aqui mesmo'
)
st.write(texto)

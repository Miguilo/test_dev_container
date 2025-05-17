import streamlit as st
import requests

st.title('Interface Streamlit')

# Função para buscar dados da API
def fetch_data():
    try:
        response = requests.get('http://backend:8000/')
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def fetch_item(item_id):
    try:
        response = requests.get(f'http://backend:8000/items/{item_id}')
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# Exibir mensagem do backend
data = fetch_data()
st.write("Mensagem do backend:", data.get("message", "Erro ao conectar"))

# Interface para buscar itens
st.subheader("Buscar Item")
item_id = st.number_input("Digite o ID do item", min_value=1, value=1)

if st.button("Buscar"):
    item_data = fetch_item(item_id)
    if "error" not in item_data:
        st.success(f"Item encontrado: {item_data['nome']}")
        st.success("Testando docker")
    else:
        st.error("Erro ao buscar item") 
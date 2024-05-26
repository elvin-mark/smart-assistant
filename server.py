import streamlit as st
import requests

def get_response(prompt:str) -> str:
    res = requests.post("http://localhost:8181/completion",json={"prompt":f"Question: {prompt}\nAnswer: ","n_predict": 128})
    return res.json()["content"]

st.title("Chat with the Smart Assistant!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    response = get_response(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
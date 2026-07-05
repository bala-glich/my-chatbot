import streamlit as st
import requests

st.set_page_config(page_title="My Local AI Chatbot", page_icon="🤖")
st.title("My Local AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I am your local chatbot powered by Llama 3."}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def ask_ollama(user_text):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": user_text,
            "stream": False
        },
        timeout=120
    )
    response.raise_for_status()
    return response.json()["response"]

prompt = st.chat_input("Type your message here")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            reply = ask_ollama(prompt)
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

import streamlit as st
from ollama import chat

st.set_page_config(page_title="My ChatGPT-like App", page_icon="🤖")
st.title("My ChatGPT-like App")

SYSTEM_PROMPT = "You are a helpful, friendly assistant. Answer clearly and concisely."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Hi! I’m ready to chat."}
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

prompt = st.chat_input("Type your message here")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat(
                model="llama3",
                messages=st.session_state.messages,
            )
            reply = response.message.content
            st.write(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

import streamlit as st

st.title("My First App")

name = st.text_input("Enter your name")
if st.button("Say hello"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Hello!")

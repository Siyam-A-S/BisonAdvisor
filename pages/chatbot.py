import streamlit as st
st.title("Chatbot")



prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")


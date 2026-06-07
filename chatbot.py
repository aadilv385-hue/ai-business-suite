import streamlit as st

st.title("AI Chatbot")

question = st.text_input("Ask a Question")

if question:
    if "hello" in question.lower():
        st.write("Hello! How can I help you?")
    else:
        st.write("I am a simple support chatbot.")
import streamlit as st

st.title("Spam Detector")

message = st.text_area("Enter Message")

spam_words = ["win", "free", "prize", "lottery"]

if st.button("Check"):
    if any(word in message.lower() for word in spam_words):
        st.error("Spam Message")
    else:
        st.success("Ham Message")
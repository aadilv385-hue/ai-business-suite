import streamlit as st

st.title("Caption Generator")

product = st.text_input("Product Name")

if st.button("Generate Caption"):
    st.success(
        f"🔥 Introducing {product}! Premium quality at the best price. #Sale #Trending"
    )
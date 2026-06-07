import streamlit as st

st.title("Invoice Generator")

customer = st.text_input("Customer Name")
product = st.text_input("Product")
amount = st.number_input("Amount")

if st.button("Generate Invoice"):
    st.write(f"""
Customer: {customer}

Product: {product}

Amount: ₹{amount}
""")
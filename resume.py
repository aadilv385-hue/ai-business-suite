import streamlit as st

st.title("Resume Builder")

name = st.text_input("Name")
skills = st.text_area("Skills")
education = st.text_input("Education")

if st.button("Generate Resume"):
    st.write(f"""
# {name}

## Skills
{skills}

## Education
{education}
""")
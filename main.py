import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Aman Jain")
    content = """
    Hi, I am Aman!. Currently pursuing Master's in Data Science at ASU, with aspirations for an internship in Data Science, ML, or Computer Vision for summer 2025.
    Possess two years of experience as a Software Engineer, specializing in performance and load testing.
    Eager to advance expertise
    """
    st.write(content)
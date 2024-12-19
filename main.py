import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=450)
with col2:
    st.title("Aman Jain")
    content = """
    Hi, I am Aman!. Currently pursuing Master's in Data Science at ASU, with aspirations for an internship in Data Science, ML, or Computer Vision for summer 2025.
    Possess two years of experience as a Software Engineer, specializing in performance and load testing.
    Eager to advance expertise
    """
    st.write(content)

content2 = """
    Below you can find the details of my contact 
"""

st.write(content2)

df = pd.read_csv("data.csv", sep=";")
col3,emptycol, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" +row["image"])
        st.write(f"[source code]{row['url']}")

with col4:
    for index,row in df[10:20].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" +row["image"])
        st.write(f"[source code]{row['url']}")

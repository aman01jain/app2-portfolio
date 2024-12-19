import streamlit as st
from send_email import email_send

st.header("Contact Me")

with st.form(key="Form"):
    user_email = st.text_input("Enter Email Address")
    user_text = st.text_area("Message")
    message = f"""\
Subject : New email from {user_email}

From : {user_email}
{user_text}
"""
    submit = st.form_submit_button()
    if submit:
        email_send(message)
        st.info("Email sent successfully")
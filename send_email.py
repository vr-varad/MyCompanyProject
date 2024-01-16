import smtplib,ssl

import streamlit as st

host = 'smtp.gmail.com'
port = 465


def sendEmail(message):
    username = st.secrets['email']
    recieverEmail = st.secrets['email']
    password = st.secrets['password']
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,recieverEmail,message)


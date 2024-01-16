import streamlit as st
from send_email import sendEmail

st.title('Contact Us')

with st.form(key='email_form'):
    senderEmail = st.text_input('Your Email Address: ')
    senderTopic = st.selectbox('What Topic You want to discuss?', ('Job Equiries', 'Project Proposal', 'Others'))
    senderMessage = st.text_area('Your Message: ')
    message = f"""\ Subject: New mail - {senderEmail}
    
    From: {senderEmail}
    Hello,

    I am reaching out to discuss the following topic: {senderTopic}

    Message:
    {senderMessage}

    Best regards,
    Your Name
    """
    button = st.form_submit_button()
    if button:
        sendEmail(message)
        st.info('The email has been sent successfully!!!')

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('My Company')
st.write(
    """
    Welcome to our world of excellence! At Xmos, we redefine industry standards with unparalleled expertise and innovation. Our commitment to delivering exceptional quality, unmatched service, and cutting-edge solutions sets us apart. Join countless satisfied clients who have experienced the pinnacle of excellence. Choose Xmos – where greatness begins!
    """
)
st.subheader('My Team')

file = pd.read_csv('data.csv',sep=',')

col1,col2,col3 = st.columns(3)

with col1:
    for i,r in file.iterrows():
        if i%3==0:
            st.subheader(r['first name'].capitalize()+' '+r['last name'].capitalize())
            st.write(r['role'])
            st.image(f'images/{r['image']}')

with col2:
    for i,r in file.iterrows():
        if i%3==1:
            st.subheader(r['first name'].capitalize()+' '+r['last name'].capitalize())
            st.write(r['role'])
            st.image(f'images/{r['image']}')

with col3:
    for i,r in file.iterrows():
        if i%3==2:
            st.subheader(r['first name'].capitalize()+' '+r['last name'].capitalize())
            st.write(r['role'])
            st.image(f'images/{r['image']}')
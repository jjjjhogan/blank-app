import streamlit as st

num = 0

button = st.button('Press me')
if button:
    num+=1
st.write(num)
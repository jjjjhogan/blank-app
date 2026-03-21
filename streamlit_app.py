import streamlit as st

num = 0
if 'num' not in st.session_state:
    st.session_state['num']=0

button = st.button('Press me')
if button:
    num+=1
st.write(num)
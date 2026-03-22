import streamlit as st

if 'num' not in st.session_state:
    st.session_state['num']=0

button = st.button('Press me')
if button:
    st.session_state['num']+=1
st.write(st.session_state['num'])
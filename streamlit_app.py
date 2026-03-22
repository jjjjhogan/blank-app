import streamlit as st
from st_chat_message import message

message("Hi Spongebob", is_user=True)
message("Hey there, I'm Spongebob Squarepants! How can I help you today?")

if 'num' not in st.session_state:
    st.session_state['num']=0

button = st.button('Press me')
if button:
    st.session_state['num']+=1
st.write(st.session_state['num'])
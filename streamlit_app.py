import streamlit as st

"""
# Hello what is your name!
"""

name = st.text_input("Put your name")

if 'name' not in st.session_state:
    st.session_state['name'] = name

if st.session_state['name'] != '':
    st.write(f'welcome {st.session_state['name']}')

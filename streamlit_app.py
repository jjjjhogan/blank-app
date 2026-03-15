import streamlit as st

"""
# Hello what is your name!
"""
with st.form('my-form'):

    name = st.text_input("Put your name")


    button = st.form_submit_button('input name')

    if button:

        if 'name' not in st.session_state:
            st.session_state['name'] = name
        st.write(f'welcome {st.session_state["name"]}')

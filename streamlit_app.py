import streamlit as st

"""
#Hello what is your name!
"""

name = st.text_input("Put your name")

if 'name' not in st.session_state:
    st.session['name'] = name

 
if name:
    f"""
    Welcome {name}
    """

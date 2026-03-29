import streamlit as st

name = ""
dif = ""
with st.form('name'):
    name = st.text_input('Input name')
    sub = st.form_submit_button('Submit name')
    if sub:
        st.write('sub')

with st.form('diff'):
    dif = st.text_input('Input name')
    sub = st.form_submit_button('Submit name')

    if sub:
        st.write('sub')

st.write('name: ' + name)

st.write('dif: ' + dif)